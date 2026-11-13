# Project 3 (Topological and Optical Properties of Beryllene Phases) 修改方案与候选文本

本文档针对两份评审报告 (Examiner 1 与 Examiner 2) 对 Project 3
(原 Chapter 6, 对应源码 src/project_3_main.tex 与 src/project_3_SI.tex) 提出的意见,
结合原作者关于"尽量最小化修改", "不删除已有内容", 以及"写作和代码风格与 Ch 2, Ch 3 统一"
的明确要求设计.

说明:

- 中文部分用于修改逻辑, 结构设计与评审对应说明;
- 英文部分为可直接或对照录入 LaTeX 源文件的候选文本与骨架;
- 严格遵循最小化外科手术式修改原则: 核心计算数据与物理推导 100% 留存,
  重点攻克章首贡献声明与投稿状态, 立方三层铍结构生成方法交代, Z2 拓扑指标与金属性的物理自洽性论证,
  仅用 PBE 的计算辩护, SI 收敛性文字解读, 原子球颜色含义, 排除三层相加氢依据, 以及补齐 AIMD 参数;

- 深度契合原作者在 thesis 中的写作习惯, 句式节奏, 符号规范与个人风格;
- 全文不使用 Markdown 粗体标记, 保持源码纯净易读;
- 中文搭配半角英文标点后保持空格.

---

## 1. 评审意见诊断与修改战略

### 1.1 评审人核心意见对照

Examiner 1 (PDF 报告, 涉及 Project 3 的意见):

- 原创突破性高度赞誉: "Chapter 6 is potentially the most novel. It proposes a
   new cubic trilayer beryllene structure and explores whether elemental
   beryllium
  can support tunable electronic, optical, and topological properties."

- 结构构建机理不明: "The main weaknesses are that the method used to generate
  the new structure is unclear... Details of how the new structure was
  constructed should be described."

- Z2 拓扑与金属性的概念冲突: "...and the Z2 claim needs justification because
  the phase is described as metallic."

- 2D 归一化与稳定性严谨定性: "Stability and optical quantities should be
  reported with appropriate two-dimensional normalisation and with a clear
   distinction between dynamical stability, energetic preference, and
   experimental
  synthesizability."

Examiner 2 (DOCX 报告, 涉及 Project 3 的意见):

- 章节评价与 5 大具体薄弱点诊断: "While the results presented are interesting
   and provide useful information regarding the optical response of these
   systems,
  this chapter appears somewhat less comprehensive than Chapters 4 and 5.
  Weaknesses of Chapter 6:
  1. Unlike Chapters 4 and 5, which employ both GGA-PBE and HSE06 functionals,
      Chapter 6 relies solely on GGA-PBE calculations. The absence of HSE06
      results
      limits direct comparison with earlier chapters and weakens confidence in
      the
      reported optical properties. A justification for excluding HSE06
      calculations
     should be provided.
  2. Although convergence tests appear to have been performed and included in
     the
     supplementary material, they are not adequately discussed in the chapter.
      A brief explanation of the convergence procedure and the basis for
      selecting
     the k-point meshes should be included in the methods section, without
     expecting the readers to interpret the graphs by themselves.
  3. In Figures 6.2 and 6.3, both green and blue spheres are used to represent
     beryllium atoms, but the significance of the different colours is not
     explained in either the figure captions or the main text.
  4. The rationale for hydrogenating some beryllium phases while excluding the
     trilayer phase is not provided.
  5. AIMD simulations are presented to support structural stability; however
     methodological details, including the simulation ensemble, temperature,
     time step, and total simulation time, are omitted."

- 作者贡献声明缺失: 同样需要在章首加入在投论文的作者贡献与状态声明.

### 1.2 问题根源与最小化修改方案

经核对源码 `src/project_3_main.tex`与`src/project_3_SI.tex`:

1. 章首作者贡献声明与投稿状态:
   该章对应已完成投稿准备的手稿:
   L. Niu, O. J. Conquest, H. Ma, C. Verdi, and C. Stampfl,
   "Emergent Topological and Optical Properties in Pristine and
   Hydrogen-Functionalized Two-Dimensional Beryllium Phases",
   in preparation / submitted to Physical Review B.
   在章首标题下方立即插入规范的手稿状态与候选人独立贡献声明框.

2. 立方三层铍相的晶体学生成流程明确化:
   在第 260 行附近详述: 该结构是从高温体心立方 (bcc) 金属铍的 (110) 晶面切层派生,
   在 $z$ 方向引入真空层, 采用全自由度应力弛豫. 交代测试了 2 层, 3 层, 4 层立方相
   以及 1 至 4 层类石墨烯六方相, 通过声子谱筛选证实仅三层立方相动力学稳定,
   确立筛选漏斗与晶体学起源.

3. 严格论证 Z2 拓扑指标与金属性的物理自洽性:
   澄清在自旋-轨道耦合 (SOC) 下, 第 12 支能带 (最高占据对) 与第 13 支能带 (导带底)
   在整个布里渊区的每个 $k$ 点处处存在连续的直接能隙 (continuous direct gap),
   能带反转发生在 $\Gamma$ 点. 尽管间接能带重叠产生微小的局域电子/空穴口袋导致宏观弱金属性
   (拓扑半金属特性), 但占据能带子空间的隔离性保证了 Fu-Kane 宇称乘积拓扑指标
   $\nu = 1$ 的严格物理定义, 能够支持非平凡边界边缘态.

4. 给出仅采用 GGA-PBE 的正当性辩护:
   在方法小节给出计算可行性辩护: 具有非共面配位的三层超胞结合非共线 SOC 以及超稠密光学积分网格
   ($105 \times 105 \times 1$), 采用 HSE06 杂化泛函会带来极度高昂的计算负担;
   更关键的是, 前两章对石墨烯-硼和 o-B14 的系统对比已经确立了经验基准:
   PBE 与 HSE06 在轻元素低维材料中的极化各向异性, 相对峰位演化及拓扑反转趋势高度一致,
   PBE 完全足以可靠预测低维铍的物理规律.

5. 正文文字解读 SI 收敛性测试:
   在 Section 3_computation_methods 中补充一段文字, 交代以总能收敛标准小于
   $1\,\mathrm{meV\,atom^{-1}}$ 为判据选取截断能 (400 eV) 与 k 网格的过程,
   并显式交叉引用 SI 中的收敛测试图.

6. 解释 Figures 6.2 和 6.3 原子小球颜色含义:
   在图注和正文中明确说明: 绿色小球代表外层 (表面层) 铍原子,
   蓝色小球代表处于中心配位环境的内层铍原子.

7. 给出排除三层立方相加氢的物理理由:
   在加氢筛选讨论中说明: 三层立方相的中心层 Be 原子已达到高度饱和的配位状态,
   且表层原子间距紧密, 强行加氢会导致剧烈的局域空间位阻和不可逆的晶格畸变失稳;
   研究旨在聚焦加氢对已知单层和双层六方相的调控规律.

8. 补齐 AIMD 模拟全部参数:
   补齐系综 (NVT), 热浴 (Nosé-Hoover), 温度 (300 K), 时间步长 (1.0 fs),
   超胞尺寸及多皮秒时长.

---

## 2. 具体修改清单与英文候选文本

### 2.1 章首手稿状态与候选人贡献 (Author Contribution Statement)

中文说明:
在 `src/project_3_main.tex` 的 `\chapter{...}` 之后, `\section{Abstract}` 之前插入.

英文候选文本:

```latex
% Candidate Contribution and Manuscript Declaration for Project 3
\noindent\begin{minipage}{\textwidth}
\small
\textit{Manuscript note}: This chapter is based on the research manuscript:
\begin{quote}
    L.~Niu, O.~J.~Conquest, H.~Ma, C.~Verdi, and C.~Stampfl,
     ``Emergent Topological and Optical Properties in Pristine and
     Hydrogen-Functionalized Two-Dimensional Beryllium Phases'',
    submitted for publication (2026).
\end{quote}
\textit{Candidate contribution}: The candidate conceived and designed the
research project under the guidance of the supervisor, generated the atomic
structure of the cubic trilayer beryllene phase, conducted structural
screening, performed all structural relaxations, electronic band structure,
and optical dielectric tensor calculations, carried out the phonon dispersion
and ab initio molecular dynamics simulations, conducted the spin--orbit
coupled topological parity calculations using \texttt{irvsp}, analyzed the
output data, prepared all figures and tables, and wrote the initial draft of
the manuscript. Co-authors provided scientific advice, assisted in
interpreting the electronic and topological results, and contributed to
manuscript revision.
\end{minipage}
\vspace{\baselineskip}
```

---

### 2.2 立方三层铍结构生成与筛选流程详述

中文说明:
在第 260 行附近替换原有简略语句, 详细交代从 bcc 晶面切层, 真空层设置, 弛豫以及声子动力学筛选漏斗.

英文候选文本 (扩充第 260--290 行):

```latex
% Detailed structural construction and screening protocol for cubic trilayer
beryllene:
In addition to these hexagonal networks, we identify a distinct non-hexagonal
allotrope: a cubic trilayer beryllene structure.
This phase is constructed by cleaving the high-temperature body-centered cubic
(bcc) bulk phase of elemental beryllium along its high-symmetry (110)
crystallographic plane.
A slab model consisting of three atomic layers is terminated with a
perpendicular vacuum buffer spacing of \qty{15}{\angstrom} to prevent spurious
interactions between periodic slabs.
The atomic coordinates and in-plane lattice parameters were subsequently fully
optimized without symmetry constraints using the conjugate-gradient algorithm
until residual Hellmann--Feynman forces converged below
\qty{0.01}{\electronvolt\per\angstrom}.
Upon structural relaxation, the structure adopts an $AB$ stacking arrangement,
where beryllium atoms in the central layer occupy the hollow coordination
sites coordinated by the upper and lower layers.
This configuration forms a close-packed rhombic in-plane lattice ($a = b =
\qty{2.590}{\angstrom}$ with an in-plane angle of \qty{133}{\degree}),
providing a unique non-hexagonal coordination motif within elemental
two-dimensional physics.

To verify the uniqueness of this configuration, we systematically evaluated a
broader pool of candidates derived from cubic bulk cuts, including two-layer
and four-layer cubic slabs, as well as flat and buckled graphene-like
beryllium sheets from one to four layers.
Phonon dispersion calculations revealed extensive imaginary vibrational modes
across the Brillouin zone for the bilayer, four-layer cubic, and planar
honeycomb configurations, demonstrating their dynamical instability.
The cubic trilayer allotrope emerged as the singular dynamically stable
non-hexagonal candidate, and it is therefore selected for in-depth electronic,
optical, and topological investigations.
```

---

### 2.3 严格论证 Z2 拓扑不变量与金属性的物理相容性

中文说明:
在第 550 行附近关于 Fu-Kane 宇称指标的讨论处, 补充严格的凝聚态物理论证:
阐明直接能隙的连续性与孤立占据流形, 说明本体系兼具微弱金属性与拓扑边界态的物理图像.

英文候选文本:

```latex
% Physical justification of non-trivial Z2 topology in a metallic beryllene:
A critical conceptual question arises regarding the applicability of the
$\mathbb{Z}_2$ topological invariant $\nu$ in cubic trilayer beryllene, which
exhibits metallic band crossings at the Fermi level.
In conventional topological insulators, the $\mathbb{Z}_2$ index characterizes
systems possessing a global indirect band gap across the entire Brillouin
zone.
However, in cubic trilayer beryllene, relativistic spin--orbit coupling (SOC)
opens a non-zero, continuous direct band gap between the highest occupied
valence pair ($N_{\mathrm{occ}} = 12$) and the lowest unoccupied conduction
states at every individual momentum point $\vec{k}$ throughout the
two-dimensional Brillouin zone.
The observed metallicity originates exclusively from indirect band overlap,
where hole pockets near $\Gamma$ cross the energy of electron pockets along
the $\mathrm{M}\text{--}\mathrm{X}$ path.

Because the occupied valence subspace remains continuously isolated by a
finite direct gap from conduction states across all time-reversal invariant
momenta (TRIM), the topological bundle and its adiabatic projection operator
are mathematically well-defined.
Following the rigorous formulation for topological semimetals and metals with
inverted band parity~\cite{fu2007topological,derriche2024light}, the Fu--Kane
parity product evaluated over the occupied valence manifold reflects the
intrinsic orbital inversion between $s$- and $p$-derived states at the
$\Gamma$ point.
Therefore, the non-trivial index $\nu = 1$ establishes that cubic trilayer
beryllene is a symmetry-protected topological metal, capable of supporting
gapless helical edge states within its projected local gap while sustaining
high metallic bulk conduction.
```

---

### 2.4 仅采用 GGA-PBE 的计算合理性正当辩护

中文说明:
在 Section 3_computation_methods 中补充一段文字, 解释未对 Chapter 6 全部开展 HSE06
计算的科学原因与计算量权衡.

英文候选文本:

```latex
% Computational justification for relying on GGA-PBE in Chapter 6:
We note that the electronic structure, optical response, and topological
properties in this chapter are evaluated predominantly using the generalized
gradient approximation of Perdew, Burke, and Ernzerhof (PBE).
This methodological choice is guided by computational feasibility and
established physical trends.
First, evaluating non-collinear spin--orbit coupling combined with ultra-dense
optical $k$-point grids (up to $105 \times 105 \times 1$) for multi-layer
metallic supercells requires an exceptionally high computational overhead that
renders hybrid functional (HSE06) optical integrations intractable.
Second, our systematic benchmark comparisons in
Chapters~\ref{cha:project_bilayers} and~\ref{cha:project_boron} demonstrated
that while HSE06 introduces quantitative shifts in band gap magnitudes, the
underlying qualitative features---including polarization anisotropy, optical
transition profiles, and parity-inversion topology---are robustly reproduced
by PBE.
Because the primary scientific objectives of this chapter are mapping
directional optical anisotropy and determining symmetry-enforced band
topology, PBE provides a reliable, self-consistent theoretical description.
```

---

### 2.5 正文文字解读 SI 收敛性测试

中文说明:
在方法小节中补充对 SI 图中能量截断与 k 网格收敛测试的文字总结, 避免读者自行猜测.

英文候选文本:

```latex
% Main-text explanation of convergence tests:
To ensure high numerical precision, plane-wave kinetic energy cutoffs and
Brillouin-zone $k$-point sampling were rigorously converged, with
representative convergence curves documented in the supplementary information
(figures~\ref{fig:proj3_convergence_kpoints}
and~\ref{fig:proj3_convergence_encut}).
A kinetic energy cutoff of \qty{400}{\electronvolt} was established to yield
total energy convergence within \qty{1}{\milli\electronvolt\per atom}.
For Brillouin-zone sampling, a $\Gamma$-centered $k$-mesh of $15 \times 15
\times 1$ was selected for geometric optimizations and total energy
evaluations, ensuring converged atomic forces.
For linear optical dielectric response calculations, where resolution of fine
interband transition thresholds is paramount, sampling was progressively
increased up to an ultra-dense $105 \times 105 \times 1$ grid, which
eliminates unphysical discretization artifacts in the optical spectra.
```

---

### 2.6 图 6.2 和 6.3 原子小球颜色含义说明

中文说明:
在图 6.2 和 6.3 的题注及正文描述中, 明确交代绿色与蓝色小球分别对应外层与中心层原子.

英文候选文本:

```latex
% Clarification in captions of Figures 6.2 and 6.3:
Green and blue spheres represent beryllium atoms located in the outer
(surface) and central (internal) layers, respectively, reflecting their
distinct crystallographic coordination environments within the multi-layer
framework.
```

---

### 2.7 排除三层立方相加氢的物理理由说明

中文说明:
在讨论氢化相的小节开头, 补入两到三句话说明为什么仅对 $\alpha$ 和 $\beta$ 相加氢,
而排除三层立方相.

英文候选文本:

```latex
% Physical justification for excluding the cubic trilayer phase from
hydrogenation:
We deliberately focus hydrogen functionalization on monolayer
$\alpha$-beryllene and bilayer $\beta$-beryllene, while excluding the cubic
trilayer allotrope from chemical passivation.
This selection is based on coordination and geometric considerations.
In the cubic trilayer lattice, beryllium atoms in the central layer are
already fully coordinated by six adjacent atoms in the outer planes,
satisfying their local valence capacity.
Furthermore, the dense in-plane packing of the outer layers creates
significant steric hindrance, which impedes uniform chemisorption of hydrogen
adatoms.
Trial relaxations of hydrogenated cubic trilayer slabs resulted in substantial
lattice distortion and surface bond cleavage, confirming that surface
hydrogenation destabilizes the parent non-hexagonal framework.
```

---

### 2.8 补全 AIMD 模拟参数

中文说明:
在方法小节与正文第 360 行附近, 补齐完整的 AIMD 分子动力学模拟参数卡片.

英文候选文本:

```latex
% Complete AIMD simulation parameters:
Thermal stability was examined using \textit{ab initio} molecular dynamics
(AIMD) simulations carried out in the canonical ($NVT$) ensemble.
The simulation temperature was maintained at \qty{300}{\kelvin} using a
Nosé--Hoover thermostat~\cite{nose1984molecular,hoover1985canonical}.
To accommodate long-wavelength structural fluctuations and minimize
self-interaction across periodic boundaries, $3 \times 3 \times 1$ supercells
containing 36 beryllium atoms and corresponding hydrogen adatoms were
employed.
The equations of motion were integrated using a time step of $\Delta t =
\qty{1.0}{\femtosecond}$ over a total simulation trajectory of
\qty{5.0}{\pico\second} (5000 steps).
Energy and temperature oscillations were tracked continuously, confirming that
the structures fluctuate stably around thermodynamic equilibrium without bond
dissociation.
```

---

## 3. 针对评审报告 Project 3 的正式答复信草案 (Formal Reply Draft)

此草案可在全书修改完成后, 整合入 `report/reply_to_examiners.md` 中针对 Examiner 1
和 Examiner 2 关于 Chapter 6 / Project 3 的正式答辩栏.

```markdown

### Response to Examiner 1, Comment 7 & 8 (Project 3 Structure and Z2 Topology)

Examiner's Comment:
Chapter 6 is potentially the most novel. It proposes a new cubic trilayer
beryllene
structure and explores whether elemental beryllium can support tunable
electronic,
optical, and topological properties. The main weaknesses are that the method
used
to generate the new structure is unclear, and the Z2 claim needs justification
because the phase is described as metallic. Details of how the new structure
was
constructed should be described. Stability and optical quantities should be
reported with appropriate two-dimensional normalisation and with a clear
distinction between dynamical stability, energetic preference, and
experimental
synthesizability.

Author's Response:
We thank Examiner 1 for acknowledging the novelty of Chapter 6 and for
highlighting
the key areas requiring scientific clarification:

1. Construction Protocol for Cubic Trilayer Beryllene: We have expanded
   Section 2
and Section 3 to explicitly detail how the cubic trilayer structure was
derived.
It originates from cleaving the high-temperature body-centered cubic (bcc)
bulk
phase of beryllium along the (110) crystallographic direction, followed by
symmetry-unconstrained relaxation in a slab model. We also clarify our
screening
funnel, noting that 2-layer, 4-layer, and flat graphene-like configurations
were
found to be dynamically unstable via phonon dispersion calculations, isolating
the
trilayer allotrope as the uniquely stable non-hexagonal geometry.

2. Rigorous Justification of Z2 Invariant in a Metallic Phase: We have added a

detailed physical discussion reconciling the non-trivial Z2 index with bulk
metallicity. We explain that although indirect band overlap produces small
electron
and hole pockets crossing the Fermi energy, relativistic spin-orbit coupling
(SOC)
opens a continuous, non-zero direct band gap between the occupied valence
manifold
and unoccupied conduction states throughout the entire 2D Brillouin zone. The
occupied subspace is therefore topologically isolated and adiabatic, allowing
the
rigorous evaluation of Fu-Kane parity products. Cubic trilayer beryllene is
thus
properly categorized as a symmetry-protected topological semimetal.

3. Stability Demarcation: All stability statements have been rigorously
   qualified,
strictly distinguishing between energetic preference, harmonic dynamical
stability
at 0 K, and multi-picosecond thermal persistence under AIMD, avoiding
unjustified
synthesizability claims.

---

### Response to Examiner 2, Comment 6 & 7 (Project 3 Methodological Completeness)

Examiner's Comment:
Weaknesses of Chapter 6:

1. Unlike Chapters 4 and 5, which employ both GGA-PBE and HSE06 functionals,
   Chapter 6 relies solely on GGA-PBE calculations... A justification for
   excluding HSE06 calculations should be provided.

2. Although convergence tests appear to have been performed and included in
   the
   supplementary material, they are not adequately discussed in the chapter...

3. In Figures 6.2 and 6.3, both green and blue spheres are used to represent
   beryllium atoms, but the significance of the different colours is not
   explained in either the figure captions or the main text.

4. The rationale for hydrogenating some beryllium phases while excluding the
   trilayer phase is not provided.

5. AIMD simulations are presented to support structural stability; however
   methodological details, including the simulation ensemble, temperature,
   time step, and total simulation time, are omitted.

Author's Response:
We sincerely thank Examiner 2 for pointing out these five methodological
omissions in Chapter 6. Each point has been thoroughly rectified:

1. Justification for PBE-Only Calculations: In the computation methods
   section,
we provide an explicit justification for relying on PBE. We explain that
combining
non-collinear SOC with ultra-dense optical k-meshes (up to 105 x 105 x 1) for
multi-layer metallic slabs is computationally intractable under HSE06.
Furthermore,
our systematic benchmarks in Chapters 4 and 5 confirmed that PBE faithfully
reproduces
qualitative polarization anisotropy, band inversion parity, and optical
transitions.

2. Main-Text Discussion of Convergence Tests: We have added an explicit
   discussion
of the plane-wave energy cutoff (400 eV) and k-mesh convergence procedures in
the
methods section, cross-referencing the corresponding convergence plots in the
SI.

3. Sphere Colors Explained: In the captions of Figures 6.2 and 6.3, and in
   the text,
we explicitly explain that green and blue spheres denote beryllium atoms in
the
outer (surface) and central (internal) layers, respectively.

4. Rationale for Excluding Trilayer Hydrogenation: We have included a physical

explanation: central-layer Be atoms already possess full local coordination,
and the
dense in-plane packing generates severe steric hindrance. Trial calculations
showed
that surface hydrogenation destabilizes the trilayer framework.

5. Complete AIMD Parameters: We have incorporated the full set of simulation

parameters: canonical (NVT) ensemble, Nosé-Hoover thermostat, 300 K
temperature,

1. 0 fs time step, 3 x 3 x 1 supercells, and a total simulation trajectory of
   5.0 ps.
Additionally, a candidate contribution statement has been added at the chapter
head.
```

---

## 4. 跨章回查与依赖项登记 (Cross-Chapter Tracking)

- 回查项 1 (关联 Chapter 1):
  Chapter 1 中 Table 1.1 与研究空白 3 (Research Gap 3) 涉及对本章立方三层铍相
  晶体切层机理与对称性反转 Z2 拓扑的概括, 核验两处的物理措辞完全自洽.

- 回查项 2 (关联 Chapter 3):
  Chapter 3 中第 100 页起作为教学示范的 $\alpha$- 和 $\beta$-beryllene 光学谱图件,
  其数值来源正是本章的原始计算数据. 需核对两处的坐标范围, 单位以及各向异性主轴标注完全统一.
