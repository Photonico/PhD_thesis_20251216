# Reproducing the optical figures

## Source-project synchronization on 2026-11-18

The six PDFs are now copies of the thesis versions written by `0.0_thesis_demo.ipynb`
in `../H-Beryllene_20250718` (run with `figure_version("thesis")`), the same files that
Project 3 uses:

| Chapter 3 | `../H-Beryllene_20250718/figures/` |
| --- | --- |
| `3.1_dielectric.pdf` | `dielectric_alpha-beta_thesis.pdf` |
| `4.1_absorption.pdf` | `optics_alpha-beta_absorption_thesis.pdf` |
| `4.2_refractive.pdf` | `optics_alpha-beta_refractive_thesis.pdf` |
| `4.3_extinction.pdf` | `optics_alpha-beta_extinction_thesis.pdf` |
| `4.4_reflectivity.pdf` | `optics_alpha-beta_reflectivity_thesis.pdf` |
| `4.5_energy-loss.pdf` | `optics_alpha-beta_energy-loss_thesis.pdf` |

Subplot titles sit in rounded boxes inside the upper-left corner of each panel and the
legends sit in a corner. The scripts below reproduce the earlier layout, with titles
above the panels.

## Source-project synchronization on 2026-09-21

The PDFs were subsequently synchronized from the repaired calculation
project `../H-Beryllene_20250718/exported_figures/`. That project's notebook-based
pipeline is the canonical generator for all 34 A/B/C figures, including the bulk,
cubic, hydrogenated and convergence comparisons. See `../optics_update.md` and
`../optics_update_manifest.json` from this directory for the synchronization record.
The self-contained scripts below remain an independent A-group reproduction;
the earlier audit hashes described below are historical and do not identify the
new source-library export bytes.

`regenerate_optics.py` produces the six Chapter 3 figures and the six
corresponding Project 3 figures from the same corrected arrays. It retains
the original filenames, colors, solid curves, panel layout, visible-spectrum
background, and separate publication/thesis font sizes.

Use Python with NumPy, h5py, Matplotlib and PyMuPDF. Download `CONTCAR` and
`vaspout.h5` from each of `6.0_dielectric_selection/a-Beryllene` and
`6.0_dielectric_selection/b-Beryllene` in the
[fixed source archive](https://github.com/Photonico/H-Beryllene_20250718/tree/f863ab02ebf93d5804f5552967ea750571778335).
Preserve that directory structure under an archive directory. The script
verifies all four SHA-256 hashes pinned in the script from the source audit before
reading the data; no raw file is modified or copied into the thesis repository.
The source audit in the ignored `agents` directory is not a runtime dependency.

From the thesis root:

```sh
python figures_ch3/regenerate_optics.py \
  --source-root /path/to/archive \
  --audit agents/ch3_verification/corrected-export-audit.json

python figures_ch3/verify_optics.py \
  --source-root /path/to/archive \
  --audit agents/ch3_verification/corrected-pdf-vs-h5-numeric-audit.json
```

Both commands accept `--output-root /path/to/preview` to use a separate
directory instead of the thesis repository. The exporter is deterministic
within the recorded software environment; PDF timestamps are omitted.

The corrections are limited to the approved postprocessing changes:

- Read the full cell height and fractional atomic span from `CONTCAR`.
  The retained radius convention is 1.98 Å, giving effective thicknesses
  3.96 Å and 5.855086567902241 Å for the two phases.
- Use angular frequency `2*pi*energy/h` in the absorption coefficient,
  with `h = 4.135667662e-15 eV s` and `c = 2.99792458e17 nm/s`.
  The displayed absorption unit remains nm^-1.
- Retain the original effective optical-volume rescaling for both components.
  No Drude term or new DFT result is introduced.
- Show absorption through 0.2625 nm^-1 and loss through 2.5 in-plane
  and 9.5 out-of-plane, with a small margin below zero.

Every input sample in the 0–12 eV window is retained in the PDF paths.
The verifier independently calibrates each PDF panel using its printed
numeric ticks and vector tick marks, then checks all 56 exported curves
(28 distinct curves in two versions). It checks for clipped high values and
requires retained-vertex residuals below 0.01 PDF point. The original source
and pre-correction evidence remain in `agents/ch3_verification/`; the two
`corrected-*.json` files record the replacement figures and their validation.

Before replacement, the twelve original PDFs and their SHA-256 manifest
were saved outside the repository at
`/var/folders/jd/spwt8xjd2jdcbvqz6zhd785m0000gn/T/thesis-ch3-figures-before-mscey1z1`.
That temporary backup is not required for regeneration.
