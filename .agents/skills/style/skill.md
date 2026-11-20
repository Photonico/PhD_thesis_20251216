---
name: style
description: >-
  Lu Niu's own English writing style for the PhD thesis on light-element xenes
  (DFT, linear optical response, band topology), grounded strictly in the pure
  hand-written units verified as human (Chapter 2A, Chapter 2B, Appendix A1,
  Appendix A2, and Appendix D) and contrasted against AI-edited chapters. Load
  it before drafting, de-AI-ing, rewriting, polishing, or reviewing any English
  prose or LaTeX in this repository, including chapters, appendices, abstract,
  captions, and replies to examiners, and whenever the user asks for text
  "in my style".
---

# Lu Niu 论文真实写作风格与去 AI 痕指南

本文件严格依据经 AI 检测验证为纯人工 (human) 的五个纯手搓单元归纳作者本人的英文学术写作风格, 并与仓库中被检出为 ai 或 mix 的章节做定量对照, 用于后续文本的去 AI 味儿 (de-AI), 续写, 改写与审读.
原文范例和改写示例见 `references/examples.md` (其中部分节选来自 `ch3` 和 `appB`, 仅作公式格式与特定局部参考, 散文句式以本文件第 0 至 3 节为准).

---

## 0. 纯手搓基准语料与检测对照 (`.output/.parts/check.txt`)

### 0.1 纯手搓基准单元 (human, 唯一风格依据)

五个纯手搓单元合计约 11,800 个正文词, 754 个句子, 218 个行间公式.

`ch2A` (`source/fundamentals_a.tex`, 第 1–593 行): 第 2 章导言与 2.1 节 (量子力学中的密度泛函与 Hohenberg--Kohn 定理).

`ch2B` (`source/fundamentals_a.tex`, 第 594–1479 行): 第 2 章 2.2.1–2.2.6 节 (辅助体系与 Kohn--Sham 理论框架, 至式 `v_\mathrm{KS}^{(0)}(x)=v_\mathrm{ext}(x)`).

`appA1` (`source/appendix_quantum.tex`, 第 1–501 行): 附录 A 导言与 A1 节 (时间演化, 多体 Schrödinger 方程, Heisenberg 绘景与连续性方程).

`appA2` (`source/appendix_quantum.tex`, 第 502 行至末尾): 附录 A 的 A2–A4 节 (约化密度, 泛函定义, Thomas--Fermi 方法及其局限).

`appD` (`source/appendix.tex`, 全章): 附录 D (源代码与数据分析说明, 代表无公式的客观说明与文档语体).

### 0.2 非基准单元 (严禁作为作者散文风格来源)

旧版风格文档曾误把 `ch2C`, `ch3`, `appB` 一并当作纯手写语料, 导致把 Claude Opus 5.5 的改写习惯当成了作者习惯.

ai 单元为 `ch1` (`source/introduction.tex`) 和 `appC` (`source/appendix_topology.tex`).
mix 单元为 `ch2C` (`source/fundamentals_a.tex` 第 1480 行至末尾, 其中 2.4 节为典型 AI 改写) 和 `appB` (`source/appendix_electrodynamics.tex`).
第 3, 4, 7, 8 章含大量 AI 重写或待核查段落; 第 5, 6 章经师兄深度润色.

### 0.3 纯手搓 (human) 与 AI 改写 (ch1 + appC + ch2.4) 定量对照

单位除注明外均为每 1000 正文词 (已剥离公式与宏命令):

| 指标 / 句式特征 | 纯手搓 human (11.8k 词) | AI 单元 ch1+appC+2.4 (10.1k 词) | 诊断结论 |
| --- | --- | --- | --- |
| 句长标准差 SD / 变异系数 CV (突发性) | SD 6.5–9.5 (`appD` 19.6), CV 0.43–0.90 | SD 4.8–6.1, CV 0.32–0.39 | 头号差异: 手搓长短句交错; AI 句长被削平在 12–18 词 |
| 极短句 ($\le 8$ 词) / 长句 ($\ge 30$ 词) 占比 | 短句 9.5%–15.7% / 长句 3.3%–18.2% | `ch2.4` 短句 3.4% / 长句 0.0% | 禁止把所有大于 25 词的有机长句机械拆成定长短句 |
| 句首 `Therefore, we` vs 句中 `We therefore` | `Therefore, we` 1.10 vs `We therefore` 0.17 | `Therefore, we` 0.00 vs `We therefore` 1.28 | 作者把逻辑副词放句首加逗号; AI 习惯塞在 `We` 后面 |
| 句首 `Then, we` / `Now, we` vs `We then` / `We now` | 句首 0.76 vs 句中 0.76 | 句首 0.00 vs 句中 3.65 | `We then` / `We now` 连续刷屏是典型 AI 痕迹 |
| `Accordingly,` / `Hence` / `Moreover,` | 1.27 / 1.02 / 0.93 | 0.20 / 0.00 / 0.00 | 这组逻辑连接词是作者高频真迹, AI 几乎不用 |
| `Let us ...` / `Recall ...` / `According to ...` | 1.02 / 0.93 / 0.51 | 0.20 / 0.10 / 0.00 | 作者典型的讲义式推导引导语 |
| `In what follows,` / `Up to now,` | 0.68 / 0.25 | 0.00 / 0.00 | 作者真实的阶段切换语 |
| `In principle,` / `In practice,` / `In particular,` | 0.51 / 0.34 / 0.42 | 0.00 / 0.00 / 0.10 | 作者真实高频限定语, 严禁按旧规删除 |
| `In this sense,` / `In other words,` / `in terms of` | 0.34 / 0.34 / 0.76 | 0.00 / 0.00 / 0.10 | 作者常用的物理换述方式 |
| `can be` + 过去分词 (`expressed/written/regarded as`) | 3.40 (40 次) | 0.40 (4 次) | 关键反转: 作者大量使用自然数学被动情态; AI 强行改成物作主语反而极假 |
| `it is` (`convenient/instructive/important to`) | 1.44 (17 次) | 0.10 (1 次) | 关键反转: 作者自然使用 `it is ... to`, 严禁一刀切禁用 |
| 对照词: `while` vs `whereas` | `while` 0.85 vs `whereas` 0.08 (仅 1 次) | `while` 2.17 vs `whereas` 0.79 (`ch3` 达 2.14) | 严禁滥用 `whereas` 对照句, 作者几乎只用 `while` |
| 替代词: `rather than` vs `instead` | `rather than` 0.59 vs `instead` 0.08 (仅 1 次) | `rather than` 0.30 vs `instead` 0.89 | 少用句首 `Instead,`, 优先用句中 `rather than` |
| `The previous section established...` 模板 | 仅 1 次 | AI/Mix 合计 16 次 | 这是 Claude 模板, 不是作者的节首固定公式 |
| `characterize(s)` | 0.00 (0 次) | 0.69 (7 次) | `characterize` 是纯 AI 词, 作者不用 |

* 其实作者不排斥 characterize, since;

---

## 1. 去 AI 味儿 (De-AI) 原则与工作流

最小化手术原则: 去 AI 痕时, 只修改被检测器标黄, 标橙或存在明显 AI 模板的句子, 未标出 AI 痕迹的原句一字不动.

先剥离 LaTeX 宏再送检: 外部 AI 检测器会被 `\ce{BC3}`, `\qty{1.822}{\electronvolt}`, `\eqref{}` 等宏切碎 token 分布而产生误报 (false positive). 检测时先替换成纯文本, 如 `BC3` 和 `1.822 eV`.

恢复句长突发性 (burstiness), 拒绝大约 15 词定长切句: AI 最致命的统计指纹是把每句话都切成 12–18 词的齐整短句 (`Subject + verb + object.`), 导致句长方差暴跌. 作者真实节奏是长短错落, 既有 5–9 词的干脆判断句 (`The electron density is an obvious choice.`, `Next, we switch to the coordinate representation.`), 也有 25–38 词的完整复合句 (带条件状语, `which` 非限制性定语从句, `namely that ...` 同位语, 或真实项目列举).

把 `We <副词> <动词>` 改回作者习惯的句首状语加逗号: 少写 `We therefore ...`, `We then ...`, `We now ...`, `We next ...`. 改回作者高频写法 `Therefore, we ...`, `Accordingly, ...`, `Consequently, ...`, `Hence, ...`, `Then, we ...`, `Now, we ...`, `Next, we ...`, `Subsequently, we ...`, 或前置方法状语 `Through the calculation of ..., we ...`, `From ..., we ...`, `By substituting ..., we ...`.

解除对自然数学被动句和 `it is` 的错误禁令: 不要让所有无生命名词强行充当施事主语去演动作片 (如 `This step compresses...`, `The factor converts...`, `The limitation motivates...`). 恢复作者自然的学术表达, 包括 `can be expressed as`, `can be written as`, `can be regarded as`, `is uniquely determined by`, `is commonly referred to as`, 以及 `It is convenient/instructive to ...`.

---

## 2. 语体分层与篇章结构

作者在五个纯手搓单元中展现出两种清晰的自然语体, 按章节性质选用, 不跨语体硬套模板.

### 2.1 理论与推导语体 (`ch2A`, `ch2B`, `appA1`, `appA2`)

理论推导部分以讲义式的 `we` 为叙述主线 (约 20–31 次/千词), 带读者沿一条推导路线前进.

章首导言包含四个常见成分. 先用定位句交代本章位置, 例如 `We start our discussion of the fundamentals in this chapter by introducing ...` 或 `In this appendix, we develop the basic quantum-mechanical descriptions used in chapter~\ref{...}.`. 随后用 `In principle, ...` 与 `However, as ..., direct calculation becomes impractical ...` 指出核心矛盾并给出方法路线. 如有资料来源说明则直接交代, 例如 `This chapter partly draws on my notes from ...`. 最后的路线图段落用 `We start from ...`, `With ... as the central variable, we construct ...`, `Finally, section~\ref{...} demonstrates ...`, `In addition, appendix~\ref{...} collects ...` 自然串联, 不写 `Readers interested in X can proceed directly to Y` 这类跳读元话语. 故事引子仅在附录大章开头偶一为之 (`Imagine that we are watching ... Something has changed. But how do we describe this evolution in physical language?`), 随后立即回到物理史与核心方程.

节与小节的开头多样化切入, 不套用千篇一律的 `The previous section established X. We now turn to Y.` 模板. 常见切入方式有四类. 第一类是直接点出物理便利性或现实约束, 例如 `In quantum mechanics, it is often convenient to shift the basic variable from ... to ...`, `In practical many-body problems, an exact treatment of the hamiltonian is impossible, and approximation is inevitable. This motivates a reformulation in terms of a simpler basic variable. The electron density is an obvious choice.`, 或 `In practical applications, we have to solve the Kohn--Sham equations~\eqref{...}.`. 第二类是设定假设或考察对象, 例如 `Suppose that the hamiltonian is independent of time, so that it does not depend explicitly on $t$.`, `Consider the operator for the measurement ..., and the ground-state $N$-body wave function ...`, 或 `For a many-body system, it is instructive to contrast the exact density functional with ...`. 第三类是阶段回顾, 例如 `Up to now, we have mainly discussed a single-particle quantum system ...` 或 `After the general framework of the Kohn--Sham construction has been established through equations~\eqref{...}, we examine ...`. 第四类是直接聚焦核心定理, 例如 `In this subsection, we focus on the Hohenberg--Kohn theorem, which provides the conceptual foundation of density functional theory: ...`.

节与小节的结尾自然收尾, 不喊固定口号. 需要特别澄清 `we arrive at` 的真实用法: 在纯手搓语料中, 10 处 `arrive at` 有 9 处以冒号结尾用于引出推导终式 (`Summing all these terms, we arrive at the full many-body hamiltonian:`, `Substituting equation~\eqref{a} into equation~\eqref{b}, we arrive at ...:`, `Therefore, we arrive at:`), 仅 1 处用于定理结论 (`Therefore, we arrive at the conclusion that ...`). 它不是每节末尾必写的 `At this stage, we arrive at X as role. We now turn to Y.` 机械模板. 真实的小节结尾方式包括: 一句简短结论直接收束 (`This procedure constitutes the Thomas--Fermi method.`), 坦率的后文预告 (`In what follows, we introduce ...` 或 `We will introduce approximations for it later.`), 或者推导完最后一个方程与解释句后直接结束本小节, 不强行加过渡套话.

### 2.2 客观说明与结果摘要语体 (`appD` 与摘要/结果段)

在无公式的代码说明 (`appD`) 中, 不强塞 `we` 或推导连接词. 直接以具体对象 (`The program code`, `Each chapter repository`, `Later repositories`) 或正式学位论文第三人称 (`The candidate used \texttt{vmatplot} to ...`, `the candidate releases ...`) 平实陈述功能与范围, 用 `In particular,` 点出重点功能.

在摘要与结果概述中, 用 `Our first study examines ...`, `In this thesis, we study/apply ...` 替代无人称的 `The <topic> study examines ...`. 用前置方法短语引出发现, 例如 `Through the calculation of ..., we reveal/obtain ...` 和 `From the dielectric response, we find ...`. 避免连续三四句使用完全同构的 `A remains X, whereas B and C are Y` 对称句模.

---

## 3. 句子与连接词特征

### 3.1 连接副词与引导短语 (作者真迹清单)

句首连接词后一律加逗号. 优先使用作者在 `fundamentals_a.tex` 手稿末尾自列的顺序词及正文中高频出现的连接词.

逻辑推论常用 `Therefore,` (最常用), `Accordingly,` (顺应前文设定得出下一步), `Consequently,`, `Hence,` (亦常作句中 `, and hence ...`), 以及 `As a result,`. 递进与补充常用 `Moreover,`, `In addition,`, `In particular,`, 和 `Specifically,`. 转折与对比在句首用 `However,` 和 `Nevertheless,`, 句中对比优先用 `while` (不用或极少用 `whereas`), 取舍用 `rather than` (少用 `; instead,` 或句首 `Instead,`).

推导步骤序数词按作者手稿清单顺序使用, 不跳号: `Firstly,`, `Secondly,`, `Thirdly,`, `Next,`, `Then,`, `Subsequently,`, `Afterwards,`, 收尾用 `Finally,`. 阶段与视角切换常用 `Up to now,`, `Now,`, `At this stage,`, `In what follows,`, `From this point of view,`, `In this sense,`, `In other words,`, `In principle,`, 和 `In practice,`. 互动式推导引导常用 `Let us ...`, `Recall ...` / `Recall that ...`, `Suppose (that) ...`, `Consider ...`, `According to equation~\eqref{...}, ...`, 以及 `We are going to apply ...` 和 `We will discuss ... later.`.

### 3.2 主动与被动的自然配比

叙述者动作 (`we`) 常用 `introduce`, `define`, `denote`, `write`, `express`, `obtain`, `arrive at`, `construct`, `apply`, `substitute`, `examine`, `focus on`, `start from`, `switch to`.

同时保留自然的数学被动与情态被动, 包括 `can be expressed as`, `can be written as`, `can be obtained from`, `can be regarded as`, `may be written as`, `is defined as`, `is given by`, `is evaluated through`, `is uniquely determined by`, `is commonly referred to as`, 和 `is handled through`.

评价性引导句如 `In quantum mechanics, it is often convenient to ...`, `For a many-body system, it is instructive to contrast ...`, `It is worth noting that ...`, 以及适度使用的 `There is ...` 均属作者自然表达, 不必强行改写.

### 3.3 括号与从句

纯手搓语料中适度保留精确的数学圆括号补充 (约 1–2 处/千词), 例如 `(up to an additive constant)`, `(up to an overall phase)`, `(in particular, for a non-degenerate ground state)`, `(self-adjoint)`, 以及缩写首次定义 `independent-particle approximation (IPA)`, 不必把所有圆括号机械拆成独立短句.

纯手搓语料中也自然存在适量的 `why` 和 `how` 从句 (约 0.7 处/千词, 例如 `showing, at the density-functional level, why the auxiliary non-interacting construction is variationally consistent` 与 `They also elucidate why its exchange-correlation component can remain highly non-trivial...`). 在解释物理机制时允许自然使用, 仅避免 AI 式的自问自答套话 (`This explains why X.`).

---

## 4. 公式与符号规范 (严格执行)

纯手搓单元的 218 个行间公式在格式上高度统一, 以下规范严格执行.

### 4.1 公式引导与标点

每一个行间公式前的引导句必须以冒号 `:` 结尾, 例如 `we introduce the density operator:` 或 `we arrive at the full many-body hamiltonian:`. 行间公式内部末尾不加逗号或句号. 散文正文中的冒号仅偶尔用于定理或核心概念的总括说明 (如 `provides the conceptual foundation of density functional theory: for a fixed form of ...`), 其余普通句子不用冒号. 正文完全不用破折号 `---`, 极少用分号 `;` (约 0.5 处/千词).

### 4.2 小写 `here,` 符号解释段

公式后若需解释新符号, 新起一段并以小写 `here,` 开头 (纯手搓单元 41 比 0, 从不用 `where`), 例如 `here, $\ket{\Psi_0}$ denotes the ground-state many-body wave function, which encodes the full complexity of the current interacting $N$-electron system.`. 解释符号常用动词 `denotes` (最常用), `represents`, `labels`, `is`. 前文已完整定义过的符号不重复解释. 命名新物理量可用 `We name it the kinetic-correlation functional.` 或 `which is commonly referred to as ...`.

### 4.3 LaTeX 与数学记号约定

数学定义用 `\coloneqq` (纯手搓单元 45 处). 成对或联立关系优先放在 `\left\{\begin{aligned} ... \end{aligned}\right.` 中, 右侧可用 `&&\qquad \text{...}` 标注物理名称.

正文引用在句中一律小写并加不换行空格 `~`, 即 `equation~\eqref{...}`, `equations~\eqref{a} and~\eqref{b}`, `section~\ref{...}`, `subsection~\ref{...}`, `chapter~\ref{...}`, `appendix~\ref{...}`, `figure~\ref{...}`, `table~\ref{...}`, 仅句首大写. 公式引用一律用 `\eqref`, 不用 `\ref`.

矢量用 `\vec{}`; 后接 `)`, `'`, `|`, `}` 时必加细空格 `\,`, 如 `n(\vec{r}\,)`, `\vec{r}\,'`, `|\vec{r}-\vec{r}\,'|`, `\ket{\vec{r}\,}`, `\hat{\vec{r}}_i\,)`. 常数与算子用正体 `\mathrm{i}` (或 `\ii`), `\mathrm{e}` (或 `\euler`), `\mathrm{\pi}`, `\dif` (`\mathrm{d}`). 描述性上下标正体 (`v_\mathrm{ext}`, `E_\mathrm{xc}`, `T_\mathrm{c}`), 指标上下标斜体 (`\psi_{n\vec{k}}`, `\varepsilon_{\alpha\beta}`). 泛函用方括号 `E[n]`, 含空间变量与泛函依赖写作 `v_\mathrm{xc}([n];\vec{r}\,)`. 算符加帽 `\hat{H}`, `\hat{n}(\vec{r}\,)`, 狄拉克记号用 `braket` 宏包. 正文中 `hamiltonian` 一律小写 (纯手搓单元 43 比 1, 仅专名 `Hamiltonian mechanics` 大写). 数值与单位一律用 `siunitx`, 例如 `\qty{0.67}{\electronvolt}` 和 `\unit{\per\nano\metre}`.

---

## 5. 全文一致性约定 (拼写与连字符)

注释行, `\label`, 引用键与 URL 不改动, 正文统一遵循以下约定.

Oxford 拼写: `-ize` 与 `-ization` 用 `organize`, `organization`, `synthesize`, `stabilize`, `realize`, `normalize`, `polarization`, `delocalization`, `minimizing`. 英式 `-our`, `-re`, `-ll-` 用 `behaviour`, `favour`, `favourable`, `colour`, `neighbour`, `centre`, `$\Gamma$-centred`, `labelled`, `modelling`. 保留 `analyse` 和 `analysed`; `towards` 带 `s`; 名词写 `licence` (`MIT License` 专名除外); 写 `tunable`.

复合定语连字符: 修饰紧随其后的名词时加连字符, 作名词时分写. 例如 `the ground-state density` 与 `in the ground state`, `first-principles calculations` 与 `from first principles`, `band-gap opening` 与 `a band gap of ...`, 以及 `two-dimensional`, `many-body`, `one-body`, `non-degenerate`, `time-dependent`, `spin-orbit`, `electron-phonon`, `exchange-correlation`. 例外是理论全称作定语仍分写, 如 `density functional theory framework` 和 `linear response theory`. `non-` 前缀一律加连字符, 如 `non-interacting`, `non-local`, `non-trivial`, `non-zero`, `non-degenerate`, `non-magnetic`.

人名与材料记号: 多人并列用 en dash `--`, 如 `Hohenberg--Kohn`, `Kohn--Sham`, `Thomas--Fermi`, `Born--Oppenheimer`, `Kramers--Kronig`, `Fu--Kane`, `Allen--Dynes`, `Migdal--Eliashberg`, `Heyd--Scuseria--Ernzerhof`. 单人复姓用连字符, 如 `Ismail-Beigi` 和 `Levi-Civita`. 材料通用名小写 (`graphene`, `borophene`, `$\alpha$-beryllene`, `$\beta$-beryllene`), 化学式用 `\ce{}`. `Xene` 与 `Xenes` 首字母大写. 第 5 章特定双层体系名保留大写 (`Graphene-Borophene`, `Graphene-\ce{BC3}`, `Graphene-\ce{B4C3}`). 拓扑不变量写 `$\mathbb{Z}_2$`, `et al.` 用正体. 吸收系数统一用 `\unit{\per\nano\metre}` (第 6 章沿用的已发表图 `fig2.11a.pdf` 除外).

---

## 6. 典型 AI 痕迹黑名单 (去 AI 时重点清除)

遇到以下 Claude 或 GPT 高频模式时, 按右侧的作者纯手搓习惯替换:

| AI 典型痕迹 (高危标黄) | 作者纯手搓替代写法 |
| --- | --- |
| 连续 12–18 词齐整短句 (`We first consider X. We then examine Y. We next identify Z.`) | 合并关联紧密的因果与条件句, 穿插 6–9 词短判断句与 25–35 词含从句长句, 拉开句长方差 |
| `We therefore <verb> ...`, `We then <verb> ...`, `We now <verb> ...` | `Therefore, we <verb> ...`, `Accordingly, ...`, `Then, we ...`, `Now, we ...`, `Subsequently, we ...` |
| `The previous section established X. We now turn to Y.` | 直接从本节物理问题, 假设 (`Suppose...`, `Consider...`) 或 `Up to now, we have ...` 切入 |
| `At this stage, we arrive at X as the central ... We now turn to ...` | 直接收尾, 或简短写 `In what follows, we ...` / `We will discuss ... later.` |
| `A is X, whereas B is Y` (尤其同一段连续出现 `whereas` / `remains`) | 改用 `while`, 或拆成前后两句自然对比 |
| `... ; instead, ...` 或句首高频 `Instead, ...` | 句中用 `rather than`, 或直接正面陈述 |
| `X does not by itself establish Y` / `X alone does not determine Y` | 肯定句直接写什么决定 Y (`Y requires ...` / `Y is determined by ...`) |
| `This limitation motivates the search for alternative ... in which ...` | `This constraint leads us to ...` 或直接写我们考察什么体系及调控手段 |
| `The <topic> study examines ...` / `The analysis characterizes ...` | `Our first study examines ...` / `Through the calculation of ..., we obtain/reveal ...` / `We examine ...` |
| 空泛套话词 (`characterize(s)`, `provide contrasting ... characters`, `supports ... features`, `shows a similar feature`, `crucial`, `robust`, `remarkable`, `intriguing`, `promising`, `novel`, `rich physics`) | 换成具体物理量与平实动词 (`show`, `give`, `yield`, `obtain`, `find`, `determine`, `excitations`, `modes`, `states`, `behaviour`) |
| 跳出文本的读者指南 (`Readers interested in ... can proceed directly to ...`) | 直接删除, 或平实交代 `Section~\ref{...} connects ...` |

---

## 7. 常见非母语笔误修正表 (仅修语法硬伤, 不伤个人文风)

仅修正真正的语法与拼写硬伤, 保留作者地道的讲义式表达 (`In principle`, `In practice`, `It is convenient to`, `can be expressed as` 等):

| 语法/用词硬伤 | 修正为 |
| --- | --- |
| 逗号拼接两个完整主句 (`A are semiconductors, their gaps reach ...`) | 改为句号分句, 或加连词 `, and their gaps ...` / `, whose gaps ...` |
| 用 `separately` 表示各自对应 (`1.82 eV and 2.38 eV separately`) | `..., respectively.` |
| `the researches on ...` / `a effective ...` | `research on ...` (不可数) / `an effective ...` |
| `let us start by <名词>` | `let us start with <名词>` |
| `we process X as` | `we treat X as` 或 `we regard X as` |
| `it demonstrates as:` | `it takes the form:` 或 `it can be written as:` |
| `We adopt $i$ labels the electrons` | `We use $i$ to label the electrons` |

---

## 8. 自检清单

去 AI 时确认做到最小化修改, 未标黄或未含 AI 模板的原句保持未动.

检查句长突发性, 保留长短句交错节奏, 没有把全文削平为约 15 词的均一短句.

检查连接词位置, `Therefore`, `Accordingly`, `Consequently`, `Then`, `Now`, `Next` 多放在句首加逗号, 不连续使用 `We therefore`, `We then`, `We now`.

检查对比与被动语态, 用 `while` 和 `rather than` 替代成堆的 `whereas` 和 `Instead,`, 同时保留自然的 `can be ...` 与 `it is ... to`.

检查公式规范, 每个行间公式前以冒号结尾, 公式末尾无标点, 新符号在小写 `here,` 段解释.

检查符号与拼写, `\vec{r}\,`, `\vec{r}\,'`, 正体 `\mathrm{i},\mathrm{e},\mathrm{\pi},\dif`, 小写 `hamiltonian`, `\eqref`, `siunitx`, Oxford 拼写及复合定语连字符保持一致.


