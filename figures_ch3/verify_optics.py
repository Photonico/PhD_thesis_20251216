"""Calibrate existing vector paths from actual tick marks, then compare to archived h5.
Does not rescale/fit curves to the source data; only the printed numeric axes calibrate
PDF coordinates. PyMuPDF decodes PDF paths and text, including clipping boundaries.
"""
from pathlib import Path
import json, re
import fitz
import numpy as np
import argparse
from types import SimpleNamespace
import sys
sys.dont_write_bytecode = True
import regenerate_optics

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source-root',type=Path,required=True)
parser.add_argument('--output-root',type=Path,default=regenerate_optics.THESIS_ROOT)
parser.add_argument('--audit',type=Path,required=True)
args=parser.parse_args()
THESIS=args.output_root.resolve()
data,_,_=regenerate_optics.load_data(args.source_root.resolve())

def peak(energy,y,mask):
    ids=np.flatnonzero(mask)
    i=int(ids[np.argmax(y[ids])])
    return {'energy_eV':float(energy[i]),'value':float(y[i]),
            'at_window_boundary':bool(i in (ids[0],ids[-1]))}

raw=SimpleNamespace(REF=regenerate_optics.SOURCE_COMMIT,
                    cache={(phase,channel,'corrected'):value for (phase,channel),value in data.items()},peak=peak)
FIGURES=[]
for quantity,_,chapter_file,project_file in regenerate_optics.FIGURES:
    FIGURES.extend([(str(Path('figures_ch3')/chapter_file),quantity),
                    (str(Path('figures_proj3')/project_file),quantity)])
NUMBER=re.compile(r'^[-+−]?(?:\d+(?:\.\d*)?|\.\d+)$')

def key(rect):return tuple(round(x,3) for x in rect)
def unpack_lines(items):
    segments=[]
    for item in items:
        if item[0]=='l':segments.append(((item[1].x,item[1].y),(item[2].x,item[2].y)))
        else:raise ValueError('Non-linear curve path '+str(item[0]))
    return np.array(segments,dtype=float)

def calibrate(rect,drawings,words):
    xt=[];yt=[]
    for d in drawings:
        its=d.get('items',[])
        if len(its)!=1 or its[0][0]!='l':continue
        _,a,b=its[0];dx=abs(a.x-b.x);dy=abs(a.y-b.y)
        if dx<.02 and 3<dy<4 and abs(max(a.y,b.y)-rect.y1)<.03:xt.append(a.x)
        if dy<.02 and 3<dx<4 and abs(min(a.x,b.x)-rect.x0)<.03:yt.append(a.y)
    xt=np.unique(np.round(xt,5));yt=np.unique(np.round(yt,5))
    assert len(xt)>=4 and len(yt)>=3,('missing ticks',rect,xt,yt)
    pairsx=[];pairsy=[]
    for w in words:
        if not NUMBER.match(w[4]):continue
        value=float(w[4].replace('−','-'));cx=(w[0]+w[2])/2;cy=(w[1]+w[3])/2
        if rect.x0-10<cx<rect.x1+10 and rect.y1-3<=w[1]<rect.y1+20:
            nearest=xt[np.argmin(abs(xt-cx))]
            if abs(nearest-cx)<2:pairsx.append((float(nearest),value))
        if rect.x0-90<w[2]<rect.x0-.5 and rect.y0-15<cy<rect.y1+15:
            nearest=yt[np.argmin(abs(yt-cy))]
            if abs(nearest-cy)<3:pairsy.append((float(nearest),value))
    # Mathtext may omit the minus glyph in PDF text extraction. Tick ordering
    # and the printed zero locate the sign unambiguously on these linear axes.
    zero=[p for p,v in pairsy if v==0]
    if zero:
        yzero=zero[0]
        pairsy=[(p,-abs(v) if p>yzero+.01 else v) for p,v in pairsy]
    pairsx=sorted(set(pairsx));pairsy=sorted(set(pairsy))
    assert len(pairsx)>=4 and len(pairsy)>=3,('not enough numeric labels',rect,pairsx,pairsy)
    ax,bx=np.polyfit(*np.array(pairsx).T,1)
    ay,by=np.polyfit(*np.array(pairsy).T,1)
    errx=max(abs(ax*p+bx-v) for p,v in pairsx);erry=max(abs(ay*p+by-v) for p,v in pairsy)
    assert errx<1e-4 and erry<1e-4,('nonlinear axis calibration',errx,erry)
    return {'x':(ax,bx),'y':(ay,by),'x_ticks':pairsx,'y_ticks':pairsy,
            'max_tick_fit_residual_x_eV':float(errx),'max_tick_fit_residual_y':float(erry)}

def stats(x):
    x=np.asarray(x)
    return {'max_abs':float(np.max(abs(x))),'rms':float(np.sqrt(np.mean(x*x))),
            'median_abs':float(np.median(abs(x))),'p99_abs':float(np.quantile(abs(x),.99))} if len(x) else None

report={'source_commit':raw.REF,'pdf_decoder':fitz.__doc__.splitlines()[0:3],
        'method':'Numeric axis labels matched to actual vector tick marks define independent affine coordinate calibration; no fit to h5 curve values. Compare each retained colored PDF vertex against corrected h5 values linearly interpolated in energy. Also compare all in-view raw samples against PDF polylines, reporting simplification errors separately.',
        'figures':[]}
for filename,quantity in FIGURES:
    page=fitz.open(THESIS/filename)[0]
    drawings=page.get_drawings(extended=True);words=page.get_text('words')
    rectangles={key(d['scissor']):d['scissor'] for d in drawings if d['type']=='clip' and d['scissor'].width>300 and d['scissor'].height>150}
    frames=sorted(rectangles.items(),key=lambda p:(round(p[1].y0,2),p[1].x0))
    frame_index={k:i for i,(k,r) in enumerate(frames)}
    cal={k:calibrate(r,drawings,words) for k,r in frames}
    fig={'file':str(THESIS/filename),'axes':[{'panel':i,'clip_rect_pt':list(r),**cal[k]} for i,(k,r) in enumerate(frames)],'curves':[]}
    current=None
    for drawing in drawings:
        if drawing['type']=='clip' and key(drawing['scissor']) in frame_index:current=key(drawing['scissor'])
        color=drawing.get('color')
        if color is None or max(color)-min(color)<.2 or len(drawing.get('items',[]))<30:continue
        assert current is not None
        i=frame_index[current];rect=rectangles[current];axis=cal[current]
        phase='a' if color[2]>color[0] else 'b'
        channel='in_plane' if i%2==0 else 'out_of_plane'
        field=('eps1' if i<2 else 'eps2') if quantity=='dielectric' else quantity
        energy,values=raw.cache[(phase,channel,'corrected')];yraw=values[field]
        segpx=unpack_lines(drawing['items'])
        seg=segpx.copy();seg[:,:,0]=axis['x'][0]*segpx[:,:,0]+axis['x'][1];seg[:,:,1]=axis['y'][0]*segpx[:,:,1]+axis['y'][1]
        vertices_px=np.unique(segpx.reshape(-1,2),axis=0)
        vertices=np.column_stack((axis['x'][0]*vertices_px[:,0]+axis['x'][1],axis['y'][0]*vertices_px[:,1]+axis['y'][1]))
        visible=(vertices_px[:,0]>=rect.x0-.01)&(vertices_px[:,0]<=rect.x1+.01)&(vertices_px[:,1]>=rect.y0-.01)&(vertices_px[:,1]<=rect.y1+.01)&(vertices[:,0]>=-1e-5)&(vertices[:,0]<=12+1e-5)
        xv,yv=vertices[visible].T
        predicted=np.interp(xv,energy,yraw)
        vertex_errors=yv-predicted
        # Distance to original sample locations is diagnostic: simplification
        # normally retains existing input vertices, except backend clipping.
        nearidx=np.searchsorted(energy,xv).clip(1,len(energy)-1)
        dx=np.minimum(abs(xv-energy[nearidx]),abs(xv-energy[nearidx-1]))
        ylim=sorted([axis['y'][0]*rect.y0+axis['y'][1],axis['y'][0]*rect.y1+axis['y'][1]])
        rawmask=(energy>=max(0,float(np.min(vertices[:,0])))-1e-5)&(energy<=min(12,float(np.max(vertices[:,0])))+1e-5)&(yraw>=ylim[0])&(yraw<=ylim[1])
        ids=np.flatnonzero(rawmask);polyerrors=[];polyids=[]
        for j in ids:
            e=energy[j];candidates=seg[(seg[:,0,0]<=e+1e-5)&(seg[:,1,0]>=e-1e-5)&(seg[:,1,0]>seg[:,0,0]+1e-9)]
            if not len(candidates):continue
            # At a shared endpoint either adjacent segment has the same value.
            s=candidates[0];t=(e-s[0,0])/(s[1,0]-s[0,0]);yp=s[0,1]+t*(s[1,1]-s[0,1])
            polyerrors.append(yp-yraw[j]);polyids.append(int(j))
        raw_range=float(np.max(yraw[(energy>=0)&(energy<=12)])-np.min(yraw[(energy>=0)&(energy<=12)]))
        distances=(np.abs(vertex_errors)/abs(axis['y'][0])).tolist()
        plotted_raw=(energy>=0)&(energy<=12)
        record={'phase':phase,'channel':channel,'quantity':field,'panel':i,'color_rgb':list(color),
                'pdf_vertices_total':len(vertices),'pdf_vertices_visible':len(xv),
                'raw_samples_0_to_12_eV':int(np.sum(plotted_raw)),
                'pdf_x_range_eV':[float(np.min(vertices[:,0])),float(np.max(vertices[:,0]))],
                'raw_0_to_12_x_range_eV':[float(energy[plotted_raw][0]),float(energy[plotted_raw][-1])],
                'calibrated_y_limits':ylim,'max_vertex_energy_distance_to_input_sample_eV':float(np.max(dx)),
                'visible_vertex_vs_raw_linear_interpolation':stats(vertex_errors),
                'visible_vertex_residual_in_pdf_points':stats(distances),
                'visible_raw_sample_vs_pdf_polyline':stats(polyerrors),
                'raw_samples_compared_with_polyline':len(polyids),
                'polyline_max_abs_error_over_raw_range':float(max(abs(np.array(polyerrors)))/raw_range),
                'raw_samples_above_plot_limit':int(np.sum(plotted_raw&(yraw>ylim[1]+1e-6))),
                'raw_max_0_to_12':raw.peak(energy,yraw,plotted_raw),
                'segments_disconnected_after_page_clipping':int(np.sum(np.linalg.norm(segpx[1:,0,:]-segpx[:-1,1,:],axis=1)>.01))}
        fig['curves'].append(record)
    assert len(fig['curves'])==(8 if quantity=='dielectric' else 4),(filename,len(fig['curves']))
    report['figures'].append(fig)

out=args.audit
out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(report,indent=2)+'\n')
print('REPORT',out)
for fig in report['figures']:
 print(Path(fig['file']).name)
 for c in fig['curves']:
  print(c['phase'],c['channel'],c['quantity'],'vertex',c['visible_vertex_vs_raw_linear_interpolation'],'vertex_pt_max',c['visible_vertex_residual_in_pdf_points']['max_abs'],'poly_rel',c['polyline_max_abs_error_over_raw_range'],'n',c['pdf_vertices_visible'],'clipped',c['raw_samples_above_plot_limit'])

curves=[curve for figure in report['figures'] for curve in figure['curves']]
assert len(curves)==56
assert all(curve['raw_samples_above_plot_limit']==0 for curve in curves)
assert all(curve['visible_vertex_residual_in_pdf_points']['max_abs']<0.01 for curve in curves)
print('PASS: 28 independent curves verified in both figure versions; no clipped high values.')
