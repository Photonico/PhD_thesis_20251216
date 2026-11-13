# Chapter 4：对 DeepSeek report 4 的独立复核

核查日期：2026-09-23。核查快照为当前 `src/fundamentals_c.tex`、相关跨章源文件及 330 页的 `.output/thesis.pdf`。本记录只给出判断与最小修改建议，不修改 TeX 或图件。下述行号对应核查时的源文件；后续应用修改会使行号移动。

## 结论

DeepSeek 抓住了两个仍值得处理的点：Chapter 4 可以更具体地解释 helical edge states 的物理后果；Introduction 的章节路线确实遗漏了 Chapter 4。不过，它对若干关键限定的“缺失”判断已经不符合当前版本，不能据此重新扩写理论章。

建议本轮只补一小段边缘态说明、在已有全布里渊区检查段明确点出 TRIM 也不充分、补两处简短章间指引，并修正符号表的子空间措辞。保留现有 Fu--Kane 路线；不加入论文未使用的 Wilson loop、Wannier centres、Berry curvature 或 Chern-number 教程。Chapter 4 的理论增量约半页至一页，实际页数由整书编译确认。

Project 3 的金属性与拓扑主张仍需要实际计算证据。这是材料研究章节的独立问题，不能通过扩写 Chapter 4 宣称已经解决。

## 一、报告中不应重复采纳的意见

1. **“131 是偶数页”错误。** 当前 Chapter 4 从印码 131、PDF 物理页 165 开始，两者均为奇数。现有 class 层面的 `\cleardoublepage` 已生效，无须在 `thesis.tex` 再加重复分页命令。

2. **“没有等价的全布里渊区警告”已经过时。** 当前 `fundamentals_c.tex:843--848` 已要求二维布里渊区采样、最小间隔附近加密及插值对照，并指出高对称路径只覆盖部分区域。第 245--246 行也明确图中的一维 cuts 不能取代二维检查。可以补上“TRIM 也不充分”几个词，但不应将已有内容重新写一遍。

3. **“宇称乘积本身不能确立结论的警告已完全消失”已经过时。** 第 861 行直接说明：若选定谱子空间尚未证明隔离，宇称乘积本身不能建立该子空间的 $Z_2$ invariant。第 864--875 行继续区分绝缘填充、间接重叠的金属和子空间边界接触。这里的要求实际上比“不是拓扑绝缘体”的单句警告更完整。精确字符串搜索没有命中旧句，不等于物理限定不存在。

4. **“Chapter 4 没有 X/Y 等价的对称性条件”已经过时。** 第 800--804 行既要求 actual structure，又给出了“绕所选反演中心的四重旋转”这一充分情形；第 808--810 行要求在对称性和反演约定核实之前保留全部四个 TRIM 因子。当前表述足够谨慎。方形布里渊区本身不能替代原子结构的对称性检查。

5. **“必须再写简并时单带 Berry phase 没有定义”不宜照抄。** 第 381--385 行已经准确写成：简并子空间本身不唯一规定其中某一单带的 Berry phase。这比笼统的“简并就无定义”更精确：闭合路径内部存在简并点并不使路径上隔离能带的 Berry phase 失效；额外守恒对称性也可能分辨简并子空间中的支路。保留现文。

6. **“缺少全局规范障碍说明”不成立。** 第 700--709 行已经区分：非平庸 $Z_2$ 阻碍的是满足时间反演配对条件的全局光滑基，而不是所有光滑基，也不是光滑 projector。这个限定与 Soluyanov--Vanderbilt 的原文一致，不应退化成“非平庸拓扑没有全局光滑规范”。[原始论文](https://arxiv.org/abs/1009.1415)

7. **“publications/appendix 仍写旧章号”已经修复。** 两个源文件目前都用 `\ref{cha:project_bilayers}`、`\ref{cha:project_boron}`、`\ref{cha:project_beryllene}`。当前 PDF 对应 5、6、7，无须再次改动。

8. **“140、145 两页都半空”不符合当前 PDF。** 印码 140 确实较空，由下一节前的作者惯用 `\newpage` 造成；印码 145 当前正常排满。不能为了消除一页留白打破作者在 fundamentals 中按节起页的既定体例，也不能借此把新理论内容塞入没有逻辑关联的位置。

9. **Wilson loop、Wannier centres、Berry curvature 不是本论文 Fu--Kane 分析的缺件。** 原始 Fu--Kane 论文确实给出反演对称情况下的宇称捷径；本文已说明其成立前提与适用对象。增加另一整套数值拓扑方法既不能替代实际的直接间隔证据，也不符合“未涉及的知识点不讲”的用户范围。可在未来真正采用该方法时再写。[Fu--Kane 原始论文，sections II--III](https://arxiv.org/abs/cond-mat/0611341)

## 二、建议本轮采纳的最小修改

### A. 具体说明 helical edge states，并保持适用条件

原始 Examiner 1 PDF 的要求是解释 topology 的重要性和 non-trivial $Z_2$ 的物理后果，并未使用 `dissipationless helical edge states` 这个示例。这个更强的用语来自合并解读稿。应直接满足 examiner 的物理要求，不将“无耗散”写成无条件承诺。

建议在 `fundamentals_c.tex` 第 711--716 行原有边界段基础上作以下替换。保留原来的绝缘填充、单粒子和时间反演前提，并用一个简短 Dirac 公式呼应此前的 antiunitary/Kramers 推导：

```tex
For an insulating filling, this distinction has a physical consequence at an interface with a topologically trivial insulator.
Within the non-interacting description and with time-reversal symmetry preserved at the boundary,
the non-trivial phase supports an odd number of Kramers pairs of edge modes connecting the bulk bands~\cite{kane2005z2}.
These edge states are helical:
time-reversed partners propagate in opposite directions and have opposite spin expectation values.
This relation does not require a conserved spin component.

For a single pair, we consider a static one-electron perturbation $\hat{V}$ that is Hermitian and preserves time reversal.
The same antiunitary relation used in equation~\eqref{kramers_orthogonality_topology} gives:

\begin{equation}
    \bra{\hat{\Theta}\psi}\hat{V}\ket{\psi}=0,
    \qquad
    \hat{V}^{\dagger}=\hat{V},\quad
    [\hat{V},\hat{\Theta}]=0
\label{helical_edge_backscattering_topology}
\end{equation}

here, $\ket{\psi}$ and $\hat{\Theta}\ket{\psi}$ are the two time-reversed edge states.
Thus this perturbation cannot produce elastic backscattering between the partners~\cite{kane2005z2}.
The statement concerns a single edge within the one-electron description;
it does not establish dissipationless transport in the presence of bulk conduction or inelastic processes.
For a metallic filling, the same insulating-edge interpretation cannot be inferred from a parity sign alone,
because bulk states can remain at the Fermi level.
```

物理核验：Kane--Mele 的原始论文明确区分 spin conservation 与 $Z_2$ 稳定性，并讨论一对边缘态的 single-particle elastic backscattering 禁戒；Fu--Kane section II 也限定了该物理图像。这里不宣称任意多对边缘态之间均无散射，也不宣称有限样品的两侧边缘耦合、非弹性过程或金属体态已被计算。[Kane--Mele 原始论文](https://arxiv.org/abs/cond-mat/0506581)

若最终分页需要更紧凑，可以将该矩阵元写成行内公式；无需添加另一张示意图，也无需引入输运量子或模型 hamiltonian。

### B. 将已有 full-BZ 段的操作性要求说得更直接

只替换原第 843--844 行，保留后面的实际采样、加密与插值验证段：

```tex
The direct separation has to be checked over the two-dimensional Brillouin zone.
Its positivity at the four TRIM or along a plotted high-symmetry path does not establish the condition throughout that zone.
```

这是数学上的取样范围限定，不暗示本文已经完成密集二维检查，也不暗示四点宇称判据本身要求处处计算宇称。先有隔离子空间与所需对称性，后有四点宇称评价，两步应明确区分。Fu--Kane 对负间接隙的 Bi/Sb 的分析也以全区有限直接间隔为前提。[Fu--Kane section V.A](https://arxiv.org/pdf/cond-mat/0611341)

### C. 只补 Introduction 的缺失指引，不在本轮重写它

在 §1.5 的 Chapter 3 两句之后补：

```tex
Chapter~\ref{cha:fundamentals_c} develops the band-subspace and symmetry conditions for the topological analysis.
It distinguishes the topology of an isolated band subspace from an insulating state at the Fermi level.
```

在 §1.3.2 最后一段，将原本直接指向研究章的最后一句替换为两句：

```tex
Chapter~\ref{cha:fundamentals_c} develops these symmetry and band-isolation conditions.
They provide the basis for assessing the topological interpretation of the beryllium structures considered in chapter~\ref{cha:project_beryllene}.
```

Chapter 2 §2.6 已有指向 Chapter 4 的自然前向说明。章末删除 `and topological` 后只总结本章实际完成的计算方法，是正确分工，不必再插入重复路线图。

### D. 修正符号表的 selected/occupied 分工

目前 `font_matter.tex:168--170` 将宇称因素统一称为 occupied，与 Chapter 4 的一般选定子空间表述不一致。最小替换如下；`N_\mathrm{occ}` 保留其真正的 occupied 含义，不把它重新定义成任意 band count：

```tex
  \item[\(\vec{\Lambda}_i\)] \(i\)th time-reversal-invariant wave vector
  \item[\(N_{\mathrm{p}}\)] Number of Kramers pairs in the selected band subspace at a TRIM
  \item[\(N_{\mathrm{occ}}\)] Number of occupied spinor bands in an insulating state
  \item[\(\xi_{2m}(\vec{\Lambda}_i\,)\)] Inversion parity of one state in the \(m\)th selected Kramers pair at \(\vec{\Lambda}_i\)
  \item[\(\delta_i\)] Product of one parity eigenvalue per selected Kramers pair at \(\vec{\Lambda}_i\)
```

若符号表空间允许，可补 projector、direct/indirect separation、Berry connection/phase 和两个 symmetry operators；这些条目属于检索便利，并非修复物理结论的必要条件，不建议为此强行增页。

## 三、留待 Project 3 证据核查的事项

当前 `project_3_main.tex:542`、第 555--589 行和第 639--649 行仍把结果称作 occupied-state $Z_2$ classification，并直接使用两个 X 点相等。该问题真实存在，但不能据理论段落直接判断每个材料最终结论。

必须核对的内容是：

- 各结构实际计算中固定选取了多少 spinor bands、多少 Kramers pairs；表中的 2、4、6 个宇称符号看起来像 pair counts，但不能未经原输出核查就把它们当作已证实的完整子空间。
- 同一 SOC hamiltonian 下，该 band count 与下一能带的直接间隔是否在完整二维区域内保持正值；原文的 `24 × 24 × 1` self-consistent mesh 不自动等于已经完成 gap-minimum convergence 验证。
- 计算结构的实际反演与旋转操作、所选反演中心、TRIM 坐标和 `irvsp` 输出是否一致；只有在核实 X/Y 对称相关后，才能将两个因子消去。
- 若只能确认宇称乘积，而无法确立隔离子空间，应明确将结果记为待核实的 parity analysis，不能仅以“金属子空间拓扑”更名便保留原来的确定性结论。反之，若直接间隔成立，必须把子空间分类与实际金属输运区分。
- Abstract、Project 3 的章首摘要/结论和整书 conclusion 必须随最终证据同步；没有新计算证据之前不写边缘态已观察到或输运已证实。

这组事项是 examiner 对金属性与拓扑主张的核心疑问。本轮对 Chapter 4 的小改不能代替它，也不应假称已经闭环。

## 四、图形样式的独立提醒

当前 `figures_ch4/figures_ch4.ipynb` 的独立设置是 serif、Computer Modern mathtext、坐标标签 16 pt、ticks/legend 14 pt、tab subtitle 12 pt、线宽 1.5 pt、Matplotlib `round` 文本框与默认 legend 框边色。色板为 `#1478E1`、`#19A0A0`、`#FA8200`、`#8C64E1`。

不能只统一各程序的 rcParams。当前 4.1 的导出宽约 723.66 PDF pt，插入宽为 `0.8\textwidth`，因此它的 source 14 pt 在整书中约为 6.7 pt。不同画布与 TeX 缩放会使相同代码字号产生不同的印刷字号。Project 1/2 的合并图应统一最终页面上的标签、刻度、legend 和 panel tab 尺寸，再由各图输出宽度反算 source 字号。相同量的图宜共用一个 legend、减少重复坐标标签；不能靠把整张图缩小来容纳多组重复 legend。

本记录没有修改任何数据、图像、正文或论文结论。

## 五、本轮最终实施状态

上述 A–D 的最小文字方案已应用至 TeX，中文通读稿已同步。用户现有两张图的数据和绘图文件保持；为统一最终印刷字号，只将 4.1 的 TeX 插图比例改为正文全宽、4.2 改为 0.75 正文宽。第 4 节记录的原始 0.8 比例属于修改前状态。

整本 thesis 编译成功。Chapter 4 为正文第 131–152 页，较本轮开始增加 2 页（包括正常章间留白），满足篇幅上限。新式为 (4.30)，后续公式编号和中文稿已同步。单对 helical states 的矩阵元及其限定经独立复核，图 4.1/4.2 和相关正文页已检查。第三节列出的 Project 3 材料证据仍留待该项目核查，不视为本轮已解决。

最终收尾另补 SOC、TRIM 两个缩略语。旧示意图验证脚本的检查代码已适应 notebook 的内联 internal-pair 表达式；在禁止保存图件的内存执行中，四种间隔、内部接触、两类 TRIM 和周期副本断言全部通过，用户 Notebook/PDF 哈希不变。补缩略语后整书仍为 332 页，章节起页及 Chapter 4 的两页增长上限不变。
