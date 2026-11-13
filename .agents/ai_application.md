# AI Application Record

## Chapters 2–3 application record

Applied on 2026-09-21 after approval of `ai_ch2_last.md` and `ai_ch3_last.md`.
The user's subsequent instruction defers the creation of Chapter 4.

### Applied scope

- `src/fundamentals_a.tex`: the approved local corrections and practical-method additions are applied. The original topology subsection remains intact as Section 2.6.6. The optical cross-reference uses the Chapter 3 n/m band indices and occupation factors.
- `src/fundamentals_b.tex`: all 41 approved operations are applied: 31 local replacements, seven source-citation cleanups, and three removals of directly repeated sentences. The six example figures and the original derivation sequence remain. The text and captions identify the author as the source of the calculations and refer to Chapter 6.
- `src/project_3_main.tex` and `src/project_3_SI.tex`: the necessary shared-data corrections are synchronized, including effective thickness, the verified alpha/beta calculation settings, NBANDS terminology, optical units, and the interpretations affected by the corrected spectra.
- Twelve optical PDFs are regenerated from the same archived alpha/beta dielectric arrays. Beta uses an unrounded effective thickness of 5.855086567902241 Å; absorption uses angular frequency and is displayed in nm^-1; the loss axes show the complete peaks. The original DFT data are unchanged. No Drude term or new DFT calculation is introduced.
- The exporter, PDF verifier, and reproduction instructions are in `figures_ch3/`. The fixed source commit and input SHA-256 hashes are embedded in the exporter; reproduction does not depend on the ignored `agents/` directory.

No new Chapter 4 exists in the formal source. `thesis.tex`, `src/introduction.tex`, `src/publications.tex`, and `src/appendix.tex` are byte-for-byte unchanged from the start of this application. Research chapters retain numbers 4, 5, and 6. The temporary topology seed is retained only at `/tmp/thesis-apply-approved/fundamentals_c.deferred.tex` for later discussion.

### Verification

The final `.output/thesis.pdf` was built with latexmk/pdflatex and Biber and converged without undefined references, undefined citations, or duplicate labels. The ten existing overfull-box warnings have the same types and widths as the baseline; no new overfull warning was introduced. Existing class-name, footnote-command, and deprecated angstrom-unit notices remain.

All 291 original Chapter 2 labels and all 63 original Chapter 3 labels are preserved. Chapter 2 now has 299 labels and Chapter 3 has 65. Chapter 3 retains its original headings and six figure environments; its equation environments change from 52 to 54 with the Drude and optical-volume-normalization expressions. `git diff --check` passes.

The twelve exported PDFs were checked against the corrected arrays using their printed ticks and PDF vector paths. All 56 exported curves contain the expected 33,516 sampled vertices. The maximum retained-vertex residual is 0.003245 PDF point, and no high peak is clipped. The final PDF was built after all twelve replacement files were written; their hashes match the export audit.

Visual inspection covered 39 pages of the final thesis: printed page 36; pages 88–99; pages 113–116, 119–120, and 124–132; and pages 207–209, 218–221, 228–229, and 236–237. The formulas, longer captions, units, and complete loss peaks are visible without new clipping or overlap. The two figures on page 220 fit on the page. Project 3 retains relatively small original figure legends. The existing SI float order places two subsection headings together on page 229; this was not changed in this local revision.

The final PDF has 292 physical pages, compared with 288 before this application. Chapter 2 begins on printed page 15, Section 2.6 on page 88, and Chapter 3 on page 101. Chapters 4, 5, and 6 begin on pages 133, 169, and 203. Chapter 3 remains 32 pages including its closing page; Chapter 2 has increased by four pages. This revision must not be described as an overall page reduction.

TeXcount reports Chapter 2 body text changing from 14,795 to 15,496 words. Chapter 3 body text changes from 5,985 to 6,218 words, with captions and other outside-text words changing from 123 to 261. These are text counts, not counts of mathematical symbols.

### Remaining work

- Chapter 4 is deferred by the user's latest instruction. The approved plan's migration instructions have not been retained in the formal source.
- The other multi-system optical plots in Project 3 still require their own data/postprocessing audit, including any repeated alpha/beta curves. This application validates only the six figure pairs specified in the approved Chapter 3 plan.
- The research chapters' broader computational, topological, stability, and plasmon claims remain part of their later revisions. The two verified alpha/beta parameter sets cannot be generalized to other systems.
- `reports/reply_to_examiners.md` is unchanged. Its old appendix/page-reduction placeholder is not an accurate description of this application and must be replaced when the response letter is finalized. The source-attribution requirement is implemented; this record does not claim that all examiner requests are closed.

The approved `last` files remain as approval records. Their pre-application status statements and proposed Chapter 4 migration are superseded, for implementation status, by this record and the user's later instruction.

Machine-readable application, static, build, and page-map records are in `agents/application_verification/`. Optical provenance and exported-curve audits are in `agents/ch3_verification/`. Original TeX backups are in `/tmp/thesis-apply-approved/backup/`; the original twelve PDFs and their hash manifest are at the temporary path recorded in `figures_ch3/README.md`.
