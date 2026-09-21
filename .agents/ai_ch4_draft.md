# Chapter 4 草稿说明

日期: 2026-09-21.

正文: `src/fundamentals_c.tex`.
绘图: `figures_ch4/figures_ch4.ipynb`.
独立预览: `.output/ch4-draft/fundamentals_c_draft.pdf`.

## 内容与范围

草稿按 Chapters 2–3 的理论讲解方式组织为五节:

1. Bloch 态、相位自由度、固定带数的子空间及直接与间接带隙.
2. 相邻态的重叠、Berry connection、闭合回路的 Berry phase 与多态子空间.
3. 自旋时间反演、Kramers 配对、四个 TRIM、反演宇称.
4. 二维 Z2 分类、Fu--Kane 判据、额外晶体对称性允许的乘积简化.
5. 将上述条件连接到实际计算, 区分孤立带子空间的拓扑与费米能级处的绝缘态.

共 26 个编号公式环境、两幅示意图.
独立预览为 17 页正文与 1 页参考文献.
量子态采用 Dirac notation, 使用 `equation`、`aligned`、单行 label、
小写 `here,`、`\vec`、`\mathrm{i}`、`\dif` 和 `\coloneqq`.
物理问题、公式、符号与意义按因果顺序展开.

第一幅图比较正全局带隙、间接能量重叠和直接带隙闭合.
第二幅图标示三角与方形晶格 Brillouin zone 的四个不等价 TRIM.
这些图是示意图, 不代表 beryllene 的计算数据.
没有加入 Chern 模型、Wilson-loop 实现、三维指标或边缘输运计算.
边缘态只在解释绝缘填充下 Z2 的物理意义时简短出现.

## 绘图习惯

Notebook 只保留简短标题、绘图代码和图像输出.
解释在正文和图注中, 核验代码单独放在 `ch4_verification/`.
字体沿用 Chapter 2 的 serif 和 Computer Modern mathtext.
使用 Chapter 2 的蓝、青、橙、紫:
`#5082FF`, `#50AFAF`, `#FAA03C`, `#B95FF5`.
两幅 PDF 均为矢量图.
两幅图的画布和 PDF 页面均固定为 `8 × 4` 英寸,
与 Chapter 2 notebook 及其输出 `2.0_HK.pdf` 一致.
标签、刻度和图例为 14 pt, 标题为 16 pt.
使用 Matplotlib 原生 legend 与 constrained layout 自动安排图例;
曲线旁的重复量名和 contact 引线说明已归入图例.
TRIM 的点位名称保留在相应位置, 以便直接识别倒空间坐标.

## 核验

- 对照原始方法文献, 独立复核了 Berry phase 的符号、Kramers 正交性、
  反演宇称、PT 简并、子空间隔离条件和每个 Kramers pair 只计一次的原因.
- 单带 Berry phase 明确限制在非简并的引入情形; 实际简并态使用整个子空间.
- Kramers 正交性证明采用完整 Bloch 态, 避免在非零 TRIM 上遗漏 cell-periodic 态的倒格矢变换.
- 明确时间反演保护此 Z2 分类, 反演提供宇称判据这一计算途径.
- 新增三个已核实的文献条目: Berry 1984、Kane--Mele 2005、Wilczek--Zee 1984.
  同时使用已有 Fu--Kane 2007 与 irvsp 方法文献.
- Notebook 在仓库根目录和 `figures_ch4/` 中均完成全新内核运行.
  两次导出的对应 PDF 字节一致.
- 三种示意色散的最小直接分离与间接分离分别为
  `(1.20, 0.76)`, `(0.70, -0.90)`, `(0, 0)`.
  四个 TRIM 的分数坐标、周期副本和所在 Brillouin zone 均已核验.
- 独立编译通过; 无未定义引用、重复 label、overfull 或 underfull box.
  仍有模板原有的 class 名称与 footnote 命令两类提示.
- 最新 18 页预览已渲染检查, 图页与较长公式另作放大检查.

具体记录在 `ch4_verification/draft-audit.json`,
`ch4_verification/final-verification.json` 和
`ch4_verification/schematic_verification.json`.

## 与当前论文的关系

本轮生成独立草稿, 尚未在 `thesis.tex` 中插入.
独立预览使用当前主文件的排版设置, 外部交叉引用沿用当前论文编号;
因此 Project 3 仍显示为 Chapter 6.
将来正式插入时, 正文的语义 label 会随统一编译更新编号.

Chapter 2 现有拓扑方法概览保留, 未在本轮迁移或删除.
正式整合时可检查与新章的必要回指和明显重复.
Introduction 按约定留待 Project 3 完成后调整.
Project 3 的实际带数、全 BZ 隔离证据、宇称输出及相应结论仍由源头核验决定;
本草稿不将这些尚未确认的事实写成已完成验证.

## 重新生成

从仓库根目录运行:

```sh
/opt/homebrew/Caskroom/miniconda/base/envs/py314/bin/python agents/ch4_verification/verify_schematics.py
python3 agents/ch4_verification/build_draft.py
```

第一条执行绘图并验证, 第二条使用当前 thesis preamble 单独编译草稿.
第二条需要现有 `.output/thesis.aux` 提供跨章引用.
也可以直接在 Jupyter 中运行 notebook 的全部绘图单元.

## 原始方法文献

- Berry: https://doi.org/10.1098/rspa.1984.0023
- Wilczek--Zee: https://doi.org/10.1103/PhysRevLett.52.2111
- Kane--Mele: https://doi.org/10.1103/PhysRevLett.95.146802
- Fu--Kane: https://doi.org/10.1103/PhysRevB.76.045302
- irvsp: https://doi.org/10.1016/j.cpc.2020.107760
