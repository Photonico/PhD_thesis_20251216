# Project 1/2：图组合并、原数据核对与统一绘图

后续字号与布局已按用户反馈回调；当前分级缩放和图例设置见 `figure_layout_rescaling.md`，此前三面板的 2×2 排列记录见 `figure_layout_refinement.md`。下文保留前轮科学核对与历史编译记录。

本轮日期：2026-09-23 至 2026-09-24（Sydney）。
本记录补充此前的 `ai_proj1_last.md`、`ai_proj2_last.md`，并以本轮核对结果更新其中涉及的绘图与数据解释。

## 调图入口

每个计算仓库各有一本 `figures_for_thesis/figures_for_thesis.ipynb`。
首个设置单元格控制字体、颜色、线宽与保存方式；后续单元格直接给出各组图的 Matplotlib 绘制代码，可以逐组修改画布、坐标范围、子图间距与图例。
运行后先在该仓库的 `figures_for_thesis` 输出 PDF，再复制到 Thesis。
Notebook 不保存大块图片输出；重新运行即可显示，避免重复占用空间。

- Project 1：`/Users/lu/Repos/Graphene-BC_20230622/figures_for_thesis/`
- Project 2：`/Users/lu/Repos/o-B14_20241024/figures_for_thesis/`

原有 Python 脚本保留为批处理版本。手动调整 Notebook 后，应从 Notebook 重新出图；旧批处理代码不会自动包含新的 Notebook 调整。
没有重新运行第一性原理计算，没有修改原计算输入、原 notebook 或已发表 PDF，也没有建立备份副本。

## 图像与排版

Project 1 的 36 张现用图已重新生成，包括 33 张数值图和 3 张结构图。
Project 2 的 23 张现用数值图和 5 张结构图已重新生成；两张单独的示意图 `S2.6.png`、`S2.7.png` 保留。

主要合并关系如下，其余已经包含多个子图的图件沿用文件名：

- `proj1.3a/b/c/d` → `proj1.3_bands.pdf`，2×2 能带图，共用图例。
- `proj1.8a/b` → `proj1.8_schottky.pdf`，示意图和实际能带放在同一画布。
- `proj1.12a/b` → `proj1.12_optics.pdf`；`proj1.13a_cor/b` → `proj1.13_optics.pdf`。
- `S1.13a–d` → `S1.13_dielectric.pdf`；`S1.14a–e` → `S1.14_optics.pdf`。
- `S1.4–6` 各自显示完整能量图组，删除 TeX 中旧的裁切及跨页续图。
- `fig2.2` 的 band/BZ/PDoS → `fig2.2.pdf`；`fig2.6a/b/c` → `fig2.6.pdf`。
- `fig2.9a/b` → `fig2.9.pdf`；`fig2.11a/b` → `fig2.11.pdf`；`fig2.12a/b` → `fig2.12.pdf`。
- `S2.1a/b`、`S2.9a/b`、`S2.10`、`S2.11a/b`、`S2.16a/b` 分别合成同编号 PDF。

样式采用 Chapter 4 的 serif、Computer Modern 数学字体、1.5 pt 线宽、Matplotlib 原生 legend 与默认 `round` 标题框。
源字号为轴标题 16 pt、刻度和图例 14 pt、子图标题 12 pt。
数值图统一 10 inch 宽、按正文全宽插入。Project 2 的结构图按原来的 0.8 或 0.75 正文宽度插入，对应画布设为 8 或 7.5 inch，因此最终印刷字号与数值图相同。
Chapter 4 的两个图文件保留用户的现有版本，只调整 TeX 插入比例，使最终字号与本轮图像基本一致。

结构图保留原始 PNG 或 XCF 中的原子、等值面、单位胞及圈选标记。
Project 2 的 XCF 仅临时隐藏文字层，再用 Matplotlib 加入统一字体；不保存或覆盖 XCF。
独立图像对照确认科学内容不变。

## 原数据核对中发现的必要修正

### Project 1

1. **PDoS 的网格与能量参考。** 原绘图混用了普通网格的原子投影、可选网格的 total DoS 和 Fermi energy，并将后者配在普通网格的能量轴上。三套 HSE06 的可选网格投影还存在后半原子全零的归档不完整问题，不能解释为真实零贡献。
   `S1.9–11` 现统一使用完整的 `17×17×1` 普通网格、其 total/projected DoS、能量轴与 Fermi energy；主文能带旁的完整 total DoS 仍使用 `33×33×1` 可选网格。两者的 Gaussian 参数均为 0.1 eV，方法部分已区分。

2. **Hollow 2 源文件。** 原 notebook 将 Graphene-Borophene 与 Graphene-B4C3 的 Hollow 2 面板指向了 Hollow 1 文件。现使用各自真正的 Hollow 2 数据。最低能堆叠的结论不变。

3. **二维能量图的最低点。** 原程序同时扫描两个坐标的一条对角线，不能据此声称找到了二维拟合极小值。`S1.4–6` 保留原线性插值，标记实际采样数据的最低点；与后续弛豫结构参数明确区分。一维 EOS 拟合最低点保留。

4. **图文对应。** 普通 PDoS 不能支持“Graphene-Borophene 费米能附近的态主要来自碳”的原说法，现改为两层均有贡献；B4C3 主要态在约 −0.8 eV 以下和 1.2 eV 以上的描述仍与数据相符。静态介电常数按零能原始值更新：BC3 的面内值约 4.1，B4C3 约 3.8。

5. **收敛比较的条件。** `S1.12` 三组均使用 `ALGO=Exact`，删除只在最密网格后出现的这个标签。`S1.16` 的 `EDIFF=10^-4/10^-5` 使用 `PREC=Normal`，`10^-6` 使用 `PREC=Accurate`；图注明确这不是只改变一个参数的比较。

原始光学张量未作静默对称化；此前对吸收系数角频率和单位的修正保留。234 条能带曲线与此前原图恢复数据的最大差异约为 `5.114×10^-5 eV`；10 套主要光学张量与此前审计数组逐点一致。

### Project 2

1. **自旋 DoS。** 原读取函数分别为两个自旋生成不同的能量网格，不能直接按数组下标求和。`S2.16` 现直接用两组 OUTCAR 本征值、25 个归一化 k 权重及同一 4000 点能量网格重构，Gaussian 宽度为 0.05 eV。独立计算差异小于 `10^-13`，每个自旋通道积分为 32。正文不再单凭 total DoS 将分裂归属于 apical atoms；独立的局域磁矩讨论保留。

2. **超导能隙文件。** EPW 的旧两列输出将第一列写成 `T + rho/max(rho)`，第二列为能隙 bin。第一列含分布显示偏移，不能直接当作温度做拟合。该含义可由 [QE 6.8 官方实现](https://github.com/QEF/q-e/blob/qe-6.8/EPW/src/io_eliashberg.f90#L2034-L2082) 确认；这不等于已经确认本地计算使用的软件版本。
   新 `fig2.9` 从文件名读取真实温度，显示全部 112 个文件的归一化能隙分布及分布均值，移除旧经验拟合和其 Tc 竖线。均值采用离散 bin 权重求和，不将缺失 bin 当作连续插值区间。
   bulk 归档止于 30 K，此时分布仍为 0.93–2.28 meV；氢化双层在 26 K 仅剩 0.03 meV 的最低 bin。归档没有正常态和迭代收敛输出，因此不能独立确认精确 Tc，也不据此给出严格界限。
   发表稿的 31.3 K、24.3 K 在研究正文保留为 **reported estimates**，不再宣称由新图直接证明闭合；摘要与结论同步去掉未经重新确认的精确数值。没有以另一组经验拟合参数替代已发表值。

3. **收敛图的实际输入。** `S2.1(c)` 的晶格扫描采用 `10×14×9`、600 eV，原图注的 `34×48×31` 不描述该扫描；正文主计算的密网格保持。`S2.3` 的横轴是完整超胞高度 `a3`，不是单独真空层厚度。

4. **实际 band 数与原子组。** `S2.5` 图例采用 VASP 实际使用的 48、72、144、264 bands，图注另列请求的 32、64、128、256。bulk PDoS 的橙色 s 与 p 曲线使用相同的 B3_index；旧图将 s 误标为旧 Group 3，而同组 p 标为旧 Group 2。现修正这处不一致，并将原 Group 1/2/3 统一命名为 G2/G3/G7。原子选择不变，三组选区相互重叠，并非不相交的原子划分。

此前确认的 NM-PBE 光学参考、厚度约定、吸收系数单位和 5500 步 AIMD 处理均保留。已有 H2 能量记账、完整 QE/EPW 输入以及小负声子收敛证据的缺口，没有被图形重画自动解决。

## Chapter 4 与验证记录

对 `ai_ch4_report4.md` 的逐条判断见 `ai_ch4_report4_review.md`。
只补充 helical edge states 的有限条件、单对边缘态的零弹性反散射矩阵元，以及 TRIM 不能替代全 Brillouin-zone 间隔检查的限定；同步 Introduction 的 Chapter 4 指引和 selected/occupied 符号措辞。
中文通读稿已同步。没有加入论文未使用的 Wilson loop 等内容。

数值与来源证据位于两个源仓库的 `figures_for_thesis`：Project 1 的 `verification.json`、`spacing_audit.json`、各 `*_sources.json`；Project 2 的 `numerical_manifest.json`、`spin_dos_verification.json`、`gap_summary.json`；结构来源记录为各自的 `structure_manifest.json`。
整书最终页数、章节起页、图像缩放及编译检查另存于 `proj12_figure_style_verification.json`。
已移除 Thesis 中被原数据流程替代的临时绘图脚本、NPZ 和重复结构图片，合计约 41.46 MB；保留来源审计记录及 Git 中原有图件。

## 最终验证

整本 `.output/thesis.pdf` 已重新编译为 332 页。Chapter 4 为正文第 131–152 页（含章间空白页），比本轮开始时增加 2 页；末页为正常的奇数起章留白。所有 16 个章节级书签均指向奇数页。没有未定义引用、未定义文献或超高浮动图警告；原有 9 处 overfull hbox 警告未增加。

两本 Notebook 的 21 / 28 个代码单元均完整执行通过，保存时清空图片输出。64 张现用新 PDF 的源仓库与 Thesis 副本逐字节一致，文字均未超出图像边界；各图按 TeX 缩放后的相对字号一致。最终整书检查了两张 Chapter 4 示意图、helical 公式、合并能带图、结构图、能隙分布及补充图页面。用户现有 Chapter 4 Notebook、4.1 PDF 和发表稿 PDF 的文件哈希均保持本轮开始时的状态。

收尾再次对照原始 reports 后，补齐 SOC/TRIM 缩略语，并修正 Schottky 图注的面板方向及 Project 2 SI 的两处 DoS 身份说明。最终重编译仍为 332 页；当前完成性审计见 `ai_proj12_report_check.md` 的末节。
