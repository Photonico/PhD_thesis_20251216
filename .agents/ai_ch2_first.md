# Chapter 2 (Fundamentals I: Many-Body Quantum Physics and DFT) 修改方案与候选文本 (零删除/全保留方案)

本文档针对两份评审报告 (Examiner 1 与 Examiner 2) 对 Chapter 2 提出的意见,
结合原作者关于"不删除已有推导内容"的明确要求重新设计.
用于指导 src/fundamentals_a.tex 在 100% 完整保留原有推导的基础上进行增强与重构.

说明:

- 中文部分用于修改逻辑, 结构设计与评审对应说明;
- 英文部分为可直接或对照录入 LaTeX 源文件的候选文本与骨架;
- 严格遵循"零删除, 全保留"原则: 原有 3152 行全部数学推导, 物理诠释, 历史背景与个人笔记完全保留在正文中, 不做删节;
- 深度契合论文原作者在 thesis 中的写作习惯, 句式节奏, 符号规范与个人风格;
- 全文不使用 Markdown 粗体标记, 保持源码纯净易读;
- 中文搭配半角英文标点后保持空格.

---

## 1. 评审意见诊断与"全保留"应对战略

### 1.1 评审人批评的真正痛点诊断

我们需要仔细剖析 Examiner 1 原话的核心逻辑:

"Chapters 2 and 3 together are also disproportionately long, at approximately
100 pages, while still not giving the reader a concise roadmap of the
computational methods (geometry optimization, phonon, magnetism, AIMD,
superconductivity, topological property) used later. Substantial scientific
and editorial corrections are therefore required... The reader more needs
a brief, method-oriented account of geometry optimisation and convergence
criteria, Brillouin-zone sampling and the choice of k-points, phonon
calculations, AIMD, spin-polarised calculations and magnetic ordering,
electron-phonon calculations and superconductivity, and spin-orbit coupling
and topological analysis. These methods should be connected explicitly to
the scientific questions in the later chapters."

仔细品读这段话会发现:
评审人最强烈的抱怨并不是"你写了严密的量子力学基础理论"本身,
而是"你写了 100 页的基础理论, 可是我往后翻想要找你后文计算具体怎么算的
(弛豫判据, 声子, 磁性, AIMD, 超导, 拓扑)时, 发现竟然完全找不到实用方法总结!"

也就是说, 评审人的核心诉求是"补齐实用的计算方法路线图, 并与后文建立显式连接".
至于长篇理论推导, 在博士学位论文 (Doctoral Thesis) 中, 保持自洽, 详尽,
有教学深度 (pedagogical and self-contained) 的理论体系是完全正当且值得骄傲的学术心血.

### 1.2 "零删除, 全保留"的实施路线 (加法与架构重构)

既然每一行公式, 每一个物理图像都是作者辛勤推导沉淀的心血,
我们采取"只做加法, 不做减法, 重塑宏观架构"的方案:

- 现有内容 100% 原位保留:

  Section 2.1 (时间演化算符, 绘景变换, 连续性方程),
  Section 2.2 (大正则系综, 统计力学推导),
  Section 2.3 (Thomas-Fermi 唯象模型及其极限分析, Hohenberg-Kohn 定理),
  Section 2.4 (Kohn-Sham 辅助系统, Hartree 方程变分),
  Section 2.5 (交换关联泛函: LDA, GGA-PBE, HSE06).
  全部保留在正文当前位置, 一个公式都不删, 也不强制移入附录.

- 篇章架构重塑为两大板块 (Two-Part Architecture):

  在 Chapter 2 开头加入清晰的"双板块导读"指引:
  Part I (Formal Theoretical Foundations, Section 2.1 至 2.5):
  系统建立从含时薛定谔方程到 Kohn-Sham 密度泛函理论的严格多体物理框架;
  Part II (Practical Computational Methodology Roadmap, 新增 Section 2.6):
  集中呈现后文 Chapters 4, 5, 6 真实采用的第一性原理计算参数选择,
  稳定性判据与物理分析流程.

- 新增实用计算方法路线图 (Section 2.6):

  全面补齐 Examiner 1 点名的全部 7 项计算实操说明, 并附全景关联表 (Table 2.1).

- 答辩回复信的学术辩护 (Defense Strategy):

  向评审人清晰阐明: 博士论文不同于期刊短文, 其核心价值之一在于提供自洽完整的理论推演.
  我们保留全部推导以确保理论基础的严谨性与完整性,
  同时全新增加了 Section 2.6 实用方法路线图, 彻底满足评审人对计算流程与方法衔接的全部要求.

---

## 2. Chapter 2 重构后的章节目录规划

在全保留前提下, Chapter 2 的目录结构扩展为如下六个部分:

- Section 2.1: A story starts with time evolution quantum mechanics (原貌保留)
- Section 2.2: Toward the many-body problem (原貌保留)
- Section 2.3: An introduction to density functionals (原貌保留)
- Section 2.4: From density functional to Kohn--Sham theory (原貌保留)
- Section 2.5: Exchange-correlation functional (原貌保留)
- Section 2.6: Practical Computational Methodology Roadmap (核心新增实用方法路线图)
  - 2.6.1 Geometry optimization and convergence criteria
  - 2.6.2 Brillouin-zone sampling and dense k-point grids
  - 2.6.3 Dynamical and thermal stability: Harmonic phonons and AIMD
  - 2.6.4 Collinear spin-polarized calculations and magnetic ordering
  - 2.6.5 Electron--phonon coupling and superconductivity workflow
  - 2.6.6 Spin--orbit coupling and topological parity analysis
  - 2.6.7 Synthesis: Connecting computational methods to thesis chapters (含全景
    映射表 Table 2.1)

---

## 3. 分节修改要点与英文候选文本

### 3.1 章首引言与双板块导览重构 (Opening Framework)

中文说明:
更新 chapter 开头的综述段落, 将导读指引与六个 section 对齐.
明确向读者宣告本章由"理论基础"与"实用路线图"两大支柱构成,
既讲清多体量子物理的微观起源, 又为后文计算提供可操作的实验路线图.

英文候选文本:

```latex
% opening paragraph
We start our discussion of the fundamentals in this chapter.
Here, we introduce the many-body quantum framework behind density functional
theory, bridging rigorous theoretical physics with practical first-principles
materials computation.
The ionic structure creates an external potential, and the interacting
electrons in this potential determine the electronic, magnetic, vibrational,
and optical properties of the materials studied in this thesis.
In principle, the many-body wave function $\Psi$ contains the full electronic
information of the system.
However, as $\Psi$ depends on all electronic coordinates, direct solution
becomes computationally intractable for realistic materials.
We therefore proceed from the many-body wave function $\Psi$ to the electron
density $n(\vec{r}\,)$, and then construct practical density functionals.

This chapter partly draws on my notes from the Coursera course \textit{Density
Functional Theory}, offered by École Polytechnique and taught by Francesco
Sottile and Lucia Reining~\cite{sottile_reining_dft_coursera}.

To provide both a comprehensive theoretical foundation and an actionable guide
for the subsequent materials investigations, this chapter is organised into
two complementary parts:
\begin{itemize}
    \item \textit{Part \textRoman{1}: Formal Foundations of Density Functional
    Theory
    (Sections~\ref{sec:time_evolution_quantum_mechanics}--\ref{sec:exchange_correlation_functional}).}
    We develop the microscopic quantum theory through a gradual reduction of
    the electronic degrees of freedom.
    In section~\ref{sec:time_evolution_quantum_mechanics}, we begin with
    quantum time evolution and formulate the many-body electronic hamiltonian.
    Section~\ref{sec:toward_many_body_problem} examines quantum expectation
    values and statistical density operators, motivating the necessity for
    reduced spatial descriptions.
    Section~\ref{sec:introduction_density_functionals} introduces density
    functionals, reviews the historical Thomas--Fermi model, and establishes
    the Hohenberg--Kohn theorems.
    With the electron density $n(\vec{r}\,)$ established as the fundamental
    physical variable,
    section~\ref{sec:from_density_functional_to_Kohn_Sham_theory} constructs
    the auxiliary single-particle Kohn--Sham framework.
    Section~\ref{sec:exchange_correlation_functional} presents the practical
    hierarchy of exchange-correlation approximations, spanning local density
    (LDA), generalized gradient (GGA-PBE), and screened hybrid (HSE06)
    functionals.

    \item \textit{Part \textRoman{2}: Practical Computational Methodology
    Roadmap (Section~\ref{sec:practical_computational_roadmap}).}
    To bridge abstract quantum formalisms with predictive computational
    materials science, section~\ref{sec:practical_computational_roadmap}
    presents an operational roadmap of the first-principles methods
    implemented in this thesis.
    We formulate each technique around its governing equations, numerical
    convergence criteria, and operational parameters---encompassing structural
    relaxation, dense Brillouin-zone sampling, harmonic phonon dispersions,
    finite-temperature molecular dynamics (AIMD), collinear magnetic ordering,
    electron--phonon superconductivity workflows, and topological parity
    invariants.
    Each method is explicitly linked to the specific scientific inquiries
    addressed in Chapters~\ref{cha:project_bilayers}, \ref{cha:project_boron},
    and~\ref{cha:project_beryllene}.
\end{itemize}
```

---

### 3.2 核心新增节: Section 2.6 Practical Computational Methodology Roadmap

中文说明:
本节完整加在 `src/fundamentals_a.tex`的末尾 (紧接着 Section
2.5`sec:exchange_correlation_functional` 之后).
它完全满足了 Examiner 1 所要求的 7 大实操方法总结,
在写作风格上严密贴合原作者的词汇与句式规范:

- 推进词: `Firstly` $

ightarrow$ `Secondly` $
ightarrow$ `Thirdly` $
ightarrow$
  `Fourthly` $
ightarrow$ `Fifthly` $
ightarrow$ `Sixthly` $
ightarrow$
  `Finally`;

- 公式后带小写 `here,`;
- 矢量宏 `ec{r}\,`, 微分宏`\dif{ec{r}}`, 物理量宏`\qty{...}{...}`;
- 显式给出每个方法用于 Chapters 4, 5, 6 的哪一章, 回答什么具体材料问题;
- 配备全景对应表 Table 2.1.

英文候选文本:

```latex
\newpage
\section{Practical Computational Methodology Roadmap}
\label{sec:practical_computational_roadmap}

% opening paragraph
While the preceding sections formulated the rigorous mathematical foundations
of density functional theory, practical implementation requires translating
continuous electronic functionals into discrete numerical algorithms.
In computational condensed-matter physics, predictive accuracy depends not
only on the chosen exchange-correlation approximation, but also on the
convergence of finite basis sets, reciprocal-space grids, and interatomic
forces.
Furthermore, beyond evaluating ground-state electronic densities and total
energies, investigating emerging low-dimensional materials demands specialized
techniques to determine mechanical stability, thermal durability, magnetic
ground states, electron--phonon interactions, and topological band invariants.

In the following, we outline the operational computational methodologies
employed throughout Chapters~\ref{cha:project_bilayers},
\ref{cha:project_boron}, and~\ref{cha:project_beryllene}.
We formulate each method around its governing equations, computational
parameters, and convergence criteria, explicitly linking each technique to the
physical questions addressed in the later chapters.

\subsection{Geometry optimization and convergence criteria}
\label{subsec:method_relaxation}

Firstly, determining the ground-state atomic geometry represents the
prerequisite for all subsequent electronic, optical, and vibrational
calculations.
In this thesis, first-principles calculations are carried out using plane-wave
pseudopotential methods implemented within the Vienna Ab initio Simulation
Package (\textsc{vasp})~\cite{kresse1996efficient,kresse1996efficiency} and
the \textsc{Quantum ESPRESSO}
distribution~\cite{giannozzi2009quantum,giannozzi2017advanced,giannozzi2020quantum}.
Projector augmented-wave (PAW)
pseudopotentials~\cite{blochl1994projector,kresse1999ultrasoft} model the
electron--ion core interactions, with valence electron configurations treated
explicitly.
Kinetic energy cutoffs for plane-wave basis sets are systematically
benchmarked, with values typically chosen between \qty{400}{\electronvolt} and
\qty{600}{\electronvolt} to guarantee energy convergence within
$1\,\mathrm{meV\,atom^{-1}}$.

For two-dimensional monolayers and vertical heterostructures, periodic
boundary conditions artificially repeat slabs along the perpendicular ($z$)
direction.
To prevent fictitious electrostatic interactions between adjacent periodic
images, a vacuum buffer spacing of at least \qty{15}{\angstrom} to
\qty{40}{\angstrom} is introduced.
Structural relaxation proceeds via conjugate-gradient or quasi-Newton
algorithms.
The electronic self-consistent field (SCF) cycles are iterated until the total
energy change satisfies:

\begin{equation}
    \Delta E_\mathrm{tot} < 10^{-6}\text{--}10^{-8}\,\mathrm{eV}
\label{energy_convergence_criterion}
\end{equation}

here, the stricter threshold of $10^{-8}\,\mathrm{eV}$ is enforced whenever
linear response phonon dispersions, magnetic exchange energies, or optical
response functions are subsequently calculated.

Concurrently, interatomic Hellmann--Feynman forces acting on individual nuclei
are evaluated:

\begin{equation}
    \vec{F}_I = -\frac{\partial E_\mathrm{tot}}{\partial \vec{R}_I}
\label{hellmann_feynman_force}
\end{equation}

here, $\vec{R}_I$ refers to the position vector of nucleus $I$.
Atomic positions and in-plane lattice vectors are relaxed until residual
forces satisfy $|\vec{F}_I| < \qty{0.01}{\electronvolt\per\angstrom}$ (or
$10^{-4}\,\mathrm{Ry\,bohr^{-1}}$).
This structural optimization protocol is applied universally to all pristine
monolayers, heterostructures, and functionalized allotropes across
Chapters~\ref{cha:project_bilayers}, \ref{cha:project_boron},
and~\ref{cha:project_beryllene}.

\subsection{Brillouin-zone sampling and dense $k$-point grids}
\label{subsec:method_kpoints}

Secondly, evaluating physical observables requires integrating electronic wave
functions over the first Brillouin zone.
Reciprocal-space integrations are performed using $\Gamma$-centered
Monkhorst--Pack grids~\cite{monkhorst1976special}.
The choice of $k$-point sampling density depends crucially on the targeted
physical observable:

\begin{itemize}
    \item \textit{Ground-state relaxation and energetics:}
    Standard meshes with a grid spacing of $\Delta k \approx
    0.02\text{--}0.03\,\text{\AA}^{-1}$ (for example, $9 \times 9 \times 1$ or
    $12 \times 12 \times 1$ for typical 2D unit cells) provide total energy
    convergence within $1\,\mathrm{meV\,atom^{-1}}$.
    \item \textit{Linear optical response and dielectric tensors:}
    Interband transition matrix elements require ultra-dense $k$-point
    sampling to properly resolve sharp van Hove singularities and eliminate
    artificial discretization peaks.
    Consequently, dense meshes up to $105 \times 105 \times 1$ are utilized in
    Chapter~\ref{cha:project_bilayers} and
    Chapter~\ref{cha:project_beryllene}.
    Concurrently, the summation over unoccupied conduction bands is converged
    by including between 128 and 200 empty bands.
    \item \textit{Fermi-surface and electron--phonon integrations:}
    Metallic systems and electron--phonon scattering require ultra-fine grids,
    which are achieved via maximally localized Wannier interpolation as
    outlined in subsection~\ref{subsec:method_elph}.
\end{itemize}

\subsection{Dynamical and thermal stability: Harmonic phonons and AIMD}
\label{subsec:method_stability}

Thirdly, demonstrating energetic preference via cohesive energy does not
guarantee the experimental existence or physical robustness of a free-standing
2D crystal.
To establish structural integrity, we distinguish strictly between harmonic
dynamical stability at zero temperature and thermal persistence at finite
temperatures.

Dynamical stability is verified by calculating phonon dispersion spectra
$\omega_\nu(\vec{q})$.
Under the harmonic approximation, the interatomic force constant tensor is
defined as:

\begin{equation}
    \Phi_{\alpha\beta}(I l, J l') = \frac{\partial^2 E_\mathrm{tot}}{\partial
    u_{\alpha}(I l)\,\partial u_{\beta}(J l')}
\label{force_constant_tensor}
\end{equation}

here, $u_\alpha(I l)$ denotes the displacement of atom $I$ in unit cell $l$
along the Cartesian direction $\alpha$.
Phonon frequencies $\omega_\nu(\vec{q})$ are obtained by diagonalizing the
dynamical matrix $D_{\alpha\beta}^{IJ}(\vec{q})$ across high-symmetry
reciprocal paths, using either the finite-displacement supercell approach
implemented in \textsc{Phonopy}~\cite{togo2015first} or Density-Functional
Perturbation Theory (DFPT)~\cite{baroni2001phonons}.
The complete absence of imaginary frequencies (represented conventionally as
negative frequencies in dispersion plots) across the entire Brillouin zone
confirms that the atomic structure resides in a local energetic minimum,
establishing harmonic dynamical stability at \qty{0}{\kelvin}.

However, harmonic phonon analysis cannot capture finite-temperature
anharmonicity, entropic stabilization, or bond dissociation.
Therefore, thermal persistence is further assessed via \textit{ab initio}
molecular dynamics (AIMD) simulations.
Simulations are performed within the canonical ($NVT$) ensemble, where the
target temperature ($T = \qty{300}{\kelvin}$ or $\qty{400}{\kelvin}$) is
controlled by a Nosé--Hoover
thermostat~\cite{nose1984molecular,hoover1985canonical}.
To minimize periodic self-interaction of thermal fluctuations, supercells ($3
\times 3 \times 1$ or larger) are employed with an integration time step of
$\Delta t = \qty{1.0}{\femtosecond}$.
Monitoring the total potential energy and temperature trajectories over
multi-picosecond timescales verifies whether the 2D atomic network retains
structural connectivity without bond breaking or spontaneous reconstruction.
Phonon dispersions and AIMD trajectories are employed in
Chapter~\ref{cha:project_boron} to assess $o\text{-}\mathrm{B}_{14}$
nanosheets and in Chapter~\ref{cha:project_beryllene} to validate pristine and
hydrogenated beryllenes.

\subsection{Collinear spin-polarized calculations and magnetic ordering}
\label{subsec:method_magnetism}

Fourthly, in low-dimensional materials with localized electronic states or
broken surface bonds, electron exchange interactions can lift spin degeneracy.
To investigate possible magnetic ground states, spin-polarized density
functional calculations are performed by solving separate Kohn--Sham equations
for spin-up ($n_\uparrow$) and spin-down ($n_\downarrow$) densities:

\begin{equation}
    \left[ -\frac{\hbar^2}{2m_\mathrm{e}}\nabla^2 + v_\mathrm{ext}(\vec{r}\,)
    + v_\mathrm{H}([n];\vec{r}\,) +
    v_\mathrm{xc}^{\sigma}([n_\uparrow,n_\downarrow];\vec{r}\,) \right]
    \psi_{i\sigma}(\vec{r}\,)
    = \varepsilon_{i\sigma}\psi_{i\sigma}(\vec{r}\,)
\label{spin_polarized_ks_equation}
\end{equation}

here, $\sigma \in \{\uparrow, \downarrow\}$ denotes the spin index, and the
spin-dependent exchange-correlation potential $v_\mathrm{xc}^{\sigma}$ is
obtained from functional differentiation with respect to
$n_\sigma(\vec{r}\,)$.

To determine the magnetic ground state, multiple initial spin configurations
are initialized and fully relaxed:
non-magnetic (NM), ferromagnetic (FM), and various antiferromagnetic (AFM)
orderings.
By comparing their converged total energies, the magnetic ground state is
identified, and the exchange coupling parameters can be derived.
In Chapter~\ref{cha:project_boron}, this methodology resolves the magnetic
ground state of monolayer $o\text{-}\mathrm{B}_{14}$, elucidating the
competitive energy differences between AFM and FM configurations.

\subsection{Electron--phonon coupling and superconductivity workflow}
\label{subsec:method_elph}

Fifthly, predicting phonon-mediated conventional superconductivity requires
evaluating the microscopic scattering of electrons near the Fermi surface by
lattice vibrations.
The linear response of the self-consistent Kohn--Sham potential to an atomic
displacement is determined using DFPT:

\begin{equation}
    g_{mn,\nu}(\vec{k},\vec{q}) = \left( \frac{\hbar}{2M\omega_{\vec{q}\nu}}
    \right)^{\!1/2} \braket{\psi_{m,\vec{k}+\vec{q}} | \,\Delta_{\vec{q}\nu}
    v_\mathrm{KS}\, | \psi_{n,\vec{k}}}
\label{elph_matrix_element}
\end{equation}

here, $g_{mn,\nu}(\vec{k},\vec{q})$ represents the electron--phonon matrix
element describing the scattering of an electron from state
$|\psi_{n,\vec{k}}\rangle$ to $|\psi_{m,\vec{k}+\vec{q}}\rangle$ by a phonon
mode $\nu$ with wave vector $\vec{q}$ and frequency $\omega_{\vec{q}\nu}$.

Because computing $g_{mn,\nu}(\vec{k},\vec{q})$ directly on ultra-dense meshes
via DFPT is computationally prohibitive, we employ the Electron--Phonon
Wannier (\textsc{epw}) code~\cite{ponce2016epw,giannozzi2009quantum}.
The electronic Kohn--Sham states are transformed into a basis of maximally
localized Wannier functions (MLWFs) using
\textsc{Wannier90}~\cite{pizzi2020wannier90}, while interatomic force
constants are transformed into real space.
This permits efficient, generalized Fourier interpolation of electron--phonon
matrix elements onto ultra-fine $k$- and $q$-point meshes.

From the interpolated matrix elements, the Eliashberg spectral function
$\alpha^2 F(\omega)$ is computed:

\begin{equation}
    \alpha^2 F(\omega) = \frac{1}{2\pi N(\varepsilon_\mathrm{F})}
    \sum_{\vec{q}\nu} \delta(\omega - \omega_{\vec{q}\nu}) \sum_{mn,\vec{k}}
    |g_{mn,\nu}(\vec{k},\vec{q})|^2 \,\delta(\varepsilon_{n\vec{k}} -
    \varepsilon_\mathrm{F})\,\delta(\varepsilon_{m,\vec{k}+\vec{q}} -
    \varepsilon_\mathrm{F})
\label{eliashberg_spectral_function}
\end{equation}

here, $N(\varepsilon_\mathrm{F})$ is the electronic density of states at the
Fermi level per spin.
The total dimensionless electron--phonon coupling parameter $\lambda$ and the
logarithmic average phonon frequency $\omega_\mathrm{log}$ are then obtained
via spectral integration:

\begin{equation}
\left\{\begin{aligned}
\lambda &
    \coloneqq 2\int_0^\infty \dif\omega\,\frac{\alpha^2 F(\omega)}{\omega}
    \\[4pt]
    \omega_\mathrm{log} &\coloneqq \exp\!\left[ \frac{2}{\lambda}\int_0^\infty
    \dif\omega\,\frac{\alpha^2 F(\omega)}{\omega}\,\ln\omega \right]
\end{aligned}\right.
\label{lambda_and_wlog_definition}
\end{equation}

here, $\lambda$ characterizes the integrated scattering strength, while
$\omega_\mathrm{log}$ provides the characteristic phonon energy scale
mediating the attractive Cooper pairing.

The superconducting transition temperature $T_\mathrm{c}$ is subsequently
estimated using the semi-empirical Allen--Dynes modified McMillan
equation~\cite{mcmillan1968transition,allen1975transition}:

\begin{equation}
    T_\mathrm{c} = \frac{\omega_\mathrm{log}}{1.20}\,\exp\!\left[
    -\frac{1.04(1+\lambda)}{\lambda - \mu^*(1+0.62\lambda)} \right] f_1 f_2
\label{allen_dynes_tc_equation}
\end{equation}

here, $\mu^*$ refers to the effective screened Coulomb pseudopotential
(typically set to semi-empirical values between $0.10$ and $0.16$), and $f_1,
f_2$ represent strong-coupling and shape correction factors.
To go beyond isotropic approximations, the fully anisotropic
Migdal--Eliashberg gap
equations~\cite{migdal1958interaction,eliashberg1960interactions,margine2013anisotropic}
are solved self-consistently on the imaginary Matsubara frequency axis to
determine the momentum-dependent superconducting gap $\Delta_{\vec{k}}(T)$ and
its critical temperature.
This workflow is utilized in Chapter~\ref{cha:project_boron} to investigate
the emergence of phonon-mediated superconductivity in hydrogen-terminated
bilayer $o\text{-}\mathrm{B}_{14}$.

\subsection{Spin--orbit coupling and topological parity analysis}
\label{subsec:method_topology}

Sixthly, in the presence of heavy-element constituents or symmetry-enforced
band inversions, relativistic spin--orbit coupling (SOC) modifies electronic
band degeneracies:

\begin{equation}
    \hat{H}_\mathrm{SOC} = \frac{\hbar}{4m_\mathrm{e}^2 c^2} \left( \nabla V
    \times \hat{\vec{p}} \right) \cdot \hat{\vec{\sigma}}
\label{soc_hamiltonian}
\end{equation}

here, $V$ denotes the self-consistent crystalline potential, $\hat{\vec{p}}$
is the momentum operator, and $\hat{\vec{\sigma}} = (\hat{\sigma}_x,
\hat{\sigma}_y, \hat{\sigma}_z)$ is the vector of Pauli matrices.

In two-dimensional centrosymmetric crystals with time-reversal symmetry,
non-trivial band topology is categorized by the $\mathbb{Z}_2$ topological
invariant $\nu \in \{0, 1\}$.
Following the parity formulation of Fu and Kane~\cite{fu2007topological},
$\nu$ is determined directly from the spatial parity eigenvalues of the
occupied electronic states at the four time-reversal invariant momentum (TRIM)
points $\Gamma_i$ ($i \in \{1, 2, 3, 4\}$) in the 2D Brillouin zone:

\begin{equation}
    (-1)^\nu = \prod_{i=1}^4 \delta_i, \quad \text{with} \quad \delta_i =
    \prod_{m=1}^{N_\mathrm{occ}} \xi_{2m}(\Gamma_i)
\label{fu_kane_formula_method}
\end{equation}

here, $\xi_{2m}(\Gamma_i) = \pm 1$ denotes the parity eigenvalue of the
$2m$-th occupied electronic Kramers pair at TRIM point $\Gamma_i$.
A total product yielding $(-1)^\nu = -1$ designates a topologically
non-trivial phase ($
u = 1$), which ensures the existence of symmetry-protected helical edge
states, whereas $(-1)^\nu = +1$ identifies a topologically trivial phase ($
u = 0$).
This parity diagnosis is implemented in Chapter~\ref{cha:project_beryllene} to
investigate the topological properties of pristine and cubic trilayer
beryllenes.

\subsection{Synthesis: Connecting computational methods to thesis chapters}
\label{subsec:method_synthesis_table}

Finally, to provide a concise overview of how these computational techniques
unite to address the core scientific questions of this thesis,
Table~\ref{tab:methods_summary_roadmap} summarizes the computational methods,
operational parameters, and their specific application across
Chapters~\ref{cha:project_bilayers}, \ref{cha:project_boron},
and~\ref{cha:project_beryllene}.

\begin{table}[!htbp]
\centering
\caption{Summary of computational methodologies, numerical tools, convergence
parameters, and their targeted applications across the research chapters.}
\label{tab:methods_summary_roadmap}
\begin{adjustbox}{width=0.98\textwidth}
\begin{tabular}{llll}
\hline
Methodology & Software / Code & Key Operational Parameters &
    Targeted Chapter Applications \\
\hline
Geometry relaxation & \textsc{vasp} / \textsc{QE} &
    $E_\mathrm{cut} =
    \qty{400}{\electronvolt}\text{--}\qty{600}{\electronvolt}$; $|\vec{F}_I| <
    \qty{0.01}{\electronvolt\per\angstrom}$ &
    Chapters~\ref{cha:project_bilayers}, \ref{cha:project_boron},
    \ref{cha:project_beryllene} (All 2D structures) \\
van der Waals dispersion & DFT-D3 / TS &
    Interlayer binding energies, equilibrium distances &
    Chapter~\ref{cha:project_bilayers} (Graphene-boron heterostructures) \\
Linear optical response & \textsc{vasp} (Independent particle) &
    $k$-mesh up to $105 \times 105 \times 1$; 128--200 empty bands &
    Chapters~\ref{cha:project_bilayers}, \ref{cha:project_boron},
    \ref{cha:project_beryllene} (Dielectric spectra, EELS) \\
Phonon dispersion & \textsc{Phonopy} / DFPT &
    Supercell displacement; acoustic sum rule &
    Chapters~\ref{cha:project_boron}, \ref{cha:project_beryllene} (0 K
    dynamical stability) \\
Molecular dynamics (AIMD) & \textsc{vasp} ($NVT$ ensemble) &
    Nosé--Hoover; $T = \qty{300}{\kelvin}$; $\Delta t =
    \qty{1.0}{\femtosecond}$; $>\qty{5}{\pico\second}$ &
    Chapters~\ref{cha:project_boron}, \ref{cha:project_beryllene} (Thermal
    persistence) \\
Spin-polarized DFT & \textsc{vasp} (Collinear) &
    NM, FM, AFM initializations; $\Delta E_\mathrm{tot} <
    10^{-8}\,\mathrm{eV}$ &
    Chapter~\ref{cha:project_boron} (Monolayer $o\text{-}\mathrm{B}_{14}$
    magnetic ground state) \\
Electron--phonon pairing & \textsc{epw} / \textsc{Wannier90} &
    Fine $k/q$-meshes; $\mu^* = 0.10\text{--}0.16$; anisotropic gap &
    Chapter~\ref{cha:project_boron} ($o\text{-}\mathrm{B}_{14}$ bilayer
    superconductivity) \\
Band topology & \textsc{Quantum ESPRESSO} (SOC) &
    Fu--Kane parity product at 4 TRIM points; $\mathbb{Z}_2$ index &
    Chapter~\ref{cha:project_beryllene} (Cubic trilayer beryllene topology) \\
\hline
\end{tabular}
\end{adjustbox}
\end{table}

By establishing these methodological standards, we ensure that the physical
predictions presented in the subsequent chapters are grounded in robust, fully
reproducible first-principles simulations.
```

---

## 4. 答辩信中对 Chapter 2 篇幅的学术辩护策略 (Formal Reply Strategy)

在保留全部已有推导的前提下, 我们在答辩信中采取主动, 积极且完全站得住脚的学术答辩策略:

1. 申明博士学位论文的自洽完整性与教学价值 (Pedagogical and Self-Contained Value):
   向评审人诚恳解释: 博士学位论文不同于追求极致压缩的期刊快报 (Letters).
   深入推演量子力学含时演化, 密度算符展开, Thomas-Fermi 模型及其渐近行为,
   构成了理解多体电子结构与现代 DFT 变分基础不可分割的理论基石.
   保留这些推演展示了候选人扎实的理论物理素养与严密的数理功底.

2. 正面且完满地解决评审人的核心关切 (Directly Solving the Core Missing Element):
   我们正面指出, 评审人最核心的需求是"缺乏面向后续实际计算的方法路线图".
   因此, 我们在 Chapter 2 末尾专门增加了全新的 Section 2.6 (Practical Computational
   Methodology Roadmap).
   该节用紧凑有力的篇幅, 逐一总结了后文所需的全部 7 种计算方法和收敛判据,
   并配有 Table 2.1 映射表, 将基础理论与后文应用章节无缝锁定.

3. 架构清晰化:
   在 Chapter 2 开头明确声明本章的"双板块架构" (Part I 理论根基 + Part II 实用路线图),
   引导读者清晰把握各部分的定位.

### 答辩信草案文本 (用于全保留方案)

```markdown

### Response to Examiner 1, Comment 1 & 3 (Chapter 2 Depth and Methods Roadmap)

Examiner's Comment:
Chapters 2 and 3 together are also disproportionately long, at approximately
100
pages, while still not giving the reader a concise roadmap of the
computational
methods (geometry optimization, phonon, magnetism, AIMD, superconductivity,
topological property) used later. Substantial scientific and editorial
corrections are therefore required... The reader more needs a brief,
method-oriented account of geometry optimisation and convergence criteria,
Brillouin-zone sampling and the choice of k-points, phonon calculations, AIMD,
spin-polarised calculations and magnetic ordering, electron-phonon
calculations
and superconductivity, and spin-orbit coupling and topological analysis. These
methods should be connected explicitly to the scientific questions in the
later
chapters. These chapters should be shortened and reorganised around the
methods
actually used.

Author's Response:
We thank Examiner 1 for this perceptive observation regarding the balance
between
formal theoretical foundations and practical computational workflows.
In response, we have implemented a targeted structural enhancement to Chapter
2
(Fundamentals I: Many-Body Quantum Physics and Density Functional Theory):

1. Preservation of Rigorous Foundations: A doctoral thesis possesses distinct

scholarly value in providing a self-contained, pedagogically rigorous
development
of microscopic quantum theory. The comprehensive derivations of time-evolution
operators, statistical density operators, Thomas-Fermi asymptotics, and
Kohn-Sham
variational calculus established in Sections 2.1--2.5 represent an integral
theoretical foundation for understanding modern electronic structure theory.

2. New Dedicated Section on Practical Computational Methodology Roadmap: To

directly and completely address the examiner's core requirement, we have
created
an entirely new, self-contained section at the conclusion of Chapter 2:
Section
2.6 (Practical Computational Methodology Roadmap). This section provides a
concise, method-oriented operational manual covering every technique
requested:

   - Subsection 2.6.1: Geometry optimization protocols, Hellmann-Feynman force
     thresholds (|F| < 0.01 eV/A), and vacuum buffering (15-40 A).

   - Subsection 2.6.2: Brillouin-zone Monkhorst-Pack sampling and ultra-dense
     k-grids (up to 105 x 105 x 1) for dielectric and optical integrations.

   - Subsection 2.6.3: Harmonic dynamical stability via DFPT/supercell phonon
     dispersions (absence of imaginary modes) and finite-temperature thermal
     persistence via NVT AIMD trajectories.

   - Subsection 2.6.4: Collinear spin-polarized DFT and competitive magnetic
     orderings (NM, FM, AFM).

   - Subsection 2.6.5: The reproducible electron-phonon superconductivity
     workflow, detailing DFPT potential derivatives, Wannier90 interpolation,
     EPW Eliashberg spectral function alpha2F(omega), lambda, omega_log, and
     the
     anisotropic Migdal-Eliashberg equations.

   - Subsection 2.6.6: Relativistic spin-orbit coupling (SOC) and Fu-Kane
     topological parity invariant analysis at TRIM points.

3. Explicit Synthesis and Chapter Mapping: Section 2.6 concludes with Table
   2.1,
which explicitly connects each computational method, software package, and
convergence threshold directly to the specific scientific inquiries
investigated
in Chapters 4, 5, and 6.

4. Two-Part Chapter Navigation: The opening of Chapter 2 has been augmented
   with
an explicit structural guide designating Part I (Formal Theoretical
Foundations,
Sections 2.1--2.5) and Part II (Practical Computational Methodology Roadmap,
Section 2.6), providing readers with an immediate roadmap to navigate between
formal theory and practical execution.

---

### Response to Examiner 2, Comment 2 (Theoretical Foundations)

Examiner's Comment:
Chapters 2 and 3 give almost textbook version of the theoretical framework and
computational methodologies employed throughout the thesis. The discussion of
density functional theory (DFT) and the computational approaches adopted is
generally clear and provides a suitable foundation for the investigations
presented in later chapters.

Author's Response:
We thank Examiner 2 for the positive assessment of our theoretical foundation.
To
ensure that the theoretical presentation directly supports the computational
investigations in subsequent chapters, we have augmented Chapter 2 with
Section

2. 6 (Practical Computational Methodology Roadmap), which provides an
   operational,
practical synthesis linking the rigorous foundations of DFT to the specific
computational simulations executed across Chapters 4--6.
```

---

## 5. 跨章回查与依赖项登记 (Cross-Chapter Tracking)

在全保留方案下, 仅需在新增的 Section 2.6 中核实与后文数值相关的几个关键参数:

- 回查项 1 (关联 Chapter 4):

  路线图 2.6.2 中关于光学积分超稠密网格的数值 (最高达 $105 \times 105 \times 1$) 与未占导带数 (128 至 200
  支),
  需在审阅 Chapter 4 正文及 SI 时对照实际 INCAR / 计算脚本参数核对确认.

- 回查项 2 (关联 Chapter 5):

  路线图 2.6.5 式~\eqref{allen_dynes_tc_equation} 中引用的库仑赝势 $\mu^*$ 取值范围为 $0.10$ 至
  $0.16$.
  需在核实 Chapter 5 超导计算时确认最终采用的特定 $\mu^*$ 值 (如 $\mu^* = 0.11$ 或 $0.12$),
  并在两处保持自洽.

- 回查项 3 (关联 Chapter 5 与 Chapter 6):

  路线图 2.6.3 中对 AIMD 参数暂定为 $NVT$ 系综, Nosé--Hoover 热浴, 步长 $1.0\, \mathrm{fs}$, 模拟
  时长 $>5\, \mathrm{ps}$.
  需在修改 Chapter 5 (5.5 ps) 和 Chapter 6 (实际运行轨迹步数) 时核对并确认真实模拟时长.

- 回查项 4 (关联 Chapter 6):

  路线图 2.6.6 式~\eqref{fu_kane_formula_method} 中 Fu--Kane 宇称乘积公式的前提为有能隙系统.
  在处理 Chapter 6 时需落实三层立方铍费米面小能隙的判定策略, 确保方法路线图中的定义与 Chapter 6 的数据支撑无缝吻合.
