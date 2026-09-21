# Chapter 3 (Fundamentals II: Linear Optical Response) 修改方案与候选文本 (零删除/全保留方案)

本文档针对两份评审报告 (Examiner 1 与 Examiner 2) 对 Chapter 3 提出的意见,
结合原作者关于"不删除已有推导内容"以及"第 100 页起的示例来自 Chapter 6
(PhD 期间最后一个工作)"的事实验证重新设计.
用于指导 src/fundamentals_b.tex 在 100% 完整保留原有推导的基础上进行精准修订.

说明:

- 中文部分用于修改逻辑, 结构设计与评审对应说明;
- 英文部分为可直接或对照录入 LaTeX 源文件的候选文本与骨架;
- 严格遵循"零删除, 全保留"原则: 原有 1164 行关于麦克斯韦方程组, 极化张量,
  微观介电函数跃迁矩阵元, Kramers-Kronig 严格解析推导与光学参数体系完全保留;

- 彻底解决示例数据归属问题: 明确声明第 100 页起的 alpha- 和 beta-beryllene
  光学光谱为作者本人在 Chapter 6 中的原创计算成果, 修正之前误挂的一串外部文献引用;

- 深度契合论文原作者在 thesis 中的写作习惯, 句式节奏, 符号规范与个人风格;
- 全文不使用 Markdown 粗体标记, 保持源码纯净易读;
- 中文搭配半角英文标点后保持空格.

---

## 1. 评审意见诊断与修改战略

### 1.1 评审人核心意见对照

Examiner 2 (DOCX 报告, 第 2 条意见):

"Chapters 2 and 3 give almost textbook version of the theoretical framework
and
computational methodologies employed throughout the thesis... There are
certain
sections that need to be rectified - From page 100 onwards, optical properties
of
alpha-beryllene and beta-beryllene are discussed as examples within the
methodology
chapter. While the use of examples to illustrate particular concepts is
helpful,
the source of the results should be clearly identified. If the results are
generated
as part of the present thesis, an appropriate statement and cross-reference
should
be provided. If they are taken from published literature, the relevant
citation
should be included."

Examiner 1 (PDF 报告, 涉及 Chapter 3 的意见):

"Chapters 2 and 3 together are also disproportionately long, at approximately
100
pages... Substantial scientific and editorial corrections are therefore
required."
"The motivation for calculating optical properties is also not sufficiently
clear:
absorption, refractive index, reflectivity, and loss spectra are often
presented
as a standard set of outputs rather than as observables answering defined
scientific questions."

### 1.2 问题根源与事实澄清

经核对源码 src/fundamentals_b.tex (行 530 至 1160) 以及作者反馈:

1. 示例数据的真实来源:
   从第 100 页起出现的 6 幅光学光谱图 (Figures 3.1 至 3.6:
   包括介电函数实部与虚部, 吸收系数, 折射率, 消光系数, 反射率, 能量损失谱),
   其研究对象为 alpha-Beryllene 和 beta-Beryllene.
   这正是作者在博士期间最后一个独立工作 (即 Chapter 6: Beryllene Phases) 中完成的
   第一性原理计算数据.

2. 之前的引用混乱原因:
   作者在行 530 处留有注释 % cite my third project here (即指代 Project 3 / Chapter 6).
   但在后续排版时, 在行 868, 983, 1083, 1144 处一次性混杂挂载了多达 7 篇外部文献引用
   (\cite{niu2024electronic,khan2025insight,huang2023optical,suk2024ultrafast,...}).
   其中 niu2024electronic 是作者的 Project 1 (异质结) 论文, 其余为外部文献.
   这种写法直接导致评审人 2 产生严重困惑:
   读者无法判断这些谱线究竟是作者自己算的, 还是从文献中抄录来做教学示例的.

3. 科学动机的针对性补强:
   评审人 1 指出光学性质不能仅仅作为一套例行输出 (routine outputs),
   而需要回答明确的物理问题. 我们在全保留已有推导公式的同时,
   对吸收, 折射, 反射和能量损失谱的物理内涵进行点睛提炼,
   阐明每个物理量如何作为回答能带嵌套, 极化各向异性与等离激元激发的判定探针.

---

## 2. Chapter 3 "零删除"具体修改清单

本章保持全部现有推导 100% 留存, 仅做以下两项外科手术式的精准增强:

### 2.1 明确数据来源并建立与 Chapter 6 的交叉索引 (响应 Examiner 2)

在正文中所有引入 alpha- 和 beta-beryllene 示例的段落以及对应的 6 幅图注中:

- 移除混杂的外部文献引用链 (\cite{niu2024electronic,khan2025insight,...});
- 显式声明: 该光谱系本论文作者在 Chapter 6 中针对单层与双层铍相进行的原创第一性原理计算结果,
  此处提前用作解释各向异性介电张量与推导光学量的代表性示范;

- 正式添加向 Chapter 6 的精确交叉引用: (cf. Chapter~\ref{cha:project_beryllene},
  Section~\ref{sec:proj3_optical_response}).

涉及的具体图件清单:

- Figure 3.1 (行 535): Representative dielectric functions of alpha- and
  beta-beryllene;

- Figure 3.2 (行 868): Absorption coefficients;
- Figure 3.3 (行 988): Refractive indices;
- Figure 3.4 (行 1003): Extinction coefficients;
- Figure 3.5 (行 1088): Reflectivities;
- Figure 3.6 (行 1149): Energy-loss spectra (EELS).

### 2.2 强化光学可观测量的物理动机与科学问题指向 (响应 Examiner 1)

在 Section 3.4 (From the dielectric function to optical properties) 中,
保留原有的电磁波边界条件推导, 在每个光学参量的段首增补 2 至 3 句提纲挈领的物理问题导引:

- 吸收系数 \alpha(\omega): 回答带间直接跃迁阈值, 联合态密度分布与光生载流子产生窗口;
- 折射率 n(\omega) 与消光系数 k(\omega): 回答电磁波在介质内的相速度改变,
  色散耗散行为以及低维界面的光学阻抗匹配;

- 反射率 R(\omega): 回答电磁波在低维表面/界面的功率衰减与法向入射反射屏障;
- 能量损失谱 L(\omega): 回答等离激元集体电子震荡模式 (Plasmon),
  区分单粒子带间阻尼与真正电荷密度波激发.

---

## 3. 具体修改要点与英文候选文本

### 3.1 数据来源澄清与规范引言文本 (用于 Section 3.2 末尾及图注)

中文说明:
在行 530 附近替换原有的注释和模糊语句, 正式确立数据原创归属与章节呼应.

英文候选文本:

```latex
% Replacement for lines 528--534 in src/fundamentals_b.tex:
To illustrate the physical manifestations of direction-resolved dielectric
response in low-dimensional crystals, we examine the calculated in-plane and
out-of-plane dielectric spectra of pristine monolayer $\alpha$-beryllene and
bilayer $\beta$-beryllene.
These spectra are generated within the present thesis via density functional
theory calculations and represent original results from our systematic
investigation of two-dimensional beryllium allotropes presented in
Chapter~\ref{cha:project_beryllene}.
Here, they serve as representative pedagogical examples to demonstrate how
structural anisotropy and dimensional stacking govern the frequency-dependent
dielectric tensor.

\begin{figure}[htbp]
\centering
    \includegraphics[width=0.95\textwidth]{figures_ch3/3.1_dielectric.pdf}
\caption{Representative real and imaginary parts of the in-plane
($\varepsilon_{\varparallel}$) and out-of-plane ($\varepsilon_{\perp}$)
dielectric function as a function of photon energy for $\alpha$-beryllene and
$\beta$-beryllene. The spectra are original first-principles results
calculated in this thesis (cf. Chapter~\ref{cha:project_beryllene}), shown
here to illustrate the direction-resolved complex dielectric response
discussed in the text.}
\label{figure_representative_dielectric_response}
\end{figure}
```

---

### 3.2 光学可观测量引言与图注修正 (用于 Section 3.4 各小节)

#### (1) 吸收系数小节 (Absorption coefficient, 行 860 至 875)

英文候选文本:

```latex
% Replacement for lines 864--871 in src/fundamentals_b.tex:
The absorption coefficient $\alpha(\omega)$ directly addresses the scientific
question of where and how efficiently incident radiation is converted into
interband electronic transitions.
To illustrate the resulting spectral features, the following figure presents
the direction-resolved absorption spectra $\alpha_{\lambda}(\omega)$ for
$\alpha$-beryllene and $\beta$-beryllene, calculated as part of our materials
investigation in Chapter~\ref{cha:project_beryllene}:

\begin{figure}[htbp]
\centering
    \includegraphics[width=0.95\textwidth]{figures_ch3/4.1_absorption.pdf}
\caption{The absorption coefficients for the in-plane and out-of-plane
directions as functions of photon energy for $\alpha$-beryllene and
$\beta$-beryllene. The spectra represent original calculations from
Chapter~\ref{cha:project_beryllene}, demonstrating how interband transition
thresholds and optical attenuation rates vary with structural coordination.}
\label{absorption_coefficient_present_systems}
\end{figure}
```

#### (2) 折射率与消光系数小节 (Refractive index and extinction coefficient, 行 980 至 1015)

英文候选文本:

```latex
% Replacement for lines 981--991 in src/fundamentals_b.tex:
While the absorption coefficient governs total energy attenuation,
optoelectronic device design demands knowledge of the phase velocity and
amplitude decay of the propagating electromagnetic wave.
These quantities are governed by the real refractive index $n(\omega)$ and the
extinction coefficient $k(\omega)$, respectively.
Using equations~\eqref{refractive_index_from_dielectric_response}
and~\eqref{extinction_coefficient_from_dielectric_response}, the calculated
spectra for $\alpha$-beryllene and $\beta$-beryllene (obtained from the
first-principles calculations in Chapter~\ref{cha:project_beryllene}) are
displayed below:

\begin{figure}[htbp]
\centering
    \includegraphics[width=0.95\textwidth]{figures_ch3/4.2_refractive.pdf}
\caption{The refractive indices for the in-plane and out-of-plane directions
as functions of photon energy for $\alpha$-beryllene and $\beta$-beryllene
(calculated in this thesis; cf. Chapter~\ref{cha:project_beryllene}).}
\label{refractive_index_present_systems}
\end{figure}

% Replacement for lines 1000--1007 in src/fundamentals_b.tex:
We next present the corresponding extinction coefficient $k_{\lambda}(\omega)$
spectra, which resolve the spectral dissipation rate in phase space:

\begin{figure}[htbp]
\centering
    \includegraphics[width=0.95\textwidth]{figures_ch3/4.3_extinction.pdf}
\caption{The extinction coefficients for the in-plane and out-of-plane
directions as functions of photon energy for $\alpha$-beryllene and
$\beta$-beryllene (calculated in this thesis; cf.
Chapter~\ref{cha:project_beryllene}).}
\label{extinction_coefficient_alpha_beta_beryllene}
\end{figure}
```

#### (3) 反射率小节 (Reflectivity, 行 1080 至 1092)

英文候选文本:

```latex
% Replacement for lines 1081--1091 in src/fundamentals_b.tex:
The reflectivity $R(\omega)$ addresses the critical physical inquiry of
surface impedance matching and optical shielding, answering how much radiant
power is rejected at normal incidence before penetrating the atomic layer.
The following figure presents the direction-resolved reflectivity spectra
$R_{\lambda}(\omega)$ for $\alpha$-beryllene and $\beta$-beryllene, calculated
using the first-principles framework developed in
Chapter~\ref{cha:project_beryllene}:

\begin{figure}[htbp]
\centering
    \includegraphics[width=0.95\textwidth]{figures_ch3/4.4_reflectivity.pdf}
\caption{The reflectivities for the in-plane and out-of-plane directions as
functions of photon energy for $\alpha$-beryllene and $\beta$-beryllene,
illustrating surface reflection thresholds derived from the original
calculations in Chapter~\ref{cha:project_beryllene}.}
\label{reflectivity_alpha_beta_beryllene}
\end{figure}
```

#### (4) 能量损失谱小节 (Energy-loss spectrum, 行 1140 至 1152)

英文候选文本:

```latex
% Replacement for lines 1142--1152 in src/fundamentals_b.tex:
Crucially, optical absorption does not distinguish between single-particle
interband transitions and collective charge density oscillations.
The electron energy-loss spectrum $L(\omega) =
-\mathrm{Im}[1/\varepsilon(\omega)]$ resolves this ambiguity by addressing the
question of collective plasmonic resonances: prominent peaks in $L(\omega)$
coinciding with zeros or minima in $\varepsilon_1(\omega)$ pinpoint
self-sustained plasmon modes.
The following figure presents the calculated energy-loss spectra
$L_{\lambda}(\omega)$ for $\alpha$-beryllene and $\beta$-beryllene, calculated
as part of our original work in Chapter~\ref{cha:project_beryllene}:

\begin{figure}[htbp]
\centering
    \includegraphics[width=0.95\textwidth]{figures_ch3/4.5_energy-loss.pdf}
\caption{The energy-loss spectra for the in-plane and out-of-plane directions
as functions of photon energy for $\alpha$-beryllene and $\beta$-beryllene
(calculated in this thesis; cf. Chapter~\ref{cha:project_beryllene}). Peaks in
$L(\omega)$ identify directional plasmonic excitations.}
\label{energy_loss_spectrum_alpha_beta_beryllene}
\end{figure}
```

---

## 4. 答辩信中对 Chapter 3 的学术答复草案 (Formal Reply Draft)

此草案可直接并入 report/reply_to_examiners.md 中针对 Examiner 2 (Comment 2)
以及 Examiner 1 (Comment on Optical Properties) 的正式回应栏.

```markdown

### Response to Examiner 2, Comment 2 (Optical Properties of Beryllene)

Examiner's Comment:
Chapters 2 and 3 give almost textbook version of the theoretical framework and
computational methodologies employed throughout the thesis... There are
certain
sections that need to be rectified - From page 100 onwards, optical properties
of alpha-beryllene and beta-beryllene are discussed as examples within the
methodology chapter. While the use of examples to illustrate particular
concepts
is helpful, the source of the results should be clearly identified. If the
results are generated as part of the present thesis, an appropriate statement
and cross-reference should be provided. If they are taken from published
literature, the relevant citation should be included.

Author's Response:
We sincerely thank Examiner 2 for pointing out this ambiguity regarding the
origin of the beryllene optical spectra in Chapter 3.
We clarify that all optical spectra for alpha-beryllene and beta-beryllene
presented from page 100 onwards (Figures 3.1 to 3.6, covering dielectric
functions, absorption, refractive index, extinction coefficient, reflectivity,
and electron energy-loss spectra) are original first-principles calculations
generated as part of the present thesis. Specifically, they stem from our
investigation of two-dimensional beryllium allotropes detailed in Chapter 6.
In the revised thesis, we have rectified this completely:

1. Explicit Attribution: In Section 3.2 and throughout Section 3.4, we have

added explicit statements clarifying that these spectra are original
computational results calculated within this thesis.

2. Cross-References Added: Each relevant figure caption (Figures 3.1--3.6) and

associated text now explicitly cross-references the full physical analysis in
Chapter 6 (e.g., "calculated in this thesis; cf. Chapter 6").

3. Citation Cleanup: We have removed the erroneous pile of external literature

citations that was inadvertently appended to these figure introductory
sentences, ensuring unambiguous attribution of our original data.

---

### Response to Examiner 1, Comment on Optical Properties Motivation

Examiner's Comment:
The motivation for calculating optical properties is also not sufficiently
clear: absorption, refractive index, reflectivity, and loss spectra are often
presented as a standard set of outputs rather than as observables answering
defined scientific questions.

Author's Response:
We thank Examiner 1 for this constructive critique regarding the scientific
motivation behind evaluating optical response functions. In response:

1. Physical Question Mapping: In Chapter 3 (Section 3.4), we have introduced

focused introductory paragraphs for each optical observable, explicitly
explaining what physical inquiry it resolves:
   - Absorption alpha(omega): Identifies interband transition thresholds,
     joint
     density of states, and energy windows of optical attenuation.
   - Refractive index n(omega) and extinction coefficient k(omega): Quantifies
     phase velocity modification, dispersion, and phase-space damping across
     interfaces.
   - Reflectivity R(omega): Determines normal-incidence surface impedance
     mismatch and optical shielding.
   - Energy-loss spectrum L(omega): Directly isolates collective plasmonic
     resonances from single-particle interband damping via the zeros of the
     real dielectric function.

2. Integrated Application: These motivations connect directly to the material-

specific analyses in Chapters 4, 5, and 6, where optical spectra are used to
probe interfacial symmetry breaking, dimensional confinement, and directional
plasmon excitation.
```

---

## 5. 跨章回查与依赖项登记 (Cross-Chapter Tracking)

- 回查项 1 (关联 Chapter 6):
  Chapter 3 中使用的 alpha-beryllene 和 beta-beryllene 光学谱图件
  (figures_ch3/3.1_dielectric.pdf 至 4.5_energy-loss.pdf)
  需与 Chapter 6 中的图件数据完全同源. 在审阅 Chapter 6 时,
  核验两处的坐标范围, 能量单位 (eV) 以及各向异性标注 (xx 与 zz) 是否完全统一.

- 回查项 2 (关联 Chapter 6):
  在修改 Chapter 6 正文时, 同样在相应位置增加与 Chapter 3 的呼应语句
  (例如: "as introduced pedagogically in Chapter~\ref{cha:fundamentals_b}"),
  形成全书前呼后应的严谨结构.
