---
tags:
  - 公司财务管理
  - ch14-MM资本结构
  - 模型
courses:
  - 公司财务管理
aliases:
  - MM Proposition I and II No Tax
  - MM无税定理
  - Modigliani-Miller No Tax
created: 2026-06-30
source: Chap14_MM.pdf 第20-31页
chapter: "第14章 MM 资本结构"
importance: "*****"
---

# MM 无税定理 (MM Proposition I & II, No Tax)

## 📌 定义
Modigliani & Miller（1958）在无税、完美资本市场的假设下证明了两个革命性命题：

- **命题 I**：$V_L = V_U$ —— 杠杆公司的价值 = 无杠杆公司的价值。**资本结构与公司价值无关。**
- **命题 II**：$R_S = R_0 + \frac{D}{E} \times (R_0 - R_D)$ —— 权益成本随杠杆线性上升，恰好抵消债务便宜的好处，使 WACC 保持不变。

> 💬 通俗理解：无税世界里，你借多少钱都不改变公司价值。因为借债虽然降低了融资成本（债务比股权便宜），但股东的回报要求（$R_S$）也上升了——两者恰好互相抵消，WACC 不变，$V$ 不变。饼的大小取决于你烤饼的技术（资产），不取决于你怎么切（资本结构）。

## 🔗 前置知识
- [[Capital Structure and Pie Theory 资本结构与派理论]]
- [[Financial Leverage and EPS 财务杠杆与每股收益]]
- [[Cost of Equity Capital 权益资本成本]]（ch12）
- [[Weighted Average Cost of Capital 加权平均资本成本]]（ch12）

## 🧠 机制

### 关键假设

| 假设 | 说明 |
|------|------|
| 同质预期 | 所有投资者对未来收益和风险有一致预期 |
| 同质经营风险 | 公司可按经营风险分类 |
| 永续现金流 | 便于定价 |
| 完美资本市场 | 无税、无交易成本、无信息不对称、个人和公司能以相同利率借贷 |

### 命题 I：$V_L = V_U$

> 杠杆公司的价值 = 无杠杆公司的价值。资本结构不影响公司总价值。

**证明思路**：自制杠杆。如果投资者可以通过个人借贷复制任何公司杠杆结构带来的收益，那么公司层面的杠杆不能创造额外的价值——投资者不需要花钱让公司替自己做自己能做的事。

| 操作 | 效果 |
|------|------|
| 买无杠杆公司 40 股（$2,000），其中 $800 来自借款 | 获得的 ROE 与直接买杠杆公司的股票完全相同 |
| 买杠杆公司 24 股（$1,200）+ 买入 $800 公司债券 | 获得的收益与持有无杠杆公司的股票完全相同 |

> 无论公司如何选择资本结构，投资者都能通过自制杠杆或自制去杠杆，复制任何想要的结果。

### 命题 II：$R_S$ 随杠杆上升

$$R_S = R_0 + \frac{D}{E} \times (R_0 - R_D)$$

| 符号 | 含义 |
|------|------|
| $R_S$ | 杠杆后的权益成本（股东要求回报率） |
| $R_0$ | 无杠杆公司的权益成本（全股权公司的 $R_E$） |
| $R_D$ | 债务成本（利率） |
| $D/E$ | 负债权益比 |

### WACC 不变

$$WACC = \frac{D}{D+E} \times R_D + \frac{E}{D+E} \times R_S = R_0$$

> 杠杆↑ → $R_S$↑（命题 II）→ 完全抵消 $R_D$ 的权重上升 → WACC 恒等于 $R_0$。

### MM 无税世界三线图

![[ch14 MM No Tax Cost of Capital.png]]

| 线 | 含义 | 形状 |
|----|------|:---:|
| $R_S$ | 权益成本 | 随 $D/E$ 线性上升 |
| $R_D$ | 债务成本 | 水平线（假设无违约风险） |
| **WACC** | 加权平均资本成本 | **水平线 = $R_0$** |

## 📐 公式

| 命题 | 公式 |
|------|------|
| 命题 I | $V_L = V_U$ |
| 命题 II | $R_S = R_0 + \frac{D}{E}(R_0 - R_D)$ |
| WACC | $WACC = R_0$（与杠杆无关） |

## 🏛️ 应用
- **理论基准**：MM 无税定理是资本结构理论的起点——它不是描述现实，而是告诉我们"如果资本结构无关紧要，需要哪些条件"
- 现实中资本结构确实影响价值 → 说明 MM 的某些假设被违反了（税、破产成本、信息不对称）

## 📖 相关术语
- [[MM Proposition I and II With Tax MM有税定理]]：加入税盾后 $V_L > V_U$
- [[Weighted Average Cost of Capital 加权平均资本成本]]（ch12）：MM 证明无税时 WACC 与杠杆无关
- [[Cost of Equity Capital 权益资本成本]]（ch12）：$R_S$ 就是有杠杆时的 $R_E$

## 📄 来源原文
> MM Proposition I (No Taxes): The value of the levered firm is the same as the value of the unlevered firm. VL = VU. Capital structure is irrelevant in determining the value of the firm. Proposition II: Required return to stockholders rises with leverage. RS = R0 + (B/S)(R0 - RB). The capital structure is irrelevant because shareholders can create their own leverage or unlever the stock to create the payoff they desire.
