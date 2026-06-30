---
tags:
  - 公司财务管理
  - ch14-MM资本结构
  - 模型
courses:
  - 公司财务管理
aliases:
  - Financial Leverage and EPS
  - 财务杠杆与每股收益
  - EPS Break-Even
  - Homemade Leverage Detail
created: 2026-06-30
source: Chap14_MM.pdf 第13-18页
chapter: "第14章 MM 资本结构"
importance: "***"
---

# 财务杠杆与每股收益 (Financial Leverage and EPS)

## 📌 定义
财务杠杆（借债）**放大 EPS 的波动**：经济好时 EPS 更高，经济差时 EPS 更低。在 EBIT-EPS 图上，杠杆线和无杠杆线存在一个**盈亏平衡点**（Break-Even EBIT）——高于此点杠杆有利，低于此点杠杆有害。

> 💬 通俗理解：借钱就像给 EPS 加了"放大器"——公司赚钱时每股赚更多，但一旦赚不够利息钱，亏得也更惨。杠杆让好日子更好、坏日子更坏。

## 🔗 前置知识
- [[Capital Structure and Pie Theory 资本结构与派理论]]
- [[Beta Estimation and Determinants 贝塔估计与决定因素]]（ch12）

## 🧠 机制

### 计算实例：无杠杆 vs 杠杆

> 资产 $20,000，全股权（400 股 × $50）。考虑发行 $8,000 债务（利率 8%）回购 160 股。

| | 无杠杆 | 杠杆（D/E = 2/3） |
|---|:---:|:---:|
| 股价 | $50 | $50 |
| 股数 | 400 | 240 |
| 权益 | $20,000 | $12,000 |
| 债务 | $0 | $8,000 |

### EPS 对比

| 情景 | EBIT | 无杠杆 EPS | 杠杆 EPS | 杠杆效应 |
|------|------|:---:|:---:|:---:|
| 衰退 | $1,000 | $2.50 | $1.50 | ❌ 更差 |
| 预期 | $2,000 | $5.00 | $5.67 | ✅ 更好 |
| 繁荣 | $3,000 | $7.50 | $9.83 | ✅ 更好 |

### 盈亏平衡点 (Break-Even EBIT)

$$\frac{EBIT}{400} = \frac{EBIT - 640}{240} \quad \Rightarrow \quad EBIT = \$1,600$$

| EBIT 水平 | 结论 |
|-----------|------|
| EBIT > $1,600 | 杠杆有利（杠杆 EPS > 无杠杆 EPS） |
| EBIT = $1,600 | 无差异 |
| EBIT < $1,600 | 杠杆有害（杠杆 EPS < 无杠杆 EPS） |

### 杠杆放大 ROE

| 情景 | 无杠杆 ROE | 杠杆 ROE |
|------|:---:|:---:|
| 衰退 | 5.0% | 3.0% |
| 预期 | 10.0% | 11.3% |
| 繁荣 | 15.0% | 19.7% |

> ROE 的离散度从 5%-15% 扩大到 3%-19.7%——风险随杠杆上升。

## 📊 图形

![[ch14 EPS Break Even EBIT.png]]

> 图形说明：EPS-EBIT 盈亏平衡图——杠杆线斜率更大（高 EBIT 时 EPS 更高），但截距更低（低 EBIT 时 EPS 更低）。两线相交于 EBIT = $1,600。

## 🏛️ 应用
- 判断增加杠杆是否对 EPS 有利的临界分析
- 但注意：**高 EPS ≠ 高股价**——杠杆在增加 EPS 的同时也增加了风险（→ $R_E$ 上升 → P/E 可能下降）

## 📖 相关术语
- [[Capital Structure and Pie Theory 资本结构与派理论]]
- [[MM Proposition I and II No Tax MM无税定理]]：MM 证明杠杆改变 EPS 但不改变公司价值
- [[Beta Estimation and Determinants 贝塔估计与决定因素]]（ch12）：$\beta_E = (1+D/E)\beta_A$

## 📄 来源原文
> Financial leverage amplifies EPS: higher in good times, lower in bad times. Break-even EBIT is the point where EPS is the same under both structures. Under proposed structure with leverage: Recession EPS=$1.50, Expected=$5.67, Expansion=$9.83. Under current without leverage: $2.50, $5.00, $7.50. Break-even at EBIT=$1,600.
