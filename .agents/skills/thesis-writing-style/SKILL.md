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

语料中反复出现以下用法, 新写和改写时一律替换:

| 原文 | 改为 | 出处举例 |
| --- | --- | --- |
| let us start by <名词> | let us start with <名词> | `fundamentals_a.tex`, `appendix_electrodynamics.tex` |
| we achieve: | we obtain: | `fundamentals_a.tex` |
| we process X as | we treat X as / we regard X as | `fundamentals_a.tex` |
| the problem degenerates to | the problem reduces to | `fundamentals_a.tex` |
| the density of ground state | the ground-state density | `fundamentals_a.tex` |
| it demonstrates as: | it takes the form: | `fundamentals_a.tex` |
| the kernel idea | the key idea / the central idea | `fundamentals_a.tex` |
| Review the expression of ... | Recall the expression for ... | `fundamentals_a.tex` |
| We adopt $i$ labels the electrons | We use $i$ to label the electrons | `appendix_quantum.tex` |
| This is convenient to introduce | It is convenient to introduce | `appendix_quantum.tex` |
| does not aim to review a complete lecture of | does not review | `appendix_electrodynamics.tex` |
| Afterwards, ... then ... | 二者只留一个 | `appendix_electrodynamics.tex` |
| In practice, ... in principle ... | 二者只留一个 | `fundamentals_a.tex` |
| Since A. (无主句) | Since A, B. 或 A. Therefore, B. | `fundamentals_a.tex` |
| If one starts from ...: <公式> Therefore, ... | If we start from ..., then ... | `fundamentals_a.tex` |

## 8. 一致性约定

- 拼写采用 Oxford spelling, 即 -ize 加英式 -our 和 -re: characterize, polarization, normalized, behaviour, favour, colour, neighbour, centre, $\Gamma$-centred. analyse 保留 -yse. 全文 -ize 416 处, -ise 15 处, 后者需统一.
- 复合词放在名词前作定语时加连字符, 作名词时分写. 形容词加名词和名词加名词都按这一条处理.
  - ground state: `the ground state`, `the ground-state density`, `ground-state observables`, `the ground-state $N$-body wave function`. 全文已统一, 定语 92 处, 名词 44 处.
  - first principles: `from first principles`, `first-principles calculations`. 全文已统一. 第 5 章标题中作名词用的 `from First-Principles` 已改为 `from First Principles`.
  - two-dimensional, many-body, low-energy, long-range, short-range, first-order, high-symmetry, single-particle 作定语时全文都已加连字符. 同一词组作名词时分写: at low energy, in two dimensions.
  - 尚未统一: total energy 作定语时混用 (total-energy 8 处, total energy functional 6 处). band gap, band structure, charge density, spin density, density functional 作定语时也混用.
- 区分名词和定语的方法: 后面紧跟被修饰的名词时是定语. 后面接标点, 动词, 介词, 连词, 或同位的符号时是名词, 例如 `the ground state $\ket{\Psi_0}$`, `from the ground state $g$`. 中间插入括号说明时仍按定语处理, 例如 `the ground-state ($g\coloneqq 0$) many-body wave function`.
- 人名并列用 en dash `--`: Kohn--Sham, Hohenberg--Kohn, Kramers--Kronig, Born--Oppenheimer, Thomas--Fermi, Perdew--Burke--Ernzerhof, Heyd--Scuseria--Ernzerhof, Fu--Kane, Allen--Dynes, Migdal--Eliashberg, Schottky--Mott.
- 物理复合词用连字符: spin-orbit, electron-phonon, electron-electron, electron-hole, exchange-correlation. 第 1, 7, 8 章中的 `spin--orbit`, `electron--phonon`, `electron--hole` 改为连字符.
- non- 前缀按英式统一加连字符, 全文已统一: non-interacting, non-zero, non-local, non-locality, non-linear, non-classical, non-relativistic, non-commuting, non-monotonically, non-degenerate, non-trivial, non-magnetic, non-negative, non-negligible, non-Abelian, non-self-consistently, non-spin-polarized. none 和 nonetheless 不属于前缀构词. label 和引用键保持原样, 例如 `general_nonlocal_constitutive_relation`, 不随正文改动.
- 材料名小写: $\alpha$-beryllene, borophene, graphene. 第 3 章的 `$\alpha$-Beryllene` 需改为小写. 化学式用 `\ce{}`.
- 拓扑指数统一写 $Z_2$ (全文 25 处). 摘要, 引言, 结论中的 $\mathbb{Z}_2$ 需统一.
- et al. 用正体, 不用斜体.
- 吸收系数统一用 \unit{\per\nano\metre}.

## 9. 避免的写法

以下写法常见于 AI 修订或他人润色的章节, 不属于作者风格:

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
