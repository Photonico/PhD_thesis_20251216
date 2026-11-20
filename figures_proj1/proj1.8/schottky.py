"""Schottky-barrier figure for chapter 5 (figure 5.8).

Panel (a) draws the Schottky--Mott schematic.
Panel (b) plots the HSE06 band structure of the Graphene-B4C3 bilayer
directly from the original VASP output.
The settings follow the chapter 5 figure notebook
(Graphene-BC_20230622/figures_for_thesis/figures_for_thesis.ipynb):
24 pt titles, 18 pt axis labels, 16 pt ticks and corner labels,
1.5 pt lines, and a 16 x 6 inch canvas for two panels.
"""

import logging
from pathlib import Path

import h5py
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

HERE = Path(__file__).resolve().parent
DATA = (Path.home() / "Repos/Graphene-BC_20230622/3_Bandstructure"
        / "G_Graphene-B4C3_top_HSE/vaspout.h5")
OUTPUT = HERE / "proj1.8_schottky.pdf"
logging.getLogger("fontTools").setLevel(logging.ERROR)  # silence harmless font-timestamp warnings

plt.rcParams.update({
    "font.family": "serif", "mathtext.fontset": "cm", "axes.titlesize": 24,
    "axes.titlepad": 10, "axes.labelsize": 18, "xtick.labelsize": 16,
    "ytick.labelsize": 16, "legend.fontsize": 12, "lines.linewidth": 1.5,
    "xtick.direction": "in", "ytick.direction": "in", "xtick.top": True,
    "ytick.right": True, "pdf.fonttype": 42, "path.simplify": False,
})
BLUE, ORANGE, VIOLET, FERMI, GREY = "#1478E1", "#EB731E", "#8C64E1", "#643CC3", "#787878"
TAB = dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="#B4B4B4",
           alpha=0.75, linewidth=1.5)

def corner_label(ax, text, inset=8):
    """Label inside the upper-left corner of the axes, as in the other thesis figures."""
    ax.annotate(text, xy=(0, 1), xycoords="axes fraction", xytext=(inset, -inset),
                textcoords="offset points", ha="left", va="top", fontsize=16,
                bbox=TAB, zorder=10)


def barrier(ax, x, low, high, label, color, side="right"):
    """Double arrow from low to high, labelled on one side."""
    ax.annotate("", (x, high), (x, low), arrowprops=dict(
        arrowstyle="<->", color=color, lw=1.5, shrinkA=0, shrinkB=0))
    offset = 8 if side == "right" else -8
    ax.annotate(label, (x, (low + high) / 2), xytext=(offset, 0),
                textcoords="offset points", ha="left" if side == "right" else "right",
                va="center", color=color, fontsize=20)

def schematic(ax):
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    corner_label(ax, "(a) Schottky barriers")
    levels = {"C": (0.80, BLUE, "-"), "F": (0.65, FERMI, "--"), "V": (0.40, ORANGE, "-")}
    for name, (y, color, style) in levels.items():
        ax.plot([0.14, 0.92], [y, y], color=color, ls=style)
        ax.text(0.11, y, rf"$E_\mathrm{{{name}}}$", ha="right", va="center", fontsize=20)
    barrier(ax, 0.66, levels["F"][0], levels["C"][0], r"$\Phi_\mathrm{n}$", BLUE)
    barrier(ax, 0.36, levels["V"][0], levels["F"][0], r"$\Phi_\mathrm{p}$", ORANGE)
    notes = [r"$\Phi_\mathrm{n}<\Phi_\mathrm{p}$: $n$-type Schottky barrier",
             r"$\Phi_\mathrm{n}>\Phi_\mathrm{p}$: $p$-type Schottky barrier",
             r"$\Phi_\mathrm{n}$ or $\Phi_\mathrm{p}\approx0$: Ohmic contact"]
    blank = Line2D([], [], linestyle="none")
    ax.legend([blank] * len(notes), notes, loc="lower right", fontsize=20,
              handlelength=0, handletextpad=0, bbox_to_anchor=(0.92, 0.02))

def band_structure(ax):
    with h5py.File(DATA) as f:
        bands = f["results/electron_eigenvalues_kpoints_opt"]
        kpoints = bands["kpoint_coords"][()]
        energies = bands["eigenvalues"][0] - f["results/electron_dos_kpoints_opt/efermi"][()]
    # Path length in fractional coordinates, normalized to 1, as in the other chapter 5 band plots.
    path = np.concatenate([[0.0], np.cumsum(np.linalg.norm(np.diff(kpoints, axis=0), axis=1))])
    path /= path[-1]
    segment = len(kpoints) // 3                       # Gamma-K, K-M and M-Gamma
    ticks = path[[0, segment - 1, 2 * segment - 1, -1]]
    m_point = 2 * segment - 1
    phi_n = energies[m_point][energies[m_point] > 0].min()   # conduction band edge at M
    phi_p = -energies[0][energies[0] < 0].max()             # valence band edge at Gamma

    ax.plot(path, energies, color=VIOLET)
    for x in ticks[1:-1]:
        ax.axvline(x, color=GREY, ls="--", zorder=0)
    ax.axhline(0, color=FERMI, ls="--", zorder=0)
    ax.text(0.035, 0.51, r"$E_\mathrm{F}=0$", transform=ax.transAxes,
            color=FERMI, fontsize=16, va="bottom")
    ax.set(xlim=(0, 1), ylim=(-3, 3), yticks=range(-3, 4), ylabel="Energy (eV)",
           xticks=ticks, xticklabels=[r"$\Gamma$", "K", "M", r"$\Gamma$"])
    ax.set_title(r"Bandstructure for Graphene-B$_4$C$_3$")
    corner_label(ax, r"(b) Graphene-B$_4$C$_3$ (HSE06)")

    arrow_x = 0.96
    ax.hlines(phi_n, ticks[2], 1, colors=BLUE, linestyles="--")
    ax.hlines(-phi_p, 0.92, 1, colors=ORANGE, linestyles="--")
    barrier(ax, arrow_x, 0, phi_n, r"$\Phi_\mathrm{n}$", BLUE, side="left")
    barrier(ax, arrow_x, -phi_p, 0, r"$\Phi_\mathrm{p}$", ORANGE, side="left")
    return phi_n, phi_p

def main():
    fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(16, 6), layout="constrained")
    schematic(ax_a)
    phi_n, phi_p = band_structure(ax_b)
    fig.savefig(OUTPUT, metadata={"CreationDate": None})
    plt.close(fig)
    print(f"Phi_n = {phi_n:.2f} eV, Phi_p = {phi_p:.2f} eV -> {OUTPUT.name}")

if __name__ == "__main__":
    main()
