# Chapter 1 (Introduction) 修改方案与候选文本

本文档针对两份评审报告 (Examiner 1 与 Examiner 2) 对 Chapter 1 提出的意见,
结合 agents/ai.md 中的协作规范编写.
用于指导 src/introduction.tex 的重构与扩写.

说明:

- 中文部分用于修改逻辑, 结构设计与评审对应说明;
- 英文部分为可直接或对照录入 LaTeX 源文件的候选文本与骨架;
- 全文不使用 Markdown 粗体标记, 保持源码纯净易读;
- 本章涉及后续章节的数据和结论, 在文末设立跨章回查清单.

---

## 1. 评审意见诊断与本章修改目标

### 1.1 评审人核心意见对照

Examiner 1 (PDF 报告):

- 论文缺乏清晰的宏观研究定位与核心动机 (The thesis-level research position
  is nevertheless not sufficiently clear: the early literature review does not
  lead to a sharp research gap or central motivation);
- 各研究章之间显得在不同材料间跳跃, 缺乏内在纽带 (The rest chapters look like
  hopping between different materials and there is a lack of relationship
  between them);
- 第 1 章像广泛的背景罗列而非紧凑的立论, 需阐明为何石墨烯-硼体系, 硼多形体和铍相
  同属于一篇论文, 每章解决什么未决问题, 如何共同支持一个结论 (It should explain why
  graphene-based boron systems, boron phases, and beryllene belong to one
  thesis,
  what unresolved question each chapter addresses, and how the studies
  collectively
  support one conclusion);
- 文献综述需批判性地分离实验已实现体系与理论预言体系, 明确研究空白 (The literature
  should be used critically to separate established experimental systems from
  theoretical
  proposals and to identify the research gap);
- 光学性质计算缺乏明确物理动机, 各光谱量不应作为常规数据罗列, 而应作为回答具体科学问题的
  可观测量 (The motivation for calculating optical properties is also not
  sufficiently
  clear: absorption, refractive index, reflectivity, and loss spectra are
  often presented
  as a standard set of outputs rather than as observables answering defined
  scientific questions);
- 需简要解释拓扑为何重要, 非平庸 Z2 不变量预示何种物理结果, 再引入宇称计算 (The introduction
  should also briefly explain why topology is important and what physical
  consequence is
  expected from a non-trivial Z2 invariant, before introducing the parity
  calculation).

Examiner 2 (DOCX 报告):

- 缺少独立的, 系统批判性的文献综述 (The principal weakness of this chapter, and indeed
  of the thesis as a whole, is the absence of a dedicated and comprehensive
  literature review);
- 需补充二维硼和铍基相关材料的关键研究综述, 指出现有成果与研究空白 (The candidate should
  include a discussion of the key studies that have been undertaken on related
  two-dimensional
  boron, and beryllium-based materials, highlighting the findings of previous
  researchers and
  identifying the gaps in knowledge that motivate the present work);
- 需综述文献中采用的理论与计算方法, 包括在同类体系中成功预测物理性质所用的理论层级
  (Such a review should also discuss the various theoretical and computational
  approaches
  that have been employed in the literature, including the levels of theory
  used successfully
  to predict properties of similar systems).

### 1.2 重构原则与篇幅目标

原有 src/introduction.tex 仅 74 行 (约 3 至 4 页), 缺乏文献深度与物理主线.
本次修改目标是将 Chapter 1 扩充重构为约 12 至 14 页的完整导论章:

- 新设独立的 Section 1.2 (Literature Review), 分系统综述 2D 硼基材料, 2D 铍基材料及计算理论层级;
- 建立明确的物理主线: 从外禀界面范德华工程 (Chapter 4), 到内禀复杂多中心键合与表面功能化 (Chapter 5),
  再到极端轻质金属极限下的晶格对称性与拓扑能带 (Chapter 6);
- 明确划分 Experimental reality (实验已有体系) 与 Theoretical proposals (理论预测);
- 专门设节阐明光学介电响应和 Z2 拓扑不变量的物理动机与可观测量意义;
- 在章末确立尖锐的研究空白 (Research Gaps) 和贯穿全篇的 Thesis Statement.

---

## 2. Chapter 1 重构提纲与小节规划

重构后的 Chapter 1 建议采用以下五个小节结构:

- Section 1.1: Background and Research Scope: Light-Element Xenes
  从后石墨烯时代的轻元素二维晶体出发, 阐述 B (Z=5) 与 Be (Z=4) 相比于 C (Z=6) 的独特性:
  缺电子多中心键合 vs. s-p 轨道杂化与强离域性; 提出调控自由度(界面堆叠, 维度截断, 氢化吸附).
- Section 1.2: Literature Review: 2D Boron, Beryllium, and Theoretical
  Methodologies
  - 1.2.1 Two-Dimensional Boron and Boron Carbide Systems (实验合成如衬底上硼烯 vs 独立理论
    相, o-B14 块体到低维);
  - 1.2.2 Two-Dimensional Beryllium Systems (从理论预言 alpha/beta 相到 Chahal 2023
    剥离实验, 遗留问题);
  - 1.2.3 Theoretical Approaches and Levels of Theory in Light-Element 2D
    Materials (PBE vs HSE06 vs GW/BSE, DFPT 与 EPW 超导, AIMD 热稳定性, 拓扑诊断方法);
  - 1.2.4 Critical Assessment: Experimental Status versus Theoretical
    Predictions (系统归类表).
- Section 1.3: Physical Motivations for Optical and Topological Observables
  - 1.3.1 Dielectric Response and Derived Optical Spectra as Physical Probes
    (介电函数实部/虚部, EELS 等离激元, 各向异性与非对角分量, 折射率/反射率/吸收);
  - 1.3.2 Band Topology and Physical Significance of the Z2 Invariant (无重原子强
    SOC 下的拓扑可行性, 边界态与量子自旋霍尔效应, 宇称诊断前提).
- Section 1.4: Central Motivation and Specific Research Gaps
  针对 Chapters 4, 5, 6 分别提炼 3 个未解研究空白, 给出本论文的核心论题.
- Section 1.5: Thesis Organisation and Synergistic Cohesion
  阐明从外禀界面(Ch4), 内禀多中心骨架(Ch5)到轻金属拓扑(Ch6)的三阶段递进主线, 概述各章内容.

---

## 3. 分节修改要点与英文候选文本

### 3.1 Section 1.1: Background and Research Scope: Light-Element Xenes

中文说明:
保留原 introduction.tex 开头关于石墨烯及二维材料重要性的论述, 但需从单纯的材料介绍提升到
轻元素轨道物理与键合特性的对比上. 明确指出碳的 sp2 蜂窝晶格虽然经典, 但零带隙与单一晶格结构
限制了功能扩展; 而硼 (Z=5, 2s2 2p1) 的缺电子性导致多中心键 (如 3c-2e 键), 产生极为丰富的同素异形体;
铍 (Z=4, 2s2) 作为最轻的碱土金属, 在低维下发生强烈的 s-p 杂化, 表现出不同于传统金属的独特性质.

英文候选文本:

```latex
\section{Background and Research Scope: Light-Element Xenes}
\label{sec:intro_background}

The isolation of monolayer graphene fundamentally transformed modern condensed
matter
physics and materials science~\cite{novoselov2004electric,geim2007rise}.
Beyond demonstrating
that strictly two-dimensional (2D) crystals can remain dynamically stable at
ambient conditions,
graphene revealed that reducing physical dimensions to the atomic scale
radically reshapes
electronic band dispersion, interfacial screening, and collective excitations.
The emergence of
massless Dirac fermions, ballistic electronic transport, and gate-tunable
carrier densities in
graphene established 2D materials as a premier testing ground for fundamental
quantum phenomena
and low-dimensional device concepts.

Despite these extraordinary properties, the gapless semimetallic band
structure of pristine
graphene presents an intrinsic bottleneck for switching devices and
optoelectronic applications
requiring distinct interband optical thresholds. This limitation stimulated
intensive exploration
into alternative monoelemental 2D lattices, broadly designated as
Xenes~\cite{molle2018silicene,
butler2013progress}. While initial efforts concentrated on heavier group-IV
counterparts such
as silicene, germanene, and stanene, atomically thin materials composed of the
lightest elements
in the periodic table---specifically boron ($Z=5$) and beryllium
($Z=4$)---govern an entirely
different regime of bonding physics and emergent electronic behavior.

The fundamental divergence among carbon, boron, and beryllium stems from their
valence electron
configurations and orbital hybridization:
\begin{itemize}
    \item Carbon ($2s^2 2p^2$) possesses four valence electrons, which
    naturally form classical,
    covalent $sp^2$ $\sigma$-bonds and delocalized $\pi$-systems within the
    planar honeycomb network.
    \item Boron ($2s^2 2p^1$), possessing one fewer valence electron than
    available bonding orbitals,
    is intrinsically electron-deficient. Unable to satisfy the conventional
    octet rule in a simple
    honeycomb lattice, boron resolves this deficiency through multicentre
    two-electron
    ($3c\text{--}2e$) bonding and hollow-hexagon configurations. This gives
    rise to a vast landscape
    of competing structural polymorphs, ranging from planar borophene networks
    with tunable vacancy
    concentrations to 3D networks built from icosahedra or pentagonal
    bipyramids.
    \item Beryllium ($2s^2$), as the lightest alkaline-earth element, exhibits
    a closed-shell divalent
    configuration in the free atom. In low-dimensional condensed phases,
    strong quantum confinement
    drives prominent $s\text{--}p$ orbital hybridization and electron
    delocalization, transforming
    beryllium into an ultralight metallic platform that can support unexpected
    electronic phases,
    unconventional lattice dynamics, and symmetry-protected topological bands
    without requiring
    heavy atoms.
\end{itemize}

Modulating the quantum ground states of these light-element 2D allotropes
requires targeted
physical and chemical strategies. Interlayer van der Waals engineering
provides an extrinsic
approach, where stacking light-element sheets modifies charge transfer, breaks
inversion symmetry,
and tunes optical dielectric screening without disrupting in-plane covalent
integrity. Conversely,
dimensional reduction of complex 3D allotropes and surface functionalization
(such as hydrogen
chemisorption) represent intrinsic mechanisms that alter coordination numbers,
saturate dangling
bonds, and induce electronic transitions between metallic, semiconducting,
magnetic, and
superconducting states.
```

---

### 3.2 Section 1.2: Literature Review: 2D Boron, Beryllium, and Theoretical Methodologies

中文说明:
本节直接回应 Examiner 2 提出的 dedicated and comprehensive literature review 以及
Examiner 1 提出的
separate established experimental systems from theoretical proposals.
建议细分为四个小节:

1. 2D 硼基材料综述: 区分衬底外延硼烯(实验已证实)与独立自由悬浮相/复合物硼碳化物(理论预言), 并介绍 o-B14 复杂块体结构及其降维背景;
2. 2D 铍基材料综述: 梳理理论预言的 alpha/beta 相, 重点评述 Chahal 等人 2023 年利用超声化学剥离实现的 beryllene
   实验进展及其局限;
3. 理论与计算层级述评: 评价 PBE, HSE06 杂化泛函在能带与带隙中的表现, 阐述 DFPT + EPW 在电声耦合超导中的适用性, 以及
   AIMD 热稳定性的评估标准;
4. 批判性反思与归纳表: 以清晰对比表格区分实验事实与理论预言.

英文候选文本:

```latex
\section{Literature Review: 2D Boron, Beryllium, and Theoretical
Methodologies}
\label{sec:intro_lit_review}

\subsection{Two-Dimensional Boron and Boron Carbide Systems}
\label{subsec:lit_boron}

The structural and electronic versatility of boron has inspired extensive
theoretical and
experimental investigations. Early theoretical calculations predicted that
planar boron sheets
require a mixture of triangular coordination and hexagonal hollows to
stabilize the bonding
network by balancing bonding and antibonding
states~\cite{tang2007novel,yang2008boron}. The
experimental synthesis of borophene was subsequently achieved via molecular
beam epitaxy (MBE) on
metallic substrates under ultra-high vacuum conditions, notably on Ag(111)
surfaces~\cite{mannix2015synthesis,
feng2016experimental}, and later on Al(111) and
Cu(111)~\cite{li2018realization,wu2019experimental}.
These synthesized phases (such as the $\beta_{12}$ and $\chi_3$ sheets)
confirmed the metallic
nature of monolayer borophenes and demonstrated anisotropic electronic
transport and optical transparency.

However, an important distinction must be maintained between
substrate-supported borophene and
freestanding boron layers. Experimental borophenes exhibit significant
substrate-mediated charge
transfer and interfacial hybridization, which stabilize specific vacancy
patterns that might
otherwise be metastable in isolated sheets. The experimental realization of
freestanding, pristine
borophene remains challenging because atomic boron sheets possess high surface
energies and readily
oxidize or form bulk networks in the absence of passivating interfaces or
vacuum encapsulation.

Beyond pure borophene, incorporating carbon into 2D boron networks yields
stoichiometric boron
carbides, such as $\mathrm{BC}_3$ and
$\mathrm{B}_4\mathrm{C}_3$~\cite{yan2014two,zhao2015predicting}.
Unlike metallic borophene, these binary honeycomb derivatives exhibit
semiconducting behavior with
sizeable band gaps, combining chemical stability with high carrier mobilities.
Combining graphene
with borophene and boron carbides into vertical van der Waals heterostructures
represents a
promising route for designing tunable electronic interfaces and Schottky
barriers. While isolated
studies have addressed specific bilayer
geometries~\cite{hou2021borophene,liu2019borophene},
a systematic comparative investigation spanning structural energetics,
interfacial dipole formation,
and full-tensor optical dielectric response using consistent levels of theory
has been lacking.

In parallel with planar allotropes, complex 3D boron structures offer an
untapped reservoir for
dimensional engineering. Elemental boron forms multiple bulk allotropes
dominated by interconnected
icosahedral or polyhedral clusters, including $\alpha$-rhombohedral,
$\beta$-rhombohedral, and
orthorhombic phases~\cite{oganza2009novel}. Among them, the orthorhombic boron
allotrope
$o\text{-}\mathrm{B}_{14}$, composed of edge-sharing pentagonal bipyramids,
displays an unusual
three-dimensional coordination network that exhibits notable mechanical
hardness and electronic
complexity~\cite{zhao2012novel}. Prior to the work in this thesis,
investigations of $o\text{-}\mathrm{B}_{14}$
were strictly confined to its bulk phase. Whether this pentagonal bipyramidal
framework could be
cleaved into stable 2D nanosheets, and how surface truncation and chemical
termination would modify
its electronic ground state, magnetic ordering, and electron--phonon
interactions, remained completely
unexplored.

\subsection{Two-Dimensional Beryllium Systems}
\label{subsec:lit_beryllene}

As the lightest alkaline-earth metal, beryllium has historically attracted
attention in aerospace
and nuclear applications due to its high strength-to-weight ratio, high
melting point, and neutron
moderation capability. In the bulk, beryllium crystallizes in a close-packed
hexagonal close-packed
(hcp) structure at ambient conditions, undergoing a transition to a
body-centered cubic (bcc) phase
at high temperatures ($T > 1527$~K)~\cite{evans1984beryllium}.

The transition of beryllium into the 2D regime is a recent development.
Initial first-principles
calculations explored planar hexagonal ($\alpha$-beryllene) and buckled or
bilayer ($\beta$-beryllene)
phases, predicting that low-dimensional beryllium remains metallic and
supports unusually high Fermi
velocities and anisotropic mechanical
characteristics~\cite{li2023coexistence,sun2020beryllene}.
Vibrational and thermal transport calculations further suggested that
monolayer beryllium allotropes
could host unconventional phonon transport channels driven by light atomic
mass and strong interatomic
force constants~\cite{chowdhury2024unusual}.

A significant milestone was reached in 2023, when Chahal \textit{et al.}
reported the first experimental
synthesis of beryllene via sonochemical liquid-phase exfoliation from
commercial beryllium powder
dispersed in organic solvents~\cite{chahal2023beryllene}. Transmission
electron microscopy and Raman
spectroscopy confirmed the formation of multi-layer and few-layer metallic
beryllium flakes,
demonstrating room-temperature stability in ambient liquid environments.

Despite this experimental breakthrough, several fundamental questions remain
open in the physics of
2D beryllium:
\begin{enumerate}
    \item Structural exploration has been largely confined to monolayer
    $\alpha$ and bilayer $\beta$
    arrangements derived from the hcp lattice. Whether alternative
    coordination motifs---such as
    multilayers cleaved from or inspired by the cubic bcc phase---can achieve
    dynamical stability
    in the 2D limit has not been addressed.
    \item While pristine beryllenes are consistently metallic, the response of
    2D beryllium networks
    to surface functionalization remains largely uncharacterized. In
    particular, it is unknown whether
    hydrogenation can passivate surface states to open wide electronic band
    gaps, or whether it preserves
    itinerant metallic conduction depending on the parent lattice geometry.
    \item The intersection of light-element physics and band topology in
    beryllene represents an
    emerging frontier. Conventional topological phases rely on heavy elements
    with strong atomic
    spin--orbit coupling. Recent theoretical frameworks suggest that band
    inversion driven by spatial
    inversion symmetry and orbital hybridization can generate topological
    states even in light-element
    systems~\cite{derriche2024light}. However, a concrete realization and
    topological characterization
    of non-trivial invariants in pristine and functionalized beryllene
    allotropes has remained absent.
\end{enumerate}

\subsection{Theoretical Approaches and Levels of Theory in Light-Element 2D
Physics}
\label{subsec:lit_methods}

Predictive modelling of light-element low-dimensional systems requires careful
selection of
first-principles methodologies. Because physical observables can be sensitive
to the treatment of
electron exchange and correlation, it is essential to review the capabilities
and limitations of
different levels of theory applied to these systems:

\begin{itemize}
    \item \textbf{Semilocal versus Hybrid Exchange-Correlation Functionals:}
    The standard Generalized Gradient Approximation (GGA), such as the
    Perdew--Burke--Ernzerhof (PBE)
    functional~\cite{perdew1996generalized}, accurately describes structural
    parameters, cohesive
    energies, and phonon dispersions in light-element crystals. However, GGA
    functionals suffer from
    spurious self-interaction errors and unphysical charge delocalization,
    which routinely underestimate
    semiconductor band gaps and can misidentify narrow-gap semiconductors as
    semimetals or metals.
    Screened hybrid functionals, predominantly
    HSE06~\cite{heyd2003hybrid,krukau2006influence},
    incorporate a fraction of non-local exact Hartree--Fock exchange at short
    range, effectively
    counteracting self-interaction errors and delivering reliable electronic
    band gaps and optical
    transition thresholds. While many-body perturbation theory within the $GW$
    approximation and the
    Bethe--Salpeter equation (BSE) provides the benchmark for quasiparticle
    band structures and
    excitonic effects, its computational cost is often prohibitive for large
    supercells, heterostructures,
    and extensive k-point samplings required for optical integration.
    \item \textbf{Dispersion Corrections for Heterostructures:}
    Standard semilocal DFT cannot capture non-local London dispersion forces
    that govern interlayer
    binding in van der Waals heterostructures. Semi-empirical dispersion
    corrections, such as the
    DFT-D3 method of Grimme~\cite{grimme2010consistent}, are essential to
    predict accurate interlayer
    equilibrium distances, binding energies, and registry energetics across
    graphene-boron interfaces.
    \item \textbf{Dynamical Stability and Anharmonicity:}
    In 2D materials, mechanical and dynamical stability cannot be inferred
    solely from negative
    cohesive or formation energies. Harmonic phonon dispersion curves
    calculated via the
    finite-displacement method (Phonopy)~\cite{togo2015first} or
    Density-Functional Perturbation
    Theory (DFPT)~\cite{baroni2001phonons} are required to verify the absence
    of imaginary (negative)
    frequencies across the entire Brillouin zone at 0~K. To complement
    harmonic analysis,
    \textit{ab initio} molecular dynamics (AIMD) simulations in the canonical
    ($NVT$) ensemble test the
    thermal persistence of atomic frameworks against thermal fluctuations at
    finite temperatures
    ($T = 300\text{--}400$~K).
    \item \textbf{Electron--Phonon Coupling and Superconductivity:}
    Predicting phonon-mediated superconductivity requires the microscopic
    determination of the
    electron--phonon matrix elements across the Fermi surface. DFPT combined
    with maximally localized
    Wannier function interpolation, as implemented in the EPW
    code~\cite{ponce2016epw,
    giannozzi2009quantum}, permits ultra-dense Brillouin-zone sampling of the
    Eliashberg spectral
    function $\alpha^2 F(\omega)$. This framework enables numerical solutions
    of both the semi-empirical
    Allen--Dynes modified McMillan equation and the fully anisotropic
    Migdal--Eliashberg equations.
    \item \textbf{Topological Parity Invariants:}
    In centrosymmetric 2D crystals with time-reversal symmetry, the
    topological $\mathbb{Z}_2$ invariant
    can be determined rigorously from the parity eigenvalues of all occupied
    Kramers pairs at the
    four time-reversal invariant momentum (TRIM) points in the 2D Brillouin
    zone, following the Fu--Kane
    parity formula~\cite{fu2007topological}.
\end{itemize}

\subsection{Critical Assessment: Experimental Realities versus Theoretical
Predictions}
\label{subsec:lit_critical_status}

To establish a clear boundary between established physical facts and
predictive computational
discoveries, Table~\ref{tab:experimental_vs_theoretical} summarizes the
research status of the
materials investigated in this thesis.

\begin{table}[!htbp]
\centering
\caption{Classification of materials investigated in this thesis into
established experimental systems and theoretical predictions.}
\label{tab:experimental_vs_theoretical}
\begin{adjustbox}{width=0.98\textwidth}
\begin{tabular}{llll}
\hline
Material System & Structural Description & Status & Key References \\
\hline
Graphene & Honeycomb carbon monolayer & Established experiment &
     Novoselov \textit{et al.}~\cite{novoselov2004electric} \\
Borophene ($\beta_{12}$, $\chi_3$) & Triangular/hexagonal B sheets &
     Substrate-supported experiment &
     Mannix \textit{et al.}~\cite{mannix2015synthesis},
     Feng \textit{et al.}~\cite{feng2016experimental} \\
Beryllene flakes & Multilayer/few-layer Be & Exfoliated liquid experiment &
     Chahal \textit{et al.}~\cite{chahal2023beryllene} \\
Bulk $o\text{-}\mathrm{B}_{14}$ & 3D pentagonal bipyramid boron &
     Synthesized bulk experiment &
     Oganov \textit{et al.}~\cite{oganza2009novel},
     Zhao \textit{et al.}~\cite{zhao2012novel} \\
\hline
$\mathrm{BC}_3$, $\mathrm{B}_4\mathrm{C}_3$ monolayers &
     Semiconducting boron carbide sheets & Theoretical prediction &
     Yan \textit{et al.}~\cite{yan2014two},
     Zhao \textit{et al.}~\cite{zhao2015predicting} \\
Graphene-boron heterostructures &
     Bilayers (Gr-Borophene, Gr-$\mathrm{BC}_3$,
     Gr-$\mathrm{B}_4\mathrm{C}_3$) &
     Predictive design (Chapter~\ref{cha:project_bilayers}) &
     This thesis (Niu \textit{et al.}~\cite{niu2024electronic}) \\
2D $o\text{-}\mathrm{B}_{14}$ sheets &
     Monolayer, bilayer, hydrogenated bilayer &
     Predictive design (Chapter~\ref{cha:project_boron}) & This thesis \\
Cubic trilayer beryllene & Non-hexagonal bcc-cleaved Be trilayer &
     Predictive design (Chapter~\ref{cha:project_beryllene}) & This thesis \\
Hydrogenated beryllenes & 2H-$\alpha$, 1H-$\beta$, 2H-$\beta$ phases &
     Predictive design (Chapter~\ref{cha:project_beryllene}) & This thesis \\
\hline
\end{tabular}
\end{adjustbox}
\end{table}

This distinction is crucial: while Chapters~\ref{cha:project_bilayers},
\ref{cha:project_boron},
and \ref{cha:project_beryllene} build upon established experimental
foundations, the specific
heterojunction architectures, truncated $o\text{-}\mathrm{B}_{14}$ nanosheets,
cubic trilayer
beryllene, and hydrogenated phases represent computational predictions. Their
reported stabilities
reflect energetic preference relative to reference allotropes, harmonic
dynamical stability, and
short-time thermal persistence, which provide essential physical guidance for
future experimental
synthesis.
```

---

### 3.3 Section 1.3: Physical Motivations for Optical and Topological Observables

中文说明:
本节直接回应 Examiner 1 的两点核心批评:

1. 光学性质动机不明确, 看起来像是一套标准计算流程而非回答特定科学问题;
2. 拓扑与 Z2 不变量的物理意义缺失, 在给出宇称乘积公式前未解释为什么轻元素中拓扑重要以及非平庸 Z2 会产生何种物理后果.

英文候选文本:

```latex
\section{Physical Motivations for Optical and Topological Observables}
\label{sec:intro_observables}

Throughout this thesis, optical response spectra and topological indices are
evaluated not as
routine post-processing outputs, but as decisive physical observables designed
to resolve specific
questions regarding electronic structure, symmetry breaking, and transport
protection.

\subsection{Optical Response and Dielectric Properties as Physical Probes}
\label{subsec:opt_observables_motivation}

In low-dimensional materials, the linear optical response provides direct
spectroscopic access to
both single-particle interband transitions and collective electronic modes.
Within the framework of
independent-particle linear response, all derived optical quantities originate
from the complex
frequency-dependent dielectric tensor, $\varepsilon_{\alpha\beta}(\omega) =
\varepsilon_1(\omega) + \ii \varepsilon_2(\omega)$.
Each optical spectrum calculated in this thesis addresses a defined physical
inquiry:

\begin{itemize}
    \item \textbf{Imaginary Part of the Dielectric Function
    ($\varepsilon_2$):}
    The imaginary component directly reflects the joint density of states
    weighted by optical dipole
    transition matrix elements between occupied valence and unoccupied
    conduction bands. It identifies
    fundamental optical band gaps, interband absorption thresholds, and van
    Hove singularities.
    Comparing $\varepsilon_2(\omega)$ calculated with PBE and HSE06 elucidates
    how non-local exchange
    modifies quasiparticle shifts across visible and ultraviolet spectral
    ranges.
    \item \textbf{Real Part of the Dielectric Function ($\varepsilon_1$) and
    Zero-Crossings:}
    The real component represents the dispersive screening of the material.
    Zero-crossings of
    $\varepsilon_1(\omega)$ with positive slope ($\dif \varepsilon_1 / \dif
    \omega > 0$) define the
    energies of longitudinal collective electron excitations (plasmons). In
    metallic or semimetallic
    allotropes, regions where $\varepsilon_1(\omega) < 0$ identify frequency
    windows where metallic
    reflection and screened plasma behavior dominate.
    \item \textbf{Off-Diagonal Dielectric Components ($\varepsilon_{xy}$):}
    In isotropic or highly symmetric hexagonal systems, off-diagonal
    dielectric tensor components
    vanish identically. Evaluating $\varepsilon_{xy}(\omega)$ directly tests
    whether structural
    hetero-interfaces (such as Graphene-$\mathrm{B}_4\mathrm{C}_3$) break
    spatial mirror and rotational
    symmetries, revealing in-plane optical anisotropy and potential optical
    activity.
    \item \textbf{Electron Energy-Loss Spectrum (EELS):}
    Defined as $L(\omega) = -\mathrm{Im}[1/\varepsilon(\omega)] =
    \varepsilon_2 / (\varepsilon_1^2 + \varepsilon_2^2)$,
    the energy-loss function provides the direct observable measured in
    transmission electron
    microscopy EELS experiments. Prominent peaks in $L(\omega)$ corresponding
    to the zero-crossings
    of $\varepsilon_1(\omega)$ provide unambiguous identification of volume
    and surface plasmon
    resonances, distinguishing collective electronic modes from
    single-particle interband damping.
    \item \textbf{Reflectivity, Absorption, and Refractive Indices:}
    The derived absorption coefficient $\alpha(\omega)$, reflectivity
    $R(\omega)$, refractive index
    $n(\omega)$, and extinction coefficient $\kappa(\omega)$ connect
    microscopic band transitions to
    macroscopic electromagnetic behavior. In 2D materials, evaluating in-plane
    versus out-of-plane
    components reveals directional optical transparency, birefringence, and
    polarization-dependent
    filtering capabilities across solar, visible, and near-ultraviolet
    windows.
\end{itemize}

\subsection{Emergent Band Topology and the Significance of the $\mathbb{Z}_2$
Invariant}
\label{subsec:topo_motivation}

Topological phases of matter have fundamentally altered our understanding of
electronic structure.
In two dimensions, a non-trivial topological insulator (or Quantum Spin Hall
insulator) is characterized
by an insulating (or gapped) bulk electronic state accompanied by gapless,
one-dimensional edge states.
These edge states exhibit spin-momentum locking, where electrons with opposite
spins propagate in
opposite directions along the boundary. Protected by time-reversal symmetry,
these helical edge
channels are completely immune to elastic backscattering from non-magnetic
impurities and crystalline
defects, offering a pathway toward dissipationless electronic transport and
quantum information
platforms.

In conventional topological materials (such as $\mathrm{Bi}_2\mathrm{Se}_3$,
$\mathrm{Bi}_2\mathrm{Te}_3$,
and stanene), non-trivial band topology relies on heavy elements possessing
massive intrinsic
spin--orbit coupling (SOC), which scales roughly as the fourth power of the
atomic number ($Z^4$).
Strong atomic SOC forces an energetic inversion between valence and conduction
bands of opposite
spatial parity.

In light-element materials ($Z \le 5$), atomic SOC is intrinsically weak
(typically on the order
of micro- to milli-electronvolts). However, band topology can still emerge
through an alternative
physical mechanism: \textit{symmetry-enforced orbital parity inversion}. In
specific crystal
symmetries, strong crystalline bonding and low-dimensional confinement can
push orbitals of different
spatial symmetries across one another at high-symmetry points in the Brillouin
zone. Even with tiny
relativistic SOC, the symmetry-dictated crossing gaps out, producing an
inverted band order that
endows the electronic ground state with a mathematically non-trivial
topological index.

For centrosymmetric 2D crystals invariant under time reversal, the topological
classification is
governed by the $\mathbb{Z}_2$ invariant ($\nu \in \{0, 1\}$). As formulated
by Fu and Kane~\cite{fu2007topological},
the $\mathbb{Z}_2$ index $\nu$ can be computed by evaluating the spatial
parity eigenvalues
$\xi_{2m}(\Gamma_i) = \pm 1$ of all occupied Kramers pairs $m$ at the four
time-reversal invariant
momentum (TRIM) points $\Gamma_i$ in the 2D Brillouin zone:
\begin{equation}
    (-1)^\nu = \prod_{i=1}^4 \prod_{m=1}^{N_{\mathrm{occ}}} \xi_{2m}(\Gamma_i)
    \label{eq:intro_fu_kane}
\end{equation}
A product yielding $(-1)^\nu = -1$ establishes a topologically non-trivial
phase ($\nu = 1$),
demonstrating the existence of topologically protected edge channels, whereas
$(-1)^\nu = +1$
denotes a topologically trivial insulator ($\nu = 0$).

Introducing this topological framework in Chapter~\ref{cha:project_beryllene}
allows us to explore
whether purely elemental beryllium lattices can realize symmetry-driven
non-trivial band topology
in the complete absence of heavy atoms.
```

---

### 3.4 Section 1.4: Central Motivation and Specific Research Gaps

中文说明:
本节直接回应两份报告共同指出的核心问题: 缺乏清晰尖锐的研究空白 (sharp research gap).
必须列举三个明确的科研空白, 分别对应 Chapters 4, 5, 6, 并指出全篇论文共同解决的核心科学议题.

英文候选文本:

```latex
\section{Central Motivation and Specific Research Gaps}
\label{sec:intro_gaps}

Despite substantial progress in the physics of graphene and related 2D
crystals, light-element
monolayers based on boron and beryllium represent an underdeveloped domain
where structural
multicentre bonding, low coordination, and quantum confinement intersect. The
overarching scientific
objective of this thesis is to elucidate how atomic arrangement, dimensional
truncation, and
surface functionalization dictate emergent quantum properties---ranging from
semiconductivity and
magnetism to superconductivity, anisotropic plasmonics, and band topology---in
ultralight 2D materials.

Specifically, this doctoral research addresses three well-defined research
gaps in the literature:

\begin{enumerate}
    \item \textbf{Research Gap 1: Interfacial Screening and Symmetry-Broken
    Optical Activity in Graphene-Boron Heterostructures (addressed in
    Chapter~\ref{cha:project_bilayers}).}
    While graphene has been successfully integrated with traditional hexagonal
    boron nitride ($\mathrm{hBN}$)
    and transition-metal dichalcogenides, heterostructures formed by combining
    graphene with metallic
    borophene or semiconducting boron carbides ($\mathrm{BC}_3$,
    $\mathrm{B}_4\mathrm{C}_3$) remain
    insufficiently mapped. It is unknown how varying the boron-to-carbon ratio
    and atomic vacancy
    patterns across the van der Waals interface modifies interfacial charge
    transfer, controls Schottky
    barrier heights, and influences both diagonal and off-diagonal optical
    dielectric tensor components.
    A rigorous, comparative first-principles evaluation using both semilocal
    PBE and hybrid HSE06
    functionals is needed to resolve these questions.

    \item \textbf{Research Gap 2: Quantum Multiphase Behavior in Dimensionally
    Reduced Penta-Bipyramid Boron (addressed in
    Chapter~\ref{cha:project_boron}).}
    Prior investigations of complex elemental boron have focused almost
    exclusively on bulk allotropes
    or flat, planar borophene monolayers. The low-dimensional physics of the
    orthorhombic $o\text{-}\mathrm{B}_{14}$
    phase, characterized by interconnected pentagonal bipyramids, has remained
    unexplored. It is an open
    question whether the $o\text{-}\mathrm{B}_{14}$ framework can maintain
    dynamical stability when thinned
    to the 2D bilayer and monolayer limits, whether dimensional truncation
    unquenches magnetic ordering,
    and whether surface passivating with hydrogen can induce strong
    electron--phonon coupling capable of
    supporting high-$T_c$ conventional superconductivity.

    \item \textbf{Research Gap 3: Structural Exploration, Functionalization,
    and Symmetry-Enforced Topology in 2D Beryllium (addressed in
    Chapter~\ref{cha:project_beryllene}).}
    Following the recent experimental isolation of beryllene flakes, research
    has been limited to
    elementary planar $\alpha$ and buckled $\beta$ geometries. Crucial
    structural and physical questions
    remain unaddressed: Can elemental beryllium stabilize in non-hexagonal
    layered configurations,
    such as multi-layer allotropes derived from its high-temperature bcc bulk
    phase? How does hydrogen
    chemisorption alter the electronic ground state across different beryllium
    geometries? And most
    fundamentally, can an elemental light-metal such as beryllium host a
    non-trivial topological
    $\mathbb{Z}_2$ invariant driven purely by crystal symmetry and orbital
    parity inversion without
    relying on heavy-element spin--orbit coupling?
\end{enumerate}

By resolving these three gaps, this thesis establishes a unified
materials-by-design framework for
engineering electronic, optical, and quantum ground states in light-element
Xenes.
```

---

### 3.5 Section 1.5: Thesis Organisation and Synergistic Cohesion

中文说明:
本节直接回应 Examiner 1 的批评: hopping between different materials and lack of
relationship between them.
需将后文各章用一条严密的逻辑主线串联起来, 形成三阶段递进式叙事:

- 第一阶段(外禀界面调控): 从石墨烯出发, 通过外禀范德华堆垛杂化缺电子硼体系, 探索界面电荷与对称性破缺对光学各向异性的调控(Chapter 4);
- 第二阶段(内禀复杂多中心键合): 深入到复杂单质硼 o-B14 结构内部, 通过维度降低(块体到双层, 单层)和表面氢化, 在同一硼相中探索从反铁磁半
  导体到
  24.3 K 超导电性的相转变(Chapter 5);
- 第三阶段(极轻金属极限与非平庸拓扑): 推向周期表最轻的金属元素铍, 探索非常规堆叠相(立方三层铍), 全氢化对金属-半导体相变的调控, 以及轻元素中
  由晶格对
  称性诱导的 Z2 拓扑非平庸态(Chapter 6).

英文候选文本:

```latex
\section{Thesis Organisation and Synergistic Cohesion}
\label{sec:intro_organisation}

To address the research gaps outlined above, the research presented in this
thesis is structured
into a cohesive, three-stage investigative journey across the domain of
light-element 2D materials,
supported by foundational methodological chapters. The thesis is organised as
follows:

\begin{itemize}
    \item \textbf{Chapter~\ref{cha:fundamentals_a} (Fundamentals
    \textRoman{1}: Many-Body Quantum Physics and DFT)}
    reviews the quantum mechanical many-body problem and the theoretical
    foundations of density
    functional theory. It develops the Hohenberg--Kohn theorems, the
    Kohn--Sham auxiliary single-particle
    scheme, and the physical mechanisms underlying local, semilocal (PBE), and
    screened hybrid (HSE06)
    exchange-correlation functionals. It concludes with a practical
    computational methodology roadmap
    summarizing convergence protocols, phonon perturbation theory, molecular
    dynamics, and electron--phonon
    workflows implemented throughout the research chapters.

    \item \textbf{Chapter~\ref{cha:fundamentals_b} (Fundamentals
    \textRoman{2}: Linear Optical Response)}
    formulates the electrodynamic response of condensed matter starting from
    Maxwell's equations.
    It details the microscopic derivation of the frequency-dependent
    dielectric tensor, Kramers--Kronig
    relations, and the exact physical expressions for derived optical spectra,
    providing the analytical
    foundation for evaluating light-matter interactions and plasmonic modes in
    2D systems.

    \item \textbf{Chapter~\ref{cha:project_bilayers} (Stage 1: Extrinsic Van
    der Waals Heterostructures of Graphene and Boron Systems)}
    examines interfacial coupling in bilayer heterostructures formed by
    stacking graphene onto borophene
    and 2D boron carbides ($\mathrm{BC}_3$ and $\mathrm{B}_4\mathrm{C}_3$). By
    systematically comparing
    isolated monolayers against bilayer assemblies using PBE and HSE06, this
    study resolves how weak
    van der Waals interactions tune electronic band alignments, modify
    Schottky barrier profiles, and
    induce in-plane optical anisotropy and low-energy plasmons without
    degrading the Dirac cone of graphene.

    \item \textbf{Chapter~\ref{cha:project_boron} (Stage 2: Intrinsic
    Multicentre Bonding and Quantum Phases in Penta-Bipyramidal Boron)}
    progresses from extrinsic interface engineering to the intrinsic quantum
    behavior of the complex
    orthorhombic boron allotrope $o\text{-}\mathrm{B}_{14}$. By tracking
    dimensional reduction from bulk
    crystals to 2D bilayers and monolayers, this investigation reveals how
    pentagonal bipyramidal networks
    host antiferromagnetic ordering in the monolayer. Furthermore, it
    demonstrates that surface hydrogen
    passivation restructures the Fermi surface and activates high-frequency
    boron-hydrogen bond-stretching
    phonons, driving conventional phonon-mediated superconductivity with $T_c
    \approx 24.3$~K.

    \item \textbf{Chapter~\ref{cha:project_beryllene} (Stage 3:
    Symmetry-Driven Topology and Low-Dimensional Beryllium Phases)}
    extends the exploration to the ultimate limit of light divalent metals by
    investigating pristine
    and hydrogen-functionalized beryllene allotropes. In addition to
    characterizing known hexagonal
    $\alpha$ and $\beta$ phases, this chapter proposes a dynamically stable
    cubic trilayer beryllene
    allotrope derived from the high-temperature bcc phase. It demonstrates
    that surface hydrogenation
    drives a metal-to-semiconductor transition in $\alpha$-beryllene while
    preserving metallic conduction
    in $\beta$-based networks. Crucially, parity analysis of the
    spin-orbit-coupled electronic states
    demonstrates the emergence of a non-trivial topological $\mathbb{Z}_2$
    invariant in cubic trilayer
    beryllene, establishing an elemental light-metal platform for
    symmetry-enforced band topology.

    \item \textbf{Chapter~\ref{cha:conclusion_outlook} (Conclusions and
    Outlook)}
    synthesizes the principal physical findings across all three stages,
    provides a critical assessment
    of computational approximations and theoretical limitations (such as
    self-interaction errors and
    finite AIMD time scales), clearly delineates experimental realities from
    theoretical predictions,
    and proposes concrete avenues for future experimental synthesis and
    many-body theoretical refinement.
\end{itemize}
```

---

## 4. 文献补充与核查项 (Literature Additions Checklist)

为支撑 Section 1.2 的系统性文献综述, 需在 `thesis.bib` 中核对并确认以下参考文献的 bibkey 是否完整:

1. 硼烯实验合成:
   - `mannix2015synthesis`: Mannix et al., Science 350, 1513 (2015)
     (Ag(111) 上合成硼烯). 已在库中.
   - `feng2016experimental`: Feng et al., Nat. Chem. 8, 563 (2016)
     (Ag(111) 上合成 beta12 和 chi3 硼烯). 已在库中.
   - `li2018realization`: Li et al., Adv. Mater. 30, 1707077 (2018)
     (Al(111) 衬底上的硼烯). 需核查或补充 bib entry.
   - `wu2019experimental`: Wu et al., Nat. Commun. 10, 1684 (2019)
     (Cu(111) 衬底上的大面积硼烯). 需核查或补充 bib entry.
2. 硼碳化物理论预测:
   - `yan2014two`: Yan et al., J. Phys. Chem. C 118, 14068 (2014)
     (预测二维 BC3 半导体). 需核对 bibkey.
   - `zhao2015predicting`: Zhao et al., Nanoscale 7, 7207 (2015)
     (预测二维 B4C3). 需核对 bibkey.
3. 块体 o-B14 实验与理论:
   - `oganza2009novel`: Oganov et al., Nature 457, 863 (2009)
     (高压下新型超硬单质硼及 o-B14 相关相). 已在库中或核查拼写.
   - `zhao2012novel`: Zhao et al., Phys. Rev. Lett. 109, 175502 (2012)
     (o-B14 晶体结构与电子性质). 需核对 bibkey.
4. 二维铍与超导/拓扑进展:
   - `chahal2023beryllene`: Chahal et al., npj 2D Mater. Appl. 7, 55 (2023)
     (超声化学剥离实验). 已在库中.
   - `li2023coexistence`: Li et al., Mater. Today Phys. 38, 101257 (2023)
     (beryllene 超导与拓扑共存). 已在库中.
   - `derriche2024light`: Derriche et al., Nano Lett. 24, 3811 (2024)
     (轻元素晶格拓扑保护态). 已在库中.
   - `fu2007topological`: Fu and Kane, Phys. Rev. B 76, 045302 (2007)
     (时间反演不变系统宇称乘积拓扑指标). 已在库中.
5. 计算方法经典文献:
   - `grimme2010consistent`: Grimme et al., J. Chem. Phys. 132, 154104 (2010)
     (DFT-D3 范德华修正). 需核对 bibkey.
   - `ponce2016epw`: Ponce et al., Comput. Phys. Commun. 209, 116 (2016)
     (EPW 代码与 Wannier 插值). 已在库中.
   - `baroni2001phonons`: Baroni et al., Rev. Mod. Phys. 73, 515 (2001)
     (DFPT 综述). 已在库中.

---

## 5. 跨章回查与依赖项登记 (Cross-Chapter Tracking)

在修改 Chapter 1 时涉及后文研究章节的若干结论和参数, 在此登记并在后续章节修改中逐一闭环:

- 回查项 1 (关联 Chapter 5):
  Chapter 1 候选文本中提到 monolayer o-B14 的基态为 antiferromagnetic (AFM).
  需在修改 Chapter 5 时最终确认: Monolayer 基态到底是 AFM 半导体还是金属?
  若 Chapter 5 确认其为微带隙 (0.105 eV) AFM 半导体, Chapter 1 文本保持一致;
  若 Chapter 5 对光学讨论改用非自旋极化态, 需在 Chapter 1 与 Chapter 5 同步注明.
- 回查项 2 (关联 Chapter 5):
  Chapter 1 候选文本中提到氢化双层 o-B14 的超导临界转变温度为 Tc 约 24.3 K (在部分正文处为 28.2 K).
  需在 Chapter 5 超导小节最终核算 Allen-Dynes 与各向异性 Migdal-Eliashberg 结果,
  确保 Chapter 1, Chapter 5 与 Abstract, Conclusion 中引用的数值完全一致.
- 回查项 3 (关联 Chapter 6):
  Chapter 1 候选文本中将 cubic trilayer beryllene 定性为具有 non-trivial Z2 topological
  invariant.
  Examiner 1 尖锐指出该相在后文被描述为 metallic.
  需在修改 Chapter 6 时根据真实能带结构落实最终策略:
  如果 SOC 在全局打开了连续直接带隙 (或属于微费米面拓扑半金属), 需在 Chapter 6 补全带隙表,
  Chapter 1 的宇称论述即可站稳; 如果无法论证能隙闭合, 需同步微调 Chapter 1 的拓扑表述.
- 回查项 4 (关联 Chapter 4):
  Table 1.1 中引用的合作发表论文 Niu et al. (2024), 需在 Chapter 4 章首的作者贡献声明中保持一致.

---

## 6. 针对评审报告 Chapter 1 的正式答复信草案 (Formal Reply Draft)

此草案可在论文全部修改完成后, 整合入 report/reply_to_examiners.md.

```markdown

### Response to Examiner 1, Comment 1 & 2 (Scope and Cohesion)

Examiner's Comment:
The thesis-level research position is nevertheless not sufficiently clear: the
early literature review does not lead to a sharp research gap or central
motivation... The rest chapters look like hopping between different materials
and there is a lack of relationship between them. Chapter 1 provides useful
background but reads more as a broad survey than as a focused argument for the
thesis. It should explain why graphene-based boron systems, boron phases, and
beryllene belong to one thesis, what unresolved question each chapter
addresses,
and how the studies collectively support one conclusion. The literature should
be used critically to separate established experimental systems from
theoretical proposals and to identify the research gap. The motivation for
calculating optical properties is also not sufficiently clear... The
introduction should also briefly explain why topology is important and what
physical consequence is expected from a non-trivial Z2 invariant, before
introducing the parity calculation.

Author's Response:
We sincerely thank Examiner 1 for this constructive critique, which has guided
a
major structural revision of Chapter 1. The chapter has been substantially
expanded from 4 pages to [x] pages to establish a sharp, cohesive research
paradigm. Specifically:
1. Unifying Scientific Narrative: Section 1.1 has been rewritten to explicitly
connect graphene-boron heterostructures, complex boron allotropes, and
beryllenes under the unifying theme of light-element Xenes (Z=4, 5). We
clarify
how moving from carbon (2s2 2p2) to electron-deficient boron (2s2 2p1) and
closed-shell divalent beryllium (2s2) departs from planar sp2 bonding,
activating multicentre bonds, s-p orbital hybridization, and
symmetry-protected states.
2. Dedicated Literature Review and Critical Demarcation: In Section 1.2, we
provide a comprehensive review of 2D boron and beryllium allotropes, alongside
theoretical methodologies. We explicitly separate established experimental
systems (such as epitaxial borophene on Ag(111) and sonochemically exfoliated
beryllene flakes) from theoretical predictions, summarized clearly in
Table 1.1.
3. Physical Motivations for Optical and Topological Observables: Section 1.3
has been newly added. It details why optical spectra (dielectric tensor, EELS,
reflectivity, off-diagonal elements) are evaluated as decisive physical probes
of interband thresholds, plasmonic collective modes, and in-plane symmetry
breaking, rather than routine outputs. Furthermore, we provide a
self-contained
physical explanation of why band topology is significant in light-element
systems without heavy-atom SOC, explaining how spatial inversion and orbital
parity inversion protect gapless helical edge channels, before introducing the
Fu-Kane parity invariant formula.
4. Sharp Research Gaps and Cohesive Structure: Section 1.4 defines three
distinct, unresolved research gaps directly addressed by Chapters 4, 5, and 6.
Section 1.5 outlines the synergistic three-stage progression of the thesis
(extrinsic interface engineering -> intrinsic multicentre bonding ->
light-metal elemental topology).

---

### Response to Examiner 2, Comment 1 (Literature Review)

Examiner's Comment:
Chapter 1 provides a clear introduction to the systems under investigation and
establishes the scientific background and motivation for the work. The
principal
weakness of this chapter, and indeed of the thesis as a whole, is the absence
of
a dedicated and comprehensive literature review. While relevant background
information is provided, the thesis would benefit significantly from a more
thorough critical review of previous research in the area. The candidate
should
include a discussion of the key studies that have been undertaken on related
two-dimensional boron, and beryllium-based materials, highlighting the
findings
of previous researchers and identifying the gaps in knowledge that motivate
the
present work. Such a review should also discuss the various theoretical and
computational approaches that have been employed in the literature, including
the levels of theory used successfully to predict properties of similar
systems.

Author's Response:
We thank Examiner 2 for highlighting the need for a dedicated and critical
literature review. In response, Chapter 1 has been thoroughly restructured:
1. Dedicated Literature Review Section: We have incorporated Section 1.2,
comprising dedicated subsections on 2D boron systems (Section 1.2.1), 2D
beryllium systems (Section 1.2.2), and computational methodologies
(Section 1.2.3).
2. Review of Key Experimental and Theoretical Studies: We review key
experimental milestones (MBE growth of borophene, sonochemical exfoliation of
beryllene by Chahal et al.) and theoretical proposals (boron carbides, alpha-
and beta-beryllene), identifying unresolved questions regarding multi-layer
bcc-derived phases, hydrogen functionalization, and complex o-B14 networks.
3. Theoretical Approaches and Levels of Theory: Section 1.2.3 specifically
discusses the predictive capabilities, benchmark performance, and trade-offs
of various theoretical frameworks employed in the literature, including
semilocal GGA-PBE, hybrid functional HSE06, van der Waals D3 corrections, DFPT
phonon stability, Wannier-interpolated EPW Eliashberg superconductivity, and
Fu-Kane topological parity invariants.
4. Research Gaps Identified: The review culminates in Section 1.4, where three
focused research gaps are formally articulated to provide the explicit
motivation for the investigations in Chapters 4-6.
```
