# 图像排版回调与三面板重排

本轮绘图样式已被用户后续决定取代：恢复原论文各图配置，当前记录见 `figure_original_style.md`。以下保留为历史记录。

后续用户要求进一步恢复原比例；当前设置以 `figure_layout_rescaling.md` 为准。下文为前一轮记录。

日期：2026-09-24（Sydney）。本记录更新 `ai_proj12_figure_style.md` 中上一轮的字号与布局说明；此前的数据修正保留。

## 当前样式

Chapter 4、Project 1、Project 2 共 66 张现用 PDF 已纳入本轮调整。轴标题为 13 pt，刻度、图例和子图标题为 11 pt，线宽为 1.5 pt；沿用 serif、Computer Modern 数学字体、原颜色与 Matplotlib 原生 legend / round 标题框。

数值图仍为 10 inch 宽，并按正文全宽插入；结构图与 Chapter 4 示意图采用对应的画布宽度与 TeX 比例，保持字号尺度一致。短图例放在不遮挡数据的图内空处；较长的图例紧贴下方排列。没有另加第三列图例区。

按照后续要求，恰好三幅子图的图件改为紧凑的 2×2：前三格依次为 (a)、(b)、(c)，右下格放共享图例。

- Project 1：`proj1.3`、`S1.3`、`S1.4`、`S1.9`、`S1.20`、`S1.21`、`S1.22`、`S1.23_correct`、`S1.24_correct`。
- Project 2：`fig2.2`、`fig2.6`、`S2.1`、`S2.18`。

`S1.4` 的共享色条也放在右下格；`proj1.3` 的第四格说明 boron、carbon 和 unit cell。原本完整的九分量张量图仍为 3×3。正文与 caption 的相关位置说明改用子图编号，避免“从左到右”等旧措辞与新布局不符。

## 数据与显示范围

本轮没有修改原计算数据或重新运行第一性原理计算。为避免标题遮挡或坐标裁切，只对个别图的坐标上、下限与标题位置作必要调整；包括 Project 2 的 `S2.9` 负声子支和 `S2.16` DoS 峰顶。它们的数值保持原样。

Project 1 同一成分的二维能量子图采用统一色阶，以便直接比较不同堆叠；坐标、插值数据及采样最低点未改。这是显示归一化的改变。

Project 1 本轮重新校验了 66 份原始文件与 Git index 的 blob 身份，以及三组 PDoS 的 Fermi energy / 附近态密度；PDoS 与前轮记录的差值为零。另将两个项目中选取的 12 个数据读取、光谱计算及能带绘制函数与各自 Git HEAD 作 AST 比较，结果一致。Project 1 的 Git 目录名实际为 `Figures_for_thesis`（大写 F），核查时使用了该大小写。此前旧图数组对比结果属于历史证据，不冒充本轮重算。详见源仓库的 `moderate_layout_verification.json`。

22 张已经被合并图替代、且不再被正文引用的旧 PDF 恢复为 Git 原版，避免留下无效重绘。现用合并图继续包含前轮科学修正；恢复清单与哈希见 `superseded_figure_restore.json`。

## 可编辑入口与验证

每个项目各保留一本 `figures_for_thesis/figures_for_thesis.ipynb`。首个设置单元格控制共同字体、颜色和线宽；各组图的单元格直接包含画布、子图间距、坐标与图例设置。PDF 先保存至源仓库，再复制到 Thesis。Notebook 保存时清空图片输出。

- Project 1：`/Users/lu/Repos/Graphene-BC_20230622/figures_for_thesis/figures_for_thesis.ipynb`
- Project 2：`/Users/lu/Repos/o-B14_20241024/figures_for_thesis/figures_for_thesis.ipynb`

最终 PDF 哈希、画布尺寸、源仓库与 Thesis 副本一致性、Notebook 状态和整书编译结果以 `figure_layout_refinement_verification.json` 为准。

最终整本 `.output/thesis.pdf` 为 330 页；16 个章节级书签均从奇数页开始。Chapter 4 仍为 22 页（含章间留白），没有超过原先的增幅限制。未出现未定义引用、未定义文献或超高浮动图警告；原有 9 处 overfull hbox 警告没有增加。66 张现用图逐图完成视觉检查，64 张源项目 PDF 与 Thesis 副本字节一致；两本项目 Notebook 格式、语法与清空输出状态通过，修改过的绘图单元已执行。
