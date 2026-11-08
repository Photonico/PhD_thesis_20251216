# 范例与改写示例

本文件配合 `../SKILL.md` 使用.
第一部分逐字摘录作者语料中的典型段落, 并标出它体现的规则.
第二部分给出改写示例, 原文取自需要统一风格的章节.
摘录中省略的引用键写作 `\cite{...}`.

## 第一部分: 原文范例

### A1. 章的开头: 定位, 物理动作链, 方法路线

`src/fundamentals_b.tex`, 第 5 至 9 行:

```latex
We continue our discussion of the fundamentals in this chapter, where we introduce the linear optical response of matter.
The interaction between materials and light occurs through the response of electrons to the electric-field component of incident radiation.
This response induces polarization and produces electronic excitations, including interband transitions and plasmonic charge excitations.
Collectively, these processes determine the dielectric function, plasmonic behaviour, absorption, reflection, refraction, and energy loss.
We therefore use linear response theory to connect the electromagnetic field to the dielectric response of the medium.
```

- 第一句给出本章在理论链条中的位置.
- 第二到四句是物理动作链: 光场作用于电子, 电子产生极化和激发, 这些过程决定可观测量.
- 最后一句用 We therefore 给出方法路线, 并以 the medium 收尾.

### A2. 节的开头: 回扣上一节, 列出本节路线

`src/fundamentals_b.tex`, 第 63 至 75 行:

```latex
The previous section introduced the constitutive relations for optical response.
There, we introduced the polarization field $\vec{P}(\vec{r},t)$,
the electric susceptibility tensor $\chi_{\alpha\beta}(\omega)$,
and the dielectric tensor $\varepsilon_{\alpha\beta}(\omega)$.
These quantities connect the applied field to the response of matter.
We now recover the response function that electronic structure calculations actually provide,
which is the frequency-dependent dielectric function~\cite{...}.

In this section, we start by expressing the polarization response in the language of electric susceptibility and the complex dielectric function.
We then identify the microscopic electronic processes that generate its imaginary part.
Next, we formulate this response for anisotropic systems,
since the present work compares the in-plane and out-of-plane optical channels explicitly.
Therefore, we advance from the general constitutive picture to a response function that can be calculated, interpreted, and subsequently converted into optical observables.
```

- 回扣时, 物理量的名称和符号同时给出.
- 路线用 start by, then, Next, Therefore 串联, 最后一句说明本节从哪里走到哪里.

### A3. 先讲物理动作, 再写公式

`src/fundamentals_b.tex`, 第 86 至 102 行:

```latex
Under a monochromatic electric field, part of the polarization stays in phase with the field,
while another part lags behind it.
The first part stores energy in the medium, and the second part transfers energy from the field into the medium.
We therefore write the dielectric tensor in complex form as:

\begin{equation}
    \varepsilon_{\alpha\beta}(\omega)
    = \varepsilon_{1,\alpha\beta}(\omega)
    + \mathrm{i}\,\varepsilon_{2,\alpha\beta}(\omega)
\label{complex_dielectric_tensor_definition}
\end{equation}

here, $\varepsilon_{1,\alpha\beta}(\omega)$ denotes the real part of the dielectric tensor,
and $\varepsilon_{2,\alpha\beta}(\omega)$ denotes the imaginary part of the dielectric tensor.

The real part denotes the dispersive part of the response.
It describes how the medium polarizes with the field and therefore how it stores electromagnetic energy.
```

- 公式出现之前, 读者已经知道实部和虚部各自对应的物理动作: 同相部分储能, 滞后部分吸能.
- 公式前是冒号, 公式末尾无标点, 公式后以小写 here 解释符号.
- 最后一句含 how 从句. 按 SKILL.md 3.4 可改为: `It describes the in-phase polarization of the medium, which stores electromagnetic energy.`

### A4. 先一般, 后近似

`src/appendix_electrodynamics.tex`, 第 138 至 159 行:

```latex
Firstly, we start from the most general linear-response form.
For any time $t$, the polarization may depend not only on the electric field at the same point,
but also on fields acting earlier and in a surrounding spatial region.
Therefore, before introducing the simplified form used in the present work,
we write the constitutive relation in its general nonlocal form in space and time~\cite{...}:

\begin{equation}
    P_\alpha(\vec{r},t) =
    \varepsilon_0\sum_\beta\int\dif^3{r'}
    \int_{-\infty}^{t}\dif{t'}
    \,\chi_{\alpha\beta}(\vec{r},t;\vec{r}\,',t')\,E_\beta(\vec{r}\,',t')
\label{general_nonlocal_constitutive_relation}
\end{equation}

here, $\chi_{\alpha\beta}(\vec{r},t;\vec{r}\,',t')$ describes the contribution of the electric field acting at $(\vec{r}\,',t')$ to the polarization that develops later at $(\vec{r},t)$.
In this sense, the medium does not have to respond only at one point and one instant;
instead, it may spread the response over space and retain memory in time.
At the same time, the upper limit $t$ in equation~\eqref{general_nonlocal_constitutive_relation} keeps the causal order explicit: the perturbation acts first, and the response follows.

For the present work, we focus on the linear response in the long-wavelength regime.
Under this approximation, spatial nonlocality drops out, and the constitutive relation retains only the memory of the earlier perturbation.
Therefore, it reduces to the time-domain constitutive relation:
```

- 一般形式先给出, 并用物理语言解释其中的非局域性和记忆效应.
- 近似条件单独一句, 被丢掉的部分和保留的部分在下一句里并列.
- the medium 是动作主体: spread the response, retain memory.
- `the perturbation acts first, and the response follows` 用两个短分句讲清因果顺序.
- 按 SKILL.md 第 5 节, 其中的分号可改为句号加 Instead.

### A5. 命名新量

`src/fundamentals_a.tex`, 第 880 至 889 行:

```latex
For comparison, the kinetic energy functional $T[n]$ appearing in the Hohenberg--Kohn functional $E_\mathrm{HK}[n]$ is evaluated on the minimizing interacting many-body state $\Psi[n]$ that yields the same density.
In general, $T[n]$ and $T_s[n]$ are not equal, and we write their difference as:

\begin{equation}
    T[n]=T_s[n]+T_c[n]
\label{T_decomposition}
\end{equation}

here, $T_c[n]$ measures the kinetic correlation beyond the noninteracting reference.
We name it the kinetic-correlation functional.
```

- 新量出现后立即用 `We name it the ...` 给出名字, 之后正文可以直接使用这个名字.

### A6. 叙述一个计算流程

`src/fundamentals_a.tex`, 第 1543 至 1548 行:

```latex
Next, the Hartree equations already demonstrate the basic one-particle structure of a self-consistent field theory.
We start from a trial density,
construct the Hartree potential $v_\mathrm{H}([n];\vec{r}\,)$,
solve equation~\eqref{Hartree_equations_expansion},
update the density through equation~\eqref{density_with_occupation_number},
and repeat these steps until convergence is reached.
```

- 一个 we 带出一串并列的动词, 每个动词一行, 读者看到的就是算法本身.

### A7. 用作用路径解释公式

`src/fundamentals_a.tex`, 第 1511 行, 解释逆 Kohn--Sham 迭代的更新公式:

```latex
Accordingly, the Kohn--Sham potential is increased where the density is overestimated and decreased where it is underestimated.
```

`src/fundamentals_b.tex`, 第 412 至 414 行, 解释静态极限的积分权重:

```latex
Next, the factor $1/\omega'$ gives higher weight to low-energy spectral contributions.
The dominant contribution nevertheless depends on the spectral weight over the full energy range.
Therefore, the static limit represents an accumulated response over the full absorption spectrum.
```

- 不复述公式, 而是说明公式中的某一项对物理量做了什么.

### A8. 小节的结尾

`src/fundamentals_b.tex`, 第 135 至 140 行:

```latex
At this stage, we arrive at the complex dielectric function as the central response quantity for discussing optical performance.
When we enter the frequency domain, the optical response no longer appears as a static redistribution of charge;
instead, the field drives the electrons continuously, and the medium responds with a frequency-dependent polarization.
Within this complex quantity, microscopic electronic processes generate the imaginary part $\varepsilon_2(\omega)$,
while the Kramers--Kronig relation determines the real part $\varepsilon_1(\omega)$~\cite{...}.
We now turn to the microscopic origin of the imaginary part $\varepsilon_2(\omega)$.
```

- 收束句点名结果, 并说明它的角色.
- 中间两句把实部和虚部的来源用 while 并列.
- 最后一句引出下一小节.

### A9. 故事引子, 只用于章或附录的第一段

`src/appendix_quantum.tex`, 第 18 至 25 行:

```latex
Imagine that we are watching the evolution of electrons and atoms as a microscopic performance.
You blink, and suddenly the stage configuration has shifted.
Something has changed. But how do we describe this evolution in physical language?

In classical physics, we started with Newton's laws to describe motion.
Later, Lagrangian and Hamiltonian mechanics provided a different framework for describing physics from the perspective of degrees of freedom, symmetries, and conservation laws.
The twentieth century then brought the quantum revolution, establishing quantum mechanics as the fundamental framework for describing microscopic physics.
In this new framework, the Schrödinger equation plays the central role.
```

- 引子是短句, 用一个设问把读者带到本章的核心对象.
- 第二段立即回到历史和物理脉络, 最后一句点出核心方程.

### A10. 短句定调

`src/appendix_electrodynamics.tex`, 第 21 至 22 行:

```latex
Therefore, before introducing the dielectric function, we need a language that describes both the applied field and the feedback of matter to that field.
That language is electrodynamics.
```

- 一个长句提出需求, 一个短句给出答案.

### A11. 带名称的方程组

`src/appendix_electrodynamics.tex`, 第 44 至 56 行:

```latex
\begin{equation}
\left\{\begin{aligned}
    \nabla\cdot\vec{E}(\vec{r},t) &= \frac{\rho(\vec{r},t)}{\varepsilon_0}
    &&\space \text{Gauss's law for electric field} \\
    \nabla\cdot\vec{B}(\vec{r},t) &= 0
    &&\space \text{Gauss's law for magnetic field} \\
    \nabla\times\vec{E}(\vec{r},t) &= -\frac{\partial}{\partial t}\vec{B}(\vec{r},t)
    &&\space \text{Faraday's law} \\
    \nabla\times\vec{B}(\vec{r},t) &= \mu_0\vec{J}(\vec{r},t)+\mu_0\varepsilon_0\frac{\partial}{\partial t}\vec{E}(\vec{r},t)
    &&\space \text{Ampère--Maxwell law}
\end{aligned}\right.
\label{maxwell_equations_with_total_sources}
\end{equation}
```

### A12. whereas 对照对

`src/fundamentals_b.tex`, 第 557 至 558 行:

```latex
The refractive index determines the phase evolution,
whereas the extinction coefficient describes the attenuation of the wave amplitude.
```

## 第二部分: 改写示例

### B1. 防御性否定句改为肯定句

原文, `src/project_3_main.tex`, 第 1011 至 1018 行:

```latex
For $\beta$-beryllene,
the in-plane real part contains zero crossings and a low-energy interval in which its sign differs from the out-of-plane component.
On the calculated grid, these components have opposite signs from approximately \qtyrange{1.22}{2.21}{\electronvolt};
these are sampled endpoints rather than interpolated zeros.
For $\alpha$-beryllene, the out-of-plane real part crosses zero near \qty{10.64}{\electronvolt}, where the imaginary part is comparatively small.
The sign changes and loss features identify candidate energy ranges for further analysis of collective response.
They do not by themselves establish propagating modes in a finite two-dimensional layer or determine their lifetimes.
The numerical broadening is an input to the calculation, not a calculated scattering lifetime.
```

改写:

```latex
We first follow the sign of the real part $\varepsilon_{1}(\omega)$.
For $\beta$-beryllene, the in-plane component crosses zero at low photon energy and takes the opposite sign to the out-of-plane component.
The two components keep opposite signs between approximately \qty{1.22}{\electronvolt} and \qty{2.21}{\electronvolt}, the endpoints sampled on the calculated energy grid.
Over this interval, $\beta$-beryllene behaves as an indefinite medium.
For $\alpha$-beryllene, the out-of-plane component crosses zero near \qty{10.64}{\electronvolt}, where the imaginary part $\varepsilon_{2}(\omega)$ remains comparatively small.
These sign changes, together with the loss features below, locate the candidate energy ranges of collective electronic response.
A finite-momentum calculation determines the dispersion of such modes in the two-dimensional layer, and a carrier-scattering treatment determines their lifetimes.
The broadening of \qty{0.1}{\electronvolt} enters the present spectra as a numerical parameter.
```

- 原文的四条限制全部保留: 端点是采样值, 只是候选能区, 传播模式和寿命需要另行计算, 展宽是数值参数.
- 每条限制改写为 "什么决定什么" 的肯定句, 否定词从 4 个减到 0 个, 分号去掉.
- indefinite medium 沿用第 6 章的定义, 即面内与面外的 $\varepsilon_1$ 符号相反. 使用前请核对数据.

### B2. why 从句改为陈述句

| 原文 | 改写 |
| --- | --- |
| `To understand why there are only four, we rewrite equation~\eqref{trim_condition_topology} as $2\vec{\Lambda}_i=\vec{G}_i$.` (`fundamentals_c.tex`, 第 296 行) | `We count these points by rewriting equation~\eqref{trim_condition_topology} as $2\vec{\Lambda}_i=\vec{G}_i$.` |
| `This is why we compare optical properties alongside the band structures of the isolated layers, heterostructures, and hydrogen-functionalized systems.` (`introduction.tex`, 第 250 行) | `We therefore compare the optical properties together with the band structures of the isolated layers, heterostructures, and hydrogen-functionalized systems.` |
| `This comparison illustrates why the coupling constant alone does not determine $T_{\mathrm{c}}$. The phonon frequencies entering the pairing problem also control its energy scale.` (`conclusion.tex`, 第 63 至 64 行) | `The logarithmic phonon frequency $\omega_\mathrm{log}$ therefore enters $T_\mathrm{c}$ together with the coupling strength $\lambda$.` |

### B3. 规定式 must 改为陈述句

| 原文 | 改写 |
| --- | --- |
| `The ensemble, temperature control, time step, and duration must therefore be specified with each calculation.` (`fundamentals_a.tex`, 第 2022 行) | `Each research chapter therefore reports the ensemble, thermostat, time step, and duration of its trajectories.` |
| `The datasets and their convergence settings must be specified for each calculation.` (`fundamentals_a.tex`, 第 1885 行) | `The research chapters report the datasets and their convergence settings.` |

### B4. 重复的公式改为引用

原文, `src/appendix_electrodynamics.tex`, 第 364 至 371 行, 再次显示了第 199 至 203 行已经定义的 $\varepsilon_{\alpha\beta}=\delta_{\alpha\beta}+\chi_{\alpha\beta}$:

```latex
We then express the dielectric tensor $\varepsilon_{\alpha\beta}(\omega)$ via the electric susceptibility tensor $\chi_{\alpha\beta}(\omega)$~\cite{...}:

\begin{equation}
    \varepsilon_{\alpha\beta}(\omega) =
    \delta_{\alpha\beta}
    + \chi_{\alpha\beta}(\omega)
\label{dielectric_tensor_from_susceptibility}
\end{equation}
```

改写:

```latex
The dielectric tensor $\varepsilon_{\alpha\beta}(\omega)$ then follows from the susceptibility through equation~\eqref{dielectric_tensor_definition}.
```

删除旧 label 前, 先把所有 `\eqref{dielectric_tensor_from_susceptibility}` 改指 `dielectric_tensor_definition`.

### B5. 分号与 "not merely" 改为两句肯定句

原文, `src/fundamentals_a.tex`, 第 79 行:

```latex
This is not merely a change of notation; it marks the conceptual compression from a function of $3N$ variables, $\Psi_0(\vec{r}_1,\cdots,\vec{r}_N\,)$, to a function of only three spatial variables, $n(\vec{r}\,)$, which is the cornerstone of the practical formulation of DFT.
```

改写:

```latex
This step compresses a function of $3N$ variables, $\Psi_0(\vec{r}_1,\cdots,\vec{r}_N\,)$, into a function of three spatial variables, $n(\vec{r}\,)$.
This compression forms the basis of practical density functional theory.
```

### B6. 非母语用法

| 原文 | 改写 |
| --- | --- |
| `Firstly, let us start by an interrelated two-body system consisting of two species.` (`fundamentals_a.tex`, 第 642 行) | `Firstly, let us start with a system that contains two species of particles.` |
| `Therefore, in this noninteracting Kohn--Sham auxiliary system, we process the corresponding total ground-state energy as a functional of the density, and denote it by $E_s[n]$.` (`fundamentals_a.tex`, 第 1053 行) | `Therefore, we treat the ground-state energy of this noninteracting auxiliary system as a functional of the density, and denote it by $E_s[n]$.` |
| `Schematically, it demonstrates as:` (`fundamentals_a.tex`, 第 1451 行) | `Schematically, it takes the form:` |
| `We adopt $i$ labels the electrons and $I$ labels nuclei.` (`appendix_quantum.tex`, 第 247 行) | `We use $i$ to label the electrons and $I$ to label the nuclei.` |
