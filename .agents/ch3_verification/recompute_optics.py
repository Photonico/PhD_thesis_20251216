"""Read archived VASP h5 data; compare archived and corrected postprocessing only."""
from pathlib import Path
import hashlib
import json
import sys
import h5py
import numpy as np

ROOT = Path(__file__).resolve().parent
REF = 'f863ab02ebf93d5804f5552967ea750571778335'
H_EV_S = 4.135667662e-15  # Same ordinary Planck constant as the archived module.
C_NM_S = 2.99792458e17
WINDOWS = {'IR': (0.0, 1.65), 'visible': (1.65, 3.10), 'near_UV': (3.10, 4.13), 'deep_UV': (4.13, 12.0)}

def geometry(path):
    lines = path.read_text().splitlines()
    scale = float(lines[1]); cell = np.array([[float(x) for x in s.split()[:3]] for s in lines[2:5]]) * scale
    n = sum(int(x) for x in lines[6].split())
    start = 7
    if lines[start].lower().startswith('s'): start += 1
    assert lines[start].lower().startswith('d')
    xyz = np.array([[float(x) for x in s.split()[:3]] for s in lines[start+1:start+1+n]])
    span = float(np.ptp(xyz[:, 2]))
    return {'c_A': float(np.linalg.norm(cell[2])), 'fractional_z': xyz[:,2].tolist(), 'fractional_span': span,
            'geometric_span_A': span*float(np.linalg.norm(cell[2])),
            'effective_thickness_A': span*float(np.linalg.norm(cell[2]))+2*1.98}

def arrays(energy, dielectric, thickness, angular_frequency):
    eps = 1 + (40.0 / thickness) * (dielectric - 1)
    n = np.sqrt(np.maximum((np.abs(eps) + eps.real) / 2, 0))
    k = np.sqrt(np.maximum((np.abs(eps) - eps.real) / 2, 0))
    frequency = energy/H_EV_S * (2*np.pi if angular_frequency else 1)
    absorption = 2*frequency*k/C_NM_S
    reflectivity = ((n-1)**2+k*k)/((n+1)**2+k*k)
    loss = eps.imag/(eps.real**2+eps.imag**2)
    return {'eps1': eps.real, 'eps2': eps.imag, 'n': n, 'k': k,
            'absorption_nm^-1': absorption, 'R': reflectivity, 'L': loss}

def peak(energy, y, mask):
    ids=np.flatnonzero(mask)
    if not len(ids): return None
    i=int(ids[np.argmax(y[ids])])
    return {'energy_eV': float(energy[i]), 'value': float(y[i]), 'at_window_boundary': bool(i in (ids[0], ids[-1]))}

def intervals(energy, mask):
    ids=np.flatnonzero(mask)
    if not len(ids):return []
    groups=np.split(ids,np.flatnonzero(np.diff(ids)>1)+1)
    return [[float(energy[g[0]]),float(energy[g[-1]])] for g in groups]

def summarize(energy,y):
    use=(energy>=0)&(energy<=12)
    local=np.flatnonzero((y[1:-1]>=y[:-2])&(y[1:-1]>y[2:]))+1
    local=[int(i) for i in local if use[i]]
    kept=[]
    for i in sorted(local,key=lambda i:y[i],reverse=True):
        if all(abs(energy[i]-energy[j])>.15 for j in kept):kept.append(i)
        if len(kept)==6:break
    return {'global_max':peak(energy,y,use), 'global_min':peak(energy,-y,use)|{'value':float(np.min(y[use]))},
            'top_local_maxima':[{'energy_eV':float(energy[i]),'value':float(y[i])} for i in kept],
            'window_maxima':{name:peak(energy,y,(energy>=lo)&(energy<hi if hi<12 else energy<=hi)) for name,(lo,hi) in WINDOWS.items()}}

result={'source_commit':REF,'python':sys.executable,'h5py':h5py.__version__,'numpy':np.__version__,
        'scope':'Postprocessing of the same archived dielectric density-density h5 arrays; no DFT rerun. Corrected beta thickness follows notebook intended geometry formula; retained common 40/d dielectric rescaling for both components.',
        'spectral_window_eV':[0,12], 'descriptive_window_boundaries_eV':WINDOWS,
        'corrections':{'beta_thickness':'fractional_z_span * 40 A + 2*1.98 A','absorption':'ordinary frequency E/h replaced by angular frequency 2*pi*E/h; output remains nm^-1'},'phases':{}}
cache={}
for phase in ('a','b'):
    folder=ROOT/'6.0_dielectric_selection'/f'{phase}-Beryllene'
    geo=geometry(folder/'CONTCAR'); pos=geometry(folder/'POSCAR')
    raw=(folder/'vaspout.h5').read_bytes()
    with h5py.File(folder/'vaspout.h5','r') as f:
        energy=f['results/linear_response/energies_dielectric_function'][()]
        tensor=f['results/linear_response/density_density_dielectric_function'][()]
    old_thickness=3.96 if phase=='a' else 0.0473771641975619+3.96
    new_thickness=geo['effective_thickness_A']
    info={'CONTCAR':geo,'POSCAR':pos,'h5_sha256':hashlib.sha256(raw).hexdigest(),
          'old_thickness_A':old_thickness,'corrected_thickness_A':new_thickness,
          'ratio_corrected_to_old_eps_minus_one':old_thickness/new_thickness,
          'energy_step_eV':float(energy[1]-energy[0]),'channels':{}}
    for channel,index in [('in_plane',0),('out_of_plane',2)]:
        eps_sc=tensor[index,index,:,0]+1j*tensor[index,index,:,1]
        entries={}
        for mode,d,angular in [('archived',old_thickness,False),('corrected',new_thickness,True)]:
            computed=arrays(energy,eps_sc,d,angular)
            entries[mode]={name:summarize(energy,y) for name,y in computed.items()}
            entries[mode]['loss_above_plot_limit_2_1_eV_intervals']=intervals(energy,(energy<=12)&(computed['L']>2.1))
            entries[mode]['eps1_negative_eV_intervals']=intervals(energy,(energy<=12)&(computed['eps1']<0))
            cache[(phase,channel,mode)]=(energy,computed)
        info['channels'][channel]=entries
    result['phases'][phase]=info

result['phase_comparisons']={}
for channel in ('in_plane','out_of_plane'):
    for mode in ('archived','corrected'):
        grid=np.linspace(0,12,12001)
        ea,qa=cache[('a',channel,mode)];eb,qb=cache[('b',channel,mode)]
        comparisons={}
        for name in ('absorption_nm^-1','n','k','R','L'):
            ya=np.interp(grid,ea,qa[name]);yb=np.interp(grid,eb,qb[name])
            comparisons[name]={'beta_over_alpha_integral_0_12':float(np.trapezoid(yb,grid)/np.trapezoid(ya,grid)),
                              'fraction_of_grid_beta_above_alpha':float(np.mean(yb>ya))}
        result['phase_comparisons'][channel+'_'+mode]=comparisons
out=ROOT/'optical-postprocessing-audit.json'
out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
print(out)
for phase,info in result['phases'].items():
    print('PHASE',phase,'geometry',info['CONTCAR'],'thickness',info['old_thickness_A'],'->',info['corrected_thickness_A'])
    for channel,entries in info['channels'].items():
        print('CHANNEL',channel)
        for mode,data in entries.items():
            print(mode,'GLOBAL MAX', {k:(round(v['global_max']['energy_eV'],5),round(v['global_max']['value'],6)) for k,v in data.items() if isinstance(v,dict) and 'global_max' in v})
            print(mode,'LOSS LOCAL MAX',data['L']['top_local_maxima'])
            print(mode,'LOSS WINDOWS',data['L']['window_maxima'])
            print(mode,'LOSS CLIPPED',data['loss_above_plot_limit_2_1_eV_intervals'])
