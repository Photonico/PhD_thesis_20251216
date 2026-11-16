# Comparison

## codex gpt 6.0 sol

比较日期：2026-11-16。依据 Lu 的 [thesis.pdf](../.output/thesis.pdf)、Ollie 的 [ollie.pdf](ollie.pdf) 及 Lu 当前源码。以下均为印刷页码；PDF 物理页分别加 44、12。本次离线阅读与源码抽查未重跑计算。Ollie 未提供源码，代码规范只能评价 Lu，不能作双边排名。

**总体判断：Ollie 的研究主线、方法基准与机制论证更集中；Lu 的理论教学、物理覆盖与部分数值交叉检查更突出。写作上，Lu 偏讲授和推导，Ollie 偏结果汇报与解释；成品排版上，我更偏向 Lu 当前版本的字体协调和克制设计。**

**1. 研究页幅接近，总页数不能直接代表研究分量。**

Lu 共 420 页，Ollie 共 224 页。Lu 的基础理论与理论附录合计 162 页，Ollie 的背景章为 26 页；Ollie 的原创熵方法属于研究章，不能漏算。

- Lu：第 5 章 pp115–160，46 页；第 6 章 pp161–200，40 页；第 7 章 pp201–264，64 页。合计 **150 页，已含 58 页章内补充材料**。
- Ollie：第 3–5 章分别为 39、47、32 页，加上 37 页研究支撑附录，合计 **155 页**。

这些是页幅，不等于字数、工作量或贡献相等。两篇论文的研究体量应通过具体贡献评价。

**2. Ollie 的三个研究更像连续推进，Lu 的新版综合已经建立共同物理问题。**

Ollie 从溶液熵与自由能方法，推进到基底、缺陷和固定方式，再到连接体与活性位点设计。前章结果会推动后章选择。完整溶液熵处理并未覆盖所有固定化吸附态，但研究之间的依赖清楚。

Lu 横跨界面、维度降低、氢化、磁性、光学、拓扑和配对，读者切换问题的成本较高。第 8.2 节已将这些内容通过成键、配位、电子态和方向相关响应连接起来（pp271–273）；应让这一共同问题更早参与各章的组织。

原创贡献类型也不同：Ollie 扩展并校准已有溶液熵框架；Lu 主要贡献在材料结构、电子态和响应预测。教材推导的长度不等于原创方法贡献，多个由同一介电函数导出的光学量也不构成彼此独立的发现。

**3. 六个研究主体的强项与主要边界。**

- **Lu 第 5 章：基础完整，方法相对常规。** 界面电荷、电子结构、PBE/HSE06、各向异性光谱及收敛材料较齐全（pp119–139、144–154）。更值得加强的是特定成键与跃迁的解释，压缩依光谱种类逐项描述。局部带隙与全局绝缘、模型带对齐与实际接触输运需要分清。
- **Lu 第 6 章：机制和验证最均衡。** 平带与高 DOS 引出磁态和畸变检验，再定位到顶点 B 自旋；固定自旋、FM/AFM、r²SCAN、结构破缺及跨代码比较有实质内容（pp177–180、196–197）。AFM–FM 能差仍是零温比较，氢终止双层近 Γ 虚频仍待判定，短时 AIMD 只支持轨迹内存续。
- **Lu 第 7 章：覆盖最广，关键预测的条件也最多。** 软模、氢化自由能、竞争结构、拓扑和 EPC 检查提高了可信度。需把不同结构参考、能量尺度与各项结论对应起来，不能仅凭最高 Tc 判断其已比第 6 章更完备。
- **Ollie 第 3 章：方法基准最鲜明。** 56 个分子的 TΔS MAE 约由 0.09 降至 0.07 eV，优化气相缩放基准为 0.08 eV（p59）。修正与评价使用同一数据集，未见独立留出集；21/56 达到文中 0.04 eV 阈值，不能概括为普遍达到化学精度。
- **Ollie 第 4 章：对照设计和机制推进较强。** 苯模型与完整催化剂、曲率、缺陷、电荷、连接体和自由能修正逐项比较。pp98–100 从电荷解释不足转向 Co 的 d 轨道，推进自然；文献 TOF 排序主要提供定性支持。
- **Ollie 第 5 章：连接设计进一步进入反应路径。** 包含稳定性、轨道、还原电位和替代解释检验。但势垒来自约束坐标扫描，并非 NEB 或严格鞍点核验（pp142–144）；固定电荷与预吸附 H 限定了路径，NH₂ 连接体的理论/实验稳定性差异仍未解决。

**4. 验证的强项不同，第 7 章需要守住三项结论的边界。**

Ollie 有较明确的实验相关基准，但存在同集拟合、理论与实验载体不同、不同实验条件间比较等限制。Lu 的多泛函、磁态、代码、网格和拓扑方法检查较深入，但内部收敛、理论间一致与实验验证提供的支持不同。

- **稳定性：** 单模量子分析未包含模式间耦合；吸附放热、氢化学势下稳定、竞争结构与动力学存续应分别判断（pp216–219、249–251）。
- **拓扑：** 非平庸子空间的约 1 meV SOC 隙位于 EF 上方约 1.2–2.7 eV，中性体系仍是金属。它是条件性带子空间结果；独立 SOC 尺度收敛和全布里渊区 HSE06+SOC 隔离仍是后续检查（pp224–225、252）。
- **超导：** 2H-β 的各向异性 Migdal–Eliashberg Tc≈31.7 K，μ*=0.13，采用 PBE+D3 结构和 40 cm⁻¹ 低频阈值（pp227–228）。已有同阈值网格比较（pp255–257），仍需充分说明低频贡献的物理归属。配对尺度与二维相干转变应区分。

这些边界决定措辞强度，不要求博士论文完成所有后续研究。

**5. 写作风格：Lu 的个人节奏更鲜明，Ollie 的研究转场更直接。**

两人都用 we。Lu 理论章多用 introduce、define、obtain、recall，常按“物理动作→命名公式→here 解释符号→说明作用”展开，短段和明确路标适合跟读（pp43–48、75–78）。Ollie 多用 find、observe、figure shows，从结果进入解释；pp98–100 的“描述符不足→进一步检查→机制”尤其有效，方法段则有时较密集。

Lu 的主要问题是重复路标和释义：pp35–45 多次重述辅助体系，pp73–77 多次预告同一光学路线。章间声音也有差异：第 2/3 章偏推导，第 5/6 章偏依图叙述，第 7/8 章条件说明较密。统一风格需要统一信息推进方式，单纯增加 we 效果有限。

当前抽样英文中，Lu 的句法与术语较稳定；Ollie 亦有 “can exists”“barriers where obtained”等错误。Lu 应保留推导式个人声音，集中必要条件，减少反复自我限定。写作规范文件包含目标，不能将其中旧统计当作现稿已经达标的证据；文风也不能可靠鉴定 AI 来源。

**6. 代码规范：Lu 已有可复用工作流，工程规范仍分层。**

**LaTeX 源码：** 章节与 SI 分文件、常用宏集中，描述性标签、正体下标、`\qty` 和 `\eqref` 提高可维护性（[主文件](../thesis.tex#L407)、[符号示例](../src/fundamentals_a.tex#L906)）。但主文件与类文件都定义章节样式，存在多层覆盖；重复宏包、旧 `style/bib.sty` 与 biblatex 并存，增加维护负担（[导言区](../thesis.tex#L33)、[旧引用定义](../style/bib.sty#L10)）。标签体系和一句一行习惯尚未完全统一。这些是源码整理问题，不能据此断言成品有错。

**Python 分析：** `vmatplot` 已复用公共绘图和转换函数；新 [regenerate_optics.py](../figures_ch3/regenerate_optics.py#L29) 固定输入 commit/SHA256、记录软件版本与输出哈希，[verify_optics.py](../figures_ch3/verify_optics.py#L157) 对曲线和残差作专项验证。旧库同时保留 alpha/beta/dev/backup，多处关闭 pylint 检查，部分模块很长；本次未找到统一依赖与格式化配置。旧 [linear_optical_properties.py](../vmatplot/linear_optical_properties.py#L28) 将普通 Planck 常数数值命名为 `hbar`，也提示物理量名称和单位需要统一；这里未追溯其调用链来判断图值。

因此，较准确的评价是“部分新流程可审计，旧研究库仍需整理”，不能说整个软件库都经过测试。仅有 Ollie PDF，也不能判断他的代码规范优劣。

**7. LaTeX 审美：我更偏向 Lu 当前版的整体协调；Ollie 的部分图更醒目。**

Lu 的 Latin Modern 正文与数学字形较协调，左对齐章标题、适度留白、小型大写页眉，以及蓝/紫/绿的克制链接配色，形成较统一的学术专著感（例如 p17、p102）。Ollie 的 Times 风格正文、居中章标题和横线更接近传统学位模板（p6）。这是审美判断，两套方案都成立。

Lu 的强项是公式对齐、符号和单位的细节，以及 Fig4.1 这类直接帮助理解的示意图。弱项是部分多面板图的字、图例和细线偏小，黄绿曲线在白底上较淡（p237）；Ollie 的部分图内标签更大，快速读图更容易（p98）。字号和对比度应按最终印刷尺寸判断，而不是只看原始图文件。

给定 Ollie 版另有 6 处未解析引用标记；Lu 版文本扫描未检出同类标记。这是校对状态差异，不等于所有链接已正确。成品美观与 LaTeX 工程整洁度也应分别评价。

**8. 完成度与最值得改进的方向。**

Lu 第 8.2–8.4 节的综合、限制与后续问题比 Ollie 的简短结尾更具体（pp271–280；Ollie pp150–153）。依据各自 PDF 的记录，Lu 有两章已发表、一章稿件；Ollie 三个研究主体均已发表或接收。这里只比较文稿所载完成状态，不按期刊名称倒推质量。Lu 附录 D 也提供了更明确的代码和数据入口，实际可复现性仍需运行检验。

改进优先级：**先稳固第 7 章关键预测的条件，再压缩理论铺垫与逐图复述；用具体疑问和对照组织结果，最后统一源码配置、代码入口和图形可读性。** Lu 最值得保留的是推导教学、第 6 章的机制检验和跨项目综合；最值得向 Ollie 学习的是问题、证据与解释之间的紧密衔接。

## gemini 4.0 carbon

## claude opus 5.5

## deepseek 4.1 flash

依据：`src/` 编译出的 `.output/thesis.pdf`（420 页）与 `.agents/ollie.pdf`（224 页），以及全文抽取后的统计（LaTeX 命令剥离、按章切分）。页码为印刷页；PDF 物理页分别 +44 与 +12。未重跑任何计算，关于"结果是否成立"的判断只针对论文自身的论述与呈现。

**总判断：Ollie 的论文在一个具体问题上做到了可被实验采纳；Lu 的论文在一个方向上把第一性原理工具箱全部打开。前者赢在叙事与外部锚点，后者赢在技术广度、严谨度与工程完成度。Ollie 的失分几乎都是可修的（排版、语法、参考文献）；Lu 的失分要动结构（三章缝合、缺实验对标）。**

### 1. 量级对照

| 维度 | Lu（2026） | Ollie（2023） |
| --- | --- | --- |
| 总页 / 印刷正文 | 420（前置 43）/ 376 | 224（前置 12）/ 212 |
| 正文词数（PDF 文本层，只计字母词） | 64 600（第 1–8 章 + SI） | 46 700（第 1–6 章） |
| 其中研究章词数 | **33 200**（含 SI） | **37 300** |
| 理论部分 | Ch2–4 = 98 页；附录 A–C = 64 页；**合计 162 页 = 43%** | Ch2 = **26 页 = 12%** |
| 研究正文（不含 SI/附录） | 92 页（Ch5 25 + Ch6 28 + Ch7 39） | 118 页（39 + 47 + 32） |
| 章内 SI / 研究附录 | 58 页（21 + 12 + 25） | 37 页 |
| 总结章 | Ch8，16 页（含 Limitations） | 无；Outlook 4 页 |
| 图 / 表 | 125 / 15 | 48（+ 附录 18）/ 12（+ 附录 20） |
| 编号公式 | 372，其中 **358（96%）在理论章与附录** | ≈90 |
| 参考文献 | 305，中位年份 2016，43% ≥2018 | 260，中位年份 2010，27% ≥2018 |
| 未解析引用 | 0 | **7**（4 处 `figure ??` + 3 处文献标号 `[?]`） |

读法三段。**第一，页数会骗人**：Lu 的 420 页是 Ollie 的 1.9 倍，但研究章词数反而少 11%（33.2k vs 37.3k）——多出来的页数给了理论（22.4k vs 7.6k 词）与 58 页以图为主的 SI。**第二，公式密度暴露了重心**：372 个编号公式里只有 14 个在三个研究章，其余 96% 在理论章与附录；Ollie 全书只有 ≈90 个。**第三，两篇的"研究正文"其实体量相当**（92 页 vs 118 页，33k vs 37k 词），差别不在做了多少事，而在怎么分配篇幅。

### 2. 骨架：因果链 vs 平行案例

Ollie 的三章是递进的因果链：第 3 章先解决"自由能算不准"这个前置障碍（56 分子溶剂化熵基准），第 4 章用这套自由能看催化剂如何键合到石墨烯/碳纳米管的缺陷位，第 5 章在"吡啶链接剂最优"的结论上推广成八种原子级链接剂的筛选。每一章的入口都由上一章的出口开出，读者读完知道作者下一步做什么。

Lu 的三章是平行的案例研究（石墨烯基双层、五角双锥硼 o-B₁₄ 家族、铍烯），共享的是方法论主线（结构改造 → 电子结构 → 响应），不是同一个物理问题。Ch1 §1.4 与 Ch8 §8.2 确实把线缝合了，但缝合发生在叙述层：读完 Ch5 无法预测 Ch6，因为 Ch6 的动机来自硼化学而非 Ch5 的结果。这是"三篇论文装订成册"与"一部专著"的分界，也是唯一一处我认为 Ollie 的结构明确优于 Lu。

体例上反过来：Lu 每章开头有期刊出处、DOI 与逐章的分工声明（Ch7 明写 EPW/QE 计算由 H. Ma 完成），每章有 Data availability 与 SI 小节，全书有 LoF/LoT/符号表、AI 使用声明、代码仓库附录；Ollie 只有一页 List of Publications 的笼统说明，附录以独立文档形式嵌入（页眉在 "REFERENCES" 与 "1 APPENDIX A" 之间跳变，图为位图），且无数据可用性声明。**他没有总结章，这是硬伤**：Lu 的 Ch8 用 16 页做了成果汇总、三线联系、逐条 Limitations 与 Outlook，这在答辩里是防守资源，Ollie 没有对等物。

### 3. 方法学

| | Lu | Ollie |
| --- | --- | --- |
| 代码 | VASP 6.5.0 + QE/EPW（合作者） | VASP 5.4.4 |
| 泛函 | PBE(+D3(BJ))、HSE06、r²SCAN | PBE + D3(BJ) |
| k 采样 | 27³、27×27×1、105×105×1 | **仅 Γ 点** |
| SOC 计算 | 仅 Ch7（能带 + 宇称 + Wilson loop） | 无 |
| 声子 | Ch6/Ch7：DFPT + 有限位移（phonopy / QE-DFPT），q 到 40×40；**Ch5 无** | **无** |
| AIMD | 300 K，5.5 ps | 无 |
| 电子-声子 | EPW + 各向异性 Migdal–Eliashberg + Allen–Dynes + μ\* 扫描 | 无 |
| 拓扑 | Wannier90 + Z2Pack/WannierTools，Wilson loop | 无 |
| 光学 | 独立粒子（LOPTICS），有 k/NBANDS 收敛测试与真空归一化 | 无 |
| 能垒 | **无** | 有（约束坐标扫描，逐点弛豫，固定 Co/C） |
| 外部标定 | 无 | 熵基准、吸附自由能、TOF 排序、氧化还原电位 |

三点判断：

1. **技术广度与严谨度 Lu 明显占优。** 声子、AIMD、电子-声子、拓扑不变量、光学五类计算 Ollie 一项都没有；Lu 还有成组的收敛测试（晶格、k 网格、NBANDS、截断、介电函数），Ollie 的收敛证据只有两张图，且几百原子体系只用 Γ 点，布里渊区误差没有量化。
2. **Ollie 唯一但很实的独立方法贡献在第 3 章。** 把溶剂化熵按平移/转动/振动/空腔形成逐项分解、用 56 分子基准拟合经验修正，将 TΔS 的全集 MAE 从 0.09 压到 0.07 eV（对比 ChemSol 的 0.32、纯振动的 0.43），再回到 CO 在 Co^III^TPP 上的吸附自由能（−0.24 eV vs 实验 −0.26 eV）。要注意他并没有宣称达到化学精度（0.043 eV）：最好的结果仍是阈值的 1.6 倍，经验修正与评价用的是同一套数据，没有独立留出集。Lu 的三个项目里没有任何对等物——所有结果都是"算出来是什么就是什么"，没有一条外部标定。
3. **Ollie 的能垒算法偏弱。** 所谓 "activation barriers" 是固定原子逐点扫描的势能曲线，没有 NEB/dimer，也没有虚频验证（全书无一声子计算，根本验证不了）。这会被催化方向的委员追问。Lu 这边反过来：完全不碰动力学，因此不产生这类主张，但也少了"机理"这一层。

### 4. 验证与可信度

差异不是水平，是学科位置：Ollie 的结果大多能落到一个外部数字上（实验熵、实验自由能、TOF、电位），Lu 的结果几乎全部落在"另一个计算"上。

- **可信度（作为科学断言）Ollie 略高，但高得没有看上去那么多。** 他有外部锚，可是：（i）熵修正与评价用的是同一套 56 分子，是样本内拟合，亚军与冠军只差 0.01 eV；（ii）第 3 章自己测出"只用振动熵"的 MAE 是 0.43 eV，而第 4 章正是用振动熵给所有固定化催化剂的路径排序（正文也承认了这一点）；（iii）TOF 只有 3 个点，排序只能算定性支持。
- **严谨度（作为计算）Lu 明显更高**：收敛测试成体系，Ch8 Limitations 把交换关联泛函、独立粒子光学、真空归一化、声子与分子动力学的适用边界、meV 级能隙的收敛性逐条写清楚。Ollie 没有 Limitations 章节，限制散落在正文。
- **Lu 的过度主张集中在一处**：摘要写 "identify non-trivial ℤ₂ band subspaces"，正文（7.4.5、7.5）已写明这些相在费米面处是金属、非平庸子空间只由 ≈1 meV 能隙隔离，是 conditional screening。摘要把正文的限定丢掉了。

### 5. 写作风格（统计口径：去公式、按章切分）

| 指标 | Lu | Ollie |
| --- | --- | --- |
| 平均句长 | 15.3（Ch1）→ 20.7（Ch5）→ 19.4（Ch7） | 21.6（Ch1）→ **33.6（Ch3）**→ 23.6（Ch5） |
| 句长中位数 | 15–20 | 22–27 |
| 90 分位句长 | 23–31 | **37–51** |
| we/our/us（每千词） | 29.1（Ch1）、22.2（Ch2）、**5.9（Ch5）** | 6.3–15.3 |
| Therefore（每千词） | 0–3.8 | 0–0.6 |
| 宣传性/评价性词（每万词） | 15.2 | 30.0（其中 significant(ly) 10.7） |

- **Lu 的句子短而克制，Ollie 的长而评价性强。** Ollie 第 3 章平均 33.6 词、90 分位 51 词，已经到会掉读者的程度："Values of solvation entropies within chemical accuracy (< 1 kcal/mol or < 0.043 eV) has been demonstrated using molecular dynamics (MD) calculations…"（34 词，且主谓不一致）。
- **Ollie 有可引用的语法硬伤**："This facilities stronger CO₂ adsorption"（摘要）、"Arguments surrounds whether one can actually 'derive'…"、"this is what experiments **where** showing at the time"、"can exists"、"barriers where obtained"、"with all values in this table are in units of eV"、"expect for values in brackets"、"for **there** support"（致谢）、"learned **alot**"。Lu 的正文我做双词与拼写一致性扫描（behaviour 34 / behavior 0；characterize 36 / characterise 0），没有同类问题。
- **Lu 真正的问题是一致性，不是语法。** 按仓库里的风格清单，Ch2/3 与附录 A/B 是作者逐字写的，Ch5/6 主要经师兄润色，Ch1/4/7/8 与附录 C 是后改的。统计完全吻合：Ch2 的 we 密度 22.2、Therefore 3.8，Ch5 只有 5.9 和 0.8。结果是**最像作者、信息量最大的理论章，恰是委员最不会细读的部分；委员最认真读的研究章，是两个人的混合腔。** 这不是学术问题，但认真读完的人会觉得像三份来源不同的手稿。

### 6. 呈现与生产质量

- **矢量 vs 位图。** Lu 的 173 个图形对象里 162 个是 PDF 矢量（另 10 个 PNG、1 个 JPG 是示意图/标识）。Ollie 全书 33 页含嵌入位图（JPEG，约 485–760 ppi），包括正文的多面板 DOS 图与附录的多数图；放大后笔画会糊。
- **编译状态。** Lu：0 未解析引用、0 overfull box。Ollie：7 处断引用（4 处 `figure ??`，3 处文献标号 `[?]`，其中一处是 `[?, 159, 161, 216]`），附录页眉错标 "REFERENCES"，第 2 章公式 (2.4) 把 Hamiltonian 写成 Ĥ = iℏ/2m·∂/∂x + V(x)——量纲不对，而紧接的 (2.5) 又写对了。这是"交稿前没有再编译一遍"级别的失误。
- **章节拼接的痕迹。** Ollie 的三章是期刊稿直接搬入：正文里还留着原稿编号（"the intermediate adsorption section (**section 6**)"、"the CHE model used in **section 3.2**"、"**sections 3.2–3.3**"），4.1 节开头写的是 "**The paper** is organised as follows"。Lu 的三章虽然也是论文移植，但编号与交叉引用都是全书的，没有这类残留。
- **表与图的分工。** Ollie 表多（正文 12 张 + 附录 20 张），把数值摊开便于横向比较；Lu 表少（15），数据集中在曲线里。**这是 Lu 可以直接学的一点：关键数值给一张汇总表，比十张曲线好读。**
- **图内字号。** Lu 的部分多面板图字号偏小、图例挤到画布边缘（如 fundamentals 第 3 章的吸收系数图），需按最终印刷尺寸复核；Ollie 的图内标签反而更大，快速读图更容易。
- **前置页。** Lu 的 LoF/LoT/符号表占 22 页（图注全文收录），前置共 43 页；Ollie 只 12 页。信息更全，但比例偏厚。

### 7. 期刊与产出

Ollie：*J. Chem. Theory Comput.* 17, 7753 (2021)、*J. Phys. Chem. C* 126, 10081 (2022)、*J. Catal.*（接收），另有两篇合作署名（*ACS Catal.*、*Anal. Chem.*），三章全部发表或接收，且背后都有实验组（Jiang 组）。
Lu：*Nanomaterials* 14, 1659 (2024，MDPI)、*Phys. Rev. Materials* 10, 074001 (2026)、*Phys. Rev. B*（在投）。

两者方向不同，不宜按刊名打分；但要承认两点：其一，*Nanomaterials* 是 MDPI 刊，在部分评审眼里会折价，尽管它是同一工作的正式发表版本；其二，Ollie 每一篇都有实验共同作者背书，Lu 三篇全是理论，引用曲线会慢。另外，**Ollie 是 Lu 三篇论文的共同作者，还润色了第 5、6 章**——所以这不是竞争关系，而是"师兄证明了能在一个具体问题上做出可被采纳的结论，师弟证明了能独立覆盖一大片技术并写成一部规范的书"。

### 8. 如果我是委员

**Lu 会被攻击的：**

1. 全文无一处实验标定；B₄C₃、o-B₁₄ 单双层、三层立方铍烯都是纯理论模型，需要一句"这些预测如何被证伪"。连体相 hcp Be 的晶格常数都没有拿来对一次实验，而铍烯其实已被合成，正文没有比对。
2. ℤ₂ 的物理重量被摘要放大（见 §4）。这些相在费米面处是金属，非平庸子空间只由 0.7–1.1 meV 的能隙隔离，而论文自己说这已低于 DFT 精度且未做独立的 SOC 尺度收敛；必须与 7.4.5/7.5 的措辞对齐。
3. **31.7 K 那个数与正文不是同一个晶体。** EPW 用的是加了 D3、晶格常数小 2.4% 的 2H-β 结构，该结构没有软模；而软模分析与结构参数表用的是 PBE 结构。论文两处都写了，但读者得自己拼出"哪条结论属于哪个结构"。委员一定会追问这个，也会追问 40 cm⁻¹ 的低频切除：同一个 40×40 网格上，把低于 40 cm⁻¹ 的模去掉，λ 从 3.06 掉到 1.50，T_c^AD 从 15.1 K 抬到 21.9 K。论文在 SI 里报告了这条对照，但摘要只引了较大的那个数。
4. 超导章没有 α²F(ω)、没有分模 λ_qν、T_c 没有误差棒。对一篇要把 T_c 当卖点的论文，这是最容易被要求补的一张图。
5. Ch5 完全没有声子计算（四个单层、三个双层的动力学稳定性未验证），真空层厚度只在 Table 3.1 间接出现，原子数从未写明。
6. 光学是独立粒子近似：无激子、无 Drude、无局域场，二维金属的"等离激元"判据只靠 Re ε 过零 + 阻尼小；三章用了三套真空归一化、两种吸收单位（nm⁻¹ 与 Å⁻¹）。
7. 没有任何能垒/动力学；氢化与吸附都只是热力学量。
8. 篇幅：162 页理论 + 58 页 SI，研究正文仅 92 页，"把附录 A–C 移到网上"是很自然的建议。
9. 跨章语气不统一（§5 的统计）。

**Ollie 会被攻击的：**（最重的一条）**pH 项算错**——第 3、4 章写 ΔG_pH = k_B T ln(10·pH) 并打印 0.11 eV（pH 7），正确的 k_B T ln(10)·pH 是 0.41 eV，而第 5 章用的正是 0.41 eV；也就是说两个章节里每个质子–电子步系统偏 0.30 eV，而这两章讨论的自由能差正是 0.1–0.2 eV 量级。其余：公式 (2.4) 的 Hamiltonian；无 NEB/无鞍点验证却称 activation barrier；无虚频验证却谈稳定性；几百原子体系仅 Γ 点；没有结论章与 Limitations；语法硬伤；标题许诺 "on Semiconductor Surfaces" 与 "Metalloporphyrins"，而正文基底是石墨烯与碳纳米管、金属只有 Co（"semiconductor" 全篇只出现两次，一次在标题、一次在一条参考文献的刊名里）；无数据/代码可用性声明；附录表格编号错位（正文引用 table B1，印出来是 TABLE B8）、表 A3 出现物理上不可能的数值（乙酸 4.37 eV/K）；摘要 553 词且除"56 个分子"外没有任何数字。

### 9. 建议（按性价比排序）

1. **摘要补一句"金属 + 条件性"，并把 31.7 K 与所用结构（D3 弛豫）绑定**。半小时工作量，直接消掉两个风险点。
2. **每章加 3–5 句"如何用实验检验"**（哪条谱线、哪个能量、哪个温度）。不需要新计算，但这是 Ollie 论文读起来"落地"的原因。最低成本的一条：把 hcp Be 的 a、c 与实验值、铍烯的已合成事实写进去。
3. **Ch8 加一张跨体系综合表**：结构改造（异质结/降维/氢化）→ 电子结构变化 → 光学/超导/拓扑响应 → 可用实验手段。§8.2 现在只有文字，一张表能把三章真正缝起来（方案见 §9.1）。
4. **补 α²F(ω) 与分模 λ_qν 图**，至少对 2H-β 与三层立方两张。这是超导章节的"标准配置"，也是对付"T_c 从哪来"这一问的最直接证据。
5. **考虑把附录 A–C 移出纸质本或压到三分之一**，并把 SI 中最具方法价值的部分（软模分析、Z₂ 的能隙下界）提到正文。
6. **统一文风**：用逐章统计（we 密度 5.9 vs 22.2、句长 20.7 vs 16.0）把 Ch1/4/7/8 与附录 C 对齐到 Ch2/3，重点是信息推进方式，不是单纯加 we。
7. **补一张与其他计算的定量对照表**（hcp Be 晶格常数与实验、BC₃ 带隙、α-铍烯 T_c 与 Li et al. 及 Petrov–Milošević 的争议值），把散在正文的比较集中起来。
8. **细节**：`Table 3.1` 里 chapter 5 的吸收单位是空的、行标题小写与全书 `Chapter~\ref` 不一致；部分多面板图字号偏小、缺 (a)/(b) 分幅标签，图例有裁切，需按印刷尺寸复核；Ch6 有一处 jet 色标，建议换 viridis。

#### 9.1 Conclusion and Outlook 章：还能放什么

诊断（读 `src/conclusion.tex` 全部 353 行）：这一章的**防守**已经很强——§8.2 的五条连接、§8.3 的七段 limitations、正文四处 "conditional" 措辞，都是答辩资产，比 Ollie 的四页 Outlook 强得多。缺的是**进攻**：

- §8.1 用约 2 000 词逐条复述三章各自的结论，委员想横向比较仍需自己翻三章；
- 第一章 §1.4 提的三个研究问题，正文没有一处逐条回答；
- §8.2 停在"观察"层（三个体系各不相同），没有凝练成可迁移的设计规则；
- §8.4 是四条并列的方法清单，没有优先级，也没有一句交给实验组的话；
- anyon 段（第 340–346 行）是全文最后的实质内容，但它是六句里的第三次概念跳跃，读起来像附加物。

结论：**不要增加长度，重新分配长度**——把 §8.1 的复述压掉 1–2 页，换成下面五样。

**（1）一张跨体系总表**（放 §8.1 开头或 §8.2 之前）。收益最大的一处：九个结构 × 五个维度，一页纸抓住全书骨架。

| 章 | 结构 | 电子结构（HSE06，另有注明） | 关键响应 | 附加性质 | 可用实验手段 |
| --- | --- | --- | --- | --- | --- |
| 5 | Graphene-Borophene | 金属 | ~1 eV 可见吸收最强 | 面内低能能量损失峰缺失 | 输运、EELS |
| 5 | Graphene-BC₃ | 半金属，K 点开 50 meV | 亚 eV 面内损失峰 | n 型对齐（Φₙ 0.19 eV） | 输运 |
| 5 | Graphene-B₄C₃ | 半金属，K 点开 20 meV | 5–6 eV 面内 Re ε < 0 | p 型对齐（Φₚ 0.87 eV） | 输运 |
| 6 | 体相 o-B₁₄ | 金属 | zz 可见吸收 | λ = 0.931，T_c^AD 28.2 K | 输运、μSR |
| 6 | 单层 o-B₁₄ | AFM 半导体，0.105 eV | 未计算（非磁参考） | 0.262 μ_B / 顶角 B | 磁化率 |
| 6 | 双层 o-B₁₄ | 0.67 eV 间接带隙 | xx 可见吸收 | — | 光学 |
| 6 | 氢终止双层 | 金属 | yy 可见吸收 | λ = 1.01，18.5 K | 输运 |
| 7 | α-铍烯 | 金属 | 各向异性，损失谱 | ℤ₂ = 1（1.13 meV 之上） | ARPES |
| 7 | 三层立方铍烯 | 金属 | 面内弱于 bcc | λ = 0.46，3.7 K；ℤ₂ = 1 | 输运 |
| 7 | 2H-α-铍烯 | 6.00 eV 带隙 | 低能区弱而宽 | ΔG_H = −0.08 eV | 光学 |
| 7 | 1H-β / 2H-β | 金属 | 方向性重分布 | 14.2 K / 31.7 K | 输运 |

有了这张表，§8.1 可以从"十段复述"压成"三段解读"，把篇幅让给下面四样。

**（2）一小节直接回答第一章的三个问题**（3–5 句，放 §8.1 开头或 §8.2 开头）。闭环是答辩加分项。按本仓库文体（一句一行、平均 15 词、we 主动态）改写的草稿：

```latex
Firstly, we asked how stacking graphene on a boron-containing layer changes its electronic states and its optical response.
The constituent dispersions remain recognizable in all three bilayers.
The interlayer coupling opens local gaps of \qtyrange{20}{50}{\milli\electronvolt} at the $\mathrm{K}$ point.
The alignment changes from n-type to p-type with the boron-carbide species.
Next, we asked how reducing the thickness of the o-\ce{B14} framework and terminating its surfaces change its bonding.
The bilayer becomes a semiconductor with a gap of \qty{0.67}{\electronvolt}.
The monolayer supports an antiferromagnetic state.
Hydrogen termination restores a metallic sheet with the stronger electron-phonon coupling.
Finally, we asked how the layer geometry and the hydrogen arrangement change the stability, the topology, and the pairing of beryllene.
Hydrogen drives 2H-$\alpha$-beryllene into a wide-gap semiconductor.
The selected subspaces carry non-trivial indices under an explicit isolation condition.
The pairing reaches \qty{31.7}{\kelvin} in 2H-$\beta$-beryllene.
These three answers share one structure.
A change in the atomic arrangement alters the bonding environment, and the electronic and vibrational states follow from that environment.
```

**（3）把 §8.2 从"观察"升级成 3–4 条设计规则**。现在是六个并列段落，读完记住的是"各处都不一样"；改成规则，读者才能带走：

```latex
The comparisons also yield conditions that transfer between structures.
Firstly, the effect of hydrogen follows the filling of the parent states rather than the coverage alone.
2H-$\alpha$-beryllene opens a gap of \qty{6.00}{\electronvolt}, while the hydrogen-functionalized $\beta$-beryllene sheets remain metallic under a comparable coverage.
Secondly, an interface preserves the constituent dispersions while it changes their alignment.
The graphene-derived bands survive in all three bilayers.
The alignment reverses with the boron-carbide species.
Thirdly, reduction of dimensionality selects the direction of the optical response.
The largest visible absorption occurs in $xx$ for the pristine bilayer, in $yy$ for the terminated bilayer, and in $zz$ for the bulk.
Each condition names the structural coordinate that controls the property.
Each one can be tested by comparing two structures that differ only in that coordinate.
```

**（4）加一段"相对已有工作的增量"**（6–8 句，放 §8.1 末尾）。现在"哪条是复现、哪条是新预言"分散在各章；集中成一段，顺带修掉摘要把 ℤ₂ 放大的问题：明确写 α/β 的拓扑是复现 Li et al. 的结论，新意在三层立方相与氢化相。

**（5）Outlook 加"如果只做一件事"和"什么结果能证伪"**。现在 §8.4 四条并列、没有顺序。加开头一段（3–5 句）：

```latex
Not every extension carries the same value.
We would begin with the phonon spectrum of the puckered square-layer \ce{BeH2} candidate.
Its electronic energy lies \qty{38}{\milli\electronvolt} below 2H-$\alpha$-beryllene, so the stability of the triangular sheet depends on that comparison.
We would then resolve the near-$\Gamma$ instability of 1H-$\beta$-beryllene.
The present assignment rests on interpolated force constants.
The low-frequency part of the coupling in 2H-$\beta$-beryllene would follow.
The reported $\lambda$ changes by a factor of two with the chosen cutoff.
Each calculation answers a question that the preceding one cannot.
```

"什么能证伪"不必单列，并进各小节收尾即可（8.4.2 末尾"若可制备，输运与磁响应可检验"就是好写法）。

**建议删或压的：**

- §8.1 三小节各压到 3–4 段（表已经承担数值），省 1–2 页；
- §8.3 每条限制补一个**量级**（例如"独立粒子谱把起始位置移动约多少 eV"），否则限制读起来像免责声明；
- anyon 段压到 3 句并挪到 8.4.4 末尾，或整段删——它出现在"最后一句"之前，会稀释结尾；
- §8.4 开头的 "the preceding limitations suggest a sequence" 与 §8.3 结尾重复，合并。

一句话：**防守已经写扎实了（做了什么、哪里靠不住），缺的是"这些结果怎么被拿走"——一张表、三个回答、几条规则、一个优先级。**

### 10. 总评

| 维度 | 胜者 |
| --- | --- |
| 选题聚焦与可执行性 | Ollie（明显） |
| 章节逻辑链 | Ollie（明显） |
| 技术广度与计算深度 | **Lu**（明显） |
| 方法严谨性与不确定性 | **Lu**（明显） |
| 与实验的连接 | Ollie（很大） |
| 跨章一致性与自查 | **Lu**（明显：Ollie 的 pH 项在第 3、4 章与第 5 章之间不一致） |
| 排版与生产质量 | **Lu**（很大） |
| 可复现性 | **Lu**（压倒性） |
| 总结与自我批判 | **Lu**（很大） |

两本都能过，但理由不同。Ollie 的论文是"一个博士该有的样子：在真问题上做出实验组愿意接手的结论"；Lu 的论文是"一个博士能做到的上限：把工具箱全部打开，并把过程写清楚到可以复现"。他要补的是写作与生产质量（可修），Lu 要补的是"把三个故事讲成一个故事"以及"至少一个外部锚点"（要动结构）。**Lu 的论文比他的更难读，也比他的更经得起翻；但答辩只有三小时，委员会记住的是叙事，不是附录。**
