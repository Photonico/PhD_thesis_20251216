> 后续更新：2026-09-24 的原数据重画与交叉核对发现了进一步修正，尤其涉及 PDoS、EPW 能隙文件及 Tc 解释。请同时阅读 [本轮记录](ai_proj12_figure_style.md)；本文件保留为上一轮审阅记录。

# Project 2 已实施修改与证据记录

更新日期: 2026-09-23.

本轮对象为 `src/project_2_main.tex`, `src/project_2_SI.tex` 及两张需要纠正的图.
依据为两份 examiner reports, `reports/report_merge.md` 第 3.4 节,
`.agents/proj_contributors.md`, 已发表的 `paper 2-compressed.pdf`,
以及作者确认的原计算仓库.
保留原章节结构, 结果和讨论主体; 只前移结构图, 补必要方法说明,
纠正可核实的公式, 图件和事实, 并收窄超出证据的结论.
没有新增第一性原理计算, 没有修改已发表论文 PDF.

## 1. 证据范围

已发表论文为 Physical Review Materials 10, 074001 (2026),
[doi:10.1103/b2q9-fytt](https://doi.org/10.1103/b2q9-fytt).
下述论文页码指根目录 PDF 的文件页码, 从 1 开始.

计算归档固定为
[Photonico/o-B14_20241024, commit a9476a5c0e5ce764456c4cc7a50f8e15d64f951c](https://github.com/Photonico/o-B14_20241024/tree/a9476a5c0e5ce764456c4cc7a50f8e15d64f951c).
关键数值, 源文件路径及图件身份核验保存在 `proj2_evidence.json`.
方法和结果来自论文与实际输入/输出的交叉核查, 未采用 AI 模板补造参数.
相关结构, 声子, AIMD, 能带及光学图均检查过实际图像.

## 2. 按评审意见实施的最小修改

1. 发表与贡献, 对应 Examiner 2 的章首贡献要求.
   在 `cha:project_boron` 下加入简短普通段落, 使用实际卷号和文章号.
   按作者提供的分工说明计算, 分析和绘图由候选人完成,
   Oliver James Conquest 指导 AIMD, Hongyang Ma 指导超导计算,
   全体作者参与写作和修改. 未采用 Gemini 所写的未经确认的研究构思分工.

2. 结构图位置, 对应 Examiner 2 的 Figure 5.1 意见.
   将原图及 `fig:ob14_atomic_structure` 整体前移到 Introduction 首次正式介绍 o-B14 的段落附近,
   在 `2_methods` 之前简短引入. 保留原图, 分组 G2/G3/G7 和图注内容,
   不新增未经核实的切割晶向.

3. 稳定性, 对应 Examiner 1 的证据分级及负频矛盾.
   在 `2_abstract`, `xene_ob14_phonon_dispersion`, `2_conclusions`
   和 `S2.9`/`S2.10` 图注区分凝聚能比较, 所计算路径上的声子结果,
   400 K 的短时热保持及实验可合成性.
   氢化双层在 Gamma 附近确有小负频; 现文明确其数值来源尚未得到证明,
   不再把它直接写成已排除的数值伪影.
   AIMD 的 5.5 ps 轨迹不能单独证明热力学稳定或可合成性.
   bulk 相对 alpha-B12 的文献差值补上 0.232 eV per atom,
   不再由该正差值声称热力学稳定. Han et al. 的 SI Table S4
   标为 1 atm 下的 Gibbs free-energy differences, 单位为 eV/atom.
   该单位通过出版者的 SI 表索引核对；原 SI PDF 链接此次返回 404，未声称重新下载核查了完整附件.

4. 磁态, 对应 Examiner 1 的小 AFM-FM 能量差和光学身份问题.
   在 `xene_ob14_electronic_properties` 将约 0.02 eV 明确为
   HSE06 比较中每个 14-B 原胞的能量差, 不换算成 Gemini 的 3.2 meV/atom.
   归档的 AFM-FM 差为 F: -18.244 meV/cell,
   E0: -19.004 meV/cell, 与发表稿第 6 页的约 0.02 eV 相符.
   这是零温能量比较, 不给出磁有序温度; 交换机制解释保留为可能解释.
   两套 HSE06 原子位置存在约 0.0011 Angstrom 的差别,
   因而记录不将其夸大为严格同一几何结构上的泛函对照.

5. PBE/HSE06, 对应 Examiner 1 的带隙解释要求.
   保留双层 HSE06 0.67 eV 与 PBE 半金属结果,
   补充短程 Fock exchange 对自相互作用和离域误差的部分改善,
   并明确两者均是近似. `tab:xene_ob14_structure` 图表说明中的
   semiconductor 分类限定到 HSE06 能带.
   另有归档 PBE 磁态比较, 但几何, 色散修正与展宽设置并不构成
   与上述 HSE06 的严格受控对照, 本轮不据此新增泛函决定磁序的结论.

6. 超导, 对应 Examiner 1 的 DFPT/Wannier/EPW 工作流要求.
   在 `2_methods` 顺着原方法段落补齐
   DFPT phonons/first-order potential -> Wannier electron-phonon matrix elements
   -> Fermi-surface average of squared matrix elements -> alpha2F -> lambda/omega_log
   -> Allen-Dynes 的物理链, 引用 Chapter 2 已有公式.
   各向异性 Migdal-Eliashberg 由温度依赖能隙闭合另行估计 Tc.
   保留论文第 3 页已有的真实电子网格, q 网格, B s/p 投影和 mu*=0.13.
   在 `2_superconducting` 及 `fig:ob14_superconducting_gap` 区分
   bulk: 28.2 K (Allen-Dynes) / 31.3 K (anisotropic ME),
   H-bilayer: 18.5 K / 24.3 K; 数值未改.
   单层 lambda=0.05 不支持从所用简化 Allen-Dynes 式直接给出可信 Tc,
   也不代表已计算了有隙 AFM-HSE06 态的超导性.
   这是方法解释的补全, 完整数值复现仍需要原 QE/EPW 输入.

7. 光学参考态和归一化, 对应 Examiner 1 的 AFM semiconductor/metallic 矛盾.
   `2_methods`, `2_optical` 和 `fig:ob14_dielectric_function` 现明确使用 NM-PBE:
   实际输出 ISPIN=1, LHFCALC=F, LSORBIT=F, SIGMA=0.01 eV,
   CSHIFT=0.1 eV, WPLASMAI=0; 后处理没有另加参数化 Drude 项.
   CSHIFT 是数值展宽, 不是拟合的载流子散射率.
   不将这些结果称为 AFM-HSE06 的光谱, 也不据 WPLASMAI=0
   泛化为 VASP 完全不含任何带内贡献.
   输入 NBANDS=128, 实际 bulk 为 129, 三个 2D 体系均为 168;
   所展示 bulk 曲线使用 34x48x31, 与原文 20x28x18 收敛检查区分.
   `S2.5` 改明 NBANDS 是包含占据态的总带数.
   单层有效厚度按真实作图值由 5.897 改为 5.807 Angstrom.
   保留原来三对角分量的厚度缩放数据, 但说明它是 adopted effective-thickness
   convention; 尤其 zz 不等同于唯一的 intrinsic, vacuum-free dielectric constant.

8. 吸收与 plasmon, 对应 Examiner 1 的预测范围与正文自洽.
   `fig:ob14_absorption_loss` 附近明确 alpha=2 omega k/c, E=hbar omega,
   吸收起始不等于 epsilon2 的第一个峰.
   纠正吸收图的频率及长度单位, 删除原来缺乏同单位依据的
   bulk silicon 0.005 Angstrom^-1 绝对比较, 保留文献背景.
   通过归档 epsilon 重新检查零交叉, epsilon2 和 loss 峰:
   负 epsilon1 本身不证明 plasmon; 有限 epsilon2 意味阻尼,
   光学极限结果也不确定传播的 2D plasmon dispersion.
   主文将低能响应和出平面特征收窄为相应 loss features,
   并保留有效厚度约定及阻尼限制, 摘要/结论同步限定.

9. 氢吸附计量, 属于核查中确认的科学修正.
   发表稿第 3 页和原 thesis 在 EH 定义为每个 H 的半个 H2 能量时,
   分子中均漏写 nH. `hydrogen_adsorption_energy` 现为
   Ead=(EH/B-EB-nH EH)/nH, EH=EH2/2.
   电荷差分说明的 H fragment 包含同一胞内全部吸附 H,
   并说明共同胞与吸附构型的坐标约定.
   表中 -1.450/-1.525 eV/H 暂保留为已报告数值;
   公式修正不等于已核实这两个数值的 H2 能量账目.

## 3. 两张图分别改了什么

1. `figures_proj2/fig2.11a.pdf`: 吸收系数图.
   原 `vmatplot/algorithms.py` 返回 E/h, 而
   `vmatplot/linear_optical_properties.py` 的吸收式需要 E/hbar,
   同时光速使用 nm/s, 原图却按 Angstrom^-1 解释.
   12 条原曲线均与这段旧实现及相应原始 epsilon 匹配,
   最大坐标残差约 0.019 PDF point.
   修正后, 以 Angstrom^-1 表示的新数值是原绘图数值乘 2 pi/10,
   约 0.6283185. 不仅是换一个轴标签, 也不是单乘 2 pi.
   现图由同一介电数组独立重绘, 保留四体系, 三分量及对应配色,
   明确 y 轴单位. 没有重新运行 DFT, 没有替换原介电函数或 loss 图.

2. `figures_proj2/S2.10/S2.10a_long.pdf`: AIMD 图.
   原图内标题误写 bulk, 实际数据确定来自氢化双层.
   修改前 PDF 与归档 `figures_collection/S2.10a_long.pdf`
   及 `figures/8.0_aimd_bilayer_H.pdf` 的 Git blob 完全一致:
   `9edbaf12b734031bcd16b307a1fb1c525a5be549`.
   `8.0_aimd.ipynb` 读入 `6.0_AIMD/bilayer_H`,
   POSCAR 为 B112 H16, INCAR 为 NVT/Nose-Hoover, 400 K, 1 fs,
   OSZICAR 有 5500 步. Notebook 导出时传入了错误标题.
   现图从同一 OSZICAR 重绘, 标题改为 hydrogen-terminated bilayer,
   原曲线 F 正确标为 electronic free energy, 保留温度和 5.5 ps 时长.
   同步更新重复导出 `figures_proj2/S2.10a_long.pdf`;
   这两个路径是同一张图, 不是两组 AIMD 计算. 右侧结构图未改.

重绘入口为 `figures_proj2/reproduce_revisions.py`,
所需归档介电数组和 AIMD 的 step/T/F 存在 `figures_proj2/revision_data.npz`.
程序不依赖外部 vmatplot, 可以直接重绘这两张图.

## 4. 未采用的 Gemini 项目

- AFM-FM=3.2 meV/atom; AFM-HSE06 光学谱及 2.1/0.05 eV Drude 参数.
- 小负频低于 0.05 THz, 明确属于 ZA 数值伪影, 已随加密 k 网格消失.
- 所有体系统一的 6x6x1/3x3x1, 1e-14 Ry DFPT 阈值,
  -10/+6 eV Wannier 窗口, 48x48x1/24x24x1 细网格,
  0.05 eV 积分展宽, 0.8 eV Matsubara 截断, mu*=0.11.
- 未经确认的 [010] 构造方向和作者构思分工;
  将已正式发表的文章继续写作 accepted for publication.

这些内容或与归档/发表稿冲突, 或没有原始证据; 均不能作为已实施计算写入论文.

## 5. 尚未关闭的证据项

1. H2 参考及吸附能账目: 归档 `1.1_energy_atom/Hydrogen/POSCAR`
   是单个孤立 H, 不能代替 H2. 尚未找到对应 H2 总能与两组吸附能
   同一套设置下的完整能量账目. 需要核对原始记录后才能确认数值是否需要更新.
   当前没有据此断言已发表数值错误, 也没有声称已验证其正确.

2. QE/EPW 输入及收敛: 完整递归树未截断;
   `superconductivity/` 和其中 ZIP 主要保留 112 个 anisotropic gap 输出及绘图文件,
   没有找到原 QE/EPW 输入, Wannier 窗口, 精细 k/q 网格, 截断及 alpha2F 文件.
   也不能由 VASP 的 NM 光学记录推定 QE 单层 EPC 的实际自旋设置.
   当前方法链和发表参数已交代, 完整数值复现尚未完成.

3. H-bilayer 的 Gamma 小负频: 原图仍有负频,
   其数值起源与收敛尚待原始力常数/收敛记录或专门计算确认.
   5.5 ps AIMD 不能消除此项不确定性.

跨章回查: 总摘要, Introduction, 全文 Conclusion 与最终回复信中的
AFM/NM-PBE 区别, 稳定性, Tc 方法及光学定性应按本章已核实范围同步.


历史恢复性复核亦已完成: 固定提交可达的 549 个 commits (含 2 个 merge),
32,771 个历史路径及 24,848 个曾删除路径均已筛查; 20 个明确相关历史文本 blob
共 261,055 bytes 经 Git SHA-1 校验. 历版几何 notebook、旧孤立原子目录与
superconductivity 两次导入仍未给出 H2 账目或 QE/EPW 输入.
可恢复的旧 Superconducting gap.ipynb 仅用于能隙绘图.
这个范围不包括不可达提交、已删除远程分支或离线/私有工作目录;
未找到记录不等于证明计算从未做过. 机器记录为 `proj2_history_evidence.json`.

另修复方法引用: Monkhorst--Pack 网格原误引 Methfessel--Paxton 的展宽方法,
现引用 Monkhorst and Pack, Phys. Rev. B 13, 5188 (1976),
并补入原始文献条目 `monkhorst1976special`.

## 6. 最终编译核验

已使用 latexmk 完整编译 `.output/thesis.pdf`, 最终共 330 页.
Project 2 为印刷页 197–234, 由原来的 34 页变为 38 页;
保留原研究章节结构, 新增内容为贡献说明, 必要方法链与结果适用范围.
Figure 6.1 位于 202 页, 早于 203 页开始的 Computation methods;
吸附能公式在 204 页, 吸收图 Figure 6.11 在 218 页,
AIMD 图 Figure 6.22 在 229 页.

已渲染核查结构图位置, 新公式, 光学图与 AIMD 图, 没有超页或遮挡.
无未解析引用, 无新增 overfull box; 原有九个 overfull box 与修改前相同.
16 个章级目录目标全部仍从奇数页开始.
`paper 2-compressed.pdf` 的 SHA256 与修改前一致.
详细机器记录见 `proj12_build_verification.json`.

List of Publications 同步由 accepted 改为已正式发表的 10, 074001 (2026),
并与 Appendix 一起使用实际章节交叉引用.
本记录不将原始数据缺失或未完成的收敛检查列为已经解决.
