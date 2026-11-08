---
name: thesis-writing-style
description: >-
  Lu Niu's own English writing style for the PhD thesis on light-element xenes
  (DFT, linear optical response, band topology). Load it before drafting,
  rewriting, polishing, or reviewing any English prose or LaTeX in this
  repository, including chapters, appendices, abstract, captions, and replies to
  examiners, and whenever the user asks for text "in my style" or "我的风格".
  Derived from the parts the author wrote word by word and the supervisor
  approved: Chapter 2, Chapter 3, Appendix A, and Appendix B.
---

# Lu Niu 论文写作风格

本文件归纳作者本人的英文学术写作风格, 用于续写, 改写和审读本仓库中的论文文本.
规则后面的数字来自对语料的统计, 用来区分两类内容: 作者的真实习惯, 以及作者希望达到的目标.
原文范例和改写示例见 `references/examples.md`.
第 11 节是作者的待办清单, 列出全文需要修改的具体位置.

## 0. 依据与适用范围

风格语料 (作者逐字写成, 经导师验收):

- `src/fundamentals_a.tex`, 第 2 章, DFT.
- `src/fundamentals_b.tex`, 第 3 章, 线性光学响应.
- `src/appendix_quantum.tex`, 附录 A.
- `src/appendix_electrodynamics.tex`, 附录 B.

合计约 23,000 词, 335 个行间公式.

不作为风格依据:

- 第 5, 6 章 (`project_1_main.tex`, `project_2_main.tex`). 这两章主要由师兄润色, 已经没有作者的特征.
- 第 1, 4, 7, 8 章与附录 C. 这些部分不在作者逐字写成的范围内, 语气与语料明显不同. 它们是按本风格统一改写的对象.

语料与其他章节的对照, 单位为每 1000 词:

| 指标 | 语料 | 第 5, 6 章 | 第 1, 4, 7, 8 章与附录 C |
| --- | --- | --- | --- |
| we / us / our | 22.2 | 4.2 | 14.0 |
| Therefore | 3.0 | 0.4 | 0.3 |
| arrive at | 0.70 | 0 | 0.12 |
| medium | 2.5 | 0.3 | 0.1 |
| not / no / cannot 等否定词 | 3.2 | 3.2 | 5.8 |
| why / how | 1.0 | 0.5 | 2.7 |
| "does not establish", "by itself" 一类防御句 | 0.30 | 0.78 | 1.04 |
| 分号 | 1.0 | 1.5 | 2.1 |
| 正文括号 | 0.7 | 2.5 | 0.8 |

公式与句子的统计:

- 98% 的行间公式, 前一句以冒号结尾.
- 98 处公式之后, 新段以小写 `here,` 开头解释符号.
- 句子平均 15.6 词, 中位数 14 词, 90% 的句子不超过 25 词.
- 公式之间的文字块很短, 73% 只有一到两句.

## 1. 总纲

1. 叙事推进. 用 we 作叙述者, 带读者沿一条推导路线前进. 每一步都由上一步引出. 读者始终知道我们从哪里来, 现在做什么, 下一步去哪里.
2. 物理先行. 先提出物理问题或物理动作, 再引入并命名概念, 最后写公式. 写完公式, 立即用物理动作和因果路径解释它.
3. 先一般, 后近似. 先给出一般形式, 再说明本文采用的近似, 最后收束到工作形式.
4. 命名一切. 新概念, 新物理量, 新公式都有名字. 重要物理量在正文出现时, 名称和符号同时给出.
5. 肯定陈述. 用肯定句交代适用范围和限制条件. 写 "X determines Y", 少写 "X alone does not establish Y".
6. 短句. 一句只做一件事, 长度约 15 词. 源文件一句一行.
7. 不重复. 一个公式只显示一次, 之后用 `equation~\eqref{}` 引用. 一个论点只论证一次.
8. 首尾衔接. 小节开头回扣上一节. 小节结尾用 we arrive at 收束本节, 再引出下一节.

## 2. 篇章结构

### 2.1 章的开头

固定由三步组成:

1. 定位句, 说明本章在整个理论链条中的位置:
   `We start our discussion of the fundamentals in this chapter by introducing ...`
   `We continue our discussion of the fundamentals in this chapter, where we introduce ...`
2. 物理动作链, 两到四句, 从物理对象出发讲清要解决的问题. 最后一句用 `We therefore ...` 给出方法路线.
3. 路线图段落, 按节列出, 每节一句, 句中带 `section~\ref{}`, 用 `then`, `Next`, `Finally` 串联.

单位制在章首声明一次, 例如 `We use the Hartree atomic units ...` 或 `We use SI units for the macroscopic electrodynamic equations.`
之后需要恢复常数时, 明确写出 `We now restore $\hbar$ explicitly.`

故事引子 (附录 A 的 `Imagine that we are watching ...`) 只用于章或附录的第一段, 两到四个短句, 可以用一个设问.
正文其他位置不用设问和第二人称.

### 2.2 节的开头

语料中有 17 处以 `The previous section ...` 一类句式开头. 模板:

```
The previous section established/introduced <结果 X>.
We now turn to/identify/connect <对象 Y>.
In this section, we start by <步骤 1>.
We then <步骤 2>.
Next, we <步骤 3>.
Therefore, we advance from <起点> to <终点>.
```

### 2.3 从物理问题到公式

每引入一个公式, 依次完成四个动作:

1. 物理动作: 场, 电子, 介质, 势等对象做了什么.
2. 命名: 给即将出现的量或关系起名字.
3. 引导句: 以冒号结尾, 句中点出公式的名字.
4. 解释: `here,` 段解释符号, 接着一句讲这个公式描述的物理过程.

推导中的步骤用序数副词标明: Firstly, Secondly, Thirdly, Next, Then, Subsequently, Afterwards, Thereafter, Finally.
这组词是作者自己在 `fundamentals_a.tex` 末尾列出的清单. 同一推导中按顺序使用, 不跳号.
发起一步运算用 `Let us ...`, 调回前文结果用 `Recall ...`.

### 2.4 先一般, 后近似

模板:

```
Firstly, we start from the most general <...> form.
<一句说明一般形式包含的物理: 非局域, 记忆效应, 全张量, 多体波函数 ...>
Therefore, before introducing the simplified form used in the present work, we write <...> as:
<一般公式>
For the present work, we focus on <条件>.
Under this approximation, <被丢掉的部分> drops out, and <保留的部分> remains.
Therefore, it reduces to the <工作形式名称>:
<工作公式>
```

### 2.5 小节的结尾

语料中有 16 处 arrive at. 结尾两句:

1. 收束句, 点名本节得到的结果, 以及它的物理角色:
   `At this stage, we arrive at <named result> as <role>.`
   `Consequently, we arrive at <...>.`
   `Therefore, we arrive at the conclusion that <...>.`
2. 过渡句, 说明下一节要用这个结果做什么:
   `We now turn to <...>.`
   `In the next subsection, we derive <...> and clarify its physical meaning.`

## 3. 句子层面

### 3.1 we 与主动语态

- 方法动作由 we 完成: introduce, define, write, obtain, derive, express, impose, construct, recall, apply, substitute, separate, collect, restore, examine.
- 物理动作由物理对象完成, 同样用主动语态: `the field drives the electrons`, `the medium stores energy`, `causality constrains the real and imaginary parts`, `the Bloch phase carries the change between cells`.
- 被动语态在语料中约占每 1000 词 10 处, 主要是 `is defined as`, `is given by`, `is obtained from`. 这类约定性表述可以保留. 同一段内不连续使用两个以上被动句.

### 3.2 具体动词

用具体动词替换空泛结构:

| 少用 | 改用 |
| --- | --- |
| is responsible for, plays a role in | drives, determines, controls, generates |
| there is / there are | <主语> + 具体动词 |
| it is ... that | 直接陈述 |
| is related to | connects ... to, depends on, follows from |
| has an effect on | modifies, shifts, suppresses, enhances |

### 3.3 肯定句

用肯定句交代条件和范围, 把限制写成适用条件:

- 写 `The scalar relations apply to the diagonal response along a principal direction.`
- 少写 `Applying them to an off-diagonal element does not give ...`
- 写 `A finite-momentum calculation determines the dispersion of these modes.`
- 少写 `These features do not by themselves establish propagating modes.`

确有对照时才用否定, 并立即给出正面陈述:
`The polarization does not follow the electric field instantaneously. Instead, the medium retains a memory of the earlier perturbation.`

### 3.4 why 与 how 从句

语料中仍有约 23 处 why/how. 新写和改写时按下表处理:

| 原句 | 改为 |
| --- | --- |
| This explains why X. | X therefore follows. |
| To understand why there are four, we rewrite ... | We count these points by rewriting ... |
| This is why we compare A with B. | We therefore compare A with B. |
| It describes how strongly P responds to E. | It measures the strength of the response of P to E. |

设问只用于章首故事引子, 或在整章中提出一次核心问题: `a natural question is the following: what ...?`

### 3.5 连接副词

句首副词后加逗号. 按功能选词:

- 推论: Therefore (语料最常用, 68 次), Consequently, Hence, As a result. Therefore 只用于真正的推论, 程序性的下一步用 Next 或 We then.
- 顺应前文而采取行动: Accordingly.
- 追加: Moreover.
- 同时成立: Meanwhile, At the same time.
- 对照: However, By contrast, Instead. 句中对照用 whereas, while.
- 换一种说法: Equivalently, In other words, In this sense, Specifically, In particular.
- 顺序: Firstly, Secondly, Thirdly, Next, Then, Subsequently, Afterwards, Thereafter, Finally.
- 阶段: At this stage, Up to now, In what follows, Here.
- 原因或伴随: as 引导的从句, 例如 `As different principal components produce different optical responses along different directions, optical anisotropy appears.`

### 3.6 whereas 对照对

两个量分工不同时, 用一句 whereas 并列:
`The refractive index determines the phase evolution, whereas the extinction coefficient describes the attenuation of the wave amplitude.`
两个分句的主语和动词结构保持平行.

### 3.7 名称与符号同时出现

`the electron density $n(\vec{r}\,)$`, `the dielectric tensor $\varepsilon_{\alpha\beta}(\omega)$`, `the absorption coefficient $\alpha(\omega)$`.
每节第一次出现时写全名和符号. 同一推导内部可以只写符号.

### 3.8 medium

在光学和电动力学部分, 材料称为 the medium, 并让它做动作: the medium responds, stores energy, absorbs, retains memory, spreads the response over space.
语料中 medium 出现 58 次, 其他章节几乎不用.

### 3.9 句长与段落

- 一句只表达一个动作或一个判断. 超过 30 词的句子拆成两句.
- 源文件一句一行. 长句可以在逗号处换行.
- 公式之间的文字块通常是: 引导句, 公式, `here,` 解释, 物理解释或推论.
- 不在正文中描述图中的颜色, 箭头和线型. 这些信息写进图注.

## 4. 公式

### 4.1 引导句与公式末尾

- 行间公式前一句以冒号结尾, 并点出公式的名字: `we obtain the Euler--Lagrange condition:`, `we define the potential shift function:`.
- 行间公式末尾不加任何标点.
- 冒号后必须紧跟公式. 冒号后接文字段落属于错误.

### 4.2 here 解释段

公式后新起一段, 以小写 `here,` 开头, 依次解释新符号:
`here, $\omega$ refers to the screening parameter that controls the range separation.`
`here, $n$ and $m$ label the initial and final bands, and $f_{n\vec{k}}$ and $f_{m\vec{k}}$ denote their occupations.`
解释符号用 `here,`, 不用 `where`. 只有前文已有完整解释的符号不再重复.

### 4.3 公式后的物理解释

符号解释之后, 用一句以 `This relation/expression/equation` 开头的句子讲公式的物理作用:
`This relation demonstrates that the imaginary part of the dielectric response directly describes the energy-absorbing part of the induced current.`
`This expression separates the dissipative channel from the dielectric screening.`
讲作用路径: 哪个量驱动哪个量, 增大什么会怎样.
例如 `Accordingly, the Kohn--Sham potential is increased where the density is overestimated and decreased where it is underestimated.`

### 4.4 LaTeX 写法

- 定义用 `\coloneqq` (语料 55 处).
- 成对或相关的关系放在同一个大括号系统中, 需要时在右侧写名字:

```latex
\begin{equation}
\left\{\begin{aligned}
    &0\le f_i\le 1              &&\qquad  \text{Pauli bound} \\
    &\textstyle{\sum_i}f_i = N  &&\qquad  \text{particle-number constraint}
\end{aligned}\right.
\label{occupation_constraints}
\end{equation}
```

- 多步推导用 `aligned`, 每行一步, 以 `&=` 对齐.
- label 用描述性的 snake_case, 写明物理内容: `KS_effective_potential_definition`, `kk_positive_frequency_dielectric_component`, `absorption_coefficient_from_dielectric_function`. 常用后缀: `_definition`, `_decomposition`, `_condition`, `_relation`, `_from_<source>`. 不用 `obvious`, `approx` 一类无信息的 label.

### 4.5 正文中的引用

- 句中一律小写: `equation~\eqref{}`, `equations~\eqref{a} and~\eqref{b}`, `section~\ref{}`, `subsection~\ref{}`, `chapter~\ref{}`, `appendix~\ref{}`, `figure~\ref{}`, `table~\ref{}`. 只有位于句首时大写.
- 公式一律用 `\eqref`, 不用 `\ref`. 引用前一律加 `~`.
- 名称加编号的写法: `the Slater determinant representation~\eqref{slater_determinant}`, `the universal Hohenberg--Kohn functional~\eqref{functional_HK_definition}`.
- 已经显示过的公式不再重写. 用 `Recall the Kohn--Sham equations~\eqref{KS_equation}.` 调回.

### 4.6 符号约定

- 矢量用 `\vec{}`. 矢量后面紧跟 `)`, `'`, `|`, `}` 时加细空格 `\,`: `n(\vec{r}\,)`, `\vec{r}\,'`, `|\vec{r}-\vec{r}\,'|`, `\ket{\vec{r}\,}`, `\hat{\vec{r}}_i\,)`. 语料中带 prime 的矢量 35 处全部如此, 后接右括号的情形 447 处全部如此.
- 常数和微分用正体: `\mathrm{i}`, `\mathrm{e}`, `\mathrm{\pi}`, `\dif` (即 `\mathrm{d}`). 不用斜体 i 和 e.
- 描述性上下标用正体: `v_\mathrm{ext}`, `E_\mathrm{xc}`, `\varepsilon^\mathrm{inter}`. 指标性下标用斜体: `\varepsilon_{\alpha\beta}`, `\psi_{n\vec{k}}`.
- 泛函用方括号 `E[n]`. 对密度的泛函依赖写成 `v_\mathrm{H}([n];\vec{r}\,)`.
- 算符加帽: `\hat{H}`, `\hat{n}(\vec{r}\,)`. 狄拉克记号用 braket 宏包.
- 正文中 hamiltonian 小写 (语料 64 比 1).
- 数值与单位用 siunitx: `\qty{0.67}{\electronvolt}`, `\unit{\electronvolt}`.
- 时间依赖约定 `\exp(-\mathrm{i}\,\omega t)` 在章首声明一次.

## 5. 标点

- 正文只用逗号和句号.
- 冒号只用于引出行间公式.
- 分号改成两句. 语料正文中有 23 个分号, 其中 8 个是 `; instead,` 结构, 改写为 `... . Instead, ...`.
- 括号内的补充说明改写进句子, 或单独成句. 缩写首次出现时的括号可以保留, 例如 `independent-particle approximation (IPA)`.
- 正文不用破折号.
- 不用感叹号. 设问只用于 2.1 和 3.4 规定的位置.

## 6. 词汇

### 6.1 动词

按功能列出, 括号内为语料出现次数:

- 解释符号: denote (91), represent (18), refer to (9).
- 描述物理: describe (49), determine (47), provide (29), connect (20), characterize (15), reproduce (15), demonstrate (13), drive (8), generate (6), induce (6), enforce (4), measure (3), encode (3), reveal (2), govern, store, transfer, absorb, retain.
- 叙述者动作: introduce (25), obtain (19), write (15), arrive at (16), define (10), express, derive, construct, impose, recall, apply, substitute, collect, separate, restore, examine, resolve.

### 6.2 名词

response (171), approximation (68), structure (46), observable (42), contribution (32), channel (23), picture (22), framework (19), constraint (17), construction (15), medium (58), descriptor, ingredient, language, backbone, route, stage, counterpart, correspondence.

### 6.3 常用框架句

- `We start our discussion of ... by introducing ...`
- `The previous section established ... We now turn to ...`
- `In physical terms, ...`
- `Here, the central object is ...`
- `This relation demonstrates that ...`
- `In this sense, ...`
- `Equivalently, ...`
- `We name it the ... .`
- `For the present work, we focus on ...`
- `In what follows, we ...`
- `At this stage, we arrive at ...`

### 6.4 形容词

用精确的描述性形容词: central, universal, compact, practical, direct, explicit, local, effective, auxiliary, causal, directional.
不用评价性和宣传性形容词: crucial, essential, robust, remarkable, intriguing, powerful, promising, unprecedented, rich (physics), novel.

## 7. 已知的非母语用法

语料中反复出现以下用法, 新写和改写时一律替换. 行号以 2026-11-09 的版本为准, 行号变动后按原文搜索.

| 原文 | 改为 | 位置 | 状态 |
| --- | --- | --- | --- |
| let us start by <名词> | let us start with <名词> | `fundamentals_a.tex:643`, `appendix_electrodynamics.tex:34` | 待改 |
| we achieve: | we obtain: | `fundamentals_a.tex:516`, `fundamentals_a.tex:1056` | 待改 |
| we process X as, we can process X as | we treat X as, we regard X as | `fundamentals_a.tex:1054`, `fundamentals_a.tex:1441` | 待改 |
| the problem degenerates to | the problem reduces to | `fundamentals_a.tex:698` | 待改 |
| the electron density of ground state | the ground-state electron density | `fundamentals_a.tex:42` | 待改 |
| the density of ground state $n(\vec{r}\,)$ | the ground-state density $n(\vec{r}\,)$ | `fundamentals_a.tex:59` | 已改 |
| the corresponding wave function of ground state $\Psi_0$ | the corresponding ground-state wave function $\Psi_0$ | `fundamentals_a.tex:59` | 待改 |
| it demonstrates as: | it takes the form: | `fundamentals_a.tex:1452` | 待改 |
| the kernel idea of density functional theory is here: ... | the key idea. 句中的冒号改为句号 | `fundamentals_a.tex:59` | 待改 |
| Review the expression of ... | Recall the expression for ... | `fundamentals_a.tex:193` | 待改 |
| We adopt $i$ labels the electrons | We use $i$ to label the electrons | `appendix_quantum.tex:247` | 待改 |
| This is convenient to introduce | It is convenient to introduce | `appendix_quantum.tex:1297` | 已改 |
| The present section does not review a complete lecture of electrodynamics; instead, we only extract ... | The present section extracts only the ingredients required for ... | `appendix_electrodynamics.tex:23` | 待改. 上次只删了 aim to, "review a complete lecture" 仍不通, 且是否定句加分号 |
| Afterwards, ... then ... | 二者只留一个 | `appendix_electrodynamics.tex:351` | 已改 |
| In practice, the Kohn--Sham equations give the exact electron density in principle | In principle, the Kohn--Sham equations give the exact electron density | `fundamentals_a.tex:1296` | 待改. 第 607 行删去的 in principle 不是这一处, 那处改动本身没有问题 |
| Since A. (无主句) | A. Therefore, B. | `fundamentals_a.tex:301`, `fundamentals_a.tex:1022`, `appendix_quantum.tex:1406` | 已改 |
| If we start from the naive choice: <公式> Therefore, the density ... is concentrated ... | We first test the naive choice: <公式> With this choice, the density ... concentrates near the centre of the well. | `fundamentals_a.tex:1421`, `fundamentals_a.tex:1428` | 待改. 上次只把 one 改成了 we, 条件句仍没有主句 |

## 8. 一致性约定

以下约定已在全文所有参与编译的源文件中落实. 注释行, label, 引用键, 文献键和 URL 不随正文改动, 例如 `general_nonlocal_constitutive_relation`, `sec:intro_organisation`.

### 8.1 拼写

采用 Oxford spelling:

- -ize 和 -ization: characterize, organize, organization, synthesize, stabilize, realize, normalize, polarization, delocalization.
- 英式 -our, -re, -ll-: behaviour, favour, favourable, colour, neighbour, centre, $\Gamma$-centred, labelled, modelling.
- analyse 和 analysed 保留 -yse.
- towards 带 s.
- 名词写 licence. 专名 MIT License 保持原样.
- tunable 不写 tuneable.

### 8.2 复合定语

复合词放在名词前作定语时加连字符, 作名词时分写. 形容词加名词和名词加名词都按这一条处理.

- ground state: `the ground state`, `the ground-state density`, `the ground-state $N$-body wave function`.
- first principles: `from first principles`, `first-principles calculations`.
- 其他已统一的定语: total-energy functional, charge-density difference, electron-density difference, phonon-dispersion curves, band-gap energies, band-structure analysis, density-functional formalism, dielectric-function convergence, exchange-correlation functional, zero-temperature setting, two-dimensional, many-body, low-energy, long-range, short-range, first-order, high-symmetry, single-particle, k-point mesh.
- 同一词组作名词时分写: the band gap, a band gap of 0.67 eV, at a k point, the phonon dispersion, at low energy, in two dimensions.

区分名词和定语的方法: 后面紧跟被修饰的名词时是定语. 后面接标点, 动词, 介词, 连词, 或同位的符号时是名词, 例如 `the ground state $\ket{\Psi_0}$`, `from the ground state $g$`. 中间插入括号说明时仍按定语处理, 例如 `the ground-state ($g\coloneqq 0$) many-body wave function`.

两类例外:

- 理论名称一律分写, 即使作定语: density functional theory, density functional perturbation theory, time-dependent density functional theory, linear response theory.
- 不是固定术语的描述性短语不强行加连字符, 例如 energy convergence criterion, electronic convergence criterion.

共用中心词的悬垂复合词保留连字符: `time-reversal and inversion symmetry`, `zero-point and thermal contributions`, `the near-infrared and ultraviolet regions`.

### 8.3 连字符与 en dash

- 人名并列用 en dash `--`: Kohn--Sham, Hohenberg--Kohn, Kramers--Kronig, Born--Oppenheimer, Thomas--Fermi, Hartree--Fock, Perdew--Burke--Ernzerhof, Heyd--Scuseria--Ernzerhof, Becke--Johnson, Fu--Kane, Allen--Dynes, Migdal--Eliashberg, Schottky--Mott, Nos\'e--Hoover, Amp\`ere--Maxwell.
- 一个人的复姓用连字符: Levi-Civita, Ismail-Beigi.
- 两个实体之间的关系用连字符: spin-orbit, electron-phonon, electron-electron, electron-hole, exchange-correlation, metal-semiconductor, potassium-boron, ket-bra. 化学键同样用连字符: B-B, Be-Be, Be-H.
- 材料组合的泛称用连字符并小写: graphene-borophene interfaces. 第 5 章定义的体系名保留首字母大写: Graphene-Borophene, Graphene-\ce{BC3}, Graphene-\ce{B4C3}.
- 某一方本身是带连字符的复合词时用 en dash: graphene--boron-carbide.

### 8.4 前缀

non- 前缀按英式加连字符: non-interacting, non-zero, non-local, non-locality, non-linear, non-classical, non-relativistic, non-commuting, non-monotonically, non-degenerate, non-trivial, non-magnetic, non-negative, non-negligible, non-Abelian, non-self-consistently, non-spin-polarized. none 和 nonetheless 不属于前缀构词.

### 8.5 名称与记号

- 材料名小写: $\alpha$-beryllene, $\beta$-beryllene, borophene, graphene. 化学式用 `\ce{}`.
- Xene 和 Xenes 首字母大写, X 代表元素.
- 拓扑指数写 $\mathbb{Z}_2$, 与 Chern 数的 $C_n\in\mathbb{Z}$ 用同一套整数记号. 斜体 $Z$ 已用于核电荷 $Z_I$ 和附录 C 的重叠乘积 $Z_C$, 不再用于拓扑指数. 软件名 Z2Pack 和 PDF 书签中的 Z2 保持纯文本.
- et al. 用正体.

### 8.6 单位

吸收系数统一用 \unit{\per\nano\metre}. 例外: 第 6 章沿用已发表论文中的图 `figures_proj2/fig2.11a.pdf`, 单位保持 Å⁻¹, 不重新出图. 图注中写明单位.

## 9. 避免的写法

以下写法常见于 AI 修订或他人润色的章节, 不属于作者风格. 全文中的具体位置见 11.2 节.

- 防御性否定句: `X does not by itself establish Y`, `X alone does not determine Y`, `need not`. 改为肯定句, 说明 Y 由什么确定 (见 3.3).
- 每个图后重复同一条限制. 限制条件在方法部分或一个 scope 段落中集中说明一次, 结果段专注于物理.
- 规定式语气: `must be specified`, `must be identified with`. 论文自己就是执行者, 改为陈述句: `Each research chapter reports ...`.
- why 和 how 解释句 (见 3.4).
- 宣传性形容词 (见 6.4).
- 跨章节重复的教科书段落. 定义只出现在理论章, 结果章引用.
- 同一公式多次显示, 同一定理多次复述.
- 正文描述图中的颜色, 箭头和阴影.
- 没有明确对象的 `This` 开头句. `This` 后面接名词: `This relation`, `This step`, `This contribution`.

## 10. 自检清单

写完一个小节后逐条检查:

1. 开头是否回扣了上一节, 并说明本节要做什么.
2. 每个公式之前, 是否先讲了物理动作并给出了名字.
3. 每个行间公式前是否是冒号, 末尾是否没有标点.
4. 新符号是否都在 `here,` 段中解释.
5. 公式后是否有一句讲物理作用的解释.
6. 是否有重复显示的公式或重复论证的段落.
7. 是否有防御性否定句, why/how 从句, 分号, 括号, 破折号.
8. Therefore 是否只用于真正的推论.
9. 句子是否大多在 25 词以内, 一句一行.
10. 重要物理量第一次出现时是否名称与符号并列.
11. 符号约定: `\vec{r}\,)`, `\vec{r}\,'`, 正体 i, e, π, d, 小写 hamiltonian, `\eqref`.
12. 结尾是否用 we arrive at 一类句式收束, 并引出下一节.

## 11. 待办清单

这一节是作者完善论文用的待办清单, 按优先级排列. agent 按本风格改写论文时, 也可以逐条处理. 行号以 2026-11-09 的版本为准, 行号变动后按引文搜索. 完成一条, 就把 `[ ]` 改为 `[x]`.

### 11.1 内容一致性 (P0)

这些问题会让读者质疑结论, 应最先处理. 有几组防御句的根源就在这里, 问题解决后可以一并删除.

- [ ] [abstract.tex:19](../../../src/abstract.tex#L19) 摘要说 Graphene-\ce{B4C3} "possibly chiral optical behaviour", 第 5 章却说非对角元不能证明旋光性. 删去 chiral.
- [ ] [abstract.tex:39](../../../src/abstract.tex#L39) 摘要说 "identify non-trivial $\mathbb{Z}_2$ topology", 没有交代第 7 章的条件: 隔离能隙约 1 meV, 位于费米能以上, 体系是金属. 补上限定, 与第 7 章一致.
- [ ] [project_3_main.tex:34](../../../src/project_3_main.tex#L34) 和 [project_3_main.tex:1273](../../../src/project_3_main.tex#L1273): "combines metallicity, tunable optical properties, and non-trivial topology" 偏强, 与条件性的结论不符.
- [ ] 第 5 章的非对角介电元: 核实 (对称化, 与 VASP 输出的 6 个分量对照), 或删去相关讨论和面板. 解决后删除对应的防御句: project_1_main.tex 第 557, 558, 618, 620, 621, 744 行, project_1_SI.tex 第 274, 280, 282, 304, 317 行, conclusion.tex 第 201 行.
- [ ] [project_2_main.tex:706](../../../src/project_2_main.tex#L706) Migdal--Eliashberg 的 $T_c$: 存档数据没有越过 $T_c$. 补算跨过能隙闭合的温度点, 或改为区间表述. 解决后处理第 710, 711 行和 conclusion.tex 第 66 行.
- [ ] [project_2_main.tex:467](../../../src/project_2_main.tex#L467) 双层的结合能比体相低 0.19 eV/atom, 需要解释或核查 (自由原子参考, 自旋极化, D3, 截断能是否一致).
- [ ] [project_1_main.tex:136](../../../src/project_1_main.tex#L136) 定义了层间结合能 $E_\mathrm{b}$, 全章没有给出数值, 第 732 行的结论却说 "small binding energies".
- [ ] 光学有效厚度的约定各章不同: 第 5 章不归一化 ([project_1_main.tex:511](../../../src/project_1_main.tex#L511)), 第 6 章用 B 1.91 Å 和 H 1.2 Å ([project_2_SI.tex:64](../../../src/project_2_SI.tex#L64)), 第 7 章用 Be 1.98 Å 和 H 0.70 Å ([project_3_main.tex:357](../../../src/project_3_main.tex#L357)). 在第 3 章用一张表说明各章的约定.

### 11.2 防御性句子

GPT 润色时常写这类句子. 每条后面标出类型, 改法如下:

- 否定: "X does not (by itself) establish Y", "X alone does not ...", "need not". 改为肯定句, 说明 Y 由什么确定. 见 3.3 节和 examples.md 的 B1.
- 规定: "must be ...", "should be ...", "we must also ...". 改为陈述论文实际做了什么, 或直接删去. 见 examples.md 的 B3.
- 待定: "remains to be established", "has not been calculated", "requires further checks". 正文最多保留一次, 集中写进第 8 章的 Limitations 或 Outlook.
- 范围: "within the stated approximations", "under the stated convention". 在方法部分说明一次, 结果段删去.
- 对比: "rather than ...", "X, not Y". 直接陈述它是什么.
- 图注: 在正文里否认图的含义, 如 "they are not calculated bands". 移进图注, 改为肯定描述.

正文里的数学或物理否定不属于这一类, 不需要改, 例如 "its $\mathbb{Z}_2$ index cannot change", "the polarization response cannot occur before the external electric field is applied". 第 5 章非对角元和第 6 章 $T_c$ 相关的句子已归入 11.1.

#### 摘要

- [ ] [abstract.tex:38](../../../src/abstract.tex#L38) 否定: "Neither dimensional reduction nor hydrogenation enhances absorption in every direction or throughout the visible range."

#### 第 1 章

- [ ] [introduction.tex:49](../../../src/introduction.tex#L49) 否定: "Elemental composition alone does not specify the structure of a boron sheet."
- [ ] [introduction.tex:50](../../../src/introduction.tex#L50) 规定: "We must also specify the arrangement of triangular units and holes within the sheet."
- [ ] [introduction.tex:56](../../../src/introduction.tex#L56) 否定: "... explains why it need not select one unique sheet."
- [ ] [introduction.tex:75](../../../src/introduction.tex#L75) 否定: "... retaining metallicity does not imply an unchanged optical response."
- [ ] [introduction.tex:90](../../../src/introduction.tex#L90) 规定: "... we must also determine the transition strengths ...; the gap alone does not specify them."
- [ ] [introduction.tex:133](../../../src/introduction.tex#L133) 否定: "... show why a stable bulk element does not automatically produce a stable sheet in every geometry."
- [ ] [introduction.tex:136](../../../src/introduction.tex#L136) 规定: "For each candidate, we must also examine how the atoms respond to displacement."
- [ ] [introduction.tex:155](../../../src/introduction.tex#L155) 否定: "Thus, adding a layer need not produce a simple interpolation between monolayer and bulk properties."
- [ ] [introduction.tex:192](../../../src/introduction.tex#L192) 范围: "...; they do not include the bound electron-hole excitations of a Bethe--Salpeter treatment."
- [ ] [introduction.tex:196](../../../src/introduction.tex#L196) 否定: "... interactions that a semilocal functional alone does not adequately describe ..."
- [ ] [introduction.tex:197](../../../src/introduction.tex#L197) 规定: "We must also specify how we represent the optical response."
- [ ] [introduction.tex:248](../../../src/introduction.tex#L248) 规定: "To describe the response to light, we must also determine which transitions couple ..."
- [ ] [introduction.tex:272](../../../src/introduction.tex#L272) 对比: "... rather than assigning a mode from a peak alone."
- [ ] [introduction.tex:274](../../../src/introduction.tex#L274) 范围: "Within the stated optical treatment, we use the calculated loss spectra ..."
- [ ] [introduction.tex:286](../../../src/introduction.tex#L286) 否定: "Band energies alone do not specify this organization, since they do not contain the full information ..."

#### 第 2 章 (集中在第 2.3, 2.4 节)

- [ ] [fundamentals_a.tex:79](../../../src/fundamentals_a.tex#L79) 对比: "This is not merely a change of notation; it marks ..." 见 examples.md 的 B5.
- [ ] [fundamentals_a.tex:1719](../../../src/fundamentals_a.tex#L1719) 否定: "A larger band gap does not by itself imply a more accurate result."
- [ ] [fundamentals_a.tex:1721](../../../src/fundamentals_a.tex#L1721) 规定: "... we need to consider the limitations of both functionals."
- [ ] [fundamentals_a.tex:1777](../../../src/fundamentals_a.tex#L1777) 规定: "... it must also enter the energy and its derivatives used for relaxation."
- [ ] [fundamentals_a.tex:1799](../../../src/fundamentals_a.tex#L1799) 否定: "... satisfying these stopping criteria does not establish convergence with respect to the plane-wave cutoff ..."
- [ ] [fundamentals_a.tex:1884](../../../src/fundamentals_a.tex#L1884) 否定: "The smooth auxiliary density alone is therefore not the reconstructed all-electron density."
- [ ] [fundamentals_a.tex:1886](../../../src/fundamentals_a.tex#L1886) 规定: "The datasets and their convergence settings must be specified for each calculation." 见 examples.md 的 B3.
- [ ] [fundamentals_a.tex:1906](../../../src/fundamentals_a.tex#L1906) 否定: "A high-symmetry path used to display a band structure does not replace this integration mesh."
- [ ] [fundamentals_a.tex:2002](../../../src/fundamentals_a.tex#L2002) 规定: "Small imaginary frequencies require convergence checks before they can be attributed to numerical errors."
- [ ] [fundamentals_a.tex:2003](../../../src/fundamentals_a.tex#L2003) 范围: "... within the wave vectors and numerical accuracy examined."
- [ ] [fundamentals_a.tex:2023](../../../src/fundamentals_a.tex#L2023) 规定: "... must therefore be specified with each calculation." 见 examples.md 的 B3.
- [ ] [fundamentals_a.tex:2025](../../../src/fundamentals_a.tex#L2025) 否定: "Neither test alone establishes thermodynamic stability or experimental synthesizability."
- [ ] [fundamentals_a.tex:2081](../../../src/fundamentals_a.tex#L2081) 规定: "The normalization must be stated when reporting an energy difference, and the numerical uncertainty must be small ..."
- [ ] [fundamentals_a.tex:2086](../../../src/fundamentals_a.tex#L2086) 否定: "A vanishing total spin moment alone does not distinguish an antiferromagnetic state from a non-magnetic state;"
- [ ] [fundamentals_a.tex:2088](../../../src/fundamentals_a.tex#L2088) 否定: "... but does not by itself establish magnetic order at finite temperature."
- [ ] [fundamentals_a.tex:2140](../../../src/fundamentals_a.tex#L2140) 规定: "For entangled bands, a subspace must first be selected within the chosen energy windows."
- [ ] [fundamentals_a.tex:2161](../../../src/fundamentals_a.tex#L2161) 规定: "The interpolation must be checked against direct calculations in the energy range of interest."
- [ ] [fundamentals_a.tex:2167](../../../src/fundamentals_a.tex#L2167) 否定: "Interpolating the band energies alone would not provide the coupling ..."
- [ ] [fundamentals_a.tex:2243](../../../src/fundamentals_a.tex#L2243) 规定: "Its applicability must be checked for the system considered;"
- [ ] [fundamentals_a.tex:2244](../../../src/fundamentals_a.tex#L2244) 规定: "... it should not be extrapolated through a zero or negative denominator in the exponent."
- [ ] [fundamentals_a.tex:2249](../../../src/fundamentals_a.tex#L2249) 否定: "The averaged function $\alpha^2F(\omega)$ alone does not retain the information required ..."
- [ ] [fundamentals_a.tex:2255](../../../src/fundamentals_a.tex#L2255) 规定: "... must be identified with those results."

#### 第 3 章

- [ ] [fundamentals_b.tex:232](../../../src/fundamentals_b.tex#L232) 范围: "Within the adopted independent-particle description, the spectra resolve ..."
- [ ] [fundamentals_b.tex:256](../../../src/fundamentals_b.tex#L256) 否定: "Therefore, these spectra do not describe the complete low-frequency response of the metallic systems." 第 7 章第 350 行, 第 8 章第 196 行重复了同一限定.
- [ ] [fundamentals_b.tex:711](../../../src/fundamentals_b.tex#L711) 范围: "The resulting reflectivity is a parameter of this effective-medium model." 连同第 712 行.
- [ ] [fundamentals_b.tex:714](../../../src/fundamentals_b.tex#L714) 对比: "... a formal out-of-plane response of the scalar model, not a second normal-incidence channel of the layer."
- [ ] [fundamentals_b.tex:783](../../../src/fundamentals_b.tex#L783) 规定: "finite momentum and surface contributions require the appropriate scattering geometry."
- [ ] [fundamentals_b.tex:799](../../../src/fundamentals_b.tex#L799) 否定: "... so a peak alone does not establish a plasmon."
- [ ] [fundamentals_b.tex:816](../../../src/fundamentals_b.tex#L816) 否定: "Therefore, a large imaginary part does not by itself produce a strong loss peak." 可改为 "A larger imaginary part therefore lowers the loss peak at the zero crossing."

#### 第 4 章

- [ ] [fundamentals_c.tex:10](../../../src/fundamentals_c.tex#L10) 否定: "... information that is not specified by the band energies alone."
- [ ] [fundamentals_c.tex:207](../../../src/fundamentals_c.tex#L207) 规定: "We must therefore specify the band count when assigning a topological index ..."
- [ ] [fundamentals_c.tex:211](../../../src/fundamentals_c.tex#L211) 图注: "... they are not calculated beryllene bands."
- [ ] [fundamentals_c.tex:235](../../../src/fundamentals_c.tex#L235) 待定: "This isolation requires a separate check beyond the illustrated cuts."
- [ ] [fundamentals_c.tex:260](../../../src/fundamentals_c.tex#L260) 对比: "...; they are not two separate bands."
- [ ] [fundamentals_c.tex:311](../../../src/fundamentals_c.tex#L311) 图注: "...; they contain no calculated parity eigenvalues."
- [ ] [fundamentals_c.tex:313](../../../src/fundamentals_c.tex#L313) 图注: "...; it does not indicate a parity or a topological class."
- [ ] [fundamentals_c.tex:377](../../../src/fundamentals_c.tex#L377) 对比: "... the transformation of the state, not the sign of its probability density ..."
- [ ] [fundamentals_c.tex:379](../../../src/fundamentals_c.tex#L379) 否定: "An arbitrary numerical basis of that eigenspace need not already have this form."
- [ ] [fundamentals_c.tex:399](../../../src/fundamentals_c.tex#L399) 规定: "At a non-zero TRIM, it must be included when extracting ..."
- [ ] [fundamentals_c.tex:416](../../../src/fundamentals_c.tex#L416) 规定: "... how parity eigenvalues must be counted in the topological criterion."
- [ ] [fundamentals_c.tex:449](../../../src/fundamentals_c.tex#L449) 否定: "This does not mean that the projector itself is discontinuous, or that all smooth choices of basis are forbidden."
- [ ] [fundamentals_c.tex:458](../../../src/fundamentals_c.tex#L458) 否定: "This relation does not require a conserved spin component."
- [ ] [fundamentals_c.tex:474](../../../src/fundamentals_c.tex#L474) 否定: "... it does not establish dissipationless transport in the presence of bulk conduction or inelastic processes."
- [ ] [fundamentals_c.tex:475](../../../src/fundamentals_c.tex#L475) 否定: "... cannot be inferred from a parity sign alone ..."
- [ ] [fundamentals_c.tex:492](../../../src/fundamentals_c.tex#L492) 否定: "energy ordering alone does not specify these partners."
- [ ] [fundamentals_c.tex:518](../../../src/fundamentals_c.tex#L518) 图注: "they are not parity results for a particular material."
- [ ] [fundamentals_c.tex:521](../../../src/fundamentals_c.tex#L521) 对比: "... an additional topological result, not a consequence of degeneracy counting."
- [ ] [fundamentals_c.tex:524](../../../src/fundamentals_c.tex#L524) 否定: "it does not equate an arbitrary-loop single-band Berry phase with $\mathrm{\pi}\nu$."
- [ ] [fundamentals_c.tex:565](../../../src/fundamentals_c.tex#L565) 否定: "The equality of the final expressions does not make the two Brillouin zones equivalent."
- [ ] [fundamentals_c.tex:570](../../../src/fundamentals_c.tex#L570) 否定: "A high-symmetry path alone does not justify the reduction."
- [ ] [fundamentals_c.tex:589](../../../src/fundamentals_c.tex#L589) 否定: "The small atomic number of an element does not justify omitting spin-orbit coupling from this step:"
- [ ] [fundamentals_c.tex:598](../../../src/fundamentals_c.tex#L598) 否定: "... the phrase ``occupied bands'' alone does not identify the subspace."
- [ ] [fundamentals_c.tex:600](../../../src/fundamentals_c.tex#L600) 否定: "Numerical smearing of the occupations also does not define a fixed-rank projector."
- [ ] [fundamentals_c.tex:601](../../../src/fundamentals_c.tex#L601) 规定: "The band count must instead refer to the selected spectral subspace at every wave vector."
- [ ] [fundamentals_c.tex:604](../../../src/fundamentals_c.tex#L604) 否定: "... does not establish the condition throughout that zone."
- [ ] [fundamentals_c.tex:607](../../../src/fundamentals_c.tex#L607) 规定: "... its accuracy near those separations must be checked against direct calculations."
- [ ] [fundamentals_c.tex:608](../../../src/fundamentals_c.tex#L608) 规定: "A near-zero separation requires particular care ..."
- [ ] [fundamentals_c.tex:614](../../../src/fundamentals_c.tex#L614) 规定: "... the inversion representation must be resolved within that group ..."
- [ ] [fundamentals_c.tex:621](../../../src/fundamentals_c.tex#L621) 否定: "A parity product alone does not establish a $\mathbb{Z}_2$ invariant if ..."
- [ ] [fundamentals_c.tex:633](../../../src/fundamentals_c.tex#L633) 否定: "... cannot be applied without further justification."

#### 第 5 章

- [ ] [project_1_main.tex:89](../../../src/project_1_main.tex#L89) 否定: "... the calculations do not establish the performance of a fabricated device."
- [ ] [project_1_main.tex:485](../../../src/project_1_main.tex#L485) 待定: "... their dispersion and lifetimes are not calculated here."
- [ ] [project_1_main.tex:574](../../../src/project_1_main.tex#L574) 规定: "These near-zero values must be considered together with $\varepsilon_2$ and the energy-loss spectrum;"
- [ ] [project_1_main.tex:575](../../../src/project_1_main.tex#L575) 否定: "they do not alone determine the reflectivity or establish a plasmon resonance."
- [ ] [project_1_main.tex:640](../../../src/project_1_main.tex#L640) 否定: "it need not coincide with the first maximum of $\varepsilon_2(\omega)$." 第 6 章第 793 行重复.
- [ ] [project_1_main.tex:670](../../../src/project_1_main.tex#L670) 否定: "... the negative real part alone does not establish a plasmon resonance."
- [ ] [project_1_main.tex:708](../../../src/project_1_main.tex#L708) 规定: "Their optical transparency should be interpreted together with ... does not by itself guarantee weak attenuation."

#### 第 6 章

- [ ] [project_2_main.tex:28](../../../src/project_2_main.tex#L28) 待定: 本章摘要中的 "... small imaginary phonon frequencies near $\Gamma$ require further convergence checks."
- [ ] [project_2_main.tex:315](../../../src/project_2_main.tex#L315) 对比: "The latter broadening is a numerical parameter, rather than a fitted carrier scattering rate."
- [ ] [project_2_main.tex:349](../../../src/project_2_main.tex#L349) 规定: "... this rescaling should not be identified with a unique intrinsic out-of-plane dielectric constant."
- [ ] [project_2_main.tex:426](../../../src/project_2_main.tex#L426) 否定: "This positive difference does not establish o-\ce{B14} as the thermodynamic ground-state phase."
- [ ] [project_2_main.tex:542](../../../src/project_2_main.tex#L542) 待定: "... their numerical origin has not been established by the present calculations."
- [ ] [project_2_main.tex:550](../../../src/project_2_main.tex#L550) 否定: "... it does not establish thermodynamic stability against all competing phases or experimental synthesizability."
- [ ] [project_2_main.tex:587](../../../src/project_2_main.tex#L587) 否定: "... and does not determine a finite-temperature magnetic ordering temperature."
- [ ] [project_2_main.tex:629](../../../src/project_2_main.tex#L629) 对比: "... a possible interpretation of the calculated HSE06 ordering, rather than an independent determination ..."
- [ ] [project_2_main.tex:653](../../../src/project_2_main.tex#L653) 否定: "neither result alone establishes the experimental gap."
- [ ] [project_2_main.tex:688](../../../src/project_2_main.tex#L688) 否定: "A larger $\lambda$ does not necessarily imply a higher $T_c$, since ..."
- [ ] [project_2_main.tex:692](../../../src/project_2_main.tex#L692) 否定: "This result does not determine superconductivity in the gapped antiferromagnetic HSE06 state."
- [ ] [project_2_main.tex:712](../../../src/project_2_main.tex#L712) 范围: "... within the stated electronic and vibrational approximations."
- [ ] [project_2_main.tex:715](../../../src/project_2_main.tex#L715) 待定: "... remain a limitation of the stability assessment."
- [ ] [project_2_main.tex:717](../../../src/project_2_main.tex#L717) 规定: "The Allen--Dynes and anisotropic Migdal--Eliashberg estimates should be compared separately."
- [ ] [project_2_main.tex:763](../../../src/project_2_main.tex#L763) 否定: "... this response does not by itself determine the free-carrier scattering rate or the dc limit."
- [ ] [project_2_main.tex:767](../../../src/project_2_main.tex#L767) 否定: "small band overlap does not require strong optical transitions in every polarization."
- [ ] [project_2_main.tex:793](../../../src/project_2_main.tex#L793) 否定: "The absorption onset need not coincide with the first maximum of $\varepsilon_{2}(\omega)$."
- [ ] [project_2_main.tex:801](../../../src/project_2_main.tex#L801) 规定: "A quantitative comparison requires consistent absorption units and ..."
- [ ] [project_2_main.tex:804](../../../src/project_2_main.tex#L804) 否定: "A negative $\varepsilon_1$ alone does not establish a plasmon resonance:"
- [ ] [project_2_main.tex:807](../../../src/project_2_main.tex#L807) 待定: "A wave-vector-dependent response would be required to establish the dispersion ..."
- [ ] [project_2_main.tex:814](../../../src/project_2_main.tex#L814) 否定: "The negative-$\varepsilon_1$ intervals and the loss maxima need not have identical boundaries."
- [ ] [project_2_main.tex:853](../../../src/project_2_main.tex#L853) 否定: "... do not independently distinguish a plasmon from an interband transition."
- [ ] [project_2_main.tex:881](../../../src/project_2_main.tex#L881) 对比: "These comparisons concern the calculated cohesive energies rather than a complete thermodynamic phase diagram."
- [ ] [project_2_main.tex:890](../../../src/project_2_main.tex#L890) 待定: "Their plasmonic interpretation remains subject to damping and the effective-medium treatment of the layers."
- [ ] [project_2_SI.tex:140](../../../src/project_2_SI.tex#L140) 待定: 图 S2.9 图注中的 "further checks are required to distinguish this possibility from a physical instability."

#### 第 7 章

- [ ] [project_3_main.tex:25](../../../src/project_3_main.tex#L25) 范围: 本章摘要中的 "... under the stated effective-thickness convention."
- [ ] [project_3_main.tex:333](../../../src/project_3_main.tex#L333) 对比: "... provide scalar comparisons rather than optical constants obtained from the full dielectric tensor."
- [ ] [project_3_main.tex:335](../../../src/project_3_main.tex#L335) 否定: "... which need not equal the corresponding component of the inverse tensor."
- [ ] [project_3_main.tex:338](../../../src/project_3_main.tex#L338) 对比: "... not the full reflection of a finite anisotropic layer on a substrate."
- [ ] [project_3_main.tex:350](../../../src/project_3_main.tex#L350) 否定: "They therefore do not describe the complete low-frequency response of these metallic systems."
- [ ] [project_3_main.tex:509](../../../src/project_3_main.tex#L509) 待定: "... but the dynamical stability near $\Gamma$ remains to be established."
- [ ] [project_3_main.tex:528](../../../src/project_3_main.tex#L528) 待定: "... so the full anharmonic stability of 2H-$\beta$-beryllene remains to be established."
- [ ] [project_3_main.tex:624](../../../src/project_3_main.tex#L624) 待定: "... but this barrier has not been calculated."
- [ ] [project_3_main.tex:626](../../../src/project_3_main.tex#L626) 否定: "... so this comparison does not replace a global structure search."
- [ ] [project_3_main.tex:784](../../../src/project_3_main.tex#L784) 对比: "... rather than a quantum spin Hall state at the Fermi level." 含义要保留, 只改句式.
- [ ] [project_3_main.tex:788](../../../src/project_3_main.tex#L788) 范围: "... the resulting $\mathbb{Z}_2$ indices are conditional screening results." 第 919, 926, 1270 行重复了同一限定, 保留一处.
- [ ] [project_3_main.tex:919](../../../src/project_3_main.tex#L919) 范围: "... in the same conditional sense as $\alpha$-beryllene."
- [ ] [project_3_main.tex:926](../../../src/project_3_main.tex#L926) 对比: "... a band inversion rather than a quantum spin Hall insulating state." 与第 784 行重复.
- [ ] [project_3_main.tex:929](../../../src/project_3_main.tex#L929) 待定: "... has not been established separately from the local refinement of their minima."
- [ ] [project_3_main.tex:945](../../../src/project_3_main.tex#L945) 否定: "... but does not establish isolation of the corresponding subspaces throughout the Brillouin zone ..."
- [ ] [project_3_main.tex:1014](../../../src/project_3_main.tex#L1014) 对比: "these are sampled endpoints rather than interpolated zeros."
- [ ] [project_3_main.tex:1017](../../../src/project_3_main.tex#L1017) 否定: "They do not by themselves establish propagating modes ..." 见 examples.md 的 B1.
- [ ] [project_3_main.tex:1018](../../../src/project_3_main.tex#L1018) 对比: "The numerical broadening is an input to the calculation, not a calculated scattering lifetime."
- [ ] [project_3_main.tex:1035](../../../src/project_3_main.tex#L1035) 否定: "... the larger maxima do not imply that $\beta$-beryllene absorbs more strongly at every energy."
- [ ] [project_3_main.tex:1048](../../../src/project_3_main.tex#L1048) 否定: "... do not by themselves identify a plasmon resonance."
- [ ] [project_3_main.tex:1093](../../../src/project_3_main.tex#L1093) 对比: "this boundary value is not a resolved peak."
- [ ] [project_3_main.tex:1096](../../../src/project_3_main.tex#L1096) 范围: "These spectra describe the inverse dielectric response under the stated effective-thickness convention."
- [ ] [project_3_main.tex:1138](../../../src/project_3_main.tex#L1138) 范围: "Under the stated effective-thickness convention, trilayer cubic beryllene does not show a universal absorption enhancement ..."
- [ ] [project_3_main.tex:1146](../../../src/project_3_main.tex#L1146) 对比: "... rather than enhanced absorption throughout the visible and near-ultraviolet regions."
- [ ] [project_3_main.tex:1150](../../../src/project_3_main.tex#L1150) 否定: "...; they do not alone establish propagating plasmon modes."
- [ ] [project_3_main.tex:1181](../../../src/project_3_main.tex#L1181) 对比: "... not a thickness-independent measure of oscillator strength."
- [ ] [project_3_main.tex:1191](../../../src/project_3_main.tex#L1191) 否定: "... it does not produce a common peak energy, a common zero crossing, or a monotonic enhancement ..."
- [ ] [project_3_main.tex:1192](../../../src/project_3_main.tex#L1192) 规定: "The imaginary dielectric peaks should also be distinguished from maxima of the derived absorption coefficient."
- [ ] [project_3_main.tex:1214](../../../src/project_3_main.tex#L1214) 对比: "... are not evidence of a sharply defined absorption onset or strong visible absorption."
- [ ] [project_3_main.tex:1232](../../../src/project_3_main.tex#L1232) 否定: "The comparisons depend on the stated thickness convention and do not include a Drude intraband contribution."
- [ ] [project_3_main.tex:1244](../../../src/project_3_main.tex#L1244) 待定: "... leave the long-wavelength stability of 1H-$\beta$-beryllene unresolved."
- [ ] [project_3_main.tex:1248](../../../src/project_3_main.tex#L1248) 待定: "The full anharmonic stability requires further examination of coupling between modes."
- [ ] [project_3_main.tex:1265](../../../src/project_3_main.tex#L1265) 范围: "... under the stated effective-thickness convention and exclude a Drude intraband contribution."
- [ ] [project_3_main.tex:1270](../../../src/project_3_main.tex#L1270) 范围: "... these indices are conditional screening results for band inversions rather than quantum spin Hall states."
- [ ] [project_3_SI.tex:62](../../../src/project_3_SI.tex#L62) 对比: "... and is not a unique physical layer thickness."
- [ ] [project_3_SI.tex:79](../../../src/project_3_SI.tex#L79) 否定: "These comparisons do not establish convergence of the complete low-frequency metallic response ..."
- [ ] [project_3_SI.tex:81](../../../src/project_3_SI.tex#L81) 对比: "... a final-parameter reference rather than an additional strictly one-parameter convergence point."
- [ ] [project_3_SI.tex:260](../../../src/project_3_SI.tex#L260) 对比: "... rather than replacing a full anharmonic phonon calculation."
- [ ] [project_3_SI.tex:375](../../../src/project_3_SI.tex#L375) 待定: "The dynamical stability of the puckered square layer is not calculated."
- [ ] [project_3_SI.tex:414](../../../src/project_3_SI.tex#L414) 待定: "... has not been tested separately from the total-energy convergence."
- [ ] [project_3_SI.tex:424](../../../src/project_3_SI.tex#L424) 否定: "... but does not establish that the lowest-$N$ spinor subspaces remain isolated ..."
- [ ] [project_3_SI.tex:468](../../../src/project_3_SI.tex#L468) 对比: "... conditional PBE results with spin-orbit coupling, not independently determined HSE06 indices."

#### 第 8 章

结论正文和 Connections 一节中的句子:

- [ ] [conclusion.tex:27](../../../src/conclusion.tex#L27) 否定: "... but these local separations do not establish an insulating gap for the complete bilayer."
- [ ] [conclusion.tex:38](../../../src/conclusion.tex#L38) 否定: "...; this comparison does not imply stronger absorption over the whole spectrum."
- [ ] [conclusion.tex:51](../../../src/conclusion.tex#L51) 否定: "... these two operations need not produce the same trend."
- [ ] [conclusion.tex:63](../../../src/conclusion.tex#L63) 否定: "This comparison illustrates why the coupling constant alone does not determine $T_{\mathrm{c}}$." 见 examples.md 的 B2.
- [ ] [conclusion.tex:69](../../../src/conclusion.tex#L69) 待定: "... whose origin remains unresolved."
- [ ] [conclusion.tex:75](../../../src/conclusion.tex#L75) 否定: "... cannot describe the HSE06 antiferromagnetic semiconductor without a further calculation."
- [ ] [conclusion.tex:89](../../../src/conclusion.tex#L89) 对比: "... candidate two-dimensional structures rather than the thermodynamic ground state of elemental beryllium."
- [ ] [conclusion.tex:91](../../../src/conclusion.tex#L91) 待定: "... the long-wavelength flexural behaviour remains unresolved:"
- [ ] [conclusion.tex:92](../../../src/conclusion.tex#L92) 否定: "... this instability cannot be dismissed solely as an interpolation effect."
- [ ] [conclusion.tex:96](../../../src/conclusion.tex#L96) 否定: "... explains why the classical minimum alone does not determine the distortion in this model:"
- [ ] [conclusion.tex:97](../../../src/conclusion.tex#L97) 待定: "... while leaving coupling to the other modes unresolved."
- [ ] [conclusion.tex:103](../../../src/conclusion.tex#L103) 范围: "... within the adopted thermodynamic treatment."
- [ ] [conclusion.tex:104](../../../src/conclusion.tex#L104) 否定: "This comparison does not establish formation from bulk beryllium."
- [ ] [conclusion.tex:106](../../../src/conclusion.tex#L106) 待定: "Its phonon stability and the reconstruction barrier remain uncalculated."
- [ ] [conclusion.tex:113](../../../src/conclusion.tex#L113) 对比: "... rather than assign a universal electronic effect to hydrogenation."
- [ ] [conclusion.tex:119](../../../src/conclusion.tex#L119) 否定: "... without establishing quantum spin Hall insulators at neutral filling."
- [ ] [conclusion.tex:120](../../../src/conclusion.tex#L120) 规定: "... these fixed subspaces must again be distinguished from an occupied insulating manifold."
- [ ] [conclusion.tex:122](../../../src/conclusion.tex#L122) 否定: "... changes that the metallic or semiconducting classification alone cannot describe."
- [ ] [conclusion.tex:126](../../../src/conclusion.tex#L126) 否定: "... does not establish strong visible absorption across its wide electronic gap."
- [ ] [conclusion.tex:135](../../../src/conclusion.tex#L135) 对比: "... rather than to the label of a light-element material alone."
- [ ] [conclusion.tex:155](../../../src/conclusion.tex#L155) 否定: "... explain why the electronic results do not follow one trend with thickness or hydrogen coverage."
- [ ] [conclusion.tex:160](../../../src/conclusion.tex#L160) 规定: "... we must also distinguish their local separations from the electronic character of the complete system."
- [ ] [conclusion.tex:168](../../../src/conclusion.tex#L168) 否定: "... the distinction between a metal and a semiconductor does not determine an entire optical spectrum."
- [ ] [conclusion.tex:174](../../../src/conclusion.tex#L174) 规定: "Finally, the structural and electronic descriptions must refer to the same physical state."
- [ ] [conclusion.tex:175](../../../src/conclusion.tex#L175) 否定: "An optical spectrum of a non-magnetic reference cannot inherit the gap of a different antiferromagnetic calculation."

Limitations 一节 (第 181 至 226 行) 本来就是写限制的地方, 这些句子保留, 只改成肯定句:

- [ ] [conclusion.tex:191](../../../src/conclusion.tex#L191), 195, 196, 198, 204, 207, 212, 218, 221, 224, 226 行.

Outlook 一节中的句子:

- [ ] [conclusion.tex:241](../../../src/conclusion.tex#L241) 对比: "... the starting point for this calculation, rather than its final criterion."
- [ ] [conclusion.tex:245](../../../src/conclusion.tex#L245) 待定: "... first requires a phonon calculation before its lower electronic energy can support a stronger stability conclusion."
- [ ] [conclusion.tex:256](../../../src/conclusion.tex#L256) 否定: "... determining the amount of hydrogen alone would leave its adsorption arrangement and the underlying lattice unresolved."
- [ ] [conclusion.tex:297](../../../src/conclusion.tex#L297) 对比: "... rather than an idealized bulk-like coefficient."
- [ ] [conclusion.tex:302](../../../src/conclusion.tex#L302) 规定: "... although the film calculation must still account for its interaction with the sheet."
- [ ] [conclusion.tex:309](../../../src/conclusion.tex#L309) 规定: "... should therefore precede a stronger topological claim ..."
- [ ] [conclusion.tex:314](../../../src/conclusion.tex#L314) 规定: "Carrier control, strain, or a substrate should therefore be assessed for a specific purpose:"
- [ ] [conclusion.tex:315](../../../src/conclusion.tex#L315) 否定: "We cannot assume that moving the chemical potential alone removes an indirect overlap ..."
- [ ] [conclusion.tex:316](../../../src/conclusion.tex#L316) 规定: "Transport predictions should follow these checks rather than follow directly from the parity product."
- [ ] [conclusion.tex:319](../../../src/conclusion.tex#L319) 否定: "... an edge spectral feature alone would not determine its topological origin."
- [ ] [conclusion.tex:325](../../../src/conclusion.tex#L325) 否定: "... do not establish either situation in the materials studied here." 所在的 anyon 段落建议整段删去, 见 11.3.

#### 附录 C

- [ ] [appendix_topology.tex:294](../../../src/appendix_topology.tex#L294) 图注: "The pointers therefore describe phase choices, rather than spin directions or real-space vectors."
- [ ] [appendix_topology.tex:312](../../../src/appendix_topology.tex#L312) 否定: "... a Berry phase on an arbitrary loop is not by itself the two-dimensional $\mathbb{Z}_2$ index."
- [ ] [appendix_topology.tex:603](../../../src/appendix_topology.tex#L603) 图注: "The plane represents a subspace of states, rather than an energy band or a plane in the crystal;" 连同第 604 行.
- [ ] [appendix_topology.tex:672](../../../src/appendix_topology.tex#L672) 对比: "They are not two separate occupied bands."

### 11.3 重复与篇幅 (P1)

- [ ] 第 2 章: $\Omega=\Omega[n]$ 显示了 4 次 (label 依次为 `ground_state_observable_expectation_value`, `ground_state_observable_density_functional`, `functional_from_expectation`, `functional_from_density`). HK 定理的结论复述 4 到 5 次. KS 方程在 2.2.2, 2.2.3, 2.2.4 三节各推导一遍.
- [ ] 附录 A: $\hat{U}(\tau)$ 的指数形式显示 4 次 (从 [appendix_quantum.tex:73](../../../src/appendix_quantum.tex#L73) 起). 巨正则系综写了两遍, [appendix_quantum.tex:702](../../../src/appendix_quantum.tex#L702) 的文字说 "compact operator form", 显示的却是求和式. $T_\mathrm{TF}$, $T_\mathrm{vW}$, $E_\mathrm{H}$ 和 Thomas--Fermi 方程各写了两遍. 巨正则系综, 跃迁密度, Bohr 频率, 时序算符在后文都没有用到.
- [ ] 附录 B: $\varepsilon_{\alpha\beta}=\delta_{\alpha\beta}+\chi_{\alpha\beta}$ 显示两次 ([appendix_electrodynamics.tex:202](../../../src/appendix_electrodynamics.tex#L202) 与 [appendix_electrodynamics.tex:370](../../../src/appendix_electrodynamics.tex#L370)), $P_\alpha=\varepsilon_0\sum_\beta\chi_{\alpha\beta}E_\beta$ 显示两次 (第 177 行与第 357 行). 见 examples.md 的 B4.
- [ ] 第 3 章与附录 B 有四段几乎相同: 开头一句 ([fundamentals_b.tex:23](../../../src/fundamentals_b.tex#L23) 与 [appendix_electrodynamics.tex:15](../../../src/appendix_electrodynamics.tex#L15)), 单位约定 ([fundamentals_b.tex:28](../../../src/fundamentals_b.tex#L28) 与 [appendix_electrodynamics.tex:27](../../../src/appendix_electrodynamics.tex#L27)), $\mu_\mathrm{r}\approx1$ ([fundamentals_b.tex:51](../../../src/fundamentals_b.tex#L51) 与 [appendix_electrodynamics.tex:98](../../../src/appendix_electrodynamics.tex#L98)), regular response 前提 ([fundamentals_b.tex:353](../../../src/fundamentals_b.tex#L353) 与 [appendix_electrodynamics.tex:425](../../../src/appendix_electrodynamics.tex#L425)).
- [ ] 第 3 章与第 7 章用同一组铍烯光谱图, 描述也几乎逐字相同, 例如 [fundamentals_b.tex:657](../../../src/fundamentals_b.tex#L657) 与 [project_3_main.tex:1039](../../../src/project_3_main.tex#L1039).
- [ ] 第 5 章与第 6 章有相同的教科书句子: 折射率 ([project_1_main.tex:679](../../../src/project_1_main.tex#L679) 与 [project_2_main.tex:833](../../../src/project_2_main.tex#L833)), 介电张量的含义 ([project_1_main.tex:559](../../../src/project_1_main.tex#L559) 与 [project_2_main.tex:768](../../../src/project_2_main.tex#L768)), 带间跃迁与等离激元的耦合 ([project_1_main.tex:665](../../../src/project_1_main.tex#L665) 与 [project_2_main.tex:352](../../../src/project_2_main.tex#L352)).
- [ ] [fundamentals_c.tex:209](../../../src/fundamentals_c.tex#L209) 第 209 至 221 行在正文中描述图 4.1 的颜色, 箭头和阴影, 移进图注.
- [ ] [conclusion.tex:322](../../../src/conclusion.tex#L322) 第 322 至 328 行的 anyon 段落与本文结果关系很远, 建议删去.

### 11.4 排版与记号 (P2)

- [ ] [fundamentals_a.tex:1843](../../../src/fundamentals_a.tex#L1843) 指数中多了逗号: `\vec{G}` 之后换行写成了 `,)`, PDF 显示为 (k+G,)·r.
- [ ] [fundamentals_a.tex:507](../../../src/fundamentals_a.tex#L507) 第 507 至 521 行把 Slater 行列式的动能代入了相互作用泛函 $E[n]$, 与第 886 行的 $T[n]=T_s[n]+T_c[n]$ 矛盾.
- [ ] [fundamentals_a.tex:254](../../../src/fundamentals_a.tex#L254) "Hence $(E_1-E_2)/N$ is a constant" 应写成 $g(\vec{r}\,)=(E_1-E_2)/N$.
- [ ] [fundamentals_a.tex:972](../../../src/fundamentals_a.tex#L972) 冒号后面没有公式.
- [ ] [fundamentals_a.tex:422](../../../src/fundamentals_a.tex#L422) 和 [appendix_quantum.tex:407](../../../src/appendix_quantum.tex#L407) `\eqref` 前缺空格.
- [ ] 斜体 i 和 e 改为正体: [fundamentals_b.tex:15](../../../src/fundamentals_b.tex#L15), [fundamentals_b.tex:467](../../../src/fundamentals_b.tex#L467), [appendix_quantum.tex:48](../../../src/appendix_quantum.tex#L48), [appendix_quantum.tex:364](../../../src/appendix_quantum.tex#L364).
- [ ] [appendix_quantum.tex:627](../../../src/appendix_quantum.tex#L627) 核排斥项不是 "negligible", 而是一个常数能量平移.
- [ ] [appendix_quantum.tex:431](../../../src/appendix_quantum.tex#L431) "Having seen ..." 引用的是下一节才出现的内容.
- [ ] [appendix_quantum.tex:1119](../../../src/appendix_quantum.tex#L1119) 逗号后的 We 应小写.
- [ ] [appendix_quantum.tex:1089](../../../src/appendix_quantum.tex#L1089) Thomas--Fermi 部分在声明原子单位后又用了 $h^3$ 和 $2m$ (第 1089, 1096 行).
- [ ] [project_1_main.tex:271](../../../src/project_1_main.tex#L271) 第 271, 280, 283 行的引号配对错乱.
- [ ] [project_1_main.tex:124](../../../src/project_1_main.tex#L124) 第 124, 365, 371, 475 至 479 行引用公式用了 `\ref`, 改为 `\eqref`.
