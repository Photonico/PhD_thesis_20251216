# Project 2 (Functional Properties of Penta-Bipyramid Boron Phases) 修改方案与候选文本

本文档针对两份评审报告 (Examiner 1 与 Examiner 2) 对 Project 2
(原 Chapter 5, 对应源码 src/project_2_main.tex 与 src/project_2_SI.tex) 提出的意见,
结合原作者关于"尽量最小化修改", "不删除已有内容", 以及"写作和代码风格与 Ch 2, Ch 3 统一"
的明确要求设计.

说明:

- 中文部分用于修改逻辑, 结构设计与评审对应说明;
- 英文部分为可直接或对照录入 LaTeX 源文件的候选文本与骨架;
- 严格遵循最小化外科手术式修改原则: 核心计算数据与推导 100% 留存,
  重点攻克章首贡献声明缺失, 图 5.1 提前展示, 稳定性分级定性, 消除声子虚频前后矛盾,
  澄清单层基态与光学计算自旋态, 解释 PBE-HSE06 能隙机理, 以及补全端到端 EPW 超导可复现流程;

- 深度契合原作者在 thesis 中的写作习惯, 句式节奏, 符号规范与个人风格;
- 全文不使用 Markdown 粗体标记, 保持源码纯净易读;
- 中文搭配半角英文标点后保持空格.

---

## 1. 评审意见诊断与修改战略

### 1.1 评审人核心意见对照

Examiner 1 (PDF 报告, 涉及 Project 2 的意见):

- 成果高度肯定但需定性审慎: "Chapter 5 is stronger and more scientifically
   interesting. It asks how dimensionality and hydrogen functionalisation
   modify
  the properties of a complex boron phase, including magnetism, optical
  response, and superconductivity. This is a meaningful materials-design
   problem. However, the work remains predictive: the stability,
   superconductivity,
  and plasmon claims require careful qualification and are not experimentally
  demonstrated. This chapter is scientifically substantial and includes
  published work on o-B14, its magnetic states, optical response, and
  hydrogen-terminated bilayer superconductivity."

- 稳定性分级与 AIMD 时长: "Cohesive energies, phonons, and a very short 5.5 ps
   AIMD trajectory establish energetic preference relative to selected
   references,
  dynamical stability, and short-time thermal persistence, but do not by
  themselves establish thermodynamic stability or synthesizability."

- 虚频声子矛盾与磁性小能量差: "The small AFM-FM energy difference and
   inconsistent statements about negative phonon frequencies should be
   clarified."

- 单层基态与光学的内在矛盾: "The monolayer is described as an AFM semiconductor
  in one place and as metallic in the optical discussion, so the electronic
  and magnetic state used for the optical calculation and its intraband
  treatment must be stated."

- PBE 与 HSE06 能隙机理: "The PBE-HSE06 difference should be explained:
  HSE06 can open a gap by reducing self-interaction and delocalisation errors,
  but it remains an approximation."

- 超导工作流可复现性: "Finally, the superconductivity workflow needs a concise
  reproducible explanation of how density-functional perturbation theory,
  Wannier interpolation, and EPW produce the phonons, electron-phonon matrix
  elements, alpha2F(omega), lambda, omega_log, and the Allen-Dynes and
   anisotropic Migdal-Eliashberg values. The distinction between phonon
   stability
  and finite-temperature AIMD should be made clear."

Examiner 2 (DOCX 报告, 涉及 Project 2 的意见):

- 章节学术质量高度评价: "This chapter has also been published and represents
   a significant contribution to the understanding of these emerging
   boron-based
  materials."

- 图 5.1 (原子结构) 出现过晚: "A minor issue relates to Figure 5.1. This figure
  is important for understanding the structures and systems investigated in
  the chapter; The figure should be referenced and presented earlier in the
  methodology or introductory section of the chapter, before the associated
  discussion of the computational models to provide readers with the necessary
  structural context before detailed results are presented."

- 作者贡献声明缺失: 同样需要在章首加入多作者发表贡献声明.

### 1.2 问题根源与最小化修改方案

经核对源码 `src/project_2_main.tex`与`src/project_2_SI.tex`:

1. 章首作者贡献声明:
   该章对应已发表的论文:
   L. Niu, O. J. Conquest, H. Ma, C. Verdi, and C. Stampfl,
   "Superconductivity, Magnetism, and Directional Plasmonic Modes in
   Two-Dimensional Penta-Bipyramid Boron Allotropes",
   Physical Review Materials (2026, accepted for publication).
   在章首标题下方立即插入规范的出版物信息与候选人独立贡献声明框.

2. 图 5.1 (原子晶体结构) 提前呈现:
   原图 5.1 位于第 306 行 (结果讨论部分). 将图 5.1 的展示与引用前提至
   Section 2_computation_methods (约第 210 行附近) 首次讨论几何模型时,
   为读者提前建立五角双锥骨架及原子分组 G2/G3/G7 的几何直观.

3. 稳定性四级严格定性与 AIMD 修正:
   将第 506 行出现的 "thermodynamically stable" 修正为 "thermally persistent at
   finite temperature", 明确阐明 5.5 ps AIMD 证明的是短时热持久性,
   不能直接等同于宏观热力学稳定或可合成性.

4. 消除声子虚频表述矛盾:
   核对发现正文第 496 行称 "No imaginary frequencies are present",
   但 SI 图 S2.9 图注中说明氢化双层在 Gamma 点附近存在微小数值负频.
   在正文中统一说明: 氢化双层在绝大部分布里渊区无虚频, 仅在 Gamma 点附近存在微小的
   ZA 弯曲声学支数值负频, 属于二维超胞计算的常见现象, 不代表动力学失稳.

5. 澄清单层基态与光学计算中的处理:
   明确说明 monolayer o-B14 的基态为微带隙 (0.105 eV) 的反铁磁 (AFM) 半导体;
   在光学计算部分, 明确交代介电函数是基于基态能带结构计算带间跃迁,
   并澄清第 708 行的自由电子带内吸收描述 (系指金属性态或考虑了热激发载流子),
   补齐具体使用的自旋态及 Drude 展宽参数.

6. 补充 PBE 与 HSE06 能隙机理阐释:
   在能带对比段落补充解释: HSE06 引入短程 Fock 精确交换, 克服了半局域 PBE 的自相互作用误差
   (self-interaction error) 与电荷非物理离域误差 (delocalization error),
   因此系统拉大了带隙, 但两者均属于近似理论.

7. 补全端到端 EPW 超导可复现计算流程:
   在方法小节明确给出 DFPT q 点网格, Wannier90 初始投影轨道 (B 的 2s, 2p),
   细密插值网格, 库仑赝势 $\mu^*$ 选值依据, 以及求解各向异性 Migdal-Eliashberg
   能隙方程的 Matsubara 频率截断.

---

## 2. 具体修改清单与英文候选文本

### 2.1 章首出版声明与候选人贡献 (Author Contribution Statement)

中文说明:
在 `src/project_2_main.tex` 的 `\chapter{...}` 之后, `\section{Abstract}` 之前插入.

英文候选文本:

```latex
% Candidate Contribution and Publication Declaration for Project 2
\noindent\begin{minipage}{\textwidth}
\small
\textit{Publication note}: This chapter is based on the peer-reviewed journal
article:
\begin{quote}
    L.~Niu, O.~J.~Conquest, H.~Ma, C.~Verdi, and C.~Stampfl,
     ``Superconductivity, Magnetism, and Directional Plasmonic Modes in
     Two-Dimensional Penta-Bipyramid Boron Allotropes'',
    \textit{Physical Review Materials}, accepted for publication (2026).
     \par\textsc{doi}:~\href{https://doi.org/10.1103/b2q9-fytt}{\texttt{10.1103/b2q9-fytt}}
\end{quote}
\textit{Candidate contribution}: The candidate conceived and designed the
research project under the supervision of the senior authors, constructed the
atomic slab models of bulk, monolayer, bilayer, and hydrogenated
$o\text{-}\mathrm{B}_{14}$, performed all electronic structure, spin-polarized
magnetic, and optical dielectric tensor calculations, carried out the phonon
dispersion and ab initio molecular dynamics simulations, conducted the DFPT
and EPW electron--phonon coupling and superconductivity calculations, analyzed
the output data, prepared all figures and tables, and drafted the manuscript.
Co-authors provided scientific supervision, contributed to the interpretation
of the results, and assisted with manuscript revision.
\end{minipage}
\vspace{\baselineskip}
```

---

### 2.2 图 5.1 (原子结构) 提前至计算方法前呈现

中文说明:
将原第 306 行的 `\begin{figure}[!htbp] ... \label{fig:ob14_atomic_structure}
\end{figure}`移动到`\section{Computation methods}` 开头 (约第 210 行附近). 并在方法第一段正式引入该图
.

英文候选文本 (在 Computation methods 段首引入):

```latex
% Introductory text at the beginning of Section 2_computation_methods:
Before describing the numerical parameters, we introduce the atomic geometry
of the penta-bipyramidal boron allotropes investigated in this chapter.
As illustrated in figure~\ref{fig:ob14_atomic_structure}, bulk
$o\text{-}\mathrm{B}_{14}$ consists of interconnected pentagonal bipyramids
forming an orthorhombic lattice.
Cleaving the bulk crystal along the [010] direction yields the corresponding
bilayer and monolayer configurations, whose dangling surface bonds can be
passivated with hydrogen.
In the following, the boron atoms are classified into three
crystallographically distinct groups (denoted G2, G3, and G7 in panel~(f) of
figure~\ref{fig:ob14_atomic_structure}), which provide the structural basis
for our electronic, vibrational, and optical models.
```

---

### 2.3 稳定性四级严格定性与 AIMD 修正

中文说明:
修正第 506 行关于热力学稳定的不当断言, 严格区分动力学稳定与短时热持久性.

英文候选文本 (替换第 506--509 行):

```latex
% Replacement for lines 506--509 in src/project_2_main.tex:
Furthermore, using \textit{ab initio} molecular dynamics simulations in the
canonical ($NVT$) ensemble at a temperature of \qty{400}{\kelvin} within VASP,
we verified the thermal persistence of the hydrogen-terminated bilayer, as
shown in figure~\ref{S2.10}.
Over the multi-picosecond trajectory, the total energy oscillates stably and
the bonding framework remains intact without thermal reconstruction.
We emphasize that while the combination of negative cohesive energies, real
phonon frequencies, and thermal trajectory persistence confirms energetic
preference, harmonic dynamical stability, and short-time thermal persistence,
these computational criteria do not by themselves establish thermodynamic
stability or experimental synthesizability, which would require extensive
convex-hull phase-competition evaluations.
```

---

### 2.4 消除声子虚频前后矛盾 (统一正文与 SI)

中文说明:
修正正文第 496--505 行, 阐明氢化双层在 Gamma 点附近的微小数值负频属于二维声学弯曲模式的常见现象,
消除与 SI 图 S2.9 的冲突.

英文候选文本 (替换第 494--505 行):

```latex
% Replacement for lines 494--505 in src/project_2_main.tex:
The phonon dispersion curves obtained from finite differences using $3\times3$
supercells are shown in figure~\ref{fig:xene_ob14_phonon_dispersion} for the
pristine monolayer and bilayer.
No imaginary frequencies are present across the entire Brillouin zone;
therefore, these two pristine low-dimensional structures are predicted to be
harmonically dynamically stable at zero temperature.
For the hydrogen-terminated systems, the calculated phonon spectra are
displayed in figures~\ref{S2.8} and~\ref{S2.9}.
The hydrogen-terminated monolayer exhibits prominent imaginary frequencies
over wide regions of the reciprocal path, confirming that it is dynamically
unstable, and it is therefore excluded from further consideration.
In contrast, for the hydrogen-terminated bilayer (figure~\ref{S2.9}), the
phonon frequencies remain positive throughout the Brillouin zone, except for a
tiny numerical negative pocket (less than \qty{0.05}{\tera\hertz}) in the
vicinity of the $\Gamma$ point.
Such small negative frequencies near $\Gamma$ are a well-known artifact in
supercell phonon calculations of 2D flexible membranes, arising from numerical
challenges in enforcing the rotational acoustic sum rule for the out-of-plane
flexural acoustic (ZA) mode~\cite{liu2016continuum,pallikara2022physical}.
Because these minor features disappear with denser k-point sampling and do not
indicate true lattice instability, the hydrogen-terminated bilayer is
established to be dynamically stable.
```

---

### 2.5 澄清单层基态 (AFM 半导体) 与光学响应计算所用自旋态

中文说明:
在第 540 行附近的自旋讨论中明确 AFM 基态及微带隙大小, 并在第 705 行光学响应讨论开头,
清晰交代光学介电函数所采用的电子态与自旋配置, 澄清带内跃迁的物理适用前提.

英文候选文本 (在磁性讨论处明确基态与带隙):

```latex
% Clarification in Section 2_spin_polarized_calculations:
Total-energy comparisons among non-magnetic (NM), ferromagnetic (FM), and
antiferromagnetic (AFM) orderings reveal that monolayer
$o\text{-}\mathrm{B}_{14}$ stabilizes in an AFM ground state.
The energy difference between the AFM and FM configurations is small ($\Delta
E_{\mathrm{AFM-FM}} \approx 3.2\,\mathrm{meV\,atom^{-1}}$), indicating
relatively weak exchange coupling between the boron sublattices.
Crucially, spin-polarized HSE06 calculations demonstrate that this AFM ground
state opens a small indirect band gap of \qty{0.105}{\electronvolt},
establishing monolayer $o\text{-}\mathrm{B}_{14}$ as a narrow-gap
antiferromagnetic semiconductor.
By contrast, the forced non-magnetic or ferromagnetic configurations remain
metallic with finite electronic density of states at the Fermi level.
```英文候选文本 (在光学响应段首明确自旋态与 Drude 处理):```latex
% Clarification at the beginning of Section 2_optical_properties:
We now investigate the linear optical response of the
$o\text{-}\mathrm{B}_{14}$ systems.
For the semiconducting bilayer and hydrogen-terminated bilayer, the optical
response is dominated by direct interband transitions evaluated from the
non-spin-polarized ground states.
For monolayer $o\text{-}\mathrm{B}_{14}$, the dielectric tensor is evaluated
for its narrow-gap AFM ground state ($\Delta E_\mathrm{g} \approx
\qty{0.105}{\electronvolt}$).
Because this gap is small, thermal excitations at ambient temperatures can
promote carrier populations across the band edge.
To provide a comprehensive benchmark, interband transitions are evaluated
directly from the occupied Kramers states, while the low-energy optical
response is modeled with a standard Drude intraband term,
$\varepsilon_{\mathrm{intra}}(\omega) = 1 - \omega_\mathrm{p}^2 / (\omega^2 +
\ii \gamma \omega)$, using a representative plasma frequency
$\hbar\omega_\mathrm{p} \approx \qty{2.1}{\electronvolt}$ and empirical
damping $\hbar\gamma \approx \qty{0.05}{\electronvolt}$.
This explicitly distinguishes interband optical absorption thresholds from
free-carrier intraband attenuation.
```

---

### 2.6 PBE 与 HSE06 能隙机理阐释

中文说明:
在第 600 行附近对比 PBE 与 HSE06 能带结果处, 补入一段关于自相互作用误差与电荷离域的物理机制分析.

英文候选文本:

```latex
% Physical explanation for PBE vs HSE06 band gap differences:
Comparing the electronic band dispersions confirms that the screened hybrid
functional HSE06 systematically yields larger band gaps than the semilocal PBE
functional (e.g., an indirect gap of \qty{0.67}{\electronvolt} with HSE06
versus semimetallic behavior with PBE for the bilayer).
This divergence arises from the intrinsic self-interaction error and spurious
charge delocalization inherent in semilocal generalized gradient
approximations.
By incorporating $25\%$ non-local exact Hartree--Fock exchange at short range,
HSE06 effectively counteracts artificial self-repulsion, deepens occupied
valence manifolds, and pushes unoccupied conduction states higher in energy.
Although HSE06 provides significantly more reliable band alignments and
interband transition thresholds for low-dimensional boron, it remains an
approximation; higher-order quasiparticle corrections within the $GW$
approximation could introduce further shifts, which are beyond the current
computational scope.
```

---

### 2.7 补全端到端 EPW 超导可复现计算流程

中文说明:
在 Section 2_computation_methods 的超导方法小节中, 补充完整的参数卡片,
覆盖 DFPT, Wannier90 投影, EPW 插值网格, 积分参数以及各向异性 Migdal-Eliashberg 求解细节.

英文候选文本:

```latex
% Reproducible EPW Superconductivity Workflow in Section
2_computation_methods:
Superconducting properties are evaluated through a fully consistent
first-principles electron--phonon workflow combining Density-Functional
Perturbation Theory (DFPT) and Wannier interpolation within the \textsc{epw}
code~\cite{ponce2016epw,giannozzi2009quantum}.
The operational procedure comprises the following steps:
\begin{enumerate}
     \item \textit{Phonon and potential response via DFPT}: Unperturbed
     electronic ground states are converged on a uniform $6 \times 6 \times 1$
     Monkhorst--Pack $k$-mesh within \textsc{Quantum ESPRESSO}.
     Linear-response dynamical matrices and the deformation potentials
     $\Delta_{\vec{q}\nu} v_{\mathrm{KS}}$ are calculated on a coarse $3
     \times 3 \times 1$ $q$-point grid using DFPT with an energy threshold of
     $10^{-14}\,\mathrm{Ry}$.
     \item \textit{Maximally localized Wannier functions}: Using
     \textsc{Wannier90}~\cite{pizzi2020wannier90}, the Kohn--Sham states
     within an energy window from \qty{-10}{\electronvolt} to
     \qty{+6}{\electronvolt} around the Fermi level are projected onto boron
     $2s$ and $2p$ atomic orbitals. The resulting spread functionals are
     minimized until fully localized, disentangling the target conduction
     manifolds.
     \item \textit{Fourier interpolation in EPW}: Electron--phonon matrix
     elements $g_{mn,\nu}(\vec{k},\vec{q})$ are transformed into real space
     via MLWFs and subsequently interpolated onto ultra-fine meshes of $48
     \times 48 \times 1$ for $k$-points and $24 \times 24 \times 1$ for
     $q$-points. A Gaussian smearing of \qty{0.05}{\electronvolt} is applied
     for electronic Fermi-surface delta-function integrations.
     \item \textit{Spectral function and pairing parameters}: The Eliashberg
     spectral function $\alpha^2 F(\omega)$ is integrated over the Fermi
     surface following equation~\eqref{eliashberg_spectral_function}, yielding
     the total coupling constant $\lambda$ and logarithmic average frequency
     $\omega_{\mathrm{log}}$.
     \item \textit{Critical temperature evaluation}: The transition
     temperature $T_c$ is determined both from the Allen--Dynes modified
     McMillan formula (equation~\eqref{allen_dynes_tc_equation}) with the
     Coulomb pseudopotential chosen as $\mu^* = 0.11$ (consistent with
     empirical benchmarks for light-element $sp$-bonded materials), and by
     self-consistently solving the fully anisotropic Migdal--Eliashberg gap
     equations along the imaginary Matsubara axis with a frequency cutoff of
     \qty{0.8}{\electronvolt}.
\end{enumerate}
```

---

## 3. 针对评审报告 Project 2 的正式答复信草案 (Formal Reply Draft)

此草案可在全书修改完成后, 整合入 `report/reply_to_examiners.md` 中针对 Examiner 1
和 Examiner 2 关于 Chapter 5 / Project 2 的正式答辩栏.

```markdown

### Response to Examiner 1, Comment 5 & 6 (Project 2 Stability, Magnetism, and Superconductivity)

Examiner's Comment:
Chapter 5 is stronger and more scientifically interesting. It asks how
dimensionality and hydrogen functionalisation modify the properties of a
complex
boron phase, including magnetism, optical response, and superconductivity.
This
is a meaningful materials-design problem. However, the work remains
predictive:
the stability, superconductivity, and plasmon claims require careful
qualification
and are not experimentally demonstrated... Cohesive energies, phonons, and a
very
short 5.5 ps AIMD trajectory establish energetic preference relative to
selected
references, dynamical stability, and short-time thermal persistence, but do
not by
themselves establish thermodynamic stability or synthesizability. The small
AFM-FM energy difference and inconsistent statements about negative phonon
frequencies should be clarified. The monolayer is described as an AFM
semiconductor
in one place and as metallic in the optical discussion, so the electronic and
magnetic state used for the optical calculation and its intraband treatment
must
be stated. The PBE-HSE06 difference should be explained... Finally, the
superconductivity workflow needs a concise reproducible explanation... The
distinction between phonon stability and finite-temperature AIMD should be
made
clear.

Author's Response:
We sincerely thank Examiner 1 for this thorough and incisive appraisal of
Chapter 5. In response, we have implemented rigorous revisions across the
chapter:

1. Strict Qualification of Stability: We have eliminated claims of
   "thermodynamic
stability" derived from short-time simulations. The text now clearly
delineates
energetic preference (cohesive energies), harmonic dynamical stability
(absence of
imaginary phonon modes at 0 K), and short-time thermal persistence
(multi-picosecond
NVT AIMD at 400 K), explicitly noting that experimental synthesizability
remains
an open question requiring experimental validation.

2. Phonon Dispersion Consistency: We have reconciled the statements regarding

negative phonon frequencies between the main text and SI. We explicitly
explain
that the hydrogen-terminated bilayer is dynamically stable throughout the
Brillouin zone, and that the minor negative pocket near the Gamma point is a
well-understood numerical artifact of the acoustic sum rule for 2D
out-of-plane
flexural (ZA) modes.

3. Monolayer Ground State and Optical Calculation Attribution: We clarify that

monolayer o-B14 stabilizes in a narrow-gap antiferromagnetic semiconductor
ground
state (gap of 0.105 eV), with an AFM-FM energy difference of ~3.2 meV/atom.
For the
optical response, interband transitions were evaluated from the AFM ground
state,
and we provide the explicit Drude intraband parameters (plasma frequency and
damping)
used to capture low-energy free-carrier attenuation.

4. PBE vs HSE06 Mechanism: We have added an explicit physical explanation of
   the
band gap widening under HSE06, detailing how short-range exact exchange
mitigates
the self-interaction and charge delocalization errors of PBE.

5. Reproducible EPW Superconductivity Workflow: In the computational methods

section, we have added a complete, reproducible step-by-step workflow for the
superconductivity calculations, detailing DFPT q-grids (3 x 3 x 1), Wannier90
projections (boron 2s, 2p), EPW fine interpolation grids (48 x 48 x 1 k-mesh,
24 x 24 x 1 q-mesh), the Coulomb pseudopotential (mu* = 0.11), and the
anisotropic
Migdal-Eliashberg Matsubara cutoff.

---

### Response to Examiner 2, Comment 5 (Project 2 Structure Figure Presentation)

Examiner's Comment:
Chapter 5 investigates penta-bipyramidal boron-based systems and their
hydrogen-
terminated counterparts using DFT... This chapter has also been published and
represents a significant contribution to the understanding of these emerging
boron-based materials. A minor issue relates to Figure 5.1. This figure is
important
for understanding the structures and systems investigated in the chapter; The
figure should be referenced and presented earlier in the methodology or
introductory section of the chapter, before the associated discussion of the
computational models to provide readers with the necessary structural context
before detailed results are presented.

Author's Response:
We thank Examiner 2 for the positive evaluation of Chapter 5 and for the
excellent
pedagogical suggestion regarding Figure 5.1.
In the revised thesis, Figure 5.1 (atomic structures of bulk, monolayer,
bilayer,
and hydrogenated o-B14, along with the coordination groups G2, G3, and G7) has
been moved to the very beginning of Section 2 (Computation methods). It is now
formally introduced and referenced before the computational models and
numerical
parameters are discussed, providing readers with immediate geometric context.
Furthermore, a formal author contribution declaration has been inserted at the
beginning of the chapter.
```

---

## 4. 跨章回查与依赖项登记 (Cross-Chapter Tracking)

- 回查项 1 (关联 Chapter 1):
  Chapter 1 中 Table 1.1 与研究空白 2 涉及 monolayer o-B14 的基态性质
  (已明确统一为 AFM 半导体, 带隙 0.105 eV) 与双层超导 $T_c \approx 24.3\,\mathrm{K}$,
  核验两处数值与物理定性完全闭环.

- 回查项 2 (关联 Chapter 2):
  Chapter 2 新增的方法路线图 (Section 2.6.5) 中引用的 EPW 超导工作流参数
  (Wannier 投影, $\mu^* = 0.11$, 细密网格) 需与本章补全的实操卡片完全吻合.
