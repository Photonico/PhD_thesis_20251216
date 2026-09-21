# Kimi via Copilot

## 0919

### 论文修改建议: 基于两份 Examiner Reports 的逐条分析与落实方案

说明: 以下意见综合了两份审查报告.E1 指
report/Lu_Niu_PhD_report_20260824.pdf, E2 指
report/PhD Examination Report - Lu Niu.docx.
每条意见都核对了论文源码(src/ 下的 .tex 文件)中的实际位置,
给出可操作的修改措施. 讲解用中文;
建议写入论文的文字用英文给出骨架.

---

### 〇, 总体形势判断

E1(PDF 报告)的总体评价: substantial original research,
capable of reaching a professional doctoral standard,
但要求 substantial scientific and editorial corrections.
核心诉求有三: 研究定位与研究空白不清晰;
Ch2 与 Ch3 合计约 100 页, 过长且缺乏方法路线图;
多处科学表述需澄清(稳定性, 磁性态, Z2, 超导流程).

E2(DOCX 报告)的总体评价: a good PhD thesis,
appropriate standard for the award, 修改属 readily rectified,
可由 Chair of Examination 审定.
核心诉求: 缺独立的系统性文献综述; 图表质量与来源标注;
Ch6 方法细节缺失; Ch7 缺局限性讨论.

两份报告的共同点: 文献综述到研究空白的逻辑链, 方法章瘦身,
多作者章节的个人贡献声明, 预测性结论的措辞限定.
两者意见没有冲突, 可合并成一份修改清单.
E2 的修改多为点状局部修改; E1 涉及 Ch1 至 Ch3 的结构性重组,
是工作量主体. 建议先搭好全文的故事线(研究空白加章节关联),
再逐章落实.

### 一, 全局性修改(最高优先级)

#### 1.1 研究空白与全文故事线(E1 评论 1, 2; E2 评论 1)

问题: E1 指出 the early literature review does not lead to a
sharp research gap or central motivation, 各结果章节
hopping between different materials and there is a lack of
relationship between them.E2 指出 the absence of a dedicated
and comprehensive literature review.

现状: src/introduction.tex 目前是典型的 broad survey:
石墨烯, Xenes, 硼与铍, 调控手段(异质结, 氢化), DFT, 逐章剧透.
它没有回答三个问题:

- 为什么 graphene-boron 异质结构, 硼同素异形体, beryllene
  属于同一篇论文;
- 每一章针对哪个未解决的科学问题;
- 三个研究合起来支持哪一个统一结论.

措施(改 src/introduction.tex, 这是全文改动量最大的部分):

- 增设独立的 Literature Review 一节.E2 明确要求 a dedicated
  and comprehensive literature review. 建议结构:
- 2D boron 体系的关键已有研究: borophene 各相的实验制备与
  理论预测, o-B14 块体的已知性质, 逐一点明已解决什么,
  留下什么空白;
- 2D beryllium 体系: alpha 与 beta-beryllene 的理论提出,
  Chahal 等人的 sonochemical exfoliation 实验
  (已在 Ch6 引用 chahal2023beryllene, 可前移), 尚缺什么;
- 文献中用过的理论与计算方法及其层级(PBE, HSE06, DFPT,
  EPW, 结构搜索等), 并评价各自在同类体系上的可靠性.
  E2 原话要求 the various theoretical and computational
  approaches that have been employed in the literature,
  including the levels of theory;
- 批判性地区分已实验实现的体系与纯理论预测.E1 明确要求
  separate established experimental systems from
  theoretical proposals.
- 在 Ch1 末尾新增一段 Research gap and thesis statement,
  用三到四句话显式钉死空白. 英文骨架:

> "Despite these advances, three gaps remain: (i) there is no
> systematic map of structure-property relationships across
> graphene-boron heterostructures; (ii) it is unknown whether
> the bonding network of o-B14 can host magnetism and
> phonon-mediated superconductivity under dimensional reduction
> and hydrogen termination; (iii) elemental beryllium has not
> been assessed as a 2D platform combining tunable optical
> response with non-trivial topology. This thesis addresses
> these three gaps with a unified first-principles framework."

- 补写光学性质的动机.E1 指出 absorption, refractive index,
  reflectivity, and loss spectra are often presented as a
  standard set of outputs rather than as observables answering
  defined scientific questions. 在 Ch1 说明每类光学可观测量
  对应什么物理问题: 介电函数虚部对应带间跃迁与吸收边;
  energy-loss spectrum 对应等离激元; 折射率与消光系数对应
  器件相关参数; 并说明光学各向异性为何本身就是科学问题
  (对称性降低, 方向性等离激元).
- 补写拓扑动机.E1 要求 briefly explain why topology is
  important and what physical consequence is expected from a
  non-trivial Z2 invariant, before introducing the parity
  calculation. 半页即可: Z2 非平庸意味着自旋轨道耦合下存在
  受保护的边界态, 对散射鲁棒; 再引出 Fu-Kane 宇称判据作为
  可计算诊断量.
- 逐章剧透段落改写为问题驱动: 把 Ch4, Ch5, Ch6 的介绍段
  写成问句形式(This study asks how ...), 并在结尾用一句话
  说明三章如何递进(composition 到 dimensionality 与
  functionalization 再到 elemental limit), 回应 hopping
  between different materials 的批评.

#### 1.2 Ch2 与 Ch3 瘦身并重组为方法导向(E1 评论 1, 3; E2 评论 2)

问题: E1 指出两章合计约 100 页, do not provide a sufficiently
concise and practical explanation of the computational methods.
需要的是 method-oriented 的实操说明, 并与后续章节的科学问题
显式挂钩.E2 也认为两章是 almost textbook version.

现状: src/fundamentals_a.tex(3152 行)从含时薛定谔方程,
演化算符, 系综一直推到 Hartree 方程;
src/fundamentals_b.tex(1164 行)从 Maxwell 方程推到
Kramers-Kronig 关系. 形式推导占比过大, 而 geometry
optimisation 收敛判据, k 点选取, 声子, AIMD, 磁性计算,
电声耦合, SOC 与拓扑分析这些实际用到的方法反而淹没其中.

措施一: 搬迁, 而非删除. 这与 reply_to_examiners.md 中已拟的
回复策略一致(allocating sections x, y to a new Appendix).
建议迁入附录的内容:

- fundamentals_a.tex 中 A story starts with time evolution
  quantum mechanics 一节(演化算符, 绘景变换, 连续性方程
  推导), grand canonical ensemble, Thomas-Fermi 的大部分
  推导, Hartree 方程;
- fundamentals_b.tex 中 Kramers-Kronig 的解析性推导细节,
  部分静态极限讨论.

附录已有 src/appendix.tex(目前只放代码仓库链接), 可在其前
新增 Appendix A: Detailed Derivations. 正文保留一句交叉引用,
例如 The full derivation is deferred to Appendix A.

措施二: 在 Ch2 或 Ch3 开头新增一节
Computational workflow used in this thesis, 按 E1 点名的清单
逐项给出简明实操卡片(每项半页到一页), 并显式指向使用它的
章节:

- Geometry optimisation and convergence: 力与能量收敛阈值,
  截断能, k 点网格的收敛测试逻辑; 用于 Ch4 至 Ch6;
- Brillouin-zone sampling: 各体系 k 网格及选择依据
  (呼应 E2 对 Ch6 收敛性的要求); 用于 Ch4 至 Ch6;
- Phonon calculations: 有限位移与 DFPT, 虚频与动力学稳定性
  的判据; 用于 Ch5, Ch6;
- AIMD: 系综, 温度, 时间步, 时长的设定原则
  (呼应 Ch5 与 Ch6 的 AIMD 细节缺失); 用于 Ch5, Ch6;
- Spin-polarised calculations and magnetic ordering: FM 与
  AFM 初猜, 能量比较, 磁基态判定; 用于 Ch5;
- Electron-phonon coupling and superconductivity: DFPT 到
  Wannier 插值到 EPW 到 alpha2F(omega), lambda, omega_log
  再到 Allen-Dynes 与各向异性 Migdal-Eliashberg 的流程;
  用于 Ch5;
- SOC and topological analysis: Fu-Kane 宇称乘积判据,
  适用前提(绝缘体或有能隙的占据子空间); 用于 Ch6.

建议配一张流程图(methods roadmap), 一图回应 E1 的
concise roadmap of the computational methods.

措施三: 处理第 100 页起 beryllene 光学示例的来源问题
(E2 评论 2). 现状: fundamentals_b.tex 第 535, 868,
983 至 1010, 1083 至 1095 行展示了 alpha 与 beta-beryllene
的介电函数, 吸收, 折射率, 消光系数, 反射率,
其中第 983, 1083 行挂了 7 篇文献(含你自己的
niu2024electronic), 但没说清数据到底来自哪里.
两种合规做法任选:

- 若是本论文算的: 在每个示例首次出现处加一句, 例如
  The spectra shown here are calculated within the present
  thesis using the methods described above; the full analysis
  is presented in Chapter 6. 并用 \ref 指向 Ch6 对应小节,
  图注里也写明 calculated in this work (cf. Section 6.x);
- 若取自文献: 删去含自己论文的混合引用,
  精确引用数据来源那一篇.

推荐第一种.

#### 1.3 个人贡献声明(E1 总评; E2 评论 3)

问题: Ch4, Ch5 基于多作者已发表论文.E1 要求 the candidate's
individual contribution to the multi-author chapters should be
stated more explicitly; E2 要求 a clear statement at the
beginning of the chapter indicating that the work has been
published and outlining the specific contributions.

现状: src/project_1_main.tex 与 src/project_2_main.tex
章首均无此类声明(已 grep 确认).

措施: 在 Ch4, Ch5, Ch6 章首各加一个不带编号的声明框,
英文骨架:

> "This chapter is based on the publication: [full citation].
> The candidate designed the study, performed all
> first-principles calculations and data analysis, prepared all
> figures, and wrote the initial manuscript. Co-authors
> contributed to [discussion / supervision / revision]."

按实际分工填写.Ch6 若已投稿(submitted), 也照此注明状态.

#### 1.4 预测与实验事实的全文措辞区分(E1 总评, 评论 5, 8; E2 评论 8)

措施: 全文检索并柔化过强的措辞. 建议建立替换规则:

- is stable 改为 is dynamically stable (no imaginary phonon
  modes), 即只声明动力学稳定;
- 涉及可合成性时区分三档: dynamical stability(声子无虚频),
  energetic preference(结合能或形成能相对参考相更低),
  experimental synthesizability(需要实验, 本文不断言);
- 超导, 等离激元等预测性结论统一加 predicted 或 within the
  approximations employed 限定.

在 Ch1 文献综述和 Ch7 结论中各用一个短段落明确列出:
哪些体系已被实验实现(graphene, borophene 某些相,
Chahal 的 beryllene), 哪些是本文的纯理论预测
(o-B14 单层与氢化双层, cubic trilayer beryllene 等).

### 二, Chapter 4(graphene-boron 异质结构)

#### 2.1 图 4.29 至 4.36 图注过短(E1 评论 4)

现状: 核对 src/project_1_main.tex, 现有图注确实多为一句话,
例如第 397 行 \caption{Band structure and total DoS of
Graphene-\ce{BC3}.}, 第 522 行 \caption{In-plane and
out-of-plane dielectric-function components of the
Graphene-Borophene heterostructure.}.

措施: 把光学系列图(介电函数, 吸收, 反射, 折射, 消光,
loss)的图注扩写为自包含格式, 逐一写明 E1 点名的要素:
panels(哪个子图是什么), tensor components
(εxx, εzz, εxy), line styles(PBE 蓝与 HSE06 橙),
polarisation directions(in-plane 与 out-of-plane), units,
principal feature(主峰位置与物理含义一句话). 模板:

> "In-plane (solid) and out-of-plane (dashed) components of
> the complex dielectric function of Graphene-Borophene,
> calculated with PBE (blue) and HSE06 (orange). Panel (a):
> real part; panel (b): imaginary part. The principal
> absorption feature at about x eV arises from ..."

#### 2.2 图的印刷清晰度(E2 评论 4)

措施:

- 重点重做 Figs 4.29 与 4.30(图例 largely illegible):
  增大字号(图内文字等效不小于 8 pt), 放大子图面板;
  多面板图超过 4 个面板时拆成两幅图;
- 项目里的图已是 PDF 矢量图, 问题在于字号与面板尺寸.
  重出图时把 matplotlib 的 fontsize 上调,
  你的 vmatplot 里应有全局设置;
- 自检标准: 论文 PDF 以 100% 缩放打印预览,
  图例不借助原文即可辨认.

#### 2.3 章首贡献声明

见 1.3 节.E2 对 Ch4 单独点名, 务必加.

### 三, Chapter 5(o-B14 体系)

#### 3.1 Figure 5.1 提前(E2 评论 5)

措施: 在 Ch5 的 methodology 或 introduction 小节首次讨论
计算模型之前就 \ref 并展示 fig: ob14_atomic_structure,
把叙事顺序固定为结构先行: 结构, 方法, 结果.
若 LaTeX 浮动体位置不听话, 用 \FloatBarrier 锁定
(已加载 placeins 宏包).

#### 3.2 稳定性声明的限定(E1 评论 5)

措施: 在 Ch5 稳定性小节开头加一个判据声明段落, 英文骨架:

> "Three distinct levels of stability are considered in this
> chapter: energetic preference relative to selected reference
> phases (cohesive energy), dynamical stability (absence of
> imaginary phonon modes), and short-time thermal persistence
> (AIMD at 300 K for 5.5 ps). These criteria do not by
> themselves establish thermodynamic stability or
> synthesizability, which would require e.g. convex-hull
> analysis and experimental synthesis."

同时把 5.5 ps AIMD 明确称为 short-time thermal persistence,
避免暗示长时热稳定.

#### 3.3 AFM 与 FM 能量差和虚频表述矛盾(E1 评论 5)

现状: 已在源码中定位到矛盾处.src/project_2_main.tex
第 496 行写 No imaginary frequencies are present;
第 502 行写 This is reflected by the presence of imaginary
frequencies for the latter. 两处相隔 6 行, 方向相反.

措施:

- 核对声子计算结果后统一表述: 到底是哪个相
  (bulk, monolayer, bilayer, 氢化)有虚频, 哪个没有,
  逐相写清;
- 对 AFM 与 FM 的小能量差, 补一句数量级说明与不确定性
  讨论, 例如 The AFM-FM energy difference is x meV per atom,
  comparable to the numerical accuracy of the calculation;
  the AFM assignment should therefore be regarded as
  tentative. 并说明为何仍采纳 AFM 态作为后续计算基础.

#### 3.4 单层电子态与磁态矛盾, 光学计算的 intraband 处理(E1 评论 6)

现状: 第 457 行表格把 monolayer 标为 antiferromagnetic
semiconductor; 第 544 行写 A small band gap of 0.105 eV opens
in the antiferromagnetic case; 第 546 行写 the system is
metallic(指 FM 情形); 而第 708 行光学讨论出现 a large
value at low energies due to intraband absorption from free
electrons.E1 的质疑成立: 半导体态不该有自由电子的
intraband 吸收.

措施:

- 在光学小节开头显式声明所用的电子与磁态, 例如 The optical
  calculations for the monolayer were performed for the
  [AFM ground state / non-spin-polarised metallic state],
  because ...;
- 若光学确实用了金属性(非自旋极化或 FM)态, 说明
  intraband 或 Drude 项如何加入, 用了什么展宽参数,
  并讨论该选择与 AFM 基态之间的张力
  (例如带隙 0.105 eV 很小, 室温下表现接近金属, 需论证);
- 若两处文字只是笔误(把 FM 金属性写成了 monolayer 的
  性质), 则直接修正归属.

#### 3.5 PBE 与 HSE06 差异的解释(E1 评论 6)

措施: 在首次对比 PBE 与 HSE06 处加一段方法论解释,
英文骨架:

> "HSE06 opens a larger gap than PBE by partially correcting
> the self-interaction and delocalisation errors inherent in
> semilocal functionals. The HSE06 value is nevertheless still
> an approximation; quasiparticle (GW) corrections would
> provide a further benchmark, which is beyond the present
> scope."

#### 3.6 超导计算流程的可复现性(E1 评论 6)

现状: 第 244 至 254 行已有 Wannier90, EPW, Allen-Dynes,
各向异性 Migdal-Eliashberg 的描述和 k 网格, 但缺少从 DFPT
到 Tc 的端到端流水线说明: q 点网格, delta 展宽, Wannier
投影选择依据, alpha2F(omega) 与 lambda, omega_log 的求值式,
库仑赝势 mu* 的具体取值(第 251 行提到 0.10 至 0.16 的
范围, 但没写本文具体用哪个值, 为什么).

措施: 新增一小节(约一页, 可配流程图)按数据流写清:
DFPT(Quantum ESPRESSO 的 ph.x, q 网格)到电声矩阵元到
Wannier90 插值(投影 B 的 s 与 p 轨道, 细密 k 与 q 网格)到
EPW 计算 alpha2F(omega), lambda, omega_log 再到
Allen-Dynes 公式(mu* 取具体值)与各向异性
Migdal-Eliashberg 方程(温度, Matsubara 截断).
给出关键数值参数表. 同时明确区分:
声子色散无虚频等于 0 K 动力学稳定; AIMD 等于有限温短时
结构保持; 二者回答的问题不同.
E1 原话 The distinction between phonon stability and
finite-temperature AIMD should be made clear,
这一条同样适用于 Ch6.

### 四, Chapter 6(beryllene 体系, 两份报告意见最密集的一章)

#### 4.1 cubic trilayer beryllene 的构造方法(E1 评论 7, 8)

现状: src/project_3_main.tex 第 262 至 266 行只说 we also
identify a cubic trilayer beryllene structure. This structure
adopts an AB stacking arrangement, 完全没写这个结构是怎么
得到的. 第 285 至 288 行提到还测了 2 层与 4 层 cubic 以及
1 至 4 层 graphene-like 结构(动力学不稳定).
从第 278 至 283 行与 bulk bcc beryllium 的对比推测,
该结构可能取自 bcc 铍的某个晶面切割, 但文中没有说.

措施: 新增一段 Construction of the cubic trilayer candidate,
写清三点:

- 结构来源: 是从 bulk bcc-Be 的某个晶面切层得到,
  还是结构搜索(USPEX, CALYPSO, AIRSS, 随机采样)得到,
  还是手工搭建后弛豫;
- 筛选漏斗: 测试了多少候选(2, 3, 4 层 cubic 与 1 至 4 层
  graphene-like), 经声子筛选后只剩 trilayer 动力学稳定;
- 初猜的晶格参数与弛豫后的偏差.

这一段直接决定本章最新颖贡献的可信度, 务必写实写细.

#### 4.2 Z2 与金属性的矛盾(E1 评论 7)

现状: 第 29 至 31 行称 the cubic trilayer phase also exhibits
a non-trivial Z2 topological invariant, 而第 444 行写 the
cubic trilayer beryllene structure shows metallic behaviour;
第 548 行用 Fu-Kane 宇称乘积求 Z2.Fu-Kane 判据的前提是有
全局能隙的绝缘态; 对金属, 占据态子空间在某些 k 点不闭合,
宇称乘积无定义. 这是全章最需要论证的一点.

措施, 按数据实际情况三选一:

- 情形一: 金属性仅来自某个高对称点或线上的微小费米口袋,
  而占据子空间与其上方能带之间处处有直接带隙. 明确论证
  这一点, 给出各高对称点直接带隙数值表, 说明 Z2 是对
  占据子空间定义的, 并引用类似处理半金属拓扑的文献;
- 情形二: SOC 实际打开了全局小能隙, 即之前判金属是
  无 SOC 的 PBE 结论. 修正表述, 说明考虑 SOC 后为窄隙
  半导体或拓扑绝缘体;
- 情形三: 确实是金属. 撤回或弱化 Z2 论断, 改为讨论近费米
  面能带的非平庸宇称结构, 或引入拓扑半金属的正确诊断量
  (Weyl 点, 费米弧等), 不宜再用 Fu-Kane Z2.

同时在 Ch1 按 E1 要求先铺垫 Z2 的物理意义(见 1.1 节).

#### 4.3 稳定性与光学量的 2D 归一化(E1 评论 8)

措施:

- 结合能与吸附能统一 per atom 或 per area, 并与 bulk hcp-Be
  及已报道的 alpha 与 beta-beryllene 文献值对齐比较;
- 光学量对 2D 体系受真空层厚度影响: 说明采用何种归一化
  (有效层厚, 或改用与层厚无关的量, 如光学电导或吸收率);
  检查 Ch6 光学数值与 Ch3 示例中所用约定是否一致,
  两处数据应同源(见 1.2 节措施三);
- 稳定性表述按 1.4 节的三档措辞改写.

#### 4.4 缺少 HSE06 的理由(E2 评论 6.1)

措施: 在 Ch6 方法小节补一段. 可接受的论证角度,
按真实情况写:

- 计算成本: HSE06 对三层层状结构加 SOC 的计算量很大;
- 趋势可靠性: Ch4 与 Ch5 已系统对比 PBE 与 HSE06, 证明
  PBE 给出的趋势(相对变化, 各向异性方向)在 HSE06 下保持;
  Ch6 的主要结论是趋势性结论;
- 明确承认局限, 例如 Absolute band positions may shift
  under HSE06; the qualitative trends reported here are not
  expected to change, based on the PBE-HSE06 comparisons in
  Chapters 4 and 5.

#### 4.5 收敛性测试的正文讨论(E2 评论 6.2)

措施: 在 Ch6 方法小节用文字写清: 对哪个量(总能, 带隙,
光学谱)做了截断能与 k 点收敛; 判据(如总能差小于
1 meV/atom); 最终选取的网格及理由. 把 SI 里的收敛图在
正文中 \ref 并各用一句话解读, 回应 E2 原话 without
expecting the readers to interpret the graphs by themselves.

#### 4.6 Figures 6.2 与 6.3 球的颜色含义(E2 评论 6.3)

措施: 在图注或首次出现处的正文写明绿色与蓝色 Be 原子的
区别, 通常是不同层或晶体学不等价位点. 对照
src/project_3_main.tex 第 240 行附近的结构图, 补一句,
例如 Green and blue spheres denote beryllium atoms in the
outer and central layers, respectively.(按实际含义写).
顺便全文统一图注规范: Ch1 的 Fig 1.1 已有类似说明
(different colours denoting crystallographically
inequivalent boron sites), 保持同样的写法.

#### 4.7 氢化对象的选择依据(E2 评论 6.4)

措施: 加两到三句说明为什么氢化 alpha 与 beta 而不氢化
cubic trilayer. 可从这些角度写, 按真实原因:
trilayer 中央层原子配位饱和, 无悬挂键; 表面位阻;
氢化后结构弛豫不稳定; 或研究问题聚焦于氢化对已知相的
调控, 而 trilayer 是新相需先表征其本征性质.
若其实做过但失败或不稳定, 写出 we attempted ... but the
hydrogenated trilayer reconstructs / is dynamically unstable
反而是加分信息.

#### 4.8 AIMD 方法细节缺失(E2 评论 6.5)

现状: 第 356 至 363 行只说 using ab initio molecular
dynamics simulations, 以及 the temperature remains close to
the target range, 系综, 温度, 步长, 总时长全无.

措施: 在方法小节或 AIMD 首次出现处补齐参数, 英文骨架:

> "AIMD simulations were performed in the NVT ensemble
> (Nose-Hoover thermostat) at 300 K, with a time step of 1 fs
> for a total simulation time of x ps, using a 3x3x1
> supercell."

按实际参数填写, 并在 AIMD 图的图注中写明时长与温度.
与 1.2 节的方法卡片呼应.

### 五, Chapter 7(结论与展望)

#### 5.1 局限性小节(E2 评论 8)

现状: src/conclusion.tex 目前基本是逐章成果复述
(We therefore arrive at the result that ...),
没有 limitations 内容.

措施: 在结论与展望之间插入一节 Limitations of the
present work, 覆盖六点:

- 方法层级: PBE 与 HSE06 的带隙近似性, 无 GW 与 BSE
  (激子效应), 独立粒子介电响应的局限;
- 超导: mu* 的半经验性, lambda 与 Tc 对参数的敏感性;
- 稳定性判据的局限: 动力学稳定不等于热力学稳定,
  不等于可合成(呼应 3.2 节);
- AIMD 时标(5.5 ps)只能证明短时结构保持;
- 拓扑: Z2 宇称判据的适用前提(见 4.2 节);
- 明确列出已实验实现与纯理论预测的清单
  (E2 原话要求 distinguish).

#### 5.2 Future work 要说透预期改进(E2 评论 9)

现状: 结尾段已列了实验验证方向与理论延伸方向
(GW, 激子, 量子输运, 应变, 掺杂, moire 等), 但只是罗列.

措施: 每条方向补一句能带来什么具体改进, 例如:

- GW 与 BSE: 定量修正带隙与激子束缚能,
  使光学峰位可与实验直接对比;
- 更长时间的 AIMD 与凸包分析: 从短时保持升级为
  热力学可合成性判据;
- 应变与掺杂: 预期能连续调控 Tc 或等离激元频率的
  定量窗口;
- 量子输运: 验证拓扑边界态的电导特征
  (2e2/h 平台).

### 六, 建议的修改顺序

按优先级排列, P0 最高:

- P0: Ch1 重写(研究空白, 文献综述, 光学与拓扑动机,
  三章关联), 文件 src/introduction.tex, 性质为写作,
  工作量最大;
- P0: Ch2 与 Ch3 瘦身搬迁加方法路线图一节, 文件
  src/fundamentals_a.tex, src/fundamentals_b.tex,
  src/appendix.tex, 性质为结构性调整, 主要是剪贴加写一节;
- P0: Ch6 的 Z2 与金属性矛盾论证(见 4.2 节), 文件
  src/project_3_main.tex, 可能需要补算直接带隙表;
- P1: Ch5 磁性态与光学矛盾, 虚频矛盾, 超导流程
  (见 3.3 至 3.6 节), 文件 src/project_2_main.tex,
  核查数据加写作;
- P1: Ch6 结构构造, HSE06 理由, 收敛性, AIMD 细节,
  氢化依据, 图注颜色(见 4.1 与 4.4 至 4.8 节), 文件
  src/project_3_main.tex, 写作为主, 可能补少量说明图;
- P1: 三章章首贡献声明(见 1.3 节), 文件
  src/project_1_main.tex, src/project_2_main.tex,
  src/project_3_main.tex, 工作量小, 必须做;
- P2: Ch4 图注重写与图片重做(见 2.1, 2.2 节), 文件
  src/project_1_main.tex, 出图用 vmatplot, 机械但费时;
- P2: Ch3 beryllene 示例来源标注(见 1.2 节措施三),
  文件 src/fundamentals_b.tex, 工作量小;
- P2: Ch7 局限性与 future work 深化(见 5.1, 5.2 节),
  文件 src/conclusion.tex, 写作;
- P2: 全文措辞统一, 稳定性三档, 预测与实验区分
  (见 1.4 节), 涉及全部文件, 检索替换加润色.

### 七, 与回复信的联动

reply_to_examiners.md 已搭好框架, 对 E1 的第 1, 2 条已有
回复雏形, 留有 pages x, y 占位符. 建议: 每完成一项修改,
立即在回复信对应条目填入页码和关键新增文字的引文.

E2 的意见按编号 1 至 9 逐条回复即可, 多为 Added at page x
或 Corrected in the revised Figure y 型短回复.
E1 的第 3, 5, 6, 7 条需要在回复中给出稍长的解释性文字,
尤其 Z2 与磁性态两处, 回复信里的论证要和正文改动严格一致.

回复信整体策略: 开头加一段总览, 概括三类改动
(一是 Ch1 至 Ch3 重组; 二是各章科学表述澄清;
三是图表与格式), 并注明总页数变化.
对 E1 的 capable of reaching a professional doctoral
standard 和 E2 的正面评价, 回应语气保持一致:
接受几乎全部意见, 逐条给出改动位置.
对个别有保留的点(如确实无法补大规模 HSE06 计算),
用已在文中明确说明局限的方式回应, 而不是回避.

以上建议基于 2026-09-19 对两份 examiner reports 与论文
源码的交叉核对. 论文文件本身未做任何改动.
