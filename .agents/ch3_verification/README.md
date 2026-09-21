# Chapter 3 光谱来源与后处理核验

核验日期: 2026-09-21.
对应 [修改操作稿](../ai_ch3_last.md).
本目录同时保存修正前来源证据和修正后的图件核验.
2026-09-21 已按批准措施替换 Chapter 3 / Project 3 的十二个正式 PDF;
没有执行新的 DFT 计算.

固定来源:
[Photonico/H-Beryllene_20250718](https://github.com/Photonico/H-Beryllene_20250718/tree/f863ab02ebf93d5804f5552967ea750571778335).

- `source-and-numeric-audit.json`:
  十二个 PDF 的身份、十个原始文件的 Git blob/SHA-256、
  PDF 数值比对、修正前后数值及真实计算设置.
  其中 PDF 哈希及旧公式比对保留为修正前证据, 不再指向当前修正图.
- `a-vasprun-parameters-excerpt.xml` 和 `b-vasprun-parameters-excerpt.xml`:
  固定提交实际输出的 parameters 段, 包括 WPLASMAI=0.
  它们是摘录, 不是完整的 vasprun.xml.
- `recompute_optics.py`:
  只读介电数组, 对比原后处理与厚度/角频率修正, 写出审计 JSON.
- `compare_pdf_numeric.py`:
  以 PDF 自身刻度标定坐标, 检查保留曲线顶点与原后处理的一致性.
  不用原始数组拟合坐标.

两个脚本需要 Python、NumPy、h5py 和 PyMuPDF.
复核时在一个临时目录中放入脚本,
并从上述固定提交按原路径下载:

- `6.0_dielectric_selection/a-Beryllene/vaspout.h5`、`POSCAR`、`CONTCAR`.
- `6.0_dielectric_selection/b-Beryllene/vaspout.h5`、`POSCAR`、`CONTCAR`.

先按 JSON 中的哈希核对文件, 再运行重算和比对.
`compare_pdf_numeric.py` 的 THESIS 常量指向本次论文工作目录.
它读取当前 `figures_ch3` 中的图件; 如果这些图已经替换为修正版,
应改为读取原归档 `figures_for_thesis` 的对应旧图再复现本次核验,
不能期待修正图仍与旧公式吻合.
脚本输出只写到脚本所在目录, 不修改原始数组或 PDF.

本目录不重复保存约 22 MB 的原始 HDF5.
此次临时下载在系统临时目录, 后续可用固定提交重新取得.
数值精度受 PDF 折线简化、浮点输出和原能量网格限制.
严格吻合的结论针对 6,510 个可见保留顶点;
被坐标轴裁掉的峰由原始数组和轴范围共同确认.

## 2026-09-21 图件应用记录

已替换操作稿列出的 Chapter 3 / Project 3 两套共十二个 PDF.
源文件名、配色、实线、面板布局、光谱背景和两套字号保留.
修正 beta 厚度为 5.855086567902241 Å, 吸收角频率补一次 2π,
纵轴单位明确为 nm^-1; loss 面内、面外上限分别为 2.5 和 9.5.
原始 HDF5 的前后 SHA-256 不变, 没有增加 Drude 项.

- `corrected-export-audit.json`: 新版十二个 PDF 的 SHA-256、坐标、
  软件版本、源文件哈希、结构厚度和修正数组峰值.
- `corrected-pdf-vs-h5-numeric-audit.json`: 当前十二图的独立 PDF
  刻度标定与曲线核验, 共 56 条导出曲线, 即 28 条独立曲线的两种版式.
- [重生成脚本](../../figures_ch3/regenerate_optics.py)、
  [核验脚本](../../figures_ch3/verify_optics.py) 和
  [重现说明](../../figures_ch3/README.md): 接受原归档路径参数,
  读取前校验哈希, 无需在仓库重复保存原始 HDF5.

新图保留 0–12 eV 窗口内全部原始采样点, 不作折线简化.
33,516 个导出顶点与修正数组比较, 最大页面残差约 0.003245 pt;
全部 56 条曲线均无超过坐标上限的采样值.
两套图坐标相同, 吸收上限为 0.2625 nm^-1,
能容纳约 0.241453 nm^-1 的最大值.
修正数组与先前独立审计脚本的结果最大差约 2.7e-15.
十二图均经 Poppler 渲染并作视觉检查, 未发现文字重叠或峰裁剪.
论文实际编译后的版面检查由整篇编译另行完成.

替换前十二个 PDF 及 SHA-256 manifest 保存于临时目录
`/var/folders/jd/spwt8xjd2jdcbvqz6zhd785m0000gn/T/thesis-ch3-figures-before-mscey1z1`.
旧 `compare_pdf_numeric.py` 仍是修正前证据的复核工具;
它应对原归档旧图运行, 当前图应使用新的 `verify_optics.py`.
