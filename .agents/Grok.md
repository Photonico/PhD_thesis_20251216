# Grok

## 0919

Examiner reports 对照修改备忘录(Grok)

本文只给修改意见和措施, 不改动论文源文件. 讲解用中文; 审查原话, 论文现有表述, 图注, 以及建议写入论文的句子保持英文. 审查意见实际在 report/(不是
reports/). 编译稿为 .output/thesis.pdf(2026-08-26, 270 页).

审查结论: awarded the degree subject to corrections of the thesis to the satisfaction
of the University.Examiner 1 要求 substantial scientific and editorial
corrections; Examiner 2 认为可由 Chair of Examination 裁定. 策略应是: 把 Examiner 1 的科学口径全部收紧,
同时把 Examiner 2 的每一条可核对项做完. 不要另开新课题.

已有 report/reply_to_examiners.md 是回信骨架, 页码仍是 x, y. 本备忘录按"先改论文, 再填回信"来写.

0\. 怎么用这份备忘录

1. 先做 Must, 再做 Should.Optional 只在有余力时做.
2. 每一条都尽量写成: 审查原话 -> 现在稿子哪里有问题 -> 具体改什么 -> 建议英文句子.
3. 回信时, 每条审查意见对应: 改了什么, 在哪一页, 必要时摘录新段落.
4. 作者贡献, AIMD 的 ensemble / timestep / 时长, 绿色/蓝色 Be 原子的含义, 是否尝试过氢化 cubic trilayer, 只有
   你本人知道. 模板里标了 [FILL] 的地方不要编造.
5. 第 4, 5 章已发表或已接收. 科学结论不要重写; 要改的是表述边界, 图注, 图的可读性, 作者贡献, 前后不一致. 第 6 章未发表, 可以做有限补充计算, 但不是必须
   把 HSE06 光学全套重跑.

1\. 当前稿的结构性诊断

Ch 1 Introduction
  页码: 1-4
  篇幅: 约 4 页
  卡住的点: 综述而非论题; 无尖锐 research gap; 三章材料看起来互不隶属

Ch 2 Fundamentals I
  页码: 5-78
  篇幅: 约 74 页
  卡住的点: 教科书量子力学/DFT; 后面真正用到的方法没有路线图

Ch 3 Fundamentals II
  页码: 79-110
  篇幅: 约 32 页
  卡住的点: 教科书光学; p.100 起 alpha/beta-beryllene 示例未标明来源

Ch 2+3 合计
  篇幅: 约 106 页
  卡住的点: 与 4 页引言, 4 页结论完全不成比例

Ch 4 Heterostructures
  页码: 111-146
  卡住的点: 增量工作可以保留, 但贡献陈述, 图注, 印刷可读性不够

Ch 5 o-B14
  页码: 147-180
  卡住的点: 科学上最强, 但稳定性/磁性/光学/超导口径过满

Ch 6 Beryllene
  页码: 181-216
  卡住的点: 最有新意, 完成度最低: 结构怎么来的, 金属态 Z2, 无 HSE06, AIMD 细节

Ch 7 Conclusion
  页码: 217-220
  篇幅: 约 4 页
  卡住的点: 几乎全是重复摘要; 无 limitations; 实验/预测未分开

List of Publications
  页码: v-vi
  卡住的点: 列了论文, 没有 candidate vs co-author 分工

Appendix
  页码: 240 起
  卡住的点: 目前只有代码链接, 正好承接从 Ch 2-3 挪走的推导

一句话诊断: 这不是"结果不够", 而是论文还没有把自己写成一篇 PhD thesis. 三章材料研究已经够博士水平(两篇已发表/接收, 一篇在投), 但
thesis-level position 没有立住. 审查委员要看到的是一条贯穿的科学问题, 而不是三篇 paper 加两章讲义.

建议把贯穿问题写成(英文, 放进 Ch 1 和 Ch 7):

    How do composition, bonding topology, dimensionality, stacking, and hydrogen
    functionalization control the electronic structure and the
    optical/collective response of light-element xenes?

光学谱是三章的脊骨; 磁性, 超导, 拓扑是这条脊骨上, 在键合网络改变时出现的额外量子通道. 不要把论文说成"我们算了很多二维材料的光学性质".

2\. 优先级总表

Must
  重写 Ch 1: 论题 + 批判性文献 + 实验/理论分界 + 光学动机 + Z2 物理后果
  来源: Ex1-1, Ex1-2; Ex2-Ch1

Must
  压缩并改向 Ch 2-3; 增加本论文实际使用的方法路线图; 标明 Ch 3 示例来自 Ch 6
  来源: Ex1-1, Ex1-3; Ex2-Ch2/3

Must
  作者贡献: Publications + Ch 4/5/6 章首
  来源: Ex1 开篇; Ex2-Ch4

Must
  区分 known structures 的表征 vs 本文新预测
  来源: Ex1 开篇; Ex2-Ch7

Must
  Figs 4.29-4.36 自包含图注 + 加大字号/拆图
  来源: Ex1-4; Ex2-Ch4

Must
  Ch 5: 稳定性口径, 声子虚频前后矛盾, AFM 半导体 vs 光学金属, PBE/HSE06, EPW 流程, Fig 5.1 前移
  来源: Ex1-5, Ex1-6; Ex2-Ch5

Must
  Ch 6: 立方三层如何构造, 金属态 Z2, 无 HSE06 的理由, 收敛的文字说明, 原子颜色, 为何不氢化 trilayer, AIMD 方法细节
  来源: Ex1-7, Ex1-8; Ex2-Ch6

Must
  重写 Ch 7: limitations + 实验/预测 + 有预期收益的 future work
  来源: Ex2-Ch7; Ex1 总结

Should
  Ch 5/6 增加 scope of claims 短段: 内聚能不等于 convex hull, 短 AIMD 不等于可合成
  来源: Ex1-5, Ex1-8

Should
  Ch 6 正文写清二维光学归一化(现在公式在 Ch 5, Ch 6 只引了文献和 SI 厚度)
  来源: Ex1-8

Should
  Appendix 的 vmatplot 工作写入作者贡献
  来源: Ex1 开篇

Optional
  2H-alpha 的 HSE06 能带(比全套 HSE06 光学便宜, 且直接回应 "PBE underestimates the gap")
  来源: Ex2-Ch6.1

不要做
  为了"显得更完整"去新开 GW, 输运, edge-state 大计算; 这些放 future work, 并写清预期改进

3\. 第 1 章 Introduction(现在只有 4 页, 这是全文最大结构缺陷)

3.1 审查原话

Examiner 1:

    Chapter 1 provides useful background but reads more as a broad survey than
    as a focused argument for the thesis. It should explain why graphene-based
    boron systems, boron phases, and beryllene belong to one thesis, what
    unresolved question each chapter addresses, and how the studies collectively
    support one conclusion. The literature should be used critically to separate
    established experimental systems from theoretical proposals and to identify
    the research gap. The motivation for calculating optical properties is also
    not sufficiently clear: absorption, refractive index, reflectivity, and loss
    spectra are often presented as a standard set of outputs rather than as
    observables answering defined scientific questions. The introduction should
    also briefly explain why topology is important and what physical consequence
    is expected from a non-trivial Z2 invariant, before introducing the parity
    calculation.

Examiner 2:

    The principal weakness of this chapter, and indeed of the thesis as a whole,
    is the absence of a dedicated and comprehensive literature review. ...
    highlighting the findings of previous researchers and identifying the gaps
    in knowledge that motivate the present work. Such a review should also
    discuss the various theoretical and computational approaches that have been
    employed in the literature, including the levels of theory used successfully
    to predict properties of similar systems.

两个人要的东西看起来相反(一个嫌"太泛", 一个嫌"文献不够"), 正确做法是一篇短而锋利的批判性文献, 而不是把 Ch 1 写成第二本教科书. 目标篇幅大约
12-18 页, 不要超过 20 页. 文献要为 gap 服务.

3.2 现在稿缺什么

src/introduction.tex 的现有逻辑是: graphene -> Xenes -> boron 缺电子 -> beryllium 更轻 ->
heterostructure 和氢化是调控手段 -> DFT -> 三章各一段摘要. 这是摘要的拉长版, 不是论证.

具体缺口:

- 没有 "this thesis asks X".
- 没有实验体系 vs 理论预测表.
- 硼烯, 石墨烯-硼烯异质结, BC3, B4C3, o-B14, beryllene 的关键先行工作只在后面各章 introduction 里出现, Ch 1 几乎不评
  .
- 光学五件套(alpha, n, k, R, L)没有各自对应的科学问题.
- 拓扑只在第 70 行突然出现 "non-trivial Z2", 没有物理后果.
- 方法层级(PBE, PBE+D3, HSE06, DFPT, EPW, IPA 光学, SOC+parity)没有在引言里交代"为什么这些方法在同类体系上是
  够用的, 短板在哪".

3.3 建议的新结构(英文标题可直接用)

1.1 Light-element xenes as a design platform

从 graphene 的零带隙限制出发, 不要重讲石墨烯史. 点明本论题: 轻元素二维体系里, 键合拓扑和维度可以打开半导体, 磁性, 超导, 等离子体和拓扑通道.

1.2 Two-dimensional boron: experiment, prediction, and open questions

批判性评述, 而不是清单:

- 实验: borophene on Ag(111)(beta12, chi3, alpha'); graphene-borophene 异质结(Hou 2021;
  Liu 2019); graphene-like BC3(Yanagisawa / Tanaka).
- 理论: 大量 borophene 同素异形体, 超导预测, 磁性预测; B4C3 monolayer 仍是理论结构(Tian 2019).
- Gap 对本论文 Ch 4: 实验已经做出 graphene-borophene, 但对 graphene-BC3 / graphene-B4C3 的电子结构和
  光学响应缺乏系统第一性原理对比; 已有工作很少同时给出 PBE 和 HSE06, 也很少把介电张量的对角与非对角分量当作结构对称性的探针.

1.3 Penta-bipyramid boron and the o-B14 family

- Bulk o-B14 是 Han et al. (2023) 的理论预测, 不是实验相.
- 先行工作给了体相超导 Tc 约 29.1 K.
- Gap 对本论文 Ch 5: 维度降低和氢终止如何把同一套 pentagonal-bipyramid 网络分别变成半导体, 磁体和超导体, 以及各向异性等离子体是
  否随维度一起出现. 这不是"再算一遍体相".

1.4 Beryllene: from prediction to a sparse experiment

- 理论: Ono 2020, Hess 2022, Li 2023(alpha/beta, Dirac-like, 超导, alpha 的非平庸拓扑).
- 实验: Chahal 2023 超声剥离得到二维 Be, HRTEM 见 hexagonal 和 square-like motif, 电学上是金属. 实验结构基序
  与理论 alpha/beta/cubic 的对应尚未建立, 必须写清楚.
- Gap 对本论文 Ch 6: 确认 alpha/beta 动力学稳定; 提出 cubic trilayer; 氢化如何把 alpha 推进宽带隙, 却让 beta
  保持金属; 光学各向异性; 以及在轻元素, 弱 SOC 条件下拓扑标记意味着什么.

1.5 Why optical properties (not a standard output dump)

把五件套写成问题, 而不是 VASP 的默认后处理:

epsilon1(omega), epsilon2(omega)
  问题: Where does screening change sign? Which tensor components are allowed by
  symmetry?

Absorption alpha(omega)
  问题: Is there visible-region oscillator strength, and does it survive stacking
  or hydrogenation?

Energy-loss L(omega)
  问题: Are there collective (plasmon) modes, at what energy, and are they
  directional?

Reflectivity R(omega)
  问题: Does the low-energy response look metallic or gapped?

n(omega), k(omega)
  问题: How anisotropic is the propagating/decaying field, and does n<1 appear?

建议英文:

    The optical calculations in this thesis are not a default post-processing
    set. The dielectric tensor is used to test three questions: (i) whether
    visible-region absorption exists and can be moved by stacking or
    hydrogenation; (ii) whether epsilon_1(omega) changes sign along selected
    directions, which we interpret as a necessary condition for directional
    plasmonic response, later corroborated by peaks in the energy-loss function;
    (iii) whether reduced symmetry (as in Graphene-B4C3, space group P3)
    produces finite off-diagonal epsilon_alpha beta(omega). Refractive index and
    reflectivity are reported because they translate the same dielectric
    function into quantities that optical and EELS experiments actually measure.

1.6 Why topology, and what a non-trivial Z2 would mean

必须出现在 Ch 6 的 parity 公式之前. 建议英文:

    For a two-dimensional insulator with time-reversal symmetry, a non-trivial
    Z2 invariant implies a quantum spin Hall phase: helical edge states traverse
    a bulk gap and are protected against elastic backscattering by time-reversal
    symmetry. The Fu-Kane parity criterion evaluates this invariant in
    inversion-symmetric insulators from the parity eigenvalues of occupied
    Kramers pairs at the time-reversal invariant momenta. Two caveats are
    essential for the later chapters. First, the invariant is defined for an
    isolated, fully occupied manifold separated by a gap from the unoccupied
    states; it is not automatically defined for a metal. Second, even when a
    parity inversion is found in a metallic phase, it does not by itself
    establish dissipationless edge transport, because bulk metallic channels
    remain. Chapter 6 therefore reports Z2 as a diagnostic of band inversion in
    an inversion-symmetric light-element lattice, and qualifies the claim where
    the phase is metallic.

1.7 Computational approaches in the literature, and the level of theory used
here

Examiner 2 明确要这个. 用一段加一个清单即可:

- 结构与能量: PBE + 色散校正是 2D vdW 体系的标准起点.
- 半导体带隙: PBE 系统偏低, HSE06 在硼碳化物和 2D 半导体上被广泛用作 pragmatic correction(Ch 4, Ch 5 已做).
- 声子: 有限差分 supercell 与 DFPT 都用于 2D 硼/铍文献.
- 超导: QE + EPW + anisotropic Migdal-Eliashberg 是轻元素 sp 超导体的标准流程.
- 光学: 独立粒子近似(IPA)介电函数是高通量默认; GW+BSE 才能可靠给激子和绝对峰位, 本论文明确定在 IPA.
- 拓扑: 有反演时 Fu-Kane parity; 无反演或金属则需要 Wilson loop / edge states.

1.8 Thesis structure and the single conclusion the three chapters support

建议英文:

    The three materials chapters are not independent case studies. Chapter 4
    asks whether van der Waals stacking of graphene with boron-based monolayers
    can retain Dirac-like bands while producing visible absorption and, in the
    lowest-symmetry stack, off-diagonal dielectric response. Chapter 5 asks
    whether a single electron-deficient boron network can be driven between
    semiconducting, magnetic, and superconducting states by dimensionality and
    hydrogen termination, and whether the same anisotropy appears in the
    plasmonic response. Chapter 6 asks whether the still lighter beryllium limit
    supports a new stable stacking (cubic trilayer), whether hydrogen can open a
    wide gap, and whether parity inversion appears even when spin-orbit coupling
    is weak. Taken together, the thesis concludes that light-element xenes are a
    compact design platform in which bonding topology, stacking, and surface
    termination control single-particle bands and collective optical response.

3.4 必须加的表: 实验 vs 理论

Ch 1 和 Ch 7 各放一次(Ch 7 可更短). 建议表题:

    Table 1.1. Experimental status of the principal systems discussed in this
    thesis.

Graphene
  Status: Experimental
  Key evidence: Novoselov 2004
  Role: Building block, Ch 4

alpha'-borophene
  Status: Experimental (on Ag)
  Key evidence: Wu / Mannix literature
  Role: Monolayer in Ch 4

BC3 monolayer
  Status: Experimental
  Key evidence: Yanagisawa, Tanaka
  Role: Monolayer in Ch 4

Graphene-borophene heterostructure
  Status: Experimental
  Key evidence: Hou 2021; Liu 2019
  Role: Ch 4; this work adds HSE06 optics

B4C3 monolayer
  Status: Theoretical prediction
  Key evidence: Tian 2019
  Role: Ch 4 characterisation

Graphene-BC3, Graphene-B4C3
  Status: Theoretical (this work + limited prior)
  Key evidence: This thesis, Ch 4
  Role: New systematic optics

Bulk o-B14
  Status: Theoretical prediction
  Key evidence: Han 2023
  Role: Reference bulk, Ch 5

Monolayer / bilayer / H-bilayer o-B14
  Status: Theoretical (this work)
  Key evidence: Ch 5, published
  Role: New 2D predictions

alpha-, beta-beryllene
  Status: Theoretical; 2D Be sheets exist experimentally but motif mapping is
  open
  Key evidence: Ono; Hess; Li 2023; Chahal 2023
  Role: Ch 6 confirmation + optics

Cubic trilayer beryllene
  Status: Theoretical, this work
  Key evidence: Ch 6
  Role: New structure

H-functionalised beryllene
  Status: Theoretical, this work
  Key evidence: Ch 6
  Role: New

这句话必须出现(Examiner 1 开篇 + Examiner 2 Ch 7):

    Throughout this thesis, experimentally realised materials are distinguished
    from theoretical proposals. Predictions of dynamical stability, magnetism,
    superconductivity, plasmonic modes, and Z2 topology are computational
    results; they are not experimental demonstrations.

4\. 第 2-3 章 Fundamentals(约 106 页, 必须砍, 并且补上"真正用过的方法")

4.1 审查原话

Examiner 1:

    Chapters 2 and 3 together are also disproportionately long, at approximately
    100 pages, while still not giving the reader a concise roadmap of the
    computational methods (geometry optimization, phonon, magnetism, AIMD,
    superconductivity, topological property) used later. ... These chapters
    should be shortened and reorganised around the methods actually used.

Examiner 2:

    From page 100 onwards, optical properties of alpha-beryllene and
    beta-beryllene are discussed as examples within the methodology chapter. ...
    If the results are generated as part of the present thesis, an appropriate
    statement and cross reference should be provided.

report/reply_to_examiners.md 里已经写了 "Chapters 2 and 3 have been reduced ... by
allocating sections x, y to a new Appendix". 这是对的方向, 但现在还没做.

4.2 建议搬迁(具体到节)

保留在正文章节, 压缩后大约 35-50 页:

- Ch 2: 多体问题为何需要密度; Hohenberg-Kohn; Kohn-Sham; LDA/GGA/PBE; HSE06 以及它为何能开带隙(为 Ch 4/5
  铺垫).
- Ch 3: 物质中的介电张量(短); IPA 下 epsilon2 的微观表达式; Kramers-Kronig; 由 epsilon(omega) 到
  alpha, n, k, R, L 的公式; 二维真空归一化(可把 Ch 5 的公式提前到这里, Ch 4-6 只引用).

整节或整块搬进 Appendix(标明 "reproduced from the original Chapter 2/3 for
completeness"):

- 2.1 大部分: time-evolution operator, Heisenberg picture, continuity equation(现在从 p.6
  写到 p.18).
- 2.3.4-2.3.5 Thomas-Fermi.
- 2.4.7 Hartree equations.
- 2.4 中重复的 variational construction(2.4.3 与 2.4.4 高度重叠, 留一个).
- 3.1 中教科书式 Maxwell 展开, 只留 constitutive relation 和各向异性张量.

Coursera 课笔记声明(src/fundamentals_a.tex 第 12 行)可以保留, 但应改成一句: 形式推导参考该课程, 本论所用的实际计算设置见新
的 methods roadmap.

4.3 必须新增: Computational methods used in this thesis

这是 Examiner 1 点名要的东西, 现在完全不在 Ch 2-3. 各章 methods 里有碎片, 但没有 thesis-level 路线图. 建议放在 Ch
3 末尾, 或作为 2.6 短节. 表题:

    Table 2.1. Computational workflow used in this thesis and the chapters that
    employ each method.

Geometry optimisation
  Code: VASP, PBE+D3(BJ), PAW
  典型设置: Ecut 450-600 eV; forces < 0.01 eV/A; Ediff = 1e-6 eV
  用于: Ch 4, 5, 6
  问题: Stable local minima

vdW correction
  Code: D3-BJ
  用于: Ch 4-6
  问题: Layer binding / 2D spacing

Hybrid bands / optics
  Code: HSE06
  典型设置: denser k for optics in Ch 4
  用于: Ch 4, 5; not Ch 6 (justified there)
  问题: Gaps; optical onset

Phonons (finite difference)
  Code: VASP supercells
  典型设置: 3x3 (Ch 5), 5x5 (Ch 6)
  用于: Ch 5, 6
  问题: Dynamical stability

Phonons (DFPT)
  Code: Quantum ESPRESSO
  典型设置: q-meshes in Ch 5 methods
  用于: Ch 5 superconductivity
  问题: g_mn nu, alpha^2 F

AIMD
  Code: VASP
  典型设置: [FILL: NVT/NPT, T, dt, duration]
  用于: Ch 5 H-bilayer; Ch 6 H-beryllene
  问题: Short-time thermal persistence, not thermodynamic stability

Spin polarisation / magnetism
  Code: VASP, FM vs AFM, fixed-spin
  典型设置: HSE06 for gaps
  用于: Ch 5 monolayer
  问题: Magnetic ground state

Electron-phonon / Tc
  Code: QE + Wannier90 + EPW
  典型设置: mu\* = 0.13; Allen-Dynes and anisotropic ME
  用于: Ch 5
  问题: Phonon-mediated superconductivity

SOC + parity / Z2
  Code: VASP+SOC, irvsp
  典型设置: Fu-Kane at TRIM
  用于: Ch 6
  问题: Band inversion diagnostic

IPA dielectric tensor
  Code: VASP LOPTICS / linear response
  典型设置: dense k; NBANDS convergence in SI
  用于: Ch 4-6
  问题: Optical / plasmonic questions in section 1.5

2D dielectric renormalisation
  Code: post-processing, Yang 2021
  典型设置: d_2D defined in SI
  用于: Ch 5, 6
  问题: Intensive 2D optical spectra

每行在后文章节必须能找到对应数字. 这张表就是 Examiner 1 要的 concise and practical explanation.

4.4 Ch 3 中 alpha/beta-beryllene 示例(p.93 起 Figures 3.1-3.6)

这些图就是 Ch 6 的数据, 但图注只写:

    Representative real and imaginary parts of the in-plane and out-of-plane
    dielectric function ... for alpha-Beryllene and beta-Beryllene.

正文也没有 "calculated in this thesis, see Chapter 6". 这是 Examiner 2 的直接命中.

措施(二选一, 推荐 A):

A(更干净): Ch 3 只留一套示意性光谱(例如只要 Figure 3.1), 图注写清来源; alpha, n, k, R, L 的完整谱全部放到 Ch 6, Ch
3 只保留公式.

B(改动小): 六张图都留, 但每张图注和第一次出现的正文加一句.

建议图注英文:

    Figure 3.1. Real and imaginary parts of the in-plane and out-of-plane
    dielectric function of alpha-beryllene and beta-beryllene. These spectra
    were calculated in this thesis at the PBE level and are analysed in Chapter
    6; they are shown here only to illustrate the dielectric quantities defined
    in this chapter.

5\. 作者贡献(Examiner 1 开篇 + Examiner 2 第 4 章, 两处都要)

现在 src/publications.tex 只有论文列表和导师签字, 没有任何 candidate vs co-author 说明. 第 4-6 章章首也没有.
这是最容易改, 也最不该漏的一项.

5.1 List of Publications 下增加总述

建议英文骨架(分工必须你自己填):

    Authorship contributions

    All materials chapters are based on collaborative manuscripts. I confirm
    that I am the first author of each chapter. Unless stated otherwise below, I
    performed the density-functional calculations, wrote the analysis code
    (vmatplot), generated the figures, and drafted the manuscripts. The specific
    contributions of co-authors are as follows.

    Chapter 4 (published in Nanomaterials). I [FILL: designed the
    heterostructure set / performed all VASP calculations / ...]. O. J. Conquest
    [FILL]. C. Verdi [FILL]. C. Stampfl supervised the work and revised the
    manuscript.

    Chapter 5 (accepted in Physical Review Materials). I [FILL]. Hongyang Ma
    [FILL: e.g. electron-phonon / EPW calculations, if that is accurate]. O. J.
    Conquest [FILL]. C. Verdi [FILL: superconductivity methodology]. C. Stampfl
    supervised the work and revised the manuscript.

    Chapter 6 (to be submitted to Physical Review B). I [FILL, including
    identification of the cubic trilayer structure if that is yours]. Co-author
    roles [FILL].

不要猜测谁跑了 EPW. 第 5 章作者比第 4 章多了 H. Ma, 这通常意味着超导/EPW 有额外贡献; 以事实为准.

5.2 每章章首一段(Abstract 之前)

第 4 章建议:

    This chapter is based on the following published article: L. Niu, O. J.
    Conquest, C. Verdi, and C. Stampfl, Nanomaterials 14, 1659 (2024). The
    candidate performed [FILL], wrote the analysis code, generated all figures
    used here, and drafted the manuscript. Co-author contributions are stated in
    the List of Publications.

第 5, 6 章同样格式. 第 6 章写 "in preparation / to be submitted", 不要写已经 submitted, 除非真的已投
(Publications 页现在写的是 "will be submitted ... soon", Ch 6 摘要也还没投稿语言).

6\. 第 4 章 Graphene-boron heterostructures

6.1 审查口径

Examiner 1 认为这章是 useful but relatively incremental, 贡献是 structure-property map 和
optical/plasmonic tunability, 不是解决重大实际问题. 不必为此新做计算, 但引言/结论要诚实:

    The contribution of this chapter is a systematic first-principles map of
    electronic structure and dielectric response for graphene-based bilayers
    with borophene, BC3, and B4C3, including a PBE-HSE06 comparison. It does not
    claim a new synthesised material or a device demonstration.

把 "possible optically active (chiral) effects" 从断言改成:

    The finite off-diagonal epsilon_xy(omega) in Graphene-B4C3 is required by
    the reduced P3 symmetry. It indicates anisotropic, and potentially
    gyrotropic, optical response; circular-dichroism or related measurements
    would be needed to establish chirality experimentally.

6.2 Figures 4.29-4.36: 图注过短 + 印刷不可读

对应文件: src/project_1_SI.tex 的 S1.17-S1.24, 编译后编号为 Figures 4.29-4.36. 现有图注原文:

- Dielectric function components of Graphene-Borophene.
- Dielectric function components of Graphene-BC3.
- Dielectric function components of Graphene-B4C3.
- Absorption coefficient.
- Energy-loss spectrum.
- Refractive index.
- Reflectivity.
- Extinction coefficient.

Examiner 1 点名这些图注必须 identify: panels, tensor components, line styles, PBE-HSE06
comparison, polarisation directions, units, principal feature.Examiner 2 点名 4.29
和 4.30 图例在印刷版几乎不可读.

图注(以 4.29 为例, 其余按体系替换):

    Figure 4.29. Independent-particle dielectric function of the
    Graphene-Borophene bilayer. Panels show the in-plane (xx, yy) and
    out-of-plane (zz) Cartesian components of epsilon_1(omega) (left column) and
    epsilon_2(omega) (right column) versus photon energy in eV. Solid and dashed
    curves compare PBE and HSE06. Off-diagonal components are omitted because
    they vanish within numerical noise for this stacking. The principal
    low-energy feature is the metallic Drude-like rise of epsilon_2 and the
    corresponding region where epsilon_1 is negative, consistent with the
    plasmon-related loss peaks discussed in the main text.

吸收/EELS/n/R/k 的图注至少要写: three heterostructures; in-plane vs out-of-plane; PBE vs
HSE06; 单位; 主峰大致能量(可见区吸收, 4-6 eV 的 pi plasmon, 16.5-18.5 eV 的 pi-sigma plasmon). 不要再出现
一个单词的 caption.

可读性(Examiner 2 点名, 必须做, 不是可选美化):

- 图例字号至少与正文接近(不要 6 pt).
- 不要九宫格硬塞进一页; 4.29/4.30 按 PBE / HSE06 拆成两图, 或按 in-plane / out-of-plane 拆.
- 线型除颜色外加 dash/dot, 因为印刷可能黑白.
- 用打印稿或 pdftoppm 渲染后检查, 不要只看屏幕放大.
- 主文 Figures 4.9-4.14 同样检查; 审查点名的是 4.29-4.30, 但同一套多面板光学图都有风险.

6.3 第 4 章不必大改的部分

计算方法(VASP, PBE+D3, HSE06 光学)已经比第 6 章完整. 不要为了"和审查语气对齐"去贬低这章; 把它定位为 systematic map 即
可.

7\. 第 5 章 o-B14(科学上最强, 口径必须收紧)

7.1 Figure 5.1 必须前移(Examiner 2, 小但明确)

现在: methods 在 p.151, Figure 5.1 在 p.155 的 results 里才出现. 读者在 methods 里读 k 点, 氢吸附位, 单层/
双层真空时, 还不知道 G2/G3/G7 和单层/双层长什么样.

措施: 在 Introduction 末或 Computation methods 开头就 \ref{fig: ob14_atomic_structure}, 把
figure 环境提前. 不必重画, 只需浮动位置和第一次引用前移.

7.2 稳定性: 四个词不要混用(Examiner 1 最狠的一条)

审查原话:

    Cohesive energies, phonons, and a very short 5.5 ps AIMD trajectory
    establish energetic preference relative to selected references, dynamical
    stability, and short-time thermal persistence, but do not by themselves
    establish thermodynamic stability or synthesizability.

现在正文(src/project_2_main.tex 约 507-508 行)写的是:

    Using ab initio molecular dynamics calculations at a temperature of 400 K
    within VASP, we also verified that the hydrogen-terminated bilayer is
    thermodynamically stable.

这句必须删掉.400 K, 短轨迹(审查写 5.5 ps, 请你对照 Figure 5.22 / S2.10 横轴, 把真实时长写进 methods)只能支持
short-time thermal persistence.

建议替换:

    Phonon dispersions without significant imaginary frequencies indicate
    dynamical stability of the pristine monolayer, the pristine bilayer, and the
    hydrogen-terminated bilayer, relative to the supercells used here. Cohesive
    energies show that these two-dimensional phases are less favourable than
    selected bulk references, as expected for metastable two-dimensional
    allotropes. An AIMD trajectory of [FILL: e.g. 5.5 ps] in the [FILL: NVT]
    ensemble at 400 K, with a time step of [FILL] and [FILL: Nose-Hoover]
    thermostat, shows that the hydrogen-terminated bilayer does not reconstruct
    or lose hydrogen on this short timescale. These tests do not establish
    thermodynamic stability on the convex hull, nor experimental
    synthesizability.

Abstract / Conclusions 里如果还有 "remain dynamically stable" 可以保留; 如果出现 "stable
two-dimensional boron" 而不加限定, 改掉.Ch 7 同步.

7.3 声子虚频前后矛盾(Examiner 1 点名)

主文 5.4.2.2:

    we find that the hydrogen-terminated bilayer is dynamically stable ...
    presence of imaginary frequencies for the latter [H-monolayer], but not for
    the former [H-bilayer].

Figure 5.21 / S2.9 图注:

    Small negative frequencies appear around the Gamma point for the
    hydrogen-terminated bilayer. These small negative frequencies are often
    found in 2D materials and do not by themselves indicate dynamical
    instability.

审查委员两边都读了. 措施: 主文承认 Gamma 点附近的小负频, 并给出判断标准.

建议英文:

    For the hydrogen-terminated bilayer, small negative frequencies appear near
    Gamma (Figure 5.21). Their magnitude is below [FILL: e.g. 20 cm^{-1}] and
    they are confined to the long-wavelength region. Such features are common in
    two-dimensional calculations and can arise from numerical noise, supercell
    size, or the treatment of flexural modes; they do not, by themselves,
    indicate a lattice instability. In contrast, the hydrogen-terminated
    monolayer exhibits imaginary branches over a wide portion of the Brillouin
    zone and is therefore discarded.

把 "No imaginary frequencies are present" 这种绝对句只留给真正干净的谱(pristine
monolayer/bilayer, 若确实干净).

7.4 单层: AFM 半导体 vs 光学讨论里的金属(Examiner 1 点名, 必须写清)

事实(现稿):

- Table: monolayer = antiferromagnetic semiconductor.
- HSE06: AFM 比 FM 低 0.02 eV, AFM 开隙 0.105 eV.
- 光学: Except for the bilayer, the structures show characteristic metallic
  behaviour, namely a large value at low energies due to intraband absorption
  from free electrons. 单层被算进金属.
- 吸收: For all structures except bilayer o-B14, the threshold is close to zero,
  corresponding to their metallic nature.

0.02 eV 的 AFM-FM 差本身就要写 "within typical DFT uncertainty; both channels were
considered". 光学如果用了非自旋极化或 FM 金属态, 低能 Drude 是人为的, 不能用来证明 AFM 半导体有带内等离子体.

措施(必须在光学小节开头写死):

    Optical spectra of the monolayer were calculated for the [FILL:
    non-spin-polarised / ferromagnetic / antiferromagnetic HSE06] electronic
    state. In the antiferromagnetic HSE06 ground state the monolayer is a
    semiconductor with a 0.105 eV gap, so a finite absorption onset is expected
    and a Drude (intraband) term should not be included. Spectra discussed below
    for the monolayer therefore correspond to [FILL]. Plasmon-related
    conclusions for the monolayer are restricted to that electronic state and
    are not claimed for the AFM semiconductor.

如果当年光学就是非自旋极化金属态, 就承认这是与磁基态不一致的近似, 并把单层等离子体从"结论"降为"金属参考通道的结果". 不要让摘要继续同时说
"magnetism in the monolayer" 和 "the monolayer supports directional plasmonic
modes" 而不加状态.

PBE vs HSE06(审查已给了可用表述, 几乎可以直接写):

    The PBE functional yields a metallic or near-metallic monolayer, whereas
    HSE06 opens a 0.105 eV gap in the AFM state. This is the expected effect of
    reducing self-interaction and delocalisation error on an electron-deficient
    boron network. HSE06 remains an approximation: the quantitative gap is not a
    quasiparticle gap, and we do not claim GW accuracy.

7.5 超导流程写到可重复(Examiner 1)

现在 methods 已经有 QE, cutoff 45 Ry, k/q 网格, Wannier90, EPW, Allen-Dynes, anisotropic
ME, mu\* = 0.13. 审查要的是一条因果链, 让读者知道每个量从哪来. 在 5.3 或 5.4.3 加一段:

    Superconducting properties are obtained in four steps. (1)
    Density-functional perturbation theory in Quantum ESPRESSO supplies phonons
    and electron-phonon matrix elements on a coarse k/q grid. (2) Maximally
    localised Wannier functions (B s and p projections) interpolate the
    electronic structure. (3) EPW interpolates the electron-phonon matrix
    elements onto dense grids and constructs the Eliashberg spectral function
    alpha^2 F(omega), the coupling strength lambda = 2 int d omega alpha^2
    F(omega)/omega, and the logarithmic average frequency omega_log. (4) Tc is
    estimated from the Allen-Dynes formula and, independently, from the
    anisotropic Migdal-Eliashberg equations with mu* = 0.13. The two estimates
    are reported separately; the 24.3 K value quoted in the abstract is the
    anisotropic Migdal-Eliashberg Tc of the hydrogen-terminated bilayer.

把 abstract 的 24.3 K 和正文 Allen-Dynes 28.2 K(体相)的归属写死, 避免审查委员以为数字打架.

mu\* = 0.13 已经有文献辩护, 保留, 但 Ch 7 limitations 里写: Tc 对 mu\* 敏感, 本工作没有扫描 0.10-0.16 以外的值
.

7.6 等离子体声称要降调

审查: stability, superconductivity, and plasmon claims require careful
qualification and are not experimentally demonstrated.

把 "supports directional plasmonic modes" 写成操作定义:

    We identify a directional plasmonic feature operationally as a photon-energy
    window in which epsilon_1(omega) < 0 along one Cartesian direction while
    epsilon_2(omega) remains small, coincident with a peak in the energy-loss
    function L(omega). This is a dielectric-function diagnostic within the
    independent-particle approximation; it is not an experimental EELS
    demonstration, and it does not include local-field or excitonic corrections.

8\. 第 6 章 Beryllene(新意最大, 完成度最低, Must 最多)

8.1 新结构是怎么来的(Examiner 1 点名)

现在只说 we also identify a cubic trilayer beryllene structure. This structure
adopts an AB stacking arrangement... 然后补了一句测过 two-layer / four-layer cubic 和 1-4
层 graphene-like, 声子不稳定. 没有生成协议.

在 6.4.1 补一段可重复的构造史. 按你真实做法填:

    The cubic trilayer structure was constructed by [FILL: cutting a three-layer
    (111) slab from bulk bcc Be / placing two honeycomb Be sheets in AB stacking
    and inserting a third layer at hollow sites / ...]. Lattice vectors and
    internal coordinates were then fully relaxed with PBE+D3. To test whether
    the motif is unique to three layers, we relaxed two-layer and four-layer
    cubic slabs, and graphene-like Be sheets from one to four layers; all of
    these alternatives show imaginary phonon branches and were discarded. Among
    the cubic-family slabs considered, only the trilayer is dynamically stable.
    We therefore present it as a theoretically identified metastable allotrope,
    not as a globally searched ground state: no unconstrained
    evolutionary/cluster search was performed.

最后一句很重要. 没有 global search 就不要让读者以为"我们预测了铍的二维基态".

相对体相内聚能不利 0.43-0.79 eV/atom, 必须说这是 metastable relative to bulk hcp Be, 与 graphene
相对 diamond/graphite 的逻辑类似, 但不能推出可合成.

8.2 金属相上的 Z2(本备忘录里科学风险最高的一条)

审查:

    the Z2 claim needs justification because the phase is described as metallic.

现稿自己写: cubic trilayer shows metallic behaviour, with multiple bands crossing the
Fermi level; 同时又用 Fu-Kane 乘积给出 nu = 1.alpha-beryllene 也是金属, 却报 non-trivial(跟随 Li
2023).

Fu-Kane 2007 的 parity 判据的对象是绝缘体中被能隙隔开的占据流形. 金属里占据数随 k 变, Z2 不是自动有定义的. 可以做的合法表述只有两类:

1. 在 TRIM 上存在一组被局部能隙隔开, 数目固定的 Kramers 对, Z2 刻画的是这组带的宇称反转; 体系整体仍是金属.
2. 若 TRIM 上占据/未占据没有能隙, 则不应把 nu = 1 说成拓扑绝缘体, 最多说 "parity inversion among bands near
   E_F".

措施:

- SOC 能带图上标出用来计数的占据流形和局部 gap(若有).
- 写明每个 TRIM 计入的 Kramers 对数(表里 alpha 在 Gamma 是 2 个 +/-, cubic 在 Gamma 是 6 个, 要解释为什么
  是这些带而不是"所有电子").
- Abstract / Conclusions 的 topologically protected electronic states 必须降调.

建议英文(可直接改 abstract 相关句):

    Using the Fu-Kane parity criterion on the inversion-symmetric structures, we
    find a non-trivial parity product for alpha-beryllene and for cubic trilayer
    beryllene, and a trivial product for beta-beryllene, in agreement with
    previous work on the alpha and beta phases. Both alpha-beryllene and the
    cubic trilayer are metallic. The Z2 index reported here therefore classifies
    a parity inversion in an isolated set of occupied Kramers pairs at the TRIM
    points; it does not establish a bulk-insulating quantum spin Hall phase, and
    it does not by itself imply dissipationless edge transport. Helical edge
    states, if present, would coexist with bulk metallic channels. A Wilson-loop
    or ribbon calculation is left to future work.

Ch 1 的拓扑引言(上面 1.6)和这里必须一致.

8.3 没有 HSE06(Examiner 2-1)

Ch 4/5 有 PBE+HSE06, Ch 6 只有 PBE. 审查要的是理由, 不是必须重跑全部光学.

如果不能补全套 HSE06 光学(对 105x105x1 的光学网格, hybrid 非常贵), 就在 6.3 写正当理由, 并在 6.4.3 把 2H-alpha
的带隙标成 PBE 下限:

    Chapters 4 and 5 required HSE06 because they contain semiconductors whose
    gaps and optical onsets are quantitatively sensitive to the
    exchange-correlation approximation. Chapter 6 is dominated by metallic
    phases, for which PBE already captures band crossings, metallic screening,
    and the qualitative anisotropy of epsilon(omega). The one gapped phase,
    2H-alpha-beryllene, has a PBE indirect gap exceeding 4 eV; PBE is expected
    to underestimate this gap, so the true gap is larger and the system remains
    a wide-gap semiconductor. Hybrid optical spectra on the dense k-meshes used
    here were not feasible. We therefore report PBE trends and do not claim
    quantitative peak positions for the 2H-alpha onset.

Should / Optional: 只对 2H-alpha(和必要时 alpha)补 HSE06 能带, 不必补光学. 这能把 "exceeding 4.0 eV
at PBE, actual gap larger" 变成数字, 性价比最高.

8.4 收敛: 图在 SI, 正文不能让读者自己读图(Examiner 2-2)

现在 6.3 只有:

    Convergence tests show that these settings yield accurate results for the
    cohesive and total energies, as shown in figures ... The convergence of the
    dielectric function ... is shown in figures ...

补一段把判据说出来, 例如:

    Total and cohesive energies change by less than [FILL: e.g. 1 meV/atom]
    between the 27x27x1 (25x25x1 cubic) meshes used for relaxation and the next
    denser meshes tested in Figures 6.16-6.17. For the dielectric function,
    increasing the number of unoccupied bands beyond [FILL: 133 for pristine 2D;
    140 for hydrogenated; 66/70 bulk] and densifying the k-mesh beyond [FILL:
    105x105x1] does not shift the principal epsilon_1 zero-crossings or
    epsilon_2 peak positions by more than [FILL] eV (Figures 6.18-6.27). These
    thresholds determine the meshes used in the main text.

数字从 SI 图上读, 不要写 "the graphs show convergence" 就结束.

8.5 Figures 6.2 和 6.3 的绿/蓝球(Examiner 2-3)

图注完全没解释. 请你打开 VESTA/源图确认后写入图注. 最常见的是按层着色(beta 双层两色; cubic 三层三色)或按不等价 Wyckoff 位.

建议图注句(按层为例, 若不符就改):

    Beryllium atoms in different atomic layers are shown in different colours
    (green: upper layer; blue: lower layer; [FILL: third colour] for the central
    layer of the cubic trilayer). Hydrogen atoms are shown as small white/pink
    spheres. The colouring does not indicate different elements.

正文 6.4.1 第一段也写一句, 不要只改 caption.

8.6 为什么氢化 alpha/beta 却不氢化 trilayer(Examiner 2-4)

现稿只说 alpha 做双面, beta 做单面和双面, 筛选后留下 2H-alpha, 1H-beta, 2H-beta. 对 cubic trilayer 的氢化完全
沉默. 审查委员一定会问.

二选一, 必须诚实:

- 若做过: 报最稳定吸附位, 吸附能, 声子是否虚频, 为何不进入主文.
- 若没做过, 用下面这段:

    Hydrogenation was restricted to the previously proposed alpha and beta
    frameworks in order to isolate the effect of hydrogen on structures already
    discussed in the literature. Hydrogen termination of the cubic trilayer was
    not attempted; whether H can open a gap in that stacking remains an open
    question and is listed in Chapter 7.

不要事后编"我们考虑过但不稳定", 除非真算过.

8.7 AIMD 方法细节(Examiner 2-5)

Figure 6.5 的图注只有 energy/temperature vs time 和结构快照, 没有 T, 时长, ensemble, timestep. 正文也没
有. 审查等于开卷考试.

在 6.3 或 6.4.2 补:

    AIMD simulations of the hydrogen-functionalised phases were performed in
    VASP in the [FILL: NVT] ensemble at [FILL: e.g. 300 K], using a time step of
    [FILL: e.g. 1.0 fs], a [FILL: Nose-Hoover] thermostat, and a total duration
    of [FILL: e.g. X ps] after [FILL] of equilibration. The trajectories in
    Figure 6.5 show that the total energy fluctuates about a constant mean and
    that the beryllene framework does not collapse. As in Chapter 5, this is
    evidence of short-time thermal persistence, not of thermodynamic stability.

把 Figure 6.5 图注同步写上 T 和时长.

8.8 二维光学归一化(Examiner 1-8)

Ch 5 正文有 epsilon^{2D} = (d_SC / d_2D) epsilon^{SC} 公式.Ch 6 只说 using the
two-dimensional dielectric-function renormalization method 并指向 SI 厚度. 审查明确要
appropriate two-dimensional normalisation.

措施: Ch 6 methods 直接引用 Ch 5 的公式编号, 并列 SI 里那串 d_2D(alpha 3.96 A, beta 5.85 A, cubic
6.97 A, 2H-alpha 3.14 A, 1H-beta 5.52 A, 2H-beta 5.192 A). 主文不要只说 "see SI".

厚度定义要和 Ch 5 一致(顶底原子间距 + 两侧 vdW 半径). 若 cubic / 氢化结构用了不同定义, 写出来.

9\. 第 7 章 Conclusion and Outlook(现在约 4 页, 几乎全是重复摘要)

Examiner 2:

    should provide a more critical assessment of the limitations ... distinguish
    between systems that have already been experimentally found ... future work
    section simply lists potential theoretical directions ... discuss specific
    improvements that could be expected.

建议结构(仍用英文写正文):

7.1 Collective conclusion(半页, 不要再把三章结果背一遍)

回到 Ch 1 的那一句问题, 给出答案: 轻元素 xene 可以通过键合拓扑, 堆垛和氢化在同一元素族内切换金属/半导体, 开关等离子体各向异性, 并在特定网络中出现磁
性和声子介导超导.

7.2 What is experimental and what is predicted

重用 Ch 1 的表, 缩短. 明确:

- 实验: graphene, borophene, BC3, graphene-borophene, 二维 Be 薄片(Chahal), 体相 hcp Be.
- 本文预测: Graphene-BC3/B4C3 光学图, 2D o-B14 家族, cubic trilayer, H-beryllene, 单层磁性
  , H-bilayer 超导, Z2 标记.

7.3 Limitations of the theoretical approach(审查点名, 必须新写)

建议逐条:

1. Exchange-correlation. PBE 低估半导体带隙; HSE06 是 pragmatic hybrid, 不是准粒子方法.Ch 6 金属相停在
   PBE.
2. Optics. 全部是独立粒子介电函数: 无 local fields (RPA beyond IPA), 无 GW, 无 BSE 激子. 绝对峰位和可见区吸收强
   度都可能移动. 二维归一化依赖 d_2D 的定义.
3. Stability. 声子 = 动力学稳定; 短 AIMD = 短时不坍塌; 内聚能相对选定参考 = 不是 convex hull. 无衬底, 无生长动力学, 无化
   学势相图.
4. Magnetism. AFM-FM 差仅 0.02 eV, 落在 DFT 误差内; 单层磁基态对泛函敏感(PBE vs HSE06 vs r2SCAN 已在
   SI, 结论里点一句).
5. Superconductivity. mu\* 经验取值; 各向异性 ME 仍是中等耦合框架; 无实验 Tc.
6. Topology. 弱 SOC 的轻元素; 金属相上的 Z2 只是宇称反转诊断; 无 Wilson loop, 无 ribbon edge states.
7. Environment. 所有 2D 计算都是真空中的自由站立层; 实验 borophene / beryllene 在衬底或溶液环境中, 电荷转移和应变未包
   含.

7.4 Future work, 每条必须有"预期改进"

不要再写 strain, doping, moire, electric field 清单. 改成:

GW+BSE optics on the gapped phases (bilayer o-B14, 2H-alpha)
  预期改进: Corrects IPA peak positions and may bind excitons below the
  independent-particle onset

HSE06 or GW bands for 2H-alpha (if not already added)
  预期改进: Places a quasiparticle lower bound on the wide gap

Longer AIMD (tens of ps) and H-desorption barriers
  预期改进: Tests whether hydrogen remains bound, which 5 ps cannot

Convex-hull / chemical-potential diagrams vs bulk B, Be, BeH2, graphene
  预期改进: Converts "dynamically stable" into a synthesizability argument

Wilson loop or Be-terminated ribbon for cubic trilayer
  预期改进: Tests whether the metallic Z2 marker produces edge modes

Substrate models (Ag for borophene; realistic supports for beryllene)
  预期改进: Estimates doping and epitaxial strain present in experiment

mu\* scan and anharmonic phonons for H-bilayer o-B14
  预期改进: Bounds the uncertainty on the 24.3 K Tc

Experimental collaboration: Raman/EELS on graphene-borophene; transport on any
synthesised o-B14 sheet
  预期改进: The only way to promote predictions to observations

Outlook 里现有的 "Future work can first test these theoretical predictions through
experimental synthesis..." 可以保留为第一段, 但后面必须接上这种具体改进.

10\. 贯穿全文的用语: 建议统一替换

这些句子在摘要, Ch 1, Ch 5, Ch 6, Ch 7 重复出现, 审查委员是对照着读的. 统一口径比改公式更重要.

不要再写: thermodynamically stable(基于短 AIMD)
改成: dynamically stable; remains intact over an AIMD trajectory of X ps

不要再写: confirms the stability
改成: confirms dynamical stability relative to the phonon supercell used

不要再写: identifies a stable cubic trilayer
改成: identifies a dynamically stable, metastable cubic trilayer (not on the bulk
convex hull)

不要再写: topologically protected electronic states(对金属)
改成: a non-trivial Fu-Kane parity product for an occupied manifold; not a QSH
insulator

不要再写: supports plasmons
改成: shows dielectric-function signatures of directional plasmonic response
(epsilon_1 < 0, peak in L(omega)) within IPA

不要再写: the monolayer is metallic(光学段)
改成: 先声明光学计算用的电子态; AFM HSE06 基态是 0.105 eV 半导体

不要再写: possible chiral optical behaviour(当作结论)
改成: finite epsilon_xy required by P3 symmetry; chirality not demonstrated

不要再写: promising for devices(无限定)
改成: 可留一句, 但 Ch 7 必须立刻接 limitations

11\. 图注与印刷检查清单

按审查点名的优先级做. 印刷版是 Examiner 2 的明确标准: without requiring access to the published
article.

必须重写图注:

- Figs 4.29-4.36(S1.17-S1.24): 见上面 6.2.
- Figs 3.1-3.6: 补 "calculated in this thesis, analysed in Chapter 6".
- Figs 6.2, 6.3: 补绿/蓝(及第三色)含义.
- Fig 6.5: 补 ensemble, T, timestep, duration.
- Fig 5.21 / S2.9: 与主文统一"小负频"说法.
- Fig 5.10 光学: 若单层光谱不是 AFM 基态, 图注写电子态.

必须检查字号/拆图:

- 4.29, 4.30 以及任何多面板光学图(4.9-4.14, 4.25-4.28, 5.10-5.12, 6.9-6.15).
- 能带+DoS 组合图(4.5-4.7, 5.2, 6.6).
- 打印一页真 A4, 或 pdftoppm -r 150 后不放大阅读.

建议自包含的图注要素(以后所有新图按此):

体系名称; 面板含义; 线型/颜色编码; 泛函; 极化方向; 单位; 一句话主特征. 不要再出现 "Absorption coefficient." 这种 caption.

12\. 建议动手顺序(按审查权重, 不是按章节号)

1. 作者贡献段落(Publications + 三章章首). 半日可完成, 审查两人都点了.
2. Ch 5 口径(热力学用词, 声子负频, 光学电子态, EPW 四步, Fig 5.1 前移). 不改结论, 只改不会被追问的句子.
3. Ch 6 方法诚实化(结构构造, Z2 降调, HSE06 理由, 收敛文字, 颜色, 氢化范围, AIMD 参数, 2D 归一化). 这是 Examiner 1 认为"
   最 novel 但最弱"的一章.
4. Figs 4.29-4.36 图注 + 字号. 需要出图, 但科学上零风险.
5. Ch 1 重写 与 Ch 2-3 搬迁 + methods 表. 工作量最大, 但是 thesis 能不能"立住"取决于这两步. 可以先写 Ch 1 的
   1.5-1.8(光学动机, Z2, 贯穿结论), 再补文献.
6. Ch 7 重写. 必须等 1-5 的口径定了再写, 否则 limitations 会和正文打架.
7. 最后填 report/reply_to_examiners.md 的页码和蓝色回复, 并对照本备忘录逐条勾.

第 4, 5 章已发表/接收: 除图, 图注, 贡献声明, claim 边界外, 不要改数据. 第 6 章若只补 2H-alpha 的 HSE06 能带, 在回信里写 "an
additional HSE06 band structure has been added for the gapped 2H-alpha phase;
dense-grid hybrid optics remain computationally prohibitive and are justified in
section 6.3".

13\. 回信时怎么映射(供以后填 report/reply_to_examiners.md)

下面是审查条目到本备忘录章节的对照. 改完论文后, 用真实页码替换 p. xx.

Examiner 1

贡献写清; new vs known
  改哪里: Publications; Ch 4-6 章首; Table 1.1
  回信要点: 列出 candidate 工作; 表区分实验/预测

Ch 1 无 gap; Ch 2-3 太长
  改哪里: Ch 1 重写; Ch 2-3 压缩进 Appendix; Table 2.1
  回信要点: 写减少了多少页, 哪些节进 Appendix

三章互不隶属; 光学无问题; 拓扑无动机
  改哪里: Ch 1 的 1.5-1.8
  回信要点: 摘录 "one thesis / optical questions / Z2 caveat" 新段落

Figs 4.29-4.36 图注
  改哪里: SI captions
  回信要点: 新图注要素列表

Ch 5 稳定性/AIMD/虚频/AFM vs metal/HSE06/EPW
  改哪里: Ch 5 methods + 5.4.2-5.4.4
  回信要点: 逐句替换 thermodynamically stable; 声明光学电子态

Ch 6 结构起源; 金属 Z2; 2D 归一化
  改哪里: Ch 6.4.1, 6.4.4, 6.3
  回信要点: 降调 topology; 给出构造步骤

Examiner 2

专门文献综述
  改哪里: Ch 1.2-1.4, 1.7

Ch 3 示例来源
  改哪里: Figs 3.1-3.6 图注 + 正文交叉引用 Ch 6

多作者贡献声明
  改哪里: 同 Examiner 1

图 4.29/4.30 印刷不可读
  改哪里: 重出图

Fig 5.1 太晚
  改哪里: 前移

Ch 6 无 HSE06
  改哪里: 6.3 理由(+ 可选 2H-alpha HSE06 能带)

收敛未讨论
  改哪里: 6.3 写判据数字

绿/蓝球
  改哪里: Figs 6.2-6.3

不氢化 trilayer
  改哪里: 6.4.1 一段

AIMD 细节
  改哪里: 6.3 与 Fig 6.5 图注

Ch 7 limitations / 实验 vs 理论 / future work 的预期改进
  改哪里: 新的 7.2-7.4

14\. 不需要做, 但容易做错的事

- 不要为了"显得 Ch 6 和 Ch 4/5 一样完整"而在截止日期前强行上全部 HSE06 光学. 写不清的 hybrid 光学比诚实的 PBE 理由更危险.
- 不要在没有 Wilson loop / edge 计算的情况下, 把金属 cubic trilayer 写成 quantum spin Hall
  material.
- 不要把 5.5 ps AIMD 说成 thermodynamic stability 的"补充证据"——审查已经告诉你这不是.
- 不要重写已发表第 4 章的科学故事; 增量工作被承认了, 缺的是贡献, 图和图注.
- 不要把 Ch 2 删到读者看不懂 HSE06 和 IPA. 砍的是时间演化/Thomas-Fermi/Hartree, 不是 KS 和介电函数.
- 不要在 Ch 1 堆 50 篇 borophene 综述. 批判性 = 每类工作用 2-4 篇代表, 立刻接到 gap.
- 不要改 assistance/ 以外的文件来"先替我改论文"——按你的要求, 论文由你本人改.

以上是对照 2026-08-26 编译稿和两份 examiner reports 的逐条措施. 优先顺序见第 12 节. 核心不是加计算量, 而是把已经算出来的东西,
用审查委员能接受的物理口径写成一篇 thesis.
