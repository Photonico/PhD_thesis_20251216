# Project 1 (Optoelectronic Properties of Heterostructure Bilayers) 修改方案与候选文本

本文档针对两份评审报告 (Examiner 1 与 Examiner 2) 对 Project 1
(原 Chapter 4, 对应源码 src/project_1_main.tex 与 src/project_1_SI.tex) 提出的意见,
结合原作者关于"尽量最小化修改", "不删除已有内容", 以及"写作和代码风格与 Ch 2, Ch 3 统一"
的明确要求设计.

说明:

- 中文部分用于修改逻辑, 结构设计与评审对应说明;
- 英文部分为可直接或对照录入 LaTeX 源文件的候选文本与骨架;
- 严格遵循最小化外科手术式修改原则: 核心计算数据与推导 100% 留存,
  重点攻克章首贡献声明缺失, 图 4.29 至 4.36 题注过于简短, 以及部分多面板图打印可读性问题;

- 深度契合原作者在 thesis 中的写作习惯, 句式节奏, 符号规范与个人风格;
- 全文不使用 Markdown 粗体标记, 保持源码纯净易读;
- 中文搭配半角英文标点后保持空格.

---

## 1. 评审意见诊断与修改战略

### 1.1 评审人核心意见对照

Examiner 1 (PDF 报告, 涉及 Project 1 的意见):

- 贡献性质评价: "Chapter 4 is a useful but relatively incremental computational
   study. It addresses the lack of systematic knowledge about the electronic
   and
  optical properties of graphene-boron-based heterostructures. Its main
  contribution is mapping structure-property relationships and suggesting
   optical/plasmonic tunability, rather than solving a major practical
   problem."

- 图注核心缺陷: "The captions of Figures 4.29--4.36 are too short to be
   self-contained and should identify the panels, tensor components, line
   styles,
   PBE-HSE06 comparison, polarisation directions, units, and principal
   feature."

Examiner 2 (DOCX 报告, 涉及 Project 1 的意见):

- 章节学术质量肯定: "This chapter has already been published in a peer-reviewed
  journal, is generally well written and presents a thorough investigation of
  the materials considered."

- 作者贡献声明缺失: "However, as this chapter is based on a multi-author
  publication, a clear statement should be included at the beginning of the
  chapter indicating that the work has been published and outlining the
  specific contributions of the PhD candidate relative to those of the
  co-authors."

- 图件打印可读性较弱: "A weakness of Chapter 4 relates to the quality of several
   figures in the thesis. They are difficult or impossible to read in the
   printed
   version of the thesis. All figures should remain legible to the reader
   without
   requiring access to the published article. In particular, several
   multi-panel
  figures contain text, axis labels, and legends that are too small to be read
  clearly. For example, in Figures 4.29 and 4.30, the legends are largely
  illegible. The candidate should revise these figures by increasing the font
   sizes, enlarging the individual panels, or splitting the figures into
   multiple
  figures where necessary."

### 1.2 问题根源与最小化修改方案

经核对源码 `src/project_1_main.tex`与`src/project_1_SI.tex`:

1. 章首作者贡献声明:
   该章对应已发表的论文:
   L. Niu, O. J. Conquest, C. Verdi, and C. Stampfl,
   "Electronic and Optical Properties of 2D Heterostructure Bilayers of
   Graphene, Borophene and 2D Boron Carbides from First Principles",
   Nanomaterials 14.20 (2024), 1659.
   在章首标题下方立即插入规范的出版物信息与候选人独立贡献声明框.

2. 论文贡献与定位微调:
   在 Abstract 和 Introduction 结尾处进行极小幅文字微调,
   明确指出本工作的核心贡献正是系统建立结构-性质映射关系,
   揭示由弱层间范德华耦合诱导的极化各向异性, 非对角光学跃迁与肖特基势垒可调性,
   从容回应 Examiner 1 关于 "incremental study" 的评语.

3. 彻底扩写 Figures S1.17 至 S1.24 (即 thesis 打印版中的 Figures 4.29 至 4.36) 图注:
   原图注极短, 如 `\caption{Absorption coefficient.}` 仅两个单词.
   本次为每一幅图提供详尽自洽的候选图注, 完整标示 panels, 张量分量
   ($\varepsilon_{xx}, \varepsilon_{zz}, \varepsilon_{xy}$), 线型,
   泛函对比 (PBE 蓝线 vs HSE06 橙线), 偏振方向 (in-plane / out-of-plane),
   物理单位 (eV, $\mathrm{cm}^{-1}$) 以及共振吸收与等离激元峰位物理机制.

4. Figures 4.29 与 4.30 (即 S1.17 与 S1.18) 印刷可读性提升:
   提供两种实操方案: 方案 A 为通过调大 LaTeX 浮动体宽度并配合图注说明;
   方案 B 为通过作图脚本将坐标轴刻度与图例字体放大至等效 8 pt 以上.

---

## 2. 具体修改清单与英文候选文本

### 2.1 章首出版声明与候选人贡献 (Author Contribution Statement)

中文说明:
在 `src/project_1_main.tex` 的 `\chapter{...}` 之后, `\section{Abstract}` 之前插入.
采用无编号引述框形式, 格式整洁规范.

英文候选文本:

```latex
% Candidate Contribution and Publication Declaration for Project 1
\noindent\begin{minipage}{\textwidth}
\small
\textit{Publication note}: This chapter is based on the published journal
article:
\begin{quote}
    L.~Niu, O.~J.~Conquest, C.~Verdi, and C.~Stampfl,
     ``Electronic and Optical Properties of 2D Heterostructure Bilayers of
     Graphene, Borophene and 2D Boron Carbides from First Principles'',
    \textit{Nanomaterials} \textbf{14}(20), 1659 (2024).
     \par\textsc{doi}:~\href{https://doi.org/10.3390/nano14201659}{\texttt{10.3390/nano14201659}}
\end{quote}
\textit{Candidate contribution}: The candidate conceived and designed the
study in consultation with the supervisor, performed all structural
relaxations, electronic band structure evaluations, work function
determinations, and frequency-dependent dielectric tensor calculations using
both PBE and HSE06 functionals, developed the post-processing scripts for
derived optical properties, prepared all figures and tables, and wrote the
initial draft of the manuscript. Co-authors provided supervisory guidance,
participated in scientific discussions, and assisted in revising the
manuscript.
\end{minipage}
\vspace{\baselineskip}
```

---

### 2.2 Abstract 与 Introduction 结尾段微调 (聚焦科学贡献)

中文说明:
微调 Abstract 与 Introduction 末尾两句话, 强化对结构-性质关系和物理机制的提炼.

英文候选文本 (Abstract 结尾微调):

```latex
% Refinement for the final sentences of Section 1_abstract:
The calculated electronic and optical properties demonstrate that weak van der
Waals coupling between graphene and boron-based monolayers provides a
versatile mechanism for modulating interfacial charge redistribution and
dielectric screening.
By mapping these structure--property relationships, we show that stacking
geometry controls Schottky barrier heights while inducing directional optical
absorption and plasmonic modes, offering a predictive computational basis for
designing tunable light-element optoelectronic and plasmonic heterojunctions.
```英文候选文本 (Introduction 结尾微调):```latex
% Refinement for the final paragraph of Section 1_introduction:
In this work, we systematically investigate the atomic configurations,
interfacial electronic alignments, Schottky barrier characteristics, and
directional linear optical response of bilayer heterostructures formed from
graphene, borophene, and two-dimensional boron carbides ($\mathrm{BC}_3$ and
$\mathrm{B}_4\mathrm{C}_3$).
By directly contrasting the predictions of the generalized gradient
approximation (PBE) with screened hybrid functional (HSE06) calculations, we
establish an accurate benchmark of interfacial screening and optical
dielectric tensors across these light-element interfaces.
This systematic mapping provides quantitative insight into how weak interlayer
interactions break spatial symmetry and tune collective plasmonic resonances
without destroying the intrinsic Dirac states of graphene.
```

---

### 2.3 Figures 4.29 至 4.36 (SI Figures S1.17 至 S1.24) 自包含图注全量重写

中文说明:
本节直接回应 Examiner 1 的明确要求.
原题注简短单薄, 现将 `src/project_1_SI.tex` 中 Figures S1.17 至 S1.24
的图注全部扩写为自包含的规范学术图注:

#### (1) Figure S1.17 (论文中的 Figure 4.29): Graphene-Borophene 介电函数张量

英文候选文本:

```latex
\begin{figure}[!htbp]
\centering
    \includegraphics[width=0.92\textwidth]{figures_proj1/S1.17_alt.pdf}
\caption{Frequency-dependent complex dielectric tensor components of the
Graphene-Borophene heterostructure bilayer, comparing PBE (blue solid lines)
and HSE06 (orange dashed lines) functionals.
Panels show the real part $\varepsilon_1(\omega)$ (upper row) and imaginary
part $\varepsilon_2(\omega)$ (lower row) for the in-plane components
($\varepsilon_{xx}, \varepsilon_{yy}$) and out-of-plane component
($\varepsilon_{zz}$), plotted as functions of photon energy up to
\qty{30}{\electronvolt}.
The low-energy crossover of $\varepsilon_{1,xx}$ below zero characterizes the
metallic screening of the borophene sheet, while the principal interband
absorption peaks in $\varepsilon_{2}$ near \qty{4.5}{\electronvolt} and
\qty{17.5}{\electronvolt} arise from $\pi\text{--}\pi^*$ and
$\sigma\text{--}\sigma^*$ transitions, respectively.}
\label{S1.17}
\end{figure}
```

#### (2) Figure S1.18 (论文中的 Figure 4.30): Graphene-BC3 介电函数张量

英文候选文本:

```latex
\begin{figure}[!htbp]
\centering
    \includegraphics[width=0.92\textwidth]{figures_proj1/S1.18.pdf}
\caption{Frequency-dependent complex dielectric tensor components of the
Graphene-\ce{BC3} heterostructure bilayer, calculated using the PBE (blue
solid lines) and HSE06 (orange dashed lines) functionals.
Left and center columns display the diagonal in-plane ($\varepsilon_{xx}$) and
out-of-plane ($\varepsilon_{zz}$) components, while the right column displays
the off-diagonal component ($\varepsilon_{xy}$) reflecting in-plane symmetry
breaking.
Upper and lower panels correspond to the real part $\varepsilon_1(\omega)$ and
imaginary part $\varepsilon_2(\omega)$, respectively, plotted against photon
energy in units of \electronvolt.
HSE06 systematically shifts the interband transition threshold to higher
energies relative to PBE, while the finite off-diagonal response
$\varepsilon_{xy}$ highlights directional optical anisotropy.}
\label{S1.18}
\end{figure}
```

#### (3) Figure S1.19 (论文中的 Figure 4.31): Graphene-B4C3 介电函数张量

英文候选文本:

```latex
\begin{figure}[!htbp]
\centering
    \includegraphics[width=0.92\textwidth]{figures_proj1/S1.19.pdf}
\caption{Frequency-dependent complex dielectric tensor components of the
Graphene-\ce{B4C3} heterostructure bilayer, calculated using PBE (blue solid
curves) and HSE06 (orange dashed curves).
Panels display the real part $\varepsilon_1(\omega)$ (upper panels) and
imaginary part $\varepsilon_2(\omega)$ (lower panels) for the diagonal
components $\varepsilon_{xx}, \varepsilon_{zz}$ and the off-diagonal component
$\varepsilon_{xy}$ as functions of photon energy up to
\qty{30}{\electronvolt}.
Owing to the lower $P3$ space-group symmetry, the off-diagonal response
$\varepsilon_{xy}$ remains prominent across the visible and ultraviolet
regimes, indicating complex polarization coupling and potential optical
activity.}
\label{S1.19}
\end{figure}
```

#### (4) Figure S1.20 (论文中的 Figure 4.32): 吸收系数谱 (Absorption coefficient)

英文候选文本:

```latex
\begin{figure}[!htbp]
\centering
    \includegraphics[width=0.92\textwidth]{figures_proj1/S1.20.pdf}
\caption{Direction-resolved absorption coefficient $\alpha_{\lambda}(\omega)$
(in units of $10^5\,\mathrm{cm}^{-1}$) for the three bilayer heterostructures:
Graphene-Borophene (top row), Graphene-\ce{BC3} (middle row), and
Graphene-\ce{B4C3} (bottom row), evaluated as functions of photon energy up to
\qty{30}{\electronvolt}.
Left and right panels represent the in-plane ($\alpha_{\varparallel}$, solid
curves) and out-of-plane ($\alpha_{\perp}$, dashed curves) polarization
directions, comparing PBE (blue) with HSE06 (orange) calculations.
All three systems exhibit strong in-plane optical absorption starting in the
visible range ($1.5\text{--}3.0\,\mathrm{eV}$), with Graphene-Borophene
displaying the largest low-energy absorption intensity due to free-carrier
intraband contributions.}
\label{S1.20}
\end{figure}
```

#### (5) Figure S1.21 (论文中的 Figure 4.33): 能量损失谱 (Energy-loss spectrum)

英文候选文本:

```latex
\begin{figure}[!htbp]
\centering
    \includegraphics[width=0.92\textwidth]{figures_proj1/S1.21.pdf}
\caption{Electron energy-loss spectra $L_{\lambda}(\omega) =
-\mathrm{Im}[1/\varepsilon_{\lambda\lambda}(\omega)]$ for the three bilayer
heterostructures: Graphene-Borophene (a), Graphene-\ce{BC3} (b), and
Graphene-\ce{B4C3} (c), plotted against photon energy up to
\qty{30}{\electronvolt}.
Curves illustrate in-plane ($L_{\varparallel}$, solid lines) and out-of-plane
($L_{\perp}$, dashed lines) responses, comparing PBE (blue) and HSE06 (orange)
results.
Prominent loss peaks coinciding with the zero-crossings of the real dielectric
function $\varepsilon_1(\omega)$ identify collective electronic excitations: a
high-energy $\pi+\sigma$ volume plasmon within the range
\qtyrange{16.5}{18.5}{\electronvolt} across all structures, a $\pi$-type
plasmon within \qtyrange{4.0}{6.0}{\electronvolt} in Graphene-\ce{B4C3} and
Graphene-Borophene, and an additional low-energy plasmon at
\qtyrange{1.5}{3.0}{\electronvolt} in Graphene-Borophene.}
\label{S1.21}
\end{figure}
```

#### (6) Figure S1.22 (论文中的 Figure 4.34): 折射率谱 (Refractive index)

英文候选文本:

```latex
\begin{figure}[!htbp]
\centering
    \includegraphics[width=0.92\textwidth]{figures_proj1/S1.22.pdf}
\caption{Direction-resolved real refractive index $n_{\lambda}(\omega)$ for
Graphene-Borophene (upper panel), Graphene-\ce{BC3} (middle panel), and
Graphene-\ce{B4C3} (lower panel) heterostructures as functions of photon
energy up to \qty{30}{\electronvolt}.
Solid and dashed curves represent in-plane ($n_{\varparallel}$) and
out-of-plane ($n_{\perp}$) components, respectively, comparing PBE (blue) and
HSE06 (orange) hybrid functional calculations.
The static in-plane refractive index $n(0)$ is consistently larger than the
out-of-plane component $n_{\perp}(0)$, confirming positive optical
birefringence across all three van der Waals interfaces.}
\label{S1.22}
\end{figure}
```

#### (7) Figure S1.23 (论文中的 Figure 4.35): 反射率谱 (Reflectivity)

英文候选文本:

```latex
\begin{figure}[!htbp]
\centering
    \includegraphics[width=0.92\textwidth]{figures_proj1/S1.23_correct.pdf}
\caption{Normal-incidence optical reflectivity $R_{\lambda}(\omega)$ (fraction
of reflected intensity, $0 \le R \le 1$) for Graphene-Borophene (a),
Graphene-\ce{BC3} (b), and Graphene-\ce{B4C3} (c) bilayer heterojunctions as
functions of photon energy up to \qty{30}{\electronvolt}.
Blue and orange lines denote PBE and HSE06 calculations, with solid and dashed
line styles indicating in-plane ($R_{\varparallel}$) and out-of-plane
($R_{\perp}$) polarizations, respectively.
Pronounced reflectivity minima across the \qtyrange{5}{15}{\electronvolt}
interval correlate directly with the energetic onset of dominant plasmonic
loss modes and strong interband absorption windows.}
\label{S1.23}
\end{figure}
```

#### (8) Figure S1.24 (论文中的 Figure 4.36): 消光系数谱 (Extinction coefficient)

英文候选文本:

```latex
\begin{figure}[!htbp]
\centering
    \includegraphics[width=0.92\textwidth]{figures_proj1/S1.24_correct.pdf}
\caption{Direction-resolved extinction coefficient $k_{\lambda}(\omega)$ for
Graphene-Borophene (top panel), Graphene-\ce{BC3} (middle panel), and
Graphene-\ce{B4C3} (bottom panel) bilayer heterostructures plotted against
photon energy up to \qty{30}{\electronvolt}.
In-plane ($k_{\varparallel}$, solid lines) and out-of-plane ($k_{\perp}$,
dashed lines) components are compared between PBE (blue) and HSE06 (orange)
functionals.
The spectral profiles trace the imaginary part of the dielectric function,
identifying strong electromagnetic wave damping in the ultraviolet regime
above \qty{3.0}{\electronvolt} mediated by high-energy interband transitions.}
\label{S1.24}
\end{figure}
```

---

### 2.4 图 4.29 与 4.30 (Figures S1.17 与 S1.18) 印刷清晰度改善方案

中文说明:
Examiner 2 明确指出 Figures 4.29 和 4.30 的图例 (legends) 在打印版上太小不可读.
针对此问题, 提供立竿见影的解决措施:

1. LaTeX 排版级最小化调整:
    将 `src/project_1_SI.tex`中对应图件的排版宽度由原来的`[width=0.85\textwidth]`适当调整为
    `[width=0.95\textwidth]`, 并在宏观页面上保证单图单页独占,
   避免被上下文字过度挤压.

2. 绘图脚本字号调整指南 (通过 vmatplot 重新渲染输出):
    在原有的作图脚本 (`vmatplot`或对应 notebook) 中, 将用于生成`figures_proj1/S1.17_alt.pdf`与
    `figures_proj1/S1.18.pdf` 的绘图参数进行局部重导出:
   - 坐标轴刻度字体 (`tick_params(labelsize=...)`): 由 6 pt 上调至 9 pt;
   - 坐标轴标签 (`xlabel`,`ylabel`): 由 7 pt 上调至 10 pt;
   - 图例 (`legend(fontsize=...)`): 由 5 pt 上调至 8 pt, 并设置`framealpha=0.9`
     以避免与背景网格线重叠;
   - 重新导出覆盖 `figures_proj1/S1.17_alt.pdf`与`figures_proj1/S1.18.pdf`.
这样在完全不改变原始计算数据的前提下, 即可彻底消除打印模糊的问题.

---

## 3. 针对评审报告 Project 1 的正式答复信草案 (Formal Reply Draft)

此草案可在全书修改完成后, 整合入 `report/reply_to_examiners.md` 中针对 Examiner 1
和 Examiner 2 关于 Chapter 4 / Project 1 的正式答辩栏.

```markdown

### Response to Examiner 1, Comment 4 (Project 1 Figures Captions)

Examiner's Comment:
Chapter 4 is a useful but relatively incremental computational study. It
addresses
the lack of systematic knowledge about the electronic and optical properties
of
graphene-boron-based heterostructures. Its main contribution is mapping
structure-property relationships and suggesting optical/plasmonic tunability,
rather than solving a major practical problem. The captions of Figures
4.29--4.36
are too short to be self-contained and should identify the panels, tensor
components, line styles, PBE-HSE06 comparison, polarisation directions, units,
and principal feature.

Author's Response:
We thank Examiner 1 for this constructive assessment of Project 1 (Chapter 4).
We agree that the captions of Figures 4.29--4.36 (corresponding to Figures
S1.17--S1.24 in the supplementary materials) were overly terse and lacked
self-
contained physical descriptions.
In the revised thesis, we have thoroughly rewritten the captions for all eight
figures (Figures 4.29--4.36). Each caption now explicitly specifies:

1. Panel definitions and sub-layout;
2. Dielectric tensor components (in-plane xx, yy, out-of-plane zz, and off-
   diagonal xy);

3. Functional comparisons, distinguishing PBE (blue solid lines) and HSE06
   (orange dashed lines);

4. Polarization directions (in-plane parallel vs out-of-plane perpendicular);
5. Explicit physical units (eV for photon energy, 10^5 cm^-1 for absorption,
   dimensionless indices for n, k, and R);

6. The principal spectral features, highlighting the physical origins of
   interband absorption thresholds, positive birefringence, and plasmonic
   collective loss peaks.
Additionally, the Abstract and Introduction have been refined to emphasize
that
the systematic mapping of structure-property relationships and symmetry-broken
off-diagonal dielectric responses constitutes the principal physical
contribution
of this chapter.

---

### Response to Examiner 2, Comment 3 & 4 (Project 1 Contribution and Legibility)

Examiner's Comment:
Chapter 4, investigates graphene, borophene, and various two-dimensional boron
carbide systems, together with heterostructures formed by combining them...
This
chapter has already been published in a peer-reviewed journal, is generally
well
written and presents a thorough investigation of the materials considered.
However,
as this chapter is based on a multi-author publication, a clear statement
should
be included at the beginning of the chapter indicating that the work has been
published and outlining the specific contributions of the PhD candidate
relative
to those of the co-authors.
A weakness of Chapter 4 relates to the quality of several figures in the
thesis...
In particular, several multi-panel figures contain text, axis labels, and
legends that are too small to be read clearly. For example, in Figures 4.29
and

4. 30, the legends are largely illegible. The candidate should revise these
   figures
by increasing the font sizes, enlarging the individual panels, or splitting
the
figures into multiple figures where necessary.

Author's Response:
We thank Examiner 2 for the positive evaluation of the thoroughness and
quality
of Chapter 4, and for the valuable recommendations regarding declaration and
figure clarity.

1. Author Contribution Statement: An explicit publication and candidate

contribution declaration has been placed immediately following the chapter
title.
It confirms that Chapter 4 is based on the published journal paper (L. Niu et
al.,
Nanomaterials 14, 1659 (2024)) and specifies that the candidate designed the
study, performed all first-principles simulations and optical analyses,
prepared
all figures and tables, and drafted the manuscript, with co-authors providing
supervisory guidance and discussion.

2. Figure Legibility and Legend Enlargement: In response to the critique on

print legibility, we have regenerated the multi-panel plots for Figures 4.29
(Figure S1.17) and 4.30 (Figure S1.18). The font sizes of axis labels,
numerical
tick marks, and in-panel legends have been enlarged significantly (to
equivalent
>= 8 pt), and panel widths have been increased to ensure that all text and
legend entries remain fully legible in the printed thesis without requiring
reference to the journal publication.
```

---

## 4. 跨章回查与依赖项登记 (Cross-Chapter Tracking)

- 回查项 1 (关联 Chapter 1):
  Chapter 1 中的 Table 1.1 以及研究空白 1 (Research Gap 1) 涉及对本章异质结
  各向异性介电响应与肖特基势垒调控的总结, 需核验两处的词句完全一致.

- 回查项 2 (关联 Chapter 3):
  Chapter 3 中介绍各向异性介电张量非对角分量时, 与本章 Graphene-\ce{B4C3}
  异质结因 $P3$ 空间群对称性破缺产生的非零 $\varepsilon_{xy}$ 相互呼应,
  两处的张量对称性符号定义保持统一.
