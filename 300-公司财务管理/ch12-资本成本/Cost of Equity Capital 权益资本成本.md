---
tags:
  - 公司财务管理
  - ch12-资本成本
  - 模型
courses:
  - 公司财务管理
aliases:
  - Cost of Equity Capital
  - 权益资本成本
  - Cost of Equity
created: 2026-06-30
source: Chap12_Cost_of_Capital.pdf 第4-11页
chapter: "第12章 资本成本"
importance: "*****"
---

# 权益资本成本 (Cost of Equity Capital)

## 📌 定义
权益资本成本 $R_E$ 是公司股权融资的**机会成本**——即股东将钱投给公司而非投向其他风险相当的投资所放弃的期望收益。用 CAPM 估算：$R_E = R_F + \beta_E \times (R_M - R_F)$。

> 💬 通俗理解：你用股东的每一元钱，至少要赚到股东自己去买同等风险股票能赚到的回报。如果你拿着一元钱去投赚 8% 的项目，而股东自己买同等风险的股票能赚 12%，你就是在"毁灭价值"——因为你拿着股东的钱没赚够。

## 🔗 前置知识
- [[Capital Asset Pricing Model 资本资产定价模型]]（ch11）
- [[Beta Coefficient 贝塔系数]]（ch11）
- [[Capital Budgeting 资本预算]]（ch01）

## 🧠 机制

### 为什么预期收益 = 资本成本？

> 公司持有超额现金 → 两种选择：
> ① 投资于项目
> ② 作为股利发给股东，股东自行投资于同等风险的金融资产

**公司投项目至少应赚到股东自行投资能赚到的回报**——这就是机会成本的逻辑。项目折现率 = 同等风险金融资产的预期收益 = 资本成本。

### CAPM 估算 $R_E$

$$R_E = R_F + \beta_E \times (R_M - R_F)$$

| 需要估算的 | 方法 |
|------------|------|
| $R_F$（无风险利率） | 1 年期国债利率（短期），或更长期限匹配项目寿命 |
| $R_M - R_F$（市场风险溢价） | ① 历史平均法 ② DDM 逆推法（$R = D_1/P_0 + g$ 用于大盘指数） |
| $\beta_E$（权益贝塔） | 历史回归 $R_{i,t} = \alpha + \beta R_{M,t} + \varepsilon_t$，或行业平均贝塔 |

### 计算实例

> Stansfield Enterprises：$\beta_E = 2.5$，$R_F = 5\%$，市场风险溢价 $= 10\%$，100% 股权融资。

$$R_E = 5\% + 2.5 \times 10\% = 30\%$$

| 项目 | $\beta$ | 现金流 | IRR | NPV@30% | 决策 |
|:---:|:---:|--------|:---:|:---:|:---:|
| A | 2.5 | $150 | 50% | +$15.38 | ✅ 接受 |
| B | 2.5 | $130 | 30% | $0 | 临界 |
| C | 2.5 | $110 | 10% | −$15.38 | ❌ 拒绝 |

> IRR > $R_E$ → 接受；IRR < $R_E$ → 拒绝。SML 将项目分为"好项目"（SML 上方）和"坏项目"（SML 下方）。

## 📊 图形

![[ch12 SML and Cost of Capital.png]]

> 图形说明：100% 股权融资公司——接受 IRR > 资本成本（30%）的项目，拒绝 IRR < 30% 的项目。

![[ch12 Project Selection with SML.png]]

> 图形说明：SML 线上——好项目在线上方（NPV>0），坏项目在线下方（NPV<0）。

## 📐 公式

$$R_E = R_F + \beta_E \times (R_M - R_F)$$

| 符号 | 含义 |
|------|------|
| $R_E$ | 权益资本成本 |
| $R_F$ | 无风险利率 |
| $\beta_E$ | 权益贝塔 |
| $R_M - R_F$ | 市场风险溢价 |

## 🏛️ 应用
- **项目折现率**：100% 股权公司直接用 $R_E$ 作为 NPV 计算中的 $r$
- **股东价值基准**：所有 IRR < $R_E$ 的项目都在毁灭股东财富

## 📖 相关术语
- [[Capital Asset Pricing Model 资本资产定价模型]]（ch11）：$R_E$ 的 CAPM 估算公式
- [[Weighted Average Cost of Capital 加权平均资本成本]]：有债务时用 WACC 而非纯 $R_E$
- [[Beta Estimation and Determinants 贝塔估计与决定因素]]：$\beta_E$ 的估算和影响因素
- [[Cost of Equity with DDM 股利折现法估算权益成本]]：$R_E$ 的 DDM 替代估算方法

## 📄 来源原文
> From the firm's perspective, the expected return is the Cost of Equity Capital: $R = R_F + \beta(R_M - R_F)$. A firm with excess cash can either pay a dividend or invest. Because stockholders can reinvest the dividend in risky financial assets, the expected return on a capital-budgeting project should be at least as great as the expected return on a financial asset of comparable risk. An all-equity firm should accept projects whose IRRs exceed the cost of equity capital.
