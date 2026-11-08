# 论文待办清单

完善论文用的待办清单, 配合同目录下的 `SKILL.md` 使用. 规则和改法见 `SKILL.md`, 这里只列具体位置.
行号以 2026-11-09 的版本为准, 行号变动后按引文搜索. 完成一条, 就把 `[ ]` 改为 `[x]`.

1. 内容一致性 (P0)
2. 非母语用法
3. 防御性句子
4. 重复与篇幅 (P1)
5. 排版与记号 (P2)

## 1. 内容一致性 (P0)

这些问题会让读者质疑结论, 应最先处理. 有几组防御句的根源就在这里, 问题解决后可以一并删除.

- [ ] [abstract.tex:19](../../../src/abstract.tex#L19) 摘要说 Graphene-\ce{B4C3} "possibly chiral optical behaviour", 第 5 章却说非对角元不能证明旋光性. 删去 chiral.
- [ ] [abstract.tex:39](../../../src/abstract.tex#L39) 摘要说 "identify non-trivial $\mathbb{Z}_2$ topology", 没有交代第 7 章的条件: 隔离能隙约 1 meV, 位于费米能以上, 体系是金属. 补上限定, 与第 7 章一致.
- [ ] [project_3_main.tex:34](../../../src/project_3_main.tex#L34) 和 [project_3_main.tex:1273](../../../src/project_3_main.tex#L1273): "combines metallicity, tunable optical properties, and non-trivial topology" 偏强, 与条件性的结论不符.
- [ ] 第 5 章的非对角介电元: 核实 (对称化, 与 VASP 输出的 6 个分量对照), 或删去相关讨论和面板. 解决后删除对应的防御句: project_1_main.tex 第 557, 558, 618, 620, 621, 744 行, project_1_SI.tex 第 274, 280, 282, 304, 317 行, conclusion.tex 第 201 行.
- [ ] [project_2_main.tex:706](../../../src/project_2_main.tex#L706) Migdal--Eliashberg 的 $T_c$: 存档数据没有越过 $T_c$. 补算跨过能隙闭合的温度点, 或改为区间表述. 解决后处理第 710, 711 行和 conclusion.tex 第 66 行.
- [ ] [project_2_main.tex:467](../../../src/project_2_main.tex#L467) 双层的结合能比体相低 0.19 eV/atom, 需要解释或核查 (自由原子参考, 自旋极化, D3, 截断能是否一致).
- [ ] [project_1_main.tex:136](../../../src/project_1_main.tex#L136) 定义了层间结合能 $E_\mathrm{b}$, 全章没有给出数值, 第 732 行的结论却说 "small binding energies".
- [ ] 光学有效厚度的约定各章不同: 第 5 章不归一化 ([project_1_main.tex:511](../../../src/project_1_main.tex#L511)), 第 6 章用 B 1.91 Å 和 H 1.2 Å ([project_2_SI.tex:64](../../../src/project_2_SI.tex#L64)), 第 7 章用 Be 1.98 Å 和 H 0.70 Å ([project_3_main.tex:357](../../../src/project_3_main.tex#L357)). 在第 3 章用一张表说明各章的约定.

## 2. 非母语用法

对应 `SKILL.md` 第 7 节的规则.

- [ ] [fundamentals_a.tex:643](../../../src/fundamentals_a.tex#L643), [appendix_electrodynamics.tex:34](../../../src/appendix_electrodynamics.tex#L34): "let us start by" 改为 "let us start with".
- [ ] [fundamentals_a.tex:516](../../../src/fundamentals_a.tex#L516), [fundamentals_a.tex:1056](../../../src/fundamentals_a.tex#L1056): "we achieve:" 改为 "we obtain:".
- [ ] [fundamentals_a.tex:1054](../../../src/fundamentals_a.tex#L1054), [fundamentals_a.tex:1441](../../../src/fundamentals_a.tex#L1441): "we process X as", "we can process X as" 改为 "we treat X as" 或 "we regard X as".
- [ ] [fundamentals_a.tex:698](../../../src/fundamentals_a.tex#L698): "the problem degenerates to" 改为 "the problem reduces to".
- [ ] [fundamentals_a.tex:42](../../../src/fundamentals_a.tex#L42): "the electron density of ground state" 改为 "the ground-state electron density".
- [ ] [fundamentals_a.tex:59](../../../src/fundamentals_a.tex#L59): 同一行有两处. "the kernel idea of density functional theory is here:" 改为 "the key idea", 句中的冒号改为句号. "the corresponding wave function of ground state $\Psi_0$" 改为 "the corresponding ground-state wave function $\Psi_0$".
- [ ] [fundamentals_a.tex:1452](../../../src/fundamentals_a.tex#L1452): "it demonstrates as:" 改为 "it takes the form:".
- [ ] [fundamentals_a.tex:193](../../../src/fundamentals_a.tex#L193): "Review the expression of ..." 改为 "Recall the expression for ...".
- [ ] [appendix_quantum.tex:247](../../../src/appendix_quantum.tex#L247): "We adopt $i$ labels the electrons and $I$ labels nuclei." 改为 "We use $i$ to label the electrons and $I$ to label the nuclei."
- [ ] [appendix_electrodynamics.tex:23](../../../src/appendix_electrodynamics.tex#L23): "The present section does not review a complete lecture of electrodynamics; instead, we only extract ..." 改为 "The present section extracts only the ingredients required for ...". 上次只删了 aim to.
- [ ] [fundamentals_a.tex:1296](../../../src/fundamentals_a.tex#L1296): "In practice, the Kohn--Sham equations give the exact electron density in principle" 改为 "In principle, the Kohn--Sham equations give the exact electron density". 第 607 行删去的 in principle 不是这一处.
- [ ] [fundamentals_a.tex:1421](../../../src/fundamentals_a.tex#L1421) 和 [fundamentals_a.tex:1428](../../../src/fundamentals_a.tex#L1428): "If we start from the naive choice:" 仍没有主句. 改为 "We first test the naive choice:", 第 1428 行改为 "With this choice, the density ... concentrates near the centre of the well." 上次只把 one 改成了 we.

已完成:

- [x] [fundamentals_a.tex:59](../../../src/fundamentals_a.tex#L59): "the density of ground state $n(\vec{r}\,)$" 已改为 "the ground-state density $n(\vec{r}\,)$".
- [x] [appendix_quantum.tex:1297](../../../src/appendix_quantum.tex#L1297): "This is convenient" 已改为 "It is convenient".
- [x] [appendix_electrodynamics.tex:351](../../../src/appendix_electrodynamics.tex#L351): "Afterwards, ... then ..." 已删去 then.
- [x] [fundamentals_a.tex:301](../../../src/fundamentals_a.tex#L301), [fundamentals_a.tex:1022](../../../src/fundamentals_a.tex#L1022), [appendix_quantum.tex:1406](../../../src/appendix_quantum.tex#L1406): 三处 "Since A." 残句已改.

## 3. 防御性句子

GPT 润色时常写这类句子. 每条后面标出类型, 改法如下:

- 否定: "X does not (by itself) establish Y", "X alone does not ...", "need not". 改为肯定句, 说明 Y 由什么确定. 见 SKILL.md 的 3.3 节和 references/examples.md 的 B1.
- 规定: "must be ...", "should be ...", "we must also ...". 改为陈述论文实际做了什么, 或直接删去. 见 references/examples.md 的 B3.
- 待定: "remains to be established", "has not been calculated", "requires further checks". 正文最多保留一次, 集中写进第 8 章的 Limitations 或 Outlook.
- 范围: "within the stated approximations", "under the stated convention". 在方法部分说明一次, 结果段删去.
- 对比: "rather than ...", "X, not Y". 直接陈述它是什么.
- 图注: 在正文里否认图的含义, 如 "they are not calculated bands". 移进图注, 改为肯定描述.

正文里的数学或物理否定不属于这一类, 不需要改, 例如 "its $\mathbb{Z}_2$ index cannot change", "the polarization response cannot occur before the external electric field is applied". 第 5 章非对角元和第 6 章 $T_c$ 相关的句子已归入第 1 节.

### 摘要

- [ ] [abstract.tex:38](../../../src/abstract.tex#L38) 否定: "Neither dimensional reduction nor hydrogenation enhances absorption in every direction or throughout the visible range."

### 第 1 章

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

### 第 2 章 (集中在第 2.3, 2.4 节)

- [ ] [fundamentals_a.tex:79](../../../src/fundamentals_a.tex#L79) 对比: "This is not merely a change of notation; it marks ..." 见 references/examples.md 的 B5.
- [ ] [fundamentals_a.tex:1719](../../../src/fundamentals_a.tex#L1719) 否定: "A larger band gap does not by itself imply a more accurate result."
- [ ] [fundamentals_a.tex:1721](../../../src/fundamentals_a.tex#L1721) 规定: "... we need to consider the limitations of both functionals."
- [ ] [fundamentals_a.tex:1777](../../../src/fundamentals_a.tex#L1777) 规定: "... it must also enter the energy and its derivatives used for relaxation."
- [ ] [fundamentals_a.tex:1799](../../../src/fundamentals_a.tex#L1799) 否定: "... satisfying these stopping criteria does not establish convergence with respect to the plane-wave cutoff ..."
- [ ] [fundamentals_a.tex:1884](../../../src/fundamentals_a.tex#L1884) 否定: "The smooth auxiliary density alone is therefore not the reconstructed all-electron density."
- [ ] [fundamentals_a.tex:1886](../../../src/fundamentals_a.tex#L1886) 规定: "The datasets and their convergence settings must be specified for each calculation." 见 references/examples.md 的 B3.
- [ ] [fundamentals_a.tex:1906](../../../src/fundamentals_a.tex#L1906) 否定: "A high-symmetry path used to display a band structure does not replace this integration mesh."
- [ ] [fundamentals_a.tex:2002](../../../src/fundamentals_a.tex#L2002) 规定: "Small imaginary frequencies require convergence checks before they can be attributed to numerical errors."
- [ ] [fundamentals_a.tex:2003](../../../src/fundamentals_a.tex#L2003) 范围: "... within the wave vectors and numerical accuracy examined."
- [ ] [fundamentals_a.tex:2023](../../../src/fundamentals_a.tex#L2023) 规定: "... must therefore be specified with each calculation." 见 references/examples.md 的 B3.
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

### 第 3 章

- [ ] [fundamentals_b.tex:232](../../../src/fundamentals_b.tex#L232) 范围: "Within the adopted independent-particle description, the spectra resolve ..."
- [ ] [fundamentals_b.tex:256](../../../src/fundamentals_b.tex#L256) 否定: "Therefore, these spectra do not describe the complete low-frequency response of the metallic systems." 第 7 章第 350 行, 第 8 章第 196 行重复了同一限定.
- [ ] [fundamentals_b.tex:711](../../../src/fundamentals_b.tex#L711) 范围: "The resulting reflectivity is a parameter of this effective-medium model." 连同第 712 行.
- [ ] [fundamentals_b.tex:714](../../../src/fundamentals_b.tex#L714) 对比: "... a formal out-of-plane response of the scalar model, not a second normal-incidence channel of the layer."
- [ ] [fundamentals_b.tex:783](../../../src/fundamentals_b.tex#L783) 规定: "finite momentum and surface contributions require the appropriate scattering geometry."
- [ ] [fundamentals_b.tex:799](../../../src/fundamentals_b.tex#L799) 否定: "... so a peak alone does not establish a plasmon."
- [ ] [fundamentals_b.tex:816](../../../src/fundamentals_b.tex#L816) 否定: "Therefore, a large imaginary part does not by itself produce a strong loss peak." 可改为 "A larger imaginary part therefore lowers the loss peak at the zero crossing."

### 第 4 章

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

### 第 5 章

- [ ] [project_1_main.tex:89](../../../src/project_1_main.tex#L89) 否定: "... the calculations do not establish the performance of a fabricated device."
- [ ] [project_1_main.tex:485](../../../src/project_1_main.tex#L485) 待定: "... their dispersion and lifetimes are not calculated here."
- [ ] [project_1_main.tex:574](../../../src/project_1_main.tex#L574) 规定: "These near-zero values must be considered together with $\varepsilon_2$ and the energy-loss spectrum;"
- [ ] [project_1_main.tex:575](../../../src/project_1_main.tex#L575) 否定: "they do not alone determine the reflectivity or establish a plasmon resonance."
- [ ] [project_1_main.tex:640](../../../src/project_1_main.tex#L640) 否定: "it need not coincide with the first maximum of $\varepsilon_2(\omega)$." 第 6 章第 793 行重复.
- [ ] [project_1_main.tex:670](../../../src/project_1_main.tex#L670) 否定: "... the negative real part alone does not establish a plasmon resonance."
- [ ] [project_1_main.tex:708](../../../src/project_1_main.tex#L708) 规定: "Their optical transparency should be interpreted together with ... does not by itself guarantee weak attenuation."

### 第 6 章

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

### 第 7 章

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
- [ ] [project_3_main.tex:1017](../../../src/project_3_main.tex#L1017) 否定: "They do not by themselves establish propagating modes ..." 见 references/examples.md 的 B1.
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

### 第 8 章

结论正文和 Connections 一节中的句子:

- [ ] [conclusion.tex:27](../../../src/conclusion.tex#L27) 否定: "... but these local separations do not establish an insulating gap for the complete bilayer."
- [ ] [conclusion.tex:38](../../../src/conclusion.tex#L38) 否定: "...; this comparison does not imply stronger absorption over the whole spectrum."
- [ ] [conclusion.tex:51](../../../src/conclusion.tex#L51) 否定: "... these two operations need not produce the same trend."
- [ ] [conclusion.tex:63](../../../src/conclusion.tex#L63) 否定: "This comparison illustrates why the coupling constant alone does not determine $T_{\mathrm{c}}$." 见 references/examples.md 的 B2.
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
- [ ] [conclusion.tex:325](../../../src/conclusion.tex#L325) 否定: "... do not establish either situation in the materials studied here." 所在的 anyon 段落建议整段删去, 见第 4 节.

### 附录 C

- [ ] [appendix_topology.tex:294](../../../src/appendix_topology.tex#L294) 图注: "The pointers therefore describe phase choices, rather than spin directions or real-space vectors."
- [ ] [appendix_topology.tex:312](../../../src/appendix_topology.tex#L312) 否定: "... a Berry phase on an arbitrary loop is not by itself the two-dimensional $\mathbb{Z}_2$ index."
- [ ] [appendix_topology.tex:603](../../../src/appendix_topology.tex#L603) 图注: "The plane represents a subspace of states, rather than an energy band or a plane in the crystal;" 连同第 604 行.
- [ ] [appendix_topology.tex:672](../../../src/appendix_topology.tex#L672) 对比: "They are not two separate occupied bands."

## 4. 重复与篇幅 (P1)

- [ ] 第 2 章: $\Omega=\Omega[n]$ 显示了 4 次 (label 依次为 `ground_state_observable_expectation_value`, `ground_state_observable_density_functional`, `functional_from_expectation`, `functional_from_density`). HK 定理的结论复述 4 到 5 次. KS 方程在 2.2.2, 2.2.3, 2.2.4 三节各推导一遍.
- [ ] 附录 A: $\hat{U}(\tau)$ 的指数形式显示 4 次 (从 [appendix_quantum.tex:73](../../../src/appendix_quantum.tex#L73) 起). 巨正则系综写了两遍, [appendix_quantum.tex:702](../../../src/appendix_quantum.tex#L702) 的文字说 "compact operator form", 显示的却是求和式. $T_\mathrm{TF}$, $T_\mathrm{vW}$, $E_\mathrm{H}$ 和 Thomas--Fermi 方程各写了两遍. 巨正则系综, 跃迁密度, Bohr 频率, 时序算符在后文都没有用到.
- [ ] 附录 B: $\varepsilon_{\alpha\beta}=\delta_{\alpha\beta}+\chi_{\alpha\beta}$ 显示两次 ([appendix_electrodynamics.tex:202](../../../src/appendix_electrodynamics.tex#L202) 与 [appendix_electrodynamics.tex:370](../../../src/appendix_electrodynamics.tex#L370)), $P_\alpha=\varepsilon_0\sum_\beta\chi_{\alpha\beta}E_\beta$ 显示两次 (第 177 行与第 357 行). 见 references/examples.md 的 B4.
- [ ] 第 3 章与附录 B 有四段几乎相同: 开头一句 ([fundamentals_b.tex:23](../../../src/fundamentals_b.tex#L23) 与 [appendix_electrodynamics.tex:15](../../../src/appendix_electrodynamics.tex#L15)), 单位约定 ([fundamentals_b.tex:28](../../../src/fundamentals_b.tex#L28) 与 [appendix_electrodynamics.tex:27](../../../src/appendix_electrodynamics.tex#L27)), $\mu_\mathrm{r}\approx1$ ([fundamentals_b.tex:51](../../../src/fundamentals_b.tex#L51) 与 [appendix_electrodynamics.tex:98](../../../src/appendix_electrodynamics.tex#L98)), regular response 前提 ([fundamentals_b.tex:353](../../../src/fundamentals_b.tex#L353) 与 [appendix_electrodynamics.tex:425](../../../src/appendix_electrodynamics.tex#L425)).
- [ ] 第 3 章与第 7 章用同一组铍烯光谱图, 描述也几乎逐字相同, 例如 [fundamentals_b.tex:657](../../../src/fundamentals_b.tex#L657) 与 [project_3_main.tex:1039](../../../src/project_3_main.tex#L1039).
- [ ] 第 5 章与第 6 章有相同的教科书句子: 折射率 ([project_1_main.tex:679](../../../src/project_1_main.tex#L679) 与 [project_2_main.tex:833](../../../src/project_2_main.tex#L833)), 介电张量的含义 ([project_1_main.tex:559](../../../src/project_1_main.tex#L559) 与 [project_2_main.tex:768](../../../src/project_2_main.tex#L768)), 带间跃迁与等离激元的耦合 ([project_1_main.tex:665](../../../src/project_1_main.tex#L665) 与 [project_2_main.tex:352](../../../src/project_2_main.tex#L352)).
- [ ] [fundamentals_c.tex:209](../../../src/fundamentals_c.tex#L209) 第 209 至 221 行在正文中描述图 4.1 的颜色, 箭头和阴影, 移进图注.
- [ ] [conclusion.tex:322](../../../src/conclusion.tex#L322) 第 322 至 328 行的 anyon 段落与本文结果关系很远, 建议删去.

## 5. 排版与记号 (P2)

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
