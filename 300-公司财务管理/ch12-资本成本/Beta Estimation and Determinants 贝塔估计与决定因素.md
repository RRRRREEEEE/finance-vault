---
tags:
  - 公司财务管理
  - ch12-资本成本
  - 概念
courses:
  - 公司财务管理
aliases:
  - Beta Estimation and Determinants
  - 贝塔估计与决定因素
  - Operating Leverage
  - Financial Leverage
  - Asset Beta
created: 2026-06-30
source: Chap12_Cost_of_Capital.pdf 第14-25页
chapter: "第12章 资本成本"
importance: "***"
---

# 贝塔估计与决定因素 (Beta Estimation and Determinants)

## 📌 定义
贝塔受三大因素影响：**收入周期性**（经济周期敏感度）、**经营杠杆**（固定成本占比）、**财务杠杆**（负债比例）。权益贝塔 $β_E$ > 资产贝塔 $β_A$——负债越多，股东承担的风险越大。

> 💬 通俗理解：一个公司的贝塔不是天生固定的——经济好的时候它赚不赚（周期性）？成本里固定成本多不多（经营杠杆）？借了多少钱（财务杠杆）？这三个因素共同决定了它的贝塔。

## 🔗 前置知识
- [[Beta Coefficient 贝塔系数]]（ch11）
- [[Cost of Equity Capital 权益资本成本]]

## 🧠 机制

### 贝塔的三个决定因素

| 因素 | 定义 | 如何影响 $\beta$ |
|------|------|------|
| **收入周期性** (Cyclicality) | 收入对经济周期的敏感度 | 强周期行业（汽车、零售）→ 高 $\beta$ |
| **经营杠杆** (Operating Leverage) | 固定成本 / 可变成本 | 固定成本占比高 → $DOL$ 大 → $\beta$ 放大 |
| **财务杠杆** (Financial Leverage) | 负债 / 权益 | 负债越多 → $\beta_E$ 越大 |

### 经营杠杆度 (DOL)

$$DOL = \frac{\%\ Change\ in\ EBIT}{\%\ Change\ in\ Sales} = \frac{Q(P-V)}{Q(P-V)-F}$$

> 固定成本 $F$ 越大 → DOL 越大 → 销售收入小波动被放大为 EBIT 大波动 → $\beta$ 放大。

### 资产贝塔 vs 权益贝塔

$$\beta_{Asset} = \frac{D}{D+E} \times \beta_{Debt} + \frac{E}{D+E} \times \beta_{Equity}$$

通常 $\beta_{Debt} \approx 0$（债务系统风险很低），因此：

$$\beta_{Asset} = \frac{E}{D+E} \times \beta_{Equity}$$

$$\beta_{Equity} = \left(1 + \frac{D}{E}\right) \times \beta_{Asset}$$

### 计算实例

> Grand Sport 原为全股权融资，$\beta_{Asset} = 0.90$。现改为 $D/E = 1/1$（一半债一半股），假设 $\beta_{Debt} = 0$。

$$\beta_{Equity} = \left(1 + \frac{1}{1}\right) \times 0.90 = 2 \times 0.90 = 1.80$$

> **借了钱之后，股东的贝塔从 0.90 翻倍到 1.80**——财务杠杆放大了股东风险。

### 贝塔估计的实践问题

| 问题 | 解决方案 |
|------|----------|
| 贝塔随时间变化 | 更复杂的统计技术（如调整贝塔） |
| 样本量不足 | 使用**行业平均贝塔**代替 |
| 财务杠杆和经营风险变化 | 调整业务和财务风险变化 |

> 实践中：同行业内公司的 $\beta$ 相对稳定，行业 $\beta$ 比单个公司 $\beta$ 更可靠。

## 📊 图形

![[ch12 Financial Leverage and Beta.png]]

> 图形说明：财务杠杆放大权益贝塔——$\beta_E = (1 + D/E) \times \beta_A$，借得越多股东的贝塔越高。

## 📐 公式

| 概念 | 公式 |
|------|------|
| 资产贝塔 | $\beta_A = \frac{D}{D+E}\beta_D + \frac{E}{D+E}\beta_E$ |
| 权益贝塔（杠杆） | $\beta_E = (1 + D/E) \times \beta_A$（当 $\beta_D = 0$） |
| 经营杠杆度 | $DOL = \frac{Q(P-V)}{Q(P-V)-F}$ |

## 🏛️ 应用
- **去杠杆化**：从可比公司的 $\beta_E$ 算出 $\beta_A$，再按目标公司杠杆重新加回
- 项目贝塔 ≠ 公司贝塔——新项目应与同行业可比公司对标
- 进入新行业时用行业平均贝塔

## 📖 相关术语
- [[Cost of Equity Capital 权益资本成本]]：$\beta_E$ → CAPM → $R_E$
- [[Weighted Average Cost of Capital 加权平均资本成本]]：$\beta_A$ 用于 WACC
- [[Beta Coefficient 贝塔系数]]（ch11）：贝塔的基础定义

## 📄 来源原文
> Determinants of beta: Business Risk (Cyclicality of Revenues, Operating Leverage) and Financial Risk (Financial Leverage). Operating leverage refers to the sensitivity to the firm's fixed costs of production. Financial leverage is the sensitivity to a firm's fixed costs of financing. βAsset = D/(D+E) × βDebt + E/(D+E) × βEquity. Increase in financial leverage always increases the equity beta. βEquity = (1+D/E) × βAsset.
