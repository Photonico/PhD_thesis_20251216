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

每条下面给出参考写法: "改写" 是按 `SKILL.md` 风格拟的句子, "或" 是另一种写法, "建议" 表示删去, 合并或移入图注. 参考句只改句式, 保留原句的限定含义, 不增加新的结论. 原句带 `\cite` 的, 参考句保留同一引用.

正文里的数学或物理否定不属于这一类, 不需要改, 例如 "its $\mathbb{Z}_2$ index cannot change", "the polarization response cannot occur before the external electric field is applied". 第 5 章非对角元和第 6 章 $T_c$ 相关的句子已归入第 1 节.

### 摘要

- [ ] [abstract.tex:38](../../../src/abstract.tex#L38) 否定: "Neither dimensional reduction nor hydrogenation enhances absorption in every direction or throughout the visible range."
  - 改写: Dimensional reduction and hydrogenation redistribute the absorption between directions and photon energies, strengthening some components and weakening others.
  - 建议: 删去. 前一句的 direction-dependent redistribution 已经表达了同一层意思.

### 第 1 章

- [ ] [introduction.tex:49](../../../src/introduction.tex#L49) 否定: "Elemental composition alone does not specify the structure of a boron sheet."
  - 改写: The structure of a boron sheet depends on the arrangement of its triangular units and holes, in addition to its composition.
  - 或: Boron sheets of the same composition differ in the arrangement of their triangular units and holes.
- [ ] [introduction.tex:50](../../../src/introduction.tex#L50) 规定: "We must also specify the arrangement of triangular units and holes within the sheet."
  - 建议: 删去, 已并入第 49 行的改写.
- [ ] [introduction.tex:56](../../../src/introduction.tex#L56) 否定: "... explains why it need not select one unique sheet."
  - 改写: Thus, the bonding argument accounts for the stabilizing role of the holes, while the configurational comparison reveals several sheets with closely competing energies.
  - 或: The holes therefore stabilize the boron network, and several hole arrangements compete closely in energy.
- [ ] [introduction.tex:75](../../../src/introduction.tex#L75) 否定: "... retaining metallicity does not imply an unchanged optical response."
  - 改写: The optical response therefore changes even when the sheet remains metallic.
  - 或: Strain thus reshapes the optical response of a metallic sheet while preserving its metallic character.
- [ ] [introduction.tex:90](../../../src/introduction.tex#L90) 规定: "... we must also determine the transition strengths ...; the gap alone does not specify them."
  - 改写: The optical response further depends on the transition strengths and their polarization dependence, which we determine in addition to the gap.
  - 或: We therefore determine the transition strengths and their polarization dependence together with the gap.
- [ ] [introduction.tex:133](../../../src/introduction.tex#L133) 否定: "... show why a stable bulk element does not automatically produce a stable sheet in every geometry."
  - 改写: The resulting differences in dynamical stability show that the stability of a sheet depends on its geometry, even for an element with a stable bulk phase.
  - 或: A stable bulk element therefore forms stable sheets only in selected geometries.
- [ ] [introduction.tex:136](../../../src/introduction.tex#L136) 规定: "For each candidate, we must also examine how the atoms respond to displacement."
  - 改写: For each candidate, we therefore examine the response of the atoms to displacement.
  - 或: We therefore test each candidate against atomic displacements.
- [ ] [introduction.tex:155](../../../src/introduction.tex#L155) 否定: "Thus, adding a layer need not produce a simple interpolation between monolayer and bulk properties."
  - 改写: Thus, the properties vary non-monotonically from the monolayer to the bulk.
  - 或: Thus, each added layer changes the properties in its own way, beyond an interpolation between the monolayer and the bulk.
- [ ] [introduction.tex:192](../../../src/introduction.tex#L192) 范围: "...; they do not include the bound electron-hole excitations of a Bethe--Salpeter treatment."
  - 改写: Our independent-particle calculations describe transitions between the calculated one-electron states. A Bethe--Salpeter treatment would add the bound electron-hole excitations.
  - 或: Our optical calculations remain at the independent-particle level, where the excited electron and the hole move independently.
- [ ] [introduction.tex:196](../../../src/introduction.tex#L196) 否定: "... interactions that a semilocal functional alone does not adequately describe ..."
  - 改写: Dispersion corrections add the long-range van der Waals attraction missing from semilocal functionals, and therefore enter the relaxation of the graphene-based bilayers~\cite{grimme2010consistent,grimme2011effect}.
  - 或: Dispersion corrections supply the van der Waals attraction between the layers and therefore enter the relaxation of the graphene-based bilayers~\cite{grimme2010consistent,grimme2011effect}.
- [ ] [introduction.tex:197](../../../src/introduction.tex#L197) 规定: "We must also specify how we represent the optical response."
  - 改写: We next specify the representation of the optical response.
  - 或: The optical response also depends on the way we represent the sheet in the periodic cell.
- [ ] [introduction.tex:248](../../../src/introduction.tex#L248) 规定: "To describe the response to light, we must also determine which transitions couple ..."
  - 改写: The response to light further depends on the transitions that couple to the electric field and on their strengths.
  - 或: We therefore determine the transitions that couple to the electric field, together with their strengths.
- [ ] [introduction.tex:272](../../../src/introduction.tex#L272) 对比: "... rather than assigning a mode from a peak alone."
  - 改写: We therefore compare each loss peak with both parts of the dielectric response before assigning a mode.
  - 或: We therefore read each loss peak together with both parts of the dielectric response.
- [ ] [introduction.tex:274](../../../src/introduction.tex#L274) 范围: "Within the stated optical treatment, we use the calculated loss spectra ..."
  - 改写: We use the calculated loss spectra to trace changes in screening and to examine possible collective excitations.
  - 或: The calculated loss spectra trace the changes in screening and identify candidate collective excitations.
- [ ] [introduction.tex:286](../../../src/introduction.tex#L286) 否定: "Band energies alone do not specify this organization, since they do not contain the full information ..."
  - 改写: This organization resides in the wave functions, in addition to the band energies.
  - 或: The wave functions carry this organization across the Brillouin zone.

### 第 2 章 (集中在第 2.3, 2.4 节)

- [ ] [fundamentals_a.tex:79](../../../src/fundamentals_a.tex#L79) 对比: "This is not merely a change of notation; it marks ..." 见 references/examples.md 的 B5.
  - 改写: This step compresses a function of $3N$ variables, $\Psi_0(\vec{r}_1,\cdots,\vec{r}_N\,)$, into a function of three spatial variables, $n(\vec{r}\,)$. This compression forms the basis of practical density functional theory.
  - 或: This replacement reduces the number of variables from $3N$ in $\Psi_0(\vec{r}_1,\cdots,\vec{r}_N\,)$ to three in $n(\vec{r}\,)$, and it forms the basis of practical density functional theory.
- [ ] [fundamentals_a.tex:1719](../../../src/fundamentals_a.tex#L1719) 否定: "A larger band gap does not by itself imply a more accurate result."
  - 改写: Experiment or a quasiparticle calculation determines which of the two gaps is more accurate.
  - 或: 与上一句合并为: HSE06 remains an approximation, and experiment determines which predicted gap is more accurate.
- [ ] [fundamentals_a.tex:1721](../../../src/fundamentals_a.tex#L1721) 规定: "... we need to consider the limitations of both functionals."
  - 改写: Therefore, in chapters~\ref{cha:project_bilayers} and~\ref{cha:project_boron}, we compare the PBE and HSE06 results side by side.
  - 或: Therefore, chapters~\ref{cha:project_bilayers} and~\ref{cha:project_boron} report both the PBE and the HSE06 results.
- [ ] [fundamentals_a.tex:1777](../../../src/fundamentals_a.tex#L1777) 规定: "... it must also enter the energy and its derivatives used for relaxation."
  - 改写: An empirical dispersion correction, when included, enters both the energy and the forces used for relaxation.
  - 或: When we include an empirical dispersion correction, it contributes to both the energy and its derivatives.
- [ ] [fundamentals_a.tex:1799](../../../src/fundamentals_a.tex#L1799) 否定: "... satisfying these stopping criteria does not establish convergence with respect to the plane-wave cutoff ..."
  - 改写: We therefore test the plane-wave cutoff and the reciprocal-space sampling separately.
  - 或: The plane-wave cutoff and the sampling of reciprocal space are converged in separate tests.
- [ ] [fundamentals_a.tex:1884](../../../src/fundamentals_a.tex#L1884) 否定: "The smooth auxiliary density alone is therefore not the reconstructed all-electron density."
  - 改写: The all-electron density therefore combines the smooth auxiliary density with these augmentation corrections.
  - 或: The augmentation corrections therefore restore the all-electron density from the smooth auxiliary density.
- [ ] [fundamentals_a.tex:1886](../../../src/fundamentals_a.tex#L1886) 规定: "The datasets and their convergence settings must be specified for each calculation." 见 references/examples.md 的 B3.
  - 改写: The research chapters report the datasets and their convergence settings.
  - 或: Each research chapter lists the PAW datasets or pseudopotentials together with their convergence settings.
- [ ] [fundamentals_a.tex:1906](../../../src/fundamentals_a.tex#L1906) 否定: "A high-symmetry path used to display a band structure does not replace this integration mesh."
  - 改写: The integration uses this mesh, whereas a high-symmetry path only displays the band structure.
  - 或: We use the uniform mesh for integration and the high-symmetry path for display.
- [ ] [fundamentals_a.tex:2002](../../../src/fundamentals_a.tex#L2002) 规定: "Small imaginary frequencies require convergence checks before they can be attributed to numerical errors."
  - 改写: For small imaginary frequencies, convergence tests distinguish numerical errors from a physical instability.
  - 或: Convergence tests with respect to the supercell size and the sampling separate numerical errors from a physical instability.
- [ ] [fundamentals_a.tex:2003](../../../src/fundamentals_a.tex#L2003) 范围: "... within the wave vectors and numerical accuracy examined."
  - 改写: The absence of imaginary modes supports harmonic dynamical stability of the structure.
  - 或: A spectrum without imaginary modes indicates harmonic dynamical stability on the calculated wave-vector grid.
- [ ] [fundamentals_a.tex:2023](../../../src/fundamentals_a.tex#L2023) 规定: "... must therefore be specified with each calculation." 见 references/examples.md 的 B3.
  - 改写: Each research chapter therefore reports the ensemble, thermostat, time step, and duration of its trajectories.
  - 或: Sections~\ref{2_methods} and~\ref{3_methods} list these settings for each trajectory.
- [ ] [fundamentals_a.tex:2025](../../../src/fundamentals_a.tex#L2025) 否定: "Neither test alone establishes thermodynamic stability or experimental synthesizability."
  - 改写: Thermodynamic stability and synthesizability further depend on the competing phases and the preparation conditions.
  - 或: Together, the two tests characterize local stability and thermal persistence, while thermodynamic stability follows from a comparison with competing phases.
- [ ] [fundamentals_a.tex:2081](../../../src/fundamentals_a.tex#L2081) 规定: "The normalization must be stated when reporting an energy difference, and the numerical uncertainty must be small ..."
  - 改写: We state the normalization of each energy difference and compare the difference with the numerical uncertainty.
  - 或: Each energy difference carries its normalization, here per atom, and its size relative to the numerical uncertainty.
- [ ] [fundamentals_a.tex:2086](../../../src/fundamentals_a.tex#L2086) 否定: "A vanishing total spin moment alone does not distinguish an antiferromagnetic state from a non-magnetic state;"
  - 改写: The local spin density distinguishes an antiferromagnetic state from a non-magnetic state, since both have a vanishing total spin moment.
  - 或: Both an antiferromagnetic state and a non-magnetic state have a vanishing total moment, and the local spin density separates them.
- [ ] [fundamentals_a.tex:2088](../../../src/fundamentals_a.tex#L2088) 否定: "... but does not by itself establish magnetic order at finite temperature."
  - 改写: The lowest-energy solution identifies the preferred state among the configurations examined. Magnetic order at finite temperature further depends on the exchange interactions and the magnetic anisotropy.
  - 或: The lowest-energy solution identifies the preferred zero-temperature state among the configurations examined.
- [ ] [fundamentals_a.tex:2140](../../../src/fundamentals_a.tex#L2140) 规定: "For entangled bands, a subspace must first be selected within the chosen energy windows."
  - 改写: For entangled bands, we first select a subspace within the chosen energy windows.
  - 或: For entangled bands, a disentanglement step first selects a subspace within the chosen energy windows.
- [ ] [fundamentals_a.tex:2161](../../../src/fundamentals_a.tex#L2161) 规定: "The interpolation must be checked against direct calculations in the energy range of interest."
  - 改写: We check the interpolation against direct calculations in the energy range of interest.
  - 或: A comparison with direct calculations in the energy range of interest validates the interpolation.
- [ ] [fundamentals_a.tex:2167](../../../src/fundamentals_a.tex#L2167) 否定: "Interpolating the band energies alone would not provide the coupling ..."
  - 改写: EPW therefore interpolates the matrix elements in equation~\eqref{electron_phonon_matrix_element_method} together with the band energies.
  - 建议: 删去. 前两句已经说明需要对 $\vec{k}$ 和 $\vec{q}$ 两个变量做 Fourier 变换.
- [ ] [fundamentals_a.tex:2243](../../../src/fundamentals_a.tex#L2243) 规定: "Its applicability must be checked for the system considered;"
  - 改写: The expression applies when the denominator $\lambda-\mu^*(1+0.62\lambda)$ in the exponent remains positive.
  - 或: The expression holds for $\lambda>\mu^*(1+0.62\lambda)$, which keeps the denominator in the exponent positive.
- [ ] [fundamentals_a.tex:2244](../../../src/fundamentals_a.tex#L2244) 规定: "... it should not be extrapolated through a zero or negative denominator in the exponent."
  - 建议: 与上一条是同一句, 按上一条一并改写.
- [ ] [fundamentals_a.tex:2249](../../../src/fundamentals_a.tex#L2249) 否定: "The averaged function $\alpha^2F(\omega)$ alone does not retain the information required ..."
  - 改写: This anisotropic calculation uses the band- and momentum-resolved coupling, which the averaged function $\alpha^2F(\omega)$ integrates out.
  - 或: The anisotropic treatment works with the full coupling $g_{mn,s}(\vec{k},\vec{q}\,)$, whereas $\alpha^2F(\omega)$ keeps only its Fermi-surface average.
- [ ] [fundamentals_a.tex:2255](../../../src/fundamentals_a.tex#L2255) 规定: "... must be identified with those results."
  - 改写: Section~\ref{2_methods} lists the electronic reference state, fine meshes, spectral integration, Coulomb pseudopotential, and transition-temperature estimate used for those results.
  - 或: We report these results together with the electronic reference state, fine meshes, spectral integration, Coulomb pseudopotential, and form of the transition-temperature estimate.

### 第 3 章

- [ ] [fundamentals_b.tex:232](../../../src/fundamentals_b.tex#L232) 范围: "Within the adopted independent-particle description, the spectra resolve ..."
  - 改写: The spectra therefore resolve the interband onset, the absorption peaks, and the directional contrast.
  - 或: In this description, the spectra resolve the interband onset, the absorption peaks, and the directional contrast.
- [ ] [fundamentals_b.tex:256](../../../src/fundamentals_b.tex#L256) 否定: "Therefore, these spectra do not describe the complete low-frequency response of the metallic systems." 第 7 章第 350 行, 第 8 章第 196 行重复了同一限定.
  - 改写: Therefore, these spectra describe the interband part of the low-frequency response of the metallic systems.
  - 或: The free-carrier response of the metals would add to these spectra at low frequency.
- [ ] [fundamentals_b.tex:711](../../../src/fundamentals_b.tex#L711) 范围: "The resulting reflectivity is a parameter of this effective-medium model." 连同第 712 行.
  - 改写: The resulting reflectivity characterizes this effective medium, while the measured reflectance of a finite layer also depends on its thickness, substrate, and optical geometry.
  - 或: The resulting reflectivity belongs to the effective-medium model. A measurement on a finite layer adds the effects of thickness, substrate, and optical geometry.
- [ ] [fundamentals_b.tex:714](../../../src/fundamentals_b.tex#L714) 对比: "... a formal out-of-plane response of the scalar model, not a second normal-incidence channel of the layer."
  - 改写: The value obtained from $\varepsilon_{zz}(\omega)$ therefore represents a formal out-of-plane response of the scalar model.
  - 或: The value obtained from $\varepsilon_{zz}(\omega)$ therefore describes the response to a field normal to the layer, within the scalar model.
- [ ] [fundamentals_b.tex:783](../../../src/fundamentals_b.tex#L783) 规定: "finite momentum and surface contributions require the appropriate scattering geometry."
  - 改写: This loss function describes the corresponding bulk response in electron energy-loss spectroscopy. Finite momentum transfer and surface contributions enter through the scattering geometry.
  - 或: This loss function gives the bulk response measured in electron energy-loss spectroscopy at small momentum transfer.
- [ ] [fundamentals_b.tex:799](../../../src/fundamentals_b.tex#L799) 否定: "... so a peak alone does not establish a plasmon."
  - 改写: Interband excitations also contribute to the loss spectrum, so we identify a plasmon from a loss peak together with a zero of $\varepsilon_{1,\lambda\lambda}(\omega)$~\cite{dressel2002electrodynamics,onida2002electronic}.
  - 或: Interband excitations also produce loss peaks, which we distinguish from plasmons through the behaviour of $\varepsilon_{1,\lambda\lambda}(\omega)$ and $\varepsilon_{2,\lambda\lambda}(\omega)$~\cite{dressel2002electrodynamics,onida2002electronic}.
- [ ] [fundamentals_b.tex:816](../../../src/fundamentals_b.tex#L816) 否定: "Therefore, a large imaginary part does not by itself produce a strong loss peak." 可改为 "A larger imaginary part therefore lowers the loss peak at the zero crossing."
  - 改写: Therefore, a larger imaginary part lowers the loss peak at the zero crossing.
  - 或: Therefore, the loss peak grows as the damping $\varepsilon_{2,\lambda\lambda}(\omega)$ decreases.

### 第 4 章

- [ ] [fundamentals_c.tex:10](../../../src/fundamentals_c.tex#L10) 否定: "... information that is not specified by the band energies alone."
  - 改写: This connection carries information beyond the band energies.
  - 或: The wave functions carry this connection, in addition to the band energies.
- [ ] [fundamentals_c.tex:207](../../../src/fundamentals_c.tex#L207) 规定: "We must therefore specify the band count when assigning a topological index ..."
  - 改写: We therefore state the band count together with any topological index assigned to such a subspace.
  - 或: A topological index of such a subspace therefore refers to a stated number of bands.
- [ ] [fundamentals_c.tex:211](../../../src/fundamentals_c.tex#L211) 图注: "... they are not calculated beryllene bands."
  - 改写: The model dispersions use arbitrary energy units and a dimensionless periodic coordinate $k$.
  - 建议: 整句移入图注, 写成 Model dispersions in arbitrary energy units along a dimensionless periodic coordinate $k$.
- [ ] [fundamentals_c.tex:235](../../../src/fundamentals_c.tex#L235) 待定: "This isolation requires a separate check beyond the illustrated cuts."
  - 改写: We check this isolation over the full two-dimensional Brillouin zone, beyond the illustrated cuts.
  - 建议: 删去. 上一句的 provided the direct separation holds over the full two-dimensional Brillouin zone 已经说明.
- [ ] [fundamentals_c.tex:260](../../../src/fundamentals_c.tex#L260) 对比: "...; they are not two separate bands."
  - 改写: The two spin components belong to one electronic state.
  - 或: The two spin components together form one electronic state and one band.
- [ ] [fundamentals_c.tex:311](../../../src/fundamentals_c.tex#L311) 图注: "...; they contain no calculated parity eigenvalues."
  - 改写: The diagrams indicate the wave-vector locations of the TRIM.
  - 建议: 与第 313 行一起移入图注, 写成 Schematic locations of the TRIM.
- [ ] [fundamentals_c.tex:313](../../../src/fundamentals_c.tex#L313) 图注: "...; it does not indicate a parity or a topological class."
  - 改写: Each colour identifies one inequivalent TRIM and its periodic copies within a panel.
  - 建议: 与第 311 行一起移入图注.
- [ ] [fundamentals_c.tex:377](../../../src/fundamentals_c.tex#L377) 对比: "... the transformation of the state, not the sign of its probability density ..."
  - 改写: This sign describes the transformation of the state, while its probability density remains unchanged in both cases.
  - 或: This sign belongs to the transformation of the state, and the probability density stays the same in both cases.
- [ ] [fundamentals_c.tex:379](../../../src/fundamentals_c.tex#L379) 否定: "An arbitrary numerical basis of that eigenspace need not already have this form."
  - 改写: A numerical calculation therefore rotates its basis within that eigenspace into this form.
  - 或: We therefore diagonalize inversion within each degenerate eigenspace of the numerical calculation.
- [ ] [fundamentals_c.tex:399](../../../src/fundamentals_c.tex#L399) 规定: "At a non-zero TRIM, it must be included when extracting ..."
  - 改写: At a non-zero TRIM, we include this factor when extracting the full Bloch-state parity from a cell-periodic representation.
  - 或: At a non-zero TRIM, this factor enters the full Bloch-state parity obtained from a cell-periodic representation.
- [ ] [fundamentals_c.tex:416](../../../src/fundamentals_c.tex#L416) 规定: "... how parity eigenvalues must be counted in the topological criterion."
  - 改写: This result fixes the counting of parity eigenvalues in the topological criterion.
  - 或: Each Kramers pair therefore contributes one parity eigenvalue to the topological criterion.
- [ ] [fundamentals_c.tex:449](../../../src/fundamentals_c.tex#L449) 否定: "This does not mean that the projector itself is discontinuous, or that all smooth choices of basis are forbidden."
  - 改写: The projector itself remains smooth, and smooth bases without the time-reversal pairing remain available.
  - 建议: 删去. 下一句 The constraint comes from requiring the basis to satisfy the time-reversal pairing ... 已经给出正面表述.
- [ ] [fundamentals_c.tex:458](../../../src/fundamentals_c.tex#L458) 否定: "This relation does not require a conserved spin component."
  - 改写: This relation holds even when spin-orbit coupling mixes the spin components.
  - 或: This relation holds for any spin-orbit coupling that preserves time reversal.
- [ ] [fundamentals_c.tex:474](../../../src/fundamentals_c.tex#L474) 否定: "... it does not establish dissipationless transport in the presence of bulk conduction or inelastic processes."
  - 改写: The statement concerns a single edge within the one-electron description. Bulk conduction and inelastic processes add further channels to the transport.
  - 或: This protection applies to elastic scattering at a single edge within the one-electron description.
- [ ] [fundamentals_c.tex:475](../../../src/fundamentals_c.tex#L475) 否定: "... cannot be inferred from a parity sign alone ..."
  - 改写: For a metallic filling, bulk states remain at the Fermi level alongside any edge states.
  - 或: The insulating-edge interpretation therefore applies when the Fermi level lies in the bulk gap.
- [ ] [fundamentals_c.tex:492](../../../src/fundamentals_c.tex#L492) 否定: "energy ordering alone does not specify these partners."
  - 改写: If several pairs share the same energy, we resolve inversion within that eigenspace and pair its states by time reversal.
  - 或: If several pairs share the same energy, we resolve inversion within that eigenspace and identify the partners through time reversal.
- [ ] [fundamentals_c.tex:518](../../../src/fundamentals_c.tex#L518) 图注: "they are not parity results for a particular material."
  - 改写: These illustrative signs show that the index records an even or odd count.
  - 或: These illustrative signs demonstrate the parity of the count recorded by the index.
- [ ] [fundamentals_c.tex:521](../../../src/fundamentals_c.tex#L521) 对比: "... an additional topological result, not a consequence of degeneracy counting."
  - 改写: Identifying the four-point product with $(-1)^\nu$ is an additional topological result.
  - 建议: 删去后半句. 下一句的 Fu and Kane derive this identification ... 已经说明来源.
- [ ] [fundamentals_c.tex:524](../../../src/fundamentals_c.tex#L524) 否定: "it does not equate an arbitrary-loop single-band Berry phase with $\mathrm{\pi}\nu$."
  - 改写: The criterion evaluates the global time-reversal obstruction of the selected subspace.
  - 建议: 删去后半句. 附录 C 第 312 行已经说明任意回路上的 Berry phase 与 $\mathbb{Z}_2$ 指数的区别.
- [ ] [fundamentals_c.tex:565](../../../src/fundamentals_c.tex#L565) 否定: "The equality of the final expressions does not make the two Brillouin zones equivalent."
  - 改写: The two final expressions coincide because of different symmetry relations among the four TRIM of each zone.
  - 或: The same final expression thus arises from different symmetry relations in the two Brillouin zones.
- [ ] [fundamentals_c.tex:570](../../../src/fundamentals_c.tex#L570) 否定: "A high-symmetry path alone does not justify the reduction."
  - 改写: The crystal symmetry, established from the calculated structure, justifies the reduction.
  - 建议: 删去. 上一句已经说明约化由计算结构的对称性和反演约定确定.
- [ ] [fundamentals_c.tex:589](../../../src/fundamentals_c.tex#L589) 否定: "The small atomic number of an element does not justify omitting spin-orbit coupling from this step:"
  - 改写: We include spin-orbit coupling even for light elements, since a small coupling can still affect a band crossing or a small separation relevant to the selected subspace.
  - 或: Spin-orbit coupling enters this step even for light elements. A small coupling can still open a band crossing or change a small separation in the selected subspace.
- [ ] [fundamentals_c.tex:598](../../../src/fundamentals_c.tex#L598) 否定: "... the phrase ``occupied bands'' alone does not identify the subspace."
  - 改写: For a metal, the number of states below $E_\mathrm{F}$ changes with $\vec{k}$, so we identify the subspace by its band count.
  - 或: For a metal, the number of states below $E_\mathrm{F}$ can change with $\vec{k}$. We therefore define the subspace by a fixed band count.
- [ ] [fundamentals_c.tex:600](../../../src/fundamentals_c.tex#L600) 否定: "Numerical smearing of the occupations also does not define a fixed-rank projector."
  - 建议: 删去, 与第 598, 601 行合并.
  - 或: The fixed band count, independent of the occupation smearing, defines a fixed-rank projector.
- [ ] [fundamentals_c.tex:601](../../../src/fundamentals_c.tex#L601) 规定: "The band count must instead refer to the selected spectral subspace at every wave vector."
  - 改写: The band count instead refers to the selected spectral subspace at every wave vector.
  - 或: The band count fixes the selected spectral subspace at every wave vector.
- [ ] [fundamentals_c.tex:604](../../../src/fundamentals_c.tex#L604) 否定: "... does not establish the condition throughout that zone."
  - 建议: 删去. 前一句要求在整个二维布里渊区检查, 后一句给出了具体做法.
  - 或: We therefore evaluate it on a two-dimensional mesh, beyond the four TRIM and the plotted path.
- [ ] [fundamentals_c.tex:607](../../../src/fundamentals_c.tex#L607) 规定: "... its accuracy near those separations must be checked against direct calculations."
  - 改写: When we use interpolation, we check its accuracy near those separations against direct calculations.
  - 或: Direct calculations near those separations test the accuracy of any interpolation.
- [ ] [fundamentals_c.tex:608](../../../src/fundamentals_c.tex#L608) 规定: "A near-zero separation requires particular care ..."
  - 改写: A near-zero separation receives particular attention, since an unresolved touching point would join the selected and excluded bands.
  - 或: We refine the sampling around near-zero separations, where an unresolved touching point would remove the isolation.
- [ ] [fundamentals_c.tex:614](../../../src/fundamentals_c.tex#L614) 规定: "... the inversion representation must be resolved within that group ..."
  - 改写: For a degenerate group, we resolve the inversion representation within that group and obtain parity eigenstates from the numerical mixture.
  - 或: For a degenerate group, diagonalizing inversion within the group yields the parity eigenstates.
- [ ] [fundamentals_c.tex:621](../../../src/fundamentals_c.tex#L621) 否定: "A parity product alone does not establish a $\mathbb{Z}_2$ invariant if ..."
  - 改写: A parity product defines a $\mathbb{Z}_2$ invariant once the isolation of the selected spectral subspace is established.
  - 建议: 删去. 下一句 Once its isolation and symmetries have been established, the parity criterion classifies this subspace. 是同一内容的肯定表述.
- [ ] [fundamentals_c.tex:633](../../../src/fundamentals_c.tex#L633) 否定: "... cannot be applied without further justification."
  - 改写: If the selected and excluded bands touch, the isolation condition fails, and the classification requires a different argument.
  - 或: The fixed-rank argument of this chapter applies to isolated subspaces, where the selected and excluded bands remain separated.

### 第 5 章

- [ ] [project_1_main.tex:89](../../../src/project_1_main.tex#L89) 否定: "... the calculations do not establish the performance of a fabricated device."
  - 改写: These structure-property relationships provide the main contribution of this chapter.
  - 或: These structure-property relationships provide the main contribution of this chapter. A device study would test them under operating conditions.
- [ ] [project_1_main.tex:485](../../../src/project_1_main.tex#L485) 待定: "... their dispersion and lifetimes are not calculated here."
  - 改写: We interpret the plasmon-related features below within this long-wavelength dielectric description.
  - 或: The plasmon-related features below come from the long-wavelength dielectric response, and a finite-momentum calculation would add their dispersion and lifetimes.
- [ ] [project_1_main.tex:574](../../../src/project_1_main.tex#L574) 规定: "These near-zero values must be considered together with $\varepsilon_2$ and the energy-loss spectrum;"
  - 改写: We therefore read these near-zero values together with $\varepsilon_2$ and the energy-loss spectrum.
  - 或: Together with $\varepsilon_2$ and the energy-loss spectrum, these near-zero values identify the candidate plasmon energies.
- [ ] [project_1_main.tex:575](../../../src/project_1_main.tex#L575) 否定: "they do not alone determine the reflectivity or establish a plasmon resonance."
  - 建议: 与上一条是同一句, 按上一条一并改写.
- [ ] [project_1_main.tex:640](../../../src/project_1_main.tex#L640) 否定: "it need not coincide with the first maximum of $\varepsilon_2(\omega)$." 第 6 章第 793 行重复.
  - 改写: The absorption threshold follows the onset of optically allowed transitions.
  - 或: The absorption threshold marks the onset of optically allowed transitions, below the first maximum of $\varepsilon_2(\omega)$.
- [ ] [project_1_main.tex:670](../../../src/project_1_main.tex#L670) 否定: "... the negative real part alone does not establish a plasmon resonance."
  - 改写: This assignment is consistent with the negative real part of the out-of-plane dielectric-function component.
  - 或: The negative real part of the out-of-plane component supports this assignment, together with the loss feature.
- [ ] [project_1_main.tex:708](../../../src/project_1_main.tex#L708) 规定: "Their optical transparency should be interpreted together with ... does not by itself guarantee weak attenuation."
  - 改写: The extinction coefficient and the energy-loss spectrum determine the attenuation in these regions.
  - 或: We therefore assess the transparency of these regions with the extinction coefficient and the energy-loss spectrum.

### 第 6 章

- [ ] [project_2_main.tex:28](../../../src/project_2_main.tex#L28) 待定: 本章摘要中的 "... small imaginary phonon frequencies near $\Gamma$ require further convergence checks."
  - 改写: The hydrogen-terminated bilayer also retains its bonding framework during a finite-temperature simulation at \qty{400}{K}.
  - 或: The hydrogen-terminated bilayer retains its bonding framework at \qty{400}{K}, and its phonon spectrum shows only small imaginary frequencies near $\Gamma$.
- [ ] [project_2_main.tex:315](../../../src/project_2_main.tex#L315) 对比: "The latter broadening is a numerical parameter, rather than a fitted carrier scattering rate."
  - 改写: The latter broadening is a numerical parameter.
  - 或: The complex frequency shift of \qty{0.1}{\electronvolt} smooths the spectra as a numerical parameter.
- [ ] [project_2_main.tex:349](../../../src/project_2_main.tex#L349) 规定: "... this rescaling should not be identified with a unique intrinsic out-of-plane dielectric constant."
  - 改写: For perpendicular polarization, the electrostatic boundary condition differs from the in-plane case, so the rescaled $zz$ component remains an effective quantity of this convention.
  - 或: For perpendicular polarization, the rescaled response depends on the thickness convention through a different boundary condition.
- [ ] [project_2_main.tex:426](../../../src/project_2_main.tex#L426) 否定: "This positive difference does not establish o-\ce{B14} as the thermodynamic ground-state phase."
  - 改写: o-\ce{B14} is therefore metastable relative to $\alpha$-\ce{B12}.
  - 或: This positive difference places o-\ce{B14} above $\alpha$-\ce{B12} in energy, as a metastable phase.
- [ ] [project_2_main.tex:542](../../../src/project_2_main.tex#L542) 待定: "... their numerical origin has not been established by the present calculations."
  - 改写: These small imaginary frequencies may arise from the numerical treatment of the long-wavelength modes, which larger supercells can test.
  - 或: These small imaginary frequencies lie close to $\Gamma$, where the long-wavelength modes are most sensitive to the numerical treatment.
- [ ] [project_2_main.tex:550](../../../src/project_2_main.tex#L550) 否定: "... it does not establish thermodynamic stability against all competing phases or experimental synthesizability."
  - 建议: 删去. 第 2.4 节和第 8 章 Limitations 已经说明各类稳定性测试的范围.
  - 或: Together with the cohesive energies and phonon spectra, it characterizes the local stability of the structure.
- [ ] [project_2_main.tex:587](../../../src/project_2_main.tex#L587) 否定: "... and does not determine a finite-temperature magnetic ordering temperature."
  - 改写: This small difference is a zero-temperature energy comparison.
  - 或: This small difference compares the two configurations at zero temperature, and the exchange interactions set the ordering temperature.
- [ ] [project_2_main.tex:629](../../../src/project_2_main.tex#L629) 对比: "... a possible interpretation of the calculated HSE06 ordering, rather than an independent determination ..."
  - 改写: This picture provides a qualitative interpretation of the calculated HSE06 ordering.
  - 或: This kinetic-exchange picture interprets the calculated HSE06 ordering qualitatively.
- [ ] [project_2_main.tex:653](../../../src/project_2_main.tex#L653) 否定: "neither result alone establishes the experimental gap."
  - 改写: The gap is therefore sensitive to the exchange-correlation approximation.
  - 或: The gap is therefore sensitive to the exchange-correlation approximation, and a measurement would fix its value.
- [ ] [project_2_main.tex:688](../../../src/project_2_main.tex#L688) 否定: "A larger $\lambda$ does not necessarily imply a higher $T_c$, since ..."
  - 改写: The phonon frequency scale also enters the Allen--Dynes estimate, so the larger $\lambda$ coexists with a lower $T_c$~\cite{migdal1958interaction,marsiglio2020eliashberg,eliashberg1960interactions}.
  - 或: In the Allen--Dynes estimate, the lower $T_c$ of the hydrogen-terminated bilayer therefore reflects a lower phonon frequency scale $\omega_\mathrm{log}$~\cite{migdal1958interaction,marsiglio2020eliashberg,eliashberg1960interactions}.
- [ ] [project_2_main.tex:692](../../../src/project_2_main.tex#L692) 否定: "This result does not determine superconductivity in the gapped antiferromagnetic HSE06 state."
  - 改写: This result refers to the non-magnetic PBE reference of the monolayer.
  - 或: This coupling describes the non-magnetic PBE reference, separate from the gapped antiferromagnetic HSE06 state.
- [ ] [project_2_main.tex:712](../../../src/project_2_main.tex#L712) 范围: "... within the stated electronic and vibrational approximations."
  - 改写: 删去句末的 within the stated electronic and vibrational approximations.
  - 或: ..., whereas the calculations predict phonon-mediated superconductivity in the bulk and the hydrogen-terminated bilayer.
- [ ] [project_2_main.tex:715](../../../src/project_2_main.tex#L715) 待定: "... remain a limitation of the stability assessment."
  - 建议: 删去. 第 542 行和第 8 章 Limitations 已经说明.
  - 或: For the hydrogen-terminated bilayer, the prediction rests on the vibrational reference discussed in section~\ref{xene_ob14_phonon_dispersion}.
- [ ] [project_2_main.tex:717](../../../src/project_2_main.tex#L717) 规定: "The Allen--Dynes and anisotropic Migdal--Eliashberg estimates should be compared separately."
  - 改写: The Allen--Dynes and anisotropic Migdal--Eliashberg estimates provide two separate measures of $T_c$.
  - 或: We report the Allen--Dynes and anisotropic Migdal--Eliashberg estimates as two separate results.
- [ ] [project_2_main.tex:763](../../../src/project_2_main.tex#L763) 否定: "... this response does not by itself determine the free-carrier scattering rate or the dc limit."
  - 改写: This low-energy response contains only the interband transitions.
  - 或: A Drude term with a fitted scattering rate would complete the low-frequency and dc response.
- [ ] [project_2_main.tex:767](../../../src/project_2_main.tex#L767) 否定: "small band overlap does not require strong optical transitions in every polarization."
  - 改写: The bilayer, on the other hand, has a small $\varepsilon_{2}(\omega)$ at low energy despite its PBE semimetallic band structure, since the transitions across the small band overlap are weak.
  - 或: The bilayer, on the other hand, has a small $\varepsilon_{2}(\omega)$ at low energy, which shows weak optical transitions across its small PBE band overlap.
- [ ] [project_2_main.tex:793](../../../src/project_2_main.tex#L793) 否定: "The absorption onset need not coincide with the first maximum of $\varepsilon_{2}(\omega)$."
  - 建议: 删去. 与第 5 章第 640 行重复.
  - 或: The absorption onset follows the first allowed transitions, below the first maximum of $\varepsilon_{2}(\omega)$.
- [ ] [project_2_main.tex:801](../../../src/project_2_main.tex#L801) 规定: "A quantitative comparison requires consistent absorption units and ..."
  - 建议: 连同上一句关于硅的引用一起删去.
  - 或: A quantitative comparison with those results uses the same absorption units and effective-thickness convention.
- [ ] [project_2_main.tex:804](../../../src/project_2_main.tex#L804) 否定: "A negative $\varepsilon_1$ alone does not establish a plasmon resonance:"
  - 改写: 与下一句合并: In the optical limit, a plasmon appears as a loss maximum close to a zero crossing of $\varepsilon_1$ with small $\varepsilon_2$.
  - 或: We identify a plasmon in the optical limit from a loss maximum near a zero crossing of $\varepsilon_1$, where $\varepsilon_2$ remains small.
- [ ] [project_2_main.tex:807](../../../src/project_2_main.tex#L807) 待定: "A wave-vector-dependent response would be required to establish the dispersion ..."
  - 改写: A wave-vector-dependent calculation would give the dispersion of a propagating two-dimensional plasmon.
  - 建议: 移入第 8 章 Outlook, conclusion.tex 第 291 行已有 finite-wave-vector 的计划.
- [ ] [project_2_main.tex:814](../../../src/project_2_main.tex#L814) 否定: "The negative-$\varepsilon_1$ intervals and the loss maxima need not have identical boundaries."
  - 建议: 删去.
  - 或: We compare the loss maxima with the edges of the negative-$\varepsilon_1$ intervals.
- [ ] [project_2_main.tex:853](../../../src/project_2_main.tex#L853) 否定: "... do not independently distinguish a plasmon from an interband transition."
  - 建议: 删去. 前文已用能量损失谱讨论等离激元.
  - 或: These features follow from the same dielectric function and mirror the loss features discussed above.
- [ ] [project_2_main.tex:881](../../../src/project_2_main.tex#L881) 对比: "These comparisons concern the calculated cohesive energies rather than a complete thermodynamic phase diagram."
  - 改写: These comparisons concern the calculated cohesive energies.
  - 或: These comparisons rank the structures by their calculated cohesive energies.
- [ ] [project_2_main.tex:890](../../../src/project_2_main.tex#L890) 待定: "Their plasmonic interpretation remains subject to damping and the effective-medium treatment of the layers."
  - 建议: 删去. 方法部分 (第 321 至 354 行) 已经说明有效介质处理.
  - 或: Their plasmonic character depends on the damping and on the effective-medium treatment of the layers.
- [ ] [project_2_SI.tex:140](../../../src/project_2_SI.tex#L140) 待定: 图 S2.9 图注中的 "further checks are required to distinguish this possibility from a physical instability."
  - 改写: Such modes can be sensitive to numerical convergence in two-dimensional materials~\cite{liu2016continuum,querne2023crystal,pallikara2022physical}, and larger supercells can distinguish this effect from a physical instability.
  - 或: Such modes are known to be sensitive to numerical convergence in two-dimensional materials~\cite{liu2016continuum,querne2023crystal,pallikara2022physical}.

### 第 7 章

- [ ] [project_3_main.tex:25](../../../src/project_3_main.tex#L25) 范围: 本章摘要中的 "... under the stated effective-thickness convention."
  - 改写: 删去句末的 under the stated effective-thickness convention.
  - 或: The calculated dielectric response reveals strong anisotropy and redistributes the visible-to-ultraviolet response between directions, with distinct dielectric and energy-loss features.
- [ ] [project_3_main.tex:333](../../../src/project_3_main.tex#L333) 对比: "... provide scalar comparisons rather than optical constants obtained from the full dielectric tensor."
  - 改写: For monoclinic 1H-$\beta$-beryllene and 2H-$\beta$-beryllene, the derived spectra use the diagonal components and provide scalar comparisons between directions.
  - 或: The derived spectra of monoclinic 1H-$\beta$- and 2H-$\beta$-beryllene therefore compare the diagonal components, with the off-diagonal coupling left for a full-tensor treatment.
- [ ] [project_3_main.tex:335](../../../src/project_3_main.tex#L335) 否定: "... which need not equal the corresponding component of the inverse tensor."
  - 改写: In particular, $L_{\lambda}(\omega)$ uses the inverse of the diagonal component $\varepsilon_{\lambda\lambda}(\omega)$.
  - 建议: 删去, 上一句的 scalar comparisons 已经包含这一点.
- [ ] [project_3_main.tex:338](../../../src/project_3_main.tex#L338) 对比: "... not the full reflection of a finite anisotropic layer on a substrate."
  - 改写: The reflectivity describes a homogeneous semi-infinite medium in the scalar normal-incidence approximation.
  - 或: The reflectivity describes a homogeneous semi-infinite medium at normal incidence, and a film calculation would add the thickness and the substrate.
- [ ] [project_3_main.tex:350](../../../src/project_3_main.tex#L350) 否定: "They therefore do not describe the complete low-frequency response of these metallic systems."
  - 建议: 删去. 第 3 章第 256 行已经说明.
  - 或: They therefore describe the interband part of the low-frequency response of these metallic systems.
- [ ] [project_3_main.tex:509](../../../src/project_3_main.tex#L509) 待定: "... but the dynamical stability near $\Gamma$ remains to be established."
  - 改写: This behaviour is consistent with limitations of the finite-supercell force constants at long wavelengths.
  - 或: This behaviour points to the finite-supercell force constants at long wavelengths, which a larger supercell would test.
- [ ] [project_3_main.tex:528](../../../src/project_3_main.tex#L528) 待定: "... so the full anharmonic stability of 2H-$\beta$-beryllene remains to be established."
  - 改写: This one-mode treatment captures the anharmonic potential along the soft mode.
  - 或: A coupled-mode anharmonic treatment would extend this analysis to the full lattice.
- [ ] [project_3_main.tex:624](../../../src/project_3_main.tex#L624) 待定: "... but this barrier has not been calculated."
  - 改写: 2H-$\alpha$-beryllene may remain kinetically trapped after hydrogenation if the reconstruction barrier is sufficiently high.
  - 或: The reconstruction barrier then controls whether 2H-$\alpha$-beryllene remains kinetically trapped after hydrogenation.
- [ ] [project_3_main.tex:626](../../../src/project_3_main.tex#L626) 否定: "... so this comparison does not replace a global structure search."
  - 改写: This comparison covers two square configurations, while a global structure search samples the full configuration space~\cite{li2018global}.
  - 或: We compare two square configurations, complementing the global structure search of Li et al.~\cite{li2018global}.
- [ ] [project_3_main.tex:784](../../../src/project_3_main.tex#L784) 对比: "... rather than a quantum spin Hall state at the Fermi level." 含义要保留, 只改句式.
  - 改写: The index then describes a band inversion within this subspace, while the states at the Fermi level remain metallic.
  - 或: The index then describes a band inversion within this subspace, and the metallic states at the Fermi level coexist with it.
- [ ] [project_3_main.tex:788](../../../src/project_3_main.tex#L788) 范围: "... the resulting $\mathbb{Z}_2$ indices are conditional screening results." 第 919, 926, 1270 行重复了同一限定, 保留一处.
  - 改写: The resulting $\mathbb{Z}_2$ indices are therefore conditional on the sampled gaps and on time-reversal symmetry.
  - 或: We therefore treat the resulting $\mathbb{Z}_2$ indices as screening results, conditional on the sampled gaps and on time-reversal symmetry.
- [ ] [project_3_main.tex:919](../../../src/project_3_main.tex#L919) 范围: "... in the same conditional sense as $\alpha$-beryllene."
  - 改写: Therefore, trilayer cubic beryllene also carries a non-trivial $\mathbb{Z}_2$ index for its lowest six bands.
  - 或: Therefore, the lowest six bands of trilayer cubic beryllene also form a non-trivial $\mathbb{Z}_2$ subspace.
- [ ] [project_3_main.tex:926](../../../src/project_3_main.tex#L926) 对比: "... a band inversion rather than a quantum spin Hall insulating state." 与第 784 行重复.
  - 建议: 删去. 与第 784 行重复.
  - 或: The non-trivial index therefore characterizes a band inversion within the selected subspace.
- [ ] [project_3_main.tex:929](../../../src/project_3_main.tex#L929) 待定: "... has not been established separately from the local refinement of their minima."
  - 建议: 删去. 第 8 章 Limitations (conclusion.tex 第 221 行) 已经说明.
  - 或: The local refinement locates these meV-scale minima with the cutoff and k-point mesh converged for the total energy.
- [ ] [project_3_main.tex:945](../../../src/project_3_main.tex#L945) 否定: "... but does not establish isolation of the corresponding subspaces throughout the Brillouin zone ..."
  - 改写: This check tests the band order at the time-reversal invariant momenta.
  - 或: This check confirms the band order at the time-reversal invariant momenta, and a full HSE06 calculation with spin-orbit coupling would test the isolation across the Brillouin zone.
- [ ] [project_3_main.tex:1014](../../../src/project_3_main.tex#L1014) 对比: "these are sampled endpoints rather than interpolated zeros."
  - 改写: The two components keep opposite signs between approximately \qty{1.22}{\electronvolt} and \qty{2.21}{\electronvolt}, the endpoints sampled on the calculated energy grid.
  - 或: On the calculated energy grid, these components have opposite signs between the sampled energies \qty{1.22}{\electronvolt} and \qty{2.21}{\electronvolt}.
- [ ] [project_3_main.tex:1017](../../../src/project_3_main.tex#L1017) 否定: "They do not by themselves establish propagating modes ..." 见 references/examples.md 的 B1.
  - 改写: A finite-momentum calculation determines the dispersion of such modes in the two-dimensional layer, and a carrier-scattering treatment determines their lifetimes.
  - 建议: 删去, 上一句改为 The sign changes and loss features identify candidate energy ranges of collective response.
- [ ] [project_3_main.tex:1018](../../../src/project_3_main.tex#L1018) 对比: "The numerical broadening is an input to the calculation, not a calculated scattering lifetime."
  - 改写: The broadening of \qty{0.1}{\electronvolt} enters the present spectra as a numerical parameter.
  - 建议: 删去. 方法部分 (第 347 行) 已经给出 CSHIFT.
- [ ] [project_3_main.tex:1035](../../../src/project_3_main.tex#L1035) 否定: "... the larger maxima do not imply that $\beta$-beryllene absorbs more strongly at every energy."
  - 改写: The spectra cross at some energies, so the ordering of the two phases changes with photon energy.
  - 或: The spectra cross at some energies, and the stronger absorber changes with photon energy.
- [ ] [project_3_main.tex:1048](../../../src/project_3_main.tex#L1048) 否定: "... do not by themselves identify a plasmon resonance."
  - 改写: These crossings describe the dispersion of the effective optical constants.
  - 或: These crossings describe the dispersion of the effective optical constants, and the loss spectra below test their relation to collective modes.
- [ ] [project_3_main.tex:1093](../../../src/project_3_main.tex#L1093) 对比: "this boundary value is not a resolved peak."
  - 改写: It reaches approximately 1.50 at the upper end of the calculated window near \qty{11.98}{\electronvolt}, where it is still rising.
  - 或: It continues to rise up to the upper end of the calculated window, reaching approximately 1.50 near \qty{11.98}{\electronvolt}.
- [ ] [project_3_main.tex:1096](../../../src/project_3_main.tex#L1096) 范围: "These spectra describe the inverse dielectric response under the stated effective-thickness convention."
  - 建议: 删去. 方法部分已经说明有效厚度约定.
  - 或: These spectra describe the inverse dielectric response of the effective layer.
- [ ] [project_3_main.tex:1138](../../../src/project_3_main.tex#L1138) 范围: "Under the stated effective-thickness convention, trilayer cubic beryllene does not show a universal absorption enhancement ..."
  - 改写: In the visible interval, trilayer cubic beryllene absorbs less than bulk bcc beryllium in plane, and more out of plane over part of the interval.
  - 或: Trilayer cubic beryllene redistributes the absorption relative to bulk bcc beryllium.
- [ ] [project_3_main.tex:1146](../../../src/project_3_main.tex#L1146) 对比: "... rather than enhanced absorption throughout the visible and near-ultraviolet regions."
  - 改写: These results show a redistribution of the effective interband response across the visible and near-ultraviolet regions.
  - 或: Dimensional reduction therefore redistributes the effective interband response between directions and photon energies.
- [ ] [project_3_main.tex:1150](../../../src/project_3_main.tex#L1150) 否定: "...; they do not alone establish propagating plasmon modes."
  - 改写: The scalar loss features identify variations in the inverse dielectric response.
  - 或: The scalar loss features identify variations in the inverse dielectric response and mark candidate energies for collective modes.
- [ ] [project_3_main.tex:1181](../../../src/project_3_main.tex#L1181) 对比: "... not a thickness-independent measure of oscillator strength."
  - 改写: Changes in peak height therefore describe the effective response under that convention.
  - 或: Peak heights therefore scale with the assigned thickness, whereas the peak positions of $\varepsilon_2(\omega)$ remain unchanged.
- [ ] [project_3_main.tex:1191](../../../src/project_3_main.tex#L1191) 否定: "... it does not produce a common peak energy, a common zero crossing, or a monotonic enhancement ..."
  - 改写: Thus, increasing hydrogen coverage changes the spectral distribution and the in-plane anisotropy, with peak energies and zero crossings that differ between components.
  - 或: Thus, increasing hydrogen coverage changes the spectral distribution and in-plane anisotropy.
- [ ] [project_3_main.tex:1192](../../../src/project_3_main.tex#L1192) 规定: "The imaginary dielectric peaks should also be distinguished from maxima of the derived absorption coefficient."
  - 改写: The maxima of the derived absorption coefficient differ from these dielectric peaks, since the absorption also depends on the photon energy and the real part.
  - 建议: 删去. 第 1120 行已经说明同一点.
- [ ] [project_3_main.tex:1214](../../../src/project_3_main.tex#L1214) 对比: "... are not evidence of a sharply defined absorption onset or strong visible absorption."
  - 改写: These results establish changes in the calculated interband and inverse dielectric response. The weak low-energy tails come from the numerical broadening.
  - 建议: 删去后半句. 第 1207 行已经给出 2H-$\alpha$ 可见光吸收极弱的数值.
- [ ] [project_3_main.tex:1232](../../../src/project_3_main.tex#L1232) 否定: "The comparisons depend on the stated thickness convention and do not include a Drude intraband contribution."
  - 建议: 删去. 方法部分已经说明, 第 1265 行的结论又重复了一次.
  - 或: These comparisons use the stated thickness convention and the interband response.
- [ ] [project_3_main.tex:1244](../../../src/project_3_main.tex#L1244) 待定: "... leave the long-wavelength stability of 1H-$\beta$-beryllene unresolved."
  - 改写: The phonon-dispersion calculations also confirm the dynamical stability of 2H-$\alpha$-beryllene, while 1H-$\beta$-beryllene shows interpolated imaginary frequencies near $\Gamma$.
  - 或: The phonon-dispersion calculations also confirm the dynamical stability of 2H-$\alpha$-beryllene. For 1H-$\beta$-beryllene, all commensurate modes are real, and the imaginary values appear only in the interpolated flexural branch near $\Gamma$.
- [ ] [project_3_main.tex:1248](../../../src/project_3_main.tex#L1248) 待定: "The full anharmonic stability requires further examination of coupling between modes."
  - 建议: 删去. 第 8 章 Outlook (conclusion.tex 第 240 行) 已经给出耦合模的计划.
  - 或: A coupled-mode anharmonic treatment would extend this result to the full lattice.
- [ ] [project_3_main.tex:1265](../../../src/project_3_main.tex#L1265) 范围: "... under the stated effective-thickness convention and exclude a Drude intraband contribution."
  - 改写: These comparisons use the Cartesian diagonal dielectric components and the interband response.
  - 建议: 删去. 与第 1232 行重复, 方法部分也已说明.
- [ ] [project_3_main.tex:1270](../../../src/project_3_main.tex#L1270) 范围: "... these indices are conditional screening results for band inversions rather than quantum spin Hall states."
  - 改写: The non-trivial subspaces of these metallic phases are isolated by spin-orbit gaps of approximately \qty{1}{\milli\electronvolt} above the Fermi level, and the indices characterize band inversions within these subspaces.
  - 或: These indices characterize band inversions in subspaces isolated by spin-orbit gaps of approximately \qty{1}{\milli\electronvolt}, above the Fermi level of these metallic phases.
- [ ] [project_3_SI.tex:62](../../../src/project_3_SI.tex#L62) 对比: "... and is not a unique physical layer thickness."
  - 改写: Consequently, the assigned 2H-$\alpha$ thickness is smaller than the pristine value under the chosen convention.
  - 或: Consequently, the chosen convention assigns 2H-$\alpha$-beryllene a smaller thickness than the pristine layer.
- [ ] [project_3_SI.tex:79](../../../src/project_3_SI.tex#L79) 否定: "These comparisons do not establish convergence of the complete low-frequency metallic response ..."
  - 改写: These comparisons establish the convergence of the interband response.
  - 或: These comparisons test the convergence of the interband response, and an intraband treatment would complete the low-frequency metallic response.
- [ ] [project_3_SI.tex:81](../../../src/project_3_SI.tex#L81) 对比: "... a final-parameter reference rather than an additional strictly one-parameter convergence point."
  - 改写: The selected reference uses the final k-point grid and band count, which may differ from those of a convergence series.
  - 或: The selected reference represents the final parameter set, which may change both the k-point grid and the total band count.
- [ ] [project_3_SI.tex:260](../../../src/project_3_SI.tex#L260) 对比: "... rather than replacing a full anharmonic phonon calculation."
  - 改写: These one-mode values indicate the size of the quantum fluctuations along the soft mode.
  - 或: Within this one-mode treatment, these values indicate the size of the quantum fluctuations.
- [ ] [project_3_SI.tex:375](../../../src/project_3_SI.tex#L375) 待定: "The dynamical stability of the puckered square layer is not calculated."
  - 建议: 删去. 第 8 章 Outlook (conclusion.tex 第 245 行) 已经列出这项声子计算.
  - 或: A phonon calculation would test the dynamical stability of the puckered square layer.
- [ ] [project_3_SI.tex:414](../../../src/project_3_SI.tex#L414) 待定: "... has not been tested separately from the total-energy convergence."
  - 改写: The local refinements locate minima at fixed self-consistent charge density, with the plane-wave cutoff and the k-point mesh converged for the total energy.
  - 建议: 删去后半句. 第 8 章 Limitations (conclusion.tex 第 221 行) 已经说明.
- [ ] [project_3_SI.tex:424](../../../src/project_3_SI.tex#L424) 否定: "... but does not establish that the lowest-$N$ spinor subspaces remain isolated ..."
  - 改写: This comparison checks the parity ordering at these momenta.
  - 建议: 删去后半句, 与正文第 945 行重复.
- [ ] [project_3_SI.tex:468](../../../src/project_3_SI.tex#L468) 对比: "... conditional PBE results with spin-orbit coupling, not independently determined HSE06 indices."
  - 改写: The listed $\mathbb{Z}_2$ indices are conditional PBE results with spin-orbit coupling.
  - 或: The listed $\mathbb{Z}_2$ indices come from PBE with spin-orbit coupling, and the HSE06 parities in table~\ref{tab:proj3_hse_parity} check their band order.

### 第 8 章

结论正文和 Connections 一节中的句子:

- [ ] [conclusion.tex:27](../../../src/conclusion.tex#L27) 否定: "... but these local separations do not establish an insulating gap for the complete bilayer."
  - 改写: Interlayer coupling opens local gaps of approximately 50 meV in Graphene-\ce{BC3} and 20 meV in Graphene-\ce{B4C3} at this point, while both bilayers remain semimetallic.
  - 或: Interlayer coupling opens local gaps of approximately 50 meV and 20 meV at this point, and the complete bilayers keep their semimetallic character.
- [ ] [conclusion.tex:38](../../../src/conclusion.tex#L38) 否定: "...; this comparison does not imply stronger absorption over the whole spectrum."
  - 改写: Graphene-Borophene has the stronger absorption near the low-energy rise around 1 eV.
  - 或: Graphene-Borophene has the stronger absorption near the low-energy rise around 1 eV, while the other two heterostructures rise at higher energies.
- [ ] [conclusion.tex:51](../../../src/conclusion.tex#L51) 否定: "... these two operations need not produce the same trend."
  - 改写: The resulting electronic structures show that these two operations produce different trends.
  - 或: The two operations therefore act differently on the electronic structure.
- [ ] [conclusion.tex:63](../../../src/conclusion.tex#L63) 否定: "This comparison illustrates why the coupling constant alone does not determine $T_{\mathrm{c}}$." 见 references/examples.md 的 B2.
  - 改写: The logarithmic phonon frequency $\omega_\mathrm{log}$ therefore enters $T_\mathrm{c}$ together with the coupling strength $\lambda$.
  - 或: 与下一句合并: The phonon frequency scale therefore enters $T_{\mathrm{c}}$ together with the coupling constant.
- [ ] [conclusion.tex:69](../../../src/conclusion.tex#L69) 待定: "... whose origin remains unresolved."
  - 改写: The hydrogen-terminated monolayer develops a clear harmonic instability, while the terminated bilayer retains only small imaginary frequencies near $\Gamma$.
  - 或: The hydrogen-terminated monolayer develops a clear harmonic instability, whereas the terminated bilayer shows small imaginary frequencies confined to the vicinity of $\Gamma$.
- [ ] [conclusion.tex:75](../../../src/conclusion.tex#L75) 否定: "... cannot describe the HSE06 antiferromagnetic semiconductor without a further calculation."
  - 改写: Consequently, these spectra characterize that reference.
  - 或: Consequently, these spectra characterize the non-magnetic reference, and a spin-polarized optical calculation would describe the HSE06 antiferromagnetic semiconductor.
- [ ] [conclusion.tex:89](../../../src/conclusion.tex#L89) 对比: "... candidate two-dimensional structures rather than the thermodynamic ground state of elemental beryllium."
  - 改写: They therefore represent metastable two-dimensional structures relative to bulk hcp beryllium.
  - 或: They therefore represent candidate two-dimensional structures, metastable relative to bulk hcp beryllium.
- [ ] [conclusion.tex:91](../../../src/conclusion.tex#L91) 待定: "... the long-wavelength flexural behaviour remains unresolved:"
  - 改写: For 1H-$\beta$-beryllene, the sampled commensurate modes are real, and the interpolated flexural branch develops imaginary frequencies near $\Gamma$.
  - 或: For 1H-$\beta$-beryllene, all commensurate modes are real, while the interpolated flexural branch dips below zero near $\Gamma$.
- [ ] [conclusion.tex:92](../../../src/conclusion.tex#L92) 否定: "... this instability cannot be dismissed solely as an interpolation effect."
  - 改写: The 2H-$\beta$ structure has a soft mode at a commensurate wave vector, so this instability belongs to the calculated force constants themselves.
  - 或: The 2H-$\beta$ structure has a soft mode at a commensurate wave vector, where the supercell calculation samples the frequency directly.
- [ ] [conclusion.tex:96](../../../src/conclusion.tex#L96) 否定: "... explains why the classical minimum alone does not determine the distortion in this model:"
  - 改写: Quantum motion extends across the shallow wells, so the ground state remains centred at the undistorted structure.
  - 或: The zero-point energy exceeds the well depth, and the ground state therefore stays centred at the undistorted structure.
- [ ] [conclusion.tex:97](../../../src/conclusion.tex#L97) 待定: "... while leaving coupling to the other modes unresolved."
  - 改写: This supports suppression of a static distortion along the selected coordinate.
  - 或: This supports suppression of a static distortion along the selected coordinate, and a coupled-mode treatment would extend the result to the full lattice.
- [ ] [conclusion.tex:103](../../../src/conclusion.tex#L103) 范围: "... within the adopted thermodynamic treatment."
  - 改写: Thus, only 2H-$\alpha$-beryllene favours adsorption under these conditions.
  - 或: Thus, 2H-$\alpha$-beryllene is the only structure that favours adsorption under these conditions.
- [ ] [conclusion.tex:104](../../../src/conclusion.tex#L104) 否定: "This comparison does not establish formation from bulk beryllium."
  - 建议: 删去. 上一句已经说明参考态是对应的 pristine sheet 和 \ce{H2}.
  - 或: This comparison refers to the pristine sheets, and formation from bulk beryllium involves a further step.
- [ ] [conclusion.tex:106](../../../src/conclusion.tex#L106) 待定: "Its phonon stability and the reconstruction barrier remain uncalculated."
  - 建议: 删去. 第 245 行的 Outlook 已经列出这两项计算.
  - 或: Its phonon stability and the reconstruction barrier form the next calculations, as outlined in section~\ref{sec:conclusions_outlook}.
- [ ] [conclusion.tex:113](../../../src/conclusion.tex#L113) 对比: "... rather than assign a universal electronic effect to hydrogenation."
  - 改写: The electronic effect of hydrogenation therefore depends on the bonding geometry of the parent sheet.
  - 或: This difference shows that hydrogenation acts through the bonding geometry of each parent sheet.
- [ ] [conclusion.tex:119](../../../src/conclusion.tex#L119) 否定: "... without establishing quantum spin Hall insulators at neutral filling."
  - 改写: These results therefore identify non-trivial band subspaces in two metallic structures.
  - 或: These results therefore identify non-trivial subspaces above the Fermi level, with metallic states at neutral filling.
- [ ] [conclusion.tex:120](../../../src/conclusion.tex#L120) 规定: "... these fixed subspaces must again be distinguished from an occupied insulating manifold."
  - 改写: The selected subspaces of $\beta$-beryllene and the hydrogenated structures give trivial indices.
  - 或: The selected subspaces of $\beta$-beryllene and the hydrogenated structures give trivial indices, and for the metallic systems these indices again refer to fixed band subspaces.
- [ ] [conclusion.tex:122](../../../src/conclusion.tex#L122) 否定: "... changes that the metallic or semiconducting classification alone cannot describe."
  - 改写: The optical response resolves changes beyond the metallic or semiconducting classification.
  - 或: The optical response resolves finer changes than the metallic or semiconducting classification.
- [ ] [conclusion.tex:126](../../../src/conclusion.tex#L126) 否定: "... does not establish strong visible absorption across its wide electronic gap."
  - 改写: For 2H-$\alpha$-beryllene, the response below the main absorption region remains weak, consistent with its wide electronic gap.
  - 或: For 2H-$\alpha$-beryllene, the wide electronic gap keeps the visible absorption weak, and the strong absorption begins in the ultraviolet.
- [ ] [conclusion.tex:135](../../../src/conclusion.tex#L135) 对比: "... rather than to the label of a light-element material alone."
  - 改写: The calculated properties respond to these particular structural changes.
  - 或: The calculated properties follow these particular structural changes.
- [ ] [conclusion.tex:155](../../../src/conclusion.tex#L155) 否定: "... explain why the electronic results do not follow one trend with thickness or hydrogen coverage."
  - 改写: These microscopic comparisons account for the different electronic trends with thickness and hydrogen coverage.
  - 或: These microscopic differences produce different electronic trends with thickness and hydrogen coverage.
- [ ] [conclusion.tex:160](../../../src/conclusion.tex#L160) 规定: "... we must also distinguish their local separations from the electronic character of the complete system."
  - 改写: In the resulting bands, we distinguish local separations from the electronic character of the complete system.
  - 或: The resulting bands contain local separations, which we distinguish from the electronic character of the complete system.
- [ ] [conclusion.tex:168](../../../src/conclusion.tex#L168) 否定: "... the distinction between a metal and a semiconductor does not determine an entire optical spectrum."
  - 改写: The dielectric response depends on the available transitions and their polarization-dependent matrix elements, which resolve differences beyond the distinction between a metal and a semiconductor.
  - 或: The dielectric response depends on the available transitions and their polarization-dependent matrix elements, so the optical spectrum carries more information than the metallic or semiconducting character.
- [ ] [conclusion.tex:174](../../../src/conclusion.tex#L174) 规定: "Finally, the structural and electronic descriptions must refer to the same physical state."
  - 改写: Finally, the structural and electronic descriptions refer to the same physical state.
  - 或: Finally, each response calculation starts from the structural and electronic state it describes.
- [ ] [conclusion.tex:175](../../../src/conclusion.tex#L175) 否定: "An optical spectrum of a non-magnetic reference cannot inherit the gap of a different antiferromagnetic calculation."
  - 改写: An optical spectrum of a non-magnetic reference describes that reference, separate from the gap of the antiferromagnetic state.
  - 建议: 删去. 第 75 行已经说明.

Limitations 一节 (第 181 至 226 行) 本来就是写限制的地方, 这些句子保留, 只改成肯定句:

- [ ] [conclusion.tex:191](../../../src/conclusion.tex#L191), 195, 196, 198, 204, 207, 212, 218, 221, 224, 226 行.
  - 第 191 行: Comparing these functionals tests part of this dependence, and an experimental calibration or a quasiparticle calculation would complete it.
  - 第 195 行: They exclude electron-hole attraction, and the metallic spectra in chapters~\ref{cha:project_boron} and~\ref{cha:project_beryllene} contain only interband transitions.
  - 第 196 行: A Drude term would add the intraband response of the free carriers at low frequency.
  - 第 198 行: The numerical broadening smooths the spectra as a fixed parameter.
  - 第 204 行: The assigned layer thickness affects the reported effective dielectric and absorption quantities, while the surrounding vacuum belongs to the computational cell~\cite{matthes2016influence}.
  - 第 207 行: Likewise, the scalar reflectivity formula describes an idealized semi-infinite medium.
  - 第 212 行: The two tests probe local stability and finite-time persistence, while formation and long-term survival depend on competing phases and experimental timescales.
  - 第 218 行: The preference among the tested spin configurations gives the zero-temperature ordering, while the pairing estimates depend on the phonon spectrum and the chosen Coulomb pseudopotential.
  - 第 221 行: Dense sampling and local refinement locate the smallest sampled separations, and separate cutoff and self-consistent-mesh tests would complete the convergence.
  - 第 224 行: Finally, experimental evidence exists for graphene, boron sheets, and a beryllium sheet, while the specific geometries considered here remain predictions.
  - 第 226 行: Their calculated properties identify questions for experimental testing, and independent structural evidence would confirm their realization.

Outlook 一节中的句子:

- [ ] [conclusion.tex:241](../../../src/conclusion.tex#L241) 对比: "... the starting point for this calculation, rather than its final criterion."
  - 改写: The absence of a static distortion along one coordinate is the starting point for this calculation.
  - 或: The one-coordinate result provides the starting point for this calculation.
- [ ] [conclusion.tex:245](../../../src/conclusion.tex#L245) 待定: "... first requires a phonon calculation before its lower electronic energy can support a stronger stability conclusion."
  - 改写: A phonon calculation of the puckered square-layer \ce{BeH2} candidate comes first, and its result determines the weight of the lower electronic energy.
  - 或: We first calculate the phonons of the puckered square-layer \ce{BeH2} candidate, which test whether its lower electronic energy marks a stable competitor.
- [ ] [conclusion.tex:256](../../../src/conclusion.tex#L256) 否定: "... determining the amount of hydrogen alone would leave its adsorption arrangement and the underlying lattice unresolved."
  - 改写: For a hydrogenated sheet, the structural test resolves the adsorption arrangement and the underlying lattice, in addition to the hydrogen content.
  - 或: For a hydrogenated sheet, a structural measurement determines the adsorption arrangement and the underlying lattice together with the hydrogen content.
- [ ] [conclusion.tex:297](../../../src/conclusion.tex#L297) 对比: "... rather than an idealized bulk-like coefficient."
  - 改写: A film calculation with a selected substrate, incidence angle, and polarization could then predict the measured absorption and reflection.
  - 或: A film calculation could then predict the absorption and reflection of a supported layer for a selected substrate, incidence angle, and polarization.
- [ ] [conclusion.tex:302](../../../src/conclusion.tex#L302) 规定: "... although the film calculation must still account for its interaction with the sheet."
  - 改写: Measuring the support under the same conditions would help separate its contribution, and the film calculation would include its interaction with the sheet.
  - 或: A reference measurement on the bare support would separate its contribution, while the film calculation includes its interaction with the sheet.
- [ ] [conclusion.tex:309](../../../src/conclusion.tex#L309) 规定: "... should therefore precede a stronger topological claim ..."
  - 改写: We would therefore first converge the cutoff, the self-consistent mesh, and the spin-orbit treatment, and then test the isolation with HSE06 and spin-orbit coupling beyond the symmetry points.
  - 或: The next step therefore converges the cutoff, the self-consistent mesh, and the spin-orbit treatment, followed by an HSE06 calculation with spin-orbit coupling across the Brillouin zone.
- [ ] [conclusion.tex:314](../../../src/conclusion.tex#L314) 规定: "Carrier control, strain, or a substrate should therefore be assessed for a specific purpose:"
  - 改写: We would therefore assess carrier control, strain, or a substrate by their ability to produce an accessible insulating energy interval while preserving the required symmetry and band separation.
  - 或: Carrier control, strain, or a substrate could then aim at an accessible insulating energy interval that preserves the required symmetry and band separation.
- [ ] [conclusion.tex:315](../../../src/conclusion.tex#L315) 否定: "We cannot assume that moving the chemical potential alone removes an indirect overlap ..."
  - 改写: Moving the chemical potential alone shifts the filling but leaves the indirect overlap and the small gaps in place.
  - 或: A shift of the chemical potential changes the filling, while the band overlap and the small gaps require a change of the bands themselves.
- [ ] [conclusion.tex:316](../../../src/conclusion.tex#L316) 规定: "Transport predictions should follow these checks rather than follow directly from the parity product."
  - 改写: Transport predictions then follow from these checks.
  - 或: These checks precede any transport prediction based on the parity product.
- [ ] [conclusion.tex:319](../../../src/conclusion.tex#L319) 否定: "... an edge spectral feature alone would not determine its topological origin."
  - 改写: Such a comparison would also include the edge geometry and the remaining bulk states, which together identify the topological origin of an edge feature.
  - 或: Such a comparison would combine the edge spectrum with the edge geometry and the remaining bulk states.
- [ ] [conclusion.tex:325](../../../src/conclusion.tex#L325) 否定: "... do not establish either situation in the materials studied here." 所在的 anyon 段落建议整段删去, 见第 4 节.
  - 建议: 整段删去, 见第 4 节的 anyon 段落.
  - 或: The band-subspace indices and the pairing predictions in this thesis provide a starting point for such an investigation.

### 附录 C

- [ ] [appendix_topology.tex:294](../../../src/appendix_topology.tex#L294) 图注: "The pointers therefore describe phase choices, rather than spin directions or real-space vectors."
  - 改写: The pointers therefore describe phase choices in the complex plane.
  - 建议: 移入图注, 写成 Orange pointers show the phase factors of the state representatives.
- [ ] [appendix_topology.tex:312](../../../src/appendix_topology.tex#L312) 否定: "... a Berry phase on an arbitrary loop is not by itself the two-dimensional $\mathbb{Z}_2$ index."
  - 改写: The phase $\gamma_n(C)$ can take any value modulo $2\mathrm{\pi}$.
  - 或: 与下一句合并: The phase $\gamma_n(C)$ takes general values, and the $\mathbb{Z}_2$ index additionally requires time-reversal symmetry and the full selected band subspace.
- [ ] [appendix_topology.tex:603](../../../src/appendix_topology.tex#L603) 图注: "The plane represents a subspace of states, rather than an energy band or a plane in the crystal;" 连同第 604 行.
  - 改写: The plane represents a subspace of states, while the actual Bloch states belong to a complex Hilbert space of general dimension.
  - 建议: 移入图注, 写成 The shaded plane represents a two-dimensional subspace of states in a real three-dimensional example.
- [ ] [appendix_topology.tex:672](../../../src/appendix_topology.tex#L672) 对比: "They are not two separate occupied bands."
  - 建议: 删去. 上一句已经说明两个空间分量构成一个旋量态.
  - 或: Together, they occupy one band.

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
