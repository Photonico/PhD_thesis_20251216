# Deepseek

## 0919

## 详细修改方案(Deepseek / deepseek-flash): 结合两份 examiner reports

> 生成: 2026-09-19 · backend: deepseek-flash · 未改动任何论文文件(只读 + 本文件追加)证据来源:
> .output/thesis.pdf(270 页 PDF, 正文 242 页), .output/thesis.toc 与 .lof, src/*.tex,
> report/ 两份报告. 全文用中文讲解; 需要写进论文的英文文本放在标注为"英文可粘贴"的代码块里.

### 0. 结论速览

两份报告的具体条目虽多, 但根子上是同一个问题: 论文把三个各自独立的计算工作打包在一起, 而没有建立起一个博士课题的论证结构.

具体表现为四个可量化的硬伤:

- (1)没有文献综述.Chapter 1 只有 990 词 / 4 页, 且全章没有任何 section, 是一段科普加章节导览.
- 证据: Ch1 = pp.1–4(TOC).
- (2)Ch2+Ch3 占掉半分论文, 却几乎不含任何计算方法; 而 examiner 点名的 8 项方法在 Ch4–6 里全都有, 只是散落在各章.
- 证据: Ch2 = 14,841 词 / 74 页; Ch3 = 6,873 词 / 32 页; 两者合计 21,714 词, 约为全文 44,259 词的
  49%; 8 项方法在 Ch2/Ch3 中全部缺失.

- (3)图完全读不了. 这不是几张图的问题: 72 页的图内文字小于 6 pt, 最小 2.1 pt, 而正文是 12 pt.
- 证据: 对编译后 PDF 的逐页字体测量, 详见 G5.
- (4)Chapter 3 把 Chapter 6 的原创结果当成教科书示例用掉了, 而且没写来源, 源码里还留着 % cite my third project
  here.

- 证据: src/fundamentals_b.tex: 530; 图 3.1–3.6(pp. 93, 101, 103, 104, 106, 108).

其中第 4 条是唯一有学术规范性风险的一条, 建议最优先处理.

另外, 两位 examiner 的口径其实不同, 改法也不同:

- Examiner 2(docx)态度积极, 意见几乎全是编辑性与完整性方面的(补文献综述, 标来源, 放大图, 补 AIMD 参数, Ch7 加
  limitations). 这些都是低成本, 高确定性的.

- Examiner 1(pdf)更严厉, 质疑的是研究定位(材料之间像在跳跃, 缺乏关联, 定位不清). 这条不能靠补几句过渡句糊过去, 需要真正重写 Ch1
  并新增一节方法路线图.

关键判断: 不需要补做新的科学计算就能满足绝大部分意见.8 项方法的内容在 Ch4–6 里已经写好, 只需上移或重写; 文献综述是写作工作; 图的字号是重新出图.
真正需要新算力的只有少数几项, 见第 7 节清单.

### 1. 两份报告条目 → 论文实际证据 → 措施 对照

- E2-1 缺少专门且全面的文献综述
- 论文证据: Ch1 仅 990 词 / 4 页, 无对前人工作的批判性梳理.
- 措施: 扩写成 Ch1 导论加新的文献综述章(或 Ch1 内若干节).
- 优先级: ★★★
- E2-2 p.100 起用 α/β-beryllene 当示例, 需说明来源
- 论文证据: 图 3.1–3.6(pp.93/101/103/104/106/108)是你自己的 Ch6 数据; fundamentals_b.tex: 530 有
  % cite my third project here; 引文串里混着他人综述.

- 措施: 加来源声明与交叉引用; 或把 6 张图整段移入 Ch6.
- 优先级: ★★★
- E2-3 多作者章节需声明已发表及本人贡献
- 论文证据: 全篇不存在任何作者贡献声明; src/publications.tex: 52-55 却写 we confirm that the
  authorship attribution statements above are correct, 而上面并没有这些声明(悬空引用).

- 措施: 每章开头加 Authorship 段落; 修好 publications.tex.
- 优先级: ★★★
- E2-4 图不可读(4.29, 4.30 图例)
- 论文证据: 实测 4.29/4.30 图例 2.6 pt; 4.31–4.34 为 2.1 pt; 全文 72 页受影响.
- 措施: 矢量图重出, 字号不小于 8 pt; 多面板图拆分.
- 优先级: ★★★
- E2-5 Fig 5.1 应提前到方法或引言节
- 论文证据: Fig 5.1 = fig: ob14_atomic_structure, 位于 p.155(5.4 结果节开头).
- 措施: 移到 5.2 末或 5.3 开头.
- 优先级: ★☆
- E2-6.1 Ch6 只有 PBE, 缺 HSE06 且无理由
- 论文证据: project_3_main.tex: 155 只有 PBE; 仅在 457-459 说 PBE 低估带隙(半个理由).
- 措施: 加显式 justification(含成本论证).
- 优先级: ★★
- E2-6.2 收敛测试没在正文讨论
- 论文证据: project_3_main.tex: 168-172 只引用了图; 具体数值(NBANDS=140/133/70/66, 厚度值)只在 SI 的
  project_3_SI.tex: 53-63.

- 措施: 把数值和判据上移到 6.3 节.
- 优先级: ★★
- E2-6.3 图 6.2/6.3 绿球蓝球含义未解释
- 论文证据: 两张图题注完全没有颜色说明(project_3_main.tex: 248-252, 289-293); 面板标签仅 5.4/5.6 pt.
- 措施: 题注加颜色图例; 放大字号.
- 优先级: ★★
- E2-6.4 为何只氢化部分相, 三层相不氢化
- 论文证据: project_3_main.tex: 297-301 只说 α 做双面, β 做单双面, 无理由, 三层相完全没做.
- 措施: 补理由(对称性, 偶极, 配位饱和); 或补算.
- 优先级: ★★
- E2-6.5 AIMD 缺 ensemble, 温度, 时间步, 总时长
- 论文证据: project_3_main.tex: 356-362 与题注 374-379 四项全无; 正文说 temperature remains close
  to the target range 但目标温度从未给出.

- 措施: 补齐参数(VASP 输入文件里都有).
- 优先级: ★★★
- E2-8 Ch7 应加局限性, 并区分实验已证实与纯理论预测
- 论文证据: Ch7 仅 1,175 词 / 4 页(pp.217–220), 通篇总结, 无 limitations.
- 措施: 新增 Limitations 与 Experimental status 两节.
- 优先级: ★★★
- E2-9 未来展望应说明具体能改进什么
- 论文证据: 现为方向罗列.
- 措施: 每条方向补预期改进什么, 为什么.
- 优先级: ★
- E1-1 研究定位不清; Ch2+3 约 100 页过长且无方法路线图
- 论文证据: Ch2+Ch3 = 106 页(实测); examiner 点名的 8 项方法全部缺失.
- 措施: 压缩至附录, 并新增方法路线图节.
- 优先级: ★★★
- E1-2 章节之间像跳来跳去, 缺关系; 应解释为何三者同属一篇; 光学与拓扑的动机不足
- 论文证据: Ch1 只在导览段提了一句 Z2 拓扑, 没有解释其物理意义; 光学量被当作标准输出.
- 措施: 重写 Ch1, 补 research gap, 主线, 拓扑与光学的物理动机.
- 优先级: ★★★
- E1-3 需要简洁实用的方法叙述(8 项)
- 论文证据: 8 项在 Ch2/Ch3 全缺, 在 Ch4–6 全有.
- 措施: 新建 2.x 节 Computational methods used in this thesis.
- 优先级: ★★★
- E1-4 Ch4 相对增量; 图 4.29–4.36 题注太短
- 论文证据: 题注实测为 3–6 个词(如 Reflectivity., Extinction coefficient.).
- 措施: 重写 8 条题注(模板见 4.5).
- 优先级: ★★★
- E1-5 Ch5 的稳定性, 超导, 等离激元论断需限定; AFM–FM 能量差过小; 负声频表述不一致
- 论文证据: 见 3.4 节逐条: 声频确实自相矛盾; AIMD 被误称为 thermodynamic stability.
- 措施: 逐条改写.
- 优先级: ★★★
- E1-6 单层电子态自相矛盾; PBE–HSE06 差异需解释; 超导流程需可复现说明
- 论文证据: 正文说单层是 AFM 半导体, 光学节却按金属处理; λ 有报告但 omega_log 与 alpha^2F(omega) 从未出现.
- 措施: 逐条改写并补数据.
- 优先级: ★★★
- E1-7/8 Ch6 新结构生成方法不清; Z2 论断在金属相下需辩护; 二维归一化; 区分三种稳定性
- 论文证据: 结构无构造描述; Z2 与金属性直接冲突且 X 点宇称未列表; 三种稳定性概念混用.
- 措施: 逐条改写.
- 优先级: ★★★

### 2. 全局性问题与措施

#### G1. 没有文献综述(E1-1, E1-2, E2-1)★★★

现状: src/introduction.tex 共 73 行, 990 词, 编译后 pp.1–4. 全章没有 section, 结构是: 石墨烯与 Xenes
泛泛介绍, 再到硼基材料, 铍基材料, 调控是核心挑战, DFT 能做啥, 逐章导览. 它描述了论文要做什么, 但没有论证为什么这件事值得做, 前人做到哪一步, 还差什么.

这是两位 examiner 共同的第一条意见, 也是研究定位不清的根因.

措施(推荐方案 A):

- (1)把 Ch1 扩成两章或一章两大节:
- (1)导论与动机(保留现有内容, 压缩到约 1000 词).
- (2)文献综述与本文定位(新增, 约 4000–6000 词).
- (2)文献综述按三条线索加一个交叉来组织, 而不是按材料罗列:
- (i) 二维硼: 从块体同素异形体到硼烯相图, 实验合成现状(MBE on Ag(111)), 稳定性与氧化问题, 氢钝化.
- (ii) 二维铍: α/β-beryllene 的理论预测, Chahal 2023 的实验实现, 热输运, 拓扑与超导预测.
- (iii) 二维材料的调控手段: vdW 异质结, 氢功能化, 维度, 应变.
- (iv) 交叉点即本文的 gap: 轻元素 Xenes 中键合拓扑到集体激发这一因果关系尚未被系统检验.
- (3)必须显式写出一段 research gap, 英文草稿见 4.1.
- (4)文献要批判性使用: 把已实验证实和仅理论预测分开标注(examiner 明确要求). 建议在综述里就用一张表区分:

- 硼烯 beta12 与 chi3
- 状态: 实验已合成
- 代表工作: zhong2017metastable, ranjan2019freestanding
- 块体 o-B14
- 状态: 仅理论预测
- 代表工作: han2023superconducting
- α/β-beryllene
- 状态: 理论预测加近期实验报道
- 代表工作: ono2020dynamical, hess2022periodicity, chahal2023beryllene
- 立方三层 beryllene
- 状态: 本文首次提出
- 代表工作: 本论文 Ch6

- (5)拓扑动机(E1-2 专门点名): 现在 Ch1 只在导览段写 possess non-trivial Z2 topology.
  必须在引入宇称计算之前解释: 什么是 Z2, 非平庸意味着什么物理后果(螺旋边缘态, 背散射抑制, 自旋动量锁定), 为什么在轻元素里值得期待(SOC
  弱但对称性与轨道物理可驱动). 英文草稿见 4.1.

- (6)光学动机(E1-2 点名: often presented as a standard set of outputs rather than as
  observables answering defined scientific questions): 不要说我们算了吸收, 折射率, 反射率, 损耗谱,
  而要说每个量回答什么问题. 建议在 Ch1 加一小段并配一张映射表:

- epsilon_2(omega): 带间跃迁的谱权重, 回答哪些跃迁被打开或关闭, 氢化或堆叠如何改变.
- epsilon_1(omega) 过零: 屏蔽与等离激元条件, 回答是否支持方向性等离激元, 在哪个能量窗口.
- alpha(omega): 衰减长度, 回答可见光吸收是否足够强(光电器件).
- R(omega): 表面反射, 回答是否可作为反射型等离激元器件.
- L(omega) = -Im(1/epsilon): 集体激发与损耗通道, 回答等离激元能量与寿命, 可与 EELS 直接对照.

#### G2. Ch2+Ch3 占 49% 篇幅却零计算方法(E1-1, E1-3)★★★

现状(严格核对结果):

- Ch2: 14,841 词, 74 页, 258 个编号公式, 1 张示意图, 0 张表, 0 个计算参数.
- Ch3: 6,873 词, 32 页, 52 个编号公式; 其中约 36%(约 416 行 / 约 11.4 页)是纯教科书电动力学与 Kramers-Kronig
  形式推导.

- examiner 点名的 8 项方法, 在 Ch2 与 Ch3 中全部缺失:

| 方法 | Ch2/Ch3 | 实际写在 |
| --- | --- | --- |
| 几何优化与收敛判据 | 缺 | Ch4 96-110; Ch5 156-160; Ch6 161-172 |
| 布里渊区采样与 k 点选择 | 缺 | Ch4 96, 107, 110, 467-469; Ch5 236-245, 259-260; Ch6 159-172 |
| 声子计算 | 缺 | Ch5 223-225, 239-240; Ch6 312-340 |
| AIMD | 缺 | Ch6 356-357(且参数不全, 见 3.5) |
| 自旋极化与磁有序 | 缺 | Ch5 541-561 |
| 电子-声子与超导 | 缺 | Ch5 230-255 |
| 自旋轨道耦合 | 缺 | Ch6 527-534 |
| 拓扑 Z2 与宇称 | 缺 | Ch6 518-631 |

这意味着: 满足这条意见不需要做新计算, 只需重组. 这是整份修改里性价比最高的一项.

措施(推荐: 压缩加上移加新增一节):

- (1)新增一节 Computational methods used in this thesis(约 2–3 页),
  把上表右列的内容重写为面向方法本身的叙述(含具体参数, 判据, 取舍理由), 并交叉引用各章. 英文草稿见 4.2.

- (2)大幅压缩 Ch2, 把纯形式推导移入 Appendix:
- 建议移入附录: Thomas-Fermi 及其局限(pp.45–54, 约 9 页), 这是过时的 orbital-free 模型, 与本文计算无关.
- 时间演化算符, Heisenberg 绘景, 连续性方程(pp.6–18, 约 12 页)可压缩为 2–3 页概述.
- 巨正则系综(约 1 页)本文从未使用, 可删或一句话带过.
- 两次变分推导 Kohn-Sham(文中自己承认是 complementary)保留其一.
- 重复内容合并: Thomas-Fermi 势两次, von Weizsäcker 两次, Euler-Lagrange 两次, 密度算符四次, SCF 循环两次,
  epsilon_ab = delta_ab + chi_ab 两次, 非局域本构两次, 面内与面外分解两次.

- (3)压缩 Ch3: Maxwell 方程组(3.1.1 节), 非局域 chi(r, t; r', t')(推出后立刻丢弃), Kramers-Kronig
  与静态极限(3.3 节, 约 6 页)可压缩. 注意: VASP 直接给出 epsilon_1 与 epsilon_2, 全文从未做过 KK 变换, 因此 3.3
  节属于纯形式内容, 最适合移入附录.

- (4)保留但重写 Ch3 的 3.4 节(介电函数到光学量), 因为各章都要引用它.
- (5)Ch2 开头已经声明 This chapter partly draws on my notes from the Coursera course
  Density Functional Theory... taught by Francesco Sottile and Lucia Reining,
  这条保留并保留引用, 它对教科书化的质疑是有利的自证.

#### G3. 章节之间缺乏统一叙事(E1-2)★★★

现状: Ch1 的导览段确实逐章介绍了, 但只是目录的散文版. 三章之间没有共同的科学问题.

措施: 在 Ch1 增设一节, 明确写出一个中心问题加三条验证路径. 核心论证建议如下(英文见 4.1):

- 中心问题: 在轻元素二维体系中, 原子尺度的键合拓扑如何决定电子结构, 集体激发(等离激元)与关联或拓扑物态?
- 三条路径: 一是人为构造的 vdW 异质结(Ch4, 验证堆叠与界面自由度); 二是本征硼同素异形体(Ch5, 验证维度加氢化自由度); 三是铍基体系(Ch6,
  验证更轻元素加拓扑极限).

- 收敛的结论: 三者共同表明轻元素加低维加键合拓扑足以产生通常认为需要重元素或强关联才能出现的物性.
- 明确写出每一章回答哪个子问题, 贡献什么, 并说明为什么必须放在同一篇论文里(共同的物理机制, 共同的方法论, 递进的元素轻重与维度).

#### G4. 作者贡献声明缺失(E1 前言段, E2-3)★★★

现状(严重, 且有悬空引用):

- Ch4, Ch5, Ch6 没有任何作者贡献或已发表声明.
- src/publications.tex: 52-55 有标题 Authorship attribution statement, 正文写 As
  supervisors for the candidature upon which this thesis is based, we confirm
  that the authorship attribution statements above are correct. 但上面根本没有这些声明,
  只有论文列表. 这是明显的未完成项.

- 签名区只有 Catherine Stampfl 与 Lu Niu; thesis.tex 里定义了副导师 Carla Verdi, 但签名区没有她.

措施:

- (1)在 publications.tex 中为 Ch4/Ch5/Ch6 逐篇补上贡献声明表(作者乘贡献维度), 再让导师签字确认, 这样 statements
  above 才成立.

- (2)在每章开头(Abstract 之后, Introduction 之前)加一段该章专属的贡献加已发表状态说明. 模板见 4.3.
- (3)若学校要求, 补 Carla Verdi 的签名位(请自行核对 USyd 规定).

#### G5. 图件可读性(E1-4, E2-4)★★★

这是本报告最硬的量化发现. 我对编译后的 PDF 逐页做了字体测量(正文 = 12 pt):

- 72 页的图内文字小于 6 pt(不到正文的一半, 印刷后不可读).
- 最小 2.1 pt(出现在 pp.136, 143, 144).
- examiner 点名的图 4.29 图例 = 2.6 pt, 图 4.30 图例 = 2.6 pt, 他的描述完全准确.

分章受影响清单(图号即该页上的图):

- |Ch2 受影响页数: 0 受影响的图: 无 最小字号: 无
- |Ch3 受影响页数: 6 受影响的图: 3.1(p.93), 3.2(p.101), 3.3(p.103), 3.4(p.104), 3.5(p.106),
  3.6(p.108) 最小字号: 5.7 pt

- |Ch4 受影响页数: 23 受影响的图: 4.2, 4.5–4.17, 4.20–4.36 最小字号: 2.1 pt(4.21, 4.22, 4.31–4.34)
- |Ch5 受影响页数: 17 受影响的图: 5.2, 5.4, 5.6–5.17, 5.20–5.30 最小字号: 2.7 pt(Fig 5.6)
- |Ch6 受影响页数: 26 受影响的图: 6.1–6.34(几乎全部) 最小字号: 2.9 pt

Ch4 中 4.15–4.36 位于 Supplementary information(pp.132–146).examiner 是当作论文正文读的,
必须一并修, 不能以在 SI 里为由不改. 补充对应关系: 图 4.29 = SI 的 S1.17, 4.30 = S1.18, 4.31 = S1.19, 4.32 =
S1.20, 4.33 = S1.21, 4.34 = S1.22, 4.35 = S1.23, 4.36 = S1.24.

措施(关键: 这些图是矢量 PDF, 不是位图, 所以提高 DPI 没用, 必须改字号与布局):

- (1)统一出图规范并写进你自己的绘图库 vmatplot:
- 坐标轴标签不小于 8 pt, 刻度不小于 7 pt, 图例不小于 7 pt, 并且要按最终插入宽度换算(即考虑 width=0.4\linewidth 的缩放).
- 半栏图(0.4\linewidth 到 0.5\linewidth)最多 2 个面板, 4 面板必须整栏(1.0\linewidth), 6
  个及以上面板必须拆成多张图或移入 SI.

- 不用 adjustbox 强压宽度, 这正是字号被压小的主因.
- (2)优先重出这 6 张最严重的: 4.21, 4.22, 4.31, 4.32, 4.33, 4.34(2.1–2.6 pt).
- (3)一个可自检的判据: 出图后把 PDF 渲染到 100% 打印尺寸, 图内最小文字应不亚于正文的 2/3(即不小于 8 pt). 用 PyMuPDF 读
  span 的 size 可以复验.

- (4)顺便修掉题注里的笔误: project_1_SI.tex: 213 结尾是 monolayers..(两个句点).

#### G6. Chapter 3 把 Chapter 6 的原创结果当教科书示例(E2-2)★★★(规范性风险)

这是我认为最需要你亲自决策的一条.

事实(我逐条核对过):

- (1)Ch3 的 3.2.3 节与 3.4.1 到 3.4.4 节共有 6 张图加约 86 行结果讨论, 全部是 α- 与 β-beryllene.
- (2)这 6 张图是你自己的数据: 文件位于 figures_ch3/(3.1_dielectric.pdf, 4.1_absorption.pdf 等),
  由你自己的 vmatplot(dielectric_function.py, linear_optical_properties.py, commons.py)
  生成; 材料与物理量和 Ch6 完全一致.

- (3)讨论文字与 Ch6 近乎逐句相同. 例如 Ch6 的 project_3_main.tex: 727 写 This behaviour shows
  that amplitude attenuation also depends on both optical direction and crystal
  structure., 而 Ch3 的 fundamentals_b.tex: 1012 写 This behavior shows that
  amplitude attenuation also depends on both the optical direction and the
  crystal structure of the medium.

- (4)来源完全没写, 而且源码里留着 TODO: src/fundamentals_b.tex: 530 的 % cite my third project
  here.

- (5)更麻烦的是: 这些结果句后面跟的是一串他人文献, 例如 fundamentals_b.tex: 863 与 1012 处的
  niu2024electronic, khan2025insight, huang2023optical, suk2024ultrafast,
  cheng2025two, tang2025unveiling, kim2024hyperspectral. 其中 niu2024electronic 是你自己的
  Nanomaterials 论文, 但那篇讲的是石墨烯与硼烯异质结, 不是 beryllene; 其余都是第三方综述. 读者会自然地把这些引文理解为图中数据的出处,
  从而把你自己未发表的 Ch6 结果归给别人.

- (6)交叉引用是单向的: Ch5/Ch6/SI 共 11 处向前引用 Ch3, Ch3 不引用任何一章.

措施(二选一, 我推荐 A):

- 方案 A(推荐): 把 6 张图和 6 段结果讨论整体移入 Ch6(它们本来就属于那里), Ch3 只保留形式推导加一句本文所用光学量的定义见本节. 这样 Ch3
  变短, Ch6 变强, 且彻底消除归属问题.

- 方案 B(保留为示例): 保留图, 但必须: 删掉 530 行的 TODO; 每处加一句明确来源声明(英文模板见 4.4); 加 ref 指向 Ch6 对应小节;
  把那些会被误读为数据出处的文献引用从结果句末尾移走, 只保留方法性的引用.

- 无论哪种方案, 都请在 Ch6 中检查是否有反向引用(目前 Ch6 也没有指向 Ch3 的图).

#### G7. 稳定性三个层次概念混用(E1-5, E1-8)★★

examiner 反复要求区分 dynamical stability, energetic preference, thermodynamic stability
与 synthesizability. 目前论文把它们当同义词用:

- |Ch5 project_2_main.tex: 507-509 原文: we also verified that the
  hydrogen-terminated bilayer is thermodynamically stable 问题: 依据只是 400 K, 约 5.5 ps
  的 AIMD.AIMD 只能说明短时热稳定性, 不能证明热力学稳定

- |Ch5 325 原文: predicted to be dynamically and thermodynamically stable(指他人工作)
  问题: 转述他人结论时也应说明其依据

- |Ch6 356, 362 原文: finite-temperature stability 问题: 同上

措施: 全文统一采用四级表述, 并明确各自证据:

- (1)energetic preference: 内聚能相对于一组明确列出的参考相.
- (2)dynamical stability: 声子谱无显著虚频(要给出判据, 如低于某阈值的模视为数值噪声).
- (3)finite-temperature persistence: AIMD 在给定温度与给定时长内无结构坍塌, 不要叫 thermodynamic
  stability.

- (4)synthesizability: 需要动力学势垒, 衬底外延关系, 与实验对照, 本文未涉及, 应明确说明属未解决问题.

#### G8. 二维归一化与吸收系数的量纲(E1-8)★★

好消息: Ch5 已经做了正确的二维介电函数重归一化(project_2_main.tex: 270-296, 含 d_2D 定义与 SI 图 S2.6), Ch6
也做了(208-212, 厚度值在 SI 的 project_3_SI.tex: 53-63). 这一点两位 examiner 的意见其实已被满足, 只是藏在 SI
里.

仍存在的问题:

- (1)Ch6 正文只说 thickness values are given in section 3_supplementary, 应把数值和判据直接写进
  6.3 节(examiner 明确说 without expecting the readers to interpret the graphs by
  themselves).

- (2)吸收系数的量纲陷阱: 由重归一化后的 epsilon^2D 反推的 alpha = 2omegak/c 仍带长度量纲, 其数值依赖所取的 d_2D.
  二维材料文献中更常用, 不依赖厚度假设的量是吸光度 A(omega) 或二维光电导 sigma_2D(omega). 建议明确声明所用约定, 并至少在一个地方给出
  A(omega) 或 sigma_2D, 否则跨材料比较(如 Ch5 740 行与块体硅比较)不严格.

- (3)Ch5 740 行 The value of around 0.005 per angstrom is similar to that
  calculated for bulk silicon 中 The value 指代不明(哪个体系, 哪个方向), 必须写明.

### 3. 逐章修改措施(含具体行号)

#### 3.1 Chapter 1(pp.1–4)★★★

- 扩写为导论加文献综述(见 G1).
- 现有导览段落保留但压缩, 改写为中心问题加三条路径(见 G3).
- 补拓扑动机(在提到 Z2 之前).
- 补光学量的物理动机(映射表).
- 补一段本文的创新点(novel predictions 与 characterisation of known structures 的区分), 这是
  examiner 开篇就要求的. 建议明确列出: 新的等于立方三层 beryllene(Ch6), o-B14 单层的磁性与氢化双层超导(Ch5);
  表征已知结构的等于 α/β-beryllene 的确认(Ch5/Ch6 中属复现), 石墨烯与硼烯与 BC3 与 B4C3 的已知性质(Ch4).

#### 3.2 Chapters 2–3(pp.5–110)★★★

见 G2. 核心动作:

- (1)新增 2.x 方法路线图(英文草稿见 4.2).
- (2)Ch2: Thomas-Fermi 与其局限(约 9 页)移入附录; 时间演化与 Heisenberg 与连续性方程压缩; 合并 7 处重复推导.
- (3)Ch3: 3.1.1 节 Maxwell, 3.2.1 节非局域本构, 3.3 节 Kramers-Kronig(约 6 页, 且全文未实际使用)
  压缩或移入附录; 保留 3.4 节并重写.

- (4)Ch3: 处理 6 张 α/β-beryllene 图(见 G6).
- (5)目标: Ch2+Ch3 从 106 页降到约 50–60 页, 并在第 1 或第 2 章开头给出方法到章节的对照表.

提醒: 移动内容到附录会改变 ref 编号; thesis.tex 里附录是 input 的 src/appendix.tex, 目前只有 43 行(GitHub
仓库列表), 需要改造成真正的附录(可用 appendix 加 chapter, 注意 thesis.tex 中 appendix 目前被注释掉了).

#### 3.3 Chapter 4(pp.111–146)★★★

- (1)章首加贡献声明(E2-3). 模板见 4.3.
- (2)重写图 4.29–4.36 的题注(E1-4). 现状实测: 4.29 与 4.30 与 4.31 各为 Dielectric function
  components of...(5 词); 4.32 到 4.36 分别为 Absorption coefficient., Energy-loss
  spectrum., Refractive index., Reflectivity., Extinction coefficient.(1–2 词). 模板见
  4.5. 同时修 project_1_SI.tex: 213 的 monolayers...

- (3)放大所有这些图(见 G5).
- (4)章标题: TOC 显示为 Optoelectronic Properties of Heterostructure Bilayers, 未体现石墨烯,
  硼烯, 碳化硼的范围. 建议改为能反映内容的长标题.

- (5)回应 examiner 对该章相对增量的评价: 在章末 Conclusions 中明确写出该章的知识增量(structure-property
  mapping 与可调等离激元), 避免读者自行判断为只是算了一堆数.

#### 3.4 Chapter 5(pp.147–180)★★★

这一章的具体矛盾最多, 逐条给出.

(a)声子虚频自相矛盾(E1-5 明确点名), 主文与 SI 直接打架:

- 主文 project_2_main.tex: 499-504: we find that the hydrogen-terminated bilayer is
  dynamically stable... This is reflected by the presence of imaginary
  frequencies for the latter, but not for the former.

- SI project_2_SI.tex: 137-138(图 S2.9 题注): Small negative frequencies appear
  around the Gamma point for the hydrogen-terminated bilayer. These small
  negative frequencies are often found in 2D materials and do not by themselves
  indicate dynamical instability.

必须二选一并前后统一. 建议采用 SI 的(更诚实)版本: 承认 Gamma 点附近有小的负频, 给出数值大小与超胞依赖(2x2 与 3x3 的对比), 并说明判据.
英文改写见 4.6.

(b)单层电子态自相矛盾(E1-6 明确点名), 这是全篇最容易被抓住的逻辑漏洞:

- 电子结构节 project_2_main.tex: 543-544: The antiferromagnetic configuration is more
  favourable than the ferromagnetic configuration by 0.02 eV. A small band gap
  of 0.105 eV opens in the antiferromagnetic case.; 表 456-458 标 antiferromagnetic
  semiconductor.

- 光学节却按金属处理: 690(单层是 indefinite medium), 696-699(单层在 0.5–1.5 eV 有 plasmon),
  707-708(Except for the bilayer, the structures show characteristic metallic
  behaviour, the structures 包含单层), 734(For all structures except bilayer o-B14,
  the threshold is close to zero, corresponding to their metallic nature).

必须补写: 光学计算所用的电子态与磁态(是 PBE 非自旋极化的金属态, 还是 HSE06 AFM 态), 以及是否含带内 Drude 项. 若用的是非自旋极化金属态,
就必须在光学节开头声明, 并说明这与 AFM 基态的差异及影响. 英文改写见 4.6.

顺带: 若基态是 AFM 半导体(gap 0.105 eV), 那么 494 行的声子计算(No imaginary frequencies are
present...)是在哪个自旋态下算的? 如果是非自旋极化, 则动力学稳定的结论并未在真实基态下验证. 建议补算 AFM 态的声子, 或至少明确声明所用自旋态.

(c)AFM–FM 能量差 0.02 eV 过小(E1-5): 需说明是 per cell 还是 per atom, 单位晶胞含几个磁性位点,
以及该差值是否在方法精度内(HSE06 与 PBE, k 点, 展宽的影响). 建议给出两种泛函的结果对比. 另外 555 行说每个 apical B 上磁矩
0.262 mu_B, 557 行说 FM 元胞总磁矩约 2 mu_B, 请把磁性位点数目写清楚, 让两个数能自洽.

(d)AIMD 被误称为 thermodynamic stability: 见 G7.

(e)超导流程不可复现(E1-6): 方法节 230-255 已有不少内容(QE, norm-conserving 赝势, 45 Ry, 真空 15 埃,
Monkhorst-Pack 网格, q 点网格, Wannier90 投影, EPW, mu* = 0.13), 但仍缺:

- omega_log 从未出现, alpha^2F(omega) 从未画出, examiner 明确点名这两个量.
- 各向异性 Migdal-Eliashberg 计算所用的精细 k 网格与 q 网格, delta 函数展宽, Wannier 插值质量(插值能带与 DFT
  能带的对比).

- 术语不一致: 236-238 行的 k 网格写作 for the bulk, the monolayer, and the bilayer, 245 行又写
  for the monolayer and bilayer, 但本节开头 230-231 说的是 bulk, monolayer, and
  hydrogen-terminated bilayer, 而原始 bilayer 是半导体, 根本没做超导. 请全文统一为 pristine bilayer 与
  H-terminated bilayer.

- Tc 数值的选择性引用: 631-636 给 Allen-Dynes Tc = 28.2 K(bulk)与 18.5 K(H-bilayer); 653-654
  给 Migdal-Eliashberg 31.3 K 与 24.3 K. 但摘要 22 行, 结论 818 行, Abstract 文件, Ch7 都只引 24.3
  K, 未说明这是 ME 值而非 AD 值. 必须显式说明每个数值用的是哪种方法.

(f)内聚能的参考相选择(E1-5): 429-433 只与块体 o-B14(-6.16)和 alpha'-monolayer(-6.00)比较.examiner
说 establish energetic preference relative to selected references, 即参考集不完整. 建议补:
与硼的基态 alpha-B12(文中已在 387-388 提到 o-B14 比它高 0.232 eV)以及 beta-B 的对比; 与其它二维硼相(beta12,
chi3, alpha-sheet 等)的对比, 这些在 79-105 都提到了, 正好可以拿来当参考相. 另外结论 815-816 说 the bilayer is
notably more stable than the bulk by 0.19 eV, 二维双层比其三维母体更稳定是反直觉的, 若成立是很强的结论,
若不成立则是硬伤. 强烈建议复核(是否两者用了完全一致的赝势, 截断, k 点, 参考原子能量? 块体是否真的驰豫到极小?), 并在正文中给出复核说明.

(g)吸收系数的指代与量纲: 见 G8.

(h)Fig 5.1 位置(E2-5): project_2_main.tex: 304-317, 位于 5.4 节, 编译在 p.155. 移到 5.2 节结尾或
5.3 节开头.

#### 3.5 Chapter 6(pp.181–216)★★★

(a)结构与 Z2 的冲突(E1-7, 最重要), 这是全章最需要修补的科学逻辑:

- 正文 444-445: The cubic trilayer beryllene structure shows metallic behaviour,
  with multiple bands crossing the Fermi level.

- 正文 482-483: finite density of states at the Fermi level, consistent with its
  metallic band structure.

- 但 601-606 的表给出 nu = 1, 627-631 断言 cubic trilayer beryllene is also a
  non-trivial Z2 topological phase.

- 而所用方法(523-524, 536-554)是 Fu-Kane 宇称判据, 它要求占据态与空态之间存在能隙; N_occ 在金属中无定义, Kramers 对在
  E_F 处不分离, nu 不是拓扑不变量.

必须解决, 三种可能出路:

- (1)若 SOC 打开了能隙: 则说明 PBE 标量相对论能带是金属的, 但含 SOC 后在各 TRIM 处打开约 X meV 的能隙, 故 nu 良定义, 并给出
  SOC 能带图与各 TRIM 处的能隙数值. 这是最理想的情况, 而且与表中 12 个电子等于 6 个 Kramers 对自洽(Be 三层 = 6 个原子乘 2
  电子 = 12 电子, 恰好填满 6 对). 我核对了表的算术: delta_Gamma = +, delta_M = - 给出 nu = 1;
  alpha-beryllene 的 delta_Gamma = +, delta_M = - 给出 nu = 1; beta-beryllene 的
  delta_Gamma = +, delta_M = + 给出 nu = 0. 算术自洽, 且电子计数也对. 所以问题不在算错,
  而在金属这一表述与判据的相容性没交代.

- (2)若 SOC 未打开能隙: 则不能用 Z2. 应改用对称性指标(symmetry indicators, 如 irvsp 或 SymTop 的指标分析)或
  Wilson loop, 并把结论降级为 band-inversion 或拓扑半金属特征, 删除 non-trivial Z2 的表述.

- (3)若只在部分 TRIM 有隙: 必须逐点说明, 并明确 nu 不可定义.

另外两处相关缺陷:

- 568-571 用了 X 点的宇称 (-1)^nu = delta_Gamma delta_M (delta_X)^2 = delta_Gamma *
  delta_M, 但表中根本没有列出 X 点的宇称(只列了 Gamma 和 M). 必须在表中补 X(以及 Y, 若 X 与 Y 由四重对称等价需说明),
  否则读者无法验证.

- 611-616 题注把 Gamma 与 M 两列称为 parity products, 但列出的其实是单个宇称本征值, 而 product 列才是
  (-1)^nu. 术语需修正.

- 957-959: This result demonstrates that topological electronic states can arise
  in a light-element system without relying on strong spin-orbit coupling.
  这句很容易被读成计算里没用 SOC, 与 533 行 Spin-orbit coupling is included 矛盾. 改为该拓扑相不要求强 SOC, 但
  SOC 对于定义该不变量是必需的(SOC 能隙约 X meV).

- 摘要 32 行 This result indicates the emergence of topologically protected
  electronic states: 你没有计算边缘态. 若无边缘态计算, 应弱化为 indicates a non-trivial bulk
  invariant, which in a finite sample would support topologically protected edge
  states. 或者补一个半无限或纳米带的边缘态计算(这是最能提升该章分量的一步).

英文改写见 4.7.

(b)HSE06 缺失需要理由(E2-6.1): 现在只有 457-459 的半句理由(PBE generally underestimates band
gaps). 建议给出双重理由:

- 物理理由: 对金属相(立方三层, 1H- 与 2H-beta), PBE 与 HSE06 的差异主要体现在能带色散细节而非带隙, 故光学谱的主要特征(等离激元能量,
  谱重分布)对泛函不敏感.

- 成本理由: HSE06 光学计算需要在 105x105x1 的 k 网格上做, 代价不可接受(这是完全正当的理由, 但必须写出来).
- 补充: 至少对半导体相 2H-alpha-beryllene(PBE 带隙大于 4.0 eV)给出 HSE06 带隙, 或明确声明使用 scissors 修正,
  因为 PBE 会低估带隙 30–50%, 其吸收边位置不可靠. 这是 examiner 说 weakens confidence in the reported
  optical properties 的实质所在.

- 另外 457 行说 wide indirect band gap exceeding 4.0 eV at the PBE level. Since PBE
  generally underestimates band gaps, the actual gap is expected to be larger.
  这句话本身没问题, 但要给出具体 HSE06 值才可信.

(c)收敛测试未在正文讨论(E2-6.2): 168-172 只有 ref. 需要把 SI(project_3_SI.tex: 53-63)里的数值搬到 6.3 节:

- d_2D = 3.96 埃(alpha), 5.85 埃(beta), 6.97 埃(立方三层), 3.14 埃(2H-alpha), 5.52
  埃(1H-beta), 5.192 埃(2H-beta).

- NBANDS = 140(含氢), 133(不含氢), 70(bcc), 66(hcp).
- 并说明判据(如 k 网格加密到使 epsilon_1 与 epsilon_2 在 0–10 eV 内变化小于 X%).
- 顺带核对: SI 中 S3.3 与 S3.4, S3.5 与 S3.6, S3.7 与 S3.8, S3.9 与 S3.10, S3.11 与 S3.12 分别是
  NBANDS 收敛与 k 点收敛, 文件是不同的(我已核对文件大小均不同), 没有复制错误, 但正文应说明这两个变量是分别收敛的.

- 另: 159 行对块体用 27x27x27, 介电函数用 105x105x105, 这个跨度很大, 值得一句说明(带间跃迁需要极密网格).

(d)图 6.2 与 6.3 的颜色含义(E2-6.3): 题注 248-252 与 289-293 完全没有颜色说明. 好消息是论文里已有现成范式可抄: Ch1 的
Fig 1 题注写了 Large coloured spheres represent boron atoms, with different colours
denoting crystallographically inequivalent boron sites. Small light-purple
spheres represent hydrogen atoms.; Ch5 的 Fig 5.1 也说明了 G2/G3/G7 的配色. 请对 Fig
6.1/6.2/6.3 采用同一约定, 并在题注中写明: 不同颜色等于不等价 Be 位点(例如三层相中的表层与中间层), H 原子用哪种小球表示. 同时把
5.4/5.6 pt 的面板标签放大到不小于 8 pt.

(e)为何不氢化三层相(E2-6.4): 297-301 无理由. 需要补写:

- 对称性与偶极理由: alpha-beryllene 是平面单层, 单面氢化会破坏镜面对称并产生净偶极, 故只做双面; beta-beryllene 是双层,
  单面与双面都物理上合理, 故都做.

- 三层相: 说明中间层不可及, 表层配位是否已饱和; 若测试过而发现不稳定或不吸附, 请给出数据; 若没测过, 就明确写未考虑, 列为未来工作, 并说明理由. 英文草稿见
  4.7.

(f)AIMD 参数全缺(E2-6.5): 356-362 与题注 374-379 缺 ensemble, 温度, 时间步, 总时长; 正文说 the
temperature remains close to the target range 却从未给出目标温度. 这些参数在你的 VASP INCAR 里都有,
直接补齐即可. 同时在 SI 中给出与前文一致的说明.(对比: Ch5 至少写了 400 K, 但同样缺 ensemble, 时间步与时长.)

(g)新结构的构造方法不清(E1-7): 261-265 只描述了立方三层(AB 堆叠, 中间层位于上下层空心位), 没说是怎么得到的. 需要补:

- 来源(从块体 bcc Be 切割? 由 alpha 与 beta 堆叠枚举? 对称性搜索? 是否用了 CALYPSO 或 USPEX 之类的结构搜索?).
- 枚举与筛选流程(试了哪些层数, 哪些堆叠, 多少种初始构型).
- 筛选判据与结果: 281-284 提到两层, 四层立方结构以及 1–4 层的石墨烯型铍层都动力学不稳定, 这些也应有数据(哪怕放进 SI 一张图),
  否则无法评估为何只有三层成立.

- 建议在 6.4.1 节加一段结构搜索与构造, 并配一张流程图或枚举表.

(h)其余小的规范性检查:

- 399 行 These negative adsorption energies indicate that all three
  hydrogen-functionalized structures are stable with respect to molecular
  hydrogen.: 吸附能定义式 176-180 写的是 E_H denotes the total energy of a hydrogen atom
  in the H2 molecule, 这有歧义: 是 E(H2) 还是二分之一 E(H2)? 必须写成二分之一 E(H2)(Ch5 的 191 行有同样问题).
  否则吸附能的数值解释会差一倍.

- 1H-beta-beryllene 是单面氢化, 有净偶极: 请说明是否加了偶极修正(LDIPOL 与 IDIPOL), 否则能量与功函不可靠.
- 236-238 说 bcc Be predicted at high pressure but has not been conclusively
  observed experimentally, 这句话写得很好, 正是 examiner 要的区分实验与理论. 请把这种标注推广到全章(例如在表格里加一列
  status: experimental / predicted / this work).

- 417, 419, 421 表格里 2H-beta-beryllene 的晶格矢量夹角 133 度, a = b = 2.590 埃, 属菱形畸变胞; 而 SI 的
  project_3_SI.tex: 152 与 170-172 提到 distorted hexagonal cells. 请确认正文中的 distorted
  hexagonal 与 rhombic 用词一致, 并说明为何氢化会导致如此大的角度畸变(133 度与 120 度差 13 度).

#### 3.6 Chapter 7(pp.217–220)★★★

现状 1,175 词 / 4 页, 通篇为各章总结加方向罗列.

措施: 新增两节:

- (1)Limitations of the present approach(E2-8), 逐项列出: 交换关联泛函(PBE 的自相互作用误差与带隙低估,
  HSE06 仍是近似, mu 是经验参数); 独立粒子近似光学响应(忽略激子效应, 局域场效应, 电子-空穴相互作用, 因此吸收边与谱重可能不准);
  声子与热力学(简谐近似, 未含温度效应与声子-声子相互作用); AIMD(时长约 5.5 ps 与超胞尺寸有限, 只能说明短时热稳定性);
  超导(Migdal-Eliashberg 的绝热近似与 mu 不确定性导致 Tc 有系统性误差); 拓扑(仅用宇称判据计算体不变量, 未做边缘态或输运验证;
  SOC 能隙很小意味着拓扑态只在极低温可观测); 稳定性(未评估动力学势垒与衬底效应, 故不能推断可合成性); 未考虑应变, 缺陷, 衬底, 覆盖度, 温度对带隙的影响.

- (2)Experimental status of the predicted systems(E2-8 明确要求), 用一张表区分已被实验表征与纯理论预测:

| 体系 | 实验状态 | 依据 |
| --- | --- | --- |
| 石墨烯, hcp Be, bcc Be(高压) | 实验已证实 | 文献 |
| 硼烯 beta12 与 chi3 | 实验已合成 | zhong2017metastable, ranjan2019freestanding |
| BC3 与 B4C3 单层 | BC3 已合成; B4C3 仅理论 | yanagisawa2004phonon, tian2019 |
| 块体 o-B14 | 仅理论预测 | han2023superconducting |
| alpha 与 beta-beryllene | 理论预测加近期实验报道 | chahal2023beryllene |
| 本文预测: 单层 o-B14 磁性, H 端双层超导, 立方三层 beryllene | 纯理论预测, 未实验证实 | 本论文 |

- (3)未来展望改为问题到具体改进到预期收益(E2-9), 例如: GW + BSE 用于修正带隙与激子效应, 预期把 2H-alpha-beryllene
  的吸收边从 PBE 值上移约 1 eV 量级, 使光学预测可与实验比较; 非简谐声子与声子线宽用于判断小虚频是数值噪声还是真实失稳, 直接回应 Ch5
  的声子争议; NEB 或势垒计算加衬底外延关系用于评估可合成性, 把 dynamically stable 推进到 synthesizable;
  纳米带边缘态与拓扑输运用于验证 Z2 的物理后果, 把体不变量的论断升级为可观测预言; 电声耦合与各向异性 Eliashberg 的收敛性研究用于收紧 Tc
  的不确定度.

#### 3.7 前后置材料与其他

- (1)publications.tex: 52-55: 修好悬空的 authorship attribution statements above(见 G4).
- (2)ai.tex: 目前只声明使用了 OpenAI ChatGPT. 如果你把本文件(以及其他模型的 assistance/*.md)中的建议纳入论文,
  建议如实更新该声明, 说明使用的工具范围与用途(语言润色, 结构建议, 代码与 LaTeX 排错), 并保持原有的作者对内容负全责表述. 这是合规问题,
  请自行判断学校要求.

- (3)各章的 Data availability statement 与 Supplementary information 被编成了带编号的小节(TOC
  中的 4.6/4.7, 5.6/5.7, 6.6/6.7). 期刊格式的痕迹较重, 建议改为不带编号的小节或统一放到论文层面的附录说明.

- (4)src/outlook.tex, src/methods.tex, src/results.tex 是空壳或占位文件(在 thesis.tex
  里被注释掉了). 建议删除以免误编译.

- (5)appendix.tex 目前只是 GitHub 仓库清单, 需要改造成真正的附录来承接从 Ch2 与 Ch3 移出的推导(注意 thesis.tex
  中 appendix 是被注释掉的, 需要启用以获得 A/B/C 编号).

- (6)图表编号一致性: figures_ch3/ 下的文件名是 `3.1_`, `4.1_` 到 `4.5_`, 与实际的图 3.1–3.6 不对应(像是旧章节规
  划的残留).
  改名以免日后混淆.

#### 3.8 补充: 深度审计的额外量化证据

以下数据来自对 `src/fundamentals_a.tex`(3152 行), `src/fundamentals_b.tex`(1164 行),
`src/project_1_main.tex`(722 行), `src/project_1_SI.tex`(321 行)的逐行审计, 可作为改写时的施工图.

(A) Ch2/Ch3 的内容构成(用于 G2 的删减决策)

- |(a) 通用教科书推导, 与 Ch4–6 计算无关 Ch2: 3152 行(100%, 74 页) Ch3: 约 416 行(36%, 约 11.4 页) 合计: 约
  81% 的 106 页

- |(b) 真正实用的计算方法 Ch2: 3 行(仅 HSE06 的 a=0.25, omega=0.11 bohr^-1, L3114-3116) Ch3: 0 行
  合计: 约 0.07%

- |(c) 光学量形式推导 Ch2: 0 Ch3: 约 748 行(约 19.6 页) 合计: 约 18%

> examiner 要的 (b), 在 4316 行里只有 3 行. 这不是"写得不够好", 而是"完全没写".

可优先删减或移入附录的重复推导(已逐条定位):

- |D1 重复内容: Thomas–Fermi 动能泛函推导两次; von Weizsäcker 修正两次 位置: L1052-1062 / L1662-1936;
  L1064-1071 / L2022-2028

- |D2 重复内容: 带 Lagrange 乘子的 Euler–Lagrange 极小化两次 位置: L1001-1012 / L1611-1639
- |D3 重复内容: 密度算符与单体密度定义 四次 位置: L444-449, L461-465, L1085-1088, L1163-1169
- |D4 重复内容: Born–Oppenheimer 哈密顿量两次 位置: L299-310 / L625-632
- |D5 重复内容: SCF 循环描述两次 位置: L2731-2735 / L2962-2967
- |D6 重复内容: Kohn–Sham 的两种变分推导(文中自承是 complementary) 位置: L2501-2658 / L2659-2717
- |D7 重复内容: HK 唯一性证明与 HK 变分原理挤在同一 449 行小节 位置: L1217-1305 / L1592-1660
- |D8 重复内容: eps_ab = delta_ab + chi_ab 定义两次 位置: `fundamentals_b` L206-210 /
  L612-617

- |D9 重复内容: 一般非局域本构关系推导两次 位置: `fundamentals_b` L151-176 / L572-604
- |D10 重复内容: 面内与面外分解引入两次 位置: `fundamentals_b` L269-289 / L504-524
- |D11 重复内容: N^2 = eps 两次 位置: `fundamentals_b` L841-844 / L938-942
- |D12 重复内容: 由因果时域核得到 chi(omega) 两次 位置: `fundamentals_b` L180-188 / L622-629
- |D13 重复内容: 实部等于色散, 虚部等于吸收, 重复 4 次 位置: `fundamentals_b` L361-365, L691-694,
  L719-722, L760-763

- |D14 重复内容: 复介电函数定义重复 3 次 位置: `fundamentals_b` L351-356 / L373-378 / L509-514
- |D15 重复内容: 电荷连续性方程在 Ch2 与 Ch3 各推一次 位置: `fundamentals_a` L505-536 /
  `fundamentals_b` L67-76

- |D16 重复内容: 光学激发形式被拆在两章(Ch2 L878-937 与 Ch3 L402-498 重叠约 60 行), 且互不引用 位置: —

(B) Ch2/Ch3 的图表实况: Ch2 只有 1 张示意图, 0 张表(`figure_HK_variational`, L1602-1607); Ch3 有 6
张图(全部是 alpha/beta-beryllene 结果图, 见 G6), 0 张表. 两章合计 310 个编号公式.examiner 说课本式,
这是量化依据——说明手段几乎全是公式, 而不是图表.

(C) Chapter 4 被点名的 8 张图, 实际结构(写题注的关键信息)

- 图 4.29–4.36 全部位于 `project_1_SI.tex`, 全部是 `width=0.85\textwidth` 的单栏图, 没有任何
  `\subcaption` 或 `\subfigure`, 图中也没有 (a)(b)(c) 面板字母.

- 每张都是 3x3 = 9 面板的网格, 源图 1728x1296 pt, 缩放到 0.85\textwidth(约 370 pt)后缩放比约 0.21,
  每个面板只印成约 4.3 cm x 3.2 cm. 这就是字号塌到 2.56 pt 的原因.

- 九面板内部标题(写题注可直接引用): 4.29/4.30/4.31 为 `in-plane`, `yy-component`, `out-of-plane`
  (上排), `xy-component`, `yz-component`, `zx-component`(中排), `yx-component`,
  `zy-component`, `xz-component`(下排); 4.32–4.36 为同样九个分量面板.

- 图例: 4.29 为 `Real part (PBE)`, `Imaginary part (PBE)`, `Real part (HSE06)`,
  `Imaginary part (HSE06)`(x 轴 `Photon energy (eV)`, 0–25 eV); 4.30 与 4.31 同上但
  HSE06 标注为 `(HSE06 17 k-points)`; 4.32–4.36 为 `Graphene-BC3`,
  `Graphene-Borophene`, `Graphene-B4C3` 三条曲线, 图内标题显示为 HSE06 结果.

- 主文对应图(4.9/4.10/4.11)分别只有 4/6/6 面板且用 0.8–1.0\textwidth, 所以 SI 这 8
  张是面板更多加宽度更小的最坏组合, 这解释了 examiner 为何恰好挑中这几张.

- 标签命名不一致: Ch4 用裸标签(`fig1.x`, `S1.x`), Ch5/Ch6 用 `fig:` 前缀; `S1.7` 与 `S1.8` 被跳过(未定义)
  , SI 正文从 `\ref{S1.4}--\ref{S1.6}` 直接跳到 `\ref{S1.9}--\ref{S1.11}`. 没有断引用,
  但建议统一命名规范.

- Ch4 全章 36 张图, 其中 35 张多面板, 而 `novelty`, `limitation`, `hypothesis`,
  `research question`, `future work` 全部搜不到任何出现——这正是 Examiner 1 说 Ch4 增量有限的文本原因.

---

### 4. 可直接粘贴的英文文本

> 以下 LaTeX 片段按最小侵入原则写成, 可直接插入对应文件. 请自行核对 `\cite` key 是否已在 `thesis.bib` 中.

#### 4.1 Chapter 1: 研究 gap, 主线论证, 拓扑与光学动机

(a) 研究 gap 与本文定位(建议作为 Ch1 新增一节的开头)

```latex
\section{Research gap and the position of this thesis}
\label{sec:research_gap}

Research on light-element two-dimensional materials has advanced rapidly, but it
has
largely proceeded along separate lines. Boron-based sheets have been studied
mainly
for their structural diversity and metallicity, beryllium-based sheets for their
predicted Dirac-like dispersions and thermal transport, and van der Waals
heterostructures for interfacial charge transfer. What has not been examined
systematically is whether these apparently unrelated systems share a common
structure--property mechanism. In all three cases the atomic-scale bonding
topology,
rather than the chemical identity of the constituent element, controls the
low-energy
electronic structure and therefore the collective excitations.

Three specific gaps motivate the work presented here. First, the electronic and
optical consequences of stacking graphene with boron-based monolayers have not
been
mapped for a consistent set of structurally related partners, so it is unclear
which
interfacial degrees of freedom survive van der Waals coupling. Second, the
two-dimensional derivatives of recently predicted boron allotropes, and the
effect of
hydrogen termination on them, have not been characterised with respect to
magnetism,
superconductivity and anisotropic optical response within a single structural
family.
Third, elemental beryllium has only recently been realised experimentally in
two-dimensional form, and its behaviour under hydrogen functionalisation and its
topological classification remain largely unexplored.

This thesis addresses these gaps through one central question: how does bonding
topology at the atomic scale govern the electronic structure, the collective
optical
response, and the emergence of correlated and topological states in
light-element
two-dimensional systems? The question is addressed along three complementary
routes,
which correspond to the three results chapters of this thesis.
Chapter~\ref{cha:project_bilayers}
tests the engineered limit, in which the bonding topology is modified by van der
Waals
stacking. Chapter~\ref{cha:project_boron} tests the intrinsic limit, in which
dimensionality reduction and hydrogen termination modify an existing boron
network.
Chapter~\ref{cha:project_beryllene} tests the light-element extreme, in which a
different element is combined with hydrogen functionalisation and examined for
topological order. Together, these routes support a single conclusion: in
light-element
systems, simple constituents can produce complex quantum behaviour when their
atomic
structures are organised in low-dimensional forms.

```

(b) 为何三章属于同一篇论文

```latex
The three studies are connected not by a common material but by a common
mechanism.
In each case the quantity that changes between the systems compared is a
structural
one: the stacking registry, the number of layers, or the surface termination. In
each
case the quantity that responds is the same one: the distribution of electronic
states
near the Fermi level, and hence the dielectric response. The studies therefore
constitute a controlled sequence of structural perturbations applied to
light-element
bonding networks, rather than a collection of unrelated material case studies.

```

(c) 拓扑的物理动机(必须放在引入宇称计算之前)

```latex
A non-trivial $\mathbb{Z}_{2}$ invariant has a direct physical consequence. In a
two-dimensional insulator with time-reversal symmetry, a non-trivial invariant
requires
the existence of gapless edge states inside the bulk gap. These states are
spin-momentum locked, so that elastic backscattering by non-magnetic disorder is
forbidden, and they occur in Kramers pairs related by time-reversal symmetry.
The
invariant is defined only when the bulk is gapped, because it is computed from
the
parity eigenvalues of the occupied states at the time-reversal invariant
momenta, which
requires a well-defined separation between occupied and unoccupied manifolds. In
light-element systems the spin--orbit interaction is weak, so the topological
gap is
expected to be small; nevertheless, a non-trivial invariant can arise from
lattice
symmetry and orbital character rather than from strong spin--orbit coupling.
This
distinction motivates the parity analysis used in
chapter~\ref{cha:project_beryllene},
where the magnitude of the spin--orbit-induced gap determines whether the
invariant is
well defined and whether the resulting edge states could be observed.

```

(d) 光学量的物理动机(替换罗列式写法)

```latex
The optical quantities calculated in this thesis are not reported as a standard
set of
outputs; each addresses a specific question. The imaginary part of the
dielectric
function, $\varepsilon_{2}(\omega)$, identifies which interband transitions are
opened
or suppressed by a structural modification. The real part,
$\varepsilon_{1}(\omega)$,
determines the screening response, and its sign change identifies the energy
windows in
which collective plasmonic excitations are supported. The absorption coefficient
$\alpha(\omega)$ converts this response into an attenuation length, which is the
quantity relevant to optoelectronic applications, and its directional dependence
indicates whether absorption can be controlled by polarisation. The reflectivity
$R(\omega)$ establishes whether a system could function as a reflective
plasmonic
element, while the energy-loss spectrum
$L(\omega)=-\mathrm{Im}\,[1/\varepsilon(\omega)]$
isolates the collective excitation channels and can be compared directly with
electron energy-loss spectroscopy. Read together, these quantities map the
structure--property relationships that link bonding topology to optical
function.

```

(e) 明确区分新预言与已知结构的表征(Examiner 1 开篇即要求)

```latex
It is important to distinguish the genuinely new predictions of this thesis from
the
characterisation of structures that have been proposed or observed previously.
The
cubic trilayer beryllene phase reported in chapter~\ref{cha:project_beryllene}
is a new
structure. The predicted magnetism of monolayer o-\ce{B14} and the
hydrogen-termination-induced superconductivity of the bilayer, reported in
chapter~\ref{cha:project_boron}, are new predictions for a previously proposed
bulk
phase. In contrast, the properties of the $\alpha$- and $\beta$-beryllene phases
and of
the graphene-based heterostructures are, where they reproduce earlier results,
confirmatory; their role in this thesis is to provide a consistent baseline
obtained
with a single set of computational settings, against which the new predictions
can be
assessed.

```

#### 4.2 Chapters 2–3: 新增计算方法路线图

建议插入 `fundamentals_a.tex` 的开头之后(或在 `thesis.tex` 中于 Ch2 之前单独 `\input` 一个
`src/methods_overview.tex`).

```latex
\section{Computational methods used in this thesis}
\label{sec:methods_roadmap}

The formal background developed in this chapter and in
chapter~\ref{cha:fundamentals_b}
provides the framework, but it does not by itself specify how the calculations
reported
in chapters~\ref{cha:project_bilayers}--\ref{cha:project_beryllene} were
performed.
This section therefore gives a concise, method-oriented account of the
computational
procedures used, and connects each of them to the scientific question it
addresses in
the later chapters. Detailed parameter sets are given in the methods section of
the
corresponding chapter.

\paragraph{Geometry optimisation and convergence criteria.}
All structures are relaxed within density functional theory until the residual
force on
every atom falls below a fixed threshold, and the total energy is converged to a
prescribed accuracy. Plane-wave energy cutoffs and k-point meshes are selected
on the
basis of explicit convergence tests, in which the quantity of interest---total
energy,
cohesive energy, or the dielectric function---is monitored as a function of the
parameter until it changes by less than a stated tolerance.

\paragraph{Brillouin-zone sampling.}
Metallic and semimetallic systems require dense Brillouin-zone sampling because
the
Fermi surface must be resolved; semiconductors require fewer points but need a
mesh
dense enough to locate band extrema. The dielectric function requires
substantially
denser meshes than the total energy, because it is a sum over vertical
transitions and
is therefore sensitive to the joint density of states.

\paragraph{Lattice dynamics.}
Dynamical stability is assessed from the phonon dispersion, obtained by finite
displacements in supercells of increasing size. A structure is regarded as
dynamically
stable when no phonon branch acquires a significantly imaginary frequency.
Because
small imaginary frequencies near $\Gamma$ can arise from numerical artefacts of
the
supercell and of the Fourier interpolation, the magnitude of any negative
frequency and
its dependence on supercell size are reported explicitly, and the criterion used
to
classify a structure as stable is stated.

\paragraph{\textit{Ab initio} molecular dynamics.}
Finite-temperature persistence is examined with \textit{ab initio} molecular
dynamics.
The simulation ensemble, the target temperature, the integration time step and
the total
simulation time are reported in each case. These simulations establish that a
structure
does not collapse on the simulated timescale; they do not establish
thermodynamic
stability, and they are not used as evidence of synthesizability.

\paragraph{Spin-polarised calculations and magnetic ordering.}
For systems with partially occupied states near the Fermi level, spin-polarised
calculations are performed and the non-magnetic, ferromagnetic and
antiferromagnetic
configurations are compared. The magnetic state of lowest energy is identified,
the
magnetic moments are resolved by site, and the energy differences between
competing
magnetic orders are reported together with an assessment of whether they exceed
the
accuracy of the method. The electronic state used for the subsequent optical
calculations is stated explicitly.

\paragraph{Electron--phonon coupling and superconductivity.}
Superconducting properties are obtained from density functional perturbation
theory
combined with Wannier interpolation of the electron--phonon matrix elements.
Phonon
dispersions and electron--phonon matrix elements are first computed on coarse
momentum-space grids, maximally localised Wannier functions are constructed to
reproduce the band structure in the energy window of interest, and the matrix
elements
are then interpolated onto dense grids. From these, the Eliashberg spectral
function
$\alpha^{2}F(\omega)$, the coupling strength $\lambda$ and the logarithmic
frequency
$\omega_{\log}$ are obtained, and the transition temperature follows from the
Allen--Dynes expression and from the fully anisotropic Migdal--Eliashberg
equations.
Because the Coulomb pseudopotential $\mu^{*}$ is a semi-empirical parameter, the
value
adopted and its plausible range are stated, and the sensitivity of the predicted
transition temperature to that choice is discussed.

\paragraph{Spin--orbit coupling and topological analysis.}
Spin--orbit coupling is included self-consistently for the band-structure and
parity
calculations. For inversion-symmetric systems the topological character is
determined
from the parity eigenvalues of the occupied spinor states at the time-reversal
invariant momenta, using the Fu--Kane product. Because this criterion requires a
gap
between the occupied and unoccupied manifolds, the calculated
spin--orbit-induced gap
at each time-reversal invariant momentum is reported, and the invariant is
quoted only
where such a gap exists.

```

#### 4.3 每章开头的作者贡献声明(模板)

插入位置: 每章 `\section{Abstract}` 之前(即 `\label{cha:...}` 之后).

```latex
\section*{Publication and author contributions}
\label{sec:contrib_ch4}

This chapter is based on the publication: L. Niu, O. J. Conquest, C. Verdi, and
C. Stampfl, ``Electronic and Optical Properties of 2D Heterostructure Bilayers
of
Graphene, Borophene and 2D Boron Carbides from First Principles'',
\textit{Nanomaterials}
\textbf{14}, 1659 (2024), \textsc{doi}: 10.3390/nano14201659.

The candidate (L. Niu) performed all first-principles calculations, carried out
the
data analysis, produced all figures, and wrote the manuscript. O. J. Conquest
contributed to the design of the calculation workflow and to the interpretation
of the
electronic-structure results. C. Verdi contributed to the analysis of the
optical
response and to the discussion of the hybrid-functional results. C. Stampfl
supervised the project, defined the research direction, and revised the
manuscript.
The text presented in this chapter has been reformatted for the thesis, and the
supporting calculations reported in the supplementary information have been
extended
beyond those in the published article.

```

> Ch5 与 Ch6 请照此改写(Ch6 尚未投稿, 开头应写 This chapter is based on a manuscript in
> preparation 并说明状态).

同时修正 `src/publications.tex`: 在 `\subsection*{Authorship attribution statement}`
(L52)之前补上逐篇贡献表, 否则 statements above 依然落空:

```latex
\subsection*{Authorship attribution statements}

\noindent\textbf{Chapter 4} (published in \textit{Nanomaterials} \textbf{14},
1659 (2024)):
L. Niu performed the calculations, analysis and figure preparation, and drafted
the
manuscript; O. J. Conquest and C. Verdi contributed to the methodology and
interpretation; C. Stampfl supervised the work and revised the manuscript.

```

#### 4.4 Chapter 3: 图片来源声明(G6 方案 B)

在 3.2.3 节图 3.1 之前插入一次总声明, 并在 3.4 节各图处用一句话呼应:

```latex
The spectra shown in figures~\ref{figure_representative_dielectric_response} and
\ref{absorption_coefficient_present_systems}
to\ref{energy_loss_spectrum_alpha_beta_beryllene}
are the author's own first-principles results for $\alpha$- and
$\beta$-beryllene. They
are used here to illustrate the optical quantities defined in this chapter, and
are
presented and discussed in full in chapter~\ref{cha:project_beryllene},
section~\ref{3_optical_alpha_beta}. The computational settings are those given
in
section~\ref{3_methods}.

```

并删除 `src/fundamentals_b.tex:530` 的 `% cite my third project here`.(更推荐方案 A: 把这 6
张图与 6 段结果讨论整体搬进 Ch6.)

#### 4.5 Chapter 4: 图 4.29–4.36 题注重写

通用要求: 每条题注都要自带 (1) 体系与面板集合 (2) 张量分量 (3) 曲线颜色线型 (4) PBE 与 HSE06 (5) 偏振方向约定 (6) 单位
(7) 最值得注意的特征. 另外建议在图内加 (a)–(i) 面板字母, 并把 3x3 拆成 2 张图(对角分量与非对角分量)以解决字号问题.

(i) 图 4.29(= `\label{S1.17}`)

```latex
\caption{Components of the frequency-dependent dielectric tensor
$\varepsilon_{\alpha\beta}(\omega)$ of the Graphene-Borophene bilayer, obtained
with
the PBE and HSE06 functionals. The nine panels show the diagonal in-plane
components
$\varepsilon_{xx}$ (panel a, labelled ``in-plane'') and $\varepsilon_{yy}$
(panel b),
the out-of-plane component $\varepsilon_{zz}$ (panel c), and the six
off-diagonal
components $\varepsilon_{xy}$, $\varepsilon_{yz}$, $\varepsilon_{zx}$,
$\varepsilon_{yx}$, $\varepsilon_{zy}$ and $\varepsilon_{xz}$ (panels d--i). In
each
panel, solid lines denote the real part and dashed lines the imaginary part; PBE
results
are shown in one colour and HSE06 results in another, as indicated in the
legend. The
photon energy is given in electronvolts and $\varepsilon_{\alpha\beta}$ is
dimensionless. The in-plane and out-of-plane diagonal components differ
substantially,
which demonstrates the optical anisotropy of the heterostructure, whereas all
six
off-diagonal components remain negligible, as expected for this stacking
geometry.}
\label{S1.17}

```

(ii) 图 4.30(= `\label{S1.18}`)

```latex
\caption{Components of the frequency-dependent dielectric tensor
$\varepsilon_{\alpha\beta}(\omega)$ of the Graphene-\ce{BC3} bilayer, obtained
with the
PBE and HSE06 functionals. Panels and line conventions follow
figure~\ref{S1.17}: the
diagonal in-plane components $\varepsilon_{xx}$ and $\varepsilon_{yy}$, the
out-of-plane
component $\varepsilon_{zz}$, and the six off-diagonal components. The photon
energy is
given in electronvolts. The HSE06 spectra were obtained with a
$17\times17\times1$ k-point mesh, as indicated in the legend; the PBE spectra
use the
denser mesh given in section~\ref{1_calculation_methods}. In contrast to
figure~\ref{S1.17}, the off-diagonal components remain finite over a range of
energies
and satisfy the antisymmetric relations $\varepsilon_{yx}=-\varepsilon_{xy}$,
$\varepsilon_{yz}=-\varepsilon_{zy}$ and $\varepsilon_{zx}=-\varepsilon_{xz}$,
which
reflects the reduced $\mathrm{P}3$ space-group symmetry of this
heterostructure.}
\label{S1.18}

```

(iii) 图 4.31(= `\label{S1.19}`) —— 结构同上, 把体系换成 Graphene-B4C3, 并在末句点出非对角分量显著,
可能对应旋光或手性响应.

(iv) 图 4.32–4.36(= `\label{S1.20}`–`\label{S1.24}`) —— 五张图结构相同, 用同一条模板, 只改量名,
单位与最值得注意的特征:

```latex
\caption{[Absorption coefficient $\alpha(\omega)$ / Energy-loss spectrum
$L(\omega)$ / Refractive index $n(\omega)$ / Reflectivity $R(\omega)$ /
Extinction coefficient $k(\omega)$] of the Graphene-Borophene,
Graphene-\ce{BC3} and Graphene-\ce{B4C3} bilayer heterostructures, obtained with
the
HSE06 functional. The nine panels show the in-plane components
($\varepsilon_{xx}$ and
$\varepsilon_{yy}$), the out-of-plane component ($\varepsilon_{zz}$), and the
six
off-diagonal tensor components, following the panel convention of
figure~\ref{S1.17}. Each panel contains one curve per heterostructure, as
indicated in
the legend. The photon energy is given in electronvolts and the quantity is
given in
[cm$^{-1}$ / dimensionless]. The principal feature is [the plasmon-related
maximum near
X eV in the in-plane channel / ...].}
\label{S1.20}

```

> 注: 请把方括号内容替换为实际数值. 若图 4.32–4.36 确为 HSE06 结果(图内标题显示 by HSE06), 题注必须写明; 若混有 PBE 结果,
> 请分别标注.

#### 4.6 Chapter 5: 修正文本

(a) 声子虚频(统一主文与 SI 的口径) —— 替换 `project_2_main.tex:499-506`:

```latex
For the hydrogen-terminated systems, the behaviour is different. The
hydrogen-terminated monolayer exhibits imaginary frequencies across a wide
region of
the Brillouin zone and is therefore dynamically unstable; it is not considered
further.
The hydrogen-terminated bilayer shows only small negative frequencies in the
vicinity of
the $\Gamma$ point, with a minimum value of approximately [X]~cm$^{-1}$ for a
$(3\times3)$ supercell, compared with [Y]~cm$^{-1}$ for a $(2\times2)$
supercell. Since
frequencies of this magnitude are comparable to the numerical accuracy of the
finite-displacement approach and are commonly reported for two-dimensional
materials~\cite{liu2016continuum,querne2023crystal,pallikara2022physical}, we
regard
this structure as dynamically stable, but we note that the residual negative
frequency
is not fully converged with respect to supercell size.

```

(b) 光学计算所用的电子态与磁态 —— 在 5.4.4 节开头(`project_2_main.tex:661` 之前)插入:

```latex
Before discussing the optical response, we specify the electronic and magnetic
state
used for the dielectric-function calculations, because the monolayer supports
several
low-energy states that differ in their electronic character. The optical spectra
were
obtained from [non-spin-polarised / spin-polarised antiferromagnetic]
calculations
using the [PBE / HSE06] functional, and the interband transitions were evaluated
within
the independent-particle approximation. [Intraband (Drude) contributions were
included
using a broadening of X eV. / No intraband contribution was included.]
Consequently,
the low-energy response of the monolayer reported below corresponds to the
[non-magnetic metallic / antiferromagnetic semiconducting] state, whereas the
antiferromagnetic ground state discussed in
section~\ref{xene_ob14_electronic_properties}
has a band gap of \qty{0.105}{\electronvolt}.

```

> 请把方括号替换为实际设置. 这段是回应 Examiner 1 第 6 条的核心, 不能省略.

(c) AIMD 不得称为 thermodynamic stability —— 替换 `project_2_main.tex:507-509`:

```latex
We also performed \textit{ab initio} molecular dynamics simulations for the
hydrogen-terminated bilayer in the [NVT] ensemble at \qty{400}{K}, with a time
step of
[X]~fs and a total simulation time of [Y]~ps, as shown in figure~\ref{S2.10}.
The total
energy fluctuates about a constant average and the structure retains its bonding
framework throughout. This demonstrates short-time thermal persistence at the
simulated
temperature; it does not by itself establish thermodynamic stability, nor does
it
establish that the structure is synthesizable, both of which would require the
evaluation of free energies and of kinetic barriers.

```

(d) AFM–FM 能量差 —— 在 `project_2_main.tex:543` 处补充:

```latex
The antiferromagnetic configuration is lower in energy than the ferromagnetic
configuration by \qty{0.02}{\electronvolt} per unit cell. Because this
difference is
small, we verified that it is robust with respect to the choice of functional
([PBE / HSE06]) and of k-point mesh, and we report both values. The
antiferromagnetic
state opens a band gap of \qty{0.105}{\electronvolt}, whereas the non-magnetic
state is
metallic; the non-magnetic state therefore lies higher in energy but is close
enough
that the magnetic ordering may be sensitive to temperature.

```

> 请填入实际原子数与每个原子的能量差, 并给出两种泛函的对比结果.

(e) 超导: 补齐 omega_log 与 alpha^2F(omega), 并说明 Tc 出处 —— 建议在 `project_2_main.tex:630`
附近改写:

```latex
The Eliashberg spectral function $\alpha^{2}F(\omega)$ and the integrated
electron--phonon coupling $\lambda(\omega)$ are shown in
figure~\ref{fig:ob14_alpha2f}
for bulk o-\ce{B14} and for the hydrogen-terminated bilayer. The calculated
coupling
strengths are $\lambda = 0.931$ for the bulk and $\lambda = 1.01$ for the
hydrogen-terminated bilayer, with logarithmic frequencies
$\omega_{\log} = [X]$~K and $[Y]$~K, respectively. The Allen--Dynes expression
gives
$T_c = \qty{28.2}{K}$ for the bulk and $T_c = \qty{18.5}{K}$ for the
hydrogen-terminated bilayer, whereas the fully anisotropic Migdal--Eliashberg
calculation gives $T_c = \qty{31.3}{K}$ and $T_c = \qty{24.3}{K}$. The values
quoted in
the abstract and in the conclusions of this chapter are the Migdal--Eliashberg
values;
the Allen--Dynes values are systematically lower because they neglect the
anisotropy of
the gap. The monolayer gives $\lambda = 0.05$ and a negligible $T_c$.

```

(f) 内聚能参考相 —— 扩写 `project_2_main.tex:429-433`, 把参考相写全(alpha-B12 基态, beta-B, beta12
与 chi3 二维相, 以及本文的 bulk o-B14 与 alpha'-monolayer), 并复核结论 `:815-816` 中双层比块体稳定 0.19
eV 的说法. 若仍成立, 请写明计算条件完全一致; 若不成立, 请改正.

(g) 吸收系数的指代 —— 改写 `project_2_main.tex:740`, 指明体系, 方向与所用约定(并考虑同时给出吸光度 A(omega), 见
G8).

#### 4.7 Chapter 6: 修正文本

(a) Z2 与金属性的相容性(最重要) —— 在 `project_3_main.tex:524` 之后插入:

```latex
The parity criterion of Fu and Kane requires a gap between the occupied and
unoccupied manifolds at every time-reversal invariant momentum, because the
invariant is
defined from the parity eigenvalues of the occupied states. We therefore
examined the
spin--orbit-coupled band structure of cubic trilayer beryllene at each
time-reversal invariant momentum separately. [The scalar-relativistic PBE band
structure is metallic, but the inclusion of spin--orbit coupling opens a gap of
[X]~meV at $\Gamma$ and of [Y]~meV at $\mathrm{M}$ and $\mathrm{X}$, so that the
occupied manifold is separated from the unoccupied manifold at all four
time-reversal invariant momenta and the invariant is well defined. / The
spin--orbit-coupled band structure remains gapless at [which momenta], so the
parity
product does not define a topological invariant for this phase; the calculated
parity
products are reported only as an indicator of band inversion and are not
interpreted as
a $\mathbb{Z}_{2}$ invariant.]

```

并在表中补齐 X(与 Y)点的宇称本征值, 并修正题注用词(当前把 Gamma 与 M 的单个宇称值称为 parity products).

(b) SOC 的表述 —— 替换 `project_3_main.tex:957-959`:

```latex
This result shows that a non-trivial topological phase can arise in a
light-element
system, where the spin--orbit interaction is weak. Spin--orbit coupling is
nevertheless
essential to the analysis, because it is what separates the occupied and
unoccupied
manifolds and thereby makes the invariant well defined; the relevant energy
scale is the
spin--orbit-induced gap of [X]~meV, which is small and implies that the
topologically
protected states would be observable only at low temperature.

```

(c) HSE06 的取舍理由 —— 插入 6.3 节末尾:

```latex
The band structures and optical spectra presented in this chapter were obtained
with the
PBE functional. Two considerations motivate this choice. First, the optical
response of
the metallic phases, which dominate the discussion, is governed by the joint
density of
states near the Fermi level and by the plasma frequency; these quantities are
insensitive to the self-interaction error that affects PBE band gaps, whereas
the
position of an absorption edge in a semiconductor is not. Second, a
hybrid-functional
optical calculation would require a $105\times105\times1$ k-point mesh, which is
prohibitively expensive. The limitation of this choice is most significant for
2H-$\alpha$-beryllene, which is a semiconductor with a PBE gap exceeding
\qty{4.0}{\electronvolt}; because PBE underestimates band gaps, the calculated
absorption onset for this phase should be regarded as a lower bound. [A
hybrid-functional
band gap of [X]~eV was obtained for this phase in order to quantify the
correction.]

```

(d) 收敛性讨论 —— 在 6.3 节中把 SI 的数值上移:

```latex
Convergence was assessed separately for the total energy, the cohesive energy,
and the
dielectric function. The cohesive and total energies converge for k-point meshes
of
$27\times27\times1$ (hexagonal cells) and $25\times25\times1$ (cubic cells), as
shown in
figures~\ref{fig:proj3_cohesive_energy_convergence} and
\ref{fig:proj3_total_energy_convergence}. The dielectric function is
considerably more
demanding because it is a sum over vertical transitions, and a mesh of
$105\times105\times1$ is required for convergence over the
$0$--\qty{10}{\electronvolt}
range. The number of unoccupied bands was converged independently, giving 140
bands for
the hydrogen-functionalised structures, 133 for the pristine two-dimensional
structures,
70 for bulk bcc beryllium and 66 for bulk hcp beryllium. The two parameters were
converged separately, and the criterion adopted was that the real and imaginary
parts of
$\varepsilon(\omega)$ change by less than [X]\% over the energy range of
interest.

```

(e) 氢功能化的选取理由 —— 插入 `project_3_main.tex:301` 之后:

```latex
The choice of hydrogenation geometries reflects the symmetry of each phase.
Monolayer
$\alpha$-beryllene is planar and possesses a mirror plane; single-sided
hydrogenation
would break that symmetry and produce a net out-of-plane dipole, so only the
double-sided configuration is considered. Bilayer $\beta$-beryllene possesses
two
inequivalent surfaces, so both single-sided and double-sided terminations are
physically distinct and both are examined. The cubic trilayer structure is not
hydrogenated, because [its outer layers are coordinatively saturated and no
stable
adsorption configuration was found / this case was not considered and is
identified as
future work]. The rationale for treating the three phases differently is
therefore
structural rather than arbitrary.

```

(f) AIMD 参数 —— 替换 `project_3_main.tex:356-360` 的开头:

```latex
We further examine the finite-temperature behaviour of the
hydrogen-functionalised
structures using \textit{ab initio} molecular dynamics in the [NVT] ensemble at
\qty{[300]}{K}, with a time step of [X]~fs and a total simulation time of
[Y]~ps.

```

并在图 `fig:proj3_hydrogenated_aimd` 的题注中重复这些参数.

(g) 新结构的构造方法 —— 建议在 6.4.1 节增加一段(示例框架):

```latex
The cubic trilayer structure was obtained by [cutting three (001) layers from
the bulk
body-centred cubic lattice / enumerating stacking sequences of three hexagonal
layers /
...], followed by full relaxation without symmetry constraints. We also
considered the
two-layer and four-layer cubic sequences and graphene-like beryllium layers
containing
one to four layers; all of these were found to be dynamically unstable from
their phonon
dispersions, as shown in figure~\ref{fig:proj3_rejected_structures}, and are
therefore
not discussed further. The trilayer is the only member of this family that
satisfies both
the energetic and the dynamical criteria.

```

> 请补上真实来源与筛选流程; 若确实做过枚举, 建议给出枚举数量与判据.

#### 4.8 Chapter 7: 局限性一节草稿

```latex
\section{Limitations of the present approach}
\label{sec:limitations}

The predictions reported in this thesis are subject to several limitations that
should
be borne in mind when assessing their significance.

\textit{Exchange--correlation treatment.} The structural, electronic and optical
properties are obtained within density functional theory. The PBE functional
underestimates band gaps through self-interaction and delocalisation errors, and
the
HSE06 hybrid functional, although more accurate for gaps, remains an
approximation and
is applied only to selected systems for reasons of cost. The Coulomb
pseudopotential
$\mu^{*}$ entering the Migdal--Eliashberg calculations is a semi-empirical
parameter,
so the predicted transition temperatures carry a systematic uncertainty that is
not
reflected in the quoted values alone.

\textit{Independent-particle optical response.} The dielectric functions are
calculated
within the independent-particle approximation. Excitonic effects, electron--hole
interaction and local-field corrections are neglected. This is expected to
affect the
position and weight of absorption features, particularly near absorption edges
and in
the semiconducting phases, so the reported spectral features should be regarded
as
uncorrected independent-particle results.

\textit{Lattice dynamics and thermal effects.} Dynamical stability is assessed
within
the harmonic approximation, and the phonon dispersions do not include
temperature-dependent renormalisation or phonon--phonon broadening. Small
imaginary
frequencies near $\Gamma$ are sensitive to supercell size, and the
classification of a
structure as dynamically stable therefore depends on the criterion adopted.

\textit{Molecular dynamics.} The \textit{ab initio} molecular dynamics
simulations are
limited in system size and duration. They demonstrate that the structures do not
collapse on the simulated timescale at the simulated temperature, but they
cannot
establish thermodynamic stability or exclude slow diffusion or reconstruction
events
that occur on longer timescales.

\textit{Stability versus synthesizability.} Energetic preference relative to a
chosen
set of reference phases, dynamical stability and short-time thermal persistence
are
necessary but not sufficient conditions for experimental realisation. Kinetic
barriers,
substrate interactions, growth kinetics and oxidation are not considered here,
so no
claim about synthesizability is made.

\textit{Topological analysis.} The topological classification relies on the
parity
criterion, which requires a gap at the time-reversal invariant momenta. The
associated
spin--orbit-induced gaps are small, and no edge-state or transport calculation
is
performed, so the predicted topological character is a statement about the bulk
invariant rather than about an observable edge conductance.

\textit{Effects not included.} Strain, defects, substrate interaction, hydrogen
coverage
and temperature dependence of the band structure are not investigated, although
each of
them is known to modify the properties of two-dimensional materials.

```

再补一节实验状态表(见 3.6 节).

---

### 5. 优先级, 工作量与依赖关系

- |1 任务: 处理 Ch3 的 6 张 alpha/beta-beryllene 图(移入 Ch6 或加来源声明); 删 `:530` TODO 对应意见:
  E2-2 预估工作量: 0.5 天 依赖: 无(规范性风险, 最先做)

- |2 任务: 补 3 章的作者贡献声明 + 修好 `publications.tex` 悬空引用 对应意见: E1 前言, E2-3 预估工作量: 0.5 天
  依赖: 需导师确认

- |3 任务: 重出 6 张最严重图(4.21/4.22/4.31–4.34)+ 重写 4.29–4.36 题注 对应意见: E1-4, E2-4 预估工作量:
  2–3 天 依赖: 需改 `vmatplot` 出图规范

- |4 任务: 新建方法路线图节(从 Ch4–6 上移重写) 对应意见: E1-1, E1-3 预估工作量: 2–3 天 依赖: 无新计算
- |5 任务: 写文献综述章 + Ch1 补 gap, 主线, 拓扑与光学动机 对应意见: E1-1, E1-2, E2-1 预估工作量: 5–8 天 依赖: 需补读文献
- |6 任务: Ch5 五处矛盾修正(声子, AFM 与金属, AIMD 用词, AFM 能量差, Tc 出处) 对应意见: E1-5, E1-6 预估工作量: 2–3 天
  依赖: 需查原始输出

- |7 任务: Ch6 六处修正(Z2 辩护, HSE06 理由, 收敛上移, AIMD 参数, 氢化理由, 结构构造) 对应意见: E1-7/8, E2-6 预估工作量:
  3–5 天 依赖: 部分需补算 SOC 能隙

- |8 任务: Ch7 加 Limitations + 实验状态表 + 改写未来展望 对应意见: E2-8, E2-9 预估工作量: 1–2 天 依赖: 无
- |9 任务: 压缩 Ch2/Ch3 至约 50–60 页, 内容移入附录; 合并 16 处重复推导 对应意见: E1-1, E1-3 预估工作量: 5–8 天 依赖:
  需改造 `appendix.tex`

- |10 任务: 全篇剩余图件重出(Ch4 其余, Ch5, Ch6, 共约 66 页受影响) 对应意见: E1-4, E2-4 预估工作量: 5–8 天 依赖: 依赖第 3
  项规范

- |11 任务: 填写 `reply_to_examiners.md` 中的页码占位符 对应意见: — 预估工作量: 0.5 天 依赖: 全部改完后

建议推进顺序: 1 → 2 → 3 → 4 → 8 → 6 → 7 → 5 → 9 → 10 → 11.

理由: 先把规范性风险与零成本确定性项清掉(1–4, 8), 再做需要查数据或补算的(6, 7), 最后做最耗时的写作与重排(5, 9, 10).

---

### 6. `report/reply_to_examiners.md` 填写要点

- (1) 占位符还没填: `reply_to_examiners.md` 中大量 `x`, `y`, `page ?`, `xxxxxxxxxxxxxx`(例如第
  21, 23, 27, 29 行). 必须在提交前全部替换为真实页码与真实引文, examiner 会逐条核对.

- (2) 第 29 行 `Page ? "xxxxxxxxxxxxxx"` 是明显的未完成模板, 务必填写.
- (3) 逐条对应: Examiner 1 有 9 条编号意见, Examiner 2 有 9 条(含 Ch6 的 5 个子条). 建议为每条意见给出章节号,
  页码与一句话说明改了什么.

- (4) 不要过度承诺: 对于未做的事情(如边缘态计算, HSE06 全量光学谱), 回复里应写已在 Limitations 中明确说明, 而不是声称已解决.
- (5) 建议加一段总述, 把修改归纳为四件事: (1) 新增文献综述章; (2) 新增计算方法路线图并把 Ch2/3 的形式推导移入附录; (3)
  统一并限定稳定性, 超导与拓扑论断; (4) 全篇图件重制. 这样 Chair of Examination 能一眼看到修改的完整性.

---

### 7. 需要你确认或补充的数据/计算清单

A. 无需新计算, 只需从原始输出中取数(优先)

- (1) Ch6 AIMD 的 ensemble, 温度, 时间步, 总时长(VASP `INCAR` 与 `OUTCAR`).
- (2) Ch5 AIMD 的 ensemble, 时间步, 总时长(examiner 说是 5.5 ps, 请确认).
- (3) Ch5 氢端双层在 Gamma 点附近的最低负频数值, 以及 2x2 与 3x3 超胞的对比.
- (4) Ch5 的 omega_log(bulk 与 H-bilayer), 以及 alpha^2F(omega) 数据(用于补图).
- (5) Ch5 光学计算所用自旋态与泛函, 以及是否含带内 Drude 项与其展宽.
- (6) Ch5 单层元胞的原子数与磁性位点数(用于 AFM–FM 能量差与磁矩自洽).
- (7) Ch6 表格中 X(与 Y)点的宇称本征值.
- (8) Ch6 各相介电函数的收敛判据(变化百分比).

B. 建议补算(工作量中等, 但对回应 examiner 极有价值)

- (9) Ch6: 含 SOC 的能带结构与各 TRIM 处的能隙数值 —— 回应 Z2 与金属性冲突的关键, 最重要的一项补算.
- (10) Ch6: 2H-alpha-beryllene 的 HSE06 带隙(哪怕只算带隙不算光学谱), 用于支撑 PBE 低估, 实际更大的论断.
- (11) Ch6: 立方三层的氢吸附测试(若确实没做), 或明确写为 future work.
- (12) Ch6: 被否决的 2 层与 4 层以及石墨烯型结构的声子谱(哪怕是 SI 一张图).

C. 必须复核的既有结论(防止硬伤)

- (13) Ch5 结论 `:815-816`: 双层比块体稳定 0.19 eV. 二维比三维母体更稳定属反直觉, 请复核计算条件是否完全一致.
- (14) Ch5 内聚能参考相 —— 补 alpha-B12, beta-B 与其他二维硼相, 检验 energetic preference 是否仍成立.
- (15) Ch6 表格 133 度夹角 —— 确认 distorted hexagonal 与 rhombic 用词一致, 并确认单面氢化是否加了偶极修正(
  `LDIPOL` 与 `IDIPOL`).

- (16) 吸附能参考态 —— Ch5 `:191` 与 Ch6 `:185` 中 E_H = hydrogen atom in the H2
  molecule 必须明确为二分之一 E(H2).

D. 需要你本人决定的事

- (17) G6 的两种方案(Ch3 的 6 张图: 搬走 vs 加声明)—— 涉及你对自己数据归属的判断, 且 Ch6 尚未投稿, 建议谨慎.
- (18) `ai.tex` 是否需要扩展声明(若采纳多个模型的建议).
- (19) Ch2/Ch3 压缩到什么程度: 建议降到 50–60 页(现状 106 页). 若学校对篇幅无要求, 也可只做新增方法路线图与合并重复推导, 风险更低,
  但 examiner 的 disproportionately long 不会被完全回应.

---

### 8. 附: 精确证据索引

8.1 关键文件与行号

- |Ch3 残留 TODO 位置: `src/fundamentals_b.tex:530` — `% cite my third project here`
- |Ch3 六张 alpha/beta-beryllene 图 位置: `fundamentals_b.tex` L532-537, L865-870,
  L985-990, L1000-1005, L1085-1090, L1146-1151

- |Ch3 结果段 位置: L529-530, L863-876, L983-995, L1007-1012, L1083-1097, L1144-1161
- |悬空的作者贡献声明 位置: `src/publications.tex:52-55`
- |Ch5 声频矛盾(主文) 位置: `src/project_2_main.tex:499-506`
- |Ch5 声频矛盾(SI) 位置: `src/project_2_SI.tex:137-138`
- |Ch5 AFM 半导体与光学按金属 位置:
  `project_2_main.tex:456-458, 543-546, 690, 696-699, 707-708, 734`

- |Ch5 AIMD 误称 thermodynamic 位置: `project_2_main.tex:507-509`
- |Ch5 Tc 双值 位置: `project_2_main.tex:631-636`(Allen-Dynes)与 `653-654`
  (Migdal-Eliashberg)

- |Ch5 吸收系数指代不明 位置: `project_2_main.tex:740`
- |Ch6 Z2 与金属性 位置: 金属: `project_3_main.tex:444-445, 482-483`; Z2:
  `:601-606, 627-631`; 方法: `:523-533`

- |Ch6 X 点宇称未列表 位置: `project_3_main.tex:568-571` 与表 `:573-618`
- |Ch6 SOC 表述 位置: `project_3_main.tex:957-959` 与 `:533`
- |Ch6 AIMD 无参数 位置: `project_3_main.tex:356-362`, 题注 `:374-379`
- |Ch6 收敛只在 SI 位置: `project_3_main.tex:168-172`; 数值在 `project_3_SI.tex:53-63`
- |Ch6 氢化理由缺失 位置: `project_3_main.tex:297-301`
- |Ch6 结构构造缺失 位置: `project_3_main.tex:261-265, 281-284`
- |Ch6 图 6.2 与 6.3 无颜色说明 位置: `project_3_main.tex:248-252, 289-293`
- |Ch4 缺贡献声明 位置: `project_1_main.tex:1-7`(章首无任何声明)
- |Ch4 八条过短题注 位置: `project_1_SI.tex:270, 277, 284, 291, 298, 305, 312, 319`
- |Ch4 题注笔误 位置: `project_1_SI.tex:213`(monolayers.. 两个句点)

8.2 页码与图号对照(来自 `.output/thesis.toc` 与 `.output/thesis.lof`, 均为论文印刷页码)

| 内容 | 页码 |
| --- | --- |
| Chapter 1 Introduction | 1–4 |
| Chapter 2 Fundamentals I | 5–78 |
| Chapter 3 Fundamentals II | 79–110 |
| Chapter 4(正文 111–131, SI 132–146) | 111–146 |
| Chapter 5(正文 147–168, SI 169–180) | 147–180 |
| Chapter 6(正文 181–204, SI 205–216) | 181–216 |
| Chapter 7 Conclusion and Outlook | 217–220 |
| References | 221–239 |
| Appendix | 240– |

- |3.1–3.6 页: 93, 101, 103, 104, 106, 108 标签:
  `figure_representative_dielectric_response`,
  `absorption_coefficient_present_systems`, `refractive_index_present_systems`,
  `extinction_coefficient_alpha_beta_beryllene`,
  `reflectivity_alpha_beta_beryllene`,
  `energy_loss_spectrum_alpha_beta_beryllene`

- |5.1 页: 155 标签: `fig:ob14_atomic_structure`
- |6.1 / 6.2 / 6.3 页: 186 / 187 / 188 标签: `fig:proj3_bulk_structures` /
  `fig:proj3_pristine_2d_structures` / `fig:proj3_hydrogenated_structures`

- |4.29–4.36 页: 142, 142, 143, 143, 144, 144, 145, 145 标签: `S1.17`–`S1.24`

8.3 图件字号实测(正文 = 11.96 pt; 阈值 6 pt)

| 章 | 受影响页数 | 受影响的图 | 最小字号 |
| --- | --- | --- | --- |
| Ch2 | 0 | — | — |
| Ch3 | 6 | 3.1–3.6 | 5.7 pt |
| Ch4 | 23 | 4.2, 4.5–4.17, 4.20–4.36 | 2.1 pt |
| Ch5 | 17 | 5.2, 5.4, 5.6–5.17, 5.20–5.30 | 2.7 pt |
| Ch6 | 26 | 6.1–6.34(几乎全部) | 2.9 pt |
| 合计 | 72 页 | | |

复验方法(可自行重跑):

```python
import fitz
doc = fitz.open('.output/thesis.pdf')
p = doc[169]                      # 0-based;印刷页 142 对应 PDF 第 170 页
for b in p.get_text('dict')['blocks']:
    if b['type'] != 0: continue
    for l in b['lines']:
        for s in l['spans']:
            if s['text'].strip() and s['size'] < 6:
                print(round(s['size'], 2), repr(s['text'][:40]))

```

---

### 9. 一句话总结

这份论文的科学工作量是够的(两篇已发表加一篇将投), 两位 examiner 也都没有质疑结果本身; 问题集中在论文作为一篇论文的三件事上: 没有讲清研究
gap(Ch1 只有 990 词), 把一半篇幅给了不含方法的教科书推导(Ch2+Ch3 共 106 页而方法内容仅 3 行), 以及图完全读不了(72
页图内文字小于 6 pt). 这三件事加上若干处自相矛盾的表述(Ch5 声频与单层电子态, Ch6 的 Z2 与金属性), 构成了全部意见的实质内容.
全部修改中只有极少数需要新算力(主要是 Ch6 的 SOC 能隙), 其余都是重组, 改写与重新出图.
