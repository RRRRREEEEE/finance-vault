---
tags:
  - 公司财务管理
  - ch11-CAPM
  - 模型
courses:
  - 公司财务管理
aliases:
  - Efficient Frontier
  - 有效边界
  - Efficient Set
  - Minimum Variance Portfolio
created: 2026-06-30
source: Chap11_CAPM.pdf 第22-28页
chapter: "第11章 CAPM"
importance: "****"
---

# 有效边界 (Efficient Frontier)

## 📌 定义
有效边界（Efficient Frontier）是所有**有效组合**的集合——即在给定收益水平下**风险最小**、或在给定风险水平下**收益最大**的组合构成的曲线。有效边界从最小方差组合开始，向上延伸。

> 💬 通俗理解：你把股票和债券按不同比例混合——从 0% 股票到 100% 股票——画出一条弓形的曲线。曲线的左上边缘就是"有效边界"：在边界上的组合是"聪明的投资"，在边界下的组合是"浪费机会的投资"。

## 🔗 前置知识
- [[Portfolio Return and Risk 资产组合收益与风险]]
- [[Covariance and Correlation 协方差与相关系数]]

## 🧠 机制

### 可行集 (Opportunity Set)

多只风险资产的所有可能组合构成的**伞形区域**——区域内的每一点都代表一个可能的组合。

### 最小方差组合 (Minimum Variance Portfolio)

可行集中**风险最低**的那个点——它不一定是最高收益，但没有人能用更低的风险获得同样的收益。

### 有效边界

最小方差组合**以上的上半支**曲线 = 有效边界。

> 🌟 **有效组合必须位于有效边界上，因为没有人会选"同样风险更低收益"或"同样收益更高风险"的投资。**

### 相关系数对边界形状的影响

| $\rho$ | 边界形状 | 分散化效果 |
|--------|----------|:---:|
| $\rho = +1$ | 直线 | 无——组合风险 = 加权平均 |
| $\rho = 0.2$ | 中等弯曲 | 中等 |
| $\rho = -1$ | 折线（碰 y 轴） | 最大——可以构造零风险组合 |

> 现实中股票之间的 $\rho$ 通常在 0.3-0.7 之间，所以边界有一定弯曲但不会碰到 y 轴。

## 📊 图形

![[ch11 Portfolio Risk Return Combinations.png]]

> 图形说明：不同权重组合的风险-收益散点——形成一个弯曲的可行集。

![[ch11 Correlation and Diversification.png]]

> 图形说明：不同相关系数下的组合线——$\rho$ 越小曲线越弯（分散化效果越好），$\rho=-1$ 时可达到零风险。

![[ch11 Efficient Frontier.png]]

> 图形说明：有效边界 = 最小方差组合以上的上半段——所有人都应该沿着这条线配置资产。

## 🏛️ 应用
- **资产配置的核心工具**：基金经理如何在股票、债券、现金间分配？在有效边界上找点
- Markowitz 均值-方差优化：给定风险承受力 → 选有效边界上对应的最优组合
- 两基金分离定理：任何有效组合都可以由**两个有效组合**线性组合而成

## 📖 相关术语
- [[Portfolio Return and Risk 资产组合收益与风险]]：有效边界的数学基础
- [[Capital Asset Pricing Model 资本资产定价模型]]：加入无风险资产后，有效边界变成 CML（资本市场线）

## ⚖️ 易混点对照（人类填写区域）
- 有效边界 vs 可行集：
- CML vs Efficient Frontier：

## 📝 个人批注（人类专属，AI 严禁写入）
- 考试重点：
- 计算陷阱：
- 个人理解：

## 📄 来源原文
> The efficient set, or efficient frontier, is a graphical representation of a set of possible portfolios that: Minimize risk at specific return levels; and, Maximize returns at specific risk levels. The section of the opportunity set above the minimum variance portfolio is the efficient frontier. Relationship depends on the correlation coefficient between the returns. If ρ = +1, no risk reduction is possible. If ρ = -1, complete risk reduction is possible.
