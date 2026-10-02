# Fundamentals 与理论附录的编排

更新日期: 2026-10-03.

按用户最新要求, 将原 Theory fundamentals 拆成量子物理与电动力学两个附录,
并将 Chapter 4 的通用相位几何与时间反演推导迁入第三个理论附录.
原 Appendix A 的代码与数据说明移到最后, 编号为 Appendix D.
本次编排取代 2026-09-26 的两个附录结构.

## References 之后的顺序

- Appendix A: A journey of quantum physics (`src/appendix_quantum.tex`).
  收录原 B1–B4: 时间演化、多体 Schrödinger 方程、Heisenberg 表象与连续性方程,
  多体统计与约化描述, 泛函定义, Thomas–Fermi 构造及其扩展.
- Appendix B: Essential electrodynamics you needed (`src/appendix_electrodynamics.tex`).
  收录原 B5–B6: Maxwell 方程、本构关系、各向异性基础,
  因果性与全频率 Kramers–Kronig 推导.
- Appendix C: A Glimpse of topology (`src/appendix_topology.tex`).
  收录原 Chapter 4 的相位自由、Berry 相位与多带连接,
  以及 spinor、时间反演与 Kramers 配对的一般推导.
- Appendix D: Source code and data analysis (`src/appendix.tex`).
  原代码附录内容保留, 编排位置后移.

标题采用用户指定的写法.
`thesis.tex` 使用 `\appendix` 顺序编入四个文件, 沿用奇数页开章规则.
原 `src/appendix_basic.tex` 已由 A/B 两个文件替代.
原 `cha:appendix_basic` 引用按内容分别指向
`cha:appendix_quantum` 或 `cha:appendix_electrodynamics`;
拓扑基础使用 `cha:appendix_topology`, 代码附录继续使用 `cha:appendix_code`.

## 正文与附录的分工

- Chapter 2 继续从 Density functional in quantum mechanics 开始,
  保留密度泛函与 Hohenberg–Kohn 主线, Kohn–Sham, 交换关联泛函及实际计算方法.
- Chapter 3 保留工作本构关系, 介电函数的微观表达、带间/Drude 与二维归一化,
  正频率 Kramers–Kronig 关系及静态极限, 派生光学量与全部六幅自有计算例图.
- Chapter 4 保留计算所需的 spinor Bloch 描述、子空间选择、直接与间接带隙条件,
  两幅方法图、TRIM、宇称计数、Fu–Kane 判据、晶体对称性化简和实际计算解释.
  原 Berry 推导与通用时间反演证明迁入 C, 正文保留短的工作说明和明确入口.
- Introduction 的 thesis organisation 与 Chapters 2–4 的导航、前后指代同步更新.

## Berry 相位的教学补充

Appendix C 在原有公式上增加以下推导和解释:

- 绝热演化中动力学相位与几何相位的分离, 明确有限能隙与投影近似.
- 开放路径的规范端点项, 平行输运的局部相位条件与闭路相位差.
- 单带 Berry curvature、规范不变性与 Stokes 关系的适用范围.
- 一个可直接计算的两分量态例子, 从归一化态算到 connection、curvature 和闭路相位.
- 多带曲率的交换子项及其规范协变性, 衔接正文的带子空间分析.

讲解范围参考用户指定视频 [Deriving Berry phase, Berry connection & Berry curvature](https://www.youtube.com/watch?v=6xctcmwR8wo),
数学关系按 Berry (1984)、Wilczek–Zee (1984) 和 Xiao–Chang–Niu (2010) 核验,
使用现有 `berry1984quantal`、`wilczek1984appearance` 并补入 `xiao2010berry`.
叙述遵循现有正文先引入问题、再定义、推导与解释的顺序;
保留 Dirac notation、现有符号和向量间距习惯.

## Appendix C 的示意图

`figures_topo/figures_topo.ipynb` 独立生成三张矢量 PDF, 沿用 Chapter 4 的字体、
颜色、线宽与半透明白色圆角标题框; notebook 仅保留设置与绘图代码及简短标题.
画布分别为 8×4、8×4 与 7×4 inches, 正文宽度均为 0.8 textwidth.
C.1/C.2 保持相同的字体缩放比例; C.3 按用户反馈放大文字显示.
解释放在正文, caption 保持简短.

- C.1: 闭路上四个态的局部相位选择与重叠积不变性;
  橙色指针只代表额外相位, 不代表自旋方向.
- C.2: 两分量态在态球上的纬线回路与平行输运的相位因子;
  采用 theta=pi/3, 球冠固体角为 pi, Berry 相位为 -pi/2.
  正文补充态球坐标与 Pauli 期望值的对应, 保留原 theta=pi/2 算例.
- C.3: 同一平面内的两套正交基与不变投影;
  实旋转只作为酉换基的简单示意, 不将态子空间等同于晶体中的几何平面.

C.1 按用户反馈改为 2:1, 并增大态标签与底部公式字号.
三图统一使用实心 `-|>` 箭头; C.2 左图减去密集球面网格,
保留轮廓、赤道、极轴与球心, 区分回路前后的实线/虚线并标出 phi 增大方向.
C.3 补入两对基矢的同向旋转弧线、共同角度 alpha=pi/5 与两条换基公式;
正文说明换基时测试态固定, 并明确 C.2 的固体角对应青色球冠区域.
C.3 的四条基底轴沿正、负方向延伸为灰色虚线, 保留彩色单位基矢;
notebook 中用 `axis_extent` 调整延伸长度.
C.2 的固体角标注移至青色区域左下方, 橙黄色半径与极角弧线位于蓝色回路
及青色区域的下层.
C.2 的 n 端点单独置于前景.
C.3 将标题、两条换基公式、旋转角度与投影不变性合并到图右侧的圆角白框,
框内字号由 11 调整为 13. 字体在正文中的整体缩放约增大 14%,
框内文字相对于原两条公式的显示尺寸约增大 35%.
C.2 两个小标题改用统一的画布高度定位, 字号设为 13;
theta=pi/3 与实、虚部坐标标签字号设为 15.
图中回路旁仅标注方位角 phi, 正文说明蓝色箭头沿 phi 增大的方向绕行.
C.2 的 phi 上移约一行; phi、theta_0、n、gamma=-pi/2 及两端方位角标注统一为 15 号.
按用户记号习惯, 正文 53 处圆周率改为 `\mathrm{\pi}`;
Ch4 的波矢刻度及 C.2/C.3 的圆周率标签同步更新. 轨道、化学键与等离激元中的 pi
仍采用其原有符号, 程序数值常数 `np.pi` 无变化.
三张图中的 Dirac notation 改用 MathText 的配对伸缩定界符:
ket 为 `\left|...\right\rangle`, 内积为 `\left\langle...\middle|...\right\rangle`,
修正普通竖线与角括号的高度差. 正文继续使用现有 braket 命令.

已执行完整 notebook, 并独立数值验证闭路重叠积的规范不变性、相位终点 -i
及两套基底给出的投影算符一致性.

## 保留性与编译结果

相对于本次开始时的 `5361012`, 原 Theory fundamentals 与 Chapter 4
共 213 个内容 label 和 191 组显示公式全部保留; 迁移时原显示公式逐字保留,
后续按用户要求统一圆周率的 `\mathrm{\pi}` 写法.
新增 14 组显示公式, 全部位于 Appendix C (包括示意图说明所需的两组公式).
原 A/B 拆分涉及的 157 组显示公式在拆分时均未改动.
活动 TeX 文件无重复 label、未定义交叉引用或缺失的相关 citation key.

全文 `latexmk` 已完成, 无未定义引用、重复 PDF 目标或过大的浮动体警告.
沿用原文的个别 overfull hbox 提示仍存在; 新附录 C 与本次章首编排无新增此类提示.

以章首至下一章章首的页码差计, 包含章节间的必要空白页:

- Chapter 2: 52 页 (印刷页 15–66).
- Chapter 3: 24 页 (印刷页 67–90).
- Chapter 4: 22 页变为 16 页 (印刷页 91–106).
- Appendix A: 印刷页 249 起, 36 页.
- Appendix B: 印刷页 285 起, 12 页.
- Appendix C: 印刷页 297 起, 14 页 (三张示意图及说明使本附录增加 2 页).
- Appendix D: 印刷页 311 起.
- 完整 `.output/thesis.pdf`: 348 页; 四个附录均为奇数页开章.

三图分别位于印刷页 303、306 与 307; 本次新增图文无 overfull hbox、
未定义引用或过大浮动体警告.

2026-09-26 的前次迁移已将 Chapters 2–3 从 84+32 页调整为 52+24 页,
并保留相对于 `4eb194f` 的原有 360 个 label、333 个显示公式块和 114 个 citation key.
本次沿用该正文范围, 将理论附录进一步按主题拆分.

## Examiner 对应

延续对 Examiner 1 关于 fundamentals 篇幅与实际方法组织的回应.
Examiner 2 要求的光学例图来源与研究章交叉引用继续保留在 Chapter 3.
Chapter 4 中对子空间隔离、金属填充与宇称判据适用条件的说明继续保留在正文.
此次完成内容迁移、Berry 基础补充和结构衔接, 不代表全部 examiner 意见均已关闭.
