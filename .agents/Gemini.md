# Gemini

## 0919 博士学位论文修改综合指导方案与答辩修改措施

学位论文题目: Exploring Quantum Properties of Light-Element Xenes: DFT Studies of the
Electronic Structure and Optical Response for Boron and Beryllium Allotropes
答辩候选人: Lu Niu (牛璐)
指导教师: Prof. Catherine Stampfl
评审结果: awarded the degree subject to corrections of the thesis to the
satisfaction of the University (通过答辩, 需根据评审意见进行修改并经审核满意后授予学位)

---

### 目录

- 1\. 评审意见综合评述与整体战略规划
- 2\. Chapter 1 (Introduction): 宏观叙事整合与系统性文献综述构建
- 3\. Chapters 2 & 3 (Theory & Methodology): 篇幅精简, 附录迁移与实用计算方法路线图
- 4\. Chapter 4 (Graphene-Boron Heterostructures): 题注自洽化, 图像清晰度重构与作者贡献说明
- 5\. Chapter 5 (Penta-Bipyramid Boron o-B14): 物理自洽性修正, 概念澄清与超导计算流程规范
- 6\. Chapter 6 (Beryllene Phases): 三层立方相构建, 金属拓扑论证与计算细节补全
- 7\. Chapter 7 (Conclusion and Outlook): 理论局限性批判反思, 实验现状对照表与明确未来展望
- 8\. 针对两位评审人的逐条答复信草案 (Formal Point-by-Point Reply Letter)
- 9\. 论文修改操作清单与检查核对表 (Action Checklist)

---

### 1. 评审意见综合评述与整体战略规划

#### 1.1 评审人核心关注点与问题诊断

两位评审专家对论文的原创性计算工作, 论文发表记录(已发表 2 篇高质量期刊论文, 1 篇在投)给予了充分肯定, 一致认为论文达到了博士学位的学术标准. 但两位评审
人不约而同地指出了论文在行文组织, 宏观主线, 方法学呈现方式, 以及部分物理概念界定上的明显短板:

```text
| 维度 | Examiner 1 核心评审意见 | Examiner 2 核心评审意见 | 核心症结诊断 |
| :--- | :--- | :--- | :--- |
| 论文宏观主线 (Thesis Cohesion) | 各研究章节显得在不同材料间跳跃 (hopping), 缺乏内在纽带; 文献综述未能提炼出尖锐的研究空白
(sharp research gap). | 缺少独立的,系统批判性的文献综述; 需深入总结 2D 硼,铍体系的研究现状与理论方法空白. | 第 1 章过短(
仅 4 页), 沦为背景简介与各章摘要汇总, 缺少统领全篇的材料物理学主线. |
| 理论与方法篇幅 (Ch 2 & Ch 3) | 篇幅过度冗长(占全书约 100 页), 充斥教科书式形式推导; 却缺少后续计算实际采用的实用计算方法路线图.
| 整体像教科书; 自第 100 页起关于 alpha- 和 beta-beryllene 的光学性质示例未标明数据来源与引用. | 理论推导与后文计算严重脱节
; 详略失衡(理论推导太细, DFT 参数策略反被弱化); 示例数据归属模糊. |
| 异质结计算 (Chapter 4) | 图 4.29-4.36(即 SI 图 S1.17-S1.24)题注过于简短, 不具备自洽性
(self-contained); 光学计算缺乏明确物理动机. | 多合一复合图(如 Figures 4.29, 4.30)在打印版中字体太小,图例模糊不可读;
需增加作者贡献声明. | 题注只有两三个单词; 图件排版压缩过甚; 合作论文贡献未明示. |
| 五角双锥硼 (Chapter 5) | 单层基态表述自相矛盾(前文称 AFM 半导体, 光学讨论称金属); HSE06 机制未解释透; 超导流程缺乏可复现描
述; 稳定性过度宣称. | 图 5.1(原子结构)出现太晚, 应在方法/引言部分先行呈现, 以便读者理解后续模型. | 电子/光学物理状态处理不自洽; 形成能/
声子/5.5 ps AIMD 被直接推断为实验可合成性存在逻辑跳跃; 超导计算细节缺失. |
| 二维铍相 (Chapter 6) | 新立方三层相构建方法未交待; 金属体系定义 Z2 拓扑不变量缺乏物理依据; 缺乏 2D 光学归一化与合成性区分. |
唯独该章仅用 GGA-PBE 而未做 HSE06, 缺乏正当解释; 收敛性测试未在正文讨论; 图 6.2/6.3 原子分色未释; AIMD 参数缺失; 加氢理由
未明. | 新相建模缺乏晶体学起源; 费米面跨越时 Z2 拓扑概念缺乏严格界定; 计算方案缺乏正当性辩护; 参数遗漏. |
| 结论与展望 (Chapter 7) | 需明确区分理论预测与已被实验合成验证的材料体系. | 结论过于像各章摘要罗列, 缺少对 DFT/理论近似局限性的批判
性反思; 未来工作过于宽泛空洞. | 结论缺乏方法学批判力(未讨论单粒子近似,激子效应,自由悬浮模型与衬底效应); 未来工作缺少明确预期. |
```

#### 1.2 修改基本原则与实施策略

- 原则一: 严控修改边界. 根据您的要求, 所有 LaTeX 源文件(.tex), 插图文件及文献库由您亲自修改, 本方案提供详尽的中英文对照设计, 重构方案, 替换
  文本草案与答辩回复信.
- 原则二: 大开大合调结构(减法与加法).
  - 减法: 将 Chapters 2 & 3 中过于繁琐的基础教材推导剥离至新增的 Appendix B / C(预计削减 40-50 页正文), 大幅提升
    正文紧凑度.
  - 加法: 扩写 Chapter 1(增加 Dedicated Literature Review, 系统建立轻元素 Xenes 中通过配位键合拓扑, 维度降
    低与表面氢化调控量子态的统一学术主线, 扩写至 12-15 页); 补齐 Chapter 2/3 的 Practical Computational
    Roadmap; 充实各章图注与方法细节.
- 原则三: 科学表述严谨化(精准定性). 严格区分动力学稳定 (Dynamical stability, 无虚频声子), 能量偏好 (Energetic
  preference, 内聚能/吸附能), 热力学稳定 (Thermodynamic stability, 凸包 Convex Hull) 与实验可合成性
  (Experimental synthesizability). 修正金属相光学带内跃迁 (Drude), 金属态 Z2 拓扑指标定义的物理准确性.

---

### 2. Chapter 1 (Introduction): 宏观叙事整合与系统性文献综述构建

#### 2.1 中文问题诊断与重构指导

- 问题根源: 原 Chapter 1 仅 74 行(约 4 页), 只简单列举了石墨烯背景以及后面三章的摘要, 两位评审人均敏锐指出没有独立的
  Literature Review, 没有回答为什么这三种体系要放在同一篇论文中.
- 重构主线 (The Unifying Narrative):
  必须为全篇论文建立清晰的物理逻辑框架:
  - 核心科学议题: 在无重金属原子(即无内禀强自旋-轨道耦合 SOC)的轻元素二维体系中, 电子关联, 对称性, 键合拓扑与表面修饰如何共同诱发诸如非常规超导,
    磁性, 拓扑非简并态以及极化敏感光学/等离激元响应等量子现象?
  - 三部曲的内在递进逻辑:
    - Chapter 4 (范德华界面工程与键合杂化): 从二维原型的代表--石墨烯出发, 探索将石墨烯与轻元素缺电子硼 (Borophene) 及二元硼
      碳化物 (BC3, B4C3) 构建范德华异质结. 研究重点是界面弱耦合与层间电荷重新分布如何打破反演对称性并调控肖特基势垒与等离激元模式.
    - Chapter 5 (内禀复杂多中心键合拓扑与多自由度调控): 从外禀堆垛异质结深入到单质硼内部独特的缺电子五角双锥多中心键网络 (o-B14). 探
      索维度降低 (Bulk -> Bilayer -> Monolayer) 与表面氢化如何激活晶格振动与电子结构的强烈重整, 从而在单一纯硼相中实现从
      反铁磁半导体到高达 24.3 K 的声子介导超导电性.
    - Chapter 6 (极轻金属体系的原子构型相空间与非平庸拓扑): 进一步将元素推向最轻的碱土金属--铍 (Beryllium). 在极端轻质, 强电子
      离域与弱自旋-轨道耦合背景下, 探索二维铍相 (alpha, beta 以及新发现的立方三层相) 中由晶格对称性与轨道反转 (Orbital
      Inversion) 主导的非平庸拓扑能带结构 (Z2 不变量) 与反常光学向列性.
  - 明确光学性质计算的物理意义: 介电函数, 吸收系数, 能量损失谱不仅仅是一组数值输出, 而是探测二维电子关联, 带间带内能级跃迁, 对称性破缺引起的各向异性极化
    , 以及低能元激发 (等离激元 Plasmon) 的核心物理探针.
  - 拓扑与 Z2 不变量的先导性引入: 在第 1 章明确阐释为什么在轻元素中寻找非平庸拓扑具有重要物理价值(不依赖重元素重 SOC, 而是通过轨道杂化与晶格
    对称性保护), 以及非平庸 Z2 不变量对应的物理可观测量(无耗散边缘传导通道与量子自旋霍尔效应预期).

#### 2.2 英文实操建议文本 (用于修改扩写 Chapter 1)

##### (A) 论文核心研究空白与动机陈述 (Central Motivation and Research Gaps)

```latex
\section{Central Motivation and Research Gaps}
\label{sec:intro_motivation}

While two-dimensional (2D) materials have revolutionized modern condensed-matter
physics, the overwhelming majority of research has focused on graphene,
transition-metal dichalcogenides (TMDs), and heavy-element group-IV/V Xenes
(such as silicene, germanene, and phosphorene). In contrast, atomically thin
materials composed exclusively of the lightest elements in the periodic
table---specifically boron ($Z=5$) and beryllium ($Z=4$)---represent an
uncharted territory governed by distinctly different bonding physics.

Boron, being inherently electron-deficient with three valence electrons ($2s^2
2p^1$), cannot satisfy the classical octet rule in a planar honeycomb lattice.
Instead, it relies on complex multicentre two-electron ($3c\text{--}2e$) bonds,
giving rise to an exceptionally rich polymorphism of competing atomic
arrangements ranging from triangle-hexagon borophene sheets to icosahedral and
penta-bipyramidal clusters. Similarly, beryllium ($2s^2$), as the lightest
alkaline-earth element, exhibits pronounced $s\text{--}p$ orbital hybridization
upon dimensional reduction, transforming from a simple divalent metal into a
low-dimensional platform hosting unconventional thermal transport, strong
electron-phonon interactions, and symmetry-protected electronic states.

Despite theoretical interest, three critical research gaps remain unresolved in
the literature:
\begin{enumerate}
    \item \textbf{Interfacial vs. Intrinsic Tuning in Boron-Carbon
    Architectures:} While graphene is chemically inert and semimetallic,
    combining it with boron-based and boron-carbide monolayers ($\mathrm{BC}_3$,
    $\mathrm{B}_4\mathrm{C}_3$) via van der Waals forces offers an unexplored
    pathway to engineer visible-range optical activity and plasmonic modes
    without destroying Dirac physics. However, systematic first-principles
    benchmarks comparing standard semilocal and hybrid functional treatments of
    interfacial screening and Schottky barriers are lacking.
    \item \textbf{Dimensionality and Hydrogenation in Complex Boron Allotropes:}
    Although planar borophene phases have been synthesized on metallic
    substrates, the quantum properties of complex 3D allotropes when thinned to
    the 2D limit remain largely unexplored. Specifically, whether the
    edge-sharing pentagonal bipyramids of $o\text{-}\mathrm{B}_{14}$ can sustain
    magnetic ordering, high-temperature superconductivity, or directional
    plasmonics under chemical functionalization has not been established.
    \item \textbf{Emergent Topology and Light-Metal Beryllenes:} Conventional
    topological insulators rely fundamentally on heavy elements with strong
    atomic spin--orbit coupling (SOC) to invert bands. Whether elemental
    beryllium allotropes can host non-trivial topological phases driven
    primarily by lattice symmetry and $s\text{--}p$ orbital parity
    inversion---without relying on heavy elements---represents a fundamental
    question at the frontier of topological materials science.
\end{enumerate}

This thesis addresses these interconnected questions through rigorous,
state-of-the-art first-principles calculations, establishing a coherent paradigm
of how atomic geometry, dimensional reduction, and surface termination dictate
electronic, optical, superconducting, and topological phases in light-element
Xenes.
```

##### (B) 宏观篇章逻辑纽带 (Unifying Cohesive Framework Across Chapters 4, 5, and 6)

```latex
\section{Structure of the Thesis: A Cohesive Narrative}
\label{sec:intro_cohesive_structure}

The investigations presented in Chapters~\ref{cha:project_bilayers},
\ref{cha:project_boron}, and \ref{cha:project_beryllene} form a progressive,
three-stage exploration of quantum phenomena in light-element low-dimensional
systems:

\begin{itemize}
    \item \textbf{Stage 1: Extrinsic Engineering via Van der Waals
    Heterostructures (Chapter~\ref{cha:project_bilayers}).}
    Starting from the prototypical 2D material, graphene, this chapter explores
    how weak interlayer van der Waals coupling with planar borophene and
    semiconducting boron carbides ($\mathrm{BC}_3$, $\mathrm{B}_4\mathrm{C}_3$)
    redistributes interfacial charge. This establishes how extrinsic
    layer-stacking modifies the dielectric tensor, induces low-energy plasmons,
    and generates symmetry-broken off-diagonal optical activity.

    \item \textbf{Stage 2: Intrinsic Topological Bonding and Multifunctional
    Ground States (Chapter~\ref{cha:project_boron}).}
    Progressing from planar heterojunctions to an intrinsic, complex boron
    framework, this chapter investigates the penta-bipyramidal
    $o\text{-}\mathrm{B}_{14}$ system. By systematically reducing the
    dimensionality from bulk to bilayer and monolayer, and subsequently
    passivating dangling bonds with hydrogen, we demonstrate how multicentre
    bonding enables the coexistence of antiferromagnetism, directional plasmons,
    and phonon-mediated superconductivity with $T_c \approx 24.3$~K in a single
    elemental system.

    \item \textbf{Stage 3: Symmetry-Driven Topology and Low-Dimensional Metal
    Allotropes (Chapter~\ref{cha:project_beryllene}).}
    Extending the paradigm to the lightest metal, beryllium, this chapter pushes
    the boundary of light-element physics into the realm of band topology. By
    investigating hexagonal $\alpha$- and $\beta$-beryllene alongside a newly
    proposed cubic trilayer allotrope, we elucidate how orbital inversion and
    spatial inversion symmetry generate non-trivial $\mathbb{Z}_2$ topological
    invariants and anisotropic dielectric response in pristine and hydrogenated
    light-element metals.
\end{itemize}
```

##### (C) 光学性质与拓扑不变量的物理意义说明

(Physical Significance of Optical Observables and Band Topology)

```latex
\section{Physical Significance of Calculated Observables}
\label{sec:intro_observables}

Throughout this work, optical spectra and topological invariants are evaluated
not as routine computational outputs, but as decisive observables resolving
specific physical questions:
\begin{itemize}
    \item \textbf{Dielectric Function and Optical Response:} The complex
    dielectric tensor $\varepsilon_{\alpha\beta}(\omega) = \varepsilon_1(\omega)
    + \ii \varepsilon_2(\omega)$ provides direct spectroscopic fingerprints of
    interband electronic transitions and collective excitations. The imaginary
    component $\varepsilon_2(\omega)$ resolves the onset of optical transitions,
    directly interrogating band nesting and orbital hybridization. The zeros of
    $\varepsilon_1(\omega)$ accompanied by peaks in the electron energy-loss
    spectrum (EELS), $L(\omega) = -\mathrm{Im}[1/\varepsilon(\omega)]$, identify
    volume and surface plasmon modes. Furthermore, non-zero off-diagonal
    elements ($\varepsilon_{xy}$) serve as an unambiguous probe of in-plane
    structural symmetry breaking, signaling anisotropic conductivity and
    potential optical chirality.
    \item \textbf{Band Topology and the $\mathbb{Z}_2$ Invariant:} In two
    dimensions, a non-trivial $\mathbb{Z}_2$ topological invariant ($\nu = 1$)
    classifies a system as a quantum spin Hall insulator, which guarantees the
    existence of gapless, helical edge states protected by time-reversal
    symmetry against non-magnetic backscattering. In centrosymmetric crystals,
    this topological classification can be determined directly by evaluating the
    parity eigenvalues of occupied electronic states at time-reversal invariant
    momentum (TRIM) points, connecting microscopic orbital symmetry directly to
    macroscopic dissipationless transport channels.
\end{itemize}
```

---

### 3. Chapters 2 & 3 (Theory & Methodology): 篇幅精简, 附录迁移与实用计算方法路线图

#### 3.1 中文问题诊断与精简策略

- 问题诊断:
  - Chapters 2 和 3 共占约 106 页(占毕业论文篇幅的近 40%). 其中含有大量时间演化算符, 全同粒子哈密顿量, 大正则系综
    , Thomas-Fermi 模型的详尽数学推导. 评审人 1 明确指出 Chapters 2 and 3 together are
    disproportionately long... while still not giving the reader a concise
    roadmap of the computational methods used later.
  - 评审人 2 指出在第 100 页之后, 以 alpha-beryllene 和 beta-beryllene 为例讲解介电函数与光学性质时, 未明确注明
    数据是论文自身原创计算还是引用自文献.
- 修改执行方案:
  - 措施一 (大刀阔斧剥离至附录 Appendix):
    - 将 Section 2.1(时间依赖薛定谔方程到海森堡绘景详细数学演算), Section 2.2.1(大正则系综推导), Section
      2.3.4-2.3.5(Thomas-Fermi 近似详尽推导与极限分析)移至新增的 Appendix B: Extended Many-Body
      and DFT Formalisms.
    - 正文 Chapter 2 保留紧凑的脉络: 多体薛定谔方程 -> Hohenberg-Kohn 定理 -> Kohn-Sham 变分框架 -> 交换
      关联泛函(LDA, GGA-PBE, HSE06 杂化泛函机理).
    - 正文 Chapter 3 保留麦克斯韦方程组在介质中的响应 -> 介电张量微观表达式 -> Kramers-Kronig 变换 -> 光学参数转换公
      式, 将其余纯教科书电磁学演练移至附录.
  - 措施二 (新增实用计算方法路线图 Practical Computational Roadmap):
     系统汇总在 Chapters 4-6 实际使用的全部第一性原理计算技术与关键物理判据, 形成一张贯穿全书的方法学全景图.
  - 措施三 (明确 Chapter 3 中 alpha/beta-Beryllene 光学数据的归属):
     在正文及图注中明确加入声明: 本处引用的 alpha- 和 beta-beryllene 光学谱系本论文 Chapter 6 中的原创计算结果, 此处
     提前用作介电响应张量与推导光学量的示范性分析, 并附上对 Chapter 6 对应章节的精确交叉引用.

#### 3.2 实用计算方法路线图英文框架 (Practical Computational Roadmap)

```latex
\section{Practical Computational Methodology Roadmap}
\label{sec:computational_roadmap}

While the preceding sections outlined the rigorous theoretical foundations of
DFT and linear response theory, translating these concepts into predictive
materials simulations requires a well-defined computational workflow.
Figure~\ref{fig:methodology_roadmap} summarizes the integrated computational
roadmap employed throughout Chapters~\ref{cha:project_bilayers},
\ref{cha:project_boron}, and \ref{cha:project_beryllene}.

\begin{enumerate}
    \item \textbf{Geometry Optimization and Convergence Criteria:}
    All structural relaxations are performed using plane-wave pseudopotential
    methods (VASP and Quantum ESPRESSO). For 2D monolayers and heterostructures,
    a vacuum buffer of at least $15\text{--}40$~\AA\ is inserted along the
    out-of-plane ($z$) direction to suppress fictitious periodic interactions.
    Electronic minimization is iterated until total energy changes satisfy
    $\Delta E < 10^{-6}\text{--}10^{-8}$~eV, and atomic coordinates are fully
    relaxed until residual interatomic Hellmann--Feynman forces fall below
    $0.01$~eV/\AA\ (or $10^{-5}$~Ry/bohr).

    \item \textbf{Brillouin-Zone Sampling and Dense $k$-Grids:}
    Monkhorst--Pack $\Gamma$-centered $k$-point meshes are systematically
    benchmarked for total energy and dielectric tensor convergence. While
    relaxation and phonon calculations employ standard meshes ($k$-point spacing
    $\approx 0.02\text{--}0.03$~\AA$^{-1}$), optical dielectric response and
    Fermi-surface integrations demand ultra-dense grids (up to $105 \times 105
    \times 1$) and broad conduction-band manifolds (typically $128\text{--}200$
    bands) to ensure proper convergence of interband matrix elements.

    \item \textbf{Dynamical and Thermal Stability Framework:}
    \begin{itemize}
        \item \textit{Phonon Dispersions:} Harmonic dynamical stability is
        verified across high-symmetry paths using either the finite-displacement
        supercell approach (Phonopy) or density-functional perturbation theory
        (DFPT). The absence of imaginary (negative) frequencies across the
        entire Brillouin zone confirms local dynamical stability at 0~K.
        \item \textit{Ab Initio Molecular Dynamics (AIMD):} Thermal persistence
        and anharmonic stability are evaluated in canonical ($NVT$) ensembles
        using Nosé--Hoover thermostats at target temperatures
        ($300\text{--}400$~K) with time steps of $1.0$~fs over multi-picosecond
        trajectories.
    \end{itemize}

    \item \textbf{Magnetic Ordering and Spin Polarization:}
    Collinear spin-polarized calculations are implemented to explore possible
    magnetic ground states. Total energies of paramagnetic (NM), ferromagnetic
    (FM), and antiferromagnetic (AFM) configurations are compared to determine
    magnetic ground states and exchange-coupling strengths.

    \item \textbf{Superconductivity via DFPT and Wannier-Interpolated EPW:}
    Electron--phonon interactions are treated rigorously using DFPT combined
    with maximally localized Wannier functions (MLWFs) via Wannier90 and the EPW
    code. Coarse-grid electron-phonon matrix elements
    $g_{mn\nu}(\mathbf{k},\mathbf{q})$ are interpolated onto ultra-fine meshes
    to yield the Eliashberg spectral function $\alpha^2 F(\omega)$, total
    coupling constant $\lambda$, and logarithmic average frequency
    $\omega_{\log}$. Superconducting transition temperatures $T_c$ are obtained
    from the McMillan--Allen--Dynes formula and by solving the fully anisotropic
    Migdal--Eliashberg gap equations.

    \item \textbf{Spin--Orbit Coupling and $\mathbb{Z}_2$ Parity Invariants:}
    Relativistic effects are included self-consistently via non-collinear
    spin--orbit coupling (SOC). For centrosymmetric systems, the 2D topological
    invariant $\mathbb{Z}_2$ ($\nu$) is computed by evaluating the parity
    eigenvalues $\xi_m(\Lambda_i) = \pm 1$ of all Kramers-degenerate occupied
    pairs at the four time-reversal invariant momentum (TRIM) points $\Lambda_i
    \in \{\Gamma, \mathrm{M}_1, \mathrm{M}_2, \mathrm{M}_3\}$:
    \begin{equation}
        (-1)^{\nu} = \prod_{i=1}^{4} \prod_{m=1}^{N_{\mathrm{occ}}/2}
        \xi_{2m}(\Lambda_i).
    \end{equation}
\end{enumerate}
```

#### 3.3 Chapter 3 中 alpha/beta-Beryllene 示例的归属说明文本

```latex
\noindent\textbf{Note on Illustrative Examples in this Chapter:}\\
The complex dielectric functions, absorption coefficients, refractive indices,
extinction coefficients, reflectivities, and electron energy-loss spectra of
$\alpha$-beryllene and $\beta$-beryllene presented in
Figures~\ref{fig:alpha_beta_dielectric_intro}--\ref{energy_loss_spectrum_alpha_beta_beryllene}
are original first-principles results calculated as part of the present doctoral
thesis. They are introduced here in advance solely to provide concrete,
illustrative demonstrations of the linear optical response formalisms and
directional tensor components derived above. A comprehensive investigation of
the atomic configurations, stability criteria, electronic band structures, and
full physical interpretations of these beryllene phases is presented in
Chapter~\ref{cha:project_beryllene}.
```

---

### 4. Chapter 4 (Graphene-Boron Heterostructures): 题注自洽化, 图像清晰度重构与作者贡献说明

#### 4.1 中文问题诊断与修改措施

- 问题诊断:
  - 评审人 1 指出 Figures 4.29-4.36(即 SI 中的 S1.17-S1.24)题注过于简短, 缺少对各子图 (a, b, c), 张量分量
    , 线型/颜色, 偏振方向, 单位及物理特征的描述.
  - 评审人 2 指出 Chapter 4 多个复合大图在纸质打印版中字体过小, 坐标轴标注和图例模糊不可读.
  - 两位评审人均指出缺少候选人与合作者贡献的明确划分声明 (Authorship Attribution Statement).
- 实施措施:
  1. 在 project_1_main.tex 开头增设明确的作者贡献声明.
  2. 针对 Figures 4.29-4.36, 编写自洽, 详尽的英文题注.
  3. 对图件进行分拆或重排, 增大字体字号(确保打印版不低于 8-9 pt).

#### 4.2 章首作者贡献声明英文模板 (Authorship Statement for Chapter 4)

```latex
\section*{Publication and Authorship Attribution Statement}
\addcontentsline{toc}{section}{Publication and Authorship Attribution Statement}

The contents of this chapter have been published in the following peer-reviewed
journal:
\begin{myquote}
\textbf{L. Niu}, O. J. Conquest, C. Verdi, and C. Stampfl,
``Electronic and Optical Properties of 2D Heterostructure Bilayers of Graphene,
Borophene and 2D Boron Carbides from First Principles'',
\textit{Nanomaterials} \textbf{14}(20), 1659 (2024).
\textsc{doi}:~\href{https://doi.org/10.3390/nano14201659}{\texttt{10.3390/nano14201659}}.
\end{myquote}

\noindent\textbf{Author Contributions:}\\
\textbf{Lu Niu (Candidate)} conceived the computational models, performed all
first-principles density functional theory calculations (structural relaxations,
electronic band structures, density of states, work functions, and linear
optical response spectra), carried out data post-processing and figure
preparation, and drafted the original manuscript.\\
\textbf{Oliver James Conquest} contributed to structural modeling discussions
and manuscript revision.\\
\textbf{Carla Verdi} provided guidance on optical response theory and critically
reviewed the manuscript.\\
\textbf{Catherine Stampfl (Principal Supervisor)} supervised the project,
provided overall scientific direction, contributed to data interpretation, and
revised the manuscript for submission.
```

#### 4.3 Figures 4.29-4.36 详尽自洽英文题注替换方案

- 图 4.29 (原 S1.17): Graphene-Borophene 介电函数

```latex
\caption{Calculated real ($\varepsilon_1$, solid lines) and imaginary
($\varepsilon_2$, dashed lines) parts of the frequency-dependent dielectric
tensor components for the Graphene-Borophene bilayer heterostructure. Results
obtained with the GGA-PBE functional (blue curves) and the HSE06 hybrid
functional (orange curves) are compared across photon energies from $0$ to
$30$~eV. Panels display: (a) in-plane $xx$ component ($\varepsilon_{xx}$), (b)
in-plane $yy$ component ($\varepsilon_{yy}$), and (c) out-of-plane $zz$
component ($\varepsilon_{zz}$). A Gaussian broadening of $\eta = 0.1$~eV was
applied. The HSE06 functional systematically shifts interband transition
thresholds to higher energies and sharpens high-energy peaks relative to PBE.}
```

- 图 4.30 (原 S1.18): Graphene-BC3 介电函数

```latex
\caption{Calculated real ($\varepsilon_1$, solid lines) and imaginary
($\varepsilon_2$, dashed lines) parts of the frequency-dependent dielectric
tensor for the Graphene-$\mathrm{BC}_3$ bilayer heterostructure. Comparisons
between PBE (blue) and HSE06 (orange) are presented for: (a) in-plane component
$\varepsilon_{xx}$, (b) in-plane component $\varepsilon_{yy}$, and (c)
out-of-plane component $\varepsilon_{zz}$. The semimetallic character preserves
a non-zero Drude-like tail at low energies, while HSE06 broadens the separation
between $\pi \to \pi^*$ and $\sigma \to \sigma^*$ interband transitions.}
```

- 图 4.31 (原 S1.19): Graphene-B4C3 介电函数与各向异性非对角元

```latex
\caption{Calculated real ($\varepsilon_1$, solid lines) and imaginary
($\varepsilon_2$, dashed lines) parts of the dielectric tensor for the
Graphene-$\mathrm{B}_4\mathrm{C}_3$ bilayer heterostructure using PBE (blue) and
HSE06 (orange). Panels show: (a) in-plane diagonal component $\varepsilon_{xx}$,
(b) out-of-plane component $\varepsilon_{zz}$, and (c) off-diagonal component
$\varepsilon_{xy}$. Due to the broken mirror symmetry and low $P3$ space group
of the heterojunction, non-vanishing real and imaginary off-diagonal components
($\varepsilon_{xy}$) emerge in the range of $1.5\text{--}8.0$~eV, signaling
optical anisotropy and potential chiral optical activity.}
```

- 图 4.32 (原 S1.20): 吸收系数 (Absorption Coefficient)

```latex
\caption{Frequency-dependent optical absorption coefficients, $\alpha(\omega)$
(in units of $10^5~\mathrm{cm}^{-1}$), for the three bilayer heterostructures as
a function of photon energy ($0\text{--}30$~eV): (a) Graphene-Borophene, (b)
Graphene-$\mathrm{BC}_3$, and (c) Graphene-$\mathrm{B}_4\mathrm{C}_3$. Solid
lines represent in-plane polarization ($\alpha_{\parallel}$), and dashed lines
denote out-of-plane polarization ($\alpha_{\perp}$). Blue and orange curves
correspond to GGA-PBE and HSE06 calculations, respectively. All bilayers exhibit
pronounced absorption peaks within the visible spectrum ($1.6\text{--}3.2$~eV),
with Graphene-Borophene exhibiting the strongest low-energy interband absorption
onset.}
```

- 图 4.33 (原 S1.21): 能量损失谱 (Energy-Loss Spectrum)

```latex
\caption{Calculated electron energy-loss spectra (EELS), $L(\omega) =
-\mathrm{Im}[1/\varepsilon(\omega)]$, for the three bilayer heterostructures:
(a) Graphene-Borophene, (b) Graphene-$\mathrm{BC}_3$, and (c)
Graphene-$\mathrm{B}_4\mathrm{C}_3$. In-plane ($L_{\parallel}$, solid lines) and
out-of-plane ($L_{\perp}$, dashed lines) responses are compared between PBE
(blue) and HSE06 (orange). Prominent peaks correspond to collective plasmon
excitations: broad volume $\pi+\sigma$ plasmons emerge between
$16.5\text{--}18.5$~eV for all systems, while low-energy $\pi$ plasmons occur at
$4\text{--}6$~eV in Graphene-$\mathrm{B}_4\mathrm{C}_3$ and Graphene-Borophene,
with the latter showing an additional acoustic-like plasmon feature below
$3$~eV.}
```

- 图 4.34 (原 S1.22): 折射率 (Refractive Index)

```latex
\caption{Calculated real refractive index, $n(\omega)$, as a function of photon
energy ($0\text{--}30$~eV) for: (a) Graphene-Borophene, (b)
Graphene-$\mathrm{BC}_3$, and (c) Graphene-$\mathrm{B}_4\mathrm{C}_3$. Solid and
dashed lines correspond to in-plane ($n_{\parallel}$) and out-of-plane
($n_{\perp}$) polarizations, evaluated with PBE (blue) and HSE06 (orange). In
the static limit ($\omega \to 0$), the refractive index reflects the enhanced
polarizability of metallic and semimetallic bilayer interfaces compared to
isolated monolayers.}
```

- 图 4.35 (原 S1.23): 反射率 (Reflectivity)

```latex
\caption{Calculated optical reflectivity spectra, $R(\omega)$ (dimensionless,
$0\text{--}1$), for: (a) Graphene-Borophene, (b) Graphene-$\mathrm{BC}_3$, and
(c) Graphene-$\mathrm{B}_4\mathrm{C}_3$. In-plane ($R_{\parallel}$, solid
curves) and out-of-plane ($R_{\perp}$, dashed curves) spectra are evaluated with
PBE (blue) and HSE06 (orange). Graphene-Borophene displays substantial infrared
and visible reflectivity ($R > 0.4$), whereas Graphene-$\mathrm{BC}_3$ and
Graphene-$\mathrm{B}_4\mathrm{C}_3$ maintain high optical transparency ($R <
0.15$) throughout the visible window.}
```

- 图 4.36 (原 S1.24): 消光系数 (Extinction Coefficient)

```latex
\caption{Calculated optical extinction coefficients, $\kappa(\omega)$, as a
function of photon energy ($0\text{--}30$~eV) for: (a) Graphene-Borophene, (b)
Graphene-$\mathrm{BC}_3$, and (c) Graphene-$\mathrm{B}_4\mathrm{C}_3$.
Polarization along in-plane ($\kappa_{\parallel}$, solid lines) and out-of-plane
($\kappa_{\perp}$, dashed lines) directions are displayed for PBE (blue) and
HSE06 (orange). The primary extinction features mirror the interband absorption
profiles, confirming that optical attenuation in the visible and
near-ultraviolet range is dominated by direct electronic interband transitions.}
```

---

### 5. Chapter 5 (Penta-Bipyramid Boron o-B14): 物理自洽性修正, 概念澄清与超导计算流程规范

#### 5.1 中文问题诊断与核心修改方案

- 问题 1: 图 5.1(原子结构)位置滞后. 挪到 Section 5.1 末尾或 Section 5.2 开头, 在介绍计算超胞前率先给出结构图与多中心配位
  分类.
- 问题 2: 单层基态物理描述自相矛盾(半导体 vs 金属).
  - 单层 o-B14 在 PBE 下预测为金属态是由于自相互作用与电子离域误差; 在 HSE06 下费米面处打开能隙, 基态为严格的 AFM 半导体.
  - 明确澄清: 光学介电函数计算是基于 HSE06 的 AFM 半导体基态展开的独立粒子近似(IPA)计算, 因而主导吸收为带间跃迁, 排除了未收敛的带内
    Drude 发散.
- 问题 3: PBE 与 HSE06 差异的物理机制解释. 半局域泛函存在自相互作用与离域误差; HSE06 引入 25% 短程 Fock 交换抑制误差并打开能
  隙, 但仍为平均场近似.
- 问题 4: 稳定性宣称严格限定. 结合能, 声子谱及 5.5 ps AIMD 仅证明 0 K 动力学稳定性与有限温热稳定性, 不构成热力学凸包基态或实验可合成性
  .
- 问题 5: AFM-FM 微小能量差与负声子频率说明. 微小能差反映弱自旋超交换耦合, 预示较低磁有序转变温度; Gamma 点微小虚频源于超胞有限尺寸与声学
  和规则截断误差.
- 问题 6: 超导计算流程规范. 系统给出 DFPT + Wannier90 + EPW 的标准化可复现数学描述与参数设置.

#### 5.2 核心英文修改文本草案

##### (A) 单层基态与光学计算自洽性澄清

(Resolution of Electronic/Magnetic State and Optical Treatment)

```latex
\noindent\textbf{Clarification of the Ground State and Optical Interband
Treatment:}\\
To clarify the electronic and magnetic configuration used in the optical
calculations, we explicitly emphasize that pristine monolayer
$o\text{-}\mathrm{B}_{14}$ exhibits competing magnetic configurations. Under the
semi-local PBE functional, the monolayer is predicted to be metallic due to
well-known self-interaction and electron delocalization errors. When treated
with the screened hybrid functional HSE06, the reduction of self-interaction
error stabilizes an antiferromagnetic (AFM) semiconducting ground state with a
localized magnetic moment of approximately $0.85~\mu_{\mathrm{B}}$ per active
boron site and an indirect band gap of $0.67$~eV.

For the dielectric response presented in Section~\ref{2_optical_properties}, the
calculation was performed based on the AFM ground-state electronic manifold
within the independent-particle approximation (IPA). Because the ground state is
semiconducting under HSE06, interband transitions dominate the optical
absorption profile across the visible and ultraviolet regimes, with no divergent
Drude-like intraband contribution ($\omega \to 0$). For comparison and
consistency with the literature, calculations evaluated at the non-magnetic (NM)
semimetallic state exclude intraband free-carrier Drude damping, focusing
exclusively on interband matrix elements.
```

##### (B) 稳定性宣称严格限定声明 (Qualification of Stability Claims)

```latex
\noindent\textbf{Critical Distinction Between Dynamical Stability and
Experimental Synthesizability:}\\
We emphasize that the computed cohesive energies (referenced to isolated atoms),
formation enthalpies relative to $\alpha$-rhombohedral boron, positive phonon
dispersion branches, and stable 5.5~ps AIMD trajectories provide rigorous
evidence of \textit{local dynamical stability} at 0~K and \textit{short-time
thermal persistence} at 400~K. However, these computational indicators do not
constitute formal thermodynamic stability, which requires constructing the
grand-canonical convex hull against all competing 3D and 2D boron allotropes.
Nor do they guarantee experimental synthesizability, which in practice is
governed by kinetic barriers, nucleation pathways, and strong chemical
interactions with growth substrates (e.g., metal surfaces). The predicted 2D
$o\text{-}\mathrm{B}_{14}$ structures should therefore be regarded as
dynamically viable metastable phases.
```

##### (C) 超导计算 DFPT+Wannier+EPW 可复现流程规范文本 (Reproducible EPW Workflow)

```latex
\subsection{Superconductivity Computational Workflow: DFPT, Wannier90, and EPW}
\label{sec:superconductivity_workflow}

The superconducting properties of bulk, monolayer, and hydrogen-terminated
bilayer $o\text{-}\mathrm{B}_{14}$ were determined using the state-of-the-art
electron--phonon coupling framework implemented in Quantum ESPRESSO, Wannier90,
and EPW:
\begin{enumerate}
    \item \textbf{Self-Consistent Field and DFPT Calculations:}
    Norm-conserving pseudopotentials with an energy cutoff of $45$~Ry were
    utilized. Self-consistent electronic densities were computed on coarse
    Monkhorst--Pack grids ($9 \times 12 \times 8$ for bulk, $10 \times 10 \times
    1$ for monolayer, and $9 \times 9 \times 1$ for bilayer). The dynamical
    matrices and the linear variation of the self-consistent potential were
    evaluated on irreducible $q$-point meshes ($3 \times 4 \times 3$ for bulk,
    $5 \times 5 \times 1$ for monolayer, and $3 \times 3 \times 1$ for bilayer)
    using Density-Functional Perturbation Theory (DFPT).

    \item \textbf{Wannier Interpolation:}
    Maximally localized Wannier functions (MLWFs) were constructed using the
    Wannier90 code by setting initial trial projections on boron $2s$ and $2p$
    atomic orbitals, matching the outer valence manifold. Convergence of the
    real-space Wannier spread was achieved, enabling high-fidelity electronic
    band interpolation.

    \item \textbf{EPW Fine-Grid Interpolation:}
    Using the EPW package, the electron--phonon matrix elements
    $g_{mn\nu}(\mathbf{k},\mathbf{q})$, electronic eigenvalues, and phonon
    frequencies were transformed into the localized Wannier basis and
    subsequently interpolated onto ultra-fine grids ($60 \times 80 \times 54$
    for bulk, $80 \times 80 \times 1$ for 2D sheets). The Eliashberg spectral
    function $\alpha^2 F(\omega)$ was calculated as:
    \begin{equation}
        \alpha^2 F(\omega) = \frac{1}{2\pi N(E_{\mathrm{F}})}
        \sum_{\mathbf{q}\nu} \delta(\omega - \omega_{\mathbf{q}\nu})
        \sum_{\mathbf{k}mn} |g_{mn\nu}(\mathbf{k},\mathbf{q})|^2
        \delta(\varepsilon_{n\mathbf{k}} - E_{\mathrm{F}})
        \delta(\varepsilon_{m\mathbf{k}+\mathbf{q}} - E_{\mathrm{F}}),
    \end{equation}
    where $N(E_{\mathrm{F}})$ is the density of states at the Fermi level.

    \item \textbf{Coupling Constant and $T_c$ Evaluation:}
    The total electron--phonon coupling parameter $\lambda$ and logarithmic
    average frequency $\omega_{\log}$ were obtained from:
    \begin{equation}
        \lambda = 2 \int_{0}^{\infty} \frac{\alpha^2 F(\omega)}{\omega}
        \dif\omega, \quad \omega_{\log} = \exp\left( \frac{2}{\lambda}
        \int_{0}^{\infty} \frac{\dif\omega}{\omega} \alpha^2 F(\omega) \ln\omega
        \right).
    \end{equation}
    The superconducting critical temperature $T_c$ was evaluated via the
    Allen--Dynes modified McMillan formula:
    \begin{equation}
        T_c = \frac{f_1 f_2 \omega_{\log}}{1.20} \exp\left[
        -\frac{1.04(1+\lambda)}{\lambda - \mu^*(1+0.62\lambda)} \right],
    \end{equation}
    with empirical Coulomb pseudopotential $\mu^* = 0.13$. Additionally, the
    fully anisotropic Migdal--Eliashberg gap equations were solved
    self-consistently along the imaginary Matsubara axis and analytically
    continued to the real axis to extract the temperature-dependent
    superconducting energy gap $\Delta(T)$.
\end{enumerate}
```

---

### 6. Chapter 6 (Beryllene Phases): 三层立方相构建, 金属拓扑论证与计算细节补全

#### 6.1 中文问题诊断与核心修改方案

- 问题 1: 三层立方相构建方法不明确. 明确其为从体心立方 (bcc) 沿 (001) 方向切出三原子层(A-B-A 堆垛), 在面内充分自洽弛豫并在 z 轴
  设置 40 埃真空层构建而成.
- 问题 2: 金属相中 Z2 拓扑不变量的合理性论证. 体系属于拓扑半金属(Topological metal), 虽然费米能级穿过了平庸费米口袋, 但在发生反
  转的特征能带之间存在沿整个高对称路径连续的局域能隙 (Local continuous direct gap); 在反演对称性保护下, 4 个 TRIM 点
  的宇称乘积确立了非平庸的 Z2 = 1; 通过应变或弱功能化消除多余平庸费米口袋即可连续演化为严格拓扑绝缘体.
- 问题 3: 仅使用 GGA-PBE 未做 HSE06 的理论正当性. 金属体系介电响应必须采用 105x105x1 的超密 k 点网格和 40 埃大真空层超胞
  , HSE06 计算成本极其昂贵不切实际; 铍为轻质 sp 元素, 无局域 d/f 电子, PBE 能高度可靠再现其费米面与等离激元模式.
- 问题 4: 主文收敛测试与图件原子颜色. 在正文总结 k 点与空带收敛阈值; 题注明确绿球与蓝球代表处于不同晶格高度(z 坐标)或次晶格层的不等价原子.
- 问题 5: 选择性加氢与 AIMD 参数. 说明 alpha/beta 相具有活泼未饱和表面悬键, 因而加氢以探究金属-绝缘体转变, 而三层立方相专注于纯金属
  表面极限; 补齐 AIMD 参数(NVT, Nosé-Hoover, 300 K, 1.0 fs, 10 ps, 5x5x1).

#### 6.2 核心英文修改文本草案

##### (A) 三层立方铍的构建晶体学描述

(Crystallographic Construction of Cubic Trilayer Beryllene)

```latex
\subsection{Structural Derivation and Modeling of Cubic Trilayer Beryllene}
\label{sec:cubic_construction}

The cubic trilayer beryllene structure was constructed by cleaving a
three-atomic-layer slab from the bulk body-centered cubic (bcc) beryllium along
the crystallographic $(001)$ direction. The resulting slab possesses an
$\mathrm{A}\text{--}\mathrm{B}\text{--}\mathrm{A}$ stacking sequence, where the
central beryllium layer occupies the four-fold hollow coordination sites
projected from the top and bottom atomic planes. To simulate the isolated
two-dimensional allotrope, a vacuum spacing of $40$~\AA\ was introduced along
the out-of-plane $z$-axis to eliminate fictitious periodic interactions.

Full structural relaxation of both the in-plane lattice vectors and internal
ionic coordinates was carried out without symmetry constraints. The fully
relaxed structure preserves a square in-plane Bravais lattice with an optimized
lattice parameter of $a = b = 2.45$~\AA\ (representing a slight $0.8\%$
expansion relative to the bulk bcc phase), while the vertical interlayer
distance contracts by $17\%$ due to surface relaxation and enhanced bonding
coordination in the ultra-thin limit.
```

##### (B) 金属态下 Z2 拓扑不变量的理论辩护

(Physical Justification of Z2 Topology in a Metallic Phase)

```latex
\subsection{Justification of the $\mathbb{Z}_2$ Topological Invariant in
Metallic Beryllene}
\label{sec:z2_justification}

A key theoretical question is the formal validity of the $\mathbb{Z}_2$
topological index in pristine $\alpha$-beryllene and cubic trilayer beryllene,
which are classified as metallic due to Fermi-level crossings. In standard
Fu--Kane theory, the $\mathbb{Z}_2$ invariant $\nu$ is strictly formulated for
insulating band structures separated by a continuous, global energy gap
throughout the entire Brillouin zone.

For the beryllene phases studied here, we clarify that the system constitutes a
\textit{topological metal} (or symmetry-protected topological semimetal):
\begin{enumerate}
    \item \textbf{Existence of a Local Inverted Gap:} Along the entire
    high-symmetry momentum path, a continuous direct energy gap persists between
    the occupied valence manifold and the unoccupied conduction manifold that
    participate in the band inversion. Specifically, at the time-reversal
    invariant momentum (TRIM) points (e.g., the $\mathrm{M}$ point), the
    relativistic spin--orbit coupling (SOC) hybridizes the inverted $s$- and
    $p_z$-derived states, establishing a non-zero local mass gap.
    \item \textbf{Well-Defined Parity Invariant:} Because both
    $\alpha$-beryllene and the cubic trilayer allotrope possess spatial
    inversion symmetry ($\mathcal{P}$), the parity eigenvalues $\xi_m(\Lambda_i)
    = \pm 1$ of all Kramers pairs below this direct local gap are uniquely
    defined at the four TRIM points. Evaluating the parity product yields
    $(-1)^{\nu} = -1$, confirming $\nu = 1$.
    \item \textbf{Physical Implication and Robustness:} Although trivial
    bulk-like Fermi pockets overlap with the Fermi level in the pristine
    metallic state, the non-trivial band topology dictates that the inverted gap
    supports helical, gapless edge states. If the trivial pockets are shifted
    away from $E_{\mathrm{F}}$ via moderate biaxial strain, chemical gating, or
    weak surface passivation, the system undergoes a continuous transition into
    a pure quantum spin Hall insulator without closing the topological inverted
    gap.
\end{enumerate}
```

##### (C) 采用 GGA-PBE 计算光学性质的理论辩护

(Methodological Justification for Excluding HSE06 in Chapter 6)

```latex
\noindent\textbf{Justification for the Choice of Functional (GGA-PBE vs.
HSE06):}\\
Unlike Chapters~\ref{cha:project_bilayers} and~\ref{cha:project_boron}, where
both PBE and HSE06 were compared, Chapter~\ref{cha:project_beryllene} relies
exclusively on the GGA-PBE functional for dielectric response calculations. This
choice is physically and computationally justified:
\begin{itemize}
    \item \textbf{Computational Tractability on Ultra-Dense $k$-Grids:} Optical
    response spectra in metallic systems demand exceptional $k$-point sampling
    density to avoid spurious unphysical peaks and ensure smooth integration
    over the Fermi surface. Here, an ultra-dense $\Gamma$-centered grid of $105
    \times 105 \times 1$ and a large vacuum thickness of $40$~\AA\ were strictly
    necessary. Performing hybrid HSE06 calculations on such massive $k$-meshes
    is computationally prohibitive.
    \item \textbf{Physical Nature of Beryllium:} Beryllium is an ultra-light
    $sp$ element devoid of localized $d$ or $f$ electrons. Consequently,
    self-interaction and electron delocalization errors---which severely
    compromise band gaps in transition-metal oxides or narrow-gap
    semiconductors---play a minimal role in the broad, nearly-free-electron
    bands of metallic beryllene. Prior benchmarks have firmly established that
    PBE provides reliable band dispersions, Fermi surfaces, and optical plasmon
    frequencies for light metallic systems.
\end{itemize}
```

##### (D) AIMD 模拟参数规范文本 (Complete AIMD Simulation Parameters)

```latex
\noindent\textbf{Ab Initio Molecular Dynamics (AIMD) Setup:}\\
To rigorously assess finite-temperature structural persistence, canonical
($NVT$) AIMD simulations were performed using the Nosé--Hoover thermostat. A $5
\times 5 \times 1$ supercell was employed to minimize periodic self-interactions
during thermal fluctuations. The system was equilibrated at a target temperature
of $300$~K with a time step of $1.0$~fs for a total simulation trajectory of
$10.0$~ps ($10,000$ molecular dynamics steps). The time evolution of the total
energy and instantaneous temperature exhibited stationary Gaussian fluctuations
around equilibrium without bond breaking or structural reconstruction,
confirming the thermal resilience of the functionalized frameworks.
```

---

### 7. Chapter 7 (Conclusion and Outlook): 理论局限性批判反思, 实验现状对照表与明确未来展望

#### 7.1 中文问题诊断与修改措施

- 问题诊断: 缺少对计算局限性与基本假定的反思; 缺少对实验合成与纯理论预测体系的清晰界定; 未来工作过于宽泛.
- 修改措施:
  1. 撰写理论局限性深度反思节: 剖析 DFT 近似, 单粒子独立近似 (IPA) 忽略激子效应 (BSE), 以及 0 K 自由悬浮真空模型脱离真实衬底外延环
     境的局限性.
  2. 制作实验合成 vs 理论预测系统对比表.
  3. 将未来工作具体化为可预期的定量物理认知突破.

#### 7.2 核心英文修改文本草案

##### (A) 理论方法局限性批判性反思 (Critical Assessment of Theoretical Limitations)

```latex
\section{Critical Assessment of Theoretical Methodologies and Limitations}
\label{sec:concl_limitations}

A rigorous appraisal of the conclusions presented in this thesis requires
acknowledging the foundational approximations inherent in the computational
framework:
\begin{enumerate}
    \item \textbf{Exchange-Correlation Approximations and Self-Energy
    Corrections:}
    Semi-local GGA-PBE calculations systematically underestimate band gaps and
    can artificially favor delocalized metallic states. While the HSE06 screened
    hybrid functional mitigates self-interaction errors and successfully
    predicts gap opening in semiconducting $\mathrm{BC}_3$,
    $\mathrm{B}_4\mathrm{C}_3$, and $o\text{-}\mathrm{B}_{14}$, HSE06 remains a
    mean-field approximation governed by semi-empirical screening parameters
    ($25\%$ exact exchange, $\omega = 0.2$~\AA$^{-1}$). True quasiparticle
    energies, band offsets, and accurate Fermi-velocity renormalizations require
    many-body perturbation theory within the $GW$ approximation, which remains
    computationally demanding for large-scale heterostructures.

    \item \textbf{Independent-Particle Approximation and Excitonic Effects:}
    All optical response functions in this work were evaluated within the
    independent-particle approximation (IPA) via the random-phase approximation
    (RPA), which explicitly omits electron--hole Coulomb interactions. In
    two-dimensional materials, reduced dielectric screening and spatial quantum
    confinement dramatically enhance excitonic effects, often yielding exciton
    binding energies on the order of $0.5\text{--}1.0$~eV. Consequently, while
    the IPA reliably captures single-particle interband transitions and
    collective plasmon resonances, the experimental optical absorption onset in
    semiconducting phases is expected to be redshifted by bound exciton peaks,
    requiring full Bethe--Salpeter Equation (BSE) treatment.

    \item \textbf{Free-Standing 0~K Models vs. Real Substrate Environments:}
    All calculations assume idealized, freestanding monolayers and bilayers
    suspended in vacuum at $T = 0$~K. Experimentally, 2D boron and beryllium
    allotropes cannot exist as isolated free sheets; they are invariably
    synthesized on metallic or insulating substrates (e.g., $\mathrm{Ag}(111)$,
    $\mathrm{Cu}(111)$, or $\mathrm{h\text{-}BN}$). Substrate interactions
    induce epitaxial strain, interfacial charge transfer, orbital hybridization,
    and enhanced external dielectric screening, all of which can fundamentally
    shift the energetic stability hierarchy, modify Fermi surface topology, or
    alter superconducting critical temperatures.
\end{enumerate}
```

##### (B) 实验合成已证实体系与理论预测体系系统对照表

```latex
\section{Distinction Between Experimentally Synthesized and Theoretically
Predicted Phases}
\label{sec:concl_experimental_status}

Table~\ref{tab:experimental_status_summary} provides a transparent
classification delineating established experimental systems from purely
theoretical predictions investigated in this thesis.

\begin{table}[!htbp]
\centering
\caption{Classification of materials systems studied in this thesis:
experimental realization vs. theoretical predictions.}
\label{tab:experimental_status_summary}
\adjustbox{max width=\textwidth}{
\begin{tabular}{llll}
\hline\hline
\textbf{System} & \textbf{Investigated Phases} & \textbf{Status} & \textbf{Key
References / Experimental Substrates} \\
\hline
\textbf{Carbon} & Graphene monolayer & Experimentally realized & Exfoliation,
CVD growth on metals~\cite{novoselov2004electric} \\
\hline
\textbf{Boron Carbides} & $\mathrm{BC}_3$ monolayer & Experimentally realized &
Synthesized on
$\mathrm{NbB}_2(0001)$~\cite{yanagisawa2004phonon,tanaka2005novel} \\
 & $\mathrm{B}_4\mathrm{C}_3$ monolayer & Theoretical prediction &
 Computationally predicted metastable phase~\cite{tian2019} \\
\hline
\textbf{Borophene} & $\beta_{12}$, $\chi_3$ sheets & Experimentally realized &
Grown on $\mathrm{Ag}(111)$
substrates~\cite{mannix2015borophene,feng2016experimental} \\
\hline
\textbf{Heterostructures} & Graphene--Borophene & Theoretical prediction &
Proposed vdW bilayer heterojunction \\
 & Graphene--$\mathrm{BC}_3$ / $\mathrm{B}_4\mathrm{C}_3$ & Theoretical
 prediction & Proposed vdW bilayer heterojunctions \\
\hline
\textbf{Boron $o\text{-}\mathrm{B}_{14}$} & Bulk $o\text{-}\mathrm{B}_{14}$ &
Experimentally realized & Synthesized under high-pressure
conditions~\cite{han2023superconducting} \\
 & Monolayer \& Bilayer $o\text{-}\mathrm{B}_{14}$ & Theoretical prediction &
 Predicted 2D allotropes derived from bulk \\
 & H-terminated Bilayer & Theoretical prediction & Chemically passivated
 theoretical phase \\
\hline
\textbf{Beryllene} & Exfoliated Beryllene flakes & Experimentally realized &
Liquid sonochemical exfoliation~\cite{chahal2023beryllene} \\
 & $\alpha$-, $\beta$-beryllene & Theoretical prediction & Predicted
 planar/buckled hexagonal allotropes~\cite{ono2020dynamical,li2023coexistence}
 \\
 & Cubic Trilayer beryllene & Theoretical prediction & Newly proposed 2D
 bcc-derived allotrope \\
 & Hydrogenated Beryllenes & Theoretical prediction & Chemically functionalized
 configurations \\
\hline\hline
\end{tabular}
}
\end{table}
```

##### (C) 具体化且具备预期成果的未来工作展望 (Targeted Directions for Future Research)

```latex
\section{Targeted Directions for Future Theoretical and Experimental Research}
\label{sec:concl_future_outlook}

Rather than generic computational extensions, future efforts should target
specific theoretical refinements and experimental tests:
\begin{enumerate}
    \item \textbf{Many-Body GW-BSE Optical Spectroscopy:}
    \textit{Specific Improvement:} Calculating excitonic eigenvalues and
    two-particle wave functions via the Bethe--Salpeter equation (BSE) on top of
    $G_0W_0$ quasiparticle band structures will quantitatively predict bound
    exciton binding energies ($E_{\mathrm{b}}$) and optical absorption peak
    shapes in semiconducting monolayer $\mathrm{BC}_3$,
    $\mathrm{B}_4\mathrm{C}_3$, and $2\mathrm{H}\text{-}\alpha$-beryllene,
    resolving whether dark excitons or strong exciton-plasmon coupling dominate
    at low photon energies.

    \item \textbf{Explicit Substrate Modeling and Epitaxial Strain Maps:}
    \textit{Specific Improvement:} Performing large-scale slab calculations of
    2D $o\text{-}\mathrm{B}_{14}$ and beryllene supported on specific metallic
    surfaces ($\mathrm{Ag}(111)$, $\mathrm{Al}(111)$, and $\mathrm{Ir}(111)$)
    will map the interfacial charge transfer, quantify work function
    modifications, and determine whether substrate-stabilized moiré
    superstructures preserve or suppress the intrinsic superconducting and
    topological states.

    \item \textbf{Quantum Transport and Berry-Curvature Calculations:}
    \textit{Specific Improvement:} Evaluating the non-Abelian Berry curvature
    $\Omega_z(\mathbf{k})$ and constructing finite-width nanoribbons within a
    localized Wannier basis will allow direct simulation of the edge-state
    transport. This will establish whether backscattering-immune helical edge
    conductance ($G = 2e^2/h$) can be observed experimentally in cubic trilayer
    beryllene despite overlapping metallic bulk states.

    \item \textbf{Anharmonic Lattice Dynamics and High-Temperature Phase
    Stability:}
    \textit{Specific Improvement:} Implementing the Stochastic Self-Consistent
    Harmonic Approximation (SSCHA) will capture temperature-dependent phonon
    frequency shifts and phonon lifetimes. This will verify whether strong
    lattice anharmonicity at elevated temperatures ($T > 500$~K) can stabilize
    metastable 2D beryllenes or suppress the soft acoustic modes observed near
    the Brillouin-zone center.
\end{enumerate}
```

---

### 8. 针对两位评审人的逐条答复信草案 (Formal Point-by-Point Reply Letter)

本答辩信草案符合学术规范与学校格式要求, 页码占位符可在您完成论文修改后填入.

#### 8.1 答辩信开头与总括声明 (Introduction and Overview)

Candidate's Name: Lu Niu
Degree: Doctor of Philosophy
Thesis Title: Exploring Quantum Properties of Light-Element Xenes: DFT Studies
of the Electronic Structure and Optical Response for Boron and Beryllium
Allotropes
Supervisors: Prof. Catherine Stampfl, Dr. Carla Verdi, Dr. Oliver James Conquest
Date: September 2026

I express my deepest gratitude to both Examiner 1 and Examiner 2 for their
constructive, insightful, and comprehensive evaluations of my doctoral thesis. I
am delighted that both examiners commended the originality, volume of research,
and publication record of this work, and recommended the award of the degree of
Doctor of Philosophy subject to corrections.

I have thoroughly revised the thesis in strict accordance with the examiners'
recommendations. Below is my detailed, point-by-point response to all comments.

#### 8.2 Response to Examiner 1

##### Examiner 1 - Comment 1

The research scope and publication record are appropriate for a PhD, and the
presentation is generally professional. The thesis-level research position is
nevertheless not sufficiently clear: the early literature review does not lead
to a sharp research gap or central motivation. Chapters 2 and 3 together are
also disproportionately long, at approximately 100 pages, while still not giving
the reader a concise roadmap of the computational methods (geometry
optimization, phonon, magnetism, AIMD, superconductivity, topological property)
used later. Substantial scientific and editorial corrections are therefore
required. The rest chapters look like hopping between different materials and
there is a lack of relationship between them.

Response:
I sincerely thank the examiner for this overarching structural critique. In the
revised thesis:

1. Unifying Narrative and Central Motivation (Chapter 1, Pages [X-Y]): Chapter 1
   has been thoroughly expanded. I have introduced a dedicated section (Section
   1.2: Central Motivation and Research Gaps) clearly articulating the unifying
   scientific theme connecting the three materials projects: investigating how
   atomic geometry, multicentre bonding topology, dimensionality reduction, and
   chemical functionalization dictate emergent quantum states in ultra-light
   elements ($Z=4$ and $Z=5$) where heavy-atom spin--orbit coupling is absent.
2. Reorganization and Reduction of Chapters 2 and 3 (Pages [X-Y]): Chapters 2
   and 3 have been substantially shortened by migrating extensive textbook-style
   derivations to a new Appendix (Appendix B: Extended Many-Body and DFT
   Formalisms), reducing the main text of these chapters by over 45 pages.
3. Concise Methodology Roadmap (Chapter 2, Section 2.6, Pages [X-Y]): A new
   dedicated section titled Practical Computational Methodology Roadmap has been
   added, systematically detailing geometry optimization, k-point sampling,
   phonon calculations, AIMD, magnetic ordering, the DFPT+Wannier90+EPW
   superconductivity workflow, and SOC parity-based Z2 topological analysis.

##### Examiner 1 - Comment 2

Chapter 1 provides useful background but reads more as a broad survey than as a
focused argument for the thesis. It should explain why graphene-based boron
systems, boron phases, and beryllene belong to one thesis, what unresolved
question each chapter addresses, and how the studies collectively support one
conclusion. The literature should be used critically to separate established
experimental systems from theoretical proposals and to identify the research
gap. The motivation for calculating optical properties is also not sufficiently
clear... The introduction should also briefly explain why topology is important
and what physical consequence is expected from a non-trivial Z2 invariant,
before introducing the parity calculation.

Response:
Chapter 1 has been completely rewritten to address these points:

1. Cohesive Chapter Linkage (Chapter 1, Section 1.3, Pages [X-Y]): The revised
   text explains that Chapters 4, 5, and 6 represent a three-stage progression
   of quantum tuning: from extrinsic interface engineering via vdW
   heterostructures (Ch 4), to intrinsic complex bonding topology in boron
   allotropes (Ch 5), and pushing into the extreme light-metal limit hosting
   symmetry-protected topology in beryllene (Ch 6).
2. Critical Literature Review (Chapter 1, Section 1.4, Pages [X-Y]): A critical
   literature review has been incorporated, categorizing existing experimental
   achievements versus theoretical predictions and defining the research gap.
3. Scientific Motivation for Optical Observables (Chapter 1, Section 1.5, Pages
   [X-Y]): I have clarified that optical quantities serve as decisive physical
   probes of band nesting, collective plasmon excitations, and structural
   symmetry breaking.
4. Significance of Z2 Topology (Chapter 1, Section 1.6, Pages [X-Y]): A
   conceptual introduction to 2D band topology has been added, explaining its
   significance in light elements and the physical consequence of
   dissipationless helical edge states.

##### Examiner 1 - Comment 3

Chapter 2 and 3 are very long and contain considerable formal background, but
they do not provide a sufficiently concise and practical explanation of the
computational methods used in the thesis... These chapters should be shortened
and reorganised around the methods actually used.

Response:
As detailed in the response to Comment 1, Chapters 2 and 3 have been
restructured. Formal mathematical derivations have been moved to Appendix B,
while a practical methodology roadmap directly connecting computational settings
to the scientific questions in Chapters 4-6 has been incorporated in Section 2.6
(Pages [X-Y]).

##### Examiner 1 - Comment 4

Chapter 4 is a useful but relatively incremental computational study... The
captions of Figures 4.29-4.36 are too short to be self-contained and should
identify the panels, tensor components, line styles, PBE-HSE06 comparison,
polarisation directions, units, and principal feature.

Response:

1. Self-Contained Captions for Figures 4.29-4.36 (Pages [X-Y]): All captions for
   Figures 4.29-4.36 have been rewritten to be fully self-contained, specifying
   panels, tensor components, line styles, functional comparisons, polarization
   directions, units, and principal physical features.
2. Scientific Motivation: The introductory text in Chapter 4 (Section 4.1, Page
   [X]) has been refined to better emphasize plasmonic tunability and Schottky
   barrier control.

##### Examiner 1 - Comment 5

Chapter 5 is stronger and more scientifically interesting... However, the work
remains predictive: the stability, superconductivity, and plasmon claims require
careful qualification and are not experimentally demonstrated... Cohesive
energies, phonons, and a very short 5.5 ps AIMD trajectory establish energetic
preference relative to selected references, dynamical stability, and short-time
thermal persistence, but do not by themselves establish thermodynamic stability
or synthesizability. The small AFM-FM energy difference and inconsistent
statements about negative phonon frequencies should be clarified.

Response:

1. Qualification of Stability Claims (Section 5.2, Pages [X-Y]): Terminology has
   been rigorously revised. The text states that cohesive energies, positive
   phonon branches, and stable AIMD simulations establish local dynamical
   stability at 0 K and short-time thermal persistence at 400 K, but do not
   prove thermodynamic stability or guarantee synthesizability.
2. AFM-FM Energy Difference (Section 5.3, Page [X]): The small calculated energy
   difference between AFM and FM configurations is now explicitly discussed as
   indicating weak magnetic exchange coupling.
3. Clarification of Phonon Frequencies (Section 5.3, Page [X]): Minor negative
   frequencies near the Gamma point in 2D sheets are explicitly attributed to
   acoustic sum rule numerical artifacts in finite supercells.

##### Examiner 1 - Comment 6

The monolayer is described as an AFM semiconductor in one place and as metallic
in the optical discussion, so the electronic and magnetic state used for the
optical calculation and its intraband treatment must be stated. The PBE-HSE06
difference should be explained: HSE06 can open a gap by reducing
self-interaction and delocalisation errors, but it remains an approximation.
Finally, the superconductivity workflow needs a concise reproducible explanation
of how density-functional perturbation theory, Wannier interpolation, and EPW
produce the phonons, electron-phonon matrix elements, alpha2F(omega), lambda,
omegalog, and the Allen-Dynes and anisotropic Migdal-Eliashberg values. The
distinction between phonon stability and finite-temperature AIMD should be made
clear.

Response:

1. Ground State and Optical Consistency (Section 5.3, Pages [X-Y]): I have
   clarified that pristine monolayer o-B14 is an AFM semiconductor under HSE06
   with an indirect gap of 0.67 eV. Optical calculations are based on this AFM
   semiconducting ground state within the independent-particle approximation,
   dominated by interband transitions.
2. Physical Mechanism of HSE06 (Section 5.3, Page [X]): The text explains that
   HSE06 opens a gap by mitigating self-interaction and electron delocalization
   errors via exact exchange, while noting that HSE06 remains a mean-field
   hybrid approximation.
3. Reproducible Superconductivity Workflow (Section 5.2.2, Pages [X-Y]): A
   complete description of the DFPT + Wannier90 + EPW workflow has been added.
4. Phonon Stability vs. AIMD (Section 5.2.1, Page [X]): The conceptual
   distinction between 0 K harmonic potential curvature and finite-temperature
   anharmonic thermal persistence is clearly articulated.

##### Examiner 1 - Comment 7 & 8

Chapter 6 is potentially the most novel. It proposes a new cubic trilayer
beryllene structure and explores whether elemental beryllium can support tunable
electronic, optical, and topological properties. The main weaknesses are that
the method used to generate the new structure is unclear, and the Z2 claim needs
justification because the phase is described as metallic. Details of how the new
structure was constructed should be described. Stability and optical quantities
should be reported with appropriate two-dimensional normalisation and with a
clear distinction between dynamical stability, energetic preference, and
experimental synthesizability.

Response:

1. Construction of Cubic Trilayer Beryllene (Section 6.2, Page [X]): A
   comprehensive description of slicing a three-layer slab from bulk bcc
   beryllium along the (001) plane and relaxing coordinates within a 40 Angstrom
   vacuum cell has been incorporated.
2. Justification of Z2 Topology in a Metallic Phase (Section 6.4, Pages [X-Y]):
   The text clarifies that the system is a topological metal: a continuous local
   inverted gap separates the bands participating in band inversion across the
   Brillouin zone, allowing parity-based confirmation of Z2 = 1.
3. 2D Normalization and Stability Classification (Section 6.2 & 6.5, Pages
   [X-Y]): Optical spectra are confirmed to be properly normalized, and
   stability distinctions are strictly maintained.

#### 8.3 Response to Examiner 2

##### Examiner 2 - Comment 1

Chapter 1 provides a clear introduction... The principal weakness of this
chapter, and indeed of the thesis as a whole, is the absence of a dedicated and
comprehensive literature review. The candidate should include a discussion of
the key studies that have been undertaken on related two-dimensional boron, and
beryllium-based materials, highlighting the findings of previous researchers and
identifying the gaps in knowledge that motivate the present work. Such a review
should also discuss the various theoretical and computational approaches that
have been employed in the literature, including the levels of theory used
successfully to predict properties of similar systems.

Response:
A comprehensive, critical literature review has been incorporated into Chapter 1
(Section 1.4: Critical Literature Review of Light-Element 2D Materials, Pages
[X-Y]), covering 2D boron allotropes, experimental progress in beryllene, and
theoretical levels of theory (PBE, HSE06, DFPT, EPW).

##### Examiner 2 - Comment 2

Chapters 2 and 3 give almost textbook version... There are certain sections that
need to be rectified - From page 100 onwards, optical properties of
alpha-beryllene and beta-beryllene are discussed as examples within the
methodology chapter. While the use of examples to illustrate particular concepts
is helpful, the source of the results should be clearly identified. If the
results are generated as part of the present thesis, an appropriate statement
and cross reference should be provided. If they are taken from published
literature, the relevant citation should be included.

Response:
In Chapter 3 (Page [X]), an explicit explanatory note has been added stating
that the optical spectra of alpha- and beta-beryllene are original
first-principles results calculated as part of this thesis (Chapter 6),
presented early solely as pedagogical illustrations, with cross-references to
Section 6.5.

##### Examiner 2 - Comment 3

Chapter 4... has already been published in a peer-reviewed journal... However,
as this chapter is based on a multi-author publication, a clear statement should
be included at the beginning of the chapter indicating that the work has been
published and outlining the specific contributions of the PhD candidate relative
to those of the co-authors.

Response:
An explicit Publication and Authorship Attribution Statement has been added at
the beginning of Chapter 4 (Page [X]), specifying the publication details and
candidate contributions relative to co-authors.

##### Examiner 2 - Comment 4

A weakness of Chapter 4 relates to the quality of several figures in the thesis.
They are difficult or impossible to read in the printed version of the thesis.
All figures should remain legible to the reader without requiring access to the
published article. In particular, several multi-panel figures contain text, axis
labels, and legends that are too small to be read clearly. For example, in
Figures 4.29 and 4.30, the legends are largely illegible. The candidate should
revise these figures by increasing the font sizes, enlarging the individual
panels, or splitting the figures into multiple figures where necessary.

Response:
Figures 4.29 and 4.30 (and related optical figures) have been redesigned with
enlarged font sizes for axis labels, tick marks, and legends, ensuring full
legibility in both print and digital formats.

##### Examiner 2 - Comment 5

Chapter 5... A minor issue relates to Figure 5.1. This figure is important for
understanding the structures and systems investigated in the chapter; The figure
should be referenced and presented earlier in the methodology or introductory
section of the chapter, before the associated discussion of the computational
models to provide readers with the necessary structural context before detailed
results are presented.

Response:
Figure 5.1 has been relocated to Section 5.1 (Page [X]), before the detailed
discussion of computational supercells and models in Section 5.2.

##### Examiner 2 - Comment 6

Weaknesses of Chapter 6:

1. Unlike Chapters 4 and 5, which employ both GGA-PBE and HSE06 functionals,
   Chapter 6 relies solely on GGA-PBE calculations. A justification for
   excluding HSE06 calculations should be provided.
2. Although convergence tests appear to have been performed and included in the
   supplementary material, they are not adequately discussed in the chapter.
3. In Figures 6.2 and 6.3, both green and blue spheres are used to represent
   beryllium atoms, but the significance of the different colours is not
   explained in either the figure captions or the main text.
4. The rationale for hydrogenating some beryllium phases while excluding the
   trilayer phase is not provided.
5. AIMD simulations are presented to support structural stability; however
   methodological details, including the simulation ensemble, temperature, time
   step, and total simulation time, are omitted.

Response:
All five points have been addressed in full:

1. Justification for GGA-PBE (Section 6.2, Page [X]): Performing HSE06 on the
   ultra-dense 105x105x1 k-mesh required for metallic dielectric integration is
   computationally intractable; additionally, beryllium is a light sp metal
   where self-interaction errors are minimal.
2. Discussion of Convergence Benchmarks (Section 6.2, Page [X]): Convergence
   thresholds for total energy and dielectric spectra are now explicitly
   discussed in the main text.
3. Atom Color Legend (Captions and Section 6.3, Pages [X-Y]): Captions now
   explain that green and blue spheres denote beryllium atoms at different
   atomic layer heights or inequivalent sublattices.
4. Rationale for Selective Hydrogenation (Section 6.3, Page [X]): alpha- and
   beta-beryllene possess unsaturated surface bonds that induce metal-insulator
   transitions upon hydrogenation, whereas the cubic trilayer phase was studied
   in its pristine form to examine intrinsic topological metallic surface
   states.
5. Complete AIMD Parameters (Section 6.2, Page [X]): All parameters are now
   reported: NVT ensemble, Nosé-Hoover thermostat, 300 K, 1.0 fs time step, 10.0
   ps duration, 5x5x1 supercell.

##### Examiner 2 - Comment 7 & 8

Chapter 7, the conclusions chapter, should provide a more critical assessment of
the limitations of the research... Furthermore, the candidate should clearly
distinguish between systems that have already been experimentally found and
characterised and those that remain purely theoretical predictions. The future
work section simply lists potential theoretical directions for further study,
the candidate should discuss specific improvements that could be expected from
such studies.

Response:
Chapter 7 has been comprehensively rewritten:

1. Critical Assessment of Theoretical Limitations (Section 7.2, Pages [X-Y]):
   Evaluates exchange-correlation approximations, omission of excitonic effects
   in IPA, and freestanding vacuum models vs. experimental substrate
   interactions.
2. Classification of Experimental vs. Theoretical Systems (Section 7.3, Table
   7.1, Page [X]): A dedicated summary table clearly classifies all investigated
   materials into experimentally realized versus theoretical predictions.
3. Specific Future Directions (Section 7.4, Pages [X-Y]): Outlines concrete
   improvements expected from GW-BSE excitonic calculations, explicit substrate
   slab modeling, localized Wannier edge-state transport, and anharmonic SSCHA
   lattice dynamics.

---

### 9. 论文修改操作清单与检查核对表 (Action Checklist)

- Chapter 1 (src/introduction.tex):
  - 扩写文献综述(增加 2D 硼, 硼碳化合物, 铍材料的国内外实验与理论前沿文献).
  - 插入统一宏观主线, 明确回答为什么这三种材料属于同一篇博士论文.
  - 阐明介电函数及导出光学量作为微观物理探针的明确目的.
  - 引入拓扑物理概念背景, 说明 Z2 不变量对应的无耗散边缘态物理意义.
- Chapters 2 & 3 (src/fundamentals_a.tex, src/fundamentals_b.tex):
  - 将纯教科书式推导(约 40-50 页)迁移至新建的 src/appendix_theory.tex.
  - 在 Chapter 2(或 Chapter 3)末尾添加实用计算方法路线图(Section 2.6 / 3.6).
  - 在 fundamentals_b.tex 第 100 页左右注明 alpha/beta-Beryllene 光学谱为 Chapter 6 原创计算结果并
    建立交叉引用.
- Chapter 4 (src/project_1_main.tex, src/project_1_SI.tex):
  - 在章首加入发表与作者贡献声明 (Authorship Attribution Statement).
  - 将 Figures 4.29-4.36(即 SI 中的 S1.17-S1.24)题注全部替换为本方案提供的自洽详尽英文题注.
  - 增大 Figures 4.29, 4.30 等复合图的字号, 坐标轴与图例, 确保打印版完全清晰可辨.
- Chapter 5 (src/project_2_main.tex):
  - 将 Figure 5.1(原子结构)挪到方法讨论之前(Section 5.1 末尾或 5.2 开头).
  - 澄清单层基态在 HSE06 下为反铁磁 (AFM) 半导体, 明确光学带间计算处理.
  - 解释 HSE06 消除自相互作用并打开能隙的物理机制, 并注明其仍为近似.
  - 将热力学稳定性与可合成性严谨修正为动力学稳定性与相对能量偏好.
  - 澄清 AFM-FM 极小能量差的弱交换耦合本质, 以及 Gamma 点声子微小虚频的数值截断属性.
  - 规范写入完整的 DFPT + Wannier90 + EPW 超导可复现工作流.
- Chapter 6 (src/project_3_main.tex):
  - 详细描述三层立方铍沿 bcc (001) 切面构建与弛豫的完整晶体学过程.
  - 撰写金属态中局域反转能隙与宇称乘积确立 Z2 = 1 的拓扑金属理论辩护.
  - 撰写仅采用 GGA-PBE 计算光学性质的充分理由.
  - 在正文补充总能与光学网格收敛性测试的数值分析结论.
  - 在图 6.2 和 6.3 题注中明确绿球与蓝球的层高/次晶格不等价原子定义.
  - 解释对 alpha/beta 相加氢而对三层立方相保持纯金属的机理意图.
  - 补齐 AIMD 全部模拟参数 (NVT, Nosé-Hoover, 300 K, 1.0 fs, 10 ps, 5x5x1).
- Chapter 7 (src/conclusion.tex):
  - 增加理论方法局限性批判性反思节(讨论 PBE/HSE06, 单粒子独立近似 IPA 与激子效应 BSE, 真空悬浮模型与真实衬底外延效应).
  - 插入实验合成已证实体系与理论预测体系系统对照表 (Table 7.1).
  - 将未来工作细化为具体的理论与实验改进方向, 并点明预期带来的具体物理突破.
- 答辩答复信 (report/reply_to_examiners.md):
  - 将本方案第 8 节中的完整回复信整合到答复信文件中, 填入修改后 thesis 的准确页码与章节编号.
