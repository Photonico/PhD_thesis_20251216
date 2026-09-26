# Chapters 2–3 基础内容迁移

日期: 2026-09-26.

本次按用户确认的范围执行迁移. 此决定取代此前措施稿中“不移入附录”的旧范围约束.
目标是减轻正文 fundamentals 的篇幅, 同时保留原有推导和写作内容.

## 正文与附录的分工

- Chapter 2 从 Density functional in quantum mechanics 开始, 保留密度泛函与 Hohenberg–Kohn 主线, Kohn–Sham, 交换关联泛函, 实际计算方法.
- 原 Chapter 2 的时间演化、多体 Schrödinger 方程与 hamiltonian、Born–Oppenheimer 近似、Heisenberg 表象、连续性方程, 多体统计与约化描述, 泛函的基本定义, Thomas–Fermi 构造及其扩展移入 Appendix B.
- Chapter 3 保留工作本构关系, 介电函数的微观表达、带间/Drude 与二维归一化, 正频率 Kramers–Kronig 关系及静态极限, 派生光学量与全部六幅自有计算例图.
- 原 Chapter 3 的 Maxwell 方程、本构关系的详细推导、各向异性基础, 因果性与全频率 Kramers–Kronig 推导移入 Appendix B.
- 正文补充 Hartree 势与光学本构关系两组工作公式, 调整章首导航和因迁移失效的前后指代.
- Introduction 的组织说明增加两个附录的入口.

## 编排

References 之后依次为:

- Appendix A: Source code and data analysis (`src/appendix.tex`).
- Appendix B: Theory fundamentals (`src/appendix_basic.tex`).

Chapter 2 的完整标题为 `Fundamentals \textRoman{1}: From Many-body physics to Density Functional Theory`, 目录短标题为 `Fundamentals \textRoman{1}: From Many-Body Physics to DFT`.
按用户的追加要求, Many-body Schrödinger equation 接回附录的时间演化部分, What is the functional? 放在 Thomas–Fermi 部分之前.

`thesis.tex` 使用 `\appendix` 并编入两个文件.
沿用文档类已有的附录编号和奇数页开章规则.
Appendix B 的 chapter label 是 `cha:appendix_basic`.

## 编译结果

以章首至下一章章首的页码差计, 包含章节间的必要空白页:

- Chapter 2: 84 页变为 52 页 (印刷页 15–66).
- Chapter 3: 32 页变为 24 页 (印刷页 67–90).
- 两章正文合计减少 40 页, 内容迁入附录.
- Appendix A 从印刷页 255 开始; Appendix B 从印刷页 257 开始.
- 完整 `.output/thesis.pdf`: 338 页.

相对于迁移前的 `4eb194f`, 两章原有 360 个 label、333 个显示公式块和 114 个 citation key 均保留.
原显示公式块逐字保留; 所有活动 TeX 文件无重复 label 或未定义的正文交叉引用.
`latexmk` 完成, 最终日志无未定义引用、重复目标或过大的图像浮动体警告.
两个附录的印刷页和 PDF 实际页均为奇数起页.

## Examiner 对应

回应 Examiner 1 关于 Chapters 2–3 过重、应围绕实际方法重组的意见.
Examiner 2 要求的光学例图来源与研究章交叉引用继续保留在 Chapter 3.
此次仅完成内容迁移和结构衔接, 不代表全部 examiner 意见均已关闭.
