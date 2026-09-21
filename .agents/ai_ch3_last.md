# Chapter 3 修改操作稿

日期: 2026-09-21.
依据: [Gemini 初稿](ai_ch3_first.md), [修改流程](ai.md), 两份原始 examiner reports,
当前论文、源文件与六组图, 以及 Project 3 归档的绘图程序、原始介电数组与结构文件.

本稿取代此前仅澄清来源的版本.
按你的最新要求: 只有明显重复才缩, 不设删减页数或字数目标.
保留章节顺序、原有推导环节、六幅例图和全部原 label.
不移入附录, 不增加独立理论小节, 不逐个光学量重复扩写研究动机.
必要的物理修正与文字压缩分别记录.

本轮仅交付方案, 尚未修改论文源文件、正式图件、文献库、Gemini 初稿或回复信.
下文行号对应本次读取的源文件, 实施时结合原句及 label 定位.

## 1. 来源已经确认, 评审要求分别回应

### 1.1 两套版式共用同一组计算数据

你的记忆正确: 两章使用不同 PDF, 但来自同一组结果和同一次绘图.
本轮采用 Chapter 6 data availability statement 中的公开仓库,
固定到提交 `f863ab02ebf93d5804f5552967ea750571778335`.
参见 [原始 notebook](https://github.com/Photonico/H-Beryllene_20250718/blob/f863ab02ebf93d5804f5552967ea750571778335/9.0_thesis_demo.ipynb).

- Cell 2–7 每种物理量只调用一次绘图函数.
  先保存 publication 版本, 再对同一个 figure 调整字号和版式,
  保存 thesis 版本; 中间没有更换数据或重新计算.
  六图始终使用同一组 alpha/beta 数据及 `xx`、`zz` 分量.
- 本地十二个 PDF 的 Git blob 全部与归档中相应输出一致.
  一致的是“本地文件与各自归档副本”, 不是“一对 ch3/ch6 文件彼此相同”.
- 另从两份归档 HDF5 独立重算旧公式, 对照当前 Chapter 3 六图的 28 条曲线.
  使用 PDF 自身刻度标定坐标, 没有用原始数组拟合坐标.
  6,510 个可见保留顶点吻合, 最大页面残差约 0.00260 pt.
  这使“同源”的判断不只依赖 notebook 文件名.
  PDF 含简化折线, 因而不声称每个原始采样点均逐点存入 PDF.

原始读取路径为 `6.0_dielectric_selection/a-Beryllene/vaspout.h5`
和 `b-Beryllene/vaspout.h5`, 使用其 `density_density_dielectric_function`.
这些文件及对应结构均通过固定提交的 blob 校验.
哈希与数值核验见 [审计记录](ch3_verification/source-and-numeric-audit.json).

六组对应保留如下:

1. `figures_ch3/3.1_dielectric.pdf` →
   `figures_proj3/fig3.13_dielectric.pdf`,
   Chapter 6 label `fig:proj3_alpha_beta_dielectric`.
2. `figures_ch3/4.1_absorption.pdf` →
   `figures_proj3/fig3.14a_absorption.pdf`,
   合图 `fig:proj3_alpha_beta_abs_refractive` 的上半部分.
3. `figures_ch3/4.2_refractive.pdf` →
   `figures_proj3/fig3.14b_refractive.pdf`, 同一合图的下半部分.
4. `figures_ch3/4.3_extinction.pdf` →
   `figures_proj3/fig3.15_extinction.pdf`,
   label `fig:proj3_alpha_beta_extinction`.
5. `figures_ch3/4.4_reflectivity.pdf` →
   `figures_proj3/S3.16_reflectivity.pdf`,
   label `fig:proj3_reflectivity_alpha_beta`.
6. `figures_ch3/4.5_energy-loss.pdf` →
   `figures_proj3/S3.17_energy-loss.pdf`,
   label `fig:proj3_energy_loss_alpha_beta`.

后两幅随 Chapter 6 的 SI 连续编入论文, 仍属于该章.
这些光学计算由本人完成的事实已由你确认.
不将它扩写为整个合作项目均由本人独立完成, 也不擅自写成已发表.

### 1.2 评审要求与本稿的覆盖边界

Examiner 2 的 DOCX 要求辨明光学例子究竟来自本论文还是外部文献.
本稿以首图前声明、方法/结果交叉引用、六图来源及七处引用清理直接回应.
原报告该段没有单独编号, 不把 AI 汇总编号当成原始编号.
旧版“page 100 onwards”不作为当前页码边界, 六幅例图全部处理.

Examiner 1 同时要求实际方法组织和缩短 Chapters 2–3.
Chapter 2 的 2.6 已提供方法入口, 本章在 BZ 积分处回指它,
并把例子连接到 Chapter 6 的真实计算.
本稿仅删三处相邻直接复述, 不删理论、例图或必要解释.
这回应了方法组织和少量重复, 但不能声称已全面落实缩短要求.
必要纠错可能造成净增字数; 是否接受保留完整推导, 仍由评审程序判断.

光学动机已在 Chapter 1 的 `subsec:opt_observables_motivation` 建立.
Chapter 3 保留物理量定义与用途, Chapter 6 负责具体材料比较.
不在六小节中各新增同义的动机段落.
二维归一化、带内响应、IPA 局限和 plasmon 判断补最必要的条件,
研究章仍须依据真实设置回应其独立要求.

Examiner 2 关于图中文字难读的具体批评指向 Chapter 4.
本章保留较大字号的 thesis 版, 修复本轮发现的单位及裁剪,
不将该意见误称为 examiner 指定重画 Chapter 3.
Chapter 6 的 PBE-only、结构构造、收敛、氢化、AIMD 和 topology 等问题,
不能靠本章来源声明全部关闭.

### 1.3 对 Gemini 初稿的取舍与文风

采用来源声明、图注与引用清理方向.
不用 `pedagogical examples`、`critical physical inquiry`
或 `spectral dissipation rate in phase space` 等与原文不一致的表达.
不用不存在的 `sec:proj3_optical_response`,
不新增器件承诺或未经证实的 plasmon 归因.

沿用 `We first`、`We then`、`We now`、小写 `here,`,
`chapter~\ref{...}`、`section~\ref{...}`、`equation~\eqref{...}`.
保留 `\vec`、`\dif`、`\mathrm`、`\coloneqq`
及 `equation` 内嵌 `aligned` 或左大括号的写法.
量子态与矩阵元始终使用 Dirac notation.
位置矢量严格写为 `\vec{r}\,'` 和 `\vec{r}\,)`;
本轮不全局排版未涉及的原式.
保留原章的 Beryllene 大小写, 按句子或有意义的从句换行.

## 2. 已确认的数值问题及最小修复

### 2.1 beta 厚度漏乘了超胞高度

Notebook 注释声明层厚为 `(z_max-z_min)*d_c+2*r_be`,
实际却写成:

```python
factor_a = (40, 2*1.98)
factor_b = (40, 0.0473771641975619+2*1.98)
```

结构文件采用分数坐标.
beta 的 full cell height 为 40 Å, fractional z span 约为
0.0473771641975560, 真实原子层跨度约为 1.89508656790224 Å.
按原程序选择的半径约定, 有效厚度为:

```latex
\begin{equation}
\begin{aligned}
    d_{\mathrm{2D}}
    &= \left(s_{z,\max}-s_{z,\min}\right)d_{\mathrm{SC}}+2r_{\mathrm{Be}} \\
    &= \qty{5.8550865679}{\angstrom}
\end{aligned}
\end{equation}
```

这只是操作稿中的算术核验式, 不另外插入 Chapter 3.
`s_z` 是分数坐标, `r_Be=1.98 Å` 是原程序的厚度约定,
不把该半径宣称为唯一材料常数.
程序实际用了约 4.0073771642 Å; 最小修复是给分数跨度乘 40,
更稳妥的实施是直接由结构读取 cell 和跨度.
alpha 的 3.96 Å 不变.

Chapter 6 SI 的 5.85 Å 与预期厚度接近,
但不是 5.855086... 按两位小数正常四舍五入的结果.
应用时统一为例如 `\qty{5.855}{\angstrom}`,
后处理保留未舍入值, 不声称两者精确一致.
修正后 beta 的 `epsilon_1-1` 与 `epsilon_2`
均为旧值的约 0.6844266293 倍.
由它们导出的 n、k、R、L 不能机械乘同一个因子.

### 2.2 吸收系数少了 2π

`energy_to_frequency` 返回普通频率 `E/h`,
后续吸收函数却将它直接用于需要角频率的公式.
Chapter 3 原来的两个吸收公式是正确的, 应保留:

```latex
\begin{equation}
    \alpha_{\lambda}(\omega)
    = \frac{2\,\omega}{c}k_{\lambda}(\omega)
    = \frac{2E}{\hbar c}k_{\lambda}(\omega)
\end{equation}
```

这同样是核验关系, 不新增重复正文公式.
调用应先得到 `omega = 2*pi*energy_to_frequency(energy)`,
再传给使用角频率的吸收函数; 或在该局部函数明确完成同一换算.
只补一次 2π, 不全局改变通用 frequency 函数的语义.
代码中 `hbar=4.135667662e-15` 实际是 h 的数值,
应改正变量名或给真正的 hbar, 不留下混淆.

原光速常量是 `2.99792458e17 nm/s`,
所以正确输出单位为 `nm^-1`.
保持介电数据不变时, 正确吸收为旧值的 2π 倍.
alpha 仅需这个频率修正; beta 还受厚度修正影响.
参见固定提交的
[后处理模块](https://github.com/Photonico/H-Beryllene_20250718/blob/f863ab02ebf93d5804f5552967ea750571778335/vmatplot/linear_optical_properties.py)
和 [换算模块](https://github.com/Photonico/H-Beryllene_20250718/blob/f863ab02ebf93d5804f5552967ea750571778335/vmatplot/algorithms.py).

### 2.3 重算结果与应更新的图

在同一归档 density-density 数据上复算, 0–12 eV 内:

- alpha 面内吸收最大值约从 0.021562 改为 0.135476 nm^-1,
  面外从 0.027854 改为 0.175010 nm^-1.
- beta 面内吸收最大值约从 0.031402 改为 0.159298 nm^-1,
  面外从 0.046811 改为 0.241453 nm^-1.
  曲线存在局部交叉, 不概括为 beta 在全部能区均更强.
- beta 面内旧可见峰约 0.3443, 深紫外局部峰约 0.6534.
  修正后约为 0.4490 与 1.3335, 高能窗口边界还在上升.
  原文 `visible-range peak being stronger` 在修正前后都不成立.
- alpha 面外 loss 主峰约 8.8781, 位于约 10.637 eV.
  旧图上限 2.1 裁掉该峰和约 2.7314 的次峰.
  beta 修正后面外主峰约 1.0018, 不能继续写它比 alpha 更显著.
- alpha 面内在窗口末端约为 2.2265, 也略超旧上限.
  这是边界值, 不能称为已捕获完整高能峰.
- beta 面外 extinction 的最大值位于约 5.955 eV,
  支持 Chapter 3 的 ultraviolet 描述,
  不支持 Chapter 6 所写的“向 near-ultraviolet 快速下降”.

峰位来自约 0.020 eV 网格, 正文无需为了纠错添加这一整列数值.
这些数值证明后处理影响, 不替代泛函、展宽、局域场或 Drude 的物理验证.

应用时从同一份修正数组输出两套版式, 同步替换全部十二个 PDF.
保留原文件名、颜色、线型、面板布局和正文图宽.
吸收轴写明 `nm^-1`, 范围覆盖约 0.2415 nm^-1 并留边距.
loss 可用面内约 0–2.5、面外约 0–9.5 的范围,
保留两个面板, 不再统一限制为 2.1.
两章同种物理量使用相同数据与坐标, 字号适合各自版面.

不改原始 HDF5, 不将后处理修复说成新增 DFT 计算,
不在本轮远程修改公开归档或覆盖正式图件.
后文 loss 比较和吸收单位候选必须与新版图一起应用.

### 2.4 这六幅图的带内项已查明

实际输出参数记录为 VASP 6.5.0, LOPTICS=T, ISPIN=1, LSORBIT=F,
ISMEAR=0, SIGMA=0.01 eV, CSHIFT=0.1 eV.
两份 vasprun.xml 的完整 parameters 段均明确记录 WPLASMAI=0,
WPLASMA 的九个分量也均为零.
后处理没有另加 Drude.
因此, 这六图确实是没有 Drude 带内项的 IPA 带间谱,
不是根据现行默认值猜测的结论.
这不包含完整金属低频响应, 也不把数值展宽当成真实散射率或寿命.

实际总能带数为 133, 输入请求为 128;
程序调整后的 NBANDS 不能写成 133 条未占据能带.
这些参数留在 Chapter 6, Chapter 3 只增加最短的模型范围说明.
上述结论仅针对这两个原始数据集, 不推广到所有其他图件.

## 3. 按本章顺序执行的 LaTeX 候选

各项给出当前行号、原句起点和完整替换段.
未列出的文字、公式和衔接保留.
六个 caption 只替换 caption 内容, figure 环境其余部分保留.
七处引用清理与三处纯去重在第 4 节单列.


### 3.1. 单位与频率约定

位置: `src/fundamentals_b.tex:36`.
原句起点: `In the present section, we mainly use SI units for the macroscopic electrodynamic equations.`.

替换原来的两句单位说明. 后文沿用这一约定, 不把普通频率当作角频率.

```latex
In this chapter, we use SI units for the macroscopic electrodynamic equations.
The dielectric function is dimensionless and denotes the relative dielectric response.
We use the angular frequency $\omega$ with the time dependence $\exp(-\mathrm{i}\,\omega t)$,
and the photon energy is $\hbar\omega$.
```

### 3.2. 电磁方程中的光学近似

位置: `src/fundamentals_b.tex:105`.
原句起点: `For the nonmagnetic media considered in the present work, the electric response is the central object.`.

保留紧随其后的 Maxwell 方程组. 光学近似不等于所有体系均无电子磁序, 因而不与 Chapter 5 的 AFM 结果冲突.

```latex
For the optical response considered here, we neglect magnetic-permeability effects and take the relative magnetic permeability as $\mu_{\mathrm{r}}(\omega)\approx1$.
The electric response is then the central object, and we keep the Maxwell equations in the form:
```

### 3.3. 主轴形式的前提

位置: `src/fundamentals_b.tex:254`.
原句起点: `When we choose the Cartesian axes along the principal directions of the crystal,`.

只限定原矩阵式的适用条件, 不增写一般各向异性模式理论.

```latex
When the crystal symmetry allows a diagonal dielectric tensor in the chosen Cartesian axes,
the dielectric tensor $\varepsilon_{\alpha\beta}(\omega)$ takes the principal-axis form~\cite{nye1985physical}:
```

### 3.4. 面内等价方向的前提

位置: `src/fundamentals_b.tex:271`.
原句起点: `Therefore, it is convenient to introduce the in-plane dielectric function $\varepsilon_{\varparallel}(\omega)$ and the out-of-plane dielectric function $\varepsilon_{\perp}(\omega)$~\cite{nye1985physical,guo2021complete,matthes2016influence}:`.

不将所有 xene 的 xx 与 yy 默认为相等. 实际六幅例图使用 xx 与 zz.

```latex
When the two in-plane directions are symmetry-equivalent,
we introduce the in-plane dielectric function $\varepsilon_{\varparallel}(\omega)$ and the out-of-plane dielectric function $\varepsilon_{\perp}(\omega)$~\cite{nye1985physical,guo2021complete,matthes2016influence}:
```

### 3.5. 标量响应与模式的关系

位置: `src/fundamentals_b.tex:367`.
原句起点: `For the later discussion on optical observables,`.

固定偏振本身不足以把一般各向异性传播化为独立标量问题. 保留后面的标量定义.

```latex
For the later discussion on optical observables,
we consider a decoupled principal-axis mode.
We then suppress the tensor indices and write the dielectric response in scalar form.
```

### 3.6. 带间跃迁式与带内响应

位置: `src/fundamentals_b.tex:437`.
原句起点: `Next, we describe this microscopic process in a periodic solid as an interband transition from an occupied valence state $\ket{\psi_{v\vec{k}}}$ to an empty conduction state $\ket{\psi_{c\vec{k}}}$.`.

替换从 Next, we describe this microscopic process... 到下一个 subsection 前的局部段落. 保留“跃迁 → 占据 → 能量守恒 → 矩阵元 → 各向异性”的解释链与原 label, 补速度式缺少的 1/ω², 不另造全套归一化常数. 新增 Drude 式说明模型边界, 不声称已有数据包含该项. 此项属于正确性修复, 不计为纯文字压缩.

```latex
Next, we describe this microscopic process in a periodic solid as a transition from an initial state $\ket{\psi_{n\vec{k}}}$ to a final state $\ket{\psi_{m\vec{k}}}$.
Here, $\vec{k}$ denotes the crystal momentum in the first Brillouin zone.
In the optical regime, the photon momentum is negligible on the scale of the Brillouin zone,
so the transition is effectively vertical in $\vec{k}$-space~\cite{fox2010optical}.
Accordingly, the transition strength is determined by the velocity matrix elements rather than by the band energies alone.

For the present work, we adopt the independent-particle approximation (IPA)
built from the ground-state electronic structure.
We consider the reciprocal electric response and retain the symmetric dielectric tensor,
without its antisymmetric magneto-optical contribution.
The interband part of its imaginary component takes the form~\cite{d2016accurate,gajdovs2006linear}:

\begin{equation}
\begin{aligned}
    \varepsilon_{2,\alpha\beta}^{\mathrm{inter}}(\omega)
    &\propto \frac{1}{\omega^2}\sum_{n\ne m}
    \int_{\mathrm{BZ}}\frac{\dif^3{k}}{(2\pi)^3}\,
    \left(f_{n\vec{k}}-f_{m\vec{k}}\right) \\
    &\quad\times\mathrm{Re}\left[
    \bra{\psi_{m\vec{k}}}\hat{v}_{\alpha}\ket{\psi_{n\vec{k}}}
    \bra{\psi_{n\vec{k}}}\hat{v}_{\beta}\ket{\psi_{m\vec{k}}}
    \right]
    \delta\left(E_{m\vec{k}}-E_{n\vec{k}}-\hbar\omega\right)
\end{aligned}
\label{independent_particle_imaginary_dielectric_tensor}
\end{equation}

here, $n$ and $m$ label the initial and final bands,
and $f_{n\vec{k}}$ and $f_{m\vec{k}}$ denote their occupations.
The band energies $E_{n\vec{k}}$ and $E_{m\vec{k}}$ describe the initial and final states.
The velocity operator $\hat{v}_{\alpha}=(\mathrm{i}/\hbar)[\hat{H},\hat{r}_{\alpha}]$ determines the transition strength along the $\alpha$ direction.
The proportionality sign suppresses a frequency-independent prefactor.
The state labels include spin according to the chosen electronic-structure description.
For a diagonal component, the matrix-element product reduces to
$\left|\bra{\psi_{m\vec{k}}}\hat{v}_{\alpha}\ket{\psi_{n\vec{k}}}\right|^2$.
Meanwhile, the Dirac delta function enforces the energy-conservation condition:

\begin{equation}
    E_{m\vec{k}}-E_{n\vec{k}}=\hbar\omega
\label{dirac_energy_conservation_condition}
\end{equation}

Equation~\eqref{independent_particle_imaginary_dielectric_tensor} describes the microscopic origin of the interband absorptive response.
For a transition to contribute, the occupation difference and the velocity matrix elements must be nonzero,
and the transition energy must match the photon energy $\hbar\omega$.
For an insulator at zero temperature, this reduces to a transition from an occupied valence state to an empty conduction state.
For a metal, the occupations must instead be resolved at each $\vec{k}$.
The corresponding matrix elements therefore serve as the criterion for optically allowed transitions.
When many allowed transitions contribute strongly at the same excitation energy,
a peak can appear in $\varepsilon_{2,\alpha\beta}^{\mathrm{inter}}(\omega)$.

This point clarifies what the calculated spectra describe.
The imaginary part reflects the band energies, the occupation pattern,
and the direction-resolved transition matrix elements.
The Brillouin-zone integration is evaluated using the k-point sampling discussed in section~\ref{subsec:method_kpoints}.
Within the adopted independent-particle description,
the spectra resolve the interband onset, absorption peaks, and directional contrast.
The electron--hole interaction is not included in this approximation.

The tensor indices $\alpha$ and $\beta$ enter directly through the velocity matrix elements.
Therefore, the microscopic transition strength already resolves the field polarization and the crystal directions.
This result naturally leads us to the dielectric response in anisotropic media~\cite{huang2023optical}.

The interband expression does not include the intraband response of free carriers.
For a metal, a simple model for this additional contribution along a principal direction $\lambda$ is the Drude form~\cite{dressel2002electrodynamics}:

\begin{equation}
    \varepsilon_{\lambda\lambda}(\omega)
    = \varepsilon_{\lambda\lambda}^{\mathrm{inter}}(\omega)
    - \frac{\omega_{p,\lambda}^{2}}
    {\omega\left(\omega+\mathrm{i}\,\gamma_{\lambda}\right)}
\label{interband_and_drude_dielectric_response}
\end{equation}

here, $\varepsilon_{\lambda\lambda}^{\mathrm{inter}}(\omega)$ includes the vacuum background of one,
$\omega_{p,\lambda}$ is the plasma angular frequency,
and $\gamma_{\lambda}>0$ is the carrier damping rate.
For the spectra shown here, we use the independent-particle interband response calculated with VASP,
without microscopic local-field effects or a Drude contribution from intraband transitions.
Therefore, these spectra do not describe the complete low-frequency response of the metallic systems.
```

### 3.7. 带间推导与各向异性小节的衔接

位置: `src/fundamentals_b.tex:501`.
原句起点: `The previous subsection established the microscopic expression for the imaginary part $\varepsilon_{2,\alpha\beta}(\omega)$.`.

与新 IPA 式的 interband 范围一致, 不将其写成完整金属介电响应.

```latex
The previous subsection established the microscopic expression for the interband part of the imaginary dielectric response.
```

### 3.8. 首幅例图前的来源声明与二维处理

位置: `src/fundamentals_b.tex:529`.
原句起点: `A representative example of the direction-resolved dielectric response is shown in the following figure.`.

保留原两句, 落实作者的来源注释. 归一化沿用 Chapter 5 已有 d_SC/d_2D 记号和 Chapter 6 引用的方法. 不把 40 Å 全超胞高度写成纯真空厚度. 不在六处导图句中重复整段声明.

```latex
A representative example of the direction-resolved dielectric response is shown in the following figure.
The real and imaginary parts exhibit distinct in-plane and out-of-plane features over the full photon-energy range.
The $\alpha$-Beryllene and $\beta$-Beryllene spectra in this chapter were calculated by the author for the study presented in chapter~\ref{cha:project_beryllene}.
The calculation methods and corresponding optical results are discussed in sections~\ref{3_methods} and~\ref{3_optical_alpha_beta}.

For these two-dimensional systems, the calculated dielectric response includes the vacuum region of the supercell.
We use the optical volume normalization adopted in chapter~\ref{cha:project_beryllene}~\cite{yang2021method}:

\begin{equation}
\left\{\begin{aligned}
    \varepsilon_{1,\lambda\lambda}^{\mathrm{2D}}(\omega)
    &= 1+\frac{d_{\mathrm{SC}}}{d_{\mathrm{2D}}}
    \left[\varepsilon_{1,\lambda\lambda}^{\mathrm{SC}}(\omega)-1\right] \\
    \varepsilon_{2,\lambda\lambda}^{\mathrm{2D}}(\omega)
    &= \frac{d_{\mathrm{SC}}}{d_{\mathrm{2D}}}
    \varepsilon_{2,\lambda\lambda}^{\mathrm{SC}}(\omega)
\end{aligned}\right.
\label{optical_volume_normalization_2d}
\end{equation}

here, $d_{\mathrm{SC}}$ is the full supercell height,
and $d_{\mathrm{2D}}$ is the chosen effective thickness of the layer.
The superscripts $\mathrm{SC}$ and $\mathrm{2D}$ distinguish the supercell response from the normalized response.
The thickness values are given in section~\ref{3_supplementary}.
The dielectric function and the derived optical quantities therefore remain associated with this thickness convention.
```

### 3.9. Figure 3.1 的图注

位置: `src/fundamentals_b.tex:535`.
原句起点: `\caption{Representative real and imaginary parts of the in-plane and out-of-plane dielectric function as a function of photon energy for $\alpha$-Beryllene and $\beta$-Beryllene. The figure illustrates the direction-resolved complex dielectric response discussed in the text.}`.

保留原图注及 figure 的路径、宽度和 label. 增补分量与来源; 吸收单位随修正后的图件一起采用.

```latex
\caption{Representative real and imaginary parts of the in-plane and out-of-plane dielectric function as a function of photon energy for $\alpha$-Beryllene and $\beta$-Beryllene. The figure illustrates the direction-resolved complex dielectric response discussed in the text.
The in-plane and out-of-plane curves correspond to the $xx$ and $zz$ components, respectively.
These spectra are from our calculations presented in chapter~\ref{cha:project_beryllene}.}
```

### 3.10. Kramers--Kronig 推导的适用范围

位置: `src/fundamentals_b.tex:671`.
原句起点: `We therefore represent the Kramers--Kronig relations for the dielectric tensor in the general frequency-domain form as:`.

保留两条 KK 公式与解析性推导; 不将普通积分形式无条件用于有直流导电极点的金属完整介电函数.

```latex
Here, we consider the regular electronic response without a zero-frequency conductivity pole,
with $\varepsilon_{\alpha\beta}(\omega)\to\delta_{\alpha\beta}$ at high frequency.
For a metal, the conductive term must be separated before applying these relations in the form below.
The dielectric function in this derivation then denotes the remaining regular response.
We represent the Kramers--Kronig relations in the frequency-domain form as:
```

### 3.11. 主值的定义

位置: `src/fundamentals_b.tex:688`.
原句起点: `It removes the singular contribution at $\omega'=\omega$.`.

主值规定积分极限, 不是删除奇点所代表的物理贡献.

```latex
It defines the integral through a symmetric limiting procedure around $\omega'=\omega$~\cite{stefanski2022analytical,koutserimpas2024time}.
```

### 3.12. 静态极限的收敛条件

位置: `src/fundamentals_b.tex:731`.
原句起点: `Firstly, the zero-frequency limit of the dispersive part determines the static dielectric response.`.

保留静态公式, 条件放在取极限前. 不把电子 interband 零频值当成包含离子和自由载流子的完整静态屏蔽.

```latex
Firstly, for the regular electronic response with a convergent static integral,
we set $\omega\to0$ in the positive-frequency Kramers--Kronig relations~\eqref{kk_positive_frequency_dielectric_component}.
This limit does not represent the full static dielectric response of a conducting system.
We then obtain the static electronic response in the principal-axis representation:
```

### 3.13. 低能权重与实际贡献

位置: `src/fundamentals_b.tex:748`.
原句起点: `Next, the factor $1/\omega'$ gives higher weight to low-energy spectral contributions.`.

保留因果解释, 不把 1/ω 权重写成低能部分必定主导. 此项属于正确性修复.

```latex
Next, the factor $1/\omega'$ gives higher weight to low-energy spectral contributions.
The dominant contribution nevertheless depends on the spectral weight over the full energy range.
Therefore, the static limit represents an accumulated response over the full absorption spectrum.
```

### 3.14. 派生光学量的共同前提

位置: `src/fundamentals_b.tex:793`.
原句起点: `Afterwards, we analyze the in-plane and out-of-plane optical response of the present systems.`.

在 3.4 入口集中说明, 不再将 xx/zz 分量误称为光沿 x/z 传播.

```latex
Afterwards, we analyze the in-plane and out-of-plane optical response of the present systems.
For absorption, refraction, and reflection, we use the local effective-medium description of a transverse principal-axis mode with $\mu_{\mathrm{r}}(\omega)\approx1$.
The index $\lambda$ denotes the electric-field polarization.
In the propagation equations, $z$ denotes distance along the wave path and need not coincide with the structural out-of-plane axis.
```

### 3.15. 吸收系数所标记的方向

位置: `src/fundamentals_b.tex:798`.
原句起点: `which characterizes the optical attenuation along the principal direction $\lambda$~\cite{lin2023recent}.`.

只改方向含义, 保留 Beer--Lambert 推导.

```latex
which characterizes the optical attenuation for polarization along the principal direction $\lambda$~\cite{lin2023recent}.
```

### 3.16. 介质内部的起始强度

位置: `src/fundamentals_b.tex:809`.
原句起点: `$I_{\lambda,0}(\omega)$ and $I_{\lambda}(z,\omega)$`.

外部入射光先经过界面. 保留指数式, 不把传播衰减等同于界面透射.

```latex
$I_{\lambda,0}(\omega)$ is the intensity just inside the medium at $z=0$,
and $I_{\lambda}(z,\omega)$ is the intensity at depth $z$.
```

### 3.17. Figure 3.2 的图注

位置: `src/fundamentals_b.tex:868`.
原句起点: `\caption{The absorption coefficients for the in-plane and out-of-plane directions as functions of photon energy for $\alpha$-Beryllene and $\beta$-Beryllene.}`.

保留原图注及 figure 的路径、宽度和 label. 增补分量与来源; 吸收单位随修正后的图件一起采用.

```latex
\caption{The absorption coefficients for the in-plane and out-of-plane directions as functions of photon energy for $\alpha$-Beryllene and $\beta$-Beryllene.
The in-plane and out-of-plane curves correspond to the $xx$ and $zz$ components, respectively. The absorption coefficient is given in $\mathrm{nm}^{-1}$.
These spectra are from our calculations presented in chapter~\ref{cha:project_beryllene}.}
```

### 3.18. 吸收例图的偏振措辞

位置: `src/fundamentals_b.tex:876`.
原句起点: `These trends indicate that the optical attenuation depends on both the propagation direction and the crystal structure of the medium.`.

只替换 propagation, 其余谱线解释保留.

```latex
These trends indicate that the optical attenuation depends on both the polarization direction and the crystal structure of the medium.
```

### 3.19. 复折射率推导中的横波

位置: `src/fundamentals_b.tex:898`.
原句起点: `For a monochromatic wave propagating along the principal direction $\lambda$,`.

避免把 E_lambda 写成沿传播方向的纵向电场. 指数式保留.

```latex
For a monochromatic transverse mode polarized along the principal direction $\lambda$,
we first represent the electric field along the propagation coordinate $z$ as~\cite{politano2023spectroscopic}:
```

### 3.20. 折射率与相对磁导率

位置: `src/fundamentals_b.tex:923`.
原句起点: `We then write the general relation between the complex refractive index $N_{\lambda}(\omega)$,`.

原同指标 ε_lambda,lambda μ_lambda,lambda 不是一般各向异性传播关系. 改用标量相对磁导率, 保留原 label 及后续 N²=ε、n、k 推导. 正确的吸收公式不改.

```latex
For this mode and a scalar relative magnetic permeability $\mu_{\mathrm{r}}(\omega)$,
we write the relation between the complex refractive index and dielectric function as~\cite{born2013principles,wooten2013optical,dressel2002electrodynamics,politano2023spectroscopic}:

\begin{equation}
    N_{\lambda}^{2}(\omega)
    = \varepsilon_{\lambda\lambda}(\omega)\,\mu_{\mathrm{r}}(\omega)
\label{general_refractive_index_permeability_relation}
\end{equation}

here, $\mu_{\mathrm{r}}(\omega)$ is dimensionless.
Under the optical approximation $\mu_{\mathrm{r}}(\omega)\approx1$,
the relation reduces to~\cite{wooten2013optical,dressel2002electrodynamics,born2013principles}:
```

### 3.21. Figure 3.3 的图注

位置: `src/fundamentals_b.tex:988`.
原句起点: `\caption{The refractive indices for the in-plane and out-of-plane directions as functions of photon energy for $\alpha$-Beryllene and $\beta$-Beryllene.}`.

保留原图注及 figure 的路径、宽度和 label. 增补分量与来源; 吸收单位随修正后的图件一起采用.

```latex
\caption{The refractive indices for the in-plane and out-of-plane directions as functions of photon energy for $\alpha$-Beryllene and $\beta$-Beryllene.
The in-plane and out-of-plane curves correspond to the $xx$ and $zz$ components, respectively.
These spectra are from our calculations presented in chapter~\ref{cha:project_beryllene}.}
```

### 3.22. Figure 3.4 的图注

位置: `src/fundamentals_b.tex:1003`.
原句起点: `\caption{The extinction coefficients for the in-plane and out-of-plane directions as functions of photon energy for $\alpha$-Beryllene and $\beta$-Beryllene.}`.

保留原图注及 figure 的路径、宽度和 label. 增补分量与来源; 吸收单位随修正后的图件一起采用.

```latex
\caption{The extinction coefficients for the in-plane and out-of-plane directions as functions of photon energy for $\alpha$-Beryllene and $\beta$-Beryllene.
The in-plane and out-of-plane curves correspond to the $xx$ and $zz$ components, respectively.
These spectra are from our calculations presented in chapter~\ref{cha:project_beryllene}.}
```

### 3.23. Fresnel 模型与二维薄片的区别

位置: `src/fundamentals_b.tex:1042`.
原句起点: `For the xene systems considered in the present work,`.

保留 Fresnel 推导与 R 式. r 的整体符号随反射偏振基矢约定变化, 不影响 R=|r|², 不把该符号当作数据错误. 两介质均在本节共同 μr≈1 条件下理解.

```latex
For the optical quantities derived here,
we consider an interface between vacuum and a homogeneous semi-infinite effective medium with $\mu_{\mathrm{r}}(\omega)\approx1$.
The incident medium therefore satisfies $N_{0,\lambda}(\omega)=1$.
The resulting reflectivity is a parameter of this effective-medium model.
For a finite two-dimensional layer, the measured reflectance also depends on the thickness, substrate, and optical geometry.
At normal incidence on the structural plane, the electric field is in-plane.
The value obtained from $\varepsilon_{zz}(\omega)$ is therefore a formal out-of-plane response of the scalar model,
not a second normal-incidence channel of the layer.
```

### 3.24. Figure 3.5 的图注

位置: `src/fundamentals_b.tex:1088`.
原句起点: `\caption{The reflectivities for the in-plane and out-of-plane directions as functions of photon energy for $\alpha$-Beryllene and $\beta$-Beryllene.}`.

保留原图注及 figure 的路径、宽度和 label. 增补分量与来源; 吸收单位随修正后的图件一起采用.

```latex
\caption{The reflectivities for the in-plane and out-of-plane directions as functions of photon energy for $\alpha$-Beryllene and $\beta$-Beryllene.
The in-plane and out-of-plane curves correspond to the $xx$ and $zz$ components, respectively. The reflectivities are evaluated within the effective-medium model described in the text.
These spectra are from our calculations presented in chapter~\ref{cha:project_beryllene}.}
```

### 3.25. 反射到损失的衔接

位置: `src/fundamentals_b.tex:1101`.
原句起点: `We next turn to the energy-loss spectrum $L_{\lambda}(\omega)$ and identify the photon-energy range where the dielectric screening gives way to the strongest resonant dissipation.`.

保留前后过渡, 不预设所有峰均属最强共振耗散.

```latex
We next turn to the energy-loss spectrum $L_{\lambda}(\omega)$ and examine the longitudinal loss response of the medium.
```

### 3.26. 纵向损失函数的范围

位置: `src/fundamentals_b.tex:1109`.
原句起点: `The energy-loss spectrum $L_{\lambda}(\omega)$ characterizes the energy transferred from an external probe to the medium at a given photon energy.`.

保留 L=Im[-1/ε] 及展开式; λ 在本节指纵向扰动方向. 不把标量形式当成所有 EELS 测量几何的完整结果.

```latex
The energy-loss spectrum $L_{\lambda}(\omega)$ characterizes the energy transferred from an external probe to the medium at an energy transfer $\hbar\omega$.
Here, we consider a longitudinal perturbation along the principal direction $\lambda$ in the local, long-wavelength limit.
This loss function describes the corresponding bulk response relevant to electron energy-loss spectroscopy;
finite momentum and surface contributions require the appropriate scattering geometry.

We first express this principal-axis loss function as~\cite{dressel2002electrodynamics,wooten2013optical,fox2010optical,onida2002electronic}:
```

### 3.27. 损失峰与低阻尼条件

位置: `src/fundamentals_b.tex:1125`.
原句起点: `When the dielectric screening weakens,`.

原文 finite 不足以说明尖锐集体峰. 不预先认定 Chapter 6 的具体峰为 plasmon.

```latex
For a weakly damped longitudinal collective excitation,
a loss peak can occur near a zero of $\varepsilon_{1,\lambda\lambda}(\omega)$ when $\varepsilon_{2,\lambda\lambda}(\omega)$ is small.
Interband excitations also contribute to the loss spectrum,
so a peak alone does not establish a plasmon~\cite{dressel2002electrodynamics,onida2002electronic}.
```

### 3.28. 保留分子分母解释, 纠正强耗散表述

位置: `src/fundamentals_b.tex:1139`.
原句起点: `This expression separates the dissipative channel from the dielectric screening.`.

以原式直接代入解释阻尼, 不删除物理解释链. 替换“强耗散自动增强 loss”及无条件优于 absorption 的说法.

```latex
This expression separates the dissipative channel from the dielectric screening.
The imaginary part $\varepsilon_{2,\lambda\lambda}(\omega)$ enters both the numerator and the denominator.
At $\varepsilon_{1,\lambda\lambda}(\omega)=0$ and finite positive $\varepsilon_{2,\lambda\lambda}(\omega)$,
the loss function is $L_{\lambda}(\omega)=1/\varepsilon_{2,\lambda\lambda}(\omega)$.
Therefore, a large imaginary part does not by itself produce a strong loss peak.
The loss spectrum describes longitudinal screening and complements the transverse absorption and reflection responses~\cite{dressel2002electrodynamics,onida2002electronic}.
```

### 3.29. Figure 3.6 的图注

位置: `src/fundamentals_b.tex:1149`.
原句起点: `\caption{The energy-loss spectra for the in-plane and out-of-plane directions as functions of photon energy for $\alpha$-Beryllene and $\beta$-Beryllene.}`.

保留原图注及 figure 的路径、宽度和 label. 增补分量与来源; 吸收单位随修正后的图件一起采用.

```latex
\caption{The energy-loss spectra for the in-plane and out-of-plane directions as functions of photon energy for $\alpha$-Beryllene and $\beta$-Beryllene.
The in-plane and out-of-plane curves correspond to the $xx$ and $zz$ components, respectively.
These spectra are from our calculations presented in chapter~\ref{cha:project_beryllene}.}
```

### 3.30. 按重算结果纠正损失谱比较

位置: `src/fundamentals_b.tex:1153`.
原句起点: `The energy-loss spectra demonstrate clear directional and structural contrasts.`.

这段必须与恢复完整纵轴、修正厚度后的图一起采用. 重算显示深紫外 β 面内响应更强, 且面外 α 主峰原图被裁剪. 不把窗口终点的最大值称为已捕获的完整峰.

```latex
The energy-loss spectra demonstrate clear directional and structural contrasts.
In the in-plane channel, $\beta$-Beryllene develops a visible-range peak and a stronger response in the deep-ultraviolet region,
whereas $\alpha$-Beryllene remains weak at low photon energy and rises toward the upper end of the plotted range.
In the out-of-plane channel, both materials remain weak in the visible range and develop stronger loss features at higher energies.
The deep-ultraviolet peak of $\alpha$-Beryllene is stronger than that of $\beta$-Beryllene.
```

### 3.31. 损失谱结尾保留归纳

位置: `src/fundamentals_b.tex:1158`.
原句起点: `These results demonstrate that the energy-loss spectrum $L_{\lambda}(\omega)$ varies with both the optical direction and the crystal structure of the medium.`.

保留示例总结与下一段完整光学量收束, 更正重复出现的“比吸收或反射更直接识别主导耗散”结论.

```latex
These results demonstrate that the energy-loss spectrum $L_{\lambda}(\omega)$ varies with both the response direction and the crystal structure of the medium.
As $L_{\lambda}(\omega)$ follows the inverse dielectric function,
its peaks identify energy ranges with a strong longitudinal loss response.
```

## 4. 引用清理与真正的文字去重

### 4.1 七处本人结果的来源歧义

仅去掉以下指定句子的引用链, 保留句子及标点. 不全局删除同名 cite key:

- 第 863 行: `The following figure presents the calculated absorption coefficient $\alpha_{\lambda}(\omega)$ spectra of the present systems for the in-plane and out-of-plane directions:`
- 第 983 行: `With these expressions, we present the calculated refractive index $n_{\lambda}(\omega)$ spectra of $\alpha$-Beryllene and $\beta$-Beryllene:`
- 第 1083 行: `The following figure presents the calculated reflectivity $R_{\lambda}(\omega)$ spectra of $\alpha$-Beryllene and $\beta$-Beryllene for the in-plane and out-of-plane directions:`
- 第 1144 行: `The following figure presents the calculated energy-loss $L_{\lambda}(\omega)$ spectra of $\alpha$-Beryllene and $\beta$-Beryllene for the in-plane and out-of-plane directions:`
- 第 995 行: `These trends indicate that the phase response depends on both the optical direction and the crystal structure of the medium.`
- 第 1012 行: `This behavior shows that amplitude attenuation also depends on both the optical direction and the crystal structure of the medium.`
- 第 1097 行: `These trends reflect the combined role of the refractive index $n_{\lambda}(\omega)$ and the extinction coefficient $k_{\lambda}(\omega)$ in determining the surface reflectivity.`

一般理论、教材及 Recent first-principles studies... 背景段中的引用保留.
niu2024electronic 对应 Chapter 4 的异质结研究, 不是这六幅 beryllene 图的来源.
loss 部分另有物理论断修复, 引用随论断调整, 不计为额外图件来源清理.
不删除 bibliography 条目, 不声称全章每篇引文都已独立审核.

### 4.2 只有三处直接复述作纯压缩

第 758 行删除:

```latex
This static limit shows that directional absorption produces directional dielectric response.
```

完整重复前一句 directional absorption spectra → directional static dielectric responses.

第 765 行删除:

```latex
At this stage, we arrive at the static physical interpretation of the Kramers--Kronig relations for anisotropic media.
```

重复同段开头 Consequently, the static limit reveals the physical interpretation...; 后面的 We next... 衔接保留.

第 1099 行删除:

```latex
Accordingly, the complex refractive index $N_{\lambda}(\omega)$ directly determines the reflectivity $R_{\lambda}(\omega)$,
which characterizes the surface reflection of the medium.
```

前一句已说明 n 与 k 决定反射率, 此句没有增加定义; 后面的损失谱衔接保留.

这三项仅涉及静态解释与反射率结尾两处位置.
不删必要符号、推导、物理解释或过渡; 正确性修复造成的字数变化不冒充去重.

## 5. 与 Chapter 6 同步的事项

Chapter 6 的方法段与光学导言已经回指 Chapter 3.
本章新增来源说明即可形成前后呼应, 不再增加同义回指.
以下事项必须在采用光学修正时一起落实:

1. `src/project_3_main.tex:165`:
   对这两个已核实结构, 40 Å 是 full supercell height.
   涉及其他体系时逐体系核对, 不能依据两份结构就宣称所有 slab 已核实.
2. `src/project_3_main.tex:208–212` 与 SI 厚度列表:
   将厚度相关的归一化结果表述为
   `the effective dielectric response under the chosen thickness convention`,
   不称其为唯一无约定的 intrinsic 常数.
   beta 后处理与 SI 同时统一到约 5.855 Å.
   保持研究实际采用的 Yang/Gao 光学体积归一化;
   不未经论证将 zz 单独换成静电串联电容的逆介电修正.
3. `src/project_3_main.tex:724–727` 的面外 extinction,
   最小候选为:

   ```latex
   In the out-of-plane channel,
   $\beta$-beryllene develops its strongest extinction in the ultraviolet region.
   ```

4. `src/project_3_main.tex:747–752` 的 loss 比较,
   与第 3 节替换段一致: 可见峰不是更强的峰,
   alpha 面外深紫外主峰更高, 图像必须恢复完整纵轴.
   不将窗口端点称为已捕获完整峰.
5. 具体 plasmon 能量、介电实部零点、实部异号区和吸收绝对值,
   必须用修正后的数组重核.
   beta 低能异号区在当前网格上约从 1.303–2.306 eV
   变成 1.323–2.226 eV, 原来的约 1.2–2.2 eV 不能机械保留.
   实部负值或两分量异号本身不能证明实际薄片的传播 plasmon 及其寿命.
6. 对 alpha/beta 六图, 方法段明确采用 IPA 带间谱, 未加入 Drude,
   并记录本稿 2.4 已核实的展宽与自旋设置.
   两套新版图继续保留这一原计算范围, 不擅自补经验 Drude.
   将 SI 中 NBANDS 的称呼改为计算总能带数, 不是未占据能带数.
   其他体系的实际设置另核, 不靠默认值推断.
   如果后续要解释金属完整低频响应, 须另行确定带内项的依据与阻尼,
   不能用这次后处理修正冒充已补齐.
7. 后续 Chapter 6 全章核查时, 检查其他 notebook 是否调用同一吸收函数,
   以及其他结构是否也错误使用分数坐标厚度.
   当前确认范围是这六对图; 不据此声称全部光学图已经正确.
   Chapters 4–5 若复用该库, 另查其实际版本与数据.

本轮不因后处理错误附加整套 HSE06 或 GW/BSE 补算.
若最终要保留的低能金属或集体激发结论需要额外计算,
应由对应研究章的证据缺口决定, 不由本章的示意公式预设规模.

## 6. 物理依据与边界

原来的 Maxwell → 响应 → IPA → 因果性 → KK → 派生光学量主线保留.
IPA 显式补 1/ω² 与占据差, 保留全张量骨架和 Dirac 矩阵元,
限定为本章采用的互易、实对称响应, 不冒充一般磁光表达式.
完整速度算符不能对非局域势直接替换为 p/m.
参见 [Gajdoš 等原文](https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevB.73.045112/fulltext),
正文沿用 `gajdovs2006linear`.

IPA 不含电子—空穴相互作用.
局域场、展宽、实际带内项应由研究章明确.
参见 [VASP LOPTICS](https://vasp.at/wiki/LOPTICS)
及 [VASP WPLASMAI](https://vasp.at/wiki/WPLASMAI).
Drude 式提供带内模型与 KK 导电极点的呼应,
不虚构 plasma frequency 或 damping 数值.

二维式复述的是研究采用的光学体积归一化.
参见 [Yang 与 Gao 原文 Eqs. 5、9](https://arxiv.org/pdf/2105.14689),
正文沿用 `yang2021method`.
采用这一模型不等于实际有限薄片的反射率可以无视厚度、基底与光学几何.
由 εzz 得到的标量 R 不是平面薄片正入射的第二个物理通道.

静态 KK 需要处理导电极点并满足积分收敛;
这不意味着金属不满足因果性或 KK.
参见 [Dressel–Grüner 教材](https://www.pi1.uni-stuttgart.de/img/head_of_institute/DresselGruner.pdf),
正文沿用 `dressel2002electrodynamics`.
loss 峰需结合 ε1 零点和 ε2 阻尼判断,
不将任意峰自动认定为 plasmon.

## 7. 回复信候选与旧模板纠正

以下仅在实际应用并完成图件和论文检查后使用.
本轮不将计划写成已经完成.

针对 Examiner 2 的来源问题:

```text
The optical examples for alpha-beryllene and beta-beryllene in Chapter 3 were calculated by the author for the study presented in Chapter 6.
The two chapters use different figure layouts of the same calculated spectra.
We have added a source statement before the first example, cross-references to the calculation methods and results, and source information in all six figure captions.
We have removed literature citation chains from the sentences introducing our figures and describing their calculated trends.
The examples are retained to illustrate the dielectric response and the optical quantities derived from it.
```

针对 Examiner 1, 应结合 Chapter 2 的二次核查定稿.
可使用以下如实描述实际动作的文字:

```text
We have provided a direct route to the practical methods in Section 2.6 and connected the optical-response discussion to the calculations in Chapter 6.
We have removed directly repeated statements while retaining the derivations needed for a continuous account of the theory.
We have clarified the assumptions behind the optical formulas and corrected the shared postprocessing of the illustrative spectra.
The revision provides a clearer route from the theoretical definitions to the calculations used in the research chapters.
```

这段不声称 Chapters 2–3 已大幅缩短.
若净页数没有减少, 回复中应明确说明, 并解释方法导航与去重的实际变化.
不能用删三句替代评审对整体比例的意见.

`reports/reply_to_examiners.md:21` 的旧模板写了
`Chapters 2 and 3 have been reduced in size (by x pages) by allocating sections x,y to a new Appendix.`
这项附录迁移并未发生, 最终必须以真实修改替换,
删除 `x pages` 和 `x,y` 占位符.
来源、适用范围、后处理和研究章独立要求分别回应,
不使用 `rectified this completely` 或“所有 reports 已满足”的总括承诺.

## 8. 应用顺序与检查

1. 固定原始数据与厚度约定, 修复后处理, 输出两种版式.
   比较数据、单位、坐标范围及完整峰高, 原始 HDF5 保持不变.
2. 应用第 3 节替换与第 4 节引用清理、直接重复删除.
   保留全部原 label、章节顺序和六个 figure 环境.
   原 52 组 equation 保留其推导位置和 label;
   IPA 及其能量守恒索引、磁导率式作局部更正,
   新增 Drude 与二维归一化两组 equation.
3. 同步第 5 节涉及的 Chapter 6 图件、厚度和文字.
   研究章尚未核实的收敛、其他体系的带内处理及激发归因不提前标记完成.
   本稿确认的两套 alpha/beta 数据无 Drude, 不再作为来源待确认项.
4. 正式编译后检查交叉引用、图目录、公式折行、图注与相邻解释,
   按论文实际尺寸看图, 记录真实页数.
5. 逐条回查原始 reports 与回复信, 如实区分来源要求的落实、
   最小去重与评审所要求的整体缩短, 不混淆二者.

### 8.1 本稿交付前已完成的检查

- 两份原始报告已读取; Gemini 初稿与当前论文源码逐项对照.
- 十二个 PDF 的归档身份、十个原始文件的哈希已核实.
  当前六图的 28 条曲线与旧后处理数值比对已独立复跑, 结果一致.
  两份实际输出的 WPLASMAI=0 已从 parameters 段确认.
- 全部候选已在临时 Chapter 3 副本试应用.
  63 个原 label、18 个标题与 6 个 figure 环境均保留,
  新增两个 label 唯一, 所有引用目标与 53 个文献 key 均存在.
- 使用论文实际 preamble、字体与页面宽度编译临时章,
  经 Biber 和引用重编译后无未定义引用、无公式或正文溢出.
  模板仍有 document-class 名称和 footnote 命令的既有提示.
  已查看 IPA、Drude、二维式、磁导率式及三处较长图注的渲染.
- 临时排版仍使用旧图, 只验证候选文字与公式能否正常显示,
  不等同于第 2 节图件重生成已经完成.
  正式整篇分页、图目录及新版曲线的视觉检查仍在实际应用时完成.
- TeXcount 的正文词数由 5,985 变为 6,218,
  图注等正文外文字由 123 变为 261, 标题词数不变.
  不计数学表达式, 合计净增约 371 个英文词.
  因此本方案是保留推导的局部纠错与必要说明, 不能报告为全章缩短.
- 论文源码、正式 PDF、文献库、Gemini 初稿和 Chapter 2 第一轮记录的
  26 项内容哈希均保持不变.
  新增的 [Chapter 2 二次核验稿](ai_ch2_second.md) 登记了与本章的指标联动.
