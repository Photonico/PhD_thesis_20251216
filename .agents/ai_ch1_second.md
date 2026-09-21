# Chapter 1 修改操作稿

日期: 2026-09-20.
依据: [Gemini 初稿](ai_ch1_first.md), 两份 examiner reports,
以及当前 `src/introduction.tex` 和 `thesis.bib`.

你按下面的顺序改. 每次完成一个步骤即可, 不必一次改完整章.
本轮主要操作 `src/introduction.tex`; 确需新增文献时再改 `thesis.bib`.
这里的英文代码块是候选正文, 中文是操作说明, 不要放进论文.

当前 Introduction 有 73 行. 下文行号指本次读取的版本;
你开始修改后, 请用给出的英文开头定位, 不再依赖旧行号.
本文件只提供计划, 尚未修改论文或编译新版本.

## 先明确如何采用 Gemini 的方案

采用她的五节结构, 独立 Literature Review, 光学与拓扑动机,
以及逐章研究问题的安排. 不把 12-14 页作为必须达到的指标.
先把评审要求补完整, 再判断篇幅.

主线曾有一个分歧, 你已通过对话框确定采用下面的 Codex 建议:

- Gemini: 将三章写成界面工程, 多中心键合, 轻金属拓扑的递进故事.
- Codex 建议: 将三章写成围绕结构与性质关系的三个互补项目.
  磁性, 超导和拓扑是部分体系的延伸问题, 不要求三个项目共享一种机制.

因此, 最终采用三个互补项目的主线, 保留 Gemini 的五节结构.
下面的英文候选文本按这个决定编写.

还有几处已可按证据修正, 不需要由你在相反事实之间选择:

- bulk o-B14 的来源是 Han 2023 的理论预测, 不能写成已实验合成.
- BC3 外延薄层已有实验研究, 不能与 B4C3 一起归为纯理论预测.
- Li 2023 已报道 alpha-beryllene 的非平庸拓扑,
  不能说此前没有 pristine beryllene 的拓扑研究.
- 本文不同 Tc 属于不同体系和算法, 不应强行统一成同一个数值.

这些修正已落实到下面的操作中. 依据链接放在文件末尾.

## 写作方式: 以你的 Chapter 3 为准

你已明确要求保留自己的写作特点. 本稿以 `src/fundamentals_b.tex`
为主要样本, Chapter 2 为辅助. 之后的候选文本也沿用这个标准.

从 Chapter 3 可以直接看出以下习惯:

1. 先交代问题, 再引入所需概念. 例如第 23-34 行先从 ground-state
   转向外场下的响应, 然后说明为什么需要 electrodynamics.
   Chapter 1 也先写已有研究没有回答什么, 再说我们为什么研究.
2. 用第一人称复数带读者往前走. 常见 `We first`, `We now`,
   `We then`, `We next`, 不必全部改成被动句或抽象名词结构.
3. 一句话推进一个主要意思. 先说明一个量或条件, 下一句解释它的作用,
   然后用 `Therefore` 或 `Accordingly` 接到下一步.
4. 主动保留段落之间的承接. 第 321-335 行先回顾前面的响应框架,
   再说明本节要获得什么. 第 769-793 行也是先说明对象, 再给出路线.
5. 允许有作用的重复. 反复写 `dielectric response` 或完整物理量名称,
   是为了让关系清楚, 不必为了词汇多样性不断换成模糊同义词.
6. 先声明条件和范围, 再给判断. 保留 `For the present work`,
   `Under this approximation`, `In this case`, `At this stage` 的用法,
   但每个限定都要有具体对象.
7. 理论段落采用引入, 表达式, 符号说明, 物理解释, 下一步的顺序.
   第 899-941 行的折射率讨论是清楚的样本. Chapter 1 保留这条解释链,
   但不为模仿风格而额外加入推导. 公式后用 `here,` 解释符号也是
   已有习惯, 保留其说明方式, 同时按实际句法处理大小写和标点.
8. 标题多用 sentence case, 如 `From the dielectric function to optical
   properties`. 小节和章节引用通常写 `section~\ref{...}` 和
   `chapter~\ref{...}`. 英文候选文本采用这些习惯.
9. 源码优先按句子或有意义的从句换行. 长句为避免 Markdown 长行警告
   可以折行, 不把一个词或一个 LaTeX 命令截断.

具体操作时, 先保留原句能够表达清楚的部分, 再补缺少的因果或衔接.
保留你的讲解节奏, 同时修正事实, 语法和无效重复.
不把 `synergistic cohesion`, `investigative journey`, `paradigm`
一类包装性表达当作学术化的必要条件.

下面的文献段落仍使用必要的作者归属, 但段落之间按你的解释习惯衔接.
`Firstly`, `Secondly`, `Therefore` 等词只放在真实存在相应逻辑的位置.

## 第 1 步: 保留章标题, 建立五节结构

保留原文件最上面的两行:

```latex
\chapter{Introduction}
\label{cha:introduction}
```

在它们后面按顺序建立以下标题. 先建立结构, 再按后续步骤把段落放进去.
同一 section 和 label 只保留一份, 不要同时粘贴两套骨架.

```latex
\section{Background and research scope}
\label{sec:intro_background}

\section{Critical literature review}
\label{sec:intro_lit_review}

\subsection{Boron-based materials and graphene heterostructures}
\label{subsec:lit_boron}

\subsection{Beryllene and hydrogen functionalization}
\label{subsec:lit_beryllene}

\subsection{Computational approaches and their limitations}
\label{subsec:lit_methods}

\subsection{Experimental evidence and theoretical models}
\label{subsec:lit_critical_status}

\section{Motivation for optical and topological analysis}
\label{sec:intro_observables}

\subsection{Optical response as a probe of electronic structure}
\label{subsec:opt_observables_motivation}

\subsection{Physical significance of band topology}
\label{subsec:topo_motivation}

\section{Research questions and scope of the thesis}
\label{sec:intro_gaps}

\section{Thesis organisation}
\label{sec:intro_organisation}
```

完成后应得到 1.1 至 1.5. 保持七章编号不变.

## 第 2 步: 整理 1.1, 保留已有背景

把原来以下内容移到 1.1, 按原来的相对顺序排列:

1. 第 4-7 行, 从 `The isolation of graphene demonstrated` 开始的段落.
2. 第 9-12 行, 从 `Beyond graphene` 开始的段落.
3. 第 21-27 行, 从 `Boron-based two-dimensional materials` 开始的段落.
4. 第 29-34 行, 从 `A central challenge` 开始的段落.

其中两处需要改:

- 原第 10 行暂时去掉单一 o-B14 图片作为整个材料类别例子的插入语.
  将该句改为下面第一句.
- 原第 34 行避免把所有性质都写成两种调控手段已经实现的结果.
  将该句改为下面第二句.

```latex
Light-element Xenes and related compounds provide a useful setting for
studying the connection between bonding and physical response.
Their low atomic masses and diverse bonding environments give rise to
structures with different electronic properties.
```

```latex
We therefore use these strategies to examine how structural modification
changes electronic structure and optical response.
For selected systems, we also investigate magnetism, superconductivity,
and band topology.
```

1.1 到这里结束. 不粘贴 Gemini 3.1 中关于三种元素电子组态的整个 itemize.
当前章已有足够的材料背景; 这里用两三句解释硼的缺电子键合和铍的研究价值即可.
也不要把 "解决 graphene 零带隙" 写成全篇唯一动机,
因为后文还研究金属响应与超导.

原第 36-40 行的 DFT 和总体研究目标先剪切出来, 留给第 7 步处理.
原第 42-73 行的逐章概述先保留在编辑器中, 第 8 步再整体替换.

## 第 3 步: 写 1.2.1, 按四个主题组织硼基文献

这一节是新增内容, 不能只把 Chapter 4 或 Chapter 5 的 Introduction 原样搬来.
按下面四段的顺序写. 每段都回答: 前人做了什么, 模型或实验条件是什么,
还有什么没有回答, 与本文哪个研究问题有关.

先在 1.2 的主标题后, 1.2.1 的子标题前, 放一段承接文字:

```latex
The previous section introduced the materials and the structural changes
considered in this thesis.
We now examine what earlier studies have established about these systems.
We first consider boron-based materials and graphene heterostructures,
then turn to beryllium, and finally compare the computational approaches.
Throughout this review, we distinguish experimental observations from
theoretical predictions and identify the questions that remain open.
```

### 3.1 第一段: borophene 的实验与结构背景

先从 `src/project_2_main.tex` 的 Introduction 找到以下文献:

- `chen2022synthesis`.
- `zhong2017metastable`.
- 如要讨论液相获得的薄片, 再核读 `ranjan2019freestanding`.

核对原文后, 选直接相关的研究写一段. 写清具体相型与衬底或制备环境,
随后说明这些实验结果与理想自由层模型的区别.
不要笼统写成 "所有 borophene 都只能在真空衬底上存在".

Gemini 的 Mannix 2015 和 Feng 2016 可以作为补充核读对象,
但对应 bibkey 目前不在库中. 若采用, 从出版社核对后添加题录,
不能直接照她的 "已在库中" 说明操作.

### 3.2 第二段: BC3, B4C3 与已有异质结研究

使用 Chapter 4 已有的这些引用:

- BC3: `yanagisawa2004phonon`, `yanagisawa2006phonon`,
  `tanaka2005novel`.
- B4C3 理论模型: `tian2019`.
- borophene-graphene 实验: `liu2019borophene`, `hou2021borophene`.

可以用下面这段作为起点, 再根据原文补一项与你的比较直接相关的发现:

```latex
Experimental studies have investigated substrate-supported epitaxial
\ce{BC3} sheets~\cite{yanagisawa2004phonon,tanaka2005novel}.
Theoretical work has also proposed other semiconducting boron-carbide
monolayers, including \ce{B4C3}~\cite{tian2019}.
Meanwhile, borophene--graphene heterostructures have been reported
experimentally~\cite{liu2019borophene,hou2021borophene}.
These studies establish relevant materials and interfaces.
However, their structures and environments differ from the idealised
freestanding models considered here.
We therefore compare specified monolayers and their bilayer combinations
in chapter~\ref{cha:project_bilayers}.
The central question is how the interface modifies the electronic
structure and optical response of the constituent layers.
```

关键修正: 不写 "graphene-borophene heterostructures 尚未实现".
研究空白要落在本文比较的具体模型和性质上.

### 3.3 第三段: 从既有 bulk o-B14 引出本文的降维问题

删去 Gemini 中用 Oganov 2009 和 Zhao 2012 指认 o-B14 的段落.
改用当前 Chapter 5 已采用的 `han2023superconducting`.
可用下面这段:

```latex
We next consider a different boron framework.
Han et al. predicted a bulk orthorhombic allotrope, o-\ce{B14}, using
first-principles calculations and evolutionary structure
searches~\cite{han2023superconducting}.
Its structure contains pentagonal bipyramidal units.
This theoretical bulk structure provides the starting point for the
present study.
However, reducing the structure to one or two layers changes the
coordination of the surface atoms.
Hydrogen termination modifies their bonding further.
We therefore examine how these changes affect the electronic, magnetic,
electron--phonon, and optical properties in
chapter~\ref{cha:project_boron}.
```

不把 bulk o-B14 的发现计为本文原创. 不写 "全部低维硼此前只研究平面结构".
若要使用 "首次" 或 "从未研究", 必须有相应检索和时间范围支持.

### 3.4 第四段: 补一组有比较的相关工作

从 `gao2017prediction`, `zhu2019magnetic`, `hou2020ultrastable`,
`li2021synthesis` 中选择直接相关的论文核读.
不要把四个引用一起堆在 "boron has many interesting properties" 后面.

实际写法是: 比较两个研究的结构或氢化方式, 说明采用什么方法得出什么结论,
再指出这些结论不能直接搬到 o-B14. 这一段用于形成真正的 critical review.

完成标准: 本小节同时覆盖实验前例, 理论模型, 具体研究空白;
不再只是材料名称与应用清单.

## 第 4 步: 写 1.2.2, 分清铍的实验, 已有理论与本文扩展

按下面三段写.

第一段介绍结构与实验背景. 核读现有 `ono2020dynamical`,
`hess2022periodicity` 和 `chahal2023beryllene`.
不同论文的 alpha/beta 名称可能对应不同模型, 写作时同时交代结构,
不要仅凭希腊字母认定它们相同.

实验部分可以用下面这段:

```latex
Chahal et al. reported beryllene sheets obtained by sonochemical
exfoliation and characterised several lattice
motifs~\cite{chahal2023beryllene}.
These observations provide an experimental basis for studying
atomically thin beryllium.
However, an observed sheet and an idealised computational phase are
not necessarily the same structure.
We therefore distinguish the reported experimental geometries from
the pristine and hydrogen-functionalized models considered here.
```

第二段介绍已有电子结构与拓扑研究. 使用 `li2023coexistence`,
并将 Gemini 的 "topological characterization ... has remained absent"
改为下面这段:

```latex
Previous first-principles calculations reported superconducting
behaviour in alpha- and beta-beryllene, together with non-trivial band
topology in the alpha phase~\cite{li2023coexistence}.
These results provide a theoretical reference for the present work.
We now extend the structural comparison to a cubic trilayer and selected
hydrogen-functionalized configurations.
Here, the question is how changing the layer geometry and surface bonding
affects the electronic structure, optical response, and band topology.
```

这里的 alpha 和 beta 名称对应 Li 2023 的定义.
需要排成希腊字母时, 改为 `$\alpha$` 和 `$\beta$`.

第三段介绍氢与铍的已有研究:

- `bachurin2015ab`: bulk Be 表面吸附背景.
- `li2018global`: 二维 Be hydride 化合物结构预测.

核读后各用一两句, 然后明确: bulk surface adsorption,
二维 hydride compound 和本文指定母结构上的 hydrogen termination
不是同一个建模问题. 研究空白落在本文具体相型与终止方式的比较上.

可选增强: Li 2023 后有一篇对超导预测提出质疑的
[Petrov and Milosevic Comment][ref-comment]. 若核读后采用,
把它作为预测对数值处理敏感的例子, 清楚注明预印本身份及争议性质.
本轮不必为凑文献数量强行加入, 也不能把质疑写成已经公认的定论.

## 第 5 步: 完成 1.2.3 和 1.2.4

### 5.1 计算方法述评: 比较适用范围, 不写第二遍教材

将 Gemini 的大段方法 itemize 压缩为三至四段.
每段至少联系一项前面提到的材料研究, 说明该方法能支持什么判断,
以及仍未覆盖什么. 不在此处写 cutoff, k-grid 或完整工作流程.

按这个顺序写:

1. PBE, HSE06 与电子激发. 区分 ground-state DFT,
   generalized Kohn--Sham 能带, quasiparticle corrections 和 excitonic effects.
   现有引用可用 `heyd2003hybrid`, `krukau2006influence`,
   `onida2002electronic`, `thygesen2017`.
2. 异质结相互作用与二维光学. 说明色散处理和厚度或环境约定为何重要.
   联系 Chapter 4 的模型, 可用 `grimme2010consistent`,
   `matthes2016influence`.
3. 声子与 AIMD 支持不同层面的稳定性判断, 短轨迹不等于可合成性证明.
   结合 Han 2023 与 beryllene 结构研究比较其证据范围.
4. EPC 与拓扑是选定体系的额外分析. 联系 `li2023coexistence`,
   `ponce2016epw` 和 `fu2007topological`, 说明方法前提;
   具体公式与实现留给后面的理论章或研究章.

删去或改写 Gemini 中这些保证式说法:

- PBE "accurately describes" 所有轻元素晶体的结构, 内聚能与声子.
- HSE06 光谱位移直接称为 "quasiparticle shifts".
- D3 是准确结果的唯一必要方案.
- 默认所有 AIMD 都是 NVT, 300-400 K.

具体比较要跟着读到的文献结果写, 不用一般方法介绍代替文献评价.

### 5.2 实验状态归纳: 先写短列表, 再决定是否排成表格

暂不复制 Gemini 的整个 `tabular{llll}` 和缩放外框.
先在论文中用 `description` 或短段落写清以下分类,
每项引用紧跟对应事实:

- Graphene: 实验已建立, `novoselov2004electric`.
- Borophene: 按所引用论文写明相型与实验环境.
- BC3: 有外延薄层实验前例, 与本文自由层模型区分.
- B4C3: 本文采用的模型来自理论预测, `tian2019`.
- Bulk o-B14: 理论预测, `han2023superconducting`.
- Beryllene sheets: 有实验报道, `chahal2023beryllene`;
  不等同于所有 alpha/beta 命名模型或 cubic trilayer 已实现.
- 本文特定异质结, 低维 o-B14 和氢化结构: 逐项标为本研究的计算模型,
  同时保留相关材料类别已有实验的事实.

如果之后改成表格, 分开列 BC3 与 B4C3,
不要通过整表缩小字号来塞进一页. 引言需要的是清楚的证据分类,
不需要把所有图或所有数值列进表格.

## 第 6 步: 写 1.3, 替换 Gemini 的光学与拓扑解释

### 6.1 光学动机

不要直接粘贴 Gemini 3.3 的整个光学 itemize.
重点改掉以下四点:

- 介电实部过零不能单独作为 plasmon 已被证明的结论.
- 非对角分量不自动证明 chirality 或 optical activity.
- 标量 loss function 不能直接代表所有实验几何下的 EELS 或 surface plasmons.
- 几种派生光学量来自同一响应, 不应被当作几份独立验证.

可将下面的递进说明作为 1.3.1 的主体. 相关方法来源可参见
`onida2002electronic`, `thygesen2017` 和 `matthes2016influence`.

```latex
The previous section discussed the materials and the computational
approaches used to study them.
We now explain why we examine optical response together with electronic
structure.
The electronic structure describes the states available to the electrons.
However, the band energies alone do not determine the response to light.
We also need to consider which transitions are allowed and how their
strength changes with the direction of the electric field.
We therefore compare optical spectra between constituent monolayers and
heterostructures, between different dimensional forms of o-\ce{B14},
and between pristine and hydrogen-functionalized beryllium structures.

Firstly, we compare the transition energies and spectral weight.
These quantities describe how the electronic system responds at
different photon energies within the adopted optical approximation.
We then compare different polarizations to examine optical anisotropy.
The derived absorption, refraction, and reflection describe further
aspects of the same dielectric response.
They therefore provide related descriptions of light propagation,
rather than independent tests of the electronic structure.

Next, we examine the energy-loss features.
Here, a loss peak can indicate a collective excitation, but its
interpretation also depends on dielectric screening and damping.
We therefore consider the loss spectrum together with the real and
imaginary dielectric response~\cite{thygesen2017}.
A peak or a zero crossing alone does not establish a particular
plasmon mode.

Finally, we specify the limits of the optical comparison.
The calculated spectra depend on the treatment of intraband transitions
and electron--hole interactions~\cite{onida2002electronic}.
For two-dimensional models, they also depend on the convention used
for vacuum and effective thickness~\cite{matthes2016influence}.
These choices determine how the calculated response can be related
to a measurement in a particular environment.
```

### 6.2 拓扑动机

将 Gemini 的 Fu--Kane 公式和符号推导留到 Chapter 6 的方法说明中.
Chapter 1 先提出问题, 再说明物理意义与适用边界即可:

```latex
Optical spectra describe the response of the electronic system.
We now consider another question: how are the electronic states
connected across the Brillouin zone?
Band topology addresses this question.
For a two-dimensional insulating system with time-reversal symmetry,
a non-trivial $\mathbb{Z}_2$ invariant is associated with helical edge
states within the corresponding band description~\cite{fu2007topological}.
This connection motivates the study of topology in light-element
structures.

However, the conditions of the classification must be stated.
For a metallic system, we first need to identify the band subspace
being classified.
Its separation from the other bands must hold throughout the
Brillouin zone.
Even when such a subspace exists, its topology does not by itself
establish quantum spin Hall insulating transport in the material.
We therefore examine band topology and metallic behaviour separately
in chapter~\ref{cha:project_beryllene}.
```

不要保留 "completely immune", "dissipationless electronic transport"
或 "symmetry-enforced orbital parity inversion" 作为本论文已经证明的结果.
也不要用 "微小 Fermi surface" 代替全 BZ 带子空间的核查.

Gemini 引用的 Derriche 2024 讨论的是另一类 spinless / 空间对称性相关模型.
若保留, 必须单独说明拓扑类型, 不用它直接证明 spinful Fu--Kane / QSH 结论.
依据见 [Derriche 原文][ref-derriche] 和 [Fu--Kane 原文][ref-fukane].

## 第 7 步: 写 1.4, 明确三个研究问题

这里放回原第 36-40 行中有用的总体目标, 但不原样重复.
将 "DFT allows us to determine stable structures" 改成检查或评估结构稳定性,
避免仅凭一种计算就宣布稳定.

按推荐的互补项目主线, 本节可以采用以下文本:

```latex
The preceding discussion identifies a common question.
How do changes in atomic structure modify the electronic structure
and optical response of light-element two-dimensional materials?
We investigate this question using first-principles calculations.

The three projects examine this question in different bonding environments.
Each project compares a reference structure with a modified structure.
The modification may involve an interface, a change in dimensionality,
or hydrogen termination.
This shared comparison connects the projects.
Magnetism, superconductivity, and band topology enter as further questions
for selected systems.

More specifically, we address the following research questions:
\begin{enumerate}
    \item How does coupling graphene to selected boron-based monolayers
    modify electronic structure and polarization-dependent optical response
    relative to the isolated constituents?
    \item How do dimensional reduction and hydrogen termination alter
    electronic, magnetic, and electron--phonon properties within the
    pentagonal-bipyramid boron framework, and how are these changes reflected
    in the optical response?
    \item How do layer geometry and hydrogen functionalization affect the
    stability, electronic structure, optical anisotropy, and band topology
    of the beryllium configurations examined here?
\end{enumerate}

For the present work, we compare selected structural models using
specified computational approximations.
The calculations provide evidence for the properties of those models.
We therefore state the limits of each prediction and distinguish
computational results from experimental observations.
```

随后回看 1.2: 每个问题必须有文献讨论支撑.
若问题只在这里出现, 回到对应综述段补上为何还值得研究的比较.

不要采用 Gemini 的这些研究空白或贡献表述:

- 此前全部 pristine beryllene 都没有拓扑刻画.
- 本文证明晶体对称性必然产生 QSH 状态.
- 本文已经建立普适的 materials-by-design framework.
- 未做模式分解就认定高频 B-H stretching 是本文 Tc 的主导原因.

## 第 8 步: 用简短路线图替换原来的逐章结果复述

定位原第 42 行 `Chapter~\ref{cha:fundamentals_a} introduces`.
从这里到文件末尾原来的第 73 行, 用下面的路线说明替换.
其中研究目标已在第 7 步处理, 不要再保留一套旧概述.

将这些段落放在 1.5 下:

```latex
The discussion follows the sequence of these research questions.
We first introduce the theoretical framework and then turn to the
three material studies.

Chapter~\ref{cha:fundamentals_a} introduces the many-body problem and
the density-functional framework used in the calculations.
It also discusses the exchange-correlation approximations used later.
Chapter~\ref{cha:fundamentals_b} then develops the linear optical response.
It connects the dielectric response to the optical properties examined
in the research chapters.

In chapter~\ref{cha:project_bilayers}, we compare graphene-based
heterostructures with their constituent monolayers.
This comparison examines how interfacial coupling changes the
electronic structure and optical response.

We next consider the pentagonal-bipyramid boron framework in
chapter~\ref{cha:project_boron}.
Here, we examine the effects of dimensional reduction and hydrogen
termination on electronic, magnetic, electron--phonon, and optical
properties.

Chapter~\ref{cha:project_beryllene} extends the discussion to pristine
and hydrogen-functionalized beryllium structures, including a cubic
trilayer.
We examine their structural stability, electronic properties, optical
response, and band topology.

Finally, chapter~\ref{cha:conclusion_outlook} brings the findings together.
It discusses the limits of the calculations and the questions that
remain for further work.
```

这里先不写 24.3 K, 非平庸 Z2 已证明, 或 optical activity 已证实等细节.
后面各研究章完成核查后, 若确有必要, 再在贡献概述中加入少量已确认结果.

Gemini 3.5 写 Chapter 2 已经包含 practical roadmap,
但当前章尚未按计划修改. 等 Chapter 2 真正改好后再同步补这句话.

## 第 9 步: 处理原 Figure 1.1 与引用

### 9.1 移动现有结构图

把原第 14-19 行的整个 figure 环境移到 1.2.1 中介绍
低维 o-B14 和本文研究对象的段落之后.
保留 `\label{fig:intro}` 和现有图片路径, 不复制出第二张相同图.

在图前添加一句说明:

```latex
An example of the hydrogen-terminated bilayer model considered in this
thesis is shown in Figure~\ref{fig:intro}.
```

图注保留对原子颜色的现有解释, 可加一句:

```latex
The figure illustrates a computational structural model considered in
Chapter~\ref{cha:project_boron}.
```

这张图用于展示本文模型, 不要让它承担实验已合成的证据作用.
如果后续确认图件的体系身份或来源需要修正, 再同步更新图注.

### 9.2 不照 Gemini 的清单批量添加参考文献

她的 LaTeX 候选文本用了 32 个不同 citation key,
其中以下 12 个目前不在 `thesis.bib`:

```text
evans1984beryllium
feng2016experimental
li2018realization
mannix2015synthesis
oganza2009novel
tang2007novel
togo2015first
wu2019experimental
yan2014two
yang2008boron
zhao2012novel
zhao2015predicting
```

缺 key 不等于论文不存在. 但不要为了让编译通过而根据名字补造题录.
本操作稿的英文候选段落仅使用当前库中存在的 key.

优先执行这些有明确依据的修正:

- o-B14 引用 `han2023superconducting`.
- B4C3 模型引用 `tian2019`.
- BC3 实验使用现有 Yanagisawa / Tanaka 相关条目.
- `grimme2010consistent` 已存在, 不要重复添加.
- `derriche2024light` 的现有题录是 Journal of Physics: Condensed Matter,
  36, 465601, 不要照 Gemini 清单改成 Nano Letters.

确实新增引用时, 从原文或出版社核对作者, 标题, 年份和 DOI,
再导入 BibTeX. 每个引用应支持紧邻的具体论断.

## 第 10 步: 完成本章检查, 留下明确回查项

先由你编译, 再对照检查:

- [ ] 目录出现五个主节, Literature Review 是独立部分.
- [ ] 硼基, 铍基和方法述评各有关键研究与局限的比较.
- [ ] BC3 与 B4C3, 实验薄片与理想模型的身份已分开.
- [ ] bulk o-B14 正确引用 Han 2023, 没有写成已实验合成.
- [ ] 三个研究问题都能在前面的综述中找到动机.
- [ ] 光学动机解释为什么比较谱线, 没有重复 Chapter 3 的整套推导.
- [ ] 拓扑物理意义与本文尚待核查的结论分开.
- [ ] `fig:intro` 只定义一次, 图片仍清楚, 前后文字能衔接.
- [ ] 没有 undefined citation, undefined reference 或重复 label.
- [ ] 没有因表格缩放出现难读小字, 也没有代码块中的说明误入论文.

另在修改记录中保留三个跨章回查项:

1. Chapter 4 的张量与派生光学量核查完成后, 回看本章光学措辞.
2. Chapter 5 核查完成后, 回看磁态, 稳定性和超导贡献的表述.
   当前正文中 bulk 的 Allen--Dynes / ME 数值为 28.2 / 31.3 K,
   氢化双层为 18.5 / 24.3 K. 这是现稿的归属关系,
   不是四个数需要改成同一个数, 也不是本次重新计算确认了这些结果.
3. Chapter 6 核查完成后, 回看结构来源与拓扑结论的范围.
   在此之前, 引言使用研究问题与分析范围的表述.

正式回复信现在只记 "准备做什么" 和修改位置.
本章修改完成并核验后, 才采用 "we have revised" 等完成时表述.
回复文件当前路径是 `reports/reply_to_examiners.md`.

## 本次核查依据

以下链接用于核实本稿与 Gemini 初稿之间的事实分歧,
不是要求全部新增进论文的文献清单.

- [Han et al. 原论文摘要][ref-han]: bulk o-B14 的理论预测来源.
- [BC3 外延薄层原论文][ref-bc3]: 外延薄层实验背景.
- [Li et al. 2023 原论文][ref-li]: alpha-beryllene 已有拓扑研究.
- [Chahal et al. 2023 原论文][ref-chahal]: beryllene 实验与结构信息.
- [Derriche et al. 原文][ref-derriche]: 需区分拓扑类型.
- [Fu and Kane 原文][ref-fukane]: 拓扑适用条件及金属带子空间的区分.

[ref-han]: https://pubmed.ncbi.nlm.nih.gov/37232187/
[ref-bc3]: https://doi.org/10.1103/PhysRevLett.93.177003
[ref-li]: https://doi.org/10.1016/j.mtphys.2023.101257
[ref-chahal]: https://www.nature.com/articles/s41699-023-00415-y
[ref-derriche]: https://arxiv.org/html/2404.03832v2
[ref-fukane]: https://arxiv.org/html/cond-mat/0611341v2
[ref-comment]: https://arxiv.org/abs/2407.18254
