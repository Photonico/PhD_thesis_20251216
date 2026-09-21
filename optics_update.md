# Optical result synchronization, 2026-09-21

The verified results from `../H-Beryllene_20250718/exported_figures/` were copied to 34 existing figure paths in this repository. The figure filenames and LaTeX references are preserved. `optics_update_manifest.json` records the exact source-to-target result hashes and the affected TeX files.

The changes correct structure-derived effective thicknesses, the absorption factor of `2*pi`, clipped plot ranges, a convergence band label and a duplicate convergence curve. The effective dielectric model and the original Be/H surface-radius convention are retained. The source VASP data have not changed.

The corresponding methods, optical discussion, SI, abstract and conclusion have been brought into agreement with the corrected arrays. Cubic trilayer absorption is not universally enhanced relative to bulk bcc, and hydrogenation of alpha has different effects in-plane and out-of-plane. Numerical loss features are distinguished from evidence for propagating modes and lifetimes. Absorption is given in nm^-1; NBANDS means total bands. The hcp low-energy convergence outlier is displayed and discussed.

Canonical regeneration and numerical verification remain in the calculation repository: `scripts/regenerate_optics.py`, `scripts/audit_optics.py`, and `exported_figures/validation/`. No raw calculation arrays or library copies for unrelated projects were overwritten here. The calculation project's `draft_corrections.md` contains the page-specific evidence behind the text changes.

No local backup copies were created. Existing unrelated working-tree changes were preserved. This synchronization updates local files only; it does not create a Git commit or push a remote branch.
