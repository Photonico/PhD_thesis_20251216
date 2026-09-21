# Chapter 2 二次核验与最小修改稿

日期: 2026-09-21.
依据: 当前 `src/fundamentals_a.tex`, 已应用的 [Chapter 2 修改操作稿](ai_ch2_last.md),
两份原始 examiner reports, 相关研究章的方法与结果, 以及下文列出的原始论文和官方方法说明.

本稿是已完成第一轮修改后的二次核验, 不替代 `ai_ch2_last.md` 的实施记录.
目前只提出候选修改, 尚未将下文写入 TeX.
本轮重点检查已经应用的章首导航, 2.5 泛函范围说明和新增 2.6,
以及它们与 Chapter 3 和研究章的联系.
这不表示原有 2.1–2.4 已经完成逐式独立核验.

继续遵循你的最新要求: 能少缩就少缩, 只有明显重复才缩.
保留必要公式, 符号解释, 物理含义和前后呼应;
不为回应篇幅意见而删除推导, 改成提纲, 移入附录或缩小排版.
这取代较早流程中针对本章的泛化删减建议.

## 1. 二次核验结论

当前修改已经建立了一条可以直接阅读的实际方法路线.
章首第 21–23 行引导读者进入 2.6;
2.6 依次说明结构优化与收敛, Brillouin-zone 采样, 声子与 AIMD,
自旋与磁序, EPC 与超导, SOC 与拓扑分析,
并连接前面的理论和后面的研究问题.

对新增公式的单位, 归一化和适用条件复核后,
没有发现需要重写整个 2.6 的科学错误.
建议只做下文三处最小修订, 其中一处随 Chapter 3 的指标修改联动;
另列两处可选的措辞调整.
未发现新增 2.6 中有明显到需要删掉的重复解释.
各段对前式和后章的回指承担不同的说明作用, 应继续保留.

机械核对结果如下:

- `ai_ch2_last.md` 中三个 LaTeX 候选块均逐字存在于当前源码中.
- 新增 2.6 引用的正文与公式目标均存在, 没有发现这些目标重复定义.
- 本轮没有修改 TeX, 没有重新编译 Chapter 2, 也没有把上一轮的排版检查说成本轮检查结果.

## 2. 两份原始报告: 已回应与仍开放的部分

### 2.1 Examiner 1

依据为 `reports/Lu_Niu_PhD_report_20260824.pdf`, 第 1 页关于 Chapters 2–3 的专门段落,
以及第 2 页关于 Chapter 5 超导流程和理论局限的段落.
本轮直接读取了原 PDF, 没有只依赖 AI 汇总.

该报告同时提出两类要求:

- 给出简明而实用的方法路线, 包括 geometry optimisation, convergence,
  k-point sampling, phonons, AIMD, spin polarization and magnetic ordering,
  electron–phonon coupling and superconductivity, SOC and topology,
  并与研究章的科学问题连接.
- 缩短并围绕实际方法重组 Chapters 2–3.

当前新增 2.6 已覆盖第一类要求列出的全部方法主题,
章首导航也提供了直接阅读入口.
但方法概览不等于每个体系的计算已经可复现;
研究章仍需提供和核实真实设置.

第二类要求不能标记为完全满足. 原报告明确写道:

> These chapters should be shortened and reorganised around the methods actually used.

当前选择保留原有推导并新增方法节, 没有缩短 Chapter 2,
也没有将原理论章节整体改成按实际计算方法编排.
回复应如实说明这一选择和阅读改进,
不能把“增加导航与方法节”写成“已经缩短并重组”.
是否接受这种保留方式属于后续评审判断;
本稿不以此为理由要求你删去原文.

### 2.2 Examiner 2

依据为 `reports/PhD Examination Report - Lu Niu.docx`.
本轮直接读取了原 DOCX 全文.
报告中以 `Chapters 2 and 3 give almost textbook version...` 开头的段落,
肯定了理论说明的清楚程度及其对后续研究的基础作用.
紧接的具体纠正要求是 Chapter 3 中 alpha/beta-beryllene 光学示例的来源.
它没有要求删除 Chapter 2 的理论推导.

该报告在 `Weaknesses of Chapter 6` 中提出的第 1, 2, 5 项仍需由 Chapter 6 回答:

- PBE-only 的实际理由及其限制.
- 收敛程序和选择具体 k-point meshes 的依据.
- AIMD 的实际系综, 温度, 时间步长和总时长.

Chapter 2 的通用说明有助于读者理解这些方法,
但不能代替上述真实设置, 也不能代替 Chapter 3 的图件来源说明.

## 3. 推荐修改一: 明确 EPC 谱函数的金属参考态

位置: `src/fundamentals_a.tex:3430`,
`eliashberg_spectral_function_method` 之前.

当前句子只写 `For a spin-degenerate reference state`,
而随后谱函数使用费米面平均并除以 $N(E_\mathrm{F})$.
因此应明确这里要求具有非零费米能级态密度的金属正常态.
这也能避免把 Chapter 5 的 HSE06 AFM 半导体状态
直接当作后续 PBE/QE EPC 计算的参考态.

将当前这一句替换为:

```latex
For a spin-degenerate metallic normal state with $N(E_\mathrm{F})>0$,
we use the density of states per unit cell and per spin at the Fermi energy.
```

其余谱函数公式, 自旋计数, k/q 权重和解释全部保留.
这只是补足现有公式的适用前提,
不替 Chapter 5 确认其实际电子或磁参考态,
也不在本章增加自旋极化超导方程.

现有 `giustino2017electron` 和 `margine2013anisotropic` 可继续支持这一方法背景.
核验参考: [EPW theory](https://docs.epw-code.org/Theory.html).

## 4. 推荐修改二: 连接 HSE 能量形式与 generalized Kohn--Sham 算符

位置: `src/fundamentals_a.tex:3116` 后,
即 `Moreover, $a$ refers to the mixing parameter...` 之后,
`In the standard HSE06 functional,` 之前.

当前 2.5 给出了 HSE 的混合能量表达式,
2.6 第 3365 行又回指这里的 non-local exchange contribution.
这个回指的方向正确, 但前文尚未明确说明轨道依赖
如何连接到 generalized Kohn--Sham 算符.
增加两句即可补上这一步:

```latex
The Hartree--Fock exchange term depends explicitly on the occupied orbitals.
In the generalized Kohn--Sham treatment used for hybrid functionals,
its orbital variation gives a non-local exchange operator.
```

保留原来的 $E_\mathrm{xc}^\mathrm{HSE}[n]$ 简写,
不展开 Fock 算符推导, 不更名已有公式或 label.
这也能支撑 Chapter 3 对完整速度算符及非局域项的说明.

这里特意限定 `In the generalized Kohn--Sham treatment`.
显式轨道泛函也可以通过 optimized effective potential 方法构造局域势,
因此不能无条件写成“轨道依赖必然只能产生非局域势”.

正文可沿用本小节已有的 `heyd2003hybrid` 等文献,
不为这两句自动添加未经检查的新 bib key.
独立核验依据为
[Seidl et al., Generalized Kohn-Sham schemes and the band-gap problem](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.53.3764)
及 [VASP 对 hybrid 非局域 Fock 项的说明](https://vasp.at/wiki/WRT_POTENTIAL).

## 5. 推荐修改三: 随 Chapter 3 同步光学能带指标

位置: `src/fundamentals_a.tex:3245–3246`,
回指 `independent_particle_imaginary_dielectric_tensor` 的句子.

当前 Chapter 3 仍用价带 $v$ 和导带 $c$ 写 IPA 公式,
所以 Chapter 2 现有 $E_{c\vec{k}}-E_{v\vec{k}}$ 与它一致.
这不是当前已有的指标错误.

若 Chapter 3 按本轮方案采用一般能带 $n,m$ 和占据差,
这里必须同步, 使金属的部分占据也进入方法衔接.
保留引入句, 将其后的说明改为:

```latex
In equation~\eqref{independent_particle_imaginary_dielectric_tensor} of chapter~\ref{cha:fundamentals_b},
the integrand also contains occupation factors, transition matrix elements,
and the energy difference $E_{m\vec{k}}-E_{n\vec{k}}$.
```

这是条件性联动项, 应与 Chapter 3 的 IPA 式一起应用.
章末第 3584–3587 行从电子态转向电磁响应的衔接已经自然,
无需再加同义段落.

## 6. 两处可选小改

### 6.1 更直接回应 self-interaction 与 delocalisation 的解释

位置: `src/fundamentals_a.tex:3133`.

现有第 3082 行已提及 self-interaction,
第 3133–3137 行又说明局域化, 带隙以及 HSE06 的近似性质.
因此不是缺少整段 PBE/HSE 讨论.
若希望更直接对应 Examiner 1 的措辞,
可以只替换第 3133 行:

```latex
The screened exchange contribution in equation~\eqref{HSE_exchange_correlation_functional}
can reduce self-interaction and delocalisation errors,
thereby changing the localization of electronic states and the predicted band gap.
```

紧随其后的 `However, HSE06 remains an approximation.`
和 `A larger band gap does not by itself imply a more accurate result.` 保留.
用 `can` 表示可能改善, 不把某个体系的具体变化提前归因完毕.
具体 PBE/HSE 差别仍由对应结构, 磁态和计算结果解释.

### 6.2 去掉泛函层级中的无条件精度判断

位置: `src/fundamentals_a.tex:3005`.

原句 `More accurate semilocal approximations also include the density gradient.`
容易把“包含更多信息”写成对所有体系都保证更准确.
可作词级调整:

```latex
Semilocal approximations also include the density gradient.
```

这与后文对近似和精度范围的说明一致.
不需要重写原有 LDA, GGA, PBE 和 HSE06 的解释链.

## 7. 已核验且建议保持的新增内容

以下定位对应当前 `src/fundamentals_a.tex`:

- 第 3174–3215 行: 完整 BO 能量连接电子能量与核间排斥,
  再定义力和示意停止条件; 同时区分停止条件与 cutoff/k-grid 的数值收敛.
- 第 3253–3326 行: 力常数, 质量加权动力学矩阵, 相位约定,
  声子本征矢归一化和角频率定义一致;
  声子与短时 AIMD 的证据范围已经区分.
- 第 3331–3390 行: Dirac 形式的自旋密度, 半局域自旋势,
  同大小与成分单胞的每原子 AFM–FM 能差, 以及局域磁矩的辨别均合理.
- 第 3402–3484 行: EPC 的多原子质量因子,
  cell-periodic 态与扰动相位约定, $g$ 的能量单位,
  k/q 权重与 per-spin DOS 计数相互一致.
  采用能量 delta 函数后, 无量纲谱函数与 $\lambda$ 的积分一致;
  $\omega_\mathrm{ref}$ 使对数无量纲且从最终 $\omega_\mathrm{log}$ 中消去.
- 第 3486–3515 行: 明确区分简化 Allen--Dynes 式与完整修正,
  显式恢复频率到温度所需的常数, 并排除非正分母的机械外推.
  各向异性 Migdal--Eliashberg 计算没有被误写成只依赖平均谱函数.
- 第 3520–3581 行: spinor, 固定 $2N_\mathrm{p}$ 带子空间,
  全 Brillouin zone 的直接能隙, TRIM 宇称配对,
  以及绝缘占据态的条件已经分别交代.
  没有由金属中的宇称乘积直接认定拓扑绝缘体.

这些内容无需再增加第二套公式, 方法汇总表或重复结论.
上述核验针对理论关系与其当前说明,
不等于实际计算输入输出也已验证.

## 8. 研究章仍须关闭的依赖项

继续保留 `ai_ch2_last.md` 第 8 节的跨章核查项.
这些不是需要重新塞进 Chapter 2 的内容,
也不意味着现在一律安排补算.

1. Chapter 4:
   核对不同泛函下的结构与光学设置, 能带数, 网格和各自的收敛依据.
   当前 `src/project_1_main.tex:103–105` 对 HSE06 更准确的表述,
   应与 Chapter 2 的限定保持一致.
   第 113 行把 $\omega$ 直接称为以 eV 表示的 photon energy,
   需要随 Chapter 3 的角频率与光子能量约定一起回查.
2. Chapter 5 的 EPC 与超导:
   当前 `src/project_2_main.tex:230–252` 已列出 PBE/QE,
   norm-conserving pseudopotentials, 部分 k/q 网格, Wannier90, EPW,
   以及 $\mu^*=0.13$; 不应把这些现有参数再次当作全部缺失.
   仍需从记录区分 coarse/fine meshes, 积分与展宽,
   实际电子和磁参考态, $\omega_\mathrm{log}$,
   Allen--Dynes 的具体形式及各向异性计算的温度判据.
   第 638 行的 $\lambda=0.05$ 与第 250 行的 $\mu^*=0.13$
   使本章简化 AD 式的分母为负,
   不能机械代入来证明 negligible $T_\mathrm{c}$.
   Chapter 2 已正确排除此误用, 原结论依据仍需在 Chapter 5 说明.
3. Chapter 5 的磁性与光学:
   核实 AFM–FM 能差的归一单位和误差尺度,
   并识别实际光学计算的结构, 泛函, 磁态和带内处理.
   HSE06 AFM 半导体与 PBE/QE 的 EPC 正常态不能未经核验视作同一状态.
4. Chapters 5–6 的稳定性:
   对照真实输入与轨迹说明系综, 温度, 热浴, 步长, 时长和超胞,
   核对虚频解释及图件身份.
   理论上区分 phonons 与 AIMD, 不等于这些真实设置已经补齐.
5. Chapter 6:
   第 155 行目前陈述采用 PBE,
   仍需补充选择理由与预测范围;
   Chapter 2 第 3139 行的 `We discuss this choice...` 是待落实的跨章联系.
   同时核验 SOC, 对称性, 固定带子空间及全 Brillouin zone 隔离条件.
6. Chapter 3:
   本轮 [ai_ch3_last.md](ai_ch3_last.md) 已核实两套图共用数据,
   以及 alpha/beta 原始数组未加入 Drude.
   已提出 IPA, 频率换算, 厚度及损失谱的具体修订.
   这些仍属待应用方案, 不写成图件已经修好.
   采用一般能带指标后, 同步本稿第 5 节.

各项关闭后, 再回到 Chapter 2 更新确有变化的方法概述.
在此之前, 回复只能说本章已经提供方法导读与必要理论关系,
不能说全篇计算已经可复现或所有评审方法问题已经解决.

## 9. 应用顺序与检查

1. 先采用 EPC 金属参考态和 HSE/GKS 连接两处短修订.
2. 随 Chapter 3 IPA 公式定稿, 同步一般能带指标与占据因素.
3. 两处可选措辞调整按需要采用, 不因此扩展改写范围.
4. 更新 `ai_ch2_last.md` 时保留其作为第一轮实施记录的性质;
   本轮新增修订由本文件记录, 不把第一轮的字数与页数统计当作二次修改后的结果.
5. 实际修改后检查引用, 数学符号和分页.
   不重命名现有 label, 不改变 Dirac notation 或原有 TeX 间距习惯.
6. 回复信按实际完成状态表述:
   方法导航与通用说明已经改善;
   理论推导保留, 不声称 Chapter 2 已缩短;
   实际设置与 Chapter 3 图件来源等仍由对应章节完成后统一回复.

本稿不要求再增长整个 2.6,
也不将为讲清物理过程而保留的回扣与承接当作明显重复.
