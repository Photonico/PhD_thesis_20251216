# todo list

完善论文用的待办清单, 配合同目录下的 `SKILL.md` 使用. 规则和改法见 `SKILL.md`, 这里只列具体位置.
行号以 2026-11-12 的版本为准. 行号变动后按引文搜索. 完成一条就删去该条, 删去的条目见 git 历史.

* 防御性句子

## 防御性句子

GPT 润色时常写这类句子. 每条后面标出类型, 改法如下:

- 否定: "X does not (by itself) establish Y", "X alone does not ...", "need not". 改为肯定句, 说明 Y 由什么确定. 见 SKILL.md 的 3.3 节和 references/examples.md 的 B1.
- 规定: "must be ...", "should be ...", "we must also ...". 改为陈述论文实际做了什么, 或直接删去. 见 references/examples.md 的 B3.
- 待定: "remains to be established", "has not been calculated", "requires further checks". 正文最多保留一次, 集中写进第 8 章的 Limitations 或 Outlook.
- 范围: "within the stated approximations", "under the stated convention". 在方法部分说明一次, 结果段删去.
- 对比: "rather than ...", "X, not Y". 直接陈述它是什么.
- 图注: 在正文里否认图的含义, 如 "they are not calculated bands". 移进图注, 改为肯定描述.

每条下面给出参考写法: "改写" 是按 `SKILL.md` 风格拟的句子, "或" 是另一种写法, "建议" 表示删去, 合并或移入图注. 参考句只改句式, 保留原句的限定含义, 不增加新的结论. 原句带 `\cite` 的, 参考句保留同一引用.

2026-11-13 复核: 每条都对照前后文重新看过, 原则是改动尽量小, 不改原意, 不丢信息, 只动防御性的措辞. 每条的第一行是首选做法. 多数只换掉 alone, by itself, need not, must, should, rather than 这类词, 句子其余部分是原句. 整句删去只用于与相邻句子完全重复的情形. 属于事实陈述的句子 (例如 has not been calculated) 标为保留原句, 确认后可以直接从清单删去.

正文里的数学或物理否定不属于这一类, 不需要改, 例如 "its $\mathbb{Z}_2$ index cannot change", "the polarization response cannot occur before the external electric field is applied". 第 5 章非对角元和第 6 章 $T_c$ 相关的句子已在第 1 节处理.

### 第 1 章

- [ ] [introduction.tex:75](../../../src/introduction.tex#L75) 否定: "... retaining metallicity does not imply an unchanged optical response."
  - 改写: This comparison shows that the optical response can change while the sheet remains metallic.
- [ ] [introduction.tex:90](../../../src/introduction.tex#L90) 规定: "... we must also determine the transition strengths ...; the gap alone does not specify them."
  - 改写: To compare the optical response, we also determine the transition strengths and their polarization dependence in addition to the gap.
  - 建议: 去掉 must, 分号后的 the gap alone does not specify them 改为 in addition to the gap.
- [ ] [introduction.tex:133](../../../src/introduction.tex#L133) 否定: "... show why a stable bulk element does not automatically produce a stable sheet in every geometry."
  - 改写: The resulting differences in dynamical stability show that a stable bulk element produces a stable sheet only in some geometries.
- [ ] [introduction.tex:136](../../../src/introduction.tex#L136) 规定: "For each candidate, we must also examine how the atoms respond to displacement."
  - 改写: For each candidate, we also examine how the atoms respond to displacement.
  - 建议: 只去掉 must.
- [ ] [introduction.tex:155](../../../src/introduction.tex#L155) 否定: "Thus, adding a layer need not produce a simple interpolation between monolayer and bulk properties."
  - 改写: Thus, the properties after adding a layer can deviate from a simple interpolation between the monolayer and the bulk.
- [ ] [introduction.tex:192](../../../src/introduction.tex#L192) 范围: "...; they do not include the bound electron-hole excitations of a Bethe--Salpeter treatment."
  - 建议: 保留原句的内容, 只把分号改成句号, 分成两句. 这是对计算范围的事实陈述, 不属于防御性措辞.
- [ ] [introduction.tex:196](../../../src/introduction.tex#L196) 否定: "... interactions that a semilocal functional alone does not adequately describe ..."
  - 改写: Dispersion corrections account for the van der Waals interactions missing from a semilocal functional and therefore enter the relaxation of the graphene-based bilayers~\cite{grimme2010consistent,grimme2011effect}.
- [ ] [introduction.tex:197](../../../src/introduction.tex#L197) 规定: "We must also specify how we represent the optical response."
  - 改写: We also specify how we represent the optical response.
  - 建议: 只去掉 must.
- [ ] [introduction.tex:248](../../../src/introduction.tex#L248) 规定: "To describe the response to light, we must also determine which transitions couple ..."
  - 改写: To describe the response to light, we also determine which transitions couple to the electric field and how strongly they do so.
  - 建议: 只去掉 must.
- [ ] [introduction.tex:272](../../../src/introduction.tex#L272) 对比: "... rather than assigning a mode from a peak alone."
  - 改写: We therefore compare the loss peaks with both parts of the dielectric response before assigning a mode.
- [ ] [introduction.tex:274](../../../src/introduction.tex#L274) 范围: "Within the stated optical treatment, we use the calculated loss spectra ..."
  - 改写: We use the calculated loss spectra to trace changes in screening and examine possible collective excitations.
  - 建议: 只删去句首的 Within the stated optical treatment.
- [ ] [introduction.tex:286](../../../src/introduction.tex#L286) 否定: "Band energies alone do not specify this organization, since they do not contain the full information ..."
  - 改写: This organization is specified by the wave functions, which contain information beyond the band energies.

### 第 2 章 (集中在第 2.3, 2.4 节)

- [ ] [fundamentals_a.tex:72](../../../src/fundamentals_a.tex#L72) 对比: "This is not merely a change of notation; it marks ..." 见 references/examples.md 的 B5.
  - 改写: This relation marks the conceptual compression from a function of $3N$ variables, $\Psi_0(\vec{r}_1,\cdots,\vec{r}_N\,)$, to a function of only three spatial variables, $n(\vec{r}\,)$, which is the cornerstone of the practical formulation of DFT.
  - 建议: 只把开头的 This is not merely a change of notation; it 换成 This relation, 后面是你的原句.
- [ ] [fundamentals_a.tex:1697](../../../src/fundamentals_a.tex#L1697) 否定: "A larger band gap does not by itself imply a more accurate result."
  - 改写: A larger band gap does not imply a more accurate result.
  - 建议: 只删去 by itself. 这一句的信息 (带隙大不等于更准) 上一句并没有, 所以不删.
- [ ] [fundamentals_a.tex:1699](../../../src/fundamentals_a.tex#L1699) 规定: "... we need to consider the limitations of both functionals."
  - 改写: Therefore, when comparing the results in chapters~\ref{cha:project_bilayers} and~\ref{cha:project_boron}, we consider the limitations of both functionals.
  - 建议: 只把 we need to consider 改为 we consider.
- [ ] [fundamentals_a.tex:1756](../../../src/fundamentals_a.tex#L1756) 规定: "... it must also enter the energy and its derivatives used for relaxation."
  - 改写: When an empirical dispersion correction is included, it also enters the energy and its derivatives used for relaxation.
  - 建议: 只把 must also enter 改为 also enters.
- [ ] [fundamentals_a.tex:1777](../../../src/fundamentals_a.tex#L1777) 否定: "... satisfying these stopping criteria does not establish convergence with respect to the plane-wave cutoff ..."
  - 改写: However, convergence with respect to the plane-wave cutoff and the sampling of reciprocal space is a separate requirement from these stopping criteria.
  - 建议: 下一句 We need to examine how these choices affect ... 只把 We need to examine 改为 We examine.
- [ ] [fundamentals_a.tex:1861](../../../src/fundamentals_a.tex#L1861) 否定: "The smooth auxiliary density alone is therefore not the reconstructed all-electron density."
  - 改写: The reconstructed all-electron density therefore consists of the smooth auxiliary density and the augmentation corrections.
- [ ] [fundamentals_a.tex:1863](../../../src/fundamentals_a.tex#L1863) 规定: "The datasets and their convergence settings must be specified for each calculation." 见 references/examples.md 的 B3.
  - 改写: The datasets and their convergence settings are specified for each calculation.
  - 建议: 只把 must be 改为 are.
- [ ] [fundamentals_a.tex:1883](../../../src/fundamentals_a.tex#L1883) 否定: "A high-symmetry path used to display a band structure does not replace this integration mesh."
  - 改写: A high-symmetry path used to display a band structure is separate from this integration mesh.
- [ ] [fundamentals_a.tex:1979](../../../src/fundamentals_a.tex#L1979) 规定: "Small imaginary frequencies require convergence checks before they can be attributed to numerical errors."
  - 改写: Small imaginary frequencies are attributed to numerical errors only after convergence checks.
- [ ] [fundamentals_a.tex:1980](../../../src/fundamentals_a.tex#L1980) 范围: "... within the wave vectors and numerical accuracy examined."
  - 改写: The absence of imaginary modes supports harmonic dynamical stability.
  - 建议: 只删去句尾的 within the wave vectors and numerical accuracy examined.
- [ ] [fundamentals_a.tex:2000](../../../src/fundamentals_a.tex#L2000) 规定: "... must therefore be specified with each calculation." 见 references/examples.md 的 B3.
  - 改写: The ensemble, temperature control, time step, and duration are therefore specified with each calculation.
  - 建议: 只把 must therefore be 改为 are therefore.
- [ ] [fundamentals_a.tex:2002](../../../src/fundamentals_a.tex#L2002) 否定: "Neither test alone establishes thermodynamic stability or experimental synthesizability."
  - 改写: Thermodynamic stability and experimental synthesizability are separate questions from these two tests.
- [ ] [fundamentals_a.tex:2058](../../../src/fundamentals_a.tex#L2058) 规定: "The normalization must be stated when reporting an energy difference, and the numerical uncertainty must be small ..."
  - 改写: A meaningful comparison states the normalization of the energy difference and keeps the numerical uncertainty small compared with that difference.
- [ ] [fundamentals_a.tex:2063](../../../src/fundamentals_a.tex#L2063) 否定: "A vanishing total spin moment alone does not distinguish an antiferromagnetic state from a non-magnetic state;"
  - 改写: The local spin density distinguishes the antiferromagnetic state from the non-magnetic state, as both have a vanishing total spin moment.
- [ ] [fundamentals_a.tex:2066](../../../src/fundamentals_a.tex#L2066) 否定: "... but does not by itself establish magnetic order at finite temperature."
  - 改写: The lowest-energy solution among the configurations examined identifies the preferred state within that set, while magnetic order at finite temperature requires a separate calculation.
  - 建议: 只改 but 之后的半句.
- [ ] [fundamentals_a.tex:2117](../../../src/fundamentals_a.tex#L2117) 规定: "For entangled bands, a subspace must first be selected within the chosen energy windows."
  - 改写: For entangled bands, we first select a subspace within the chosen energy windows.
- [ ] [fundamentals_a.tex:2138](../../../src/fundamentals_a.tex#L2138) 规定: "The interpolation must be checked against direct calculations in the energy range of interest."
  - 改写: A comparison with direct calculations in the energy range of interest validates the interpolation.
  - 建议: 不写成 We check ..., 因为第 6 章没有展示这项对比.
- [ ] [fundamentals_a.tex:2144](../../../src/fundamentals_a.tex#L2144) 否定: "Interpolating the band energies alone would not provide the coupling ..."
  - 改写: The coupling in equation~\eqref{electron_phonon_matrix_element_method} therefore requires the interpolated matrix elements in addition to the band energies.
- [ ] [fundamentals_a.tex:2220](../../../src/fundamentals_a.tex#L2220) 规定: "Its applicability must be checked for the system considered;"
  - 改写: 与分号后的半句合成一句: The expression applies when the denominator in the exponent, $\lambda-\mu^*(1+0.62\lambda)$, is positive.
- [ ] [fundamentals_a.tex:2221](../../../src/fundamentals_a.tex#L2221) 规定: "... it should not be extrapolated through a zero or negative denominator in the exponent."
  - 建议: 与上一条是同一句, 按上一条一并改写.
- [ ] [fundamentals_a.tex:2226](../../../src/fundamentals_a.tex#L2226) 否定: "The averaged function $\alpha^2F(\omega)$ alone does not retain the information required ..."
  - 建议: 删去. 第 2225 行已经写了 retains the band, momentum, and frequency dependence of the coupling instead of reducing it to these spectral averages.
- [ ] [fundamentals_a.tex:2232](../../../src/fundamentals_a.tex#L2232) 规定: "... must be identified with those results."
  - 改写: The electronic reference state, fine meshes, spectral integration, Coulomb pseudopotential, and form of the transition-temperature estimate are identified with those results.
  - 建议: 只把 must be 改为 are.

### 第 3 章

- [ ] [fundamentals_b.tex:232](../../../src/fundamentals_b.tex#L232) 范围: "Within the adopted independent-particle description, the spectra resolve ..."
  - 改写: The spectra resolve the interband onset, absorption peaks, and directional contrast.
  - 建议: 只删去句首的 Within the adopted independent-particle description. 下一句 The electron-hole interaction is not included in this approximation. 保留, 这里是全文定义这个近似的地方, 限制在这里说一次就够.
- [ ] [fundamentals_b.tex:256](../../../src/fundamentals_b.tex#L256) 否定: "Therefore, these spectra do not describe the complete low-frequency response of the metallic systems." 第 7 章第 350 行, 第 8 章第 196 行重复了同一限定.
  - 改写: Therefore, these spectra describe the interband part of the low-frequency response of the metallic systems.
- [ ] [fundamentals_b.tex:723](../../../src/fundamentals_b.tex#L723) 范围: "The resulting reflectivity is a parameter of this effective-medium model." 连同第 712 行.
  - 建议: 保留原句. 它本身是肯定句, 不属于防御性措辞.
- [ ] [fundamentals_b.tex:726](../../../src/fundamentals_b.tex#L726) 对比: "... a formal out-of-plane response of the scalar model, not a second normal-incidence channel of the layer."
  - 改写: The value obtained from $\varepsilon_{zz}(\omega)$ is therefore a formal out-of-plane response of the scalar model.
  - 建议: 只删去逗号后的 not a second normal-incidence channel of the layer.
- [ ] [fundamentals_b.tex:791](../../../src/fundamentals_b.tex#L791) 规定: "finite momentum and surface contributions require the appropriate scattering geometry."
  - 改写: This loss function describes the corresponding bulk response relevant to electron energy-loss spectroscopy. Finite momentum and surface contributions depend on the scattering geometry.
  - 建议: 分号改句号, require the appropriate 改为 depend on the.
- [ ] [fundamentals_b.tex:808](../../../src/fundamentals_b.tex#L808) 否定: "... so a peak alone does not establish a plasmon."
  - 改写: Interband excitations also contribute to the loss spectrum, so a plasmon assignment combines a loss peak with the zero of $\varepsilon_{1,\lambda\lambda}(\omega)$~\cite{dressel2002electrodynamics,onida2002electronic}.
- [ ] [fundamentals_b.tex:824](../../../src/fundamentals_b.tex#L824) 否定: "Therefore, a large imaginary part does not by itself produce a strong loss peak." 可改为 "A larger imaginary part therefore lowers the loss peak at the zero crossing."
  - 改写: Therefore, a larger imaginary part lowers the loss peak at the zero crossing.

### 第 4 章

- [ ] [fundamentals_c.tex:9](../../../src/fundamentals_c.tex#L9) 否定: "... information that is not specified by the band energies alone."
  - 改写: This connection carries information beyond the band energies.
- [ ] [fundamentals_c.tex:206](../../../src/fundamentals_c.tex#L206) 规定: "We must therefore specify the band count when assigning a topological index ..."
  - 改写: We therefore specify the band count when assigning a topological index to such a subspace.
  - 建议: 只去掉 must.
- [ ] [fundamentals_c.tex:210](../../../src/fundamentals_c.tex#L210) 图注: "... they are not calculated beryllene bands."
  - 改写: The model dispersions use arbitrary energy units and a dimensionless periodic coordinate $k$.
  - 建议: 只删去分号后的半句. 上一句和图注都已写明是 schematic.
- [ ] [fundamentals_c.tex:234](../../../src/fundamentals_c.tex#L234) 待定: "This isolation requires a separate check beyond the illustrated cuts."
  - 建议: 删去. 上一句的 provided the direct separation holds over the full two-dimensional Brillouin zone 已经给出条件.
- [ ] [fundamentals_c.tex:259](../../../src/fundamentals_c.tex#L259) 对比: "...; they are not two separate bands."
  - 改写: The two spin components belong to one electronic state.
  - 建议: 只删去分号后的半句.
- [ ] [fundamentals_c.tex:310](../../../src/fundamentals_c.tex#L310) 图注: "...; they contain no calculated parity eigenvalues."
  - 改写: The diagrams indicate wave-vector locations only.
  - 建议: 只删去分号后的半句, only 已经是这个意思.
- [ ] [fundamentals_c.tex:312](../../../src/fundamentals_c.tex#L312) 图注: "...; it does not indicate a parity or a topological class."
  - 改写: Each colour identifies one inequivalent TRIM and its periodic copies within a panel.
  - 建议: 只删去分号后的半句.
- [ ] [fundamentals_c.tex:376](../../../src/fundamentals_c.tex#L376) 对比: "... the transformation of the state, not the sign of its probability density ..."
  - 改写: This sign describes the transformation of the state. The probability density is unchanged in both cases.
- [ ] [fundamentals_c.tex:378](../../../src/fundamentals_c.tex#L378) 否定: "An arbitrary numerical basis of that eigenspace need not already have this form."
  - 改写: An arbitrary numerical basis of that eigenspace can mix these eigenstates.
- [ ] [fundamentals_c.tex:398](../../../src/fundamentals_c.tex#L398) 规定: "At a non-zero TRIM, it must be included when extracting ..."
  - 改写: At a non-zero TRIM, it enters the full Bloch-state parity extracted from a cell-periodic representation.
- [ ] [fundamentals_c.tex:415](../../../src/fundamentals_c.tex#L415) 规定: "... how parity eigenvalues must be counted in the topological criterion."
  - 改写: This result determines how parity eigenvalues are counted in the topological criterion.
  - 建议: 只把 must be 改为 are.
- [ ] [fundamentals_c.tex:448](../../../src/fundamentals_c.tex#L448) 否定: "This does not mean that the projector itself is discontinuous, or that all smooth choices of basis are forbidden."
  - 改写: The projector itself remains continuous, and smooth choices of basis still exist.
- [ ] [fundamentals_c.tex:457](../../../src/fundamentals_c.tex#L457) 否定: "This relation does not require a conserved spin component."
  - 改写: This relation holds even when spin-orbit coupling mixes the spin components.
- [ ] [fundamentals_c.tex:473](../../../src/fundamentals_c.tex#L473) 否定: "... it does not establish dissipationless transport in the presence of bulk conduction or inelastic processes."
  - 改写: The statement concerns a single edge within the one-electron description. Bulk conduction and inelastic processes can still dissipate the current.
- [ ] [fundamentals_c.tex:474](../../../src/fundamentals_c.tex#L474) 否定: "... cannot be inferred from a parity sign alone ..."
  - 改写: For a metallic filling, bulk states can remain at the Fermi level, so the insulating-edge interpretation requires more than the parity sign.
- [ ] [fundamentals_c.tex:491](../../../src/fundamentals_c.tex#L491) 否定: "energy ordering alone does not specify these partners."
  - 改写: If several pairs share the same energy, we resolve inversion within that eigenspace and pair its states by time reversal, as the energy ordering leaves these partners open.
- [ ] [fundamentals_c.tex:517](../../../src/fundamentals_c.tex#L517) 图注: "they are not parity results for a particular material."
  - 改写: These illustrative signs show that the index records an even or odd count.
  - 建议: 删去分号后的半句, why 改为 that.
- [ ] [fundamentals_c.tex:520](../../../src/fundamentals_c.tex#L520) 对比: "... an additional topological result, not a consequence of degeneracy counting."
  - 改写: Identifying the four-point product with $(-1)^\nu$ is an additional topological result.
  - 建议: 只删去逗号后的半句. 下一句 Fu and Kane derive this identification ... 给出了来源.
- [ ] [fundamentals_c.tex:523](../../../src/fundamentals_c.tex#L523) 否定: "it does not equate an arbitrary-loop single-band Berry phase with $\mathrm{\pi}\nu$."
  - 改写: The criterion evaluates the global time-reversal obstruction, which is distinct from a single-band Berry phase on an arbitrary loop.
- [ ] [fundamentals_c.tex:564](../../../src/fundamentals_c.tex#L564) 否定: "The equality of the final expressions does not make the two Brillouin zones equivalent."
  - 改写: 与下一句合成一句: The equality of the final expressions results from different symmetry relations among their four TRIM, and the two Brillouin zones remain inequivalent.
- [ ] [fundamentals_c.tex:569](../../../src/fundamentals_c.tex#L569) 否定: "A high-symmetry path alone does not justify the reduction."
  - 改写: The reduction follows from these symmetries, whatever high-symmetry path is plotted.
- [ ] [fundamentals_c.tex:587](../../../src/fundamentals_c.tex#L587) 否定: "The small atomic number of an element does not justify omitting spin-orbit coupling from this step:"
  - 改写: 第 587 至 588 行: We retain spin-orbit coupling even for a light element, since a small coupling may still affect a band crossing or a small separation relevant to the selected subspace.
- [ ] [fundamentals_c.tex:597](../../../src/fundamentals_c.tex#L597) 否定: "... the phrase ``occupied bands'' alone does not identify the subspace."
  - 改写: For a metal, the number of states below $E_\mathrm{F}$ can change with $\vec{k}$, so the phrase ``occupied bands'' leaves the subspace ambiguous.
- [ ] [fundamentals_c.tex:598](../../../src/fundamentals_c.tex#L598) 否定: "Numerical smearing of the occupations also does not define a fixed-rank projector."
  - 建议: 保留原句. 这是物理上的事实陈述, 不属于防御性措辞.
- [ ] [fundamentals_c.tex:599](../../../src/fundamentals_c.tex#L599) 规定: "The band count must instead refer to the selected spectral subspace at every wave vector."
  - 改写: The band count instead refers to the selected spectral subspace at every wave vector.
  - 建议: 只把 must instead refer 改为 instead refers.
- [ ] [fundamentals_c.tex:602](../../../src/fundamentals_c.tex#L602) 否定: "... does not establish the condition throughout that zone."
  - 改写: Its positivity at the four TRIM or along a plotted high-symmetry path covers only part of that zone.
- [ ] [fundamentals_c.tex:605](../../../src/fundamentals_c.tex#L605) 规定: "... its accuracy near those separations must be checked against direct calculations."
  - 改写: If interpolation is used, direct calculations near those separations verify its accuracy.
- [ ] [fundamentals_c.tex:606](../../../src/fundamentals_c.tex#L606) 规定: "A near-zero separation requires particular care ..."
  - 改写: A near-zero separation is refined further, because an unresolved touching point changes whether the chosen spectral subspace is isolated.
  - 建议: 只把 requires particular care 改为 is refined further.
- [ ] [fundamentals_c.tex:612](../../../src/fundamentals_c.tex#L612) 规定: "... the inversion representation must be resolved within that group ..."
  - 改写: For a degenerate group, we resolve the inversion representation within that group, which separates the parity eigenstates from an arbitrary numerical mixture.
- [ ] [fundamentals_c.tex:619](../../../src/fundamentals_c.tex#L619) 否定: "A parity product alone does not establish a $\mathbb{Z}_2$ invariant if ..."
  - 建议: 删去. 下一句 Once its isolation and symmetries have been established, the parity criterion classifies this subspace. 是同一内容的肯定表述.
- [ ] [fundamentals_c.tex:633](../../../src/fundamentals_c.tex#L633) 否定: "... cannot be applied without further justification."
  - 改写: If the selected and excluded bands touch, the isolation condition used throughout this chapter is absent, and applying this fixed-rank spectral-subspace argument requires further justification.
  - 建议: 只把 cannot be applied without further justification 改为肯定的说法.

### 第 5 章

- [ ] [project_1_main.tex:89](../../../src/project_1_main.tex#L89) 否定: "... the calculations do not establish the performance of a fabricated device."
  - 改写: These structure-property relationships provide the main contribution of this chapter, while the performance of a fabricated device lies outside its scope.
  - 建议: 只改分号后的半句.
- [ ] [project_1_main.tex:489](../../../src/project_1_main.tex#L489) 待定: "... their dispersion and lifetimes are not calculated here."
  - 建议: 保留原句的内容, 只把分号改成句号, 分成两句. 没有算色散和寿命是事实陈述.
- [ ] [project_1_main.tex:577](../../../src/project_1_main.tex#L577) 规定: "These near-zero values must be considered together with $\varepsilon_2$ and the energy-loss spectrum;"
  - 改写: 第 578 至 579 行: These near-zero values are considered together with $\varepsilon_2$ and the energy-loss spectrum, which together determine the reflectivity and a possible plasmon resonance.
- [ ] [project_1_main.tex:578](../../../src/project_1_main.tex#L578) 否定: "they do not alone determine the reflectivity or establish a plasmon resonance."
  - 建议: 与上一条是同一句, 按上一条一并改写.
- [ ] [project_1_main.tex:641](../../../src/project_1_main.tex#L641) 否定: "it need not coincide with the first maximum of $\varepsilon_2(\omega)$." 第 6 章第 790 行重复.
  - 改写: The absorption threshold is determined by the onset of optically allowed transitions and can differ from the first maximum of $\varepsilon_2(\omega)$.
- [ ] [project_1_main.tex:671](../../../src/project_1_main.tex#L671) 否定: "... the negative real part alone does not establish a plasmon resonance."
  - 改写: This assignment is consistent with the negative real part of the out-of-plane dielectric-function component, which is one of the conditions for a plasmon resonance.
  - 建议: 只改 although 之后的半句.
- [ ] [project_1_main.tex:709](../../../src/project_1_main.tex#L709) 规定: "Their optical transparency should be interpreted together with ... does not by itself guarantee weak attenuation."
  - 改写: Their optical transparency is interpreted together with the extinction coefficient and energy-loss spectrum, because attenuation can remain strong where the refractive index is close to or smaller than 1.

### 第 6 章

- [ ] [project_2_main.tex:28](../../../src/project_2_main.tex#L28) 待定: 本章摘要中的 "... small imaginary phonon frequencies near $\Gamma$ require further convergence checks."
  - 改写: The hydrogen-terminated bilayer also retains its bonding framework during a finite-temperature simulation, although it shows small imaginary phonon frequencies near $\Gamma$.
  - 建议: 小虚频这个事实保留, 只去掉 require further convergence checks.
- [ ] [project_2_main.tex:316](../../../src/project_2_main.tex#L316) 对比: "The latter broadening is a numerical parameter, rather than a fitted carrier scattering rate."
  - 改写: The latter broadening is a numerical parameter.
  - 建议: 只删去 rather than 之后的半句.
- [ ] [project_2_main.tex:350](../../../src/project_2_main.tex#L350) 规定: "... this rescaling should not be identified with a unique intrinsic out-of-plane dielectric constant."
  - 改写: For perpendicular polarization, the electrostatic boundary condition differs from the in-plane case, so this rescaling gives an effective quantity of the chosen convention.
  - 建议: 只改 so 之后的半句.
- [ ] [project_2_main.tex:427](../../../src/project_2_main.tex#L427) 否定: "This positive difference does not establish o-\ce{B14} as the thermodynamic ground-state phase."
  - 改写: This positive difference places o-\ce{B14} above $\alpha$-\ce{B12} in energy.
- [ ] [project_2_main.tex:543](../../../src/project_2_main.tex#L543) 待定: "... their numerical origin has not been established by the present calculations."
  - 建议: 保留原句. 这里是正文交代小虚频的地方, 来源没有确定是事实陈述.
- [ ] [project_2_main.tex:551](../../../src/project_2_main.tex#L551) 否定: "... it does not establish thermodynamic stability against all competing phases or experimental synthesizability."
  - 改写: Thermodynamic stability against all competing phases and experimental synthesizability remain separate questions.
- [ ] [project_2_main.tex:588](../../../src/project_2_main.tex#L588) 否定: "... and does not determine a finite-temperature magnetic ordering temperature."
  - 改写: This small difference is a zero-temperature energy comparison, and the magnetic ordering temperature requires a separate calculation.
  - 建议: 只改 and 之后的半句.
- [ ] [project_2_main.tex:630](../../../src/project_2_main.tex#L630) 对比: "... a possible interpretation of the calculated HSE06 ordering, rather than an independent determination ..."
  - 改写: This provides a possible interpretation of the calculated HSE06 ordering.
  - 建议: 只删去 rather than 之后的半句.
- [ ] [project_2_main.tex:654](../../../src/project_2_main.tex#L654) 否定: "neither result alone establishes the experimental gap."
  - 改写: The difference is therefore sensitive to the exchange-correlation approximation, and both values are theoretical estimates of the gap.
  - 建议: 只改分号后的半句.
- [ ] [project_2_main.tex:689](../../../src/project_2_main.tex#L689) 否定: "A larger $\lambda$ does not necessarily imply a higher $T_\mathrm{c}$, since ..."
  - 改写: A larger $\lambda$ can accompany a lower $T_\mathrm{c}$, since the phonon frequency scale also enters the Allen--Dynes estimate~\cite{migdal1958interaction,marsiglio2020eliashberg,eliashberg1960interactions}.
  - 建议: 只把 does not necessarily imply a higher 改为 can accompany a lower.
- [ ] [project_2_main.tex:693](../../../src/project_2_main.tex#L693) 否定: "This result does not determine superconductivity in the gapped antiferromagnetic HSE06 state."
  - 改写: This result refers to the non-magnetic PBE reference state, separate from the gapped antiferromagnetic HSE06 state.
- [ ] [project_2_main.tex:713](../../../src/project_2_main.tex#L713) 范围: "... within the stated electronic and vibrational approximations."
  - 建议: 只删去句末的 within the stated electronic and vibrational approximations.
- [ ] [project_2_main.tex:712](../../../src/project_2_main.tex#L712) 待定: "... remain a limitation of the stability assessment."
  - 改写: For the hydrogen-terminated bilayer, the small imaginary phonon frequencies discussed in section~\ref{xene_ob14_phonon_dispersion} limit the stability assessment.
  - 建议: 只把 remain a limitation of 改为 limit.
- [ ] [project_2_main.tex:714](../../../src/project_2_main.tex#L714) 规定: "The Allen--Dynes and anisotropic Migdal--Eliashberg estimates should be compared separately."
  - 改写: The Allen--Dynes and anisotropic Migdal--Eliashberg estimates are separate results.
- [ ] [project_2_main.tex:760](../../../src/project_2_main.tex#L760) 否定: "... this response does not by itself determine the free-carrier scattering rate or the dc limit."
  - 改写: Since no separately parameterized Drude term is added, the free-carrier scattering rate and the dc limit lie outside this response.
- [ ] [project_2_main.tex:764](../../../src/project_2_main.tex#L764) 否定: "small band overlap does not require strong optical transitions in every polarization."
  - 改写: The bilayer, on the other hand, has a small $\varepsilon_{2}(\omega)$ at low energy despite its PBE semimetallic band structure, as a small band overlap can coexist with weak optical transitions.
  - 建议: 只改分号后的半句.
- [ ] [project_2_main.tex:790](../../../src/project_2_main.tex#L790) 否定: "The absorption onset need not coincide with the first maximum of $\varepsilon_{2}(\omega)$."
  - 改写: The absorption onset can differ from the first maximum of $\varepsilon_{2}(\omega)$.
- [ ] [project_2_main.tex:798](../../../src/project_2_main.tex#L798) 规定: "A quantitative comparison requires consistent absorption units and ..."
  - 建议: 保留原句. 它是肯定句, 说的是比较的条件, 不属于防御性措辞.
- [ ] [project_2_main.tex:801](../../../src/project_2_main.tex#L801) 否定: "A negative $\varepsilon_1$ alone does not establish a plasmon resonance:"
  - 改写: 第 803 至 805 行: Beyond a negative $\varepsilon_1$, a loss maximum close to a zero crossing of $\varepsilon_1$, with sufficiently small $\varepsilon_2$, provides the optical-limit signature of a plasmon resonance.
- [ ] [project_2_main.tex:804](../../../src/project_2_main.tex#L804) 待定: "A wave-vector-dependent response would be required to establish the dispersion ..."
  - 改写: A wave-vector-dependent response would give the dispersion of a propagating two-dimensional plasmon.
  - 建议: 只把 would be required to establish 改为 would give.
- [ ] [project_2_main.tex:811](../../../src/project_2_main.tex#L811) 否定: "The negative-$\varepsilon_1$ intervals and the loss maxima need not have identical boundaries."
  - 改写: The negative-$\varepsilon_1$ intervals and the loss maxima can have different boundaries.
- [ ] [project_2_main.tex:850](../../../src/project_2_main.tex#L850) 否定: "... do not independently distinguish a plasmon from an interband transition."
  - 改写: These features follow from the same dielectric function, so they repeat the evidence of the loss spectrum for the plasmon assignment.
- [ ] [project_2_main.tex:877](../../../src/project_2_main.tex#L877) 对比: "These comparisons concern the calculated cohesive energies rather than a complete thermodynamic phase diagram."
  - 改写: These comparisons concern the calculated cohesive energies.
  - 建议: 只删去 rather than 之后的半句.
- [ ] [project_2_main.tex:886](../../../src/project_2_main.tex#L886) 待定: "Their plasmonic interpretation remains subject to damping and the effective-medium treatment of the layers."
  - 改写: Their plasmonic interpretation depends on the damping and the effective-medium treatment of the layers.
  - 建议: 只把 remains subject to 改为 depends on the.
- [ ] [project_2_SI.tex:140](../../../src/project_2_SI.tex#L140) 待定: 图 S2.9 图注中的 "further checks are required to distinguish this possibility from a physical instability."
  - 改写: Such modes can be sensitive to numerical convergence in two-dimensional materials~\cite{liu2016continuum,querne2023crystal,pallikara2022physical}, and a physical instability is the alternative explanation.

### 第 7 章

- [ ] [project_3_main.tex:25](../../../src/project_3_main.tex#L25) 范围: 本章摘要中的 "... under the stated effective-thickness convention."
  - 建议: 只删去句末的 under the stated effective-thickness convention.
- [ ] [project_3_main.tex:333](../../../src/project_3_main.tex#L333) 对比: "... provide scalar comparisons rather than optical constants obtained from the full dielectric tensor."
  - 改写: The off-diagonal coupling in monoclinic 1H-$\beta$-beryllene and 2H-$\beta$-beryllene is not included in the derived spectra, which therefore provide scalar comparisons.
  - 建议: 只删去 rather than 之后的半句.
- [ ] [project_3_main.tex:335](../../../src/project_3_main.tex#L335) 否定: "... which need not equal the corresponding component of the inverse tensor."
  - 改写: In particular, $L_{\lambda}(\omega)$ uses the inverse of $\varepsilon_{\lambda\lambda}(\omega)$, which can differ from the corresponding component of the inverse tensor.
  - 建议: 只把 need not equal 改为 can differ from.
- [ ] [project_3_main.tex:338](../../../src/project_3_main.tex#L338) 对比: "... not the full reflection of a finite anisotropic layer on a substrate."
  - 改写: The reflectivity describes a homogeneous semi-infinite medium in the scalar normal-incidence approximation.
  - 建议: 只删去逗号后的半句. 有限厚度和衬底的影响第 3 章已经说过.
- [ ] [project_3_main.tex:350](../../../src/project_3_main.tex#L350) 否定: "They therefore do not describe the complete low-frequency response of these metallic systems."
  - 改写: They therefore describe the interband part of the low-frequency response of these metallic systems.
- [ ] [project_3_main.tex:509](../../../src/project_3_main.tex#L509) 待定: "... but the dynamical stability near $\Gamma$ remains to be established."
  - 改写: This behaviour is consistent with limitations of the finite-supercell force constants at long wavelengths.
  - 建议: 只删去 but 之后的半句. 本章结论里对 1H-$\beta$ 还会说一次.
- [ ] [project_3_main.tex:528](../../../src/project_3_main.tex#L528) 待定: "... so the full anharmonic stability of 2H-$\beta$-beryllene remains to be established."
  - 改写: Coupling to the other modes is not included, so the full anharmonic stability of 2H-$\beta$-beryllene depends on this coupling.
  - 建议: 前半句是事实, 保留. 只改 so 之后的半句.
- [ ] [project_3_main.tex:624](../../../src/project_3_main.tex#L624) 待定: "... but this barrier has not been calculated."
  - 建议: 保留原句. 势垒没有算是事实陈述, 不属于防御性措辞.
- [ ] [project_3_main.tex:626](../../../src/project_3_main.tex#L626) 否定: "... so this comparison does not replace a global structure search."
  - 改写: Only these two square configurations are considered, so this comparison is narrower than a global structure search~\cite{li2018global}.
  - 建议: 只把 does not replace 改为 is narrower than.
- [ ] [project_3_main.tex:784](../../../src/project_3_main.tex#L784) 对比: "... rather than a quantum spin Hall state at the Fermi level." 含义要保留, 只改句式.
  - 改写: The index then describes a band inversion within this subspace, while the states at the Fermi level remain metallic.
  - 建议: 只改 rather than 之后的半句, 含义不变.
- [ ] [project_3_main.tex:788](../../../src/project_3_main.tex#L788) 范围: "... the resulting $\mathbb{Z}_2$ indices are conditional screening results." 第 919, 926, 1270 行重复了同一限定, 保留一处.
  - 改写: Since these gaps are sampled on a finite mesh, and since the analysis assumes time-reversal symmetry, the resulting $\mathbb{Z}_2$ indices are conditional screening results.
  - 建议: 只把 sampled rather than proven on the continuous Brillouin zone 改为 sampled on a finite mesh.
- [ ] [project_3_main.tex:919](../../../src/project_3_main.tex#L919) 范围: "... in the same conditional sense as $\alpha$-beryllene."
  - 建议: 保留原句. in the same conditional sense 把这里的结论与前面定义的 conditional 联系起来, 是有内容的限定.
- [ ] [project_3_main.tex:926](../../../src/project_3_main.tex#L926) 对比: "... a band inversion rather than a quantum spin Hall insulating state." 与第 784 行重复.
  - 建议: 保留原句. 这是物理上的区分, 也是对审稿人 1 的直接回答, 全文在这里明说一次.
- [ ] [project_3_main.tex:929](../../../src/project_3_main.tex#L929) 待定: "... has not been established separately from the local refinement of their minima."
  - 建议: 保留原句. 没有单独做收敛测试是事实陈述, 正文里只在这里说一次.
- [ ] [project_3_main.tex:945](../../../src/project_3_main.tex#L945) 否定: "... but does not establish isolation of the corresponding subspaces throughout the Brillouin zone ..."
  - 改写: This check tests the band order at the time-reversal invariant momenta, and the isolation of the corresponding subspaces throughout the Brillouin zone with HSE06 and spin-orbit coupling is a separate test.
- [ ] [project_3_main.tex:1014](../../../src/project_3_main.tex#L1014) 对比: "these are sampled endpoints rather than interpolated zeros."
  - 改写: On the calculated grid, these components have opposite signs from approximately \qtyrange{1.22}{2.21}{\electronvolt}.
  - 建议: 只删去分号后的半句. On the calculated grid 和 approximately 已经说明端点是采样值.
- [ ] [project_3_main.tex:1017](../../../src/project_3_main.tex#L1017) 否定: "They do not by themselves establish propagating modes ..." 见 references/examples.md 的 B1.
  - 改写: Establishing propagating modes in a finite two-dimensional layer and their lifetimes belongs to that further analysis.
- [ ] [project_3_main.tex:1018](../../../src/project_3_main.tex#L1018) 对比: "The numerical broadening is an input to the calculation, not a calculated scattering lifetime."
  - 改写: The numerical broadening is an input to the calculation.
  - 建议: 只删去逗号后的半句.
- [ ] [project_3_main.tex:1035](../../../src/project_3_main.tex#L1035) 否定: "... the larger maxima do not imply that $\beta$-beryllene absorbs more strongly at every energy."
  - 改写: The spectra cross at some energies, so $\beta$-beryllene absorbs more strongly only over part of the energy range.
- [ ] [project_3_main.tex:1048](../../../src/project_3_main.tex#L1048) 否定: "... do not by themselves identify a plasmon resonance."
  - 改写: These crossings describe dispersion of the effective optical constants, and a plasmon assignment requires the loss spectrum as well.
- [ ] [project_3_main.tex:1093](../../../src/project_3_main.tex#L1093) 对比: "this boundary value is not a resolved peak."
  - 改写: It reaches approximately 1.50 at the last available sample near \qty{11.98}{\electronvolt} while still rising.
  - 建议: 只删去分号后的半句, while still rising 已经是这个意思.
- [ ] [project_3_main.tex:1096](../../../src/project_3_main.tex#L1096) 范围: "These spectra describe the inverse dielectric response under the stated effective-thickness convention."
  - 建议: 整句删去. 方法部分已经说明有效厚度约定.
- [ ] [project_3_main.tex:1138](../../../src/project_3_main.tex#L1138) 范围: "Under the stated effective-thickness convention, trilayer cubic beryllene does not show a universal absorption enhancement ..."
  - 改写: Trilayer cubic beryllene shows an absorption enhancement relative to bulk bcc beryllium only in some directions and energy ranges.
- [ ] [project_3_main.tex:1146](../../../src/project_3_main.tex#L1146) 对比: "... rather than enhanced absorption throughout the visible and near-ultraviolet regions."
  - 改写: These results show a redistribution of the effective interband response.
  - 建议: 只删去 rather than 之后的半句. 具体的强弱前面已经逐项给出.
- [ ] [project_3_main.tex:1150](../../../src/project_3_main.tex#L1150) 否定: "...; they do not alone establish propagating plasmon modes."
  - 改写: The scalar loss features identify variations in the inverse dielectric response, and propagating plasmon modes require a separate analysis.
- [ ] [project_3_main.tex:1181](../../../src/project_3_main.tex#L1181) 对比: "... not a thickness-independent measure of oscillator strength."
  - 改写: Changes in peak height therefore describe an effective response under that convention.
  - 建议: 只删去逗号后的半句.
- [ ] [project_3_main.tex:1191](../../../src/project_3_main.tex#L1191) 否定: "... it does not produce a common peak energy, a common zero crossing, or a monotonic enhancement ..."
  - 改写: Thus, increasing hydrogen coverage changes the spectral distribution and in-plane anisotropy, and the peak energies, zero crossings, and enhancements differ between components.
- [ ] [project_3_main.tex:1192](../../../src/project_3_main.tex#L1192) 规定: "The imaginary dielectric peaks should also be distinguished from maxima of the derived absorption coefficient."
  - 改写: The imaginary dielectric peaks also differ from maxima of the derived absorption coefficient.
- [ ] [project_3_main.tex:1214](../../../src/project_3_main.tex#L1214) 对比: "... are not evidence of a sharply defined absorption onset or strong visible absorption."
  - 改写: These results establish changes in the calculated interband and inverse dielectric response. The weak low-energy tails arise from the finite numerical broadening.
- [ ] [project_3_main.tex:1232](../../../src/project_3_main.tex#L1232) 否定: "The comparisons depend on the stated thickness convention and do not include a Drude intraband contribution."
  - 建议: 删去. 方法部分已经说明.
- [ ] [project_3_main.tex:1244](../../../src/project_3_main.tex#L1244) 待定: "... leave the long-wavelength stability of 1H-$\beta$-beryllene unresolved."
  - 建议: 保留原句. 这是本章结论里对 1H-$\beta$ 的如实交代, 不属于防御性措辞.
- [ ] [project_3_main.tex:1248](../../../src/project_3_main.tex#L1248) 待定: "The full anharmonic stability requires further examination of coupling between modes."
  - 改写: The full anharmonic stability depends on the coupling between modes.
- [ ] [project_3_main.tex:1265](../../../src/project_3_main.tex#L1265) 范围: "... under the stated effective-thickness convention and exclude a Drude intraband contribution."
  - 改写: These comparisons use the Cartesian diagonal dielectric components and exclude a Drude intraband contribution.
  - 建议: 只删去 under the stated effective-thickness convention.
- [ ] [project_3_main.tex:1270](../../../src/project_3_main.tex#L1270) 范围: "... these indices are conditional screening results for band inversions rather than quantum spin Hall states."
  - 改写: Since the non-trivial subspaces of these metallic phases are isolated only by spin-orbit gaps of approximately \qty{1}{\milli\electronvolt} above the Fermi level, these indices are conditional screening results for band inversions.
  - 建议: 只删去句末的 rather than quantum spin Hall states. 这一区分在正文第 927 行已经明说.
- [ ] [project_3_SI.tex:67](../../../src/project_3_SI.tex#L67) 对比: "... and is not a unique physical layer thickness."
  - 改写: Consequently, the assigned 2H-$\alpha$ thickness is smaller than the pristine value, which is a consequence of the chosen convention.
- [ ] [project_3_SI.tex:84](../../../src/project_3_SI.tex#L84) 否定: "These comparisons do not establish convergence of the complete low-frequency metallic response ..."
  - 改写: These comparisons test the convergence of the interband response, and the complete low-frequency metallic response would also require an intraband treatment.
- [ ] [project_3_SI.tex:86](../../../src/project_3_SI.tex#L86) 对比: "... a final-parameter reference rather than an additional strictly one-parameter convergence point."
  - 改写: The selected reference may change both the k-point grid and the total band count relative to a convergence series, as it is a final-parameter reference.
- [ ] [project_3_SI.tex:265](../../../src/project_3_SI.tex#L265) 对比: "... rather than replacing a full anharmonic phonon calculation."
  - 改写: The coupling to the other phonon modes is neglected, so these values indicate the size of the quantum fluctuations.
  - 建议: 只删去 rather than 之后的半句.
- [ ] [project_3_SI.tex:380](../../../src/project_3_SI.tex#L380) 待定: "The dynamical stability of the puckered square layer is not calculated."
  - 建议: 保留原句. 没有算是事实陈述.
- [ ] [project_3_SI.tex:419](../../../src/project_3_SI.tex#L419) 待定: "... has not been tested separately from the total-energy convergence."
  - 建议: 保留原句的内容, 只把分号改成句号, 分成两句.
- [ ] [project_3_SI.tex:429](../../../src/project_3_SI.tex#L429) 否定: "... but does not establish that the lowest-$N$ spinor subspaces remain isolated ..."
  - 改写: This comparison checks the parity ordering at these momenta, and the isolation of the lowest-$N$ spinor subspaces throughout the Brillouin zone with HSE06 and spin-orbit coupling is a separate test.
- [ ] [project_3_SI.tex:473](../../../src/project_3_SI.tex#L473) 对比: "... conditional PBE results with spin-orbit coupling, not independently determined HSE06 indices."
  - 改写: The listed $\mathbb{Z}_2$ indices are conditional PBE results with spin-orbit coupling.
  - 建议: 只删去逗号后的半句.

### 第 8 章

结论正文和 Connections 一节中的句子:

- [ ] [conclusion.tex:27](../../../src/conclusion.tex#L27) 否定: "... but these local separations do not establish an insulating gap for the complete bilayer."
  - 改写: Interlayer coupling opens local gaps of approximately \qty{50}{\milli\electronvolt} in Graphene-\ce{BC3} and \qty{20}{\milli\electronvolt} in Graphene-\ce{B4C3} at this point, while both bilayers remain semimetallic.
  - 建议: 只把 but 之后的半句换成 while both bilayers remain semimetallic, 与摘要的说法一致.
- [ ] [conclusion.tex:38](../../../src/conclusion.tex#L38) 否定: "...; this comparison does not imply stronger absorption over the whole spectrum."
  - 改写: Graphene-Borophene has the stronger absorption near the low-energy rise around \qty{1}{\electronvolt}.
  - 建议: 只删去分号后的半句. around 1 eV 已经限定了范围.
- [ ] [conclusion.tex:51](../../../src/conclusion.tex#L51) 否定: "... these two operations need not produce the same trend."
  - 改写: The resulting electronic structures show that these two operations produce different trends.
- [ ] [conclusion.tex:63](../../../src/conclusion.tex#L63) 否定: "This comparison illustrates why the coupling constant alone does not determine $T_{\mathrm{c}}$." 见 references/examples.md 的 B2.
  - 改写: This comparison illustrates that $T_{\mathrm{c}}$ depends on more than the coupling constant.
- [ ] [conclusion.tex:69](../../../src/conclusion.tex#L69) 待定: "... whose origin remains unresolved."
  - 改写: The hydrogen-terminated monolayer develops a clear harmonic instability, while the terminated bilayer retains small imaginary frequencies near $\Gamma$.
  - 建议: 只删去句末的 whose origin remains unresolved. 这一点放在 Limitations 一节说.
- [ ] [conclusion.tex:75](../../../src/conclusion.tex#L75) 否定: "... cannot describe the HSE06 antiferromagnetic semiconductor without a further calculation."
  - 改写: Consequently, these spectra characterize that reference, and the HSE06 antiferromagnetic semiconductor requires a further calculation.
  - 建议: 只改 and 之后的半句.
- [ ] [conclusion.tex:89](../../../src/conclusion.tex#L89) 对比: "... candidate two-dimensional structures rather than the thermodynamic ground state of elemental beryllium."
  - 改写: They therefore represent candidate two-dimensional structures.
  - 建议: 只删去 rather than 之后的半句. 上一句已经说了内聚能不如 bulk hcp beryllium.
- [ ] [conclusion.tex:91](../../../src/conclusion.tex#L91) 待定: "... the long-wavelength flexural behaviour remains unresolved:"
  - 建议: 保留原句的内容. 这是如实交代, 只需把冒号换掉: For 1H-$\beta$-beryllene, the long-wavelength flexural behaviour remains unresolved, as the sampled commensurate modes are real, but the interpolated branch develops imaginary frequencies near $\Gamma$.
- [ ] [conclusion.tex:92](../../../src/conclusion.tex#L92) 否定: "... this instability cannot be dismissed solely as an interpolation effect."
  - 改写: The 2H-$\beta$ structure has a soft mode at a commensurate wave vector, so this instability appears in the directly calculated frequencies.
- [ ] [conclusion.tex:96](../../../src/conclusion.tex#L96) 否定: "... explains why the classical minimum alone does not determine the distortion in this model:"
  - 改写: 第 96 至 97 行: In this model, the comparison of these energy scales shows that quantum motion extends across the shallow wells, beyond the classical minimum.
- [ ] [conclusion.tex:97](../../../src/conclusion.tex#L97) 待定: "... while leaving coupling to the other modes unresolved."
  - 改写: This supports suppression of a static distortion along the selected coordinate.
  - 建议: 只删去 while 之后的半句.
- [ ] [conclusion.tex:103](../../../src/conclusion.tex#L103) 范围: "... within the adopted thermodynamic treatment."
  - 改写: Thus, only 2H-$\alpha$-beryllene favours adsorption under these conditions.
  - 建议: 只删去句末的 within the adopted thermodynamic treatment.
- [ ] [conclusion.tex:104](../../../src/conclusion.tex#L104) 否定: "This comparison does not establish formation from bulk beryllium."
  - 改写: Formation from bulk beryllium is a separate comparison.
- [ ] [conclusion.tex:106](../../../src/conclusion.tex#L106) 待定: "Its phonon stability and the reconstruction barrier remain uncalculated."
  - 建议: 保留原句. 没有算是事实陈述.
- [ ] [conclusion.tex:113](../../../src/conclusion.tex#L113) 对比: "... rather than assign a universal electronic effect to hydrogenation."
  - 改写: This difference reinforces the need to follow the actual bonding geometry.
  - 建议: 只删去 rather than 之后的半句.
- [ ] [conclusion.tex:119](../../../src/conclusion.tex#L119) 否定: "... without establishing quantum spin Hall insulators at neutral filling."
  - 改写: These results therefore identify conditional non-trivial subspaces in structures that remain metallic at neutral filling.
- [ ] [conclusion.tex:120](../../../src/conclusion.tex#L120) 规定: "... these fixed subspaces must again be distinguished from an occupied insulating manifold."
  - 改写: The selected subspaces of $\beta$-beryllene and the hydrogenated structures give trivial indices, and for metallic systems these fixed subspaces again differ from an occupied insulating manifold.
- [ ] [conclusion.tex:122](../../../src/conclusion.tex#L122) 否定: "... changes that the metallic or semiconducting classification alone cannot describe."
  - 改写: The optical response resolves changes beyond the metallic or semiconducting classification.
- [ ] [conclusion.tex:126](../../../src/conclusion.tex#L126) 否定: "... does not establish strong visible absorption across its wide electronic gap."
  - 改写: For 2H-$\alpha$-beryllene, the response below the main absorption region is weak and broadened, consistent with its wide electronic gap.
- [ ] [conclusion.tex:135](../../../src/conclusion.tex#L135) 对比: "... rather than to the label of a light-element material alone."
  - 改写: The calculated properties respond to these particular changes.
  - 建议: 只删去 rather than 之后的半句.
- [ ] [conclusion.tex:155](../../../src/conclusion.tex#L155) 否定: "... explain why the electronic results do not follow one trend with thickness or hydrogen coverage."
  - 改写: These microscopic comparisons explain why the electronic results follow different trends with thickness and hydrogen coverage.
  - 建议: 只把 do not follow one trend 改为 follow different trends.
- [ ] [conclusion.tex:160](../../../src/conclusion.tex#L160) 规定: "... we must also distinguish their local separations from the electronic character of the complete system."
  - 改写: Once we inspect the resulting bands, we also distinguish their local separations from the electronic character of the complete system.
  - 建议: 只去掉 must.
- [ ] [conclusion.tex:168](../../../src/conclusion.tex#L168) 否定: "... the distinction between a metal and a semiconductor does not determine an entire optical spectrum."
  - 改写: The dielectric response depends on the available transitions and their polarization-dependent matrix elements, so the optical spectrum contains more than the distinction between a metal and a semiconductor.
- [ ] [conclusion.tex:174](../../../src/conclusion.tex#L174) 规定: "Finally, the structural and electronic descriptions must refer to the same physical state."
  - 改写: Finally, a consistent conclusion requires the structural and electronic descriptions to refer to the same physical state.
- [ ] [conclusion.tex:175](../../../src/conclusion.tex#L175) 否定: "An optical spectrum of a non-magnetic reference cannot inherit the gap of a different antiferromagnetic calculation."
  - 改写: An optical spectrum of a non-magnetic reference describes that reference, separate from the gap of an antiferromagnetic calculation.

Limitations 一节 (第 184 至 228 行) 本来就是写限制的地方:

- [ ] [conclusion.tex:194](../../../src/conclusion.tex#L194) Limitations 一节, 第 194 至 228 行.
  - 建议: 这一节是全文集中写限制的地方, 审稿人也要求在结论里更明确地讨论局限. 这里的否定句大多可以保留原样, 不必逐句改成肯定句. 值得动的只有下面四处.
  - 改写: 第 199 行: Their low-frequency response therefore contains the interband part only.
  - 改写: 第 206 行: 只删去句中的 rather than to the material.
  - 改写: 第 209 行: 只删去逗号后的 rather than a supported atomically thin film.
  - 改写: 第 226 至 227 行合成一句: Finally, graphene, boron sheets, and a beryllium sheet have been prepared experimentally, whereas the particular boron frameworks, hydrogen arrangements, and cubic beryllene trilayer considered here remain theoretical models.
  - 建议: 最后这一句直接回应审稿人 2 的要求: 区分已有实验的体系和纯理论预言.

Outlook 一节中的句子:

- [ ] [conclusion.tex:240](../../../src/conclusion.tex#L240) 对比: "... the starting point for this calculation, rather than its final criterion."
  - 改写: The absence of a static distortion along one coordinate is the starting point for this calculation.
  - 建议: 只删去 rather than 之后的半句.
- [ ] [conclusion.tex:244](../../../src/conclusion.tex#L244) 待定: "... first requires a phonon calculation before its lower electronic energy can support a stronger stability conclusion."
  - 改写: A phonon calculation of the puckered square-layer \ce{BeH2} candidate would test whether its lower electronic energy corresponds to a stable structure.
- [ ] [conclusion.tex:255](../../../src/conclusion.tex#L255) 否定: "... determining the amount of hydrogen alone would leave its adsorption arrangement and the underlying lattice unresolved."
  - 改写: For a hydrogenated sheet, the structural test resolves the adsorption arrangement and the underlying lattice in addition to the hydrogen content.
- [ ] [conclusion.tex:296](../../../src/conclusion.tex#L296) 对比: "... rather than an idealized bulk-like coefficient."
  - 改写: A film calculation with a selected substrate, incidence angle, and polarization could then predict measured absorption or reflection.
  - 建议: 只删去 rather than 之后的半句.
- [ ] [conclusion.tex:301](../../../src/conclusion.tex#L301) 规定: "... although the film calculation must still account for its interaction with the sheet."
  - 改写: Measuring the support under the same conditions would help separate its contribution, while the film calculation accounts for its interaction with the sheet.
- [ ] [conclusion.tex:308](../../../src/conclusion.tex#L308) 规定: "... should therefore precede a stronger topological claim ..."
  - 建议: 保留原句. Outlook 里写下一步该做什么是正常的.
- [ ] [conclusion.tex:313](../../../src/conclusion.tex#L313) 规定: "Carrier control, strain, or a substrate should therefore be assessed for a specific purpose:"
  - 改写: Carrier control, strain, or a substrate would therefore be assessed by whether it can produce an accessible insulating energy interval while preserving the required symmetry and band separation.
- [ ] [conclusion.tex:314](../../../src/conclusion.tex#L314) 否定: "We cannot assume that moving the chemical potential alone removes an indirect overlap ..."
  - 改写: Whether moving the chemical potential alone removes an indirect overlap or makes the small gaps robust is part of this assessment.
- [ ] [conclusion.tex:315](../../../src/conclusion.tex#L315) 规定: "Transport predictions should follow these checks rather than follow directly from the parity product."
  - 改写: Transport predictions then build on these checks in addition to the parity product.
- [ ] [conclusion.tex:318](../../../src/conclusion.tex#L318) 否定: "... an edge spectral feature alone would not determine its topological origin."
  - 改写: Such a comparison would also need the edge geometry and the remaining bulk states, since they are needed to determine the topological origin of an edge spectral feature.
- [ ] [conclusion.tex:324](../../../src/conclusion.tex#L324) 否定: "... do not establish either situation in the materials studied here." 所在的 anyon 段落建议整段删去.
  - 建议: 保留原句. 这是防止过度解读的如实说明.

### 附录 C

- [ ] [appendix_topology.tex:294](../../../src/appendix_topology.tex#L294) 图注: "The pointers therefore describe phase choices, rather than spin directions or real-space vectors."
  - 改写: The pointers therefore describe phase choices.
  - 建议: 只删去 rather than 之后的半句.
- [ ] [appendix_topology.tex:312](../../../src/appendix_topology.tex#L312) 否定: "... a Berry phase on an arbitrary loop is not by itself the two-dimensional $\mathbb{Z}_2$ index."
  - 改写: 第 312 至 314 行合成两句: The phase $\gamma_n(C)$ takes general values modulo $2\mathrm{\pi}$. The two-dimensional $\mathbb{Z}_2$ index requires additional structure from time-reversal symmetry and the full selected band subspace.
  - 建议: 这是物理上的区分, 内容保留. 第 4 章里同样的话已建议删去, 以这里为准.
- [ ] [appendix_topology.tex:603](../../../src/appendix_topology.tex#L603) 图注: "The plane represents a subspace of states, rather than an energy band or a plane in the crystal;" 连同第 604 行.
  - 改写: The plane represents a subspace of states, and the actual Bloch states belong to a complex Hilbert space of general dimension.
- [ ] [appendix_topology.tex:672](../../../src/appendix_topology.tex#L672) 对比: "They are not two separate occupied bands."
  - 建议: 删去. 上一句已经说明两个空间分量构成一个旋量态.
