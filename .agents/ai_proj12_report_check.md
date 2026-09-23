> 后续更新：2026-09-24 的原数据重画与交叉核对发现了进一步修正，尤其涉及 PDoS、EPW 能隙文件及 Tc 解释。请同时阅读 [本轮记录](ai_proj12_figure_style.md)；本文件保留为上一轮审阅记录。

# Project 1 / Project 2：原始 examiner reports 完成性独立核对

核对依据直接取自 `reports/Lu_Niu_PhD_report_20260824.pdf`（E1，2 页）及 `reports/PhD Examination Report - Lu Niu.docx`（E2），不以 AI 合并报告替代。当前 Project 1 / 2 为 Chapters 5 / 6；原报告称 Chapters 4 / 5。此次为最终编译后的检查，当前整书 330 页，Project 1 为印刷页 151–196，Project 2 为 197–234。页码通过 PDF PageLabels 与 LaTeX labels 核对。

## 原报告确实要求的项目

|来源及要求|当前实际证据|判断|
|---|---|---|
|E1 p.1；E2 Chapter 4：章首明示已发表与本人/合作者贡献|两章 `src/project_1_main.tex:4`、`src/project_2_main.tex:4` 已给出版物与贡献；与 `.agents/proj_contributors.md` 一致。P1 没有把 Catherine 的构思或四人原稿全部冒称本人；P2 明示 Oliver 的 AIMD 指导、Hongyang 的超导指导。|已落实。|
|E1 p.1：区分新预测与既有结构表征|P1 introduction 最后两段明确比较堆叠前后的 band alignment、charge redistribution、optical response，且不声称已制造器件；P2 章首/intro 明确已有 o-B14 预测与本章降维/氢终止研究。|两章范围内已落实。全书 introduction/conclusion 的整合属另一个修改范围。|
|E1 pp.1–2：P1 的合理贡献是结构–性质关系与光学可调性|`project_1_main.tex:87` 附近明确上述贡献和理论研究边界。|已落实。报告的“incremental”是评价，并未要求新实验、增算整套机制或重写已发表结果。|
|E1 p.2：原 Figs 4.29–4.36 图注自足，须识别面板、分量、线型、PBE/HSE、偏振、单位及主要特征|`project_1_SI.tex` 的 S1.17–24 已逐项补足。三幅介电图说明 3×3 行列顺序、实虚线型、材料/PBE/HSE 颜色和低能/高能特征；五幅派生图说明只有 HSE06 对角 xx/yy/zz、三材料颜色、全实线、eV 横轴及量纲。8 张图按现 NPZ 原源重绘、核对矢量曲线。对应最终印刷 pp.191–196 / 物理 pp.225–230。|已落实；最终全书版面回归检查通过。|
|E2 Chapter 4：所有 Project 1 图在印刷版可独立读清，4.29/4.30 只是举例|独立逐个检查 36 个 figure、49 个 assets。修改前部分 legend 仅 2.89–3.61 pt。修改已覆盖全章 band/DOS/PDoS/收敛/光学图、三张结构图标签，以及三张能量面图的面板裁分。光学 25 个当前 PDF 已统一 8 in 原画布、11 pt ticks 和 12 pt legend，全宽最终约 8.27/9.02 pt。完整修订前清单见 `p1_figure_font_inventory.md/json`。|已完成图件修改与最终渲染；实际字号与逐图审核状态见 `proj1_figure_readability.json`。|
|E1 p.2：P2 稳定性、超导和 plasmon 均为预测，不当作实验事实|P2 Abstract、stability、superconductivity、optics、Conclusion 已增加预测及适用范围；光学结果指出负 ε1 不足以证明 plasmon，需 loss 与耗散条件及有限 q 响应。|已落实；根代理也已将 intro 的 “existence of plasmons” 改为候选共振特征，统一前后语气。|
|E1 p.2：凝聚能不是全相图/可合成性证据|P2 凝聚能正文与 conclusion 分别限定 selected-reference comparison 与非完整 thermodynamic phase diagram；稳定性结尾明确不证明实验可合成。|已落实。|
|E1 p.2：负声子陈述矛盾；声子与短 AIMD 区分|`project_2_main.tex:532–553`：pristine 单/双层路径无虚频；氢化单层明显虚频；氢化双层 Γ 附近小负频，数值起源尚未证实；400 K、5.5 ps AIMD 仅支持短时骨架保持。Abstract、SI 图注同样限定。|已落实，未凭猜测宣称加密 k/q 后负频已经消失。|
|E1 p.2：小 AFM–FM 能差须解释|`project_2_main.tex:588` 附近明确 0.02 eV / 14-atom cell，说明小能差与有序温度不等价。|已落实；未采用 AI 猜测的 3.2 meV/atom。|
|E1 p.2：AFM semiconductor 与 optical metallic 描述必须说明参考态及 intraband treatment|`project_2_main.tex:309–312`、`:727` 后说明 non-spin-polarized PBE；AFM HSE06 是另一个电子态；Gaussian smearing 0.01 eV、CSHIFT 0.1 eV，无单独参数化 Drude 项，数值展宽不是实验散射率。低频解释也有限定。|已落实；没有编造 Drude plasma frequency 或 scattering rate。|
|E1 p.2：解释 PBE/HSE06 差异并承认近似|`project_2_main.tex:650–657`：短程 Fock exchange 部分降低自相互作用/离域误差并改变量子态相对能量，不能凭其中任一结果认定实验 gap。|已落实。|
|E1 p.2：DFPT→Wannier→EPW→α²F/λ/ωlog→AD/anisotropic ME 的简明可复现流程|`project_2_main.tex:265–298` 保留已有 QE cutoff、k/q grid、relaxation、B s/p projection 和 μ*=0.13；新增一阶势响应、局域表示插值电子态/电声矩阵元、费米面平均谱函数及 Ch2 公式对应；AD 与 gap-closing ME 分开。结果段分别报告 AD 28.2/18.5 K 与 ME 31.3/24.3 K。|所要求的简明流程已落实。完整 EPW 输入归档未能逐项独立重现仍属证据范围限制；原报告没有要求这次补跑全套 EPW 或补齐每一个 fine-grid 参数。|
|E2 Chapter 5：原 Figure 5.1 在介绍结构后、详细计算模型讨论前引用并呈现|`project_2_main.tex:131–178` 首次介绍结构后 immediately figure + `\FloatBarrier` 再开始 methods。最终 Fig6.1 印刷 p.202 / 物理 p.236，methods 从印刷 p.203 / 物理 p.237。|实际 PDF 已落实，不只是源码前移。|

## 原报告没有直接要求、但查实后为正确性采取的修正

- P1 吸收系数：根据真实 PDF 矢量与原 HDF5 逐条匹配，确认旧图使用 E/h 而不是 E/ℏ，使 α 小了 2π；三处吸收图同步更正为 nm⁻¹。这是额外科学核验，不应包装成 examiner 明示的错误。
- P1 派生光学量：标量公式不能逐个应用于非对角 εij 并赋予独立可观测量意义；派生图只保留对角，完整介电 tensor 仍保留。发现的 opposite-sign off-diagonal pair 保持原数据并标注待核，未擅自数值对称化。
- P1 monolayer reflectivity：当前旧引用 S1.14d 与同源正确公式 12 曲线不符；已有 S1.14d_correct 的 12 曲线全部匹配。更正引用和其字号；原 d 文件保持不动。数值证据已保存 `figures_proj1/optics_sources.json`。
- P1 谱峰文字：用 NPZ 明确 sub-eV sharp loss 是 BC3/B4C3；Boro 的 2/5 eV 说法应指低能 ε1 负区，out-of-plane loss 最大值为约 17.9–18.6 eV；不把负 ε1 单独解释为共振确证。记录于 `.agents/proj1_spectral_checks.json`。
- P2 原 Figure 5.22（现6.22/S2.10）：E2 没有单独点名这张图。AIMD 曲线身份、标题、电子自由能含义和方法参数的查证属于协助回应 E1 稳定性问题的额外证据审查，不能凭裁掉标题就假设轨迹身份。
- P2 optical 的 NBANDS 实际输出、bulk 实际 k 网格、吸收单位等原数据核查，也应与报告原要求分开列。

## 完成边界与交付核验

- E1 的 concise reproducible superconductivity workflow 不等于本次必须重新完成一套 QE/EPW 数值实验。来源未支持的 fine k/q mesh、能窗、展宽或负频收敛结论不可补写成既成事实。
- E2 全图印刷可读性是明文要求，不得仅修 4.29/4.30 或 4.29–4.36 后宣称全章已完成。最终须复核每个实际嵌入 PDF 的字号和渲染，尤其多图同行/多行时的缩放。
- 全书重编译已确认无新 float overflow、S1.13/S1.14 的共享图例出现在同一整体 figure 中、所有 cross-reference 正确；必要时少量分成 continued figures，比压缩字体更符合报告。
- 这里没有把 Chapter 1 literature review、全书 Conclusion 的 general limitations、Project 3 要求列成 Project 1/2 本轮未完成项；它们仍需在各自阶段处理。

## 当前图注与版式对应复核

- 逐个读完 P1 所有 figure 环境，没有发现现图版与 caption 的 left/right、upper/lower、行列次序互换。主图 1.8 已改 upper schematic / lower band plot；主图 1.12 是 upper absorption / lower loss，正确。主图 1.10/1.11 保留了 real/imag 两行和 xx/zz/xy 三列。
- S1.13 四材料仍为 BC3、Borophene、B4C3、Graphene 自上而下；实线/虚线含义已补进 caption，与图外共享图例一致。S1.14 顺序仍为 absorption/loss/n/R/kappa，correct reflectivity 引用已生效。
- S1.17–19 的 row order 与程序 components 数组逐项一致；S1.20–24 的 left-to-right xx,yy,zz 与实际三面板一致。
- 根代理对 S1.4/5/6 使用原 PDF 的 panel 裁分与 ContinuedFloat；其 caption 原本没有面板 left/right 说明，因此没有遗留方位错误。最终 PDF 已独立确认 11 个裁框保留对应结构的原始面板标题、轴、色条和极值标记。
- 若 S1.14 需要拆页，不可让第一页无材料识别；可在两页分别保留 native legend 或短 caption 直接列颜色。当前单页整体则共享底部 legend 足够。

## 当前版本的收尾审计（2026-09-24）

重新直接阅读两份原始 examiner reports，并以当前 TeX、图件、Notebook 及整书 PDF 为准，核对本轮 Chapter 4、Project 1、Project 2 的完成条件。以上旧页码、画布参数和旧图组布局属于前一轮记录，当前配置及逐图哈希以 `ai_proj12_figure_style.md` 和 `proj12_figure_style_verification.json` 为准。

- Project 1：章首发表与贡献声明和 `proj_contributors.md` 一致；保留原有 13 个 section/subsection。研究定位、计算方法、光学近似与张量边界已补充。S1.17–24 的八张指定图注已逐项说明分量、泛函、偏振、颜色、线型、单位和特征；36 张现用图全部完成统一绘制及页面审阅。合并图的空间顺序已重新逐项核对。
- Project 2：章首贡献和结构图前移已落实；AFM–FM 的约 0.02 eV 明确按 14 原子胞比较；声子、小负频、短时 AIMD、相对能量与可合成性分别表述。正文明确 NM-PBE 光学参考、数值展宽和未额外加入参数化 Drude 项。DFPT、Wannier、EPW、谱函数、耦合强度和两类 Tc 方法已连接，后处理发现的温度读取问题及精确 Tc 证据限制已同步到图与结论。
- 收尾实际修正：Project 1 Schottky 图注由旧的 upper/lower 改为实际的 panels (a)/(b)；Project 2 SI 将 S2.16 正确称为 spin-resolved total DoS，并明确 S2.12 是各体系 PBE total DoS。未改动数据或再生成不必要的图像。
- Chapter 4：已采纳的三份初始报告与 report4 要求均落实；隔离子空间与金属填充、TRIM 与全 BZ、Kramers 配对、helical 条件及 X/Y 的实际对称性要求明确。中文 34 组公式与英文一致；SOC、TRIM 已补入缩略语表。原样保留用户图件，当前模型在内存中执行数值断言，未重写 Notebook 或图像。
- 最新整书编译为 332 页，Ch4 为印码 131–152（最后一页为正常章间留白），本轮增长 2 页；所有章节级内容仍从奇数页开始。没有未定义引用或文献、超高浮动图或新增 overfull 警告。新增缩略语与三处文字修正的最终页面已渲染检查。
- 两本源仓库 Notebook 均执行验证，分别覆盖 36 / 28 张图；64 张 PDF 与 Thesis 副本一致，字体缩放和边界检查通过。原始计算、发表稿和用户当前 Chapter 4 绘图文件未被覆盖。

本轮完成的是上述三个章节的修改与图件交付，不表示所有计算结果已被独立复现。H2 参考能量账目、完整 QE/EPW 输入及小负声子的收敛证据仍缺；Project 3 的全 BZ 子空间证据及引言最终对齐仍按原约定留待后续阶段。这些不列为已验证或已关闭。
