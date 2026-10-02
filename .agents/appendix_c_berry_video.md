# Appendix C 与 Berry 视频的对照

核对日期: 2026-10-03.

视频: `~/Repos/subtitles/raw videos/Deriving Berry phase, Berry connection & Berry curvature.mp4`,
时长 34:59. 核对依据为完整本地音频转录和画面中的公式.
对应正文为 `src/appendix_topology.tex`, 保留当前标题 `A prelude into topology`.

## 原稿覆盖了多少?

原稿已有视频前约 27 分钟的大部分基础推导, 以及最后的多带矩阵连接与曲率.
欠缺的是仅保留动力学相位为何不够的显式计算、协变导数、投影算符表达的辨析,
以及后半段的电磁类比、Hall 响应和微分形式.
按知识点对照如下; 时段是主题位置, 不表示其中每一句均应搬入 thesis.

- 03:11–09:54, 绝热演化与相位分离: 原稿已完整建立主要公式.
  补入只保留动力学相位时的 Schrödinger 方程残差, 解释额外相位的来由.
- 09:54–13:14, 相位为何是实数: 原稿已有归一化求导证明,
  并说明 Berry connection 的实数性; 保留这一推导.
- 13:14–21:23, connection、离散重叠和平行输运: 原稿已有相邻重叠、闭路重叠积和局部相位条件.
  补入协变导数及其正交投影表达, 并明确有限网格上重叠积的模不等于相位.
- 21:23–24:54, 规范变换: 原稿已有 connection 的变换、开放路径端点项和闭路不变性.
  沿用统一的负号约定, 保留开放路径需要端点比较的说明.
- 24:54–30:50, curvature、电磁类比和 Hall 响应: 原稿已有曲率和 Stokes 关系.
  补入三维曲率向量、电磁类比、反常速度、内禀 Hall 公式及 Chern 数的简短解释.
  自旋 Hall 仅交代与电荷 Hall 的区别及 SOC 下的限制.
- 30:50–34:59, 微分形式与多带推广: 原稿已有矩阵 connection、曲率和规范协变性.
  补入一形式、二形式、楔积与矩阵形式的衔接.

修改后覆盖视频六部分的主要物理与数学内容.
原有两分量态算例、三张示意图和时间反演推导保留;
口头重复、应用宣传和书籍推荐不写入正文.

## 学习时应修正的视频公式

全文沿用 $\vec{\mathcal{A}}=\mathrm{i}\langle u|\nabla u\rangle$ 的约定.

1. 约 15:00–17:10, 视频写 connection 可由
   $\mathrm{i}\operatorname{Tr}[P\nabla P]$ 得到. 对固定秩投影算符,
   $\operatorname{Tr}[P\partial_iP]=\tfrac12\partial_i\operatorname{Tr}P^2=0$,
   因而这不是 connection. 正确的单带曲率表达是
   $\mathcal{F}_{ij}=\mathrm{i}\operatorname{Tr}[P[\partial_iP,\partial_jP]]$.
   与此相关的投影算符离散推导也不能直接采用; 正文沿用闭路重叠积的 argument.
2. 约 21:10, 视频把 $D_s|u\rangle=0$ 写成一般的平行输运条件.
   实际上 $D_s|u\rangle=(I-P)\partial_s|u\rangle$ 可以非零.
   水平相位选择要求 $\langle\bar u|\partial_s\bar u\rangle=0$,
   不要求整个态停止变化.
3. 约 23:20, 对 $|u'\rangle=\mathrm{e}^{\mathrm{i}\varphi}|u\rangle$,
   正确变换为 $\vec{\mathcal{A}}\,'=\vec{\mathcal{A}}-\nabla\varphi$.
   视频在同一定义下写成加号; 开放路径端点项的符号也应相应修正.
4. 约 32:50–33:00, 三维曲率的 $y$ 分量应为
   $\Omega_y=\mathcal{F}_{zx}=-\mathcal{F}_{xz}$,
   不能直接写为 $\mathcal{F}_{xz}$.
5. 约 34:10, 当前 connection 约定对应
   $\mathcal{F}_{ij}=\partial_i\mathcal{A}_j-\partial_j\mathcal{A}_i
   -\mathrm{i}[\mathcal{A}_i,\mathcal{A}_j]$.
   视频使用的正交换子符号不适用于此前定义.

此外, connection 的方向取决于规范, 因而不能把“路径顺着 connection 的方向”
解释为一个规范无关的最大 Berry 相位原则.
普通 Hall 效应的实空间 Lorentz 力、Berry curvature 对速度的修正,
以及需要自旋流矩阵元的自旋 Hall 响应也应区分.

正确关系使用已有 Berry (1984)、Wilczek–Zee (1984)、Xiao–Chang–Niu (2010) 引文,
反常速度另补入 Sundaram–Niu (1999):
[Wave-packet dynamics in slowly perturbed crystals](https://arxiv.org/abs/cond-mat/9908003).

## 阅读顺序

先读绝热相位分离与归一化求导, 再读相邻重叠、规范变换和平行输运.
随后用两分量态算例核对 connection、curvature 和闭路相位,
最后读微分形式及多带推广. Hall 小节用于理解曲率的物理作用.

本次新增 8 组显示公式, 原有 label 保留.
Appendix C 从 14 页增加至 18 页; Chapter 4 的篇幅未增加.
