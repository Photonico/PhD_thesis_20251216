# Chapter 4 审阅问题报告

日期：2026-09-23。
范围：`src/fundamentals_c.tex`（Chapter 4 "Fundamentals III: Band Topology"，新版印码 131–150，物理 PDF 页 165–184）。
对照版本：`.output/thesis.pdf`（316 页，新）与 `.output/thesis_202608.pdf`（312 页，旧）。
用途：交给负责 Chapter 4 / Chapter 7 的 AI 或作者，复核证据后修改论文源文件。

## 0. 结论

1. **本章不是新写的章节**。旧版 `.output/thesis_202608.pdf` 已含 "Chapter 4 Fundamentals III: Band Topology"（印码 133–150，18 页，公式至 (4.26)）。新版把它扩写为 20 页、公式至 (4.32)，新增内容为：旋量态与 Kramers 配对（§4.1.1 式 4.2、4.3）、投影算符的作用与子空间内部交叉（§4.1.2 式 4.6、图 4.1 的 a–d 分格）、子空间基变换后的非阿贝尔联络（§4.2.3），并把直接间隔、间接间隔与绝缘填充三者明确分开。
2. **公式与逻辑主链正确**。逐式复核 (4.1)–(4.32)：Bloch 规范、周期规范、Berry 联络符号与离散式、非阿贝尔规范变换、时间反演代数、反演代数与 Kramers 对等宇称、四个 TRIM 的计数、Fu–Kane 乘积均无误；无 2π 因子问题；全章 32 处 `\eqref`/`\ref` 全部解析成功，无 `??`。
3. **问题集中在"章内立标准、结果章未执行"**：本章 §4.1.2 与 §4.5 要求拓扑指标只能赋予固定秩、处处具有正直接间隔的谱子空间，而第 7 章给出的三个体系（立方三层铍烯、α-铍烯）是金属，且其 §7.4.4 仍用 "occupied spin-orbit-coupled states" 的说法，全章未报告 $\Delta_\mathrm{dir}$ 或 $2N_p$。摘要与结论对此未加限定。
4. 另有 6 类应当修改的实质问题（TRIM 命名冲突、引文过薄、多带指标链断裂、单带 Berry 相未说明、图 4.1(d) 标注、图 4.2 配色）与若干版面问题（章首页落在偶数页、三处半空页、符号表缺项）。
5. 本次审阅只覆盖 Chapter 4 的表述、物理与体例，以及它与第 7 章的接口；未重新核验 VASP 计算、irvsp 输出或宇称数值本身。

---

## 1. 已核验通过的部分（不需改动）

- 式 (4.1) $\hat h(\vec k)\coloneqq e^{-\mathrm{i}\vec k\cdot\hat{\vec r}}\hat h\,e^{\mathrm{i}\vec k\cdot\hat{\vec r}}$ 与 (4.3) $|u_{n,\vec k+\vec G}\rangle=e^{-\mathrm{i}\vec G\cdot\hat{\vec r}}|u_{n\vec k}\rangle$ 正确，且与第 2 章式 (2.265) 的平面波约定一致（$e^{\mathrm{i}\vec G\cdot\vec L}=1$），因此 (4.24) 的 TRIM 位于 $\vec G/2$ 无误。
- Berry 联络 $\vec{\mathcal A}_n=\mathrm{i}\langle u|\nabla_{\vec k}u\rangle$ (4.12)、规范变换 (4.13)、闭合路径 Berry 相 (4.14)、离散重叠乘积 (4.15) 及其中"负号来自 (4.12) 约定"的说明互相自洽；"规范不变性只对闭合路径成立"表述正确。
- 非阿贝尔联络 (4.17) $[\vec{\mathcal A}]_{mn}=\mathrm{i}\langle u_m|\nabla_{\vec k}|u_n\rangle$ 与 $\vec{\mathcal A}'=U^\dagger\vec{\mathcal A}U+\mathrm{i}U^\dagger\nabla_{\vec k}U$ 正确，单态极限回到 (4.13) 正确。
- 时间反演 $\hat\Theta=\mathrm{i}\hat\sigma_y\hat K$、$\hat\Theta^2=-\hat I$、$\hat\Theta|\uparrow\rangle=-|\downarrow\rangle$、反线性 (4.20)、Kramers 正交性 (4.21)、等能配对 (4.22) 全部正确。
- 反演 $\hat{\mathcal I}^2=\hat I$、$\hat{\mathcal I}\hat h(\vec k)\hat{\mathcal I}^{-1}=\hat h(-\vec k)$、$[\hat{\mathcal I},\hat\Theta]=0$ ⇒ $(\hat{\mathcal I}\hat\Theta)^2=-\hat I$ ⇒ 处处二重简并、TRIM 处 $\xi_n=\pm1$、同一 Kramers 对等宇称 (4.28) 正确；"两态分别计数会把每对贡献平方、丢掉符号"的判断正确。
- 图 4.2 的几何正确：六边形区中 $\mathrm{M}_2=\vec b_2/2$ 位于带内，是倒格矢平移的结果；(4.24) 与图中标注一致；K 点被正确排除在 TRIM 之外。
- 图 4.1 四个分格与 §4.1.2 的隔离条件对应正确（(a) $\Delta_\mathrm{dir}^{\min}>0,\Delta_\mathrm{ind}>0$；(b) $\Delta_\mathrm{dir}^{\min}>0,\Delta_\mathrm{ind}<0$；(c) 带间接触；(d) 子空间内部交叉）。
- 符合全篇体例：章首过渡句与 roadmap、每节 `% opening paragraph`、`here,` 小写、`\vec`/`\mathrm{i}`/`\dif`/`\coloneqq` 用法、英式拼写、标题句首大写、`figure`/`section` 句中不大写均与第 2、3 章一致；`\texorpdfstring{$Z_2$}{Z2}` 的用法与既有章节一致；符号表新增 "Topological symbols" 组（`src/font_matter.tex` 163–172 行）。

---

## 2. 需要修改的问题清单

### P1 第 7 章未执行本章设定的前提（最重要）

**证据**

- 本章印码 149（`src/fundamentals_c.tex` 788–797 行）："We then select the fixed number $2N_\mathrm{p}$ of bands and examine $\Delta_\mathrm{dir}(\vec k)$ from equation (4.7). For an insulator … $2N_\mathrm{p}=N_\mathrm{occ}$ … Equations (4.29) and (4.30) then have the same counting as equations (7.3) and (7.4) in chapter 7. **For a metal, the number of states below $E_\mathrm{F}$ can change with $\vec k$, so the phrase "occupied bands" alone does not identify the subspace. Numerical smearing of the occupations also does not define a fixed-rank projector.**"
- 本章印码 147（645–676 行）：绝缘填充下才有奇数个 Kramers 对边缘态；"For a metallic filling, however, the same interpretation cannot be inferred from a parity sign alone."
- 第 7 章 §7.4.4（`src/project_3_main.tex` 541–543 行）："the $Z_2$ invariant calculated from the parity eigenvalues of **the occupied** spin-orbit-coupled states at the time-reversal invariant momenta"，且式 (7.3) 上限写作 $N_\mathrm{occ}/2$。
- 第 7 章 §7.4.3（462–463、500 行）：立方三层铍烯 "shows metallic behaviour, with multiple bands crossing the Fermi level"，费米能级处 DOS 有限；924 行称 pristine α-铍烯为金属。
- 第 7 章全文无 $\Delta_\mathrm{dir}$、无 $2N_\mathrm{p}$、无二维 BZ 加密证据（`grep -n "direct gap\|direct separation\|isolated\|subspace" src/project_3_main.tex` 无命中）。
- `src/abstract.tex` 39 行、`src/conclusion.tex` 63 行把立方三层铍烯直接写成非平庸 $Z_2$，未加金属性限定。

**问题**

存在性前提（$\Delta_\mathrm{dir}>0$）与所选带数在两章之间没有闭合；本章"计数相同"的说法在当前数据下并不自动成立；本章开头"这一区分对于解释本文的金属体系是必要的"所指向的解释没有落到结果章。

**建议**

1. 第 7 章 §7.4.4 增加一段：明确 $2N_\mathrm{p}$ 的取值，报告沿高对称路径与 $\Gamma$、M、X 附近的 $\Delta_\mathrm{dir}(\vec k)$（必要时对 2D BZ 加密），并说明金属填充下该指标刻画的是"所选固定秩子空间"而非费米能级处的绝缘相。
2. 摘要与结论按本章措辞加限定："non-trivial invariant for the selected band subspace, while the material remains metallic at the Fermi level"。
3. 若 α-铍烯是狄拉克半金属、其隔离由 K 点处的 SOC 微隙提供，需报告该微隙数值与所用 k 网格；否则应说明无法断言该子空间有间隔。

### P2 TRIM 命名与归约在两章之间冲突

**证据**

- 本章印码 142（545–550 行）：方形 BZ 的四个 TRIM 为 $\Gamma$、**两个边心点（标为 X 与 Y）**、**角点 M**；图 4.2(b) 即此画法。
- 本章印码 148（751–759 行）：式 (4.32) $(-1)^\nu=\delta_\Gamma\delta_\mathrm{X}\delta_\mathrm{Y}\delta_\mathrm{M}$，归约用 $\delta_\mathrm{X}\delta_\mathrm{Y}=(\delta_\mathrm{X})^2=1$。
- 第 7 章（586–589 行）："For cubic trilayer beryllene, the two $\mathrm{X}$ points contribute as $(\delta_\mathrm{X})^2$"，给出 $(-1)^\nu=\delta_\Gamma\delta_\mathrm{M}$；表 7.2 与图 7.6 的路径标签只用 $\Gamma$、M、X。
- 本章印码 148（763–764 行）自己警告：归约需要"计算结构的对称性与一致的反演中心；仅出现高对称路径不足以确立被略去乘积的相等"。

**问题**

若第 7 章的 M 指角点、两个 X 是边心点，则两章自洽，但第 7 章未说明；若体系确有 C4 使 $\delta_\mathrm{X}=\delta_\mathrm{Y}$，则图 4.2(b) 相当于替读者默认了该对称性，本章关于"必须先保留四个因子再检查其关系"的要求落空。此外图中没有给出使两点等价的具体对称操作。

**建议**

1. 在第 7 章写明 X、M 分别对应哪个 TRIM，并给出"两点宇称乘积相等"的对称操作依据。
2. 或改图 4.2(b)：画成一般矩形/斜方 BZ，不给 C4，两个边心点分别标注，使两章命名与图形一致。

### P3 引文过薄（20 页 5 篇）

**证据**（`grep -o "\\\\cite{[^}]*}" src/fundamentals_c.tex`：7 处 `\cite`，5 个键）

| 键 | 章内位置 | 其他章 | 书目编号 |
| --- | --- | --- | --- |
| `fu2007topological` | 87、694 行 | 第 1、7 章 | [36] |
| `berry1984quantal` | 294 行 | 仅本章 | [144] |
| `wilczek1984appearance` | 397 行 | 仅本章 | [145] |
| `kane2005z2` | 645、669 行 | 仅本章 | [146] |
| `gao2021irvsp` | 808 行 | 第 7 章 | [147] |

**问题**

1. 印码 147（671–674 行）"奇数个 Kramers 对边缘态"这段全章最关键的物理结论**无引文**。
2. 式 (4.30) 的识别引 `fu2007topological`（PRB 76, 045302 (2007)，三维推广）；二维情形宜另引 Fu–Kane PRB 74, 195312 (2006) 或 Kane–Mele PRL 95, 146802 (2005)（后者已在 bib，仅用于 §4.4.1）。
3. §4.4.3 两处"对称性使宇称乘积相等"（744–746、757–759 行）无引文。
4. §4.1.2"有间隔 ⇒ 谱投影算符可光滑变化"（183–185 行）无引文。
5. 全篇 bib 缺少 Bernevig–Hughes–Zhang (Science 314, 1757)、Hasan–Kane (RMP 82, 3045)、Zak (PRL 62, 2747) 等基本文献。

**建议**：补齐上述 1–4 的引文，并按需补 2–3 篇综述；`gao2021irvsp` 与第 7 章共用，注意两处描述一致。

### P4 多带子空间的指标只讲到联络

**证据**：§4.2.3（397–417 行）在给出 (4.17) 后直接转向"本文用反演对称从宇称本征值定 $Z_2$"（415–416 行）。全章无重叠矩阵、无 $\det\prod$、无 Wilson loop、无 Wannier 电荷中心（`grep` 无 "Wilson"、"Wannier"、"det"、"Tr"）；也无 Berry 曲率与 Chern 数（无 "Chern"、"curvature"）。

**问题**：读者看不到 §4.2 与 §4.4 之间缺的那一环——子空间的不变量是什么、$\prod_i\delta_i$ 为何就是它。同时因缺少曲率，无法说明"时间反演下 $\Omega(-\vec k)=-\Omega(\vec k)$ ⇒ $C=0$ ⇒ 自旋系统剩下 $Z_2$ 而非 $Z$"，§4.4.1 的"两类"显得是凭空给出。

**建议**：在 (4.17) 后补一小段（可只给结论式）：重叠矩阵 $M^{(j)}_{mn}=\langle u_{m,\vec k_j}|u_{n,\vec k_{j+1}}\rangle$、子空间 Berry 相 $\gamma_\mathrm{sub}=-\mathrm{Im}\ln\det\prod_j M^{(j)}$、以及 Wilson loop 本征值即 Wannier 电荷中心；并补 Berry 曲率 $\Omega_n=\nabla_{\vec k}\times\vec{\mathcal A}_n$ 与 $C=\frac{1}{2\pi}\int_\mathrm{BZ}\Omega$ 的一句。可引 Yu–Qi–Bernevig–Fang PRB 84, 075119；Soluyanov–Vanderbilt PRB 83, 235401。

### P5 单带 Berry 相在简并时未定义（一句可补）

**证据**：§4.2.1（264 行）限定"单条沿路径非简并的带"；§4.2.3（374–376、415 行）转向子空间，但从未明说简并时单带 Berry 相没有定义。

**建议**：在 (4.17) 前补："若该带与其他带简并，单带 Berry 相没有定义，只有多带（Wilson loop）量才是规范不变的。"

### P6 图 4.1(d) 的 $E_{2N_\mathrm{p}-2,\vec k}$ 标注与"按能量升序"定义冲突

**证据**：印码 134（`src/fundamentals_c.tex` 133 行）"We order the band energies increasingly, counting each spinor state once"；正文（223–224 行）"In (d), the dashed blue curve represents $E_{2N_\mathrm{p}-2,\vec k}$ for $N_\mathrm{p}\ge2$"；图 4.1(d) 中该虚线与 $E_{2N_\mathrm{p},\vec k}$ **相交**；正文（245–247 行）"The two pairs exchange their order in energy"。

**问题**：按定义排序后恒有 $E_{2N_\mathrm{p}-2,\vec k}\le E_{2N_\mathrm{p},\vec k}$，只能相切不能交叉。另：图例把 (c) 的带间接触与 (d) 的子空间内部交叉共用同一个 "Contact" 橙圈标记，而正文明确区分这两件事。

**建议**：把 (d) 的曲线说明改为"虚线是较低那对的绝热延续；按能量排序的标号 $E_{2N_\mathrm{p}-2}$ 与 $E_{2N_\mathrm{p}}$ 在交叉处互换，排序后的本征值只相切"；并在图例中用不同标记区分 contact 与 internal crossing。

### P7 其余表述与细节

| 位置 | 问题 | 建议 |
| --- | --- | --- |
| §4.3.1（488–489 行） | "we use a full Bloch state $\ket\psi$, so equivalent crystal momenta belong to the same translation sector" 含糊 | 改为：在 TRIM $\Lambda$ 处 $\hat\Theta$ 把 Bloch 态映到 $-\Lambda\equiv\Lambda\ (\mathrm{mod}\ \vec G)$，因此仍在同一 $\vec k$ 扇区 |
| §4.4 引言（649–650 行） | "If inversion is removed while time reversal and the band separation are preserved, the index remains unchanged" 预设了保间隔连通路径存在 | 改为：$\nu$ 只由"有间隔的子空间 + 时间反演"定义，任何同时保持两者的连续形变不能改变它；反演只是计算捷径 |
| §4.5.1（806–812 行） | (4.27) 的 $\xi_n$ 是**完整 Bloch 态**的本征值，而 §4.5 要的是"旋量态的对称表示"/irvsp 输出 | 补一句 TRIM 处晶胞周期部分的宇称关系（含 $e^{\mathrm{i}\vec G\cdot\vec r}$ 相位；平面波系数 $C_n(\vec G)\to\xi_nC_n(-\vec G-2\vec\Lambda)$），否则读者接不上 |
| §4.3.1 与 (4.29)（511–514、681–692 行） | Kramers 配对只对 $\ket\psi$ 证明，却用在 (4.5) 的晶胞周期基上；未给出 $E_n(\vec k)=E_{n+1}(-\vec k)$ | 补：TRIM 处同一配对对 $\ket{u_{n\Lambda}}$ 也成立；并写出能带形式的配对关系 |
| 符号 | 恒等算符 $\hat I$（452、462、482 行）与反演算符 $\hat{\mathcal I}$（571、587、597 行）同形 | 恒等改用 $\mathbb{1}$ |
| (4.10) 前（266 行） | 该式预设了 $\ket{u_{n\vec k}}$ 随 $\vec k$ 光滑变化的规范 | 补"在使 $\ket{u_{n\vec k}}$ 随 $\vec k$ 光滑变化的规范下" |
| (4.14) 后（367 行） | "changing the hamiltonian or the loop can change that result continuously"，而 $\gamma$ 定义在 mod $2\pi$ | 改为 $e^{\mathrm{i}\gamma_n(C)}$ 连续变化 |
| 术语（82–86、520 行） | $\vec k$ 一处称 "crystal wave vector"、一处称 "crystal momentum"（动量应为 $\hbar\vec k$） | 统一为 wave vector |
| 图 4.2(b) | 倒格基矢 $\vec b_1$ 画成向下，(a) 中向右 | 统一方向 |
| 图 4.2(a) | 四个 M 点用四种颜色（青/橙/紫/紫），而青色在 (b) 中表示 $\Gamma$ 的周期副本 | 颜色按 TRIM 类别（$\Gamma$ / M）编码 |
| 图 4.1 图注（219–229 行） | 只说明 (d) 的"coincident partners"，未说明每条支线代表每个 Kramers 对的一个成员 | 图注补一句 |
| (4.29) 说明（689–692 行） | 原文 "the indices $(2m-1,2m)$ label the members of a Kramers pair, **chosen** so that both states have the same parity"——措辞把配对说成人为选择；配对实际由 $\hat\Theta$ 决定，同一 TRIM 处若两个不同 Kramers 对相互简并，仅靠能量排序无法确定配对 | 改为"$(2m-1,2m)$ 指由时间反演确定的 $\hat\Theta$ 配对；两态等宇称由 (4.28) 给出" |
| §4.4.2（721 行） | "It is not obtained by counting degeneracies alone" 已诚实，但未给出任何推导或指路 | 至少给出 sewing matrix / Pfaffian 形式的出处（Fu–Kane PRB 74, 195312 (2006) 第 II 节；PRB 76, 045302 (2007)） |

### P8 版面

| 项 | 证据 | 建议 |
| --- | --- | --- |
| 章首页落在偶数页 | 第 4 章起于印码 131（物理页 166，左页）；第 1、2、3、5、6、7 章均起于奇数页 | `thesis.tex` 第 370 行 `\input{src/fundamentals_c.tex}` 之前缺 `\cleardoublepage`（第 365、367、369 行分别给 `fundamentals_a`、`fundamentals_b`、以及紧随其后的第 371 行都写了，唯独第 370 行前没有）。补上后其后各章印码 +1，仍全部落在奇数页 |
| 三处半空页 | 印码 140 仅 4 行正文；印码 145 仅用约 1/3 页；印码 150 空白过半。对应 `src/fundamentals_c.tex` 419、638、768 行的 `\newpage` | 该体例与第 2、3 章一致（第 2 章 6 处、第 3 章 4 处），但本章内容量最薄。建议删去 §4.4 前（638 行）一处，或把图 4.1、4.2 上移补版面 |
| 无本章小结 | 第 2、3 章同样没有 Summary 节 | 不算破例，不必新增 |
| 章末收束偏虚 | 839–844 行把"具体材料的能带选择、带隙证据和宇称本征值"全部推给研究章，而第 7 章并未兑现（见 P1） | 与 P1 一并处理 |
| 符号表缺项 | `src/font_matter.tex` 163–172 行只收 6 项：$Z_2$、$\Lambda_i$、$N_\mathrm{occ}$、$\xi_{2m}$、$\delta_i$、$\nu$。本章新引入的 $\vec{\mathcal A}_n(\vec k)$（4.12）、$\gamma_n(C)$（4.14）、$\hat{\mathcal P}(\vec k)$（4.5）、$N_\mathrm{p}$（4.29）、$\Delta_\mathrm{dir}/\Delta_\mathrm{dir}^{\min}/\Delta_\mathrm{ind}$（4.7–4.8）、$\hat\Theta$、$\hat{\mathcal I}$、$\xi_n$、$\ket{u_{n\vec k}}$ 均未列入 | 补齐；另缩略语表（78–109 行）无 TRIM 与 SOC，而 TRIM 是本章明确定义的缩写 |
| $\xi_{2m}$ 释义 | `font_matter.tex` 169 行写作"第 m 个**占据** Kramers 对的宇称本征值"，正是 §4.5.2 警告过的说法；第 7 章（557–565 行）写作"one state in the $m$th Kramers pair" | 改为"从每对 Kramers 对中取一个代表态的宇称本征值"，三处措辞统一 |

---

## 3. 由本章插入引发、但不在本章文件内的问题

1. **1.5 节 "Thesis organisation" 没有第 4 章**（`src/introduction.tex` 319–341 行），依次为 Ch2 → Ch3 → Ch5 → Ch6 → Ch7 → Ch8；而 1.3.1 节（261 行）明确写 "Chapter~\ref{cha:fundamentals_b} develops the dielectric response…"，1.3.2 节（264–279 行）却未指出拓扑框架在第 4 章展开。建议各补一句。
2. **已发表章号错位**：`src/publications.tex` 15/22/29 行与 `src/appendix.tex` 10/15/20 行仍把三篇论文写成 "Chapter 4/5/6"，现在应为 **5/6/7**。该错位在 `.output/thesis.pdf` 正文可见（List of Publications 与 Appendix 页），旧版即已存在，插入新章后更加明显。
3. **第 7 章不回引第 4 章**（`grep -n "cha:fundamentals_c" src/*.tex` 全篇仅 `fundamentals_a.tex` 3171 行一处）。第 7 章 §7.4.5 对光学量明确写了"defined in chapter 3, especially sections 3.2 and 3.4"，§7.4.4 对拓扑部分却无对应引用，建议在 §7.4.4 指向本章 §4.1.2 与 §4.4.2。
4. **`\nameref` 标题错误**：`.output/thesis.aux` 中 `\newlabel{cha:fundamentals_c}{{4}{131}{Energy-loss spectrum}{chapter.4}{}}`，即 nameref 标题继承上一章末节。同类问题也见于 `cha:fundamentals_a`、`cha:fundamentals_b` 等。目前无害（全篇未使用 `\secrefT`/`\nameref`），但若以后启用会打错章名。
5. **图文件命名撞号**：`figures_ch3/` 内仍有 `4.1_absorption.pdf` … `4.5_energy-loss.pdf`（光学章曾为第 4 章时的编号），与 `figures_ch4/4.1_…`、`4.2_…` 撞号。LaTeX 路径无歧义，仅不自解释。
6. **篇幅**：第 2+3+4 章现占印码 15–150 共 136 页 / 316 页（43%）。前次审查意见中"Ch2+Ch3 约 100 页过长"的整改记录（`reports/reply_to_examiners.md` 21 行）仍是未填的占位符 "by x pages"，新增 20 页第 4 章会使该条更显眼；建议在答复中说明第 4 章承担了把散落于绪论的拓扑框架集中、避免在各研究章重复的作用。

---

## 4. 建议的修改顺序

1. 第 7 章补 $2N_\mathrm{p}$ 与 $\Delta_\mathrm{dir}$ 证据，并按本章措辞限定摘要/结论的拓扑表述（P1）。
2. 统一 X/Y 与 M 的 TRIM 命名，并在第 7 章给出两点宇称乘积相等的对称性依据（P2）。
3. 补引文：边缘态那句、$\prod_i\delta_i$ 的识别、§4.4.3 的对称性归约、§4.1.2 的光滑投影算符（P3）。
4. 在 §4.2.3 与 §4.4 之间补 Wilson loop / 曲率一段（P4），以及单带简并时 Berry 相未定义一句（P5）。
5. 修图 4.1(d) 标注与图例、图 4.2 配色与基矢方向（P6、P7 中图谱部分）。
6. 版面：`thesis.tex` 补 `\cleardoublepage`；处理三处半空页；补符号表与缩略语（P8）。
7. 清理插入引发的连带问题：1.5 节补第 4 章、publications/appendix 章号改为 5/6/7、第 7 章回引第 4 章（第 3 节）。

---

## 5. 本次核验的锚点（便于复核）

- 编译版本：`.output/thesis.pdf`（316 页，印码 131–150 为第 4 章，物理页 165–184；偏移 +34）；对照 `.output/thesis_202608.pdf`（312 页，旧第 4 章印码 133–150，偏移 +30）。
- 提取命令：`pdftotext -layout .output/thesis.pdf /tmp/thesis_new.txt`；`pdftotext -layout .output/thesis_202608.pdf /tmp/thesis_old.txt`；章节范围 `pdftotext -layout -f 165 -l 184 .output/thesis.pdf -`。
- 图件核验：`pdftoppm -f 170 -l 170 -r 300 -png .output/thesis.pdf`（图 4.1，印码 136）、`pdftoppm -f 177 -l 177 -r 300 -png .output/thesis.pdf`（图 4.2，印码 143）。
- 引文与编号：`.output/thesis.bbl` 条目顺序给出 [36] `fu2007topological`、[144] `berry1984quantal`、[145] `wilczek1984appearance`、[146] `kane2005z2`、[147] `gao2021irvsp`。
- 日志：`.output/thesis.log` 无 undefined reference / multiply defined label；`Overfull` 共 10 处，均不在第 4 章范围。
- 工作笔记（本章写作时留下，可供对照）：`figures_ch4/topology_parity_draft_0922.md`（英文稿，其中 "square-trilayer beryllene" 的 $(-1)^\nu=\delta_\Gamma\delta_M\delta_X^2=\delta_\Gamma\delta_M$ 即 P2 的来源）、`figures_ch4/ch4_draft_inChinese.md`（中文通读稿，与当前 tex 同步）、`.agents/ai_ch4_draft.md`（草稿说明）。

本报告未修改任何论文文件。
