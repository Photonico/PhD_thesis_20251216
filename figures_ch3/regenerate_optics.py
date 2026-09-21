"""Regenerate the paired Chapter 3 / Project 3 optical figures.

Requires numpy, h5py and matplotlib. Download the two phase directories
6.0_dielectric_selection/{a,b}-Beryllene (vaspout.h5 and CONTCAR) from
https://github.com/Photonico/H-Beryllene_20250718 at SOURCE_COMMIT, then run:

    python figures_ch3/regenerate_optics.py --source-root /path/to/archive

By default, figures are written to this thesis repository. Use --output-root
for a separate preview directory. Input hashes from the prior source audit
are pinned below. The original HDF5 files and shared vmatplot helpers are read-only.
Only postprocessing is corrected; no DFT calculation or Drude term is added.
"""

import argparse
import hashlib
import json
from pathlib import Path

import h5py
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np


THESIS_ROOT = Path(__file__).resolve().parents[1]
SOURCE_COMMIT = "f863ab02ebf93d5804f5552967ea750571778335"
SOURCE_SHA256 = {
    "6.0_dielectric_selection/a-Beryllene/CONTCAR": "e36bcb9206cd198020d09178a6bc5a3bb02a73ff113dda84f70d7d217eccd5cd",
    "6.0_dielectric_selection/a-Beryllene/vaspout.h5": "50609bd82c41b81ba4c386da69e4f3bb219ddb8b66eafb4f80375c3bc76d7d19",
    "6.0_dielectric_selection/b-Beryllene/CONTCAR": "db7f6143175489b93ac9ca4caa14ac5a1e05903ea31080528dd09a69a0ef9a02",
    "6.0_dielectric_selection/b-Beryllene/vaspout.h5": "639db6a94ff71123d7758eb37014c7f1f9961a201feebdd32d395da2e9a4dbea",
}
H_EV_S = 4.135667662e-15  # Ordinary Planck constant used by the source archive.
C_NM_S = 2.99792458e17
BE_RADIUS_A = 1.98  # Retained effective-thickness convention, not a fitted radius.
PHASES = ("a", "b")
CHANNELS = (("in_plane", 0, "in-plane"), ("out_of_plane", 2, "out-of-plane"))
COLORS = {"a": ("#1478E1", "#14A0FF"), "b": ("#FA8C00", "#FFA03C")}
LABELS = {"a": "α-beryllene", "b": "β-beryllene"}
FIGURES = (
    ("dielectric", "Dielectric function", "3.1_dielectric.pdf", "fig3.13_dielectric.pdf"),
    ("absorption_nm^-1", "Absorption coefficient", "4.1_absorption.pdf", "fig3.14a_absorption.pdf"),
    ("n", "Refractive index", "4.2_refractive.pdf", "fig3.14b_refractive.pdf"),
    ("k", "Extinction coefficient", "4.3_extinction.pdf", "fig3.15_extinction.pdf"),
    ("R", "Reflectivity", "4.4_reflectivity.pdf", "S3.16_reflectivity.pdf"),
    ("L", "Energy-loss spectrum", "4.5_energy-loss.pdf", "S3.17_energy-loss.pdf"),
)
STYLE = {
    "text.usetex": False, "font.family": "serif", "mathtext.fontset": "cm",
    "axes.titlesize": 20, "axes.labelsize": 16,
    "xtick.labelsize": 14, "ytick.labelsize": 14, "legend.fontsize": 12,
    "figure.facecolor": "white", "lines.solid_capstyle": "round",
    "lines.dash_capstyle": "round", "lines.solid_joinstyle": "round",
    "lines.dash_joinstyle": "round", "path.simplify": False,
}


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def geometry(path):
    """Read the archived, orthogonal out-of-plane cell and direct coordinates."""
    lines = path.read_text().splitlines()
    scale = float(lines[1])
    cell = np.array([[float(x) for x in s.split()[:3]] for s in lines[2:5]]) * scale
    assert scale > 0 and np.allclose(cell[2, :2], 0)
    assert np.allclose(cell[:2, 2], 0)
    count = sum(int(x) for x in lines[6].split())
    start = 7 + int(lines[7].lower().startswith("s"))
    assert lines[start].lower().startswith("d")
    positions = np.array([[float(x) for x in s.split()[:3]]
                          for s in lines[start + 1:start + 1 + count]])
    height = float(np.linalg.norm(cell[2]))
    span = float(np.ptp(positions[:, 2]))
    return {"cell_height_A": height, "fractional_z_span": span,
            "geometric_z_span_A": height * span,
            "effective_thickness_A": height * span + 2 * BE_RADIUS_A}


def load_data(source_root):
    """Compute each phase/channel once; both figure versions share these arrays."""
    data, geometries, inputs = {}, {}, []
    for phase in PHASES:
        relative = Path("6.0_dielectric_selection") / f"{phase}-Beryllene"
        for name in ("CONTCAR", "vaspout.h5"):
            path = source_root / relative / name
            digest = sha256(path)
            if digest != SOURCE_SHA256[str(relative / name)]:
                raise ValueError(f"Source hash mismatch: {path}")
            inputs.append({"path": str(relative / name), "sha256": digest})
        geom = geometries[phase] = geometry(source_root / relative / "CONTCAR")
        with h5py.File(source_root / relative / "vaspout.h5", "r") as handle:
            energy = handle["results/linear_response/energies_dielectric_function"][()]
            tensor = handle["results/linear_response/density_density_dielectric_function"][()]
        omega = 2 * np.pi * energy / H_EV_S
        for channel, index, _ in CHANNELS:
            eps_sc = tensor[index, index, :, 0] + 1j * tensor[index, index, :, 1]
            # Retain the archived effective optical-volume normalization for xx and zz.
            eps = 1 + geom["cell_height_A"] / geom["effective_thickness_A"] * (eps_sc - 1)
            n = np.sqrt(np.maximum((np.abs(eps) + eps.real) / 2, 0))
            k = np.sqrt(np.maximum((np.abs(eps) - eps.real) / 2, 0))
            values = {"eps1": eps.real, "eps2": eps.imag, "n": n, "k": k,
                      "absorption_nm^-1": 2 * omega * k / C_NM_S,
                      "R": ((n - 1)**2 + k**2) / ((n + 1)**2 + k**2),
                      "L": eps.imag / np.abs(eps)**2}
            assert all(np.isfinite(y).all() for y in values.values())
            data[phase, channel] = energy, values
    return data, geometries, inputs


def visible_spectrum(ax):
    """Retain the source notebook's visible-spectrum background and x margins."""
    ax.set_xlim(ax.get_xlim())
    wavelengths = np.linspace(380, 750, 1000)
    energies = H_EV_S * C_NM_S / wavelengths
    colors = plt.get_cmap("nipy_spectral")(np.linspace(0, 1, 1000))[np.argsort(energies)]
    grad = np.tile(np.linspace(0, 1, 1000), (10, 1))
    alpha = np.tile(np.sin(np.linspace(0, np.pi, 1000)) * 0.24, (10, 1))
    ax.imshow(grad, aspect="auto", extent=[min(energies), max(energies), *ax.get_ylim()],
              cmap=ListedColormap(colors), alpha=alpha, zorder=-12)


def configure_axes(ax):
    ax.tick_params(direction="in", which="both", top=True, right=True, bottom=True, left=True)
    ax.ticklabel_format(style="sci", axis="y", scilimits=(-3, 3),
                        useOffset=False, useMathText=True)
    ax.legend(loc="best")
    visible_spectrum(ax)


def plot_quantity(data, quantity, title):
    dielectric = quantity == "dielectric"
    fig, axes = plt.subplots(2 if dielectric else 1, 2,
                             figsize=(16, 12 if dielectric else 6), dpi=196, squeeze=False)
    fig.suptitle(title + ("\n" if dielectric else ""), fontsize=20)
    panels = []
    for row in range(len(axes)):
        for column, (channel, _, alias) in enumerate(CHANNELS):
            ax = axes[row, column]
            field = ("eps1" if row == 0 else "eps2") if dielectric else quantity
            for phase in PHASES:
                energy, values = data[phase, channel]
                keep = (energy >= 0) & (energy <= 12)
                ax.plot(energy[keep], values[field][keep], label=LABELS[phase],
                        color=COLORS[phase][int(field == "eps2")], ls="solid", lw=1.5)
            if dielectric:
                ax.set_title(("Real" if row == 0 else "Imaginary") + " part for " + alias)
                if row == 0:
                    xmax = max(data[phase, channel][0][data[phase, channel][0] <= 12][-1] for phase in PHASES)
                    ax.plot([0, xmax], [0, 0], color="#787878", ls="--", lw=1.5)
                low, high = ax.get_ylim()
                high = min(80, high)
                ax.set_ylim(max(-60, low) if row == 0 else -0.05 * high, high)
                if column == 0:
                    ax.set_ylabel("Dielectric function", fontsize=18)
                if row == 1:
                    ax.set_xlabel("Photon energy (eV)", fontsize=18)
            else:
                ax.set_title(alias)
                if quantity == "absorption_nm^-1":
                    ax.set_ylim(-0.0125, 0.2625)
                elif quantity == "L":
                    ax.set_ylim(-0.1, 2.5 if column == 0 else 9.5)
                else:
                    low, high = {"n": (-0.375, 7.875), "k": (-0.25, 5.25), "R": (-0.05, 1.05)}[quantity]
                    ax.set_ylim(low, min(high, ax.get_ylim()[1]))
                if column == 0:
                    ylabel = r"Absorption coefficient (nm$^{-1}$)" if quantity == "absorption_nm^-1" else title
                    ax.set_ylabel(ylabel, fontsize=18)
                ax.set_xlabel("Photon energy (eV)", fontsize=16)
            configure_axes(ax)
            # Ensure that the corrected curves are fully visible, including low-energy data.
            for phase in PHASES:
                energy, values = data[phase, channel]
                y = values[field][(energy >= 0) & (energy <= 12)]
                assert np.min(y) >= ax.get_ylim()[0] and np.max(y) <= ax.get_ylim()[1]
            panels.append({"channel": channel, "quantity": field,
                           "xlim_eV": list(ax.get_xlim()), "ylim": list(ax.get_ylim())})
    fig.tight_layout()
    return fig, panels


def thesis_fonts(fig):
    """Apply the same font-size changes as the original thesis notebook."""
    fig._suptitle.set_fontsize(28)
    for ax in fig.axes:
        ax.title.set_fontsize(24)
        ax.xaxis.label.set_fontsize(20)
        ax.yaxis.label.set_fontsize(20)
        ax.tick_params(axis="both", which="both", labelsize=16)
        for text in ax.get_legend().get_texts():
            text.set_fontsize(18)
        ax.get_legend().get_title().set_fontsize(18)
    fig.tight_layout()


def generate(source_root, output_root):
    data, geometries, inputs = load_data(source_root)
    report = {"source_commit": SOURCE_COMMIT, "source_files": inputs, "geometry": geometries,
              "scope": "Corrected postprocessing of archived density-density interband arrays; no new DFT or Drude term.",
              "h_eV_s": H_EV_S, "c_nm_s": C_NM_S,
              "software": {"numpy": np.__version__, "h5py": h5py.__version__, "matplotlib": matplotlib.__version__},
              "figures": [], "maxima_0_to_12_eV": {}}
    with plt.rc_context(STYLE):
        for quantity, title, chapter_file, project_file in FIGURES:
            fig, panels = plot_quantity(data, quantity, title)
            for folder, name, enlarge in (("figures_proj3", project_file, False), ("figures_ch3", chapter_file, True)):
                path = output_root / folder / name
                path.parent.mkdir(parents=True, exist_ok=True)
                if enlarge:
                    thesis_fonts(fig)
                fig.savefig(path, metadata={"CreationDate": None, "ModDate": None})
                report["figures"].append({"path": str(Path(folder) / name), "sha256": sha256(path),
                                          "size_inches": fig.get_size_inches().tolist(), "panels": panels})
            plt.close(fig)
    for (phase, channel), (energy, values) in data.items():
        ids = np.flatnonzero((energy >= 0) & (energy <= 12))
        report["maxima_0_to_12_eV"][f"{phase}_{channel}"] = {
            field: {"value": float(y[ids].max()), "energy_eV": float(energy[ids[np.argmax(y[ids])]])}
            for field, y in values.items()}
    # Recheck source hashes after exporting to verify the read-only source contract.
    assert all(sha256(source_root / item["path"]) == item["sha256"] for item in inputs)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, default=THESIS_ROOT)
    parser.add_argument("--audit", type=Path, help="Optional export manifest and numerical summary")
    args = parser.parse_args()
    report = generate(args.source_root.resolve(), args.output_root.resolve())
    if args.audit:
        args.audit.parent.mkdir(parents=True, exist_ok=True)
        args.audit.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")
    print(f"Generated {len(report['figures'])} PDFs from 28 shared corrected curves.")
    print(json.dumps(report["geometry"], indent=2))


if __name__ == "__main__":
    main()
