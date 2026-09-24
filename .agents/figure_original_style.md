# Project 1/2 图像回归原稿

本轮按用户最新决定恢复原论文各图的字体、画布大小、线条、图例与整体配置，取代 `figure_layout_rescaling.md` 中的分级统一方案。原图之间原本不同的设置也保留，不再以统一字号或固定画布宽度重新设计。

只保留三项视觉改动：

- 原本横排三个数据面板的图改成 2×2，第四格放图例。
- 保留 `proj1.8_schottky` 的标题。
- 保留 `S1.4`、`S1.5`、`S1.6` 的二维 heat map 处理。

已经由原始计算数据确认的科学修正继续保留，包括 PDoS 的能量网格与费米能一致性、正确的 Hollow 2 数据、实际采样最低点、吸收系数单位、自旋 DoS 的共同网格，以及 EPW 能隙分布的正确解释。回退绘图样式不回退这些数据修正。

每个项目仍由各自 `figures_for_thesis/figures_for_thesis.ipynb` 管理；绘图代码和逐图参数直接写在单元格中，可以自行调整。输出 PDF 先保存到源仓库，再复制到 Thesis。没有重新进行第一性原理计算，也没有建立备份副本。

- Project 1：`/Users/lu/Repos/Graphene-BC_20230622/figures_for_thesis/figures_for_thesis.ipynb`
- Project 2：`/Users/lu/Repos/o-B14_20241024/figures_for_thesis/figures_for_thesis.ipynb`

Chapter 4 不在本次回退范围内。

原稿的字体设置来自两个计算仓库原有的绘图代码：轴标题 16 pt、刻度 14 pt、图例 12 pt，其他标题和结构图标注沿用各自原设置。画布按原图分别恢复，TeX 插入比例参照 Thesis 的 `47711bf` 版本。

原来横排三面板的图改为 2×2 时，相应缩小整体插入宽度，使单个面板和字体的印刷大小保持原来的比例。`S1.14` 的五组图按两组、两组、一组分页，用续图保留同一图号。其他拆分图恢复原来的组合方式。

按用户最后要求，不继续进行额外 review 或备份；完成出图、Notebook 同步和整书编译即可。

## 完成状态

Project 1 的 48 份 PDF 和 Project 2 的 25 份数值 PDF 已保存到各自 `figures_for_thesis` 并同步到 Thesis；Project 2 的五张结构图直接使用原有的高分辨率 PNG。不再引用的近期合并版已移除。两本 Notebook 保留直接可编辑的绘图单元格，运行时显示图像，保存文件时清空图像输出。

整本 `.output/thesis.pdf` 已重新编译成功，共 326 页；编译日志没有未定义引用、未定义文献或过大浮动图警告。Chapter 4 未作修改。本轮临时 review 文件和执行脚本已清理，没有建立备份或进行 Git 提交。
