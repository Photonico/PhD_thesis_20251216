# Chapter 2 最终修改措施

日期: 2026-09-21.
对象: `src/fundamentals_a.tex`.
依据: 两份原始 examiner reports, 当前 Chapter 2 和 Chapter 3 源码,
[Gemini 第一稿](ai_ch2_first.md), [二次核验稿](ai_ch2_second.md),
[修改流程](ai.md), 以及 [Ollie 的论文](ollie.pdf) 中相关方法内容.

本文件覆盖旧版 `ai_ch2_last.md`, 现在是下一次修改的最终操作稿,
不再作为第一轮修改的逐字实施记录.
当前章首导航、2.5 的 PBE/HSE06 范围说明和原版 2.6 已经在正文中;
下文给出在这一现状上的增量措施. 本轮只更新本文件, 没有应用到正式 TeX.
`ai_ch2_second.md` 保留为历史核验材料; 与本稿不同之处以本稿为准.
本稿不继承旧文件的字数、页数或“已经编译通过”记录作为本轮证据.

你的最新原则优先: 能少缩就少缩, 有明显重复才缩;
保留原有推导、例子和完整讲述, 不移入附录, 不改小字号或行距.
知识参考 Ollie, 语言、讲解顺序和 TeX 习惯参考你的原稿,
尤其是 Chapter 3 从复折射率逐步推导光学量的写法.

## 1. 最终取舍与评审对应

Examiner 1 在 PDF 第 1 页同时要求实际计算方法导读与缩短、重组基础章节.
他点名的方法包括结构优化和收敛、k 点、声子、AIMD、磁性、电子声子耦合和超导、SOC 和拓扑.
不能把这条意见解释成“只要增加方法节, 就已完全满足”.
Examiner 2 肯定了 Chapters 2–3 的理论说明;
其针对这两章的具体纠正是 Chapter 3 的自有光学例图需要明确来源.

本稿采用以下安排:

1. 原有 2.1–2.5 的结构、推导和课程笔记来源说明保留.
   只删去一处明显重复的 Hartree 引入, 另做少量已核实的局部纠错与限定.
2. 保留现有章首直接进入 2.6 的导航, 不再增加 Part I/II、方法总表或重复小结.
3. 在当前 2.6 中补齐必要中间步骤, 使读者知道前面的 DFT 怎样成为实际计算.
   不是再列一遍软件名称, 也不扩展成各个领域的完整综述.
4. 按最新讨论, Chapter 2 负责 many-body、DFT 和 practical calculations;
   Chapter 3 负责 electrodynamics 和 optical response;
   拟新增 Chapter 4 负责 band topology. 原 2.6.6 迁移, 不丢弃.
5. 新拓扑章只讲论文实际用到的概念与适用前提.
   本稿不增加边缘态、拓扑输运、无关模型或相应示意图.
6. 实际网格、阈值、磁参考态、赝势数据集、轨迹和计算结果仍由对应研究章核实.
   这里提供通用关系和明确入口, 不代填未知事实.

本稿能回答的是方法说明、理论与计算的衔接、PBE/HSE06 解释范围和基础章节的分工.
仅删除两句直接重复, 加上拓扑内容迁移, 不足以声称基础部分整体已经缩短.
迁移只是改变位置, 不是减少总内容. 最终回复应如实说明, 不宣称所有 reports 要求已全部关闭.

## 2. Ollie 论文的参考范围

核读范围为印刷页 26–31, 即 PDF 第 38–43 页:
2.5.4 Implementation of Density Functional Theory,
2.5.4.1 Bloch's Theorem,
2.5.4.2 PAW Pseudopotentials and VASP,
2.5.4.3 Ionic Relaxation.
其中印刷页 27–30 还逐页检查了公式图像.

可借鉴的知识联系是: 周期性 → Bloch 态 → 平面波基底与 cutoff → 核价处理 → 电子自洽与结构弛豫.
这些恰好解释本论文已经使用的计算环节, 因而纳入 2.6.
Ollie 没有提供这里所需的 Wannier/EPC 或声子动力学矩阵的对应论述;
这些关系依据本论文现有文献及原始方法论文核对.

不采用其坐标波函数写法、粗体矢量、段落节奏或代码习惯,
不引入 FORTRAN 历史、催化、溶剂熵或与本研究无关的内容.
也不照搬其公式: 印刷页 29 的 cutoff 式 (2.54) 只显示一个 ħ,
而恢复常数后应为 ħ²|k+G|²/(2m_e); 印刷页 30 的式 (2.55) 将力写作正能量梯度,
本稿保留正确的负梯度关系. Bloch 态也不能普遍等同于单个平面波.
这些例子说明参考论文不能代替对公式的独立核验.

新增候选优先使用 `thesis.bib` 中已有的原始方法文献,
不复制 Ollie 的文字或图像, 不新增未经核实的 bib key.

## 3. 写作与 TeX 的执行标准

- 按“提出问题 → 说明需要哪一步 → 给公式 → 解释符号 → 解释物理含义 → 回扣或引出下一步”组织.
  以 `fundamentals_b.tex` 中复折射率分离实虚部的过程为范本,
  不只在互不连接的结果公式之间加入 `Therefore`.
- 保留 `We first`, `We then`, `We next`, `Firstly`, `Accordingly`, `Subsequently` 的讲解口吻,
  只在确有先后或因果关系时使用. 不另造宣传性的段落或方法术语.
- 用自然段展开, 不把正文改成提纲或参数清单.
  小节开头的回顾、公式后的物理解释和小节末尾的过渡不自动算作重复.
- 新增量子态始终使用 Dirac notation, 坐标表达用位置投影,
  矩阵元用 `\bra{...}\hat{O}\ket{...}`.
  经典位移、力和动力学矩阵分量保持其正常写法.
- 使用 `\vec`, `\dif`, `\mathrm`, `\coloneqq`, `\kB`;
  严格保留 `\vec{r}\,'` 和 `\vec{r}\,)` 的间距.
  新增虚数单位写 `\mathrm{i}`, 不批量格式化原有推导.
- 公式用 `equation`, 按需要内嵌 `aligned` 或左大括号;
  label 单独一行, 公式后用小写 `here,` 解释新符号.
- 小节标题使用 sentence case, 正文使用 `chapter~\ref`, `section~\ref`, `equation~\eqref`.
  保留原 label, 原 `\newpage` 和 hamiltonian 等既有措辞.
- 保留 Hartree atomic units 的主约定; 需要显式使用 ħ、k_B 时就地说明.
  区分频率、角频率、能量和温度, 不机械搬用其他作者的公式常数.

## 4. 保留的内容与 2.6 最终结构

章名与章首保持现状. 原 2.1 的时间演化和多体问题,
2.2 的统计与约化描述, 2.3 的密度泛函、Hohenberg–Kohn 和 Thomas–Fermi,
2.4 的 Kohn–Sham 构造和 Hartree, 2.5 的 LDA/GGA/PBE/HSE06 均保留.
除了第 5 节的明确位置, 不顺带润色这些部分.
本稿没有逐式重新认证整个 2.1–2.5, 不将“保留”写成“所有原公式已独立核验”.

2.6 沿用 `From density functional theory to practical calculations`, 保留五个方法小节:

1. Structural relaxation and convergence.
2. Periodic states and Brillouin-zone sampling.
3. Phonons and molecular dynamics.
4. Spin polarization and magnetic ordering.
5. Electron-phonon coupling and superconductivity.

其中新增的完整性是三个具体联系:

- 2.6.2: Bloch 态与 cell-periodic 态 → 平滑辅助态的平面波展开 → cutoff 与 k 点的区别 → PAW 重建与 QE norm-conserving 路线的区别.
- 2.6.3: 力常数 → 二阶能量展开 → 谐近似运动方程 → 正常模代入 → 动力学矩阵本征方程.
- 2.6.5: cell-periodic 态上的 EPC 矩阵元 → Wannier 变换 → 实空间矩阵元及细网格插值 → 费米面谱函数 → 耦合强度和转变温度.

既有结构优化、自洽、磁性、AIMD、谱函数和温度公式的主要讲述继续保留.
电子自洽过程在 2.4 已说明, 这里用回指承接, 不另写第二套 SCF 推导.
不追加完整 PAW 能量泛函、Sternheimer 方程、Wannier spread 最小化,
或全套各向异性 Migdal–Eliashberg 方程.
这些不是本轮补齐上述联系所必需的内容.

## 5. 按原文顺序应用的具体操作

下列行号对应本次读取的当前 `src/fundamentals_a.tex`, 用于辅助定位;
执行时以原句和 label 为准. 除明确标为删除的两句外, 都是原位替换或插入.
操作 C2-08 已合并二次稿的 EPC 金属参考态限定.
光学 n/m 指标的条件性联动单独列在第 7 节, 不提前制造与当前 Chapter 3 的不一致.

### C2-01. 2.2: 修正跃迁密度中重复计入的时间相位

当前位置: 第 918 行起.

已核实的局部代数纠错, 不是删减推导. 原式在含时间相位的两个 Ψ 外再次乘相位, 且指数遗漏显式 ħ. 替换至 transition_amplitude 对应的 \end{equation}, 不含随后 Subsequently, we recall a one-body operator... 段落. 保留三个原 label 和原 f 的归一化定义; 只将时间依赖分离一次. 新写的态和投影采用 Dirac notation.

定位原句开头: `The corresponding phase factor associated with the excitation energy is $\mathrm{e}^{-i(E_n-E_g)t}$.`.

候选 LaTeX:

```latex
The corresponding phase factor associated with the excitation energy is $\mathrm{e}^{-\mathrm{i}\omega_{ng}t}$.
We retain $\hbar$ explicitly in these phase relations.
For a time-independent hamiltonian, we separate the time dependence of each stationary state as:

\begin{equation}
    \ket{\Psi_j(t)}=\mathrm{e}^{-\mathrm{i}E_jt/\hbar}\ket{\Phi_j},
    \qquad j\in\{g,n\}
\label{time_dep_eigenstate}
\end{equation}

here, $\ket{\Phi_j}$ is the time-independent many-body eigenstate with energy $E_j$.
Substituting these states into equation~\eqref{one_body_transition_quantity_compact},
we obtain:

\begin{equation}
    f_n^\mathrm{eh}(x_1,t)
    =\mathrm{e}^{-\mathrm{i}\omega_{ng}t}f_n^\mathrm{eh}(x_1,0)
\label{mod_transition_one-body}
\end{equation}

here, the phase-independent part follows from the coordinate projections of the stationary states:

\begin{equation}
    f_n^\mathrm{eh}(x_1,0)
    =\int\braket{\Phi_g|\vec{x}}\braket{\vec{x}|\Phi_n}
    \prod_{j=2}^{N}\dif{x_j}
\label{transition_amplitude}
\end{equation}

The time dependence is therefore contained in a single phase factor,
while the transition amplitude is determined by the stationary states.
```

### C2-02. 2.3: 只删去第二次引入 Hartree 项的两句重复文字

当前位置: 第 1745 行起.

当前第 1731–1732 行已经完成同一引入, 并给出 hartree_term_functional. 删除后, 原来的非经典相互作用说明直接接 interaction-level approximation. 所有公式、定义、label 和后续解释保留. 这是本稿唯一的纯文字删重, 不把必要回扣、互补推导或拓扑迁移计作删重.

仅删除以下原文, 不写替代段落:

```latex
We next approximate the interaction energy functional by the classical Coulomb energy associated with the density distribution.
Using the electron-electron Coulomb repulsion~\eqref{electrons_Coulomb}, we introduce the Hartree term:
```

### C2-03. 2.4: 限定局域 Kohn–Sham 势的语境

当前位置: 第 2772 行起.

其后 multiplicative operator 和泛函依赖的解释保留. 与 2.5 的 generalized Kohn–Sham 说明形成明确分工, 不改写原有局域势推导.

定位原句开头: `Moreover, the exchange-correlation potential $v_\mathrm{xc}([n];\vec{r}\,)$ is a static and local potential.`.

候选 LaTeX:

```latex
In the local Kohn--Sham formulation considered here, the exchange-correlation potential $v_\mathrm{xc}([n];\vec{r}\,)$ is a static and local potential.
```

### C2-04. 2.5: 去掉泛函层级中的无条件精度判断

当前位置: 第 3005 行起.

采用二次措施稿中的词级修订. 增加密度梯度信息不等于对所有物理量都保证更准确.

定位原句开头: `More accurate semilocal approximations also include the density gradient.`.

候选 LaTeX:

```latex
Semilocal approximations also include the density gradient.
```

### C2-05. 2.5: 准确表述 LDA 对非均匀密度的处理

当前位置: 第 3024 行起.

LDA 式仍逐点使用 n(r), 不能把它说成完全忽略密度的空间变化. 原来的适用限制和通向 GGA 的过渡保留, 不增加新的泛函背景.

定位原句开头: `However, it neglects the inhomogeneity of the density.`.

候选 LaTeX:

```latex
However, it does not depend explicitly on the density gradient.
```

### C2-06. 2.5: 补齐 HSE 与 generalized Kohn–Sham 的联系

当前位置: 第 3116 行起.

在原句后插入三行. 保留原 HSE 能量式、参数、推导顺序和所有 label; 不增加 Fock 算符或 optimized effective potential 的独立推导.

定位原句开头: `Moreover, $a$ refers to the mixing parameter that determines the fraction of exact exchange.`.

候选 LaTeX:

```latex
Moreover, $a$ refers to the mixing parameter that determines the fraction of exact exchange.

The Hartree--Fock exchange term depends explicitly on the occupied orbitals.
In the generalized Kohn--Sham treatment used for hybrid functionals,
its orbital variation gives a non-local exchange operator.
```

### C2-07. 2.5: 更直接回应 PBE/HSE06 的误差与适用范围

当前位置: 第 3133 行起.

采用二次措施稿的短修订. 后面 HSE06 remains an approximation 和 larger gap 不保证更准确的两句原样保留. 具体体系中的变化原因仍由研究结果支持.

定位原句开头: `The screened exchange contribution in equation~\eqref{HSE_exchange_correlation_functional} can change the localization of electronic states and the predicted band gap.`.

候选 LaTeX:

```latex
The screened exchange contribution in equation~\eqref{HSE_exchange_correlation_functional}
can reduce self-interaction and delocalisation errors,
thereby changing the localization of electronic states and the predicted band gap.
```

### C2-08. 2.6: 补齐实际计算的必要中间步骤, 将拓扑正文移交新章

当前位置: 第 3151 行起.

以下是完整的 2.6 候选, 用于一次替换当前同名 section 至章末衔接段, 不含后面的 % draft 注释. 大部分现有文字和公式保留; 改动集中在 periodic/Bloch/plane-wave/PAW, harmonic motion, Wannier interpolation, EPC 前提及拓扑迁移. 整段提供是为了避免拼接漏项, 不是要求推翻现有 2.6. 必须与第 6 节的拓扑迁移在同次集成中应用.

起点: `\section{From density functional theory to practical calculations}`.
终点: 原章末连接光学谱的段落, 在 `% draft` 注释之前.

候选 LaTeX:

```latex
\section{From density functional theory to practical calculations}
\label{sec:practical_computational_methods}

% opening paragraph
The previous sections established the density functional theory framework used in this thesis.
We now connect this framework to the calculations in the research chapters.
We start from the total energy and its derivatives,
which determine structural relaxation, lattice vibrations, and atomic motion.
We then introduce spin polarization and electron-phonon coupling.
Spin-orbit coupling and band topology are discussed in chapter~\ref{cha:fundamentals_c}.
The settings for individual systems are discussed in sections~\ref{1_calculation_methods}, \ref{2_methods}, and~\ref{3_methods}.

We retain the Hartree atomic units introduced in section~\ref{sec:manybody_schrodinger_equation}.
When discussing electron-phonon coupling and the transition temperature,
we restore $\hbar$ and $\kB$ explicitly to distinguish frequency, energy, and temperature.

\subsection{Structural relaxation and convergence}
\label{subsec:method_relaxation}

Firstly, we need an atomic structure for the calculation of electronic properties.
For fixed nuclear positions,
we solve the Kohn--Sham equations~\eqref{KS_equation_diagonal_dirac} together with the density relation~\eqref{density_with_occupation_number}.
This gives the electronic ground-state energy for the chosen structure.

Recall that equation~\eqref{absorbed_electronic_energy} separates the electronic energy $E$ from the nucleus-nucleus repulsion $E_\mathrm{NN}$.
When the nuclei move, both contributions change.
Therefore, the forces follow from the complete Born--Oppenheimer energy:

\begin{equation}
\left\{\begin{aligned}
    E_\mathrm{BO}(\{\vec{R}_I\})
    &= E(\{\vec{R}_I\})+E_\mathrm{NN}(\{\vec{R}_I\}) \\
    \vec{F}_I
    &= -\nabla_{\vec{R}_I}E_\mathrm{BO}(\{\vec{R}_J\})
\end{aligned}\right.
\label{BO_energy_and_force}
\end{equation}

here, $\vec{R}_I$ and $\vec{F}_I$ denote the position and force of nucleus $I$.
The electronic energy is evaluated self-consistently at each nuclear configuration.
The force therefore connects the electronic problem in equation~\eqref{BO_SE_with_ENN} to the motion of the nuclei.
When an empirical dispersion correction is included,
it must also enter the energy and its derivatives used for relaxation.

We then update the atomic positions and the lattice parameters allowed to vary.
For example, the electronic and force convergence criteria can be expressed as:

\begin{equation}
\left\{\begin{aligned}
    \left|E_\mathrm{SCF}^{(j)}-E_\mathrm{SCF}^{(j-1)}\right|
    &<\eta_E \\
    \max_I|\vec{F}_I|&<\eta_F
\end{aligned}\right.
\label{electronic_and_force_convergence}
\end{equation}

here, $j$ labels successive electronic iterations at fixed nuclear positions,
$E_\mathrm{SCF}^{(j)}$ denotes the energy evaluated at that iteration,
and $\eta_E$ and $\eta_F$ denote the chosen energy and force tolerances.
The first condition controls the electronic iteration,
whereas the second controls the residual forces during structural relaxation.
If lattice parameters are relaxed, the corresponding stress also needs to be converged.

However, satisfying these stopping criteria does not establish convergence with respect to the plane-wave cutoff or the sampling of reciprocal space.
We need to examine how these choices affect the physical quantity being compared.
For two-dimensional structures, the vacuum separation also controls the interaction between periodically repeated layers.
The treatment of dispersion interactions is particularly relevant to the interlayer geometry in chapter~\ref{cha:project_bilayers}.
The actual stopping criteria and numerical settings are given with the calculations in chapters~\ref{cha:project_bilayers}, \ref{cha:project_boron}, and~\ref{cha:project_beryllene}.

\subsection{Periodic states and Brillouin-zone sampling}
\label{subsec:method_kpoints}

Next, we consider the periodic electronic problem.
We label a Bloch state $\ket{\psi_{n\vec{k}}}$ by its band index $n$ and wave vector $\vec{k}$,
and denote its one-particle energy by $E_{n\vec{k}}$.
This is the periodic-system notation for the Kohn--Sham eigenvalue $\lambda_i$ in equation~\eqref{KS_equation_diagonal_dirac}.
It is also the band-energy notation used in chapter~\ref{cha:fundamentals_b}.

For a lattice translation $\vec{L}$, the periodicity of the one-particle operator allows us to write~\cite{martin2020electronic}:

\begin{equation}
\left\{\begin{aligned}
    \ket{\psi_{n\vec{k}}}
    &=\mathrm{e}^{\mathrm{i}\vec{k}\cdot\hat{\vec{r}}}\ket{u_{n\vec{k}}} \\
    \braket{\vec{r}+\vec{L}|u_{n\vec{k}}}
    &=\braket{\vec{r}\,|u_{n\vec{k}}}
\end{aligned}\right.
\label{bloch_state_cell_periodic_method}
\end{equation}

here, $\ket{u_{n\vec{k}}}$ is the cell-periodic part of the Bloch state,
and $\hat{\vec{r}}$ is the position operator.
The Bloch phase carries the change between cells, while the cell-periodic part contains the variation within a cell.
We normalize $\ket{u_{n\vec{k}}}$ over one unit cell;
the corresponding Bloch state has the same cell normalization.
This convention is also used for the electron-phonon matrix elements below.

To solve this periodic problem numerically, we need a finite basis.
In a plane-wave calculation, the rapidly varying orbitals near the nuclei are treated through a core-valence description.
The smooth auxiliary state $\ket{\widetilde{\psi}_{n\vec{k}}}$ can then be expanded as:

\begin{equation}
\left\{\begin{aligned}
    \ket{\widetilde{\psi}_{n\vec{k}}}
    &=\sum_{\vec{G}}C_{n\vec{k}}(\vec{G})\ket{\vec{k}+\vec{G}} \\
    \braket{\vec{r}\,|\vec{k}+\vec{G}}
    &=\frac{1}{\sqrt{\Omega_\mathrm{cell}}}
    \mathrm{e}^{\mathrm{i}(\vec{k}+\vec{G})\cdot\vec{r}}
\end{aligned}\right.
\label{plane_wave_expansion_method}
\end{equation}

here, $\vec{G}$ is a reciprocal-lattice vector,
$\Omega_\mathrm{cell}$ is the unit-cell volume,
and $C_{n\vec{k}}(\vec{G})$ is the expansion coefficient.
The plane waves form the basis; an individual Bloch state is generally a superposition of them.
In Hartree atomic units, we retain only the components satisfying:

\begin{equation}
    \frac{1}{2}|\vec{k}+\vec{G}|^2\leq E_\mathrm{cut}
\label{plane_wave_cutoff_method}
\end{equation}

here, $E_\mathrm{cut}$ is the plane-wave kinetic-energy cutoff.
Increasing it enlarges the basis at each k point.
This is different from increasing the number of k points,
which improves the integration over the Brillouin zone.

For the VASP calculations, the projector augmented wave (PAW) method connects the smooth auxiliary state to the reconstructed all-electron valence state~\cite{blochl1994projector,kresse1999ultrasoft}:

\begin{equation}
\begin{aligned}
    \ket{\psi_{n\vec{k}}}
    &=\ket{\widetilde{\psi}_{n\vec{k}}} \\
    &\quad+
    \sum_a\left(\ket{\phi_a}-\ket{\widetilde{\phi}_a}\right)
    \braket{\widetilde{p}_a|\widetilde{\psi}_{n\vec{k}}}
\end{aligned}
\label{PAW_reconstruction_method}
\end{equation}

here, $a$ labels an atomic site and a partial-wave channel,
$\ket{\phi_a}$ and $\ket{\widetilde{\phi}_a}$ are the all-electron and smooth partial waves,
and $\bra{\widetilde{p}_a}$ is the corresponding projector.
The correction restores the rapidly varying part inside the augmentation regions;
outside these regions, the two partial waves coincide.
The implemented calculation uses a frozen-core approximation and a finite partial-wave representation.
The smooth auxiliary density alone is therefore not the reconstructed all-electron density.
The Quantum ESPRESSO calculations for superconductivity in section~\ref{2_methods} instead use norm-conserving pseudopotentials~\cite{hamann2013optimized}.
The datasets and their convergence settings must be specified for each calculation.

Electronic quantities require integration over the Brillouin zone.
For a quantity $A(\vec{k})$, we approximate its Brillouin-zone average by:

\begin{equation}
    \frac{1}{\Omega_\mathrm{BZ}}
    \int_\mathrm{BZ}\dif^3{k}\,A(\vec{k})
    \approx \sum_{\vec{k}}w_{\vec{k}}A(\vec{k}),
    \qquad
    \sum_{\vec{k}}w_{\vec{k}}=1
\label{brillouin_zone_quadrature}
\end{equation}

here, $\Omega_\mathrm{BZ}$ denotes the Brillouin-zone volume of the periodic calculation,
and $w_{\vec{k}}$ denotes the normalized weight of each sampled point.
For a slab supercell, the in-plane mesh is refined while the sampling along the vacuum direction is usually restricted to one point.
The required mesh depends on the reciprocal-cell dimensions and the quantity of interest.
For a metal, the occupation changes near the Fermi energy make this integration more sensitive to the mesh and occupation broadening.
We therefore check their effect on the quantity of interest together.
A high-symmetry path used to display a band structure does not replace this integration mesh.

By increasing the sampling density, we examine the numerical accuracy of equation~\eqref{brillouin_zone_quadrature}.
However, a mesh that gives a converged total energy may still be insufficient for an optical spectrum.
In equation~\eqref{independent_particle_imaginary_dielectric_tensor} of chapter~\ref{cha:fundamentals_b},
the integrand also contains transition matrix elements and the energy difference $E_{c\vec{k}}-E_{v\vec{k}}$.
Therefore, optical convergence depends on the k-point mesh, the number of bands included, and the broadening of the transitions.
The research chapters discuss the meshes used for structural and optical calculations separately.

\subsection{Phonons and molecular dynamics}
\label{subsec:method_stability}

Once a structure is relaxed, we examine its response to small atomic displacements.
Let $u_{I\alpha}$ denote the displacement of nucleus $I$ along the Cartesian direction $\alpha$.
Starting from the force in equation~\eqref{BO_energy_and_force},
we define the harmonic force constants as:

\begin{equation}
    \Phi_{I\alpha,J\beta}
    \coloneqq
    \left.\frac{\partial^2E_\mathrm{BO}}
    {\partial u_{I\alpha}\,\partial u_{J\beta}}\right|_0
    =
    -\left.\frac{\partial F_{I\alpha}}{\partial u_{J\beta}}\right|_0
\label{harmonic_force_constants_method}
\end{equation}

here, the subscript $0$ denotes the relaxed reference structure.
The force constants describe the curvature of the same energy surface used for structural relaxation.
They can be obtained from finite-displacement calculations or density-functional perturbation theory~\cite{baroni2001phonons}.

At a stationary reference structure, the first derivative of the energy vanishes.
Keeping the terms up to second order in the displacements, we obtain:

\begin{equation}
\left\{\begin{aligned}
    E_\mathrm{BO}(\{u_{I\alpha}\})
    &\approx E_\mathrm{BO}(0)
    +\frac{1}{2}\sum_{I\alpha,J\beta}
    \Phi_{I\alpha,J\beta}u_{I\alpha}u_{J\beta} \\
    M_I\frac{\dif^2u_{I\alpha}}{\dif t^2}
    &=-\sum_{J\beta}\Phi_{I\alpha,J\beta}u_{J\beta}
\end{aligned}\right.
\label{harmonic_energy_and_motion_method}
\end{equation}

here, $M_I$ is the nuclear mass.
The second relation follows from the force as the negative energy gradient.
It shows that the force constants couple the displacements of different atoms.

For a periodic crystal, we write the nuclear index as $I=(l,\kappa)$,
where $l$ labels the cell and $\kappa$ labels the atom within the cell.
We seek a collective displacement with a definite wave vector and frequency:

\begin{equation}
    u_{l\kappa\alpha}(t)
    =\mathrm{Re}\left[
    \frac{Q_{\vec{q}s}}{\sqrt{M_\kappa}}
    e_{\kappa\alpha,s}(\vec{q})
    \mathrm{e}^{\mathrm{i}(\vec{q}\cdot\vec{L}_l-\omega_{\vec{q}s}t)}
    \right]
\label{phonon_normal_mode_method}
\end{equation}

here, $\vec{L}_l$ is the cell translation, $M_\kappa$ is the nuclear mass,
$\vec{q}$ is the phonon wave vector, and $s$ labels the mode.
The quantity $Q_{\vec{q}s}$ is the mass-weighted mode amplitude.
The factor $M_\kappa^{-1/2}$ separates the mass from the dimensionless eigenvector.
The real part gives the physical displacement.
Substituting this form into equation~\eqref{harmonic_energy_and_motion_method}
and using lattice translational symmetry,
we obtain the dynamical matrix and its eigenvalue equation:

\begin{equation}
\left\{\begin{aligned}
    D_{\kappa\alpha,\kappa'\beta}(\vec{q})
    &=
    \frac{1}{\sqrt{M_\kappa M_{\kappa'}}}
    \sum_l\Phi_{0\kappa\alpha,l\kappa'\beta}
    \,\mathrm{e}^{\mathrm{i}\vec{q}\cdot\vec{L}_l} \\
    \sum_{\kappa'\beta}
    D_{\kappa\alpha,\kappa'\beta}(\vec{q})
    e_{\kappa'\beta,s}(\vec{q})
    &=\omega_{\vec{q}s}^{2}e_{\kappa\alpha,s}(\vec{q})
\end{aligned}\right.
\label{phonon_dynamical_matrix_method}
\end{equation}

here, the eigenvector components $e_{\kappa\alpha,s}(\vec{q})$ describe the mass-weighted displacement pattern,
with normalization $\sum_{\kappa\alpha}|e_{\kappa\alpha,s}(\vec{q})|^2=1$.
The quantity $\omega_{\vec{q}s}$ is an angular frequency;
the ordinary frequency is $\omega_{\vec{q}s}/(2\pi)$.
Here, $\omega$ denotes a frequency, rather than the range-separation parameter used in section~\ref{sec:exchange_correlation_functional}.

A negative eigenvalue $\omega_{\vec{q}s}^{2}$ gives an imaginary frequency and indicates a harmonic instability of the reference structure.
Small imaginary frequencies require convergence checks before they can be attributed to numerical errors.
The absence of imaginary modes supports harmonic dynamical stability within the wave vectors and numerical accuracy examined.

We then turn to \textit{ab initio} molecular dynamics (AIMD).
In the Born--Oppenheimer approximation,
the electronic ground state determines the forces acting on the nuclei.
Before adding any thermostat terms, the classical nuclear equation of motion is:

\begin{equation}
    M_I\frac{\dif^2\vec{R}_I(t)}{\dif t^2}
    =
    \vec{F}_I(\{\vec{R}_J(t)\})
    =
    -\nabla_{\vec{R}_I}E_\mathrm{BO}(\{\vec{R}_J(t)\})
\label{born_oppenheimer_nuclear_motion}
\end{equation}

here, the electronic problem is solved at successive nuclear configurations to update the forces.
Phonons examine the local curvature of the energy surface,
whereas AIMD follows an atomic trajectory on that surface.
The trajectory tests whether the structure persists at the chosen temperature over the simulated time.
The ensemble, temperature control, time step, and duration must therefore be specified with each calculation.
These two methods address the boron and beryllene structures in chapters~\ref{cha:project_boron} and~\ref{cha:project_beryllene}.
Neither test alone establishes thermodynamic stability or experimental synthesizability.

\subsection{Spin polarization and magnetic ordering}
\label{subsec:method_magnetism}

In equation~\eqref{density_with_occupation_number}, the orbital index includes spin implicitly.
For a collinear spin-polarized calculation,
we now separate the spin-up and spin-down contributions:

\begin{equation}
\left\{\begin{aligned}
    n_\sigma(\vec{r}\,)
    &=\sum_i f_{i\sigma}\left|\braket{\vec{r}\,|\psi_{i\sigma}}\right|^2,
    \qquad \sigma\in\{\uparrow,\downarrow\} \\
    n(\vec{r}\,)&=n_\uparrow(\vec{r}\,)+n_\downarrow(\vec{r}\,) \\
    \Delta n(\vec{r}\,)&=n_\uparrow(\vec{r}\,)-n_\downarrow(\vec{r}\,)
\end{aligned}\right.
\label{spin_resolved_density_method}
\end{equation}

here, $\ket{\psi_{i\sigma}}$ denotes the spatial orbital in spin channel $\sigma$,
$f_{i\sigma}$ denotes its occupation,
and $\Delta n(\vec{r}\,)$ denotes the spin-density difference.
The position projection follows the coordinate representation in equation~\eqref{coordinate_representation_definition}.
In a periodic calculation, the orbital sum also includes the weighted k-point sampling in equation~\eqref{brillouin_zone_quadrature}.
The exchange-correlation energy then depends on both spin densities.
For a semilocal functional, the potential definition in equation~\eqref{xc_potential_definition} becomes:

\begin{equation}
    v_\mathrm{xc}^{\sigma}([n_\uparrow,n_\downarrow];\vec{r}\,)
    =
    \frac{\delta E_\mathrm{xc}[n_\uparrow,n_\downarrow]}
    {\delta n_\sigma(\vec{r}\,)}
\label{spin_dependent_xc_potential_method}
\end{equation}

here, each spin channel has its own exchange-correlation potential,
while the Hartree potential depends on the total density.
We accordingly solve equation~\eqref{KS_equation_diagonal_dirac} for the two spin channels and update their densities self-consistently.
For hybrid functionals, the generalized Kohn--Sham operator also contains the non-local exchange contribution discussed in section~\ref{sec:exchange_correlation_functional}.

Different initial spin arrangements allow us to examine competing magnetic solutions.
We compare their converged energies and local spin densities under consistent numerical conditions.
For ferromagnetic and antiferromagnetic configurations represented by cells of the same composition and size,
we can define the energy difference per atom as:

\begin{equation}
    \Delta e_\mathrm{AFM-FM}
    \coloneqq
    \frac{E_\mathrm{BO}^\mathrm{AFM}-E_\mathrm{BO}^\mathrm{FM}}
    {N_\mathrm{at}}
\label{magnetic_energy_difference_method}
\end{equation}

here, $N_\mathrm{at}$ denotes the number of atoms in each comparison cell.
A negative value favours the antiferromagnetic configuration within this comparison.
The normalization must be stated when reporting an energy difference,
and the numerical uncertainty must be small compared with that difference.

In chapter~\ref{cha:project_boron},
this comparison addresses the competing magnetic states of monolayer o-\ce{B14}.
A vanishing total spin moment alone does not distinguish an antiferromagnetic state from a non-magnetic state;
the local spin density is also required.
The lowest-energy solution among the configurations examined identifies the preferred state within that set,
but does not by itself establish magnetic order at finite temperature.

\subsection{Electron-phonon coupling and superconductivity}
\label{subsec:method_elph}

Lattice vibrations also perturb the Kohn--Sham potential in equation~\eqref{KS_potential_decomposition}.
Atomic displacement changes the external potential and induces a density response,
which also changes the Hartree and exchange-correlation contributions.
The same phonon eigenvectors obtained from equation~\eqref{phonon_dynamical_matrix_method}
describe the atomic displacement associated with this perturbation.
Density-functional perturbation theory gives both the phonon response and the first-order change in the self-consistent potential~\cite{baroni2001phonons}.

We now restore $\hbar$ explicitly, and keep $\omega_{\vec{q}s}$ as an angular frequency.
Using the cell-periodic parts $\ket{u_{n\vec{k}}}$ of the Bloch states, normalized over a unit cell,
we write the electron-phonon matrix element as~\cite{giustino2017electron}:

\begin{equation}
    g_{mn,s}(\vec{k},\vec{q})
    =
    \sum_{\kappa\alpha}
    \left(\frac{\hbar}{2M_\kappa\omega_{\vec{q}s}}\right)^{1/2}
    e_{\kappa\alpha,s}(\vec{q})
    \bra{u_{m,\vec{k}+\vec{q}}}
    \partial_{\vec{q}\kappa\alpha}\hat{v}_\mathrm{KS}
    \ket{u_{n\vec{k}}}_\mathrm{cell}
\label{electron_phonon_matrix_element_method}
\end{equation}

here, $\partial_{\vec{q}\kappa\alpha}\hat{v}_\mathrm{KS}$ denotes the cell-periodic part of the self-consistent perturbation operator generated by a unit-amplitude displacement of sublattice $\kappa$ along $\alpha$,
with cell dependence $\mathrm{e}^{\mathrm{i}\vec{q}\cdot\vec{L}_l}$.
The factor $\mathrm{e}^{\mathrm{i}\vec{q}\cdot\vec{r}}$ is removed from the perturbation before taking the cell matrix element.
Together with $e_{\kappa\alpha,s}(\vec{q})$,
the mass-dependent prefactor sets the zero-point displacement scale for that atom and mode.
The matrix element $g_{mn,s}(\vec{k},\vec{q})$ has the dimension of energy.
Zero-frequency rigid translations are excluded from this mode expression.
The matrix element therefore describes the scattering of an electron from $\ket{\psi_{n\vec{k}}}$ to $\ket{\psi_{m,\vec{k}+\vec{q}}}$ by the phonon $(\vec{q},s)$.
Direct evaluation on dense reciprocal-space grids is expensive.
We therefore first express the selected electronic subspace in a localized Wannier representation~\cite{pizzi2020wannier90}.
For a uniform mesh of $N_\mathrm{k}$ points in the full Brillouin zone, the transformation is:

\begin{equation}
    \ket{w_{a\vec{L}}}
    =\frac{1}{N_\mathrm{k}}\sum_{\vec{k}}
    \mathrm{e}^{-\mathrm{i}\vec{k}\cdot\vec{L}}
    \sum_n U_{na}(\vec{k})\ket{\psi_{n\vec{k}}}
\label{wannier_transformation_method}
\end{equation}

here, $a$ labels a Wannier orbital and $\vec{L}$ labels its cell.
The matrices $U(\vec{k})$ mix the chosen Bloch states to obtain a smooth, localized representation.
For an isolated set of bands, this mixing is unitary within that set.
For entangled bands, a subspace must first be selected within the chosen energy windows.
The factor $1/N_\mathrm{k}$ follows from the cell-normalized Bloch states introduced in equation~\eqref{bloch_state_cell_periodic_method};
the Wannier states are normalized over the corresponding $N_\mathrm{k}$-cell Born--von Karman supercell.

We can then express the one-particle operator by matrix elements between localized orbitals:

\begin{equation}
\left\{\begin{aligned}
    h_{ab}(\vec{L})
    &=\bra{w_{a\vec{0}}}\hat{h}_\mathrm{KS}\ket{w_{b\vec{L}}} \\
    h_{ab}^{\mathrm{W}}(\vec{k})
    &=\sum_{\vec{L}}\mathrm{e}^{\mathrm{i}\vec{k}\cdot\vec{L}}h_{ab}(\vec{L})
\end{aligned}\right.
\label{wannier_hamiltonian_interpolation_method}
\end{equation}

here, $h_{ab}(\vec{L})$ couples orbitals separated by a lattice translation,
and $h_{ab}^{\mathrm{W}}(\vec{k})$ is the interpolated matrix in the Wannier basis.
When the real-space matrix elements are sufficiently localized,
this Fourier sum can be evaluated on a finer mesh.
Diagonalizing it gives the interpolated band energies and the transformation back to the band basis.
The interpolation must be checked against direct calculations in the energy range of interest.

The electron-phonon perturbation also carries the phonon wave vector $\vec{q}$.
Its matrix elements therefore require Fourier transformations with respect to both $\vec{k}$ and $\vec{q}$,
together with the phonon eigenvectors and the electronic band rotations~\cite{giustino2007electron}.
EPW uses this localized representation to obtain the matrix elements on finer electronic and phonon meshes~\cite{ponce2016epw}.
Interpolating the band energies alone would not provide the coupling in equation~\eqref{electron_phonon_matrix_element_method}.

For a spin-degenerate metallic normal state with $N(E_\mathrm{F})>0$,
we use the density of states per unit cell and per spin at the Fermi energy.
With independently normalized weights $\sum_{\vec{k}}w_{\vec{k}}=\sum_{\vec{q}}w_{\vec{q}}=1$,
the Fermi-surface average gives the Eliashberg spectral function:

\begin{equation}
\begin{aligned}
    \alpha^2F(\omega)
    &=
    \frac{1}{N(E_\mathrm{F})}
    \sum_{mn,s}\sum_{\vec{k},\vec{q}}
    w_{\vec{k}}w_{\vec{q}}
    |g_{mn,s}(\vec{k},\vec{q})|^2 \\
    &\quad\times
    \delta(E_{n\vec{k}}-E_\mathrm{F})
    \delta(E_{m,\vec{k}+\vec{q}}-E_\mathrm{F})
    \delta(\hbar\omega-\hbar\omega_{\vec{q}s}), \\
    N(E_\mathrm{F})
    &=\sum_{n,\vec{k}}w_{\vec{k}}\,
    \delta(E_{n\vec{k}}-E_\mathrm{F})
\end{aligned}
\label{eliashberg_spectral_function_method}
\end{equation}

here, the band sums use the same per-spin convention as $N(E_\mathrm{F})$.
The first two delta functions select electronic states at the Fermi energy,
while the last selects the phonon energy.
The weights follow the Brillouin-zone normalization in equation~\eqref{brillouin_zone_quadrature}.
With the energy delta function written in this form, $\alpha^2F(\omega)$ is dimensionless.
In numerical calculations, the delta functions are replaced by a specified integration or broadening procedure.
A spin-polarized reference requires a consistent spin-resolved treatment.

We then obtain the coupling strength and logarithmic average frequency from the same spectral function:

\begin{equation}
\left\{\begin{aligned}
    \lambda
    &=2\int_0^\infty\dif{\omega}\,
    \frac{\alpha^2F(\omega)}{\omega} \\
    \omega_\mathrm{log}
    &=\omega_\mathrm{ref}
    \exp\left[
    \frac{2}{\lambda}
    \int_0^\infty\dif{\omega}\,
    \frac{\alpha^2F(\omega)}{\omega}
    \ln\left(\frac{\omega}{\omega_\mathrm{ref}}\right)
    \right]
\end{aligned}\right.
\label{electron_phonon_spectral_moments}
\end{equation}

here, $\lambda$ is the dimensionless electron-phonon coupling strength,
rather than the one-particle eigenvalue $\lambda_i$ used earlier.
The positive reference frequency $\omega_\mathrm{ref}$ makes the logarithm dimensionless.
It cancels from $\omega_\mathrm{log}$ when the first relation is used.
These expressions assume a well-defined spectrum of stable phonon modes and $\lambda>0$.

For the commonly used simplified Allen--Dynes expression,
the transition temperature is estimated as~\cite{allen-dynes}:

\begin{equation}
    T_\mathrm{c}^{\mathrm{AD}}
    =
    \frac{\hbar\omega_\mathrm{log}}{1.20\kB}
    \exp\left[
    -\frac{1.04(1+\lambda)}
    {\lambda-\mu^*(1+0.62\lambda)}
    \right]
\label{allen_dynes_temperature_estimate}
\end{equation}

here, $\mu^*$ denotes the dimensionless screened Coulomb pseudopotential.
The factor $\hbar\omega_\mathrm{log}/\kB$ converts the phonon frequency scale into a temperature.
This simplified expression omits the additional strong-coupling and spectral-shape correction factors of the full Allen--Dynes formula.
Its applicability must be checked for the system considered;
in particular, it should not be extrapolated through a zero or negative denominator in the exponent.

The anisotropic Migdal--Eliashberg treatment retains the band, momentum, and frequency dependence of the coupling instead of reducing it to these spectral averages~\cite{margine2013anisotropic}.
It determines the superconducting gap $\Delta_{n\vec{k}}(\mathrm{i}\omega_j,T)$ together with the electronic renormalization function.
Here, $\omega_j=(2j+1)\pi\kB T/\hbar$ denotes a fermionic Matsubara frequency, with integer $j$.
The averaged function $\alpha^2F(\omega)$ alone does not retain the information required for this anisotropic calculation.
The transition is determined from the disappearance of the non-zero gap solution upon increasing temperature.
The corresponding $T_\mathrm{c}$ is therefore a separate result from equation~\eqref{allen_dynes_temperature_estimate}.

Chapter~\ref{cha:project_boron} compares bulk, monolayer, and hydrogen-terminated bilayer o-\ce{B14}.
Section~\ref{2_superconducting} reports the coupling strengths and transition temperatures.
The electronic reference state, fine meshes, spectral integration, Coulomb pseudopotential, and form of the transition-temperature estimate must be identified with those results.

At this stage, we have connected the electronic ground-state framework to structural, vibrational, magnetic, and superconducting calculations.
We now turn to chapter~\ref{cha:fundamentals_b},
where the same electronic states enter the response to an external electromagnetic field.
The transition matrix elements and energy-conservation condition in equations~\eqref{independent_particle_imaginary_dielectric_tensor} and~\eqref{dirac_energy_conservation_condition}
connect these states to the optical spectra examined in the research chapters.
```

## 6. 拓扑迁移是 C2-08 的明确依赖

新章目前尚未存在于正式 `thesis.tex` 中.
本稿采用拟定的新文件 `src/fundamentals_c.tex` 和 label `cha:fundamentals_c`.
不能先删除旧 2.6.6、写入新引用, 却把新章留空或忘记纳入主文件.

迁移按以下顺序准备, 在同一次集成中完成:

1. 将当前 `fundamentals_a.tex` 中从
   `\subsection{Spin-orbit coupling and band topology}`
   到 `A non-trivial product alone does not establish a topological insulator.`
   的完整内容移入新文件. 不移动后面连接 Chapter 3 的章末段落.
2. 新文件使用下面的章头; 将原 subsection 升为 section 即可作为迁移落点,
   保留原 `subsec:method_topology` label. 新章的进一步展开另行处理,
   本稿不把这两页迁移种子当作已完成的新章全文.

```latex
\chapter{Fundamentals \textRoman{3}: Band Topology}
\label{cha:fundamentals_c}
```

3. 原拓扑小节头两句改为下面的显式回指, 后面
   `With spin-orbit coupling, these components can mix.` 及其推导保留:

```latex
We start from the one-particle description in equation~\eqref{KS_equation_diagonal_dirac} of chapter~\ref{cha:fundamentals_a}.
In the collinear treatment in subsection~\ref{subsec:method_magnetism}, the two spin channels are treated separately.
```

4. 新章保留且只定义一次以下原 label:
   `subsec:method_topology`, `KS_spinor_equation_method`,
   `isolated_band_subspace_method`, `Fu_Kane_parity_criterion_method`.
   spinor、固定带数、全 BZ 直接带隙条件、每个 Kramers pair 取一次宇称等内容都随原文迁移.
5. 在 `thesis.tex` 中紧接 `\input{src/fundamentals_b.tex}` 后纳入:

```latex
\input{src/fundamentals_c.tex}
```

6. 同次应用 C2-08, 从 Chapter 2 移除原拓扑全文,
   保留其导言中的跨章指引和章末自然通向光学的过渡.
   新文件的创建、主文件的纳入、旧正文的移除及导航更新一起提交, 避免中间状态断引用或 label 重复.
7. 更新 Introduction 的 thesis organisation, 并回查 Chapter 3 收尾.
   原三个研究章将由 4/5/6 变为 5/6/7, 结论由 7 变为 8.
   语义 label 不改名; 检查 `src/publications.tex`、声明、图注和回复信中的手写章号.
   回复引用 examiner 原文时保留其原章号, 再说明修改后的对应位置.

如果新拓扑章尚未准备好, 可先完成 C2-01 至 C2-07.
对于 C2-08 的方法补充, 可以先合入新增的计算讲述,
但暂时保留原 2.6.6 和原有拓扑范围句, 不加入未定义的 `cha:fundamentals_c` 引用.
这只是有序集成的过渡状态; 最终目标仍是本稿确定的三个基础章节分工.

Chapter 2 的迁移不能替研究章验证金属体系的拓扑结论.
具体带子空间、SOC、对称性、全 BZ 隔离证据及宇称结果仍由 beryllene 研究章回答.

## 7. 与 Chapter 3 的唯一条件性指标联动

当前 Chapter 3 的 IPA 公式仍使用 v/c 指标,
所以 C2-08 完整候选保留当前的 $E_{c\vec{k}}-E_{v\vec{k}}$,
这在当前两个源文件之间并不构成不一致.

当 [Chapter 3 措施稿](ai_ch3_last.md) 中一般能带 n/m 和占据差的 IPA 修订实际应用时,
同步将 2.6.2 对应的两句替换为:

```latex
In equation~\eqref{independent_particle_imaginary_dielectric_tensor} of chapter~\ref{cha:fundamentals_b},
the integrand also contains occupation factors, transition matrix elements,
and the energy difference $E_{m\vec{k}}-E_{n\vec{k}}$.
```

前后的 optical convergence 说明保留.
Chapter 3 的自有例图来源、厚度、频率换算、光学图件和带内项仍由 Chapter 3 方案处理,
不因为本稿补了 k 点积分就标记为已解决.

## 8. 知识核验及不从参考稿猜填的事实

本稿核对了以下关键约定:

- Bloch 态与 cell-periodic 态按单胞归一; Wannier 变换使用完整 BZ 的均匀网格,
  因而采用 1/N_k, Wannier 态在对应的 N_k 胞 Born–von Karman 晶体中归一.
  不将不可约 k 点权重直接塞入这个离散 Fourier 变换.
- 平面波 cutoff 用 Hartree atomic units 的 |k+G|²/2;
  平滑辅助态与 PAW 重建态分开, 不声称两者具有相同的普通范数或密度.
- 核位移采用质量加权正常模, 与既有动力学矩阵和 EPC 中的本征矢约定一致.
  phonons 判断谐近似动力学稳定性, AIMD 判断所模拟温度和时段内的结构保持.
- EPC 使用 per-cell、per-spin 的 N(E_F), 单独归一的 k/q 权重,
  以及能量 delta 函数 δ(ħω−ħω_qs). 对应的 α²F(ω) 无量纲,
  与 λ、ω_log 和显式含 ħ/k_B 的温度式相容.
- 费米面平均限定为 N(E_F)>0 的自旋简并金属正常态.
  不把 HSE06 AFM 半导体与另一路 PBE/QE 超导参考态未经核查视作同一状态.
- 保留简化 Allen–Dynes 与各向异性 Migdal–Eliashberg 的区别,
  不用平均 α²F 代替各向异性输入, 不将 Allen–Dynes 公式外推到非正分母.

知识核验来源包括:

- [VASP 对 plane-wave cutoff 的定义](https://vasp.at/wiki/ENCUT),
  与既有 `martin2020electronic` 配合核查周期性基底及数值离散.
- [Blöchl, PAW 原始论文](https://doi.org/10.1103/PhysRevB.50.17953)
  与 [VASP PAW formalism](https://vasp.at/wiki/Projector-augmented-wave_formalism),
  对应现有 `blochl1994projector`、`kresse1999ultrasoft`.
- [Seidl et al., generalized Kohn–Sham](https://doi.org/10.1103/PhysRevB.53.3764),
  核对 local KS 与 hybrid GKS 的区别; 正文仍沿用现有 HSE 文献, 不新造引用键.
- [Baroni et al., DFPT](https://doi.org/10.1103/RevModPhys.73.515),
  对应现有 `baroni2001phonons`.
- [Pizzi et al., Wannier90](https://doi.org/10.1088/1361-648X/ab51ff)
  和 [Giustino et al., electron–phonon Wannier interpolation](https://doi.org/10.1103/PhysRevB.76.165108),
  对应 `pizzi2020wannier90` 和 `giustino2007electron`.
- [EPW theory](https://docs.epw-code.org/Theory.html)
  与现有 `giustino2017electron`、`margine2013anisotropic`、`ponce2016epw`,
  核查 EPC 的归一化和超导方法的分工.

Gemini 的主题安排可参考, 但以下事实不沿用其第一稿:

- 不将 VASP/PAW 与 QE/norm-conserving 写成同一套核价处理.
- 不将 beryllene 的 105×105×1 光学网格套给 heterostructure 研究章.
- `NBANDS` 是计算的总能带数, 不自动等于未占据带数.
- 当前 boron 方法段已经写有 μ*=0.13、45 Ry 和部分 k/q 网格;
  这些是待对照记录的现有设置, 不是可用典型值猜填的空白.
- 不猜填 AIMD 系综、热浴、步长或时长.
- 不把 SOC/宇称计算软件改写为 QE; 当前 beryllene 路线写的是 VASP 与 irvsp.

## 9. 仍由研究章节完成的回查

这里用研究章的 label 指认对象, 不依赖迁移前后的数字:

1. `cha:project_bilayers`: 各泛函和各物理量的结构、能带数、cutoff、k 网格与收敛依据;
   HSE06 精度措辞和光子能量/角频率约定与基础章一致.
2. `cha:project_boron`: 实际 EPC 正常态、coarse/fine k/q 网格、Wannier 窗口和插值验证,
   谱积分、展宽、μ*、ω_log、Allen–Dynes 形式及各向异性温度判据.
   当前 λ=0.05 和 μ*=0.13 给简化 AD 式非正分母, 不能机械代入后宣称极低 T_c;
   原结论依据在对应结果处说明.
3. `cha:project_boron`: AFM–FM 能差的归一单位和误差尺度,
   光学计算实际使用的结构、磁态、泛函和带内处理.
4. `cha:project_boron` 与 `cha:project_beryllene`: 声子超胞、虚频收敛、AIMD 实际设置与图件身份.
   通用方法说明不能替代真实轨迹信息, 也不能据此声称 thermodynamic stability 或 synthesizability.
5. `cha:project_beryllene`: PBE-only 的实际理由, 新结构生成方法,
   能带子空间及全 BZ 拓扑条件, 二维光学归一化和氢化选择依据.
   本稿保留的 `We discuss this choice...` 必须在该章真正落实后才能关闭.
6. `cha:fundamentals_b`: 执行第 7 节的指标联动, 并按 Chapter 3 措施稿处理作者自算例图来源及图件修正.

这些回查项既不要求在 Chapter 2 再写一遍, 也不预设一律补算.
它们由原始输入输出、数据与相应正文共同决定.

## 10. 应用后的完成标准

1. 按 C2-01 至 C2-08 核对实际修改; 唯一纯删重是两句 Hartree 引入,
   原公式、label、例子和互补推导没有被误删.
2. 逐项检查 2.6 的输入、核心关系、输出、适用前提和研究章联系.
   核查 Bloch/plane-wave、正常模、Wannier 三条新增联系均有符号解释和后文用途.
3. 新拓扑章纳入后, Chapter 2 的指引存在真实目标,
   四个旧拓扑 label 只出现一次, 所有语义引用保留且编号自动更新.
4. 确认 Chapter 3 IPA 是否已应用, 仅在实际应用时同步第 7 节.
5. 编译实际整篇 thesis, 检查未定义/重复 label、文献、公式越界、章节分页及手写章号.
   不能用临时片段检查代替正式全篇最终验证.
6. 回复信按真实状态区分方法补充、局部纠错、直接删重和内容迁移.
   不把原稿保留说成完成了广泛压缩, 不把理论条件说成材料已经满足,
   不把本措施稿交付说成正式正文已经应用.

## 11. 本次措施稿交付前的核验记录

本轮核验针对本文件的候选与操作完整性, 不代表正式正文已经应用.

- 八个 C2 操作均以当前源码中的唯一原句为锚点.
  从本措施稿实际提取八个代码块, 按删除/替换规则重建的候选,
  与接受独立审阅和编译的候选逐字一致.
- 当前 Chapter 2 的 291 个 label 全部保留在 Chapter 2 或明确迁移的拓扑内容中.
  迁移后的集合没有重复定义; 新增八个方法公式 label 及一个新章 label.
  候选所用 cite keys 均存在于当前文献库.
- 方法与风格分别完成独立复核.
  重点检查了 Wannier 的 1/N_k 归一化、平面波 cutoff、PAW 态的区别,
  正常模与动力学矩阵、EPC 的自旋/网格/频率约定及 Dirac notation.
- 使用当前真实 thesis 主文件和模板, 在临时目录进行整篇集成编译.
  将既有拓扑段落放到临时新章以验证迁移, 没有把该迁移落点当作新 Chapter 4 的定稿.
  候选完成 LaTeX/Biber/LaTeX/LaTeX 编译, 没有未定义引用、未定义文献或重复 label.
- 同时重新编译未修改的当前正文作基线.
  两者均有相同的 10 条 overfull 提示及同类模板/单位宏提示;
  本候选没有新增这些提示. 本轮没有顺带修改原有提示对应的其他正文或参考文献.
- 逐页检查候选中的印刷页 88–98 (完整 2.6) 和第 36 页的相位修正.
  新公式与文字可读, 没有发现新增的裁切、重叠或越界.
  候选整篇临时 PDF 为 292 页, 基线为 288 页.
  这个数值只对应“本稿候选 + 既有拓扑段落迁移”的测试组合,
  不是未来拓扑章展开后的最终页数, 也不是正式 .output 的新页数.
- 对正式 Chapters 1–3、主文件、文献库、Gemini 初稿、二次稿、Chapter 3 措施稿,
  Ollie PDF、当前 .output/thesis.pdf 和回复信记录了 11 个 SHA-256 校验值;
  交付前全部保持一致. 本轮唯一写回的正式文件是本措施稿.

交付状态: 最终措施稿已覆盖; 正式正文、图件、文献库和 .output 尚未应用本稿.
