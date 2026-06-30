---
tags:
  - 公司财务管理
  - ch12-资本成本
  - 公式
courses:
  - 公司财务管理
aliases:
  - Cost of Debt
  - 债务资本成本
  - After-Tax Cost of Debt
created: 2026-06-30
source: Chap12_Cost_of_Capital.pdf 第34-36页
chapter: "第12章 资本成本"
importance: "***"
---

# 债务资本成本 (Cost of Debt)

## 📌 定义
债务资本成本 $R_D$ = 公司新发行债务的**到期收益率（YTM）**。由于利息可以**税前扣除**，实际成本为税后债务成本：$R_D \times (1 - T_C)$。税盾效应使债务融资比股权融资更便宜。

> 💬 通俗理解：公司借 100 元，利率 10%，每年付 $10 利息。但这 $10 在计税前就扣掉了——如果税率 40%，相当于政府帮你付了 $4，公司实际只掏 $6。所以实际债务成本 = 10% × (1 − 40%) = 6%。

## 🔗 前置知识
- [[Cost of Equity Capital 权益资本成本]]
- [[Weighted Average Cost of Capital 加权平均资本成本]]

## 🧠 机制

### 税前债务成本

$$R_D = YTM\ of\ the\ firm's\ bonds$$

- 比权益成本更容易确定——直接观察债券的市场 YTM
- 新发行债务的成本 = 当前市场上同等风险债券的 YTM

### 税后债务成本

$$After\text{-}Tax\ R_D = R_D \times (1 - T_C)$$

### 计算实例

> 公司债券 YTM = 10%，公司税率 = 40%。

$$After\text{-}Tax\ R_D = 10\% \times (1 - 40\%) = 10\% \times 0.60 = 6\%$$

> 政府补贴了 40% 的利息成本——税盾效应。

### 优先股成本

$$R_P = \frac{C}{P}$$

其中 $C$ 为优先股固定股利，$P$ 为优先股市场价格。优先股股利**不可税前扣除**（不同于债务利息）。

| 资金来源 | 成本估算 | 可否税前扣除 |
|----------|----------|:---:|
| 普通股 | $R_E$ = CAPM 或 DDM | ❌ |
| 优先股 | $R_P = C / P$ | ❌ |
| 债务 | $R_D(1-T_C)$ | ✅ |

## 📐 公式

| 概念 | 公式 |
|------|------|
| 税前债务成本 | $R_D$ = 债券 YTM |
| 税后债务成本 | $R_D \times (1 - T_C)$ |
| 优先股成本 | $R_P = C / P$ |

## 🏛️ 应用
- **WACC 中债务部分的成本**输入
- 较高税率公司 → 更大税盾 → 更偏好债务融资
- 优先股成本通常介于债务和普通股之间

## 📖 相关术语
- [[Weighted Average Cost of Capital 加权平均资本成本]]：$R_D(1-T_C)$ 是 WACC 的债务部分
- [[Cost of Equity Capital 权益资本成本]]：$R_E$ 不能税前扣除
- [[Preferred Stock 优先股]]（ch06）：优先股是永续年金，$R_P = C/P$

## 📄 来源原文
> Cost of debt: the interest rate required on new debt issuance (i.e., yield to maturity on publicly traded bonds). Adjust for the tax deductibility of interest expense: After-tax cost of capital for debt = (1-tax rate) × interest rate. Example: 6% = (1-40%) × 10%. Preferred stock is a perpetuity: P = C/R, so RP = C/P.
