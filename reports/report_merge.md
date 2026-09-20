# Comprehensive Synthesis of PhD Thesis Examination Reports

Candidate Name: Lu Niu
Thesis Title: Exploring Quantum Properties of Light-Element Xenes: DFT Studies
of the Electronic Structure and Optical Response for Boron and Beryllium
Allotropes
Examiner 1: Report dated 24 August 2026 (PDF report)
Examiner 2: Report received August 2026 (DOCX report)

---

## 1. Executive Summary and Examination Outcomes

Both examiners commend the candidate for a substantial, original
first-principles
computational research programme exploring low-dimensional light-element
materials
(boron and beryllium allotropes, alongside graphene-based heterostructures).
The candidate's strong publication record (two published peer-reviewed papers
forming Chapters 4 and 5, and one submitted manuscript forming Chapter 6) is
explicitly recognized as demonstrating the quality, timeliness, and doctoral
standard of the research.

The examination recommendations and required scopes of revision differ in
emphasis:

- Examiner 2 recommends that the degree of Doctor of Philosophy be awarded
  subject to minor corrections that can be readily rectified and adjudicated
  by the Chair of Examination.

- Examiner 1 notes that while the thesis contains substantial original
  research
  capable of reaching a professional doctoral standard, substantial scientific
  and editorial corrections are required before final acceptance.

The primary criticisms from both examiners converge on five core areas:

1. Research positioning and narrative cohesion across Chapters 1 to 6;
2. Absence of a dedicated, critical literature review in Chapter 1;
3. Excessive textbook-like length of Chapters 2 and 3 without a concise,
   practical computational methodology roadmap;

4. Incomplete methodological parameters, figure legibility, and caption
   details
   in Chapters 4, 5, and 6;

5. Scientific rigor in defining stability, magnetism, band topology in metals,
   superconductivity workflows, and limitations of DFT approximations.

---

## 2. Cross-Cutting and Thesis-Level Requirements

### 2.1 Thesis Cohesion and Overarching Narrative (Examiner 1)

Examiner 1 observes that the thesis currently appears as a collection of
studies hopping between different materials without an explicit unifying
framework. The revised thesis must:

- Clarify why graphene-based boron heterostructures, complex boron phases, and
  beryllene allotropes belong to a single coherent thesis;

- Define the specific unresolved scientific question addressed by each
  chapter;

- Explain how the individual chapters collectively support an overarching
  conclusion regarding the quantum physics of light-element Xenes.

### 2.2 Statement of Candidate Contributions (Examiners 1 and 2)

Both examiners highlight that Chapters 4 and 5 are based on published
multi-author
journal articles, and Chapter 6 is based on a submitted manuscript.
The candidate must:

- Include an explicit statement at the beginning of Chapters 4, 5, and 6
  outlining the candidate's individual contributions relative to those of the
  co-authors (study design, computational execution, data analysis, manuscript
  drafting);

- Clearly distinguish between the characterization of previously known or
  proposed structures and genuinely new structural or property predictions.

### 2.3 Stability Demarcation and Experimental Status (Examiners 1 and 2)

Both examiners emphasize the necessity of precise scientific language when
discussing computational predictions:

- Clearly separate established experimental systems (such as epitaxial
  borophene
  on metallic substrates and sonochemically exfoliated beryllene flakes) from
  purely theoretical proposals;

- Qualify all stability statements by strictly distinguishing among:
   (a) Energetic preference (cohesive or adsorption energies relative to
   selected
      bulk or elemental references);
  (b) Dynamical stability (absence of imaginary phonon frequencies across the
      entire Brillouin zone at 0 K);
   (c) Thermal persistence (preservation of atomic bonding in
   finite-temperature
      NVT AIMD trajectories over short multi-picosecond timescales);
  (d) Thermodynamic stability and synthesizability (which require convex-hull
      thermodynamics and experimental realization, neither of which is
      definitively proved by short AIMD runs alone).

---

## 3. Chapter-by-Chapter Feedback and Required Revisions

### 3.1 Chapter 1: Introduction and Literature Review

Critique from Examiner 1:

- The introduction reads more as a broad survey than as a focused, cohesive
  argument;

- The literature review fails to culminate in a sharp research gap or central
  thesis motivation;

- The motivation for calculating optical response functions (absorption,
  refractive index, extinction coefficient, reflectivity, and energy-loss
   spectra) is unclear, appearing as a standard computational output rather
   than
  observables answering defined physical inquiries;

- The concept of band topology is introduced abruptly; the text must explain
  why topology is significant and what physical consequences follow from a
   non-trivial Z2 invariant (such as dissipationless helical edge states)
   before
  presenting the Fu-Kane parity formula.

Critique from Examiner 2:

- The principal weakness of Chapter 1 and the thesis as a whole is the absence
  of a dedicated, comprehensive literature review;

- The review must cover previous studies on related 2D boron- and
  beryllium-based
  systems, highlighting earlier findings and identifying knowledge gaps;

- The review should discuss the various theoretical and computational methods
  used in the literature, including the levels of theory successfully deployed
  to predict properties of similar light-element systems.

Required Revisions for Chapter 1:

- Expand Chapter 1 to incorporate a dedicated, critical literature review
  section;

- Contrast substrate-supported borophene with freestanding theoretical layers;
- Review the experimental status of beryllene (Chahal et al., 2023) and
  outline
  unresolved questions;

- Evaluate computational levels of theory (PBE, HSE06, GW/BSE, DFPT, EPW);
- Articulate explicit, sharp research gaps corresponding to Chapters 4, 5,
  and 6;

- Provide physical motivations for all optical response quantities and clarify
  the symmetry-driven origin and transport consequence of the Z2 invariant.

### 3.2 Chapters 2 and 3: Theoretical Foundations and Computational Methodology

Critique from Examiner 1:

- Chapters 2 and 3 are disproportionately long (~100 pages, nearly 40% of the
  thesis), containing extensive textbook-style formal derivations;

- The chapters fail to provide a concise, method-oriented roadmap of the
  actual
  computational methods employed in the subsequent research chapters;

- A practical, unified account is required covering: geometry optimization and
   convergence thresholds, Brillouin-zone k-point sampling, phonon
   calculations,
  AIMD, spin-polarized calculations and magnetic ordering, electron-phonon
  coupling and superconductivity workflows, and spin-orbit coupling with
   topological parity analysis. These methods must be explicitly linked to
   later
  chapters.

Critique from Examiner 2:

- The chapters present an almost textbook version of DFT and electrodynamics;
- From page 100 onwards in Chapter 3, optical properties of alpha-beryllene
  and
   beta-beryllene are presented as examples, but their data source is
   ambiguous;

- If these results were calculated by the candidate as part of the present
  thesis, an explicit statement and cross-reference must be provided; if taken
  from literature, proper citations must be given.

Required Revisions for Chapters 2 and 3:

- In Chapter 2, construct a dedicated Practical Computational Methodology
  Roadmap
  (Section 2.5 or 2.6) detailing operational parameters, convergence criteria,
   and software workflows for relaxation, phonons, AIMD, magnetism, EPW, and
   SOC;

- Include a synthesis table mapping computational methods and parameters
  directly to the specific scientific inquiries in Chapters 4, 5, and 6;

- Retain theoretical rigor while providing a clear two-part navigation
  framework
  (Formal Foundations versus Practical Computational Roadmap);

- In Chapter 3, explicitly declare that the alpha- and beta-beryllene optical
  spectra (Figures 3.1 to 3.6) are the candidate's original calculations from
  Chapter 6, add exact cross-references (cf. Chapter 6), and remove the
  misleading cluster of external citations;

- In Section 3.4, introduce each optical observable with its underlying
  physical
  motivation and diagnostic purpose.

### 3.3 Chapter 4: Graphene-Boron Heterostructures

Critique from Examiner 1:

- The study is useful but relatively incremental, mapping structure-property
  relationships rather than solving a major practical problem;

- The captions of Figures 4.29 to 4.36 (and corresponding SI figures) are too
  short to be self-contained; they must identify panels, tensor components,
  line styles, functional comparisons (PBE vs HSE06), polarization directions,
  units, and principal spectral features.

Critique from Examiner 2:

- The chapter is well written and thorough, but lacks an explicit author
   contribution statement detailing the candidate's role relative to
   co-authors;

- Several multi-panel figures suffer from poor legibility in the printed
  version;
  text, axis labels, and legends are too small to read (specifically Figures
  4.29 and 4.30);

- The candidate must increase font sizes, enlarge individual panels, or split
  congested figures into multiple figures.

Required Revisions for Chapter 4:

- Add a formal author contribution declaration at the head of Chapter 4;
- Rewrite captions for all optical figures (Figures 4.29--4.36) to be
  completely
  self-contained;

- Remake Figures 4.29 and 4.30 (and similar multi-panel figures), increasing
  legend and axis font sizes and splitting panels where necessary to ensure
  complete legibility.

### 3.4 Chapter 5: Penta-Bipyramid Boron Allotropes (o-B14)

Critique from Examiner 1:

- The chapter is scientifically strong and interesting, but claims of
  stability,
  superconductivity, and plasmon behavior require careful qualification as
  unverified predictive models;

- Cohesive energies, harmonic phonons, and a short 5.5 ps AIMD trajectory do
  not establish thermodynamic stability or experimental synthesizability;

- The small energy difference between AFM and FM configurations and
  inconsistent
   statements regarding negative (imaginary) phonon frequencies must be
   clarified;

- An internal contradiction must be resolved: the monolayer o-B14 is described
   as an AFM semiconductor in one section, yet treated as metallic in the
   optical
   discussion; the exact electronic/magnetic state and intraband (Drude)
   treatment
  must be stated;

- The difference between PBE and HSE06 band structures should be explained in
  terms of self-interaction and delocalization error reduction;

- The superconductivity workflow needs a concise, reproducible explanation of
  how DFPT, Wannier interpolation, and EPW generate electron-phonon matrix
   elements, alpha2F(omega), lambda, omega_log, and solutions to Allen-Dynes
   and
  anisotropic Migdal-Eliashberg equations;

- The distinction between harmonic 0 K phonon stability and finite-temperature
  AIMD must be stated clearly.

Critique from Examiner 2:

- The chapter represents a significant contribution and is already published;
- Figure 5.1 (atomic structures of o-B14 phases) appears too late; it should
   be referenced and presented earlier in the introductory or methodology
   section
  before computational models are discussed.

Required Revisions for Chapter 5:

- Move or introduce Figure 5.1 early in Chapter 5 before model descriptions;
- Add an explicit qualification of stability levels (energetic vs dynamical vs
  thermal persistence vs synthesizability);

- Resolve contradictory text on imaginary phonon frequencies;
- State the small AFM-FM numerical energy difference with precision;
- Reconcile the monolayer electronic state: state whether optical response was
   computed for the AFM ground state or metallic state, and detail intraband
   Drude
  damping parameters;

- Provide a physical explanation of PBE vs HSE06 gap opening;
- Provide a step-by-step reproducible workflow for the EPW superconductivity
   calculations, specifying q-grids, Wannier projections, and Coulomb
   pseudopotential.

### 3.5 Chapter 6: Beryllene Phases and Allotropes

Critique from Examiner 1:

- The chapter is potentially the most novel, but the method used to generate
  the proposed cubic trilayer beryllene structure is unclear;

- The claim of a non-trivial Z2 topological invariant requires rigorous
   justification because the cubic trilayer phase is simultaneously described
   as
  metallic;

- Report stability parameters and optical response functions with appropriate
  two-dimensional normalization;

- Maintain strict distinction between dynamical stability, energetic
  preference,
  and experimental synthesizability.

Critique from Examiner 2:

- Chapter 6 appears less comprehensive than Chapters 4 and 5;
- Weakness 1: Relies solely on GGA-PBE calculations without HSE06; provide
  justification for excluding HSE06;

- Weakness 2: Convergence tests in SI are not adequately discussed in the
  text;
   explain the convergence procedure and basis for k-point mesh selection in
   the
  methods section;

- Weakness 3: In Figures 6.2 and 6.3, green and blue spheres representing Be
  atoms are unexplained in captions and main text;

- Weakness 4: Provide rationale for hydrogenating alpha- and beta-beryllene
  while
  excluding the cubic trilayer phase;

- Weakness 5: Methodological details of AIMD simulations (ensemble,
  temperature,
  time step, total simulation time) are omitted.

Required Revisions for Chapter 6:

- Detail the structural construction of cubic trilayer beryllene (bcc
  cleaving,
  stacking registry, relaxation);

- Address the Z2 vs metallicity issue: verify whether an indirect gap or
   continuous direct gap exists throughout the Brillouin zone with SOC, or
   clarify
  the topological subspace classification;

- Justify the omission of HSE06 calculations (computational feasibility of
  dense optical grids with SOC vs established PBE trends in Chapters 4 and 5);

- Discuss k-point and energy cutoff convergence in the main text;
- Explain sphere colors in Figures 6.2 and 6.3 (e.g. outer vs central layers);
- Provide physical justification for hydrogenating alpha and beta while
  excluding
   trilayer (e.g. coordination saturation, steric hindrance, surface
   reconstruction);

- Specify complete AIMD parameters (NVT ensemble, Nosé-Hoover, 300 K, 1 fs
  step,
  duration, supercell dimensions);

- Apply appropriate 2D normalization for optical quantities and qualify
  stability.

### 3.6 Chapter 7: Conclusions and Outlook

Critique from Examiner 1:

- The scope of several scientific claims must be qualified, separating
  established facts from theoretical predictions.

Critique from Examiner 2:

- The chapter mainly summarizes chapter findings rather than providing a
  critical assessment of research limitations;

- Discuss limitations of theoretical approaches, computational assumptions,
   and uncertainties (e.g. lack of GW/BSE excitonic effects,
   independent-particle
   approximation, supercell vacuum artifacts, semi-empirical Coulomb
   pseudopotentials);

- Clearly distinguish between experimentally verified systems and pure
  theoretical
  predictions;

- The future work section simply lists theoretical directions; discuss
  specific
   improvements expected from proposed studies (e.g. quantitative excitonic
   shifts
  from BSE, transport signatures of edge states, substrate screening).

Required Revisions for Chapter 7:

- Insert a dedicated Limitations of the Present Work section addressing DFT
  approximations, optical screening, and stability extrapolations;

- Include a summary table delineating experimental reality versus theoretical
  prediction;

- Expand the Future Work section to explain the specific physical improvements
  expected from each proposed direction.

---

## 4. Comprehensive Consolidated Action Matrix

The following structured catalogue synthesizes every required revision across
both examination reports, identifying the chapter, target file, issue
description, examiner source, and action plan.

- Item 1 (Global, thesis.tex):
  Issue: Research narrative appears as jumping between materials.
  Source: Examiner 1.
  Action: Introduce cohesive 3-stage narrative: extrinsic heterostructures
  to intrinsic multicentre bonding to elemental light-metal topology.

- Item 2 (Chapter 1, src/introduction.tex):
  Issue: Absence of dedicated, comprehensive literature review.
  Source: Examiner 2.
  Action: Create Section 1.2 systematically reviewing 2D boron, beryllium,
  and computational levels of theory.

- Item 3 (Chapter 1, src/introduction.tex):
  Issue: Vague research gaps and central thesis motivation.
  Source: Examiner 1.
  Action: Formulate Section 1.4 defining three sharp research gaps
  corresponding directly to Chapters 4, 5, and 6.

- Item 4 (Chapter 1, src/introduction.tex):
  Issue: Optical properties lack defined physical motivation.
  Source: Examiner 1.
  Action: Add Section 1.3 explaining physical inquiries answered by
  dielectric tensor components, EELS plasmons, and reflectivity.

- Item 5 (Chapter 1, src/introduction.tex):
  Issue: Topology and Z2 invariant introduced without physical context.
  Source: Examiner 1.
  Action: Explain physical consequences of Z2 (helical edge states)
  prior to presenting the Fu-Kane parity invariant formula.

- Item 6 (Chapter 2, src/fundamentals_a.tex):
  Issue: Excessive textbook length; lacks practical methodology roadmap.
  Source: Examiners 1 and 2.
  Action: Create Section 2.6 (Practical Computational Methodology Roadmap)
  detailing relaxation, k-points, phonons, AIMD, magnetism, EPW, and SOC.

- Item 7 (Chapter 3, src/fundamentals_b.tex):
  Issue: Beryllene optical examples (p. 100+) lack clear attribution.
  Source: Examiner 2.
  Action: Explicitly state spectra are original results from Chapter 6;
  cross-reference Chapter 6; remove external literature citations.

- Item 8 (Chapter 3, src/fundamentals_b.tex):
  Issue: Optical response quantities lack physical question framing.
  Source: Examiner 1.
  Action: Introduce each optical observable in Section 3.4 with its
  physical diagnostic inquiry.

- Item 9 (Chapter 4, src/project_1_main.tex):
  Issue: Multi-author publication lacks candidate contribution statement.
  Source: Examiners 1 and 2.
  Action: Add author contribution declaration at the head of Chapter 4.

- Item 10 (Chapter 4, src/project_1_main.tex):
  Issue: Captions for Figures 4.29--4.36 too brief to be self-contained.
  Source: Examiner 1.
  Action: Rewrite captions detailing panels, tensor components, PBE vs
  HSE06, line styles, units, and principal features.

- Item 11 (Chapter 4, src/project_1_main.tex):
  Issue: Figures 4.29 and 4.30 illegible in print.
  Source: Examiner 2.
  Action: Remake figures with enlarged fonts, larger panels, or split
  multi-panel layouts.

- Item 12 (Chapter 5, src/project_2_main.tex):
  Issue: Multi-author publication lacks candidate contribution statement.
  Source: Examiners 1 and 2.
  Action: Add author contribution declaration at the head of Chapter 5.

- Item 13 (Chapter 5, src/project_2_main.tex):
  Issue: Figure 5.1 presented too late in the chapter.
  Source: Examiner 2.
  Action: Move and reference Figure 5.1 early in methodology or
  introductory section before model discussion.

- Item 14 (Chapter 5, src/project_2_main.tex):
  Issue: Stability, superconductivity, and plasmon claims need qualification.
  Source: Examiner 1.
  Action: Differentiate energetic preference, harmonic phonons, 5.5 ps
  AIMD, and synthesizability.

- Item 15 (Chapter 5, src/project_2_main.tex):
  Issue: Contradictory statements on imaginary phonon frequencies.
  Source: Examiner 1.
  Action: Clarify phonon dispersion status for each o-B14 phase without
  internal contradiction.

- Item 16 (Chapter 5, src/project_2_main.tex):
  Issue: Monolayer o-B14 state contradiction (AFM semiconductor vs metallic).
  Source: Examiner 1.
  Action: State electronic and magnetic configuration used for optics;
  detail Drude intraband damping parameters.

- Item 17 (Chapter 5, src/project_2_main.tex):
  Issue: PBE vs HSE06 difference needs physical explanation.
  Source: Examiner 1.
  Action: Explain gap opening via reduction of self-interaction and
  charge delocalization errors.

- Item 18 (Chapter 5, src/project_2_main.tex):
  Issue: Superconductivity workflow lacks reproducible description.
  Source: Examiner 1.
  Action: Detail DFPT, Wannier90, EPW, alpha2F, lambda, omega_log, and
  Eliashberg equations.

- Item 19 (Chapter 6, src/project_3_main.tex):
  Issue: Submitted manuscript lacks candidate contribution statement.
  Source: Examiner 1.
  Action: Add contribution and submission status statement at head of
  Chapter 6.

- Item 20 (Chapter 6, src/project_3_main.tex):
  Issue: Construction method for cubic trilayer beryllene is unclear.
  Source: Examiner 1.
  Action: Describe structural generation (bcc cleavage, stacking sequence,
  relaxation protocol).

- Item 21 (Chapter 6, src/project_3_main.tex):
  Issue: Z2 invariant claim contradicts metallic description.
  Source: Examiner 1.
  Action: Justify band topology: establish continuous direct gap with SOC
  or define topological subspace.

- Item 22 (Chapter 6, src/project_3_main.tex):
  Issue: Sole reliance on GGA-PBE without HSE06 lacks justification.
  Source: Examiner 2.
  Action: Provide computational justification (dense optical grid feasibility,
  SOC, consistency with Chapters 4 and 5).

- Item 23 (Chapter 6, src/project_3_main.tex):
  Issue: Convergence tests in SI not discussed in main text.
  Source: Examiner 2.
  Action: Discuss energy cutoff and k-point mesh convergence procedure
  in methods section.

- Item 24 (Chapter 6, src/project_3_main.tex):
  Issue: Atom sphere colors in Figures 6.2 and 6.3 unexplained.
  Source: Examiner 2.
  Action: State physical meaning of green vs blue spheres in captions and
  text (outer vs inner layers).

- Item 25 (Chapter 6, src/project_3_main.tex):
  Issue: Rationale for excluding trilayer phase from hydrogenation missing.
  Source: Examiner 2.
  Action: Explain physical basis (coordination saturation, steric hindrance,
  surface reconstruction).

- Item 26 (Chapter 6, src/project_3_main.tex):
  Issue: AIMD simulation parameters omitted.
  Source: Examiner 2.
  Action: State ensemble (NVT), thermostat (Nosé-Hoover), temperature
  (300 K), time step (1 fs), duration.

- Item 27 (Chapter 7, src/conclusion.tex):
  Issue: Absence of critical assessment of research limitations.
  Source: Examiner 2.
  Action: Add dedicated Limitations section covering DFT approximations,
  single-particle optics, and AIMD timescales.

- Item 28 (Chapter 7, src/conclusion.tex):
  Issue: Distinguish experimental systems from theoretical predictions.
  Source: Examiners 1 and 2.
  Action: Include systematic comparison table separating experimental
  reality from computational prediction.

- Item 29 (Chapter 7, src/conclusion.tex):
  Issue: Future work lacks specific expected physical improvements.
  Source: Examiner 2.
  Action: Explain concrete physical advancements expected from GW/BSE,
  quantum transport, and substrates.
