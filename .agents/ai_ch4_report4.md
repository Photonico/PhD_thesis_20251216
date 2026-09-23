# Chapter 4 修订达成度分析

日期：2026-09-23。
问题：新版 Chapter 4 是否达成其修订目标？
对照：`.output/thesis.pdf`（316 页，新）vs `.output/thesis_202608.pdf`（312 页，旧）；源文件 `src/fundamentals_c.tex`、`src/fundamentals_a.tex`。
方法：先以文本差异确定改动的真实范围，再对照目标集合逐条判定。
本报告不修改任何论文文件。

## 0. 结论

1. **本轮修订不是"扩写第 4 章"，而是"把拓扑内容从第 2 章迁出、并在第 4 章补上前置链"。** 旧版第 2 章有 §2.6.6 "Spin-orbit coupling and band topology"（含式 2.284–2.286）；新版该小节**整节删除**，其内容并入第 4 章。净效果是第 4 章 18 → 20 页、第 2 章去掉约 2 页，同时第 4 章新增 4 页（迁移 2 页 + 净新增 2 页）。
2. **结构目标基本达成**：拓扑内容从"第 2 章末尾的概述 + 第 4 章的展开"这种分散状态，收敛为第 4 章一处完整推导；除一处有意的前向指引外，旧文没有残留、没有重复定义（已逐句核验）。
3. **前置链目标达成**：旋量、collinear 与 SOC 的关系、周期规范、Kramers 配对、投影算符作用均已补齐，"旋量态"不再无定义即使用。
4. **两个核心目标只部分达成**：物理后果只到"奇数个 Kramers 对边缘态"一句，没有说明"为什么重要"（无 helical / 无背散射抑制）；金属性前提在第 4 章建立了判据，但**该判据从未被使用**，第 7 章的论断也未加限定。
5. **修订引入了一处新的实质损失**：旧第 2 章那句最贴题的警告——"A non-trivial product alone does not establish a topological insulator"——在新版全文中**已不存在**（`grep` 零命中）。
6. 上一轮报告（`.agents/ai_ch4_report.md`）的 P1–P8 中，P1（第 7 章未执行前提）、P2（X/Y 命名）、P3（引文）、P4（Wilson loop/曲率）、P8（版面、符号表）**在本轮修订中均未处理**，因为本轮改动范围只在迁移与前置链。

---

## 1. 本轮改动的真实范围（证据）

### 1.1 从第 2 章删除的内容

`src/fundamentals_a.tex` 旧 §2.6.6（旧印码 98–99，旧 PDF 行 5142 起）包含：

| 旧编号 | 内容 | 旧文原话（关键句） |
| --- | --- | --- |
| (2.284) | 旋量电子态 $\ket{\psi_{n\vec k}}=\ket{\psi_{n\vec k,\uparrow}}\otimes\ket{\uparrow}+\ket{\psi_{n\vec k,\downarrow}}\otimes\ket{\downarrow}$，$\hat h_\mathrm{KS}^\mathrm{SOC}\ket{\psi_{n\vec k}}=E_{n\vec k}\ket{\psi_{n\vec k}}$ | — |
| (2.285) | 子空间直接间隔条件 $E_{2N_\mathrm{p}+1,\vec k}-E_{2N_\mathrm{p},\vec k}>0,\ \vec k\in\mathrm{BZ}$ | "This is a **direct-gap condition throughout the Brillouin zone**. **It cannot be established only from the time-reversal invariant momenta or from the plotted high-symmetry path.** It also does not exclude an indirect overlap between energies at different k points. Therefore, an isolated band subspace can exist without an insulating state at the Fermi level." |
| (2.286) | Fu–Kane 乘积 $\delta_i=\prod_{m=1}^{N_\mathrm{p}}\xi_{2m}(\Lambda_i)$、$(-1)^\nu=\prod_{i=1}^{4}\delta_i$ | "For an insulator whose occupied bands form this subspace, $2N_\mathrm{p}=N_\mathrm{occ}$. Equation (2.286) then has the same counting as equations (7.3) and (7.4) in chapter 7. **For the metallic beryllene systems, the chosen subspace and the separation in equation (2.285) must be checked before interpreting the parity product. A non-trivial product alone does not establish a topological insulator.**" |

同处的收束句为："…connected the electronic ground-state framework to structural, vibrational, magnetic, superconducting, **and topological** calculations."

### 1.2 在新第 4 章新增的内容

以 `diff` 定位（旧→新，剔除分页噪声后），新增集中在两处：

| 新位置 | 新增内容 |
| --- | --- |
| §4.1.1（新印码 132–133） | 旋量段：回到 Kohn–Sham 方程 (2.234)、指明 "the collinear treatment of subsection 2.6.4"、式 (4.2) 旋量、式 (4.3) 周期规范 $\ket{\psi_{n,\vec k+\vec G}}=\ket{\psi_{n\vec k}}$、$\ket{u_{n,\vec k+\vec G}}=e^{-\mathrm{i}\vec G\cdot\hat{\vec r}}\ket{u_{n\vec k}}$ 及其推导说明（引 [36]）。旧版第 4 章**完全没有**旋量与周期规范，直接从 (4.1) 跳到"本征值给出色散"。 |
| §4.1.2（新印码 134） | 式 (4.6) 投影算符作用 $\hat{\mathcal P}(\vec k)\ket{v_{\vec k}}=\sum_n\ket{u_{n\vec k}}\braket{u_{n\vec k}\|v_{\vec k}}$、幂等性 $\hat{\mathcal P}^2=\hat{\mathcal P}$、以及"子空间内交叉不影响可光滑性"。旧版只有"rank $2N_\mathrm{p}$ is fixed"一句。 |
| §4.1.2（新印码 134） | "We will establish this pairing in section 4.3."（对 $N_\mathrm{p}$ 的前向指引） |
| §4.2.3（新印码 140） | "We will establish this pairing…"以外的措辞调整与交叉引用更新（旧引 (4.3)(4.8)(4.9) → 新引 (4.5)(4.12)(4.13)） |

`grep -c "spinor\|Kramers"`：旧第 2 章有，新第 2 章为 0；`spinor`/`Kramers` 已全部只在第 4 章出现。

### 1.3 迁移完整性的核验

- 旧 §2.6.6 特征句在新版全文的命中数：`"direct-gap condition throughout"` = 0、`"It cannot be established"` = 0、`"A non-trivial product alone"` = 0（旧版各 1）。**即：旧文没有残留，没有重复定义；但同一批句子里的三条警告也一并消失，新第 4 章没有等价表述。**
- 第 2 章新增了一条前向指引（`src/fundamentals_a.tex` 3171–3172 行，位于 §2.6 导语）："Spin-orbit coupling and band topology are developed in chapter~\ref{cha:fundamentals_c}, where we examine the symmetry and connection of the electronic states." 这是全篇唯一指向第 4 章的引用。
- 第 2 章收束句改为："…connected the electronic ground-state framework to structural, vibrational, magnetic, and superconducting calculations."——**"and topological" 被删去**，章末不再提示拓扑内容已在第 4 章。

---

## 2. 目标集合

综合四处来源，本轮修订应达成的目标为：

| 编号 | 目标 | 来源 |
| --- | --- | --- |
| G1 | 把散在绪论与第 2 章的拓扑内容集中到第 4 章，形成完整、可独立阅读的框架 | `.agents/ai_ch4_draft.md` 第 11–29 行；`intro` 1.3.2 节 |
| G2 | 拓扑不该"突兀引入"：先说明其物理意义与非平庸 $Z_2$ 的后果，再给 Fu–Kane 公式 | `reports/report_merge.md` 127–131 行（审查意见 20） |
| G3 | 处理 $Z_2$ 与金属性的冲突：要么验证全 BZ 的直接间隔，要么说明该指标刻画的是子空间 | `reports/report_merge.md` 325–327、554–557 行（审查意见 21） |
| G4 | 为第 7 章的宇称分析备齐前置：旋量、Kramers 配对、TRIM、宇称本征值 | `.agents/ai_ch4_draft.md` 46–54 行（自审清单） |
| G5 | 保持与第 1–3 章相同的讲解方式、符号与体例；不重复、不留残文 | 第 2、3 章既有惯例 |
| G6 | 本轮自审自述的四项已核实点（单带 Berry 相限制、完整 Bloch 态证明、时间反演保护与反演提供判据的分工、新增三条文献） | `.agents/ai_ch4_draft.md` 46–54 行 |

---

## 3. 逐目标判定

### G1 内容集中化 —— **达成**（但整合未完成）

- 第 4 章现在自成体系：4.1 子空间与隔离条件 → 4.2 相位自由与 Berry 相 → 4.3 时间反演与反演 → 4.4 $Z_2$ 与 Fu–Kane → 4.5 到计算。旧版分散在"第 2 章 §2.6.6（结论式）+ 第 4 章（推导式）"的两处陈述已合并为一处。
- 副作用已核验：无重复定义、无残文、跨章引用全部解析（`.output/thesis.log` 无 undefined reference）。
- **未完成的部分**：
  - `src/introduction.tex` 1.3.2 节（264–279 行）仍只引 [36] 说明"物理意义"，未指出框架在第 4 章展开；对照 1.3.1 节（261 行）明确写了 "Chapter~\ref{cha:fundamentals_b} develops the dielectric response…"。**两节的处理方式不对称。**
  - 1.5 节 "Thesis organisation"（319–341 行）**根本没有第 4 章**，依次是 Ch2 → Ch3 → Ch5 → Ch6 → Ch7 → Ch8。
  - 第 2 章章末不再提拓扑（见 1.3 节第三条），而第 2 章导语的新句子位于 §2.6 之下、并不在章首 roadmap 中。

**判定**：内容确实集中了，但读者从目录与第 1 章看不到这件事。

### G2 先讲物理意义、再给公式 —— **部分达成**

- **位置达成**：第 4 章确实把后果句放在 Fu–Kane 之前——§4.4.1（印码 146）先说"与平庸绝缘体界面上的奇数个 Kramers 对边缘模式"，§4.4.2（印码 147）才给宇称乘积。审查意见要求的**顺序**满足。
- **内容未达成**：`grep -c "helical\|dissipationless\|backscatter" src/fundamentals_c.tex` = **0**。全篇"helical edge states"只出现在 `src/introduction.tex` 270 行一次。第 4 章没有说明这些边缘模"为什么重要"——即无能隙、自旋-动量锁定、背散射被抑制、耗散less 输运这一层。审查意见的原文是 "explain why topology is significant **and what physical consequences follow** from a non-trivial Z2 invariant (**such as dissipationless helical edge states**)"，本轮只满足了"位置"，没有满足"内容"。
- 另外，旧第 2 章 §2.6.6 也从未写过这些词，所以这不是迁移造成的退化，而是 G2 从一开始就只被部分实现。

**判定**：顺序对，实质说明缺。

### G3 金属性与 $Z_2$ —— **未达成，且本轮出现了反向损失**

- **判据一侧做得好**：第 4 章建立了完整判据，且旧第 2 章那两条警告的**精神**被重写进新文本——印码 149："For a metal, the number of states below $E_\mathrm{F}$ can change with $\vec k$, so the phrase ``occupied bands'' alone does not identify the subspace. Numerical smearing of the occupations also does not define a fixed-rank projector."；印码 150："The Fermi-level condition determines whether this classification describes an insulating phase."
- **但三处关键内容丢失或未做**：
  1. 旧 (2.285) 后那句 **"It cannot be established only from the time-reversal invariant momenta or from the plotted high-symmetry path."** 在新版**没有任何等价表述**。这句是判据的操作性要点（不能靠 TRIM 或高对称路径交差）。
  2. 旧 (2.286) 后那句 **"For the metallic beryllene systems, the chosen subspace and the separation in equation (2.285) must be checked before interpreting the parity product. A non-trivial product alone does not establish a topological insulator."** 已从全文消失（`grep` 零命中）。新第 4 章只保留通用形式（"若所选与被排除能带接触…"），并把具体应用推给研究章；而研究章并未做。**换言之：这条修订正是为了处理审查意见 21 而写的，却在迁移中把最贴题的那句话删掉了。**
  3. 第 7 章 §7.4.4 仍然写 "the parity eigenvalues of **the occupied** spin-orbit-coupled states"，全文仍无 $\Delta_\mathrm{dir}(\vec k)$、无 $2N_\mathrm{p}$、无二维 BZ 加密证据。
- 连带：本轮修订对摘要、结论、符号表（`src/font_matter.tex` 168–171 行仍用 "occupied" 措辞）均未触碰。

**判定**：**未达成**。判据比旧版更完整，但判据的针对性警告被删除，主张一侧完全未动——净效果是"要求更严、提醒更少、主张照旧"。

### G4 为第 7 章备齐前置 —— **达成**

- 迁移后，(旧 2.284)→(新 4.2) 旋量、collinear 处理与 SOC 的关系、Kramers 配对 (§4.3.1)、TRIM (§4.3.2)、宇称 (§4.3.3) 与 $Z_2$ (§4.4) 连续成篇，且第 7 章 §7.4.4 的式 (7.3)(7.4) 与第 4 章 (4.29)(4.30) 的确同构（第 4 章印码 149 自己给出了这个等式关系）。
- 新增的 §4.1.1 旋量段还**修掉了旧版的一个隐含引用错位**：旧 §2.6.6 在尚未定义 TRIM 时就使用了"the time-reversal invariant momenta"；现在 TRIM 在 §4.3.2 才出现，术语顺序正确。
- 同期新增的周期规范 (4.3) 也是 §4.2.2 "闭环跨 BZ 边界"和 §4.4.3 的必要工具，旧版缺失。

**判定**：**达成**，这是本轮修订最实的一项。

### G5 体例与集成 —— **部分达成**

- 体例一致：章首过渡句与 roadmap、每节 `% opening paragraph`、`here,` 小写、`\vec`/`\mathrm{i}`/`\dif`/`\coloneqq`、英式拼写、句首大写规则、`\texorpdfstring{$Z_2$}{Z2}` 均与第 2、3 章一致。
- 集成未完成：1.5 节无第 4 章（G1 已列）；`src/publications.tex` 15/22/29 行与 `src/appendix.tex` 10/15/20 行的 "Chapter 4/5/6" 应为 **5/6/7**（该错位旧版即存在，本轮未清理）。
- 版面未处理：第 4 章仍起于偶数页 131（`thesis.tex` 370 行前缺 `\cleardoublepage`），印码 140、145 两处半空页仍在。
- 删除 §2.6.6 后，第 2 章的收束句不再提拓扑（1.3 节第三条）。

**判定**：章内体例合格，章外集成遗留。

### G6 自审自述的四项 —— **全部达成**

| 自审声明（`ai_ch4_draft.md`） | 核验结果 |
| --- | --- |
| "单带 Berry phase 明确限制在非简并的引入情形；实际简并态使用整个子空间" | 达成：§4.2.1 开头限定"非简并的单带"，§4.2.3 转入子空间。**但仍未明说"简并时单带 Berry 相没有定义"**，属可补一句 |
| "Kramers 正交性证明采用完整 Bloch 态，避免在非零 TRIM 上遗漏 cell-periodic 态的倒格矢变换" | 达成且文本显式说明了理由（印码 142："so equivalent crystal momenta belong to the same translation sector"）。措辞可再精确（见上一轮报告 P7） |
| "明确时间反演保护此 Z2 分类，反演提供宇称判据这一计算途径" | 达成：印码 146 明写 "Time reversal is the symmetry that protects this $Z_2$ classification; inversion supplies the simpler route for evaluating it." |
| "新增三个已核实的文献条目：Berry 1984、Kane--Mele 2005、Wilczek--Zee 1984" | 达成：[144][145][146] 均在参考文献中，条目信息正确，且仅在第 4 章被引用 |

---

## 4. 本轮修订新引入的问题

| 编号 | 问题 | 证据 |
| --- | --- | --- |
| N1 | 删除旧 (2.285) 后的操作性警告后，**无等价表述** | 见 G3 第 1 点；`grep` 零命中 |
| N2 | 删除旧 (2.286) 后那句最贴题的结论性警告后，**全文再无该表述** | 见 G3 第 2 点；这正是第 7 章现在最需要的一句 |
| N3 | 第 2 章章末收束句删去 "and topological"，且 §2.6 导语的新指引位于小节之下 | `src/fundamentals_a.tex` 3171–3172 行；新第 2 章末段 |
| N4 | 第 4 章仍无 $Z_2$ 物理后果的实质说明（G2） | `grep -c "helical\|dissipationless\|backscatter"` = 0 |
| N5 | 第 7 章赖以成立的 $\delta_\mathrm{X}$ 两点等价前提，在第 4 章与第 7 章**都没有**给出对称性依据 | 第 4 章印码 148 只给条件式；第 7 章 586–589 行直接使用 |
| N6 | 第 4 章仍缺"真正计算该指标的工具链"（重叠矩阵、$\det\prod$、Wilson loop、Wannier 中心、Berry 曲率） | `grep` 无 "Wilson"、"Wannier"、"Chern"、"curvature" |

---

## 5. 建议的下一步

**按"投入产出比"排序**（前三项直接决定修订是否算完成）：

1. **把删掉的那两句搬回来**（N1、N2）。第 4 章印码 149 的第二段是天然位置，恢复等价表述即可：
   - "该条件不能仅由时间反演不变动量或所画的高对称路径确立。"
   - "对于本文的金属体系，必须先检查所选子空间与其间隔，再解释宇称乘积；仅凭非平庸的乘积不足以确立拓扑绝缘体。"
2. **完成判据 → 主张的闭环**（G3）：第 7 章 §7.4.4 补 $2N_\mathrm{p}$ 与 $\Delta_\mathrm{dir}(\vec k)$ 证据（金属体系需在接触点附近加密），摘要与结论按第 4 章措辞加金属性限定。
3. **补第 4 章的物理后果一段**（G2、N4）：给出"无能隙、自旋-动量锁定、背散射被抑制"的说明，并引 Kane–Mele [146]；这同时把审查意见 20 真正结清。
4. **恢复章级集成**（G1、G5）：1.5 节补第 4 章一句；`publications.tex` 与 `appendix.tex` 章号改为 5/6/7；第 2 章导语的指引可上移到章首 roadmap 或保留现状并在 1.5 节体现。
5. **补对称性依据与工具链**（N5、N6）：第 4 章 §4.4.3 给出 $\delta_\mathrm{X}$ 两点相等的对称操作；§4.2.3 与 §4.4 之间补 Wilson loop / 曲率一段（可只给结论式）。
6. **版面**（G5）：`thesis.tex` 370 行前补 `\cleardoublepage`；处理印码 140、145 的半空页；符号表补 $N_\mathrm{p}$、$\vec{\mathcal A}_n$、$\gamma_n$、$\hat{\mathcal P}$、$\Delta_\mathrm{dir}/\Delta_\mathrm{ind}$、$\hat\Theta$、$\hat{\mathcal I}$，并把 "occupied" 措辞按第 4 章 §4.5.2 的立场改写。

---

## 6. 复核锚点

- 差异定位：`diff <(pdftotext -layout .output/thesis_202608.pdf -) <(pdftotext -layout .output/thesis.pdf -)`；第 4 章范围新印码 131–150（物理页 165–184，偏移 +34），旧印码 133–150（偏移 +30）。
- 旧 §2.6.6 原文：`sed -n '/^2.6.6 Spin-orbit coupling and band topology/,/^Chapter 3/p' /tmp/thesis_old.txt`（旧 PDF 行 5142 起；式 2.284–2.286）。
- 迁移完整性：`grep -c "direct-gap condition throughout\|It cannot be established\|A non-trivial product alone" /tmp/thesis_new.txt` 全为 0；`grep -c "spinor\|Kramers" src/fundamentals_a.tex` 为 0。
- 前向指引唯一来源：`grep -rn "cha:fundamentals_c" src/` → 仅 `src/fundamentals_a.tex:3171`。
- 第 4 章目录与印码：`.output/thesis.toc` 71–89 行；`.output/thesis.aux` 中 `\newlabel{cha:fundamentals_c}{{4}{131}…}`。
- 第 7 章对应文本：`src/project_3_main.tex` 536–649 行（§7.4.4 与表 7.2）。
- 上一轮问题清单：`.agents/ai_ch4_report.md`（P1–P8，本轮均未处理）。

本报告未修改任何论文文件。
