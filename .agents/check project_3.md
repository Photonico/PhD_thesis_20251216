# AI checking for project 3

## Gemini 4.0 Carbon

### 总体评价

本次第 7 章（[src/project_3_main.tex](../src/project_3_main.tex)、[src/project_3_SI.tex](../src/project_3_SI.tex)）与 [src/abstract.tex](../src/abstract.tex)、[src/introduction.tex](../src/introduction.tex)、[src/conclusion.tex](../src/conclusion.tex) 的更新质量很高，全书 `latexmk` 编译一次通过（`rc=0`，零未定义标签与文献键，Table 7.3 中的数值与第 2 章公式 `allen_dynes_temperature_estimate` 及 [supercond_data.xlsx](../figures_proj3/superconductivity/supercond_data.xlsx) 完全吻合）。

主要进展体现在三点：
1. **研究链条完整闭环**：新增的 Quantum ESPRESSO + `WannierTools` 拓扑交叉验证，以及 DFPT + EPW 各向同性/各向异性 Migdal--Eliashberg 超导计算（特别是 2H-$\beta$-beryllene 达到 $T_\mathrm{c}^{\mathrm{aniso}} \approx \qty{31.7}{\kelvin}$），已经干净地融入全书摘要、第 1 章（1.2.3、1.3、1.4）、第 7 章首尾以及第 8 章（8.1.3、8.4.2）。
2. **命名与术语统一**：原稿中的 `ST-beryllene`、`α-2HBe`、`β-2H-2Be`、`β-H-2Be` 已全部统一为全书体系名 `trilayer cubic beryllene`、`2H-$\alpha$-beryllene`、`2H-$\beta$-beryllene`、`1H-$\beta$-beryllene`，且在第 1、7、8 章和全书摘要中统一说明了 `ABA-stacked trilayer beryllene with a square lattice`。
3. **防御性句式大幅收敛**：原有的大量消极限定已被替换为条件陈述，D3 结合能的敏感性讨论（[src/project_3_SI.tex](../src/project_3_SI.tex) `L21--25`）与 bcc Be 高温/高压相背景（[src/project_3_main.tex](../src/project_3_main.tex) `L435--439`）交代得直接清楚。

下面按优先级列出核查发现的具体问题与最小化修改建议（所有英文改写均严格按 [SKILL.md](./skills/thesis-writing-style/SKILL.md) 的个人风格给出）。

---

### P0：数据、图表与物理自洽性问题（强烈建议优先处理）

1. **1H-$\beta$-beryllene 的 QE 晶格常数顺序与 k 点网格顺序反置**
   - **位置**：[src/project_3_main.tex](../src/project_3_main.tex) `L338--342` 对照 [src/project_3_SI.tex](../src/project_3_SI.tex) `L542`（`table~\ref{tab:proj3_qe_structures}`）。
   - **问题**：在原始数据（[supercond_draft.docx](../figures_proj3/superconductivity/supercond_draft.docx) Table 2）中，QE 优化的 `β-H-2Be` 取 $a = \qty{2.11}{\angstrom}$（短轴）、$b = \qty{2.32}{\angstrom}$（长轴），因此倒格子矢量 $|\vec{b}_1| > |\vec{b}_2|$，对应的等密度 k 点网格为 $57 \times 52 \times 1$（$57 \times 2.11 \approx 52 \times 2.32 \approx \qty{120.5}{\angstrom}$）。在整理进 [src/project_3_SI.tex](../src/project_3_SI.tex) `L542` 时，为了与正文 VASP 表（$a = 2.322, b = 2.108$）一致，把 $a$ 和 $b$ 对调成了 `2.32 & 2.11`，但正文 `L338` 仍保留了 `$57 \times 52 \times 1$`。按表中 $a = \qty{2.32}{\angstrom}, b = \qty{2.11}{\angstrom}$ 的轴定义，对应的网格应为 `$52 \times 57 \times 1$`。
   - **建议**：将 [src/project_3_main.tex](../src/project_3_main.tex) `L338` 中的 `$57 \times 52 \times 1$` 改为 `$52 \times 57 \times 1$`（或在补充信息表注中说明两套轴向对调）。

2. **图 7.11 子图 (c) 与 (d) 的正文引用错位，且图注未区分符号对应的体系**
   - **位置**：[src/project_3_main.tex](../src/project_3_main.tex) `L1070--1074` 与图注 `L1136--1145`，对照 [superconductivity.pdf](../figures_proj3/superconductivity/superconductivity.pdf) 及 [supercond_data.xlsx](../figures_proj3/superconductivity/supercond_data.xlsx)。
   - **问题**：
     1. 正文 `L1070--1074` 写：“the superconducting gap of 2H-$\beta$-beryllene approaches a finite value at \qtyrange{29}{31}{\kelvin}, while at \qty{32}{\kelvin} and above, it exponentially tends to zero, as shown in figure~\ref{fig:proj3_superconducting_gap}(d).” 核查原图与 Excel 数据可知：**29 K 的收敛点只画在子图 (c) 的空心菱形中**；子图 **(d) 只画了 30 K、31 K、32 K、34 K 四条迭代曲线（至 3000 次迭代，不含 29 K）**。
     2. 图注 `L1139--1140` 写：“Circles and squares represent isotropic Migdal--Eliashberg solutions... (c) and (d) are analogous to (a) and (b), respectively, for 2H-$\beta$-beryllene.” 子图 (a) 同时包含 **1H-$\beta$-beryllene（圆点 + 空心菱形）** 和 **trilayer cubic beryllene（方块）** 两个体系，而子图 (c) 只有 2H-$\beta$-beryllene（圆点 + 空心菱形，并无方块）。图注目前没有点明方块与圆点分别对应哪个体系。
     3. 顺带一提：[superconductivity.pdf](../figures_proj3/superconductivity/superconductivity.pdf) 顶部带有大标题 `Superconductivity in pristine and hydrogen-functionalized beryllenes`，而第 7 章其余 `*_thesis.pdf` 图均无顶部总标题（且本章正文材料名不用复数 `beryllenes`）。若方便出图可裁去顶栏标题；若保持原图也不影响阅读。
   - **建议改写**：
     - `L1070--1074`：
       ```latex
       In the anisotropic calculation,
       the superconducting gap of 2H-$\beta$-beryllene converges to a finite value from \qtyrange{29}{31}{\kelvin} and decays exponentially at \qty{32}{\kelvin} and above,
       as shown in figures~\ref{fig:proj3_superconducting_gap}(c) and~(d).
       ```
     - 图注 `L1139--1144`：
       ```latex
       Circles and squares denote the isotropic Migdal--Eliashberg solutions for 1H-$\beta$-beryllene and trilayer cubic beryllene, respectively,
       while solid curves show fits to $\Delta_0\tanh\left[1.74\left(T_\mathrm{c}/T-1\right)^{1/2}\right]$.
       Open diamonds mark the converged anisotropic gaps below $T_\mathrm{c}$,
       and the shaded band indicates the estimated anisotropic $T_\mathrm{c}$ of 1H-$\beta$-beryllene.
       (b) Fermi-surface-averaged $\Delta(\mathrm{i}\omega_1)$ of 1H-$\beta$-beryllene during the anisotropic Migdal--Eliashberg iterations.
       (c,d) Corresponding isotropic and anisotropic results for 2H-$\beta$-beryllene.
       ```

3. **2H-$\beta$-beryllene 与 1H-$\beta$-beryllene 在 QE DFPT（$12\times 12\times 1$）下声子谱是否全实频需交代一句**
   - **位置**：[src/project_3_main.tex](../src/project_3_main.tex) `L351--354`、`L1076--1078`。
   - **问题**：7.4.2 节（VASP + `phonopy`，$5\times 5\times 1$ 超胞，$\qty{0.05}{\electronvolt}$ 展宽）指出 2H-$\beta$-beryllene 在 $\vec{q}=(-0.4,0.4)$ 存在 $1.65\mathrm{i}\,\si{\tera\hertz}$ 软模，1H-$\beta$-beryllene 在 $\Gamma$ 附近存在插值虚频；而第 2 章公式 `electron_phonon_spectral_moments`（[src/fundamentals_a.tex](../src/fundamentals_a.tex) `L2199`）明确声明了 `These expressions assume a well-defined spectrum of stable phonon modes`。外审看到 7.4.5 节对 2H-$\beta$-beryllene 给出 $\lambda = 1.40$、$\hbar\omega_\mathrm{log} = \qty{19.5}{\milli\electronvolt}$ 时，第一个问题必然是：**QE DFPT 在 $12\times 12\times 1$ q 网格（配合 $\qty{0.02}{Ry} \approx \qty{0.27}{\electronvolt}$ Marzari--Vanderbilt 电子展宽、二维库仑截断及略大的 $a=b=\qty{2.62}{\angstrom}$）下得到的简谐声子谱是否已无虚频，还是在 EPW 积分中截断了虚频模？**
   - **建议**：在 `L351--354` 或 `L1076--1078` 用一句肯定句点明 QE DFPT 声子谱在该参数下的实际状态（例如无虚频或 EPW 的频率阈值处理），即可提前化解外审追问。

4. **Table 7.3 的量纲符号与正文首处 $\mu^*$ 取值交代**
   - **位置**：[src/project_3_main.tex](../src/project_3_main.tex) `L1058--1061`、`L1107--1112`。
   - **问题**：
     1. 第 2 章公式 `allen_dynes_temperature_estimate`（[src/fundamentals_a.tex](../src/fundamentals_a.tex) `L2211`）已显式恢复 $\hbar$，写为 $\frac{\hbar\omega_\mathrm{log}}{1.20\kB}$，其中 $\omega_\mathrm{log}$ 是角频率，$\hbar\omega_\mathrm{log}$ 才具有能量量纲（`meV`）。而 Table 7.3 列标题 `L1107` 写成了 `$\omega_\mathrm{log}$ (meV)`。建议改为 `$\hbar\omega_\mathrm{log}$ (\unit{\milli\electronvolt})`（或正文说明以能量单位给出 $\hbar\omega_\mathrm{log}$），同时表头单位统一用 `\unit{\milli\electronvolt}`、`\unit{\kelvin}`，并将能隙比明确标为 `$2\Delta_0/(\kB T_\mathrm{c}^{\mathrm{iso}})$`（因表中同时列出了三种 $T_\mathrm{c}$）。
     2. `L1060` 首次引用 trilayer cubic beryllene 的 $T_\mathrm{c}^{\mathrm{AD}}=\qty{2.0}{\kelvin}$ 时未说明对应 $\mu^*=0.13$（后两个体系在 `L1064` 和 `L1081` 才说明 `for $\mu^*=0.13$`）。建议在 `L1060` 首次出现时即写明 `for $\mu^*=0.13$`，后两处即可省去重复。

5. **拓扑小节 QE 交叉验证段存在相邻同义重复，且可顺带点明 Be $1s$ 芯态处理并与收敛性句子呼应**
   - **位置**：[src/project_3_main.tex](../src/project_3_main.tex) `L982--984` 与 `L1005--1014`。
   - **问题**：
     1. `L1005--1008` 写：“the parity eigenvalues of the centrosymmetric structures and the Wilson loops give the same $\nu$ as in table~\ref{tab:proj3_topological_parity} for trilayer cubic beryllene, 2H-$\alpha$-beryllene, 2H-$\beta$-beryllene, and 1H-$\beta$-beryllene.” 紧接着下一句 `L1009--1012` 又重复了一遍：“For trilayer cubic beryllene, 2H-$\alpha$-beryllene, and 2H-$\beta$-beryllene, the Wilson loop calculation is consistent with the parity calculation.” 两句内容完全重叠。
     2. QE 计算将 Be $1s$ 纳入价态（因此 trilayer cubic beryllene 最低孤立子空间由 VASP 的 $N=6$ 条旋量带变为包含 6 条平庸 $1s$ 旋量带后的 12 条旋量带，在 $\mathrm{M}$ 附近仍保持约 $\qtyrange{1.2}{1.3}{\milli\electronvolt}$ 的直接能隙且 $\nu=1$）。同时，这意味着 trilayer cubic beryllene 实际上已经通过了更高截断能（$\qty{90}{Ry} \approx \qty{1224}{\electronvolt}$）与更密自洽网格（$56\times 56\times 1$）的独立程序交叉验证！而 `L982--984`（以及补充信息 `L422`、结论章 `L240, 325`）仍按旧稿写成完全未做更高参数检验的消极句式。
   - **建议改写**：
     - 将 `L982--984`（及 [src/project_3_SI.tex](../src/project_3_SI.tex) `L422`）从消极句改为正面条件句：
       ```latex
       In VASP, the plane-wave cutoff and the self-consistent k-point mesh follow the total-energy convergence criteria in section~\ref{3_methods}.
       ```
     - 将 `L1005--1014` 合并精简：
       ```latex
       For the PBE structures optimized in Quantum ESPRESSO,
       where the Be $1s$ semicore states are included in the valence manifold,
       both the TRIM parity products of the centrosymmetric phases and the Wilson-loop spectra reproduce the $\mathbb{Z}_2$ indices in table~\ref{tab:proj3_topological_parity} across trilayer cubic beryllene,
       2H-$\alpha$-beryllene,
       2H-$\beta$-beryllene,
       and 1H-$\beta$-beryllene.
       In particular, the Wannier charge centres of trilayer cubic beryllene switch partners once along the Wilson loop, confirming $\nu=1$ with an independent pseudopotential set and denser k-point mesh.
       ```

---

### P1：跨章节衔接与学位论文规范问题

1. **章标题、8.1.3 节标题与 `publications.tex` 标题尚未体现新增的超导主线**
   - **位置**：[src/project_3_main.tex](../src/project_3_main.tex) `L1`、[src/publications.tex](../src/publications.tex) `L34`、[src/conclusion.tex](../src/conclusion.tex) `L81`。
   - **问题**：2H-$\beta$-beryllene 的强耦合超导（$T_\mathrm{c}^{\mathrm{aniso}} \approx \qty{31.7}{\kelvin}$）现已成为全书摘要、第 1 章和第 8 章的核心亮点之一，但：
     - 第 7 章章标题仍是 `Emergent Topological and Optical Properties in Pristine and Hydrogen-Functionalized Two-Dimensional Beryllium Phases`（目录短标题 `Topological and Optical Properties of Beryllene Phases`）；
     - 第 8 章 `L81` 小节标题仍是 `\subsection{Structure, hydrogenation, and band topology in beryllene}`（既未含超导，也未含光学）。
   - **建议**：`publications.tex` 若对应在投/拟投论文原题可保持不变（或同步更新拟投题目），但第 8 章 `L81` 建议改为 `\subsection{Structure, hydrogenation, topology, and superconductivity in beryllene}` 或 `\subsection{Pristine and hydrogen-functionalized beryllene}`。第 7 章标题也可考虑是否纳入 `Superconducting` / `Electronic`。

2. **第 8 章 8.2（三项工作的横向联系）与 8.4.2（超导展望）遗漏了第 6 章与第 7 章超导的直接对比**
   - **位置**：[src/conclusion.tex](../src/conclusion.tex) `L150--205`（8.2 节）与 `L284--295`（8.4.2 节）。
   - **问题**：
     1. 8.2 节横向串联了电荷重排、层数/晶格几何、氢化对金属-半导体转变的相反作用、子空间能隙以及光学各向异性，唯独没有把**第 6 章氢化 o-\ce{B14} 双层（$\lambda=1.01$）与第 7 章氢化 $\beta$-beryllene（2H-$\beta$ $\lambda=1.40, T_\mathrm{c}^{\mathrm{aniso}}\approx\qty{31.7}{\kelvin}$；1H-$\beta$ $\lambda=0.61, T_\mathrm{c}^{\mathrm{aniso}}\approx\qty{14.2}{\kelvin}$）这两套轻元素氢化超导体系**放在一起对比！其实这两章放在一起非常有物理深度：在硼和铍两类轻元素层状体系中，氢功能化都能保持或诱导出具有显著电声耦合的金属态，且最终 $T_\mathrm{c}$ 同时受耦合强度 $\lambda$、对数平均声子频率 $\omega_\mathrm{log}$ 软化以及费米面能隙各向异性的共同支配。
     2. 8.4.2 节标题是 `\subsection{Magnetic states and superconducting estimates}`，但正文第二段（`L284--295`）虽然顺带提了一句 `as used for beryllene in section~\ref{3_superconductivity}`，整段研究展望却**只讨论了 o-\ce{B14}**，完全没有谈及 2H-$\beta$-beryllene 的非谐声子重整化（如利用 8.4.1 提到的 SSCHA 声子谱重新评估 $\lambda$ 和 $T_\mathrm{c}$）以及高压/衬底稳定条件下的超导验证。在 `L295` 后补两句即可让 8.4.2 真正覆盖两章的超导工作。

3. **首次出现的缩写 `BCS` 未定义，且前置符号/缩略语表可补齐新增条目**
   - **位置**：[src/project_3_main.tex](../src/project_3_main.tex) `L1067`（`above the BCS value of 3.53`）及 [src/font_matter.tex](../src/font_matter.tex)。
   - **问题**：`BCS` 在全书中仅在 `project_3_main.tex` `L1067` 出现一次，未写出全称 `Bardeen--Cooper--Schrieffer (BCS)`，也未收入 [src/font_matter.tex](../src/font_matter.tex) 缩略语表。此外，`DFPT`（已在第 6、7 章使用）也可核查是否已收入 `font_matter.tex`。
   - **建议**：因全书只用一次，最简洁的做法是在 `L1067` 直接写 `the Bardeen--Cooper--Schrieffer (BCS) weak-coupling value of 3.53~\cite{bardeen1957theory}`（或直接写全称不引入缩写）。

4. **多作者合作章节的个人贡献边界（USyd 规范提醒）**
   - **位置**：[src/publications.tex](../src/publications.tex) `L32--36` 与 [src/statement.tex](../src/statement.tex)。
   - **说明**：`publications.tex` 中第 7 章对应手稿作者为 `L. Niu, O. J. Conquest, H. Ma, C. Verdi, and C. Stampfl`。若本次新增的 QE + `WannierTools` + EPW 计算中有一部分由合作者完成或共同完成，按照 USyd 含合作成果学位论文的常见审查要求，建议确认是否需要在 `publications.tex`（或章首脚注/前言）简要注明候选人与合作者的分工（第 5、6 章同理），避免外审将合作计算误读为候选人独立完成或反之低估候选人贡献。若全部由你本人重算完成，则无需额外说明。

5. **第 7 章内部结论段顺序与正文小节顺序不一致（小结构细节）**
   - **位置**：[src/project_3_main.tex](../src/project_3_main.tex) `L1424--1444`。
   - **问题**：正文 7.4 节顺序是 `7.4.4 拓扑 -> 7.4.5 超导 -> 7.4.6 光学`，章摘要（`L28--42`）顺序是 `光学 -> 拓扑 -> 超导`，而 7.5 节结论（`L1424--1444`）顺序是 `光学 -> 超导 -> 拓扑`。将 7.5 节调整为 `拓扑 -> 超导 -> 光学`（与 7.4 节完全一致）或与章摘要统一，读感会更顺畅。

6. **bcc Be 高温/高压相陈述建议补一条文献支撑**
   - **位置**：[src/project_3_main.tex](../src/project_3_main.tex) `L435--439`（当前工作区未暂存改动）。
   - **说明**：`the body-centred cubic phase is stable only close to the melting point and has been predicted, but not conclusively observed, at high pressure.` 物理事实准确（常压下熔点前窄温区的 $\beta$-Be bcc 相及高压相变争议），但作为具体实验/理论相图判断，建议附 1--2 篇标准铍相图文献（如 Lazicki et al. 或 Robert, Rahm & Bernu 等），避免无引用的事实断言。

---

### P2：`SKILL.md` 个人风格与记号微调清单

1. **新增的 DFPT/EPW 方法段与 7.4.5 超导结果段仍保留了 [supercond_draft.docx](../figures_proj3/superconductivity/supercond_draft.docx) 的被动语态簇与非本人连接词**
   - **方法段被动语态簇（[src/project_3_main.tex](../src/project_3_main.tex) `L351--370`）**：这一整段连续使用了 12 个被动句（`are computed`、`is calculated`、`are Wannier-interpolated`、`is checked`、`are set`、`are extracted`、`is calculated`、`is used`、`are solved`、`is found`、`is monitored`、`is estimated`），而紧邻的 `L332--349` 和 `L372--395` 都已统一为你本人的 `we` 主动叙事（[SKILL.md](./skills/thesis-writing-style/SKILL.md) §3.1）。
     - **建议改写（`L351--370`）**：
       ```latex
       We compute the phonon spectra of trilayer cubic beryllene,
       2H-$\beta$-beryllene,
       and 1H-$\beta$-beryllene using density functional perturbation theory~\cite{baroni2001phonons} on a $12 \times 12 \times 1$ q-point mesh,
       and evaluate the electron-phonon coupling with EPW~\cite{lee2023electron,giustino2007electron}.
       We interpolate the electronic states and phonon perturbations with Wannier functions from coarse $24 \times 24 \times 1$ k-point and $12 \times 12 \times 1$ q-point meshes onto $80 \times 80 \times 1$ fine meshes,
       after checking convergence on $40 \times 40 \times 1$ fine meshes.
       We set the electronic and phonon smearings to \qty{0.15}{\electronvolt} and \qty{0.5}{\milli\electronvolt}, respectively,
       with a Matsubara-frequency cutoff of \qty{1.2}{\electronvolt}.
       From the resulting Eliashberg spectral function $\alpha^2F(\omega)$,
       we obtain the coupling strength $\lambda$ and the logarithmic average frequency $\omega_\mathrm{log}$ through equations~\eqref{eliashberg_spectral_function_method} and~\eqref{electron_phonon_spectral_moments}.
       We then determine the superconducting transition temperature $T_\mathrm{c}$ at two levels of approximation.
       Firstly, we apply the simplified Allen--Dynes expression~\eqref{allen_dynes_temperature_estimate}~\cite{allen-dynes,mcmillan1968transition} for Coulomb pseudopotentials $\mu^*$ from 0.10 to 0.16.
       Secondly, we solve the isotropic Migdal--Eliashberg equations on the imaginary axis~\cite{giustino2017electron,eliashberg1960interactions,migdal1958interaction} at $\mu^*=0.13$ and extract $T_\mathrm{c}^{\mathrm{iso}}$ by fitting the temperature dependence of the gap at the lowest Matsubara frequency.
       For 2H-$\beta$-beryllene and 1H-$\beta$-beryllene,
       we further solve the anisotropic Migdal--Eliashberg equations~\cite{margine2013anisotropic} at each temperature for up to 6000 iterations.
       Because convergence slows near $T_\mathrm{c}$,
       we track the gap evolution across iterations.
       A temperature lies below $T_\mathrm{c}$ when the extrapolated gap approaches a non-zero limit across all fitting windows,
       whereas it lies above $T_\mathrm{c}$ when the gap decays exponentially with iteration number.
       Finally, we estimate $T_\mathrm{c}^{\mathrm{aniso}}$ by extrapolating the limiting gaps below $T_\mathrm{c}$ together with the decay rates above $T_\mathrm{c}$.
       ```
   - **7.4.5 结果段连接词（[src/project_3_main.tex](../src/project_3_main.tex) `L1063--1095`）**：建议将原稿痕迹明显的 4 处短语替换为你的常用衔接词（[SKILL.md](./skills/thesis-writing-style/SKILL.md) §3.5）：
     - `L1063`：`The electron-phonon coupling strength $\lambda$ in the case of 2H-$\beta$-beryllene is 1.40` $\rightarrow$ `For 2H-$\beta$-beryllene, the electron-phonon coupling strength reaches $\lambda=1.40$`
     - `L1070`：`In the case of the anisotropic solution,` $\rightarrow$ `In the anisotropic calculation,`
     - `L1082`：`On the other hand, the isotropic Migdal--Eliashberg equations give...` $\rightarrow$ `By contrast, the isotropic Migdal--Eliashberg equations give...`
     - `L1094`：`As a consequence,` $\rightarrow$ `Consequently,`

2. **矢量右括号前的细空格 `\,` 遗漏（[SKILL.md](./skills/thesis-writing-style/SKILL.md) §4.6）**
   - [src/project_3_main.tex](../src/project_3_main.tex) `L284, L289`：`\xi_{2m}(\vec{\Lambda}_i)` $\rightarrow$ `\xi_{2m}(\vec{\Lambda}_i\,)`（与第 4 章及 `font_matter.tex` `L174` 保持一致）
   - [src/project_3_main.tex](../src/project_3_main.tex) `L316`：`$E_{N+1}(\vec{k})-E_{N}(\vec{k})$` $\rightarrow$ `$E_{N+1}(\vec{k}\,)-E_{N}(\vec{k}\,)$`
   - [src/project_3_main.tex](../src/project_3_main.tex) `L836`：`$E_{N+1}(\vec{k})-E_{N}(\vec{k})>0$` $\rightarrow$ `$E_{N+1}(\vec{k}\,)-E_{N}(\vec{k}\,)>0$`（第 8 章 `conclusion.tex` `L324` 已经写了 `\,`）
   - [src/project_3_SI.tex](../src/project_3_SI.tex) `L321`：`\chi_{0}(\vec{q})`、`\xi(\vec{q})` $\rightarrow$ `\chi_{0}(\vec{q}\,)`、`\xi(\vec{q}\,)`
   - [src/project_3_SI.tex](../src/project_3_SI.tex) `L442`：`$E(\vec{k})=E(-\vec{k})$` $\rightarrow$ `$E(\vec{k}\,)=E(-\vec{k}\,)$`

3. **混合裸数字与 `\qty` 的三处小瑕疵（[SKILL.md](./skills/thesis-writing-style/SKILL.md) §4.6）**
   - [src/project_3_main.tex](../src/project_3_main.tex) `L938`（Table 7.2）：`0.929 / \qty{0.415}{\electronvolt}` $\rightarrow$ `\qty{0.929}{\electronvolt} / \qty{0.415}{\electronvolt}`（或与同列其他格统一格式）
   - [src/project_3_SI.tex](../src/project_3_SI.tex) `L328`：`between 0.02 and \qty{0.10}{\electronvolt}` $\rightarrow$ `from \qtyrange{0.02}{0.10}{\electronvolt}`
   - [src/project_3_SI.tex](../src/project_3_SI.tex) `L420`：`between 0.65 and \qty{1.07}{\milli\electronvolt}` $\rightarrow$ `between \qty{0.65}{\milli\electronvolt} and \qty{1.07}{\milli\electronvolt}`（或 `\qtyrange{0.65}{1.07}{\milli\electronvolt}`）

4. **个别残余宣传性形容词与跨分支合并时回退的句子（[SKILL.md](./skills/thesis-writing-style/SKILL.md) §3.3、§3.4、§6.4）**
   - **宣传性/评价性形容词**：
     - [src/abstract.tex](../src/abstract.tex) `L24`：`an unusual bonding network` $\rightarrow$ `a distinct bonding network`（或 `a three-centre-bonded network`）
     - [src/project_3_main.tex](../src/project_3_main.tex) `L83, L99, L119, L130`：7.2 引言中残余两处 `unconventional`、一处 `exceptionally high`（直接给 `\qty{270}{\watt\per\metre\per\kelvin}` 更有力）、一处 `unusual`。
   - **第 8 章两处防御句与一处 `why` 句**：
     - [src/conclusion.tex](../src/conclusion.tex) `L134`：`Its harmonic instability at zero pressure precludes treating it as a stable bulk counterpart under those conditions.` $\rightarrow$ `Because bulk bcc beryllium is harmonically unstable at zero pressure, it enters only as a geometric reference.`
     - [src/conclusion.tex](../src/conclusion.tex) `L170`：`These microscopic comparisons explain why the electronic results follow different trends with thickness and hydrogen coverage.` $\rightarrow$ `These microscopic comparisons account for the opposite electronic trends with thickness and hydrogen coverage.`
     - [src/conclusion.tex](../src/conclusion.tex) `L343`：`The non-trivial band-subspace indices and the separate phonon-mediated pairing predictions in this thesis do not establish either situation in the materials studied here.` $\rightarrow$ `Addressing either route requires going beyond the band-subspace indices and phonon-mediated pairing calculations reported here.`（尤其现在第 7 章同时报道了子空间拓扑与电声超导，改为正面递进句会自然得多）。

## GPT 6.1 Sol
