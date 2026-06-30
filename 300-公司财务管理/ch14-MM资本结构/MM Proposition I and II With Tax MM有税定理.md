---
tags:
  - 公司财务管理
  - ch14-MM资本结构
  - 模型
courses:
  - 公司财务管理
aliases:
  - MM Proposition I and II With Tax
  - MM有税定理
  - Modigliani-Miller With Tax
created: 2026-06-30
source: Chap14_MM.pdf 第33-40页
chapter: "第14章 MM 资本结构"
importance: "*****"
---

# MM 有税定理 (MM Proposition I & II, With Tax)

## 📌 定义
Modigliani & Miller（1963）引入公司税后得出：利息的**税盾效应**使杠杆公司价值高于无杠杆公司——

- **命题 I**：$V_L = V_U + T_C \times D$ —— 每多借 $1 债务，公司价值增加 $T_C$
- **命题 II**：$R_S = R_0 + \frac{D}{E} \times (1 - T_C) \times (R_0 - R_D)$ —— 权益成本上升，但 $(1-T_C)$ 项削弱了上升幅度

> 💬 通俗理解：在有税世界里，借债有一个"隐藏好处"——利息可以抵税。每借 $1，政府帮你付了 $T_C$ 的利息。如果把所有公司都杠杆化到极限（$D = 100\%$），公司价值最大——但现实中为什么没有公司这样做？因为 MM 还没加入破产成本。

## 🔗 前置知识
- [[MM Proposition I and II No Tax MM无税定理]]
- [[Cost of Debt 债务资本成本]]（ch12）
- [[Capital Structure and Pie Theory 资本结构与派理论]]

## 🧠 机制

### 命题 I：$V_L = V_U + T_C \times D$

**推导**：投资者（股东 + 债权人）获得的总现金流：

| 公司类型 | 股东 + 债权人总现金流 |
|----------|------|
| 无杠杆 | $EBIT \times (1 - T_C)$ |
| 杠杆 | $EBIT \times (1 - T_C) + T_C \times R_D \times D$ |

折现后：
$$V_L = \frac{EBIT(1-T_C)}{R_0} + \frac{T_C \times R_D \times D}{R_D} = V_U + T_C \times D$$

| 项 | 含义 | 折现率 |
|----|------|:---:|
| $V_U$ | 无杠杆公司价值 | $R_0$（经营风险） |
| $T_C \times D$ | **税盾现值** | $R_D$（与债务同风险） |

### 计算实例：两种结构交税对比

> $EBIT = \$2,000$（预期），债务 $8,000 @ 8%，$T_C = 35\%$

| | 无杠杆 | 杠杆 | 差异 |
|---|:---:|:---:|:---:|
| EBIT | $2,000 | $2,000 | — |
| 利息 | $0 | $640 | — |
| 应税利润 | $2,000 | $1,360 | — |
| 税款 | **$700** | **$476** | −$224 |
| 股东 + 债权人现金流 | $1,300 | $1,524 | **+$224** |

> 杠杆公司少交了 $224 = $8,000 × 8% × 35% = $T_C \times R_D \times D$。这张税收节省的现值 = $T_C \times D$。

### 税盾的派理论

![[ch14 Tax Shield Pie.png]]

- 全股权公司：饼 = 权益 + 政府税收
- 杠杆公司：饼 = 权益 + 债务 + 政府税收（但政府切走的部分**变小了**）
- **杠杆让政府的份额减少，投资者（股东 + 债权人）的总份额增加**

### 命题 II：$R_S$ 上升被税盾部分抵消

$$R_S = R_0 + \frac{D}{E} \times (1 - T_C) \times (R_0 - R_D)$$

相比无税版 $R_S = R_0 + \frac{D}{E}(R_0 - R_D)$：
- $(1 - T_C) < 1$ → 有税时 $R_S$ 的**上升斜率更缓**
- 税收补贴了部分债务成本 → 股东的额外风险补偿需求减小

### WACC 随杠杆下降

$$WACC = \frac{D}{D+E} \times R_D \times (1 - T_C) + \frac{E}{D+E} \times R_S$$

> $D$↑ → $R_S$↑（但斜率被 $(1-T_C)$ 减缓）→ 便宜的税后债务权重增加 > $R_S$ 上升 → **WACC 随杠杆单调递减**。

![[ch14 MM With Tax Cost of Capital.png]]

### 无税 vs 有税对比

| 命题 | 无税（1958） | 有税（1963） |
|------|-------------|-------------|
| 命题 I | $V_L = V_U$ | $V_L = V_U + T_C \times D$ |
| 命题 II | $R_S = R_0 + \frac{D}{E}(R_0 - R_D)$ | $R_S = R_0 + \frac{D}{E}(1-T_C)(R_0 - R_D)$ |
| WACC | 恒定 = $R_0$ | 随 $D/E$↑ 而↓ |
| 最优 $D/E$ | 任意 | 100% 债务（极限） |

## 📐 公式

| 命题 | 公式 |
|------|------|
| 有税命题 I | $V_L = V_U + T_C \times D$ |
| 有税命题 II | $R_S = R_0 + \frac{D}{E}(1-T_C)(R_0 - R_D)$ |
| 税盾现值 | $PV(Tax\ Shield) = T_C \times D$ |

## 🏛️ 应用
- MM 有税定理解释了为什么**债务在现实中确实创造价值**（税盾）
- 但公司不会 100% 债务融资 → 因为 MM 还忽略了**破产成本**（后续扩展：权衡理论）
- 现实中还有**个人税**（Miller 1977 进一步修正）和**代理成本**

## 📖 相关术语
- [[MM Proposition I and II No Tax MM无税定理]]：无税基准
- [[Cost of Debt 债务资本成本]]（ch12）：税盾机制的经济学基础
- [[Weighted Average Cost of Capital 加权平均资本成本]]（ch12）：有税时 WACC = $R_0(1 - T_C \times D/V)$

## ⚖️ 易混点对照（人类填写区域）
- 无税 vs 有税 MM 到底差在哪？
- 税盾现值为什么是 $T_C \times D$（永续债假设下）？

## 📝 个人批注（人类专属，AI 严禁写入）

## 📄 来源原文
> MM Proposition I (with Corporate Taxes): Firm value increases with leverage. VL = VU + tC × B. The value of the levered firm is the value of an all-equity firm plus the present value of the tax shield in the case of perpetual cash flows. Proposition II (with Corporate Taxes): RS = R0 + (B/S)×(1-tC)×(R0 – RB). Some of the increase in equity risk and return is offset by the interest tax shield. The levered firm pays less in taxes than does the all-equity firm. Thus, the sum of the debt plus the equity of the levered firm is greater than the equity of the unlevered firm.
