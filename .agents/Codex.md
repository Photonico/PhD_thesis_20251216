# Codex

## 2026-09-19 基于两份 examiner reports 的论文修改建议

### 阅读范围与使用方式

本次建议以当前编译版 `.output/thesis.pdf` 为准, 并交叉核对相应 LaTeX 源文件. PDF
共 270 个物理页面; 正文第 1 页位于 PDF 第 29 页, 以下"p." 均指论文印刷页码, 正文
通常可用"印刷页码 + 28" 定位 PDF 页面. 源文件行号是本次检查时的位置, 修改后会变化,
应同时使用章节, 图号和 LaTeX label 定位.

实际评审目录名为 `report/`, 不是 `reports/`. 已完整读取两份原始评审:

- E1: `report/Lu_Niu_PhD_report_20260824.pdf`, 2 页.
- E2: `report/PhD Examination Report - Lu Niu.docx`.
- 辅助材料: `report/reply_to_examiners.md`, 这是已有回复草稿, 不是第三份评审, 也
  不能作为"修改已完成" 的证据.

本次只新增/追加此建议文件; 未修改, 重编译或替换论文, 图表, 计算脚本, 评审和回复
草稿, 也未改动其他模型的建议文件. 阅读覆盖评审涉及的各章正文, 方法和补充材料;
PDF 视觉核查聚焦评审点名的图和关键证据页, 并非 270 页逐页版式验收. 部分技术问题
另查了官方计算软件文档, 原始论文, 以及论文自己提供的公开数据仓库. 公开仓库文件未
必与当前 PDF 使用的数据版本相同, 下面明确保留这一限制.

下面中文解释修改原因和步骤; 英文段落是供作者核实, 改写后采用的候选文本. 方括号
`[... ]` 表示必须从本人记录补齐的内容, 不能原样提交. 所有建议均为待执行事项, 不
能在回复评审时写成已经完成.

### 总体判断和修改优先级

两位评审均认可工作的原创性和博士论文规模. 修改的关键在于让读者能够顺着"已有研究
→ 尚未解决的问题 → 本章模型和方法 → 证据支持的结论 → 适用范围" 阅读整篇论文. E2
要求更全面的文献综述, E1 要求缩短理论章节, 两者可以同时实现: 增加针对研究问题的
批判性比较, 压缩与后续计算联系较弱的教材式推导.

建议按以下次序处理:

1. P0 科学一致性与计算溯源: 先核实第 5 章磁态, 泛函与光谱对应关系, 虚频和 AIMD
   图的身份; 第 6 章金属体系的拓扑判据; 第 4 章非对角光学量的定义和后处理; 第 5,
   6 章氢吸附能公式. P0 是本次审阅给出的优先级, 不代表 examiner 已逐项认定数据
   错误.
2. P1 评审明确要求的实质修订: 研究主线, critical literature review, 实用方法路线,
   结构生成过程, PBE-only 解释, 可复现参数, 二维归一化解释, 各章贡献声明, 结论
   局限与未来工作的预期改进.
3. P2 呈现与收尾: 图 4.29–4.36 的重绘和图注, 图 5.1 前移, 图 6.2–6.3 颜色说明,
   来源说明, 出版状态, 页码和回复草稿占位符. 涉及科学含义的图注不能仅按排版任务
   处理.

不建议先把所有篇幅投入英语润色, 也不建议一开始就全面补算 HSE06, GW/BSE 或长时
AIMD. 先确定结论到底依赖哪项证据, 再决定最小必要核查和补算; 若无法补算, 应收窄结
论, 并正面说明限制.

为避免把评审意见机械套回论文, 以下几项当前已经存在, 修改时应在其基础上补实:
Introduction 已有总体目标和章节概述; 前置页已有论文书目信息及署名声明标题; 第 5,
6 章已有部分二维光学归一化说明; 第 6 章明确写过 SOC; 第 6 章部分 AIMD 信息在补
充材料中存在. 问题主要是证据链不完整, 信息分散或相互不一致.

### 内容导航

- 全篇结构: 研究主线, 文献综述, Chapters 2–3 精简与方法补全, 贡献声明, Chapter 7
  局限与展望.
- 第 4 章: C4.1–C4.6, 贡献定位, 逐图修改, 光学张量后处理, 单位及结论范围.
- 第 5 章: C5-1–C5-9, 电子/磁态一致性, Drude, 虚频, AIMD, 超导流程和结构图.
- 第 6 章: C6-01–C6-10, 氢参考态, Z2, 模型生成, 氢化筛选, AIMD, 归一化和
  PBE-only.
- 执行与回复: 四轮修改顺序, 英文回复模板, 两份评审的逐条覆盖清单.

### 全篇结构, 文献综述, 方法, 作者贡献与结论

#### 1. 首先精确诊断现状, 避免"已经有的内容" 被说成完全缺失

- Chapter1 是 pp1–4, `src/introduction.tex:1–73`. 已有轻元素, 维度, 堆叠, 氢化的
  共同主题(lines21–40), 也已有逐章目标和结果概览(48–73). 缺的是从前人证据到
  明确知识缺口的推理, 可检验的 thesis-level research questions, 以及区别实验材料
  /理论原型的 critical literature review; 不是完全没有 motivation.
- Chapter2 实际正文 pp5–77(73页), p78空白; Chapter3正文 pp79–109(31页), p110
  空白. 两章正文共104页, Chapter4 p111开始. 压缩对象很明确, 不需要重写全部理论.
  可将与实际计算无直接关系的推导移到附录或大幅精简.
- 各研究章已经有局部参数: Chapter4 methods `src/project_1_main.tex:95–139`,
  Chapter5 `src/project_2_main.tex:149–299`, Chapter6
  `src/project_3_main.tex:150`后. Examiner1要的是前置, 连贯, method-oriented 的
  路线图, 以及缺失的复现信息; 不应重复写"全文无计算参数".
- Publications 前言 ppv–vi (`src/publications.tex:15–33`) 已列第4, 5, 6章论文;
  ppvi, lines52–55已有"Authorship attribution statement" 标题及导师确认语, 但上文
  只是作者名单/题录, 没有具体角色. 第4–6章分别开篇直入 Abstract (
  `src/project_{1,2,3}_main.tex:1–4`). 因此应补"章首 publication and
  contribution statement", 补实前置 attribution 内容, 不必机械新增另一份空泛声明.
- Conclusion pp217–220, `src/conclusion.tex:71–79` 已有实验表征渠道和理论未来方
  向. 真正欠缺的是针对当前局限的判断: 为什么要做, 用哪项证据消除哪项不确定性, 预
  期会改变/检验什么, 以及什么结果会削弱当前结论.

#### 2. Chapter1: 用同一研究问题组织三个项目

##### 建议主线

不要把"轻元素能有多种 quantum properties" 当作唯一问题, 它太宽泛; 也不宜把
graphene zero band gap 作为所有项目唯一动机, 因为后文多个体系有意保持金属性并研
究等离激元和超导. 可将主线收敛为: 不同键合环境中的层间耦合, 降维和氢化如何改变能
带与方向依赖的光学响应; 这些结构变化何时进一步导致磁性, 电子-声子耦合和非平庸能
带拓扑; 每种预测的证据边界是什么.

建议保留七章编号, 最低改动方案是在 Chapter1 添加明确的 literature review
sections; 将 Chapter2 改造为计算方法, 将 Chapter3保留为短而实用的
optical-response 方法章. 以下英文目录是可编辑方案, 并非学校/考官要求的固定格式或
页数:

1. `Scientific Context and Scope`
2. `Critical Review of Boron-Based Two-Dimensional Materials`
3. `Critical Review of Beryllene and Hydrogen Functionalization`
4. `Computational Approaches, Established Results, and Open Questions`
5. `Research Questions and Original Contributions`
6. `Thesis Structure`

文献综述每小节都按四步组织: 已有研究观察/预测了什么; 以什么结构/基底/理论层级得
到; 哪些重要问题未得到回答; 本论文如何在限定范围内推进. 第4–6章保留项目特有文献,
删去每章重复 graphene/Xene 通史, 以交叉引用 Chapter1替代.

##### 可直接改写的英文研究问题

> RQ1. How does interfacial coupling between graphene and selected boron-based
> monolayers modify the electronic structure and polarization-dependent optical
> response relative to the isolated constituents?
>
> RQ2. How do dimensional reduction and hydrogen termination change the
> electronic, magnetic, and electron–phonon properties of the
> pentagonal-bipyramid boron framework, and which changes are reflected in its
> optical response?
>
> RQ3. Which investigated beryllium structures are locally stable within the
> computational tests employed, and how do layer geometry and hydrogen
> functionalization affect their electronic structure, optical anisotropy, and
> band topology?

各问题需在对应研究章开头列为目标, 章末回答, Chapter7再次按问题综合; 每章不必覆盖
所有 observable, 也不必声称三种材料拥有同一个机制.

##### 可用的英文 thesis bridging paragraph

> This thesis uses three complementary material families to examine how changes
> in bonding and dimensionality modify electronic structure and optical response
> in light-element two-dimensional systems. Graphene-based heterostructures
> provide a reference for interfacial coupling between existing monolayer
> models. The pentagonal-bipyramid boron family then isolates the effects of
> dimensional reduction and hydrogen termination within a related bonding
> network. Beryllene extends these questions to a less explored elemental system
> and to additional layer geometries. The common aim is to identify
> structure–property relationships and their computational limits; the magnetic,
> superconducting, and topological analyses address additional questions
> specific to selected systems.

##### 为什么计算 optical properties, 要放在 introduction 而非只列公式

- 对第4章: 比较异质结与孤立层能带/跃迁, 回答"堆叠改变了什么", 将吸收起始, 峰位/
  光谱权重, 偏振差异与电荷转移/轨道杂化联系起来.
- 对第5章: 比较同一键合网络不同维度/氢化, 检验电子态变化是否反映在低能响应, 各向
  异性和候选集体激发上.
- 对第6章: 用偏振和光谱特征寻找不同层结构/氢化态的可区分理论指纹; 没有实验环境
  /2D归一化/光学近似验证时, 不保证可直接用于器件性能定量预测.
- `n,k,R,alpha,L` 多由同一介电函数导出, 不是五份独立验证. 围绕少数科学问题选主图,
  其余放SI.

可用英文段:

> Optical response is used here as a probe of changes in electronic structure
> rather than as an independent catalogue of material constants.
> Polarization-resolved spectra are compared across reference and modified
> structures to identify changes in transition energies, spectral weight, and
> anisotropy. Energy-loss features are examined together with the dielectric
> response as candidate signatures of collective excitations. The interpretation
> is restricted by the treatment of intraband transitions, electron–hole
> interactions, and the normalization of the two-dimensional response, as
> specified in the methods chapters.

##### Topology 的意义要先讲物理, 再讲 parity 公式

`src/introduction.tex:69` 直接宣布非平庸 Z2, 但缺一段物理动机. 可解释"在相关对称
性和合适能隙条件下, 非平庸二维Z2能带子空间与 helical edge states 相关", 并明确
metallic band topology 和 insulating quantum spin Hall phase 的区别. 不要在
intro 宣称量子化边缘输运或已证明无耗散器件; 此点需等待第6章关键判据核验后同步定
稿.

#### 3. Literature review: 优先使用已有文献, 补批判性比较

以下既有 BibTeX keys 已在仓库核实; 除另列在线核验者外, 具体方法细节仍应作者回到
原文逐条核实, 不可从题目推断成事实.

- 异质结实验与模型边界: `liu2019borophene`(`thesis.bib:1333`, 已在线核实原文摘
  要: 实现 lateral/vertical integration), `hou2021borophene`(1324),
  `yanagisawa2004phonon`(1247), `tanaka2005novel`(1259),
  `yanagisawa2006phonon`(1270). 综述应区分基底支持的实验 BC3/borophene 或
  heterostructures 与论文计算的具体自由悬空, 配准, 应变, 相型, 不以"该材料类别已
  制备" 等同"本模型已验证".
- 2D boron-carbide 预测: `tian2019`(1665), `luo2011predicting`(1743),
  `fan2018two`(1755). 应说明第4章是已知结构与界面组合的结构-性质系统映射, 非首
  次发现这些单层.
- boron 维度/氢化/量子性质: `gao2017prediction`(1972), `zhu2019magnetic`(1927),
  `chen2022synthesis`(2062), `hou2020ultrastable`(2073),
  `li2021synthesis`(2084). 比较对象包括结构类别, 氢覆盖度, 基底, 稳定性证据及
  采用的泛函/电子-声子方法.
- o-B14 起点: `han2023superconducting`(1984), 原作是 bulk o-B14 及相关结构的理
  论预测, 本论文不能把 bulk o-B14发现或其29.1K初始预测计为自己的创新. 重点应是降
  维, H termination, 磁态, 光学和新分析; 重新计算已知bulk是对照/方法核查. 当前项
  目正文已经知道这一点(`project_2_main.tex:7–14,114–139`), 应将该边界提升到
  thesis-level contributions.
- Be 实验与理论: `chahal2023beryllene`(2575), `ono2020dynamical`(2552),
  `hess2022periodicity`(2564), `li2023coexistence`(2594),
  `jiang2025nonmonotonic`(2700).Chahal 2023提供"beryllene 实验已报道" 的背景,
  但不自动证明本文cubic trilayer, 指定α/β计算单胞, 氢化结构或拓扑已经实验实现.
- H-Be边界: `bachurin2015ab`(2655) 研究bulk surface adsorption, `li2018global`
  (2665) 研究Be hydride sheet, 二者可用于提出动机, 但应分清
  adsorption/termination 与生成二维化合物; 不能当作本文终止方式的直接实验验证.
- 方法批判: `heyd2003hybrid`/`krukau2006influence`/`paier2006screened`(
  513/526/563), `onida2002electronic`(584), `thygesen2017`(1204),
  `matthes2016influence`(817), 用于区分 ground-state DFT, hybrid gap,
  independent-particle optics, quasiparticle/exciton correction, 2D response. 引
  用应紧接所支持的命题, 不以一大串不同体系的光学论文证明本论文光谱来源.

值得新增且能体现 critical review 的例子: Li et al. 2023 的 beryllene 超导预测后
来有 Petrov & Milošević 的 comment, 认为 anisotropic gap-temperature曲线及Tc需重
新审视. 它是本次检索确认的2024年预印本, 不能宣布争论已定论, 也未核实是否有正式回
复. 它提醒综述比较方法/收敛/模型选择和可复现性, 而不只是列成功数字.

已在线核验的主要来源(原文/原文数据库页面):

- Liu & Hersam, [Borophene-graphene heterostructures][source-01].
- Han et al., [Superconducting boron allotrope featuring pentagonal bipyramid at
  ambient pressure][source-02], [DOI][source-03].
- Chahal et al., [Beryllene, the lightest Xene][source-04].
- Li et al., [Coexistence of superconductivity and topological aspects in
  beryllenes][source-05]. 在线方法摘录说明使用PBE/Quantum ESPRESSO, 因此可用来讨
  论本论文PBE的可比性; 它不能替代对本论文氢化半导体/光谱精度的独立论证.
- Petrov & Milošević, [comment preprint][source-06]. 建议在实际写入正文前再读全
  文并检索回复, 清楚标记预印本及争议性质.

综述的文献记录建议每篇包括: 具体结构与环境; 实验/理论身份; 方法层级; 主要发现;
未处理的限制; 与本论文哪个问题相关. 这个记录可作为写作笔记, 不必所有内容搬进正文,
也不必追求数量.

#### 4. Chapters2–3: 保留用到的概念, 改成计算决策路线图

##### 推荐削减/移位清单

- Ch2 `fundamentals_a.tex:22–538`: time evolution, Schrödinger/Heisenberg
  picture, continuity equation, 目前从p6铺到p17; 正文只保留计算所需的
  Born–Oppenheimer/electronic ground-state 前提, 详细量子力学推导放附录或参考教
  材.
- `fundamentals_a.tex:554–1018`: grand canonical, wave function to functionals,
  删重复铺垫; 保留职业读者理解 DFT 近似需要的最短论证.
- `fundamentals_a.tex:1028–1212`: functional概念无需多例逐步教学; Hohenberg–Kohn
  要点可概述, 不需保留数页完整证明.
- `fundamentals_a.tex:1662–2045`: Thomas–Fermi及局限与本论文实际KS计算间接相关,
  可缩成一段或附录.
- `fundamentals_a.tex:2501–2717`: 两组variational derivation/construction应合并.
  保留KS方程, SCF loop, XC选择以及所用PBE/HSE06含义.
- Ch3 `fundamentals_b.tex:39–231` Maxwell/constitutive derivation, `565–768`
  causality/Kramers–Kronig proof: 保留定义, 适用条件和关键关系, 不必重复教科书推
  导. 保留实际计算中用的 dielectric tensor, interband/intraband, 2D
  normalization, broadening, energy vs angular frequency, derived optics条件.
- 详细推导若迁至 Appendix, 当前 `src/appendix.tex` 是代码可用性说明, 应更名/拆成
  明确附录, 不把代码说明和几十页物理推导混为一个无编号 Appendix.

##### 方法章应给的实用内容

建议 Chapter2名为 `Computational Framework and Validation`, 有下列分节:

1. `Electronic Structure and Exchange-Correlation Approximations`: KS与
   PAW/pseudopotential; PBE与HSE06用途, 局限, 几何与电子/光学计算是否同一level;
   VASP和QE之间结构与参数一致性.
2. `Structural Models and Geometry Optimization`: 模型来源, 边界条件, slab厚度/
   真空, 应变/堆叠与氢位点, 力/能量容差, vdW correction.
3. `Brillouin-Zone Sampling and Convergence`: total-energy, force, band gap,
   optical spectra, meV磁能差需分别收敛; 不能拿总能平坦自动证明所有observable已
   收敛; 各章SI具体图号与参数表交叉引用.
4. `Energetics, Phonons, and Finite-Temperature Tests`: 参考相/参考原子能,
   harmonic phonons, supercell和声学支处理, AIMD系综温度dt时长超胞; 分开表述局部
   动力学稳定, 短时间热持续性和热力学稳定.
5. `Spin-Polarized Calculations and Magnetic Configurations`: NM/FM/AFM构型, 初
   始磁矩, 最终磁矩, 总能归一化, 是否共用几何/相同精度; 2D有限温磁有序不能仅由0K
   小能差推得.
6. `Electron–Phonon Coupling and Superconductivity`: DFPT coarse grids→Wannier
   validation→EPW dense
   interpolation→alpha2F/lambda/omega_log→Allen–Dynes/anisotropic ME; mu*, 数值
   截断与收敛, 公式旁标每个符号和单位; 不要直接从"有稳定phonons" 跳成"可超导".
7. `Spin–Orbit Coupling and Topological Analysis`: spinor计算, 对称性与反演前提,
   使用的band manifold, 全BZ能隙检查, parity/Wilson-loop及edge谱所能说明的证据
   级别.
8. `Connection to the Research Questions`: 每项方法对应材料/待解问题, 输出和限制.

Chapter3名可为
`Optical Response: Calculation, Normalization, and Interpretation`. 只需说明关键
操作和哪些结论依赖何种近似; 具体数值留研究章. 应核对`omega`记为角频率时公式需
hbar转换, 而图横轴是photon energy; 无需把本审查当作已判定单位算法错误, 实际代码/
原数据才是依据.

建议补一幅 workflow图: 结构模型→geometry/energetics→electronic state→三个分支(
phonon/AIMD; dielectric response; 特定体系的spin/EPC/SOC), 每个终点标可回答的问
题. 此图不能替代参数表.

验收标准: 只读这个方法章和对应研究章方法节, 读者能知道为什么选择此方法, 哪些参数
控制误差, 结果如何流到下一步骤, 以及哪项结论超出了方法能力.

#### 5. Ch3 optical examples: 来源问题从Fig3.1就开始, 且有直接证据

- Fig3.1 p93, `fundamentals_b.tex:529–535` 留有 `% cite my third project here`
  注释, 但caption无来源.
- Fig3.2 p101, lines863–868; Fig3.3 p103, 983–988; Fig3.4 p104, 998–1004; Fig3.5
  p106, 1083–1089; Fig3.6 p108, 1144–1150. 当前"calculated spectra" 周围列出多篇
  一般光学文献, 但没有明确这六图哪篇/哪组计算生成.`niu2024electronic` 实际是
  graphene-boron heterostructure论文, `khan2025insight`是chalcohalides; 不能用它
  们当α/β-Be光谱的数据出处.
- 处理优先级: 最简方案仅保留Fig3.1作为worked example, 其他曲线/描述迁回第6章或删
  除重复, 理论正文改交叉引用. 若保留全部, 每幅caption都给明确来源, 计算泛函, 偏
  振分量, 归一化约定; 避免仅在某一段笼统说明.
- 若作者确认来自本论文Chapter6, 以下英文可以用:

> The spectra used as worked examples in this chapter were calculated as part of
> the beryllene study presented in Chapter 6. They are included here solely to
> illustrate the conversion from the dielectric response to derived optical
> quantities. The structural models, computational settings, and physical
> interpretation are given in Sections [verified cross-references].

该模板含待填项, 不可未经核实把同一数据集/计算参数宣称已确认. 若来自已发表文献,
应改为`Reproduced/Adapted from...`并指明变更; 若重新计算, 应区别结构来源和光谱来
源.

- 额外目视发现: p101 Fig3.2吸收系数y轴和caption没有单位, 应从作图代码确认单位后
  补, 不臆造cm^-1或nm^-1; 厚度归一化须跟第6章一致.
- 额外术语问题: line876把张量方向描述成`propagation direction`. 应核实
  in-plane/out-of-plane实际上指电场偏振/ε分量; 明确波矢, 入射方向和偏振, 不能混
  用.

#### 6. 作者贡献, 出版状态与可复现记录

- 列表已有题录和作者姓名; 缺的是"谁提出问题/建模/跑计算/做EPC和拓扑/写代码/作图/
  解释/写稿" 的真实归属. 按章给出具体任务; 共同完成的任务如实写共同, 不能因为是第
  一作者就推断"全部计算独立完成".
- 英文模板仅供作者填真实事实:

> This chapter is based on [full publication reference and verified publication
> status]. Lu Niu contributed to [verified research tasks] and prepared
> [verified text, code, figures, or analyses]. [Co-author names] contributed to
> [verified tasks]. The thesis version additionally includes [verified additions
> or revisions]. All contribution statements have been checked against the
> actual division of work.

- Chapter5 `publications.tex:26`写accepted, Chapter6 line33写will be submitted
  soon; examiner1称preparing, examiner2称submitted. 不能从报告推断当前状态, 应按
  编辑接受函/投稿记录/期刊页面更新到同一截止日期. 公共可验证状态可查DOI, 但第6章
  投稿属作者记录.
- 当前`appendix.tex:6–38`已有GitHub代码/分析仓库和vmatplot说明, 是很好的复现入口;
  可补固定release/tag/commit, 每幅关键图→原始输出→notebook映射, 软件版本和最小
  环境说明. 仅提供仓库链接不等于全部计算输入或raw data均已存档, 应以实际文件核实
  后再写.
- `ai.tex:5–8`当前描述仅为language/LaTeX assistance. 若作者采用本次实质分析形成
  新文本, 最终声明宜忠实反映实际采用方式; 本次只写建议, 未修改其声明或提出未经核
  实的学校规则.

#### 7. Chapter7: 从结果重复升级为证据分层的综合判断

##### 新结构建议

1. `Answers to the Research Questions`: 按RQ1–3各一段, 主要变化, 证据, 适用结构,
   不重复每条峰值.
2. `Original Contributions and Relationship to Prior Work`: 第4章mapping, 第5章
   新2D/H结构相关发现, 第6章新trilayer proposal及需核验的拓扑; 与已知bulk/αβ的复
   算分开.
3. `Limitations and Scope of the Predictions`: 明确影响哪类结论, 而非通用"DFT有
   局限".
4. `Priorities for Further Work`: 由最重要未决点导出可验证步骤.

##### 需要具体写出的限制与对策

- 交换关联/激发近似: PBE/HSE06方法不统一会影响跨章定量比较; hybrid也非exact,
  independent-particle optics不含显式e–h excitons. 对策是先选代表性半导体做
  functional/quasiparticle/exciton benchmark, 量化gap, absorption onset, peak
  shifts和ordering是否改变; 不要直接预测GW/BSE必然改善所有金属谱.
- 二维光学定义: 周期supercell真空, effective layer thickness, intraband/Drude和
  broadening影响幅度/低能谱. 优先检验sheet response或统一归一化, vacuum
  convergence; 只有排除这些因素后才比较"更强吸收".
- 稳定性/合成: cohesive energy相对选择参考, harmonic phonons, 有限AIMD各回答不同
  问题. 未来进一步相竞争/氢化学势/基底/动力学分析能改变的是"哪些条件有利于目标相",
  不是凭更长AIMD保证可合成.
- magnetism: 微小AFM/FM差对数值收敛/磁构型/泛函敏感; 若未求磁各向异性和有限温涨
  落, 只能报告0K候选有序态, 不给未经计算的室温器件承诺.
- superconductivity: 预测Tc依赖mu*, phonons, EPC网格和ME假设; 二维phase
  fluctuations/环境可能影响实际transition. 未来mu*与数值敏感性分析给出范围和误差,
  不以24.3K当已测温度.
- topology: 必须先给第6章metallic系统具体band-manifold证据; parity数值不自动等于
  全局insulating gap或可见受保护边缘输运. 未来dense-k gap/Wilson loop/edge谱各补
  的是不同证据; 如无法满足条件, 收窄当前结论优先于列为未来工作.
- 实验对应: graphene/部分borophene/BC3/beryllene已有文献实验背景; 本论文具体
  free-standing configurations, o-B14系列, cubic trilayer及H化结构的性质仍须标识
  "此前理论结构/本论文新预测/已有实验相对应程度". 不要笼统写"本论文所有材料已合
  成", 也不要写"beryllene完全尚未实验发现".

##### 已有 future work如何变成行动

`conclusion.tex:71–79`已列Raman, transport, optical, EELS, edge probes以及
many-body/strain/doping/substrates等. 建议缩为4–6条, 每条采用"当前不确定性→下一
步→可判断的变化":

1. 低能金属光谱: 核查intraband和2D归一化, 必要时计算有限q响应; 看候选loss峰是否
   保持, 色散和阻尼是否支持plasmon解释.
2. 氢化半导体吸收: 代表性HSE06/GW/BSE对照, 判定光学起始和峰强度的可靠区间.
3. 小磁能差与超导: 收敛/泛函及mu*敏感性, 把单点预测转成可信范围; 不要无差别为所
   有体系增算所有高成本方法.
4. 结构可实现性: 相竞争, H覆盖/化学势, 基底与kinetics, 筛选可能的实验条件与优先
   候选.
5. 拓扑: 先补当前claim必需证据, 再在有明确能带窗口的体系上选择edge
   spectroscopy/transport作为未来实验; 不宜把解决当前Z2有效性留待将来.
6. 实验光谱辨识: 选足够显著且对理论近似稳健的Raman/absorption/EELS指纹, 说明其区
   分哪两种候选结构, 不只说"未来可做spectroscopy".

可用的英文 limitation paragraph(在各科学细项核实后采用):

> The results are predictions for the structural models and computational
> conditions examined in this thesis. Harmonic phonons and finite-duration
> molecular-dynamics trajectories test local dynamical stability and short-time
> thermal persistence; they do not establish thermodynamic stability against all
> competing phases or experimental synthesizability. The calculated optical
> response is also sensitive to the electronic-structure approximation, the
> treatment of intraband transitions, and the representation of an isolated
> two-dimensional layer. Consequently, robust comparative trends should be
> distinguished from absolute spectral intensities and transition temperatures.
> The magnetic, superconducting, and topological conclusions require the
> additional qualifications discussed for their respective systems.

##### 全文同步点

科学判据修正后再统一`abstract.tex:17–19,26–29,34–41`,
`introduction.tex:54,65–73`, `conclusion.tex:28–33,42–46,54–64,68–82`. 这几处目
前都把plasmon, possibly chiral, 稳定性, 非平庸topology写得较肯定; 不能只改结果章
却保留摘要/结论的强断言.`practical routes`可以改为
`computationally examined routes`或更具体的`structural modifications`, 避免把预
测直接等同可实施器件路线.

#### 8. 全篇结构修订的验收检查

- 在Chapter1中, 每个研究章有明确gap, 研究问题, 与前两章的关系, 并有实验/理论身份.
- 在Chapters2–3中, 所有实际使用方法有短工作流, 长推导不再压倒材料研究; 具体数值
  可追溯到各章.
- Fig3.1–3.6中每一幅保留图均有唯一明确的数据出处; 单位, 偏振/传播和2D定义正确.
- 每个多作者章开头能看出publication status和本人贡献; front matter内容一致.
- Conclusion区分新结构预测, 已知结构的进一步characterization和验证范围, 列出具体
  限制与有可判断结果的下一步.
- 摘要, 绪论, 结果章, 结论的科学措辞一致; 不能用文字修补代替当前关键claim必需的
  核验.

### 第 4 章 图表修订与光学结论核查

#### C4.1 准确界定本章贡献

对应评审: E1 第 4 章意见; E2 Chapter 4. 优先级 P1.

位置: `src/project_1_main.tex:7–20, 71–80, 703–722`, pp.111, 113, 131; 章首发表/
贡献声明参见前述全篇结构建议.

本章已经有明确的结构与光谱比较, 不需要为了"创新性" 扩张到尚未研究的器件性能. 建议
把贡献写成三个能由结果支持的层面: 统一计算条件下比较 constituent monolayers 与
heterostructures; 说明界面结合和电荷重排如何改变电子态; 比较不同体系及偏振方向的
光学特征. 对于传感, 光探测, 光学活性, 等离激元器件等应用, 应分别区分"研究动机" 和
"本文实际证明的性质".

可用英文候选:

> The contribution of this chapter is a systematic comparison of the electronic
> structure and optical response of graphene-based boron heterostructures within
> a common first-principles framework. The calculations identify
> structure-dependent trends and spectral features that motivate further
> investigation. Device performance, carrier lifetimes and experimental
> feasibility are outside the scope of the present calculations.

验收: 摘要, 引言末段和结论对于本章新增内容的说法一致; 每一项应用判断都能说明当前
有何证据, 尚缺什么.

#### C4.2 图 4.29–4.36 的逐图落实方案

对应评审: E1 图注不自明; E2 印刷可读性. 优先级 P1/P2, 重绘前须完成 C4.3 的科学核
查.

已检查当前 PDF 的 pp.142–145, 即物理页面 170–173. 每页放两幅九面板图, 重复小图例
占用大量空间; 图 4.29, 4.30 图例明显偏小. 单纯把 `width=0.85\textwidth` 改为
`1.0\textwidth` 只能放大约 18%, 不足以根本解决.

- 4.29, p.142: Graphene–Borophene dielectric tensor; `project_1_SI.tex:267–272`,
  label `S1.17`, 图源 `figures_proj1/S1.17_alt.pdf`.
- 4.30, p.142: Graphene–BC3 dielectric tensor; 同文件 `274–279`, label `S1.18`,
  图源 `S1.18.pdf`.
- 4.31, p.143: Graphene–B4C3 dielectric tensor; `281–286`, label `S1.19`, 图源
  `S1.19.pdf`.
- 4.32, p.143: absorption coefficient; `288–293`, label `S1.20`. 补吸收系数单位,
  先通过 C4.3 和 C4.4 的公式/单位核查.
- 4.33, p.144: energy-loss spectrum; `295–300`, label `S1.21`. 优先复核非对角面
  板的定义和异常尖峰.
- 4.34, p.144: refractive index; `302–307`, label `S1.22`. 明确所用偏振/本征模式
  及有效介质假设.
- 4.35, p.145: reflectivity; `309–314`, label `S1.23`, 图源 `S1.23_correct.pdf`.
  明确界面, 传播方向, 入射条件; 非对角面板需先判断是否有物理定义.
- 4.36, p.145: extinction coefficient; `316–321`, label `S1.24`, 图源
  `S1.24_correct.pdf`. 定义无量纲消光系数与所用模式.

当前还有一项图文不一致: `project_1_SI.tex:263–265` 称图 4.32–4.36 同时给出 PBE
和 HSE06; 实际五幅图内标题均为 "by HSE06", 图例主要区别三个体系. 应核实实际数据
后选择: 若仅有 HSE06, 就改引导文字和图注; 若确实要比较 PBE/HSE06, 另加明确分开的
面板, 不要把不存在的曲线写进图注.

建议采取以下重绘方式:

1. 图 4.29–4.31 将主要对角响应放在较大的 1×3 或 3×1 面板; 经核实有意义的非对角分
   量另图展示. 不能为了缩短图而隐去反例或数值问题.
2. 图 4.32–4.36 按明确的物理偏振或本征模式呈现; 经确认不成立的逐元素"光学量" 应重
   新计算或撤下, 并在回复中说明原因.
3. 每幅图只放一个共享图例, 采用颜色与线型双重编码; 写 `17 × 17 × 1 k-point mesh`,
   不要用容易误解的 "17 k-points".
4. 区分 `xx`, `yy`, `zz` 与 "in-plane". 当前有的第一面板标题为 in-plane, 第二面
   板为 yy; 必须说明第一项到底是 xx 还是面内平均. 只有已核实对称性允许时才写
   `xx = yy`.
5. 在最终 A4 页面尺寸检查字体. 建议最小图内字体约 8–10 pt, 主轴标签约 10–12 pt,
   作为实用目标而非学校强制规定. 保留矢量文字和曲线; 不要仅提高位图 DPI.
6. 图注应包含: 体系, (a)(b)... 面板对应, 张量/偏振定义, 泛函, 颜色/线型, 光子能量单
   位, 纵轴单位, 归一化约定, 以及一条经过验证的主要观察.

图 4.29 重绘后可参考的英文图注模板(仅适用于确实按此布局和线型重画的图):

> Real and imaginary parts of the dielectric response of the graphene–borophene
> heterostructure. Panels (a), (b) and (c) show the xx, yy and zz components,
> respectively, with x and y in the sheet plane and z normal to the sheet. Solid
> and dashed curves denote the real and imaginary parts; [colours] distinguish
> PBE and HSE06. The horizontal axis is the photon energy in eV and the relative
> permittivity is dimensionless. The results use [k-point meshes and
> normalisation convention]. The diagonal spectra show a pronounced difference
> between the in-plane and out-of-plane responses.

图 4.32 在单位和模式核实后可用:

> HSE06 absorption coefficients of graphene–BC3, graphene–borophene and
> graphene–B4C3 for the [specified polarisation modes]. Colours identify the
> three heterostructures. Photon energy is given in eV and the absorption
> coefficient in [verified unit]. The spectra are derived from [the stated
> effective dielectric response], using the thickness convention and broadening
> described in Section [X].

验收: 不翻正文也能解读各图; 100% A4 显示和一张实际打印样张中图例可读; 每个图注与
该图实际曲线一致.

#### C4.3 非对角分量不能直接逐元素套用标量光学公式

本次补充发现, 非 examiner 原文的独立指控. 优先级 P0 核查.

证据: 图 4.33 的 xy/yz 等面板出现约 `10^19–10^20` 的正负尖峰; 图 4.35 中
Graphene–Borophene 的多个非对角面板反射率近 1, 而其介电非对角分量在图 4.29 中近
零. 仓库 `vmatplot/linear_optical_properties.py:33–57, 286–305` 对选定的每个分量
应用标量吸收, 折射率, 反射率, 损失函数公式. 这证明代码路径有需核查的问题, 但本次
没有建立该代码版本与每张成稿图之间的完整运行记录, 不能据此宣布全部论文数值错误.

对于标量响应或适当的主轴/本征模式, `L = -Im(1/ε)` 有明确含义; 但一般张量的矩阵逆
`ε^{-1}` 不等于逐元素求倒数 `1/ε_ij`. 同样, 将接近零的 `ε_xy` 代入标量 `n,k` 和
真空界面 Fresnel 公式, 不能得到一般意义的交叉偏振反射率. 零非对角耦合应与没有该
耦合相容, 而不是自动意味着完全反射.

具体措施:

1. 从 OUTCAR/vasprun.xml/vaspout.h5 到数组, 张量坐标系, 绘图脚本逐步追踪一套数据,
   先选 Graphene–Borophene 作为近零非对角项的诊断例子.
2. 写清计算的是哪种纵向/横向响应; 对非对角张量保留其原始响应含义, 计算可测量量时
   使用适合传播方向和边界条件的张量/本征模式方法.
3. 标量近似若只用于已论证的对角主轴, 应明确限定; 删除或重算没有相应物理定义的六
   个非对角派生面板, 不能只把异常峰截掉.
4. 使用 `ε = I` 作为真空极限检查, 此时应得到 `n=1, k=0, R=0, L=0`; 使用对角各向
   异性张量检查方法能否退化为适当的主轴结果; 损耗与能量守恒检查应针对实际可观测
   量, 不能要求每个非对角矩阵元单独非负.
5. 额外检查 `linear_optical_properties.py:298`: 该行对所有分量使用
   `ε_real*r-r+1`. 即使沿用这一线性厚度修正模型, 真空基线也应按指标使用
   Kronecker delta `δ_ij`; 若将对角公式直接用于原本为零的非对角项, 在 `r≠1` 时会
   人为产生 `1-r`. 增加 `ε=I` 且 `r≠1` 的诊断; 该模型对不同响应方向是否适用仍需
   另行核实. 本次未确认成稿图是否使用了这个分支.

VASP 官方文档给出介电响应, 光学电导及 EELS 的响应函数定义, 可作为检查起点:
[Dielectric properties][source-07]. 最终几何下的光学边界问题仍需作者明确推导或引
用对应方法.

#### C4.4 吸收系数中普通频率与角频率的单位核查

本次补充发现. 优先级 P0 溯源, 影响范围尚未确定.

`vmatplot/algorithms.py:149–154` 返回 `f = E/h`;
`linear_optical_properties.py:300–303` 将它传给吸收函数, 而 `:33–35` 使用对应
`α = 2ωκ/c` 的形式.`src/fundamentals_b.tex:825–830` 也写的是 `2ωκ/c`. 这里应统
一 `E=hf=ℏω`: 若传入普通频率 f, 前因子应为 `4πfκ/c`; 若传入角频率 ω, 则为
`2ωκ/c`.

诊断算例(不是论文结果): 令 E=2 eV, κ=0.5, 且 c 使用 nm/s, 则上述普通频率路径给
约 `0.001613 nm^-1`, 角频率公式给约 `0.010135 nm^-1`, 相差 `2π`. 本次只做了公式
复核, 没有修改脚本或论文图.

措施: 先查成稿每组 absorption 图的实际生成脚本与单位换算. 只有确认经过该路径且没
有其他补偿时, 才更正数据和纵轴; 同步检查正文峰值, 图注和跨章比较. 不要对所有吸收
图直接机械乘 `2π`. 代码还有 `hbar` 命名却赋 h 数值的情况, 应以数值和公式为准, 而
非变量名. 此项是独立于 DFT 是否收敛的后处理核查.

#### C4.5 反对称介电张量和光学活性结论

本次补充核查, 关联 E1 对结论范围的要求. 优先级 P0/P1.

位置: `project_1_main.tex:529–542, 586–602, 721–722`; `project_1_SI.tex:252–261`.
当前明确写 `ε_xy = -ε_yx`, 并由 P3 对称性及非对角响应进一步讨论 chiral optical
effects.

建议查清计算是否有磁性, SOC, 外场, 空间色散, 张量是在正交 Cartesian 基还是其他坐
标表示, HDF5 的复数维度和索引是否读取正确. 对于通常的无磁场, 保持时间反演的局域
线性介电响应, 应核查互易性约束; 不能仅以"空间群低" 解释所有反对称分量. P3 的三重
旋转还给张量带来特定约束, 应与实际优化结构和数值容差一起检查.

天然光学活性需要相应的响应量和传播分析, 非零 `ε_xy` 本身不足以证明. 原始方法论文
提供了包含磁偶极, 电四极及能带色散贡献的光学活性处理: [Wang and Yan, Optical
Activity of Solids from First Principles][source-08]. 据此建议将当前结论降为待验
证线索, 或补齐专门计算后再保留.

核查前的英文候选:

> The off-diagonal response requires further assessment of tensor symmetry,
> coordinate conventions and numerical convergence. These results alone do not
> establish natural optical activity; a dedicated calculation of the relevant
> optical-activity response would be required.

#### C4.6 等离激元, 吸收边和二维比较的表述

位置: `project_1_main.tex:547–556, 576–601, 619–649`, pp.125–129.

不要将"ε1 为负" "损失函数有峰" "Dirac-like band 存在" 分别单独写成确认某类长寿命
plasmon 的充分证据. 对候选峰应联合检查损失峰, 相应介电响应的零点/阻尼, 带间跃迁
背景, 并明确 q→0 与有限 q 的范围; 二维超胞归一化及带内响应处理也会影响判断. 不能
只凭谱峰类型保证器件传播长度或寿命.

建议把未经进一步验证的表述改为 `plasmon-related spectral features` 或
`candidate collective excitations`, 并说明缺少有限 q 色散/阻尼验证.
`The absorption threshold corresponds to the first peak` 也宜修改: 吸收起始和第
一主峰不是同一个定义, 应描述实际采用的 onset 判断标准及展宽影响.

第 4 章 `:490` 已承认部分数值是 monolayer–vacuum combined response, 而第 5, 6 章
讨论了有效厚度修正. 跨章比较时不能直接把这几类介电常数, n, R 或吸收强度当作同一
种内禀量. 需给出统一约定, 或明确只比较同一约定下的谱形, 能量和相对趋势.

### 第 5 章 电子态, 稳定性, 磁性与超导

#### C5-1|P0: 统一单层与双层的电子/磁性状态, 不能把不同近似下的结果拼成同一物相

证据. `project_2_main.tex:164–168`(pp.151–152) 规定未另行说明的图均为 PBE;
`:454–467`(Table 5.2, p.158) 把 pristine monolayer 定为 AFM semiconductor,
bilayer 定为 semiconductor; `:541–546`(p.160) 明确 HSE06 AFM 单层有 0.105 eV
gap, NM 单层为 metal; `:599–603`(p.162) 明确 bilayer 的 HSE06 gap 为 0.67 eV,
PBE 为 semimetal; `:707–734`(p.165) 却把除 bilayer 外的系统都按
metallic/intraband 解读. 超导部分 `:619–622`(pp.162–163) 又纳入 monolayer, 因
"semiconducting nature" 排除 bilayer, 未交代 PBE 计算与 HSE06 分类之间的选择.

修改措施.

1. 先从实际计算目录建立每套图的可追溯清单: 结构/几何优化泛函, 性质计算泛函,
   NM/FM/AFM, 磁胞, 总磁矩与局域磁矩, 占据/展宽, 是否含 SOC, 图对应输入输出. 特
   别检查 Figures 5.6, 5.8–5.12 与 SI 中 band/DoS 图.
2. 给 Table 5.2 的 "electronic nature" 明确泛函与磁态; PBE 与 HSE06 性质不同则分
   开列. 不能用一列"semiconductor" 覆盖所有计算状态.
3. 给光学图和 EPW 结果独立说明所研究的 reference state. 若光学确为非磁 PBE 单层,
   就将结果限定为该受约束模型, 而不是 HSE06 AFM ground state 的光学响应.
4. 核查 bilayer 光学到底是否用 HSE06. 若是, 修改默认声明和 caption; 若为 PBE, 就
   解释 semimetal 的实际带重叠, 费米能附近态和低频响应, 不以 HSE06 gap 为该图的
   吸收阈值背书.
5. 若研究结论需要声称 AFM ground state 的 plasmonic response, 才补算一致的 AFM
   光学; 不要为消除文字矛盾盲目把整章重算成某一种泛函. 无法补算时明确限定现有模
   型并同步降级摘要和结论.

可用英文(方括号必须由原始文件确认, 不能原样提交).

> The optical spectra were calculated for the [magnetic state] using
> [functional] at the [geometry] geometry. These spectra therefore describe this
> specified electronic reference state. The antiferromagnetic semiconductor
> identified with HSE06 is a separate prediction and should not be assigned the
> metallic optical response without a corresponding calculation.

验收. 对每种结构能回答"这个 gap, 这个 spectrum, 这个 superconducting result 是
否来自同一状态"; 所有图注和正文不再出现无条件的 monolayer metallic / monolayer
semiconductor 并存.

#### C5-2|P0: 明确 intraband/Drude 实际处理, 低频尖峰不能自行证明已含自由载流子响应

证据. `project_2_main.tex:257–268`(p.153) 只给光学 k 网格和 NBANDS; `:173` 给
Gaussian 0.1 eV, 但没有说明实际光学的 CSHIFT, 是否 Drude, 其阻尼和等离子体频率;
`:707–708`(p.165) 直接把低能峰归为 intraband absorption.

修改措施. 查 `INCAR`, `OUTCAR`/`vasprun.xml`, 代码版本及后处理脚本, 确认真实的
光学计算开关和谱构造过程. 现代 VASP 的 `WPLASMAI` 默认 0, 正值可在 `LOPTICS` 中
加入 Drude 项; 因此既不能仅凭 `LOPTICS` 断言"有 intraband", 也不能笼统说"VASP 永
远不支持 intraband". 若未加带内项, 明确谱为已实施近似下的 interband response, 删
除低频自由电子归因, 并重新审核 plasmon 能量和低频金属性结论; 若加了, 补等离子频
率张量来源, 阻尼参数, 单位, 是否方向相关, 加入步骤和阻尼敏感性. 将光谱展宽与物理
散射时间区分开. NBANDS=128 是总能带数, 不等于对每一种电子数/原子数系统都包含相同
数目的 unoccupied bands, 也不能只用 bulk 收敛图证明所有层状系统光谱收敛.

英文模板(选择与真实计算一致的一种).

> The dielectric response reported here contains interband transitions only; no
> Drude contribution was added. Accordingly, the low-energy features are not
> interpreted as evidence of intraband absorption, and the metallic response in
> the zero-frequency limit is not resolved by the present calculation.

或:

> The metallic dielectric response combines the calculated interband
> contribution with an intraband Drude term. The plasma-frequency tensor was
> obtained from [verified procedure], and the damping parameter was [verified
> value and unit].

验收. 方法, 脚本, 图注三者一致; 不再用 finite broadening 引起的尾部直接证明
metallic Drude absorption.

官方依据. [VASP LOPTICS][source-09] 给出响应与展宽定义; [VASP
WPLASMAI][source-10] 明确 Drude 开关和默认值. 文档是当前版本说明, 原计算仍须按其
实际 VASP 版本核对.

#### C5-3|P0: 修复虚频矛盾, 并把 harmonic phonons 与短时间 AIMD 分开

证据. `project_2_main.tex:490–509`(p.159) 写 H-terminated bilayer 没有
imaginary frequencies, 400 K AIMD 证明 "thermodynamically stable";
`project_2_SI.tex:135–138`(Figure 5.21, p.175) 却明确其 Γ 附近有 small negative
frequencies. 已视觉核对 p.175, 该负支实际显示在图中. 两者不能同时保留.

修改措施.

- 正文先忠实描述所示数据: 明确哪些结构没有观察到虚频; H-bilayer 的负频出现在哪个
  分支, 哪个 q 区域, 最低频率多大. 数值从数据文件提取, 不从缩小图猜.
- 针对小负频依次检查残余力/应力, 超胞尺寸, k 采样, 位移幅度, 力精度, 以及平移/旋
  转不变性和声学和规则处理; 比较有限位移与 QE/DFPT 的对应结构和磁态. 只有经检查
  支持后, 才归因于数值误差/长波 flexural branch 处理.
- 若负支在合理收敛后持续存在, 跟随软模扰动并重新弛豫, 或把 harmonic stability 写
  成 unresolved/conditional; 不能仅凭"2D 常见" 或 AIMD 未解体就宣布消除不稳定.
- 如果声子不稳定涉及用于 EPW 的低频模式, 必须说明在 α²F/λ 中如何处理这些模式并证
  明结果不由任意截断主导. 不能无说明删除虚频后仍给出精确 Tc.

英文(在尚未确认负频来源时可直接使用的保守版本).

> Small imaginary frequencies remain near Γ for the hydrogen-terminated bilayer
> in the present harmonic calculation. Their origin requires further convergence
> and force-constant checks; the short AIMD trajectory does not by itself
> resolve this long-wavelength stability question.

验收. Figure 5.21, 主文, 摘要中的稳定性定性完全一致; 数值性归因有检查证据, 否则
明确保留局限.

原始研究依据. [Lin, Poncé and Marzari, npj Computational Materials 8, 236
(2022)][source-11] 说明二维弯曲声学支对旋转不变性和平衡应力条件敏感; 这提供检查
路径, 不能替代本体系的数值验证.

#### C5-4|P0: AIMD 图内体系名称与图注冲突; 先核对数据来源, 再改稳定性表述

新增的实际 PDF 发现. p.176(文件第 204 页)Figure 5.22 图内标题为 "AIMD
simulation for bulk o-B14", caption 却为 "hydrogen-terminated bilayer at 400 K".
已渲染, 视觉确认. 源引用为 `project_2_SI.tex:144–149`, 实际曲线 PDF 为
`figures_proj2/S2.10/S2.10a_long.pdf`. 右侧结构示意有氢端基不证明左侧轨迹也来自
该体系.

修改措施.

1. 对照生成图的脚本与 `POSCAR/CONTCAR`, `XDATCAR`, `OUTCAR`, 核对原子数, 元素组
   成, 胞形, 轨迹文件和曲线. 若只是标题模板遗留, 改标题; 若轨迹取错, 重做对应图
   并撤回错误证据.
2. 补 ensemble, thermostat 及参数, 时间步长, 总步数/总时长, 热化区间, 生产区间,
   超胞与原子数, k 网格, 电子收敛/截断能, 固定或变化晶胞. 已知 400 K; 图和
   examiner 指向约 5.5 ps, 但精确时长应由日志确定. 不要根据惯例填 1 fs, NVT 或
   Nosé–Hoover.
3. 把 `main:508` 的 thermodynamically stable 改为 "retained structural integrity
   over the simulated time window". 若有轨迹数据, 报告键长/配位, 层间距和能量温
   度的时间变化, 明确是否存在可见重构; 更长轨迹/多初态可增加证据, 但仍不能证明平
   衡热力学稳定或可合成性.

英文模板.

> At 400 K, the hydrogen-terminated bilayer retained its structural integrity
> during the [verified duration] AIMD trajectory under the specified simulation
> conditions. This supports short-time thermal persistence of the simulated
> structure, but does not establish thermodynamic stability, long-term
> durability, or experimental synthesizability.

验收. 图内标题, 图注, 轨迹物种/原子数一致; 所有实际 MD 参数可追溯; 不再将短轨迹
等同于 thermodynamic stability.

#### C5-5|P0/P1: 20 meV 的 AFM–FM 比较要能复现; 物理机制与有限温度磁序需适度限定

证据. `project_2_main.tex:541–558`(pp.160–161) 给 0.02 eV, 0.105 eV gap, 0.262
μB/apical atom 与 2 μB/cell, 但 0.02 eV 没有归一单位/磁胞说明.`:581–586`(p.161)
直接把 AFM 优势归因于 virtual hopping/Pauli/superexchange 风格解释, 没有本体系
交换参数或模型证据.`project_2_SI.tex:193–205`(pp.178–179) 固定总自旋曲线为
PBE+D3 和 r²SCAN, 而 AFM/FM DoS 为 HSE06; 这些比较不能默认为同一计算.

修改措施.

- 定义 ΔE=E_FM−E_AFM, 并明确 +20 meV per [实际 cell], 每胞 B 原子数, 对应每 B 数
  值, 同几何还是各自弛豫, 泛函, k 网格, 能量选择和占据展宽.
- 给 FM/AFM 原子自旋排列图, 报告局域磁矩定义与最终收敛状态. 总磁矩为零不足以证明
  AFM, 必须有相反的局域自旋密度.
- 收敛 ΔE 本身, 目标数值误差显著小于 20 meV/所用胞; 电子 SCF 阈值 10^-6 eV 不是
  跨 k 网格/展宽/几何的总不确定度. 检查不同初始磁矩, 至少论文实际比较过的磁序,
  避免未测试的 ground-state 泛化.
- 如果没有交换参数或能量映射, 改为 "lowest in energy among the magnetic
  configurations tested", 将 hopping 机制明确称为定性可能解释或删去. 不要以
  ΔE/k_B 直接给 Néel temperature, 也不要把 0 K 自旋极化 DFT 结果等同于室温长程磁
  序.

英文模板.

> Among the spin configurations examined, the AFM state has the lowest HSE06
> total energy, with E_FM−E_AFM = 20 meV per [verified magnetic cell]. This
> small energy separation requires convergence of relative magnetic energies and
> does not, by itself, determine the finite-temperature ordering temperature.

验收. 可从两份输出及相同归一方式得到 ΔE; 图表明确 PBE/r²SCAN/HSE06 各自用途; 不
再以未经验证的机制充当计算事实.

#### C5-6|P1, 若无法追溯数值则 P0: 补成可复现的 DFPT → Wannier → EPW → Tc 路线

现有信息, 不应重复说"全缺". `project_2_main.tex:230–255`(p.153) 已有 QE/PBE,
norm-conserving pseudo, 45 Ry, 15 Å vacuum, 各体系 SCF k 网格与 phonon q 网格,
力阈值, Wannier B s/p 初始投影, 若干 k 网格以及 μ*=0.13. 欠缺的是角色区分, 关键
输入, 收敛证据和中间输出.`:630–654`(p.163) 已经给 bulk λ=0.931 / Tc_AD=28.2 K
/ Tc_ME=31.3 K, H-bilayer λ=1.01 / Tc_AD=18.5 K / Tc_ME=24.3 K, 单层 λ=0.05. 摘
要只报 24.3 K, 要明确是 anisotropic ME prediction.

推荐补写结构.

1. Ground state. 说明 QE 与 VASP 的几何/磁态转换, 赝势文件名/来源/版本, cutoff
   convergence, 金属占据与 smearing. 既有 lattice-constant 接近只支持几何一致性,
   不能替代电子/声子/EPW 收敛.
2. DFPT. 从自洽态计算动力学矩阵, ω_qν, 本征位移和自洽势的一阶扰动, 得到
   g_mnν(k, q); 指明 coarse k/q, phonon threshold 与声学和规则处理.
3. Wannier90. 给总 Wannier 数, num_bands, disentanglement 与 frozen windows, 投
   影; H-terminated 体系是否纳入 H 轨道不能凭推测补写, 需检查实际文件. 比较
   Wannier interpolation 与直接 DFT bands, 尤其 E_F 附近.
4. EPW. 明确原文 6×8×6, 6×6×1 究竟是 coarse input 还是 fine integration grid.
   补实际 fine k/q, Fermi window, δ 函数展宽, μ*, 频率积分与 Matsubara cutoff/温
   度步长, 收敛阈值及程序版本; 附适当 fine-grid/smearing convergence.
5. Outputs. 展示 α²F(ω), cumulative λ(ω), ω_log 和必要的 phonon-resolved
   contribution. 给出 λ=2∫α²F(ω)/ω dω 和 lnω_log=(2/λ)∫[α²F(ω)/ω]lnω dω, 注明频
   率/能量单位和实现一致性. 用原始输出填写 ω_log, 不能由 Tc 反推后当作计算输出.
6. Tc. 清楚区分所使用的 McMillan–Allen–Dynes 近似表达式(是否含 f1/f2 修正) 与
   anisotropic Migdal–Eliashberg 解. Figure 5.9 要说明 gap 是最低 Matsubara 频率
   值, 实轴值或其他量, 曲线/分布代表什么, Tc 如何由数值求解提取. 报告
   0.10/0.13/0.16 的 μ* 敏感性只有真实计算/重评估后才能填结果; 不要编造区间.

必须避免的推论. `main:637` 以 λ 较大解释 phonon softening 再解释 Tc 较低, 缺少
ω_log/α²F 支持. 先比较真实谱权重与 ω_log, 再讲机制.`main:655–656` 把结果归纳为
20–30 K, 与 18.5 K 和 31.3 K 不严格吻合, 应直接分方法报值. λ=0.05 与 μ*=0.13 处
在极弱耦合/库仑竞争情形, 不能不检查适用性就把经验 Tc 公式机械代入; 核对原 EPW
"negligible Tc" 的依据, 并将结论限定为已计算参考态内没有可观的常规声子配对, 不能
排除其他机制或磁态.

英文流程模板(只能在实际流程确认后采用).

> Density-functional perturbation theory was used to obtain the phonon dynamical
> matrices and first-order changes in the self-consistent potential on the
> coarse q grid. Together with the Kohn–Sham states, these quantities define the
> electron–phonon matrix elements. Wannier interpolation was then used in EPW to
> evaluate the matrix elements on the specified dense k and q grids. The
> resulting Eliashberg spectral function was integrated to obtain λ and ω_log.
> Transition temperatures were estimated using the stated Allen–Dynes expression
> and independently determined from the temperature-dependent solution of the
> anisotropic Migdal–Eliashberg equations.

验收. 一个同行拿到方法, 输入文件和 α²F 数据能重建 λ, ω_log 与两个 Tc; 表/图/摘
要均写方法名称, 24.3 K 始终写 prediction. 原始研究并未进行相位涨落/实验检验时,
不把 ME pairing scale 当作已证实的二维材料实验转变温度.

官方依据. [QE electron–phonon coefficients][source-12] 给 g, α²F, λ, ω_log 的定
义; [EPW theory][source-13] 给 DFPT/Wannier 插值与 ME 关系; [EPW
superconductivity tutorial][source-14] 可用于核对输入输出角色. 当前文档示例不是
作者旧计算的实际参数, 不应照抄示例数值.

#### C5-7|P1: 解释 PBE–HSE06 差别, 区分"更适合该问题" 与"最终真值"

位置. `project_2_main.tex:164–168`, `:599–603`(pp.151–152, 162). 目前一句
"gives more accurate band-gap energies" 没有分析这里从 semimetal 到
semiconductor 的定性变化.

措施. 在 bilayer 能带段加入对比: 带边位点/轨道是否变化, 是否同几何, 同磁态, PBE
带重叠大小和 HSE gap 大小; 用同几何计算尽量区分交换关联效应与结构变化. HSE06 的
screened exchange 能减轻半局域泛函的自相互作用/过度离域问题, 但这不是对本体系
gap 的实验确认; 无 GW/实验时把电子相分类标为 functional-dependent prediction. 无
需为回应这一项强制新增整套 GW/BSE.

英文草稿.

> The change from a semimetallic PBE band structure to a finite HSE06 gap
> demonstrates sensitivity to the exchange–correlation approximation. Screened
> exact exchange can reduce delocalisation errors and alter the relative
> positions of the band edges. The HSE06 result remains an approximate
> generalized-Kohn–Sham prediction and is not an experimental determination of
> the gap.

验收. 不再以 HSE06 标签替代误差讨论; 正文明确其影响的是光学/超导状态选择, 非仅
数字精度.

#### C5-8|P0/P1: 吸附能计量公式, 能量比较及坐标定义需审计

吸附能公式. `project_2_main.tex:182–192`(Eq.5.1, p.152) 写
E_ad=(E_H/B−E_B−E_H)/n_H, 同时定义 E_H 为 H2 中每一个 H 的能量. 若定义确实是
E_H=E_H2/2, 则分子缺 n_H, 应为:

`E_ad = [E_H/B − E_B − (n_H/2) E_H2] / n_H`.

如果作者实际 E_H 指全部吸附氢的参考总能, 必须改定义. 先按 Table 5.2 的 −1.450 与
−1.525 eV/H 回查原始能量/脚本: 只改公式文字可能不够, 不能未经核对认定数值也错.
明示 isolated H 与 1/2 H2 参考并不相同; 负吸附能也不自动证明环境化学稳定.

凝聚能. `:386–388`, `:429–435`, `:815–816`(pp.157–158, 168) 需统一 eV atom^-1.
−6.12 比 −6.16 数值更大, 绝对值更小; 结论应写 "less negative by 0.04 eV per
atom".bilayer 比 bulk 低 0.19 eV/atom 只是在指定方法和所选参考下的 energetic
preference; 复核是否使用相同 PAW, 孤立 B 自旋参考, 泛函和基态能量定义. 相对
α-B12 的 0.232 eV 需写清 per atom 与参考来源, 并与引言中对 β-B 最稳定的说法保持
语境一致, 避免无条件称某个 α 相为唯一 ambient ground state.

坐标与距离. Table 5.1(`:345–350`, p.156)bulk b=4.0479 Å, c=6.2042 Å, 而 Table
5.2(`:469`, p.158) 在 b 列填 6.204 Å.Figure 5.1 显示面内取 bulk a–c 平面; 很可
能是 slab 轴重命名, 但应写出映射和极化轴约定, 而不是让读者猜.`:627`(p.163)
interlayer distance≈4.11 Å 与 Table 5.2 interlayer B–B≈1.645 Å 是不同测量定义,
配示意定义平面间距与跨层键长; 否则显得数据冲突. 核对正文与图中 xx/yy/zz 也用同一
坐标映射.

验收. 公式计量与数据重算一致, 能量均有 per-atom/per-H 归一, a/b/c 与 xx/yy/zz
可无歧义转换.

#### C5-9|P2: 按 examiner 2 要求前移 Figure 5.1, 并用它支撑结构构造方法

当前图块位于 `project_2_main.tex:304–317`, 第一次正文引用在 `:323`, PDF p.155;
方法已在 pp.151–154 介绍各模型. 建议在 introduction 末尾或 methods 开头新增短小
的 "Structural models" 段, 把图块与首次引用一同移到那里; 介绍
bulk→monolayer/bilayer 的切取方向, 哪些键断开, 哪些原胞轴重新定义, 氢覆盖位点及
各结构单胞的 B/H 数. 不要只改变 LaTeX 源码顺序而不确认 float 在编译后的 PDF 真正
前移.

英文引导句.

> Figure 5.1 introduces the parent bulk structure and the monolayer and bilayer
> models considered in this chapter. The slab orientation, in-plane axes and
> unit-cell definitions are specified here so that the structural and
> computational comparisons below use a common reference.

验收. 阅读者在第一次看到 vacuum, 2D k mesh 或 H termination 参数前, 已看到或紧
邻看到结构图; 图注解释面板, 原胞框, 颜色和坐标, 并与正文结构命名统一.

#### 作者需要回取的最小原始资料

- 单层 NM/FM/AFM(PBE/HSE06/r²SCAN) 的结构, INCAR, 最终能量/磁矩输出; 用于 20
  meV 对比的实际磁胞和数值收敛记录.
- 所有 Chapter 5 光谱的输入, 输出, VASP 版本, 生成脚本; Drude 处理及 ε 重归一的
  实际步骤.
- H-bilayer finite-displacement/DFPT force constants, 负频数据和相应几何; 不能以
  低分辨图替代频率数值.
- Figure 5.22 原始 AIMD 轨迹和作图脚本, 尤其核对标题 bulk 与 caption bilayer 的
  冲突.
- QE/PH/Wannier90/EPW 输入输出, 伪势标识, coarse/fine meshes, α²F, ω_log,
  gap-vs-T 数据和 convergence records.
- 氢吸附能的 E_H/B, E_B, E_H2, n_H 及计算脚本; 凝聚能同一参考的计算记录.

这些资料应先用于核对已有结果, 而不是把缺失参数按"常见设置" 补齐. 若原始证据找不到,
就明确当前不可复现的部分并收缩结论.

### 第 6 章 结构来源, 拓扑与光学证据

以下页码均为 `.output/thesis.pdf` 的印刷页码; 该部分 PDF 阅读器页码为印刷页码 +
28. 代码行号指本次只读检查时的源文件. 优先级沿用本文开头的定义. 没有运行新的 DFT,
声子, AIMD, HSE06 或拓扑计算.

本章并非完全没有方法说明: §6.3 已列 cutoff, k 网格与收敛图索引; §6.4.4 已明确
SOC, irvsp 与拓扑计算参数; §6.3 已说明介电函数作二维归一化, SI 也给了六种有效厚
度. 因此答复 examiner 应写"补充可复核细节并限定结论", 不要误写"首次加入 SOC" 或"
首次归一化".

另有一组可核实的证据来自论文 p.205 明列的公开数据仓库 [H-Beryllene_20250718, 固
定提交 f863ab0][source-15]. 以下将其称为"公开归档", 已经只读检查选定的 INCAR,
POSCAR/CONTCAR, OSZICAR, notebook 源码及 `systems_info`, 没有下载/修改整个仓库.
公开归档与当前 PDF 每张图的对应关系仍需作者确认; 它提供可追查的线索, 不能直接代
替最终计算记录.

#### C6-01[P0] 氢吸附能的参考态与公式必须优先核对

定位与证据. `src/project_3_main.tex:174–186`, Eq.6.1, p.185; 表6.1及解释在同文
件393–432行, p.190; 结论947行, p.204. 式子写成 `(E_H/Be - E_Be - E_H)/n_H`, 而紧
邻定义又说 `E_H` 是 H₂ 分子中单个 H 的能量: 按此定义, 分子中少了 `n_H` 因子. 更
实质的问题是[公开归档 systems_info][source-16] 明确将 `E_H=-0.014200286 eV` 标为
孤立氢原子能量. 以其记录的原始总能代入原子 H 参考公式, 分别得到 −3.70269,
−3.45536, −3.55012 eV/H, 与论文 −3.70, −3.46, −3.55 一一对应. 因此, 这不仅是可能
的符号笔误, 亦有强证据显示正文所称 H₂ reference 与数值来源不一致.

措施. 先追踪表6.1生成记录, 明确 H 原子参考计算是否自旋极化, 使用什么 PAW/泛函;
然后选定并统一两种定义之一. 若讨论从分子氢吸附, 应采用

$$
E_{\mathrm{ads}}^{\mathrm{H_2}}=\frac{E(\mathrm{Be}_{n}\mathrm{H}_{m})-E(\mathrm{Be}_{n})-(m/2)E(\mathrm{H}_2)}{m}.
$$

若保留原子 H reference, 则应明确 `E_ads^H=[E(Be_nH_m)-E(Be_n)-mE(H)]/m`, 且不能
据此宣称相对于 H₂ 稳定. 缺少同一设置下 H₂ 总能时, 不得自行给出"校正后的" 吸附能.
核对不同结构是否使用相同 n 个 Be 的 pristine reference, 同样电子精度与边界条件.
即使 molecular-H₂ reference 为负, 也只表示相对于该指定反应的零温电子能有利, 不能
证明比全部 Be–H 竞争相更稳定, 更不能证明可合成; 若不做凸包或化学势分析, 应明确限
制.

验收. 留下总能, n/m, 参考物, 单位, 计算设置与逐行代入结果; 修正公式, 表格, 讨论,
Abstract 和结论中的全部 reference-dependent statements. 条件满足后可用英文:

> The adsorption energy is defined per H atom relative to [isolated atomic
> hydrogen / one half of the total energy of an H₂ molecule]. A negative value
> indicates that adsorption is energetically favourable relative to this
> specified reference reaction; it does not establish stability against all
> competing Be–H phases.

#### C6-02[P0; Examiner 1]metallic cubic trilayer 的 Z₂ 必须说明究竟定义在哪一组能带上

定位. p.192 对应 `project_3_main.tex:444–459` 明说多带穿越 Fermi level;
p.193–195 对应518–631行给出 SOC/parity; 表6.2在p.195; 摘要29–35行和结论957–962行
作强结论.

判断. "金属所以绝不可能有 Z₂" 不准确. 若有一个固定维度的能带子空间, 在全二维 BZ
每个 k 都与更高能带存在有限直接能隙, 即使间接隙为负, 也可讨论该带流形的拓扑; 但
不能因此把实际 Fermi-level 金属称为 quantum spin Hall insulator.Fu–Kane 原文以
Bi/Sb 明确讨论这种情形.[Fu & Kane, PRB 76, 045302, §V.A][source-17]. 当前正文没
有提供这个关键前提.

最低必要措施.

1. 明确 relaxed cell 的 inversion centre, 空间/层群, 所采用坐标系与验证容差; 明
   确 nonmagnetic/time-reversal invariant 的实际计算态. 已有 SOC 设置不能代替
   TRS/反演核验.
2. 给出固定的带数 `N` 或 Kramers 对数, 选择理由, PAW价电子配置, NELECT, 并用全二
   维 BZ采样检查 `Δ_dir(k)=E_(N+1)(k)-E_N(k)`, 报告最小值及位置; 另报
   `Δ_ind=min E_(N+1)-max E_N`. 仅沿 Γ–M–X 路径显示未闭隙不足以证明全 BZ 直接隙;
   接近零隙区域须加密, 数值误差应明显小于所报 SOC gap.
3. 重新导出所有四个二维 TRIM 的 parity, 表中明确一个符号对应一个 Kramers pair.
   现在 α/β/cubic 各列2/4/6个符号, 但没有解释 band window 和计数; 不能凭符号数量
   直接判错, 也不能让读者猜. 三方格 M 或两方格 X/Y 的简化须有对应旋转对称性; 即
   使 X/Y 在总乘积相消, 也应在补表列出实际值及分数倒空间坐标.
4. 审核520 eV, 24×24×1, 15 Å真空的拓扑设置(527–534行) 与600 eV, 40 Å的主计算是
   否使用同一几何结构, 同一 PAW/泛函; 对微小 SOC gap 应给设置敏感性证据.
5. 固定带流形和前提确认后, 建议以 Wilson loop/Wannier charge centres 独立交叉检
   查. 它能交叉验证但不能补救一个并不存在的隔离带流形. 若继续声称具体 edge
   states, 给出 ribbon/edge spectral function, 边界终止与 bulk projected
   continuum; 没有边界计算时改为拓扑预测所暗示的边界性质, 不写已经验证低耗散输运.

验收分支. 若全 BZ direct gap>0且ν=1, 可保留非平庸带流形结论并注明 metallic
Fermi surface; 若直接隙关闭, 不能把现在的 parity product 当作完整
occupied-subspace Z₂, 需改用适合该交叉/对称性的指标, 或将本项降为待验证. 所有分
支要同步摘要, Ch.1, Ch.7. 有证据后可写:

> Although cubic trilayer beryllene is metallic at the Fermi level, the lowest
> [N] spinor bands form an isolated manifold separated from the remaining bands
> by a positive direct gap throughout the two-dimensional Brillouin zone. The
> minimum direct gap is [value] at [k], while the indirect gap is [value]. The
> reported ν = 1 characterises this isolated band manifold and does not
> establish a quantum spin Hall insulating state at the actual Fermi level.

若证据不足可写:

> The parity pattern suggests a possible non-trivial band topology, but a
> well-defined Z₂ classification requires verification of an isolated band
> manifold over the full Brillouin zone. We therefore treat the present
> topological assignment as provisional.

#### C6-03[P1; Examiner 1] 把"新 cubic trilayer" 变为别人可以重建的模型

定位. p.187–188, `project_3_main.tex:255–284`. 现文只给"AB stacking", 相对
lattice change, 试过2/4层与graphene-like结构, 缺初态生成路线, 最终坐标和筛选边界.

可直接追查的证据. [公开 cubic-trilayer POSCAR][source-18] 是3个 Be 的正方晶胞,
外层平面投影同为(0, 0), 中层为(1/2, 1/2). 相应[CONTCAR][source-19] 给
`a=b=2.18374554 Å, c=40 Å`, 分数z坐标约0.13758112, 0.1, 0.06241888; 这是 ABA 三
层注册关系, 不能只写AB而不定义.

措施. 先确认该CONTCAR正是本文结构, 再新增"Construction and screening of
structural models": 说明是否由bcc沿(001) 截层, 使用何种初始格常数与表面终止, 有哪
些1/2/3/4层候选, 是否测试不同面内周期/层移, 离子及面内晶格自由度如何优化. 几何看
起来与bcc(001) 相关, 但真实生成历史不能仅从最终坐标推断后写成事实. 提供最终
CIF/POSCAR, 绝对a/b/层间距/Be–Be键长, N_Be, 对称性及坐标. 说明"cubic" 描述母体/结
构家族; 真空slab的三维超胞不是立方体. 候选排除表记录虚频支, 最大虚频位置, 重构情
况与计算设置. 不宜把有限手动筛选写成全局搜索或全局基态发现.

验收. 一个独立读者可按文字构建相同初态, 找到最终坐标, 复算所述筛选. 英文模板:

> Cubic trilayer beryllene was constructed by [verified construction procedure].
> The relaxed slab contains three Be atoms per in-plane primitive cell and has
> an ABA stacking sequence, with the middle layer shifted by (a/2, b/2) relative
> to the outer layers. The designation "cubic" refers to [verified structural
> origin], whereas the simulation cell is a two-dimensional slab containing
> vacuum. Our search covered [enumerated candidates] and was not an exhaustive
> global structure search.

#### C6-04[P1; Examiner 2 #4] 氢化对象选择可以从已有归档补证, 不能编造"未计算" 或"必然不稳定"

定位. p.188–189, 297–339行. 现文直接保留2H-α, 1H-β, 2H-β, 未交代其它吸附位点,
覆盖度, single-sided α, trilayer H variants.

新线索. 公开归档实际上存在[trilayer氢化几何筛选][source-20] 及对应声子文件; [3.3
notebook][source-21] 列 top, hollow, top-top, hollow-hollow, top-hollow, 并备注
top-hollow转为hex-family. 因此优先恢复已做筛选记录, 而不是先启动庞大新计算. 目录
和notebook注记本身不足以证明每个候选均不稳定.

措施与验收. 建立候选清单: 起始吸附位点, 面数, m_H/n_Be或H/面积, 最终几何, 相同
参考态下能量, 声子判据, 保留/排除理由. 明确"1H/2H" 究竟是每原胞H数还是覆盖面数;
它并非所有phase统一的stoichiometry. 若已有筛选均未通过, 报告"本次测试的候选没有
满足标准", 不得推广"trilayer无法氢化"; 若某部分确实未算, 诚实列为scope
limitation, 不能用三层内部埋藏等直觉代替证据. 英文模板:

> Hydrogenated cubic-trilayer candidates were examined at [verified adsorption
> sites and coverages]. Of the configurations tested, [verified outcomes]. They
> were therefore excluded from the detailed optical comparison under the stated
> selection criteria. This finite search does not rule out other stable
> hydrogenated trilayer configurations.

#### C6-05[P1; Examiner 2 #5, Examiner 1]AIMD可以补齐真实参数, 但应将结论限定为5.5 ps尺度

定位. p.189, 图6.5 p.191, 356–379行; 当前正文只说温度在target range, 能量均值稳
定, 没有ensemble, T, dt, 总时间. 已视觉核查图6.5, 可见横轴到约5500 fs, 温度在300
K附近, 但图像不能独自证明ensemble和dt.

归档证据. [alpha_hh/INCAR][source-22] 与beta_b/beta_bb对应文件一致给
`MDALGO=2, SMASS=0, ISIF=2, TEBEG=TEEND=300, POTIM=0.5 fs, NSW=11000`; 根据[VASP
MDALGO文档][source-23], 这是固定胞的Nosé–Hoover NVT设置. 三个OSZICAR均实际有
11000个MD离子步(不是仅根据NSW推测完成), 对应5.5 ps. 三个KPOINTS均3×3×1; POSCAR
分别25Be+50H, 50Be+25H, 50Be+50H, 与5×5面内超胞一致.

必须核对的差异. 这些AIMD输入使用
`ENCUT=350 eV, EDIFF=1e-5 eV, PREC=Normal, LREAL=Auto`, 不是正文"600 eV for all
calculations"; 2H-α的MD c为26.74452 Å, 另两者40 Å.INCAR首行遗留"Ga2O3 melting
at 3000K" 显然与实际tag不符, 不能把注释当方法. 先确认图6.5对应这些trajectory, 再
在正文方法表把static, optics, SOC与AIMD分开报告. 补初速度/随机种子若有, 平衡段与
采样段, 是否约束原子, 每步电子收敛, 真空设置, 显示的能量是F/E0还是包含thermostat
的扩展能量; NVT下普通体系总能量不应被当作严格守恒量.

验收. 参数由实际输出与日志支撑; 从轨迹统计键长/配位/层厚变化, 阐明5.5 ps内未见
解体或重构即可, 不能据此证明长期, 热力学, 任意温度稳定或可合成. 新trilayer没有展
示AIMD, 应将其结论限于已完成的声子证据; 如加强finite-T claim, 再对trilayer做有针
对性的计算. 条件满足后可写:

> AIMD simulations were performed in the NVT ensemble at 300 K using a
> Nosé–Hoover thermostat, a time step of 0.5 fs, and 11,000 ionic steps (5.5
> ps). [Insert the verified supercell, electronic settings, equilibration
> procedure, and sampling interval.] The trajectories show short-time structural
> persistence under these simulation conditions; they do not establish long-term
> thermodynamic stability or experimental synthesizability.

#### C6-06[P1; Examiner 1] 二维光学归一化已经有, 应公开定义, 厚度约定与可观测量边界

定位. p.186, 201–212行; p.206, `project_3_SI.tex:53–63` 给厚度3.96, 5.85, 6.97,
3.14, 5.52, 5.192 Å. 只给厚度数值及文献引用仍不能重现最终光学谱, 也未说明不同
厚度约定对"增强" 的贡献.

措施. 给出所用复介电张量变换和对应光学近似, 明确Lz是完整超胞长度而非空白区宽度;
列每个d_eff的定义与来源(原子层高度, 采用原子半径/电子密度判据等), 实际Lz. 公
开`systems_info`显示一部分厚度来自分数z差乘40 Å再加外层原子半径, 分数坐标必须转
换为长度; 不同外表面种类(Be/H) 需要一致, 可解释的半径约定. 特别是氢化后有效厚度
较pristine更小, 因此体积归一化的幅度上升不能全部解释为更大电子极化率.

按论文所引[Yang & Gao 的光学响应归一化方法][source-24], 报告
`Re ε_eff=1+(Lz/d_eff)(Re ε_SC−1)`, `Im ε_eff=(Lz/d_eff)Im ε_SC` 的实际适用分量
和响应定义, 并追踪生成图的脚本. 不要机械地认定zz与xx使用同式必错; 该光学论文确实
讨论对面内/面外光学响应的体积缩放, 静态串联电容的inverse-ε形式不能不加区分直接替
换. 应核对计算的局域场处理, 纵向/横向及边界条件.

用至少两到三个Lz重算代表体系, 验证所选择的二维响应趋于一致; 这是响应归一化验证,
不是能量真空收敛的同义词. 优先补充in-plane sheet response, 如在明确SI与
`exp(-iωt)`约定下 `σ_2D,||=-i ε0 ω Lz(ε_SC,||−1)`, 以减少任意有效厚度对跨体系幅
值比较的影响. bulk-like n, α(长度^-1) 和半无限介质Fresnel反射率不能直接作为单层实
际吸收率/反射率; 若继续保留, 应标为规定d_eff下的有效薄膜参数, 若声称实验
absorbance/reflectance, 则用具有厚度, substrate和入射几何的电磁模型. 面内/面外应
指电场极化方向; 自由空间法向入射没有独立纯Ez通道.

验收. 图6.9–6.15每一谱追溯原始ε, Lz, d_eff与公式; 正文"trilayer比bulk吸收更强"
的结论用可比较的量或明确相同模型定义; 不得把厚度约定, 真空稀释与本征电子变化混为
一个效应. 可用英文:

> The reported effective dielectric functions use the explicitly stated
> thickness convention. Their magnitudes therefore depend on this convention,
> whereas the corresponding in-plane sheet response provides a complementary
> measure that is independent of the chosen effective material thickness. The
> derived bulk-like optical constants should not be interpreted as the
> absorbance or reflectance of an isolated atomic sheet without an
> electromagnetic boundary model.

#### C6-07[P1; Examiner 2 #1]PBE-only可论证, 但不应宣称它已给出定量可靠光学能标

定位. p.185的155–172行; p.192的455–459行; p.201–204的光谱和结论. Examiner要求解
释未用HSE06, 不等于强制对每个系统重做全部谱.

最低修改. 说明本章用统一PBE方案比较结构/功能化趋势的实际理由, 交代独立粒子近似,
electron–hole interaction/局域场/准粒子修正等具体是否包括, 区分"经k/NBANDS收敛"
与"exchange-correlation/光学理论足够准确". 不能写"HSE不适用于金属" 或"VASP无法做
HSE光学", [VASP LOPTICS文档][source-09] 明确支持混合泛函. 不能凭"金属占多数" 忽略
2H-α的宽隙绝缘/半导体情形; PBE gap偏小也不是实际gap必然更大的证明, 且optical gap
可受exciton影响.

更有说服力但按资源选择的补算. 首选2H-α的PBE/HSE06能带或关键带隙, 代表性trilayer
的band ordering/SOC gap; 若光学峰绝对位置是中心主张, 再做对应关键transition窗口
的HSE或更高层级检验. 用同一几何隔离泛函影响, 明确是否额外relax; 先做k网格的实际
收敛, 不能直接用未收敛稀疏HSE谱与105×105PBE谱比较. HSE本身不含显式BSE exciton,
不能称最终experimental spectrum. 若不补算, 就把结论限于PBE层级的趋势, 并承认跨章
定量比较的限制.

验收. 一段真实理由, 一段限制; 若有benchmark, 给数值和改变/不改变哪些结论. 英文:

> PBE was used consistently in this chapter to compare structural and
> hydrogenation trends within a common computational framework. The spectra
> should be interpreted as predictions at the stated independent-particle level,
> rather than quantitatively benchmarked excitation energies. In particular, the
> gap and absorption onset of 2H-α-beryllene remain sensitive to the treatment
> of exchange and correlation and electron–hole interactions.

#### C6-08[P1; Examiner 2 #2] 收敛图要变成明确的选择规则, 并修正NBANDS术语

定位. p.185, 158–172行; SI p.205–211, 10–15, 60–63行及图6.16–6.27. 现有一句
"yield accurate results" 未说明允许误差. SI还把66/70/133/140称作unoccupied bands;
但[VASP NBANDS官方定义][source-25] 是总KS/QP轨道数, 不是单纯空带数.

措施. 用原始数据报告每一类代表结构的能量变化(meV/atom), 力/几何变化, 光谱峰位
与谱重积分/谱形变化; 写清选择27×27, 25×25及105×105的依据, k点实际间距或轴向划分,
避免k-point总数和每轴网格混称. 给出每个体系实际输出NBANDS(VASP并行设置可能调
整输入), 占据带/所选空带说明, 最高频率/能量窗口, NEDOS, ISMEAR/SIGMA/CSHIFT, 说
明对金属峰如何评估展宽敏感性. 优先核对raw: 公开所选光学INCAR写NBANDS=128, 而SI写
133/140, 可能是输出自动调整或不同run, 必须用实际OUTCAR确认, 不能擅自认定冲突一定
是错. 能量网格不自动保证光学和微小SOC gap收敛; pristine收敛也不能完全代替H结构.

验收. 正文一小段即可让读者知道"从哪种更密设置相比, 变化多少, 为什么足够"; 阈值
必须从实际数据计算, 不能补写看似合理但未测试的1 meV/atom或0.05 eV. 附图caption列
tested grids和NBANDS, 不让读者猜.

#### C6-09[P1; Examiner 2 #3] 图6.2/6.3色彩和结构标记补成自解释

定位. p.187图6.2, p.188图6.3; 245–253, 286–295行. 已视觉核查: 绿/青蓝都用于Be,
图6.2三层的上下外层为绿, 中层为青蓝; β两层也用绿/青蓝区分层; 图6.3小橙球是H, 另
有紫色cell outline. 现caption没解释颜色, 图内层标题很小.

措施与验收. 核对作图配色后在caption明确颜色只编码层/registry, 不代表不同元素,
价态, 磁矩; 补H颜色, unit-cell边框, Cartesian axes, top/side views, panel (a–i);
最好放内嵌legend. 图中三层使用ABA, caption与正文一致; 单纯"blue/green are Be
atoms" 仍没有解释为什么分两色. 按最终A4打印大小查看内部文字, 必要时移除截图式窗口
标题, 改为更大统一panel标记.

英文caption句子可在核对后用:

> Green and cyan spheres represent Be atoms in different atomic layers; the
> colour distinction indicates layer registry and does not denote different
> chemical species or charge states. Orange spheres represent H atoms, and the
> purple outlines indicate the simulation cells. In the trilayer, the two outer
> Be layers share the same in-plane registry, while the central layer is
> displaced by (a/2, b/2).

#### C6-10[P0/P1补充] 光谱结论, 稳定性和文献存在几个应一并清理的点

- 2H-α"visible absorption enhanced" 与宽隙不协调. 455–459行p.192说PBE间接gap>4
  eV; 861和905–907行p.201–202仍称氢化α大幅增强visible-to-near-UV absorption. 其
  所报主要峰约5–5.5 eV已在UV, 视觉看图6.15主要吸收也在高于可见区处. 应从原始谱定
  义onset/峰位, 检查0.1 eV Lorentzian尾巴是否被当作可见吸收; 在未含激子/声子辅助
  跃迁的独立粒子谱中不能借这些机制事后解释低于gap信号. 相应文字很可能应限定为UV
  增强, 但须从原始数据最终判断.
- 负Re ε或loss peak不单独证明plasmon. 655–680, 763–780, 843–849行的若干归因偏强.
  列ε1过零, 同能量处ε2/阻尼与loss peak对应; 明确是否包含metallic
  intraband/Drude贡献. 公开选定INCAR未见Drude参数, 但后处理可能另加, 故须追踪完
  整代码; [VASP WPLASMAI文档][source-10] 说明现版本可通过Drude项处理intraband, 并
  须报告实际版本/阻尼/等离子频率. 无该贡献时应说明低频金属结论受限; q→0谱也不自
  动证明有特定有限q二维plasmon dispersion. 可改为"loss feature consistent with a
  possible collective excitation" 并说明仍需判据.
- bulk bcc声子结论需针对性复核. 315–320行p.189把bulk hcp和bcc都称dynamically
  stable; [原始Be相变研究][source-26] 报告低压bcc的Γ–N虚频. 应核对本文pressure,
  primitive/conventional-cell转换, 路径, supercell维度(正文只写5×5, bulk第三维
  缺失), 收敛与图6.28, 解释与既有研究的差异. 此项是有依据的复核要求, 不能在未重
  算前直接判本文数据必错.
- 结构稳定性的层级. 相对hcp cohesive energy高0.43 eV/atom, 结合无显著虚频, 只支
  持选定模型下的局域动力学稳定; 不能说thermodynamic ground state.phonon检查应含
  supercell/k mesh/displacement/force accuracy, 声学sum rule/二维低频mode的处理,
  不能任意把虚频删除或笼统称numerical noise.
- 文献需展示争议. Li et al. 2023预测α/β的Tc约9.9/12.6 K, 并讨论topology; 随后
  [Petrov & Milošević的2024 comment预印本][source-06] 质疑其超导gap温度依赖及Tc,
  报告较弱超导. 该arXiv页面未列期刊发表信息, 本次只能按预印本引用. 建议把原文与
  comment并列, 明确第6章没有重做EPC/超导复核; 100–115行及959–962行不能把文献Tc当
  本论文确认的结果. Comment存在并不自动证明原论文所有结论失效.
- 参数溯源. `project_3_main.tex:155–163`说PBE-D3(BJ), 600eV, 0.01eV/Å; [公开
  trilayer几何INCAR][source-27] 的IVDW=12被注释, EDIFFG=-1e-3. 输入差异可能来自版
  本/流程, 须逐图关联实际OUTCAR, 再决定改文字还是补算. 不能为了和草稿一致而改归
  档的历史输入.

本章验收的最低闭环是: 每条examiner意见能指向具体新增段落/表/图; 每个声称的参数能
追溯到实际run; 吸附参考态和拓扑前提核实完毕; 所有结论用词与证据等级一致. 需要补
算的项目应单列"待执行", 不能在rebuttal写成已经完成.

### 执行顺序和最小交付证据

建议用四轮完成, 而不是按页码从第一句开始逐句润色. 下面列出的检查是你后续修改的验
收要求, 本次没有替你执行论文改写或新计算.

#### 第一轮 先固定科学结论和数据身份

- 建一个结果索引: 每幅关键图对应体系, 几何, 磁态, 泛函, 原始输入输出, 作图脚本及
  版本. 优先第 5 章光谱/磁序/超导, 第 6 章拓扑/吸附能/AIMD, 第 4 章派生光学量.
- 审核氢参考态与 n_H 计量; 审核 AFM–FM 能量归一; 审核第 5 章 phonon/AIMD 图身份.
- 对第 6 章 Z2 判据作出明确选择: 已有完整证据可保留; 需补带隙/对称性/拓扑验证;
  或先撤回过强定性. 不能只新增一段普通拓扑科普以代替判据.
- 对第 4 章后处理建立一组最小诊断: 标量真空极限, 对角张量极限, 普通频率/角频率换
  算. 仅在证据确认涉及成稿图后更新相应结果.

本轮产物应是"可保留结论" "需收窄结论" "需重算结果" 三份清单. 这样再写引言和结论, 才
不会反复返工.

#### 第二轮 重建读者路线

- 改 Chapter 1: 明确中央问题, critical review, 三章各自问题与共同控制变量.
- 精简 Chapters 2–3: 保留支撑实际计算的概念, 将长推导移至组织清楚的附录或压缩;
  新增实用方法概览并与各章参数互相引用.
- 给 Chapters 4–6 增加经共同作者确认的具体贡献声明; 明确既有结构, 新构型, 新性质
  预测各属于哪一种贡献.
- 写 Chapter 7 的综合结论, 局限和有判据的未来工作, 再同步更新 Abstract. 特别追踪
  superconductivity, topology, stability, plasmon 和 chiral 等词的证据边界.

#### 第三轮 补齐方法和图表

- 先用真实输入输出补方法. 找不到的参数写入待查清单; 不能凭软件默认值或习惯补成事
  实.
- 完成 Figure 5.1 前移, Figures 6.2–6.3 图例说明, 以及 Chapter 3 例图来源.
- 在科学定义明确后重画 Figures 4.29–4.36, 并普查其他多面板图是否有同类字号问题.
- 将 optically active, in-plane/out-of-plane 与 propagation/polarisation 的使用
  统一; 横轴统一解释 E=ℏω, 量纲和厚度约定写清楚.

#### 第四轮 由最终 PDF 生成回复记录

- 重新编译后核对实际图位, 页码, 引用, 书签与目录. 不能用改动前页码填写回复评审.
- 检查 `undefined reference`, `undefined citation`, 重复 label 和 overfull 内容;
  编译无报错不等于图可读, 仍须按 A4 尺寸检查.
- 每条 reviewer comment 都对应一条实际 change, 具体位置和验证证据. 保留"未新增计
  算" 的真实说明以及相应收窄的结论.
- 对关键数值做全篇一致性检索: 0.105 eV, 0.67 eV, 20 meV, 18.5/24.3/28.2/31.3 K,
  AIMD 温度和时长, 吸附能, Z2. 包括摘要, 章节摘要, 正文, SI, 总结和回复.

### 如何完善已有 reply_to_examiners 草稿

现稿已经是很好的逐条回复骨架, 但存在 `x pages`, `sections x,y`, `pages x,y`,
`Page ?`, `xxxxxxxxxxxxxx` 等占位符, 并提前使用了 `has been modified`. 这次未修
改该文件; 在实际修改完成之前, 应把这些内容视为计划草稿.

推荐每条正式回复使用四部分, 但不必机械写四个小标题: 感谢并准确理解评论; 说清采取
了什么改变; 给出 revised section/page/figure; 对新增验证, 未补算或收窄结论作事实
说明. 不要仅写 "the relevant section has been improved".

通用英文模板, 仅在对应修改实际完成后使用:

> We thank the examiner for this comment. We have revised Section [X] to
> [specific change]. The revised text now distinguishes [relevant distinction]
> and reports [verified methodological detail or evidence]. The changes appear
> on pp. [revised pages], with the corresponding update to Figure/Table [Y].

方法没有补算, 而是补说明并收窄结论时:

> We agree that the original wording exceeded the evidence provided by the
> calculations. We have therefore restricted the conclusion to [the supported
> result] and explicitly stated that [the unverified claim] has not been
> established. No additional [type of calculation] was performed for this
> correction.

处理原文和补充材料不一致时:

> We have checked the source data for [specific result] and corrected the
> inconsistency between the main text and the supplementary discussion. The
> revised description states [verified finding] and clarifies its implications
> for [stability/electronic state/optical response]. The associated figure and
> caption have been updated consistently.

这三个模板都不能直接作为"已经完成" 的回复提交. 特别是新的计算/重绘改变论文结论时,
要说明具体影响范围; 保留学术记录, 不用模糊措辞隐藏实质修订.

另外两份评审对 Chapter 6 的发表状态说法不一致(preparing / submitted), 当前
`src/publications.tex` 又写 will be submitted soon. 正式材料应以作者投稿记录和出
版社信息统一, 不能任选对自己有利的一种. 草稿中的学位结果表述应与本人收到的正式通
知核对, 本次审阅不推断正式裁定.

### 逐条覆盖评审意见的核对清单

以下沿用现有 `reply_to_examiners.md` 的编号方便定位; 原始报告中的部分意见并没有
编号, 正式引用时以原始文字为准. E2 的 Chapter 6 应拆成五个子项, 不要因原草稿的
"6 / 7 / 1–5" 混合编号漏答.

#### Examiner 1

- [ ] 总评中关于候选人贡献及新旧工作的区分 → 结构建议中的发表/贡献声明; Chapter
      1 critical review; C4.1; Chapter 6 结构来源.
- [ ] E1-1 研究定位, gap, 两章过长 → Chapter 1 和 Chapters 2–3 的重组建议.
- [ ] E1-2 三组材料联系, 光学动机, 拓扑意义, 实验与理论区分 → 研究问题, 光学可观
      测量, 方法适用范围; Chapter 7 综合与局限.
- [ ] E1-3 优化, k 点, 声子, AIMD, 磁性, 超导, SOC/拓扑的方法路线 → 实用方法概览;
      C5-5/C5-6; Chapter 6 方法核查.
- [ ] E1-4 第 4 章贡献与 Figures 4.29–4.36 → C4.1/C4.2; 相关科学定义核查见
      C4.3–C4.6.
- [ ] E1-5 第 5 章预测性, 稳定性, AFM–FM, 小负频 → C5-3/C5-4/C5-5/C5-8.
- [ ] E1-6 单层光学状态, intraband, PBE/HSE06, DFPT–EPW 流程 →
      C5-1/C5-2/C5-6/C5-7.
- [ ] E1-7 cubic trilayer 生成与金属 Z2 → Chapter 6 结构构造和拓扑条件.
- [ ] E1-8 结构细节, 二维光学归一化, 稳定性/可合成性 → Chapter 6 相应建议; 跨章
      统一见 C4.6.
- [ ] E1-9 总体清晰度与结论范围 → 完成以上后统一摘要, 引言, 总结, 回复中的最终说
      法.

#### Examiner 2

- [ ] E2-1 专门且全面的 critical literature review, 已有方法与研究 gap → Chapter
      1 文献组织方案及方法比较.
- [ ] E2-2 方法章节 α/β-beryllene 例图来源 → Chapter 3 来源说明; 需一并覆盖 p.93
      的 Figure 3.1.
- [ ] E2-3 Chapter 4 章首发表及作者贡献 → 前置发表列表与章首声明同时完善.
- [ ] E2-4 印刷图可读性, 尤其 4.29/4.30 → C4.2, 最终 PDF 和打印验收.
- [ ] E2-5 Figure 5.1 提前 → C5-9, 验证实际 float 位置.
- [ ] E2-6/7(a) Chapter 6 不使用 HSE06 的理由 → PBE 的用途, 计算范围与限制; 若做
      代表性验证, 只报告真实结果.
- [ ] E2-6/7(b) Chapter 6 收敛过程与 k 网格依据 → 总能与光谱分别报告收敛目标和数
      值变化.
- [ ] E2-6/7(c) Figures 6.2/6.3 绿色, 蓝色 Be 球的意义 → 对实际结构/绘图脚本核对
      后补 legend.
- [ ] E2-6/7(d) trilayer 为什么没纳入氢化最终比较 → 交代实际筛选范围与排除理由;
      不能虚构"没试过" 或"全部不稳定".
- [ ] E2-6/7(e) AIMD ensemble, 温度, 步长, 总时长 → 原始日志, 正文方法与 Figure
      6.5/SI 统一.
- [ ] E2-8 Chapter 7 理论限制, 假设, 预测不确定性, 实验/理论状态 → 综合结论与局
      限段落.
- [ ] E2-9 future work 的具体改进 → 每项工作对应一个未解决问题, 预期改进及判断标
      准.

### 提交前应能回答的六个问题

1. 每个重要结论, 能否指向一组身份明确, 方法清楚的原始数据?
2. 不同泛函, 磁态, 厚度定义和响应近似的结果, 是否被清楚区分?
3. 稳定性, 超导, 拓扑和光学应用的措辞, 是否只覆盖现有证据?
4. 每一条评审评论, 是否已有具体修改及最终页码, 而不是只有"感谢/已改善"?
5. 每幅图脱离正文是否仍能读懂, 并能在论文实际页面尺寸辨认图例和单位?
6. 所有英文候选段落中的占位符是否已删除, 参数和作者贡献是否已由本人核实?

本次建议的目的, 是帮助你自己修改论文并形成可核查的逐条回复. 它不替代原始计算验证,
也不声称已完成上述修订.

### 文献和数据链接

[source-01]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6788864/
[source-02]: https://pubmed.ncbi.nlm.nih.gov/37232187/
[source-03]: https://doi.org/10.1039/D3CP00692A
[source-04]: https://www.nature.com/articles/s41699-023-00415-y
[source-05]: https://www.sciencedirect.com/science/article/pii/S2542529323002936
[source-06]: https://arxiv.org/abs/2407.18254
[source-07]: https://vasp.at/wiki/Category%3ADielectric_properties
[source-08]: https://arxiv.org/abs/2211.09845
[source-09]: https://vasp.at/wiki/LOPTICS
[source-10]: https://vasp.at/wiki/WPLASMAI
[source-11]: https://www.nature.com/articles/s41524-022-00920-6
[source-12]: https://www.quantum-espresso.org/Doc/ph_user_guide/node19.html
[source-13]: https://docs.epw-code.org/Theory.html
[source-14]: https://docs.epw-code.org/tutorials/tutorial_04/index.html
[source-15]:
https://github.com/Photonico/H-Beryllene_20250718/tree/f863ab02ebf93d5804f5552967ea750571778335
[source-16]:
https://github.com/Photonico/H-Beryllene_20250718/blob/f863ab02ebf93d5804f5552967ea750571778335/systems_info
[source-17]: https://arxiv.org/pdf/cond-mat/0611341
[source-18]:
https://github.com/Photonico/H-Beryllene_20250718/blob/f863ab02ebf93d5804f5552967ea750571778335/2.0_geometry_optimization/c3-Beryllene_trilayer/POSCAR
[source-19]:
https://github.com/Photonico/H-Beryllene_20250718/blob/f863ab02ebf93d5804f5552967ea750571778335/2.0_geometry_optimization/c3-Beryllene_trilayer/CONTCAR
[source-20]:
https://github.com/Photonico/H-Beryllene_20250718/tree/f863ab02ebf93d5804f5552967ea750571778335/2.3_geometry_optimization_with_hydrogen_c
[source-21]:
https://github.com/Photonico/H-Beryllene_20250718/blob/f863ab02ebf93d5804f5552967ea750571778335/3.3_phonon_dispersion_with_hydrogen_c.ipynb
[source-22]:
https://github.com/Photonico/H-Beryllene_20250718/blob/f863ab02ebf93d5804f5552967ea750571778335/8.0_AIMD/alpha_hh/INCAR
[source-23]: https://vasp.at/wiki/MDALGO
[source-24]: https://arxiv.org/pdf/2105.14689
[source-25]: https://vasp.at/wiki/NBANDS
[source-26]: https://www.sciencedirect.com/science/article/pii/S0927025613007623
[source-27]:
https://github.com/Photonico/H-Beryllene_20250718/blob/f863ab02ebf93d5804f5552967ea750571778335/2.0_geometry_optimization/c3-Beryllene_trilayer/INCAR
