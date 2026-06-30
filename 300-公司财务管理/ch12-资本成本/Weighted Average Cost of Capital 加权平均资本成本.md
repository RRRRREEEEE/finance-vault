---
tags:
  - 公司财务管理
  - ch12-资本成本
  - 模型
courses:
  - 公司财务管理
aliases:
  - Weighted Average Cost of Capital
  - WACC
  - 加权平均资本成本
created: 2026-06-30
source: Chap12_Cost_of_Capital.pdf 第38-43页
chapter: "第12章 资本成本"
importance: "*****"
---

# 加权平均资本成本 (WACC)

## 📌 定义
WACC（Weighted Average Cost of Capital）是公司**整体资本成本**——以市场价值为权重，对权益成本 $R_E$ 和**税后**债务成本 $R_D(1-T_C)$ 加权平均：

$$WACC = \frac{E}{D+E} \times R_E + \frac{D}{D+E} \times R_D \times (1 - T_C)$$

> 💬 通俗理解：公司融资是一个"混合桶"——一部分是股东的钱（$R_E$），一部分是债主的钱（$R_D$），还有一部分债务利息可以抵税。WACC 就是这一桶钱的**平均成本**，用来折现公司的整体项目。

## 🔗 前置知识
- [[Cost of Equity Capital 权益资本成本]]
- [[Cost of Debt 债务资本成本]]
- [[Capital Structure 资本结构]]（ch01）

## 🧠 机制

### WACC 公式

$$WACC = \frac{E}{E+D} \times R_E + \frac{D}{E+D} \times R_D \times (1 - T_C)$$

或写作：
$$WACC = w_E \times R_E + w_D \times R_D \times (1 - T_C)$$

| 组成部分 | 含义 | 权重 |
|----------|------|------|
| $w_E \times R_E$ | 权益贡献 | $E/(E+D)$（市场价值权重） |
| $w_D \times R_D(1-T_C)$ | **税后**债务贡献 | $D/(E+D)$（市场价值权重） |

> ⚠️ **为什么用市场价值而非账面价值？** 市场价值更接近证券的实际出售价格——WACC 衡量的是**机会成本**，市场价值反映当前真实融资成本。

### 为什么是税后债务成本？

- 股利 → 税后支付（不可抵税）
- 利息 → **税前**扣除 → 政府实际补贴了 $T_C \times R_D$ 部分
- 公司的实际债务成本 = $R_D \times (1 - T_C)$

### 完整计算实例：Eastman Chemical

| 参数 | 值 | 来源 |
|------|-----|------|
| $\beta_E$ | 1.81 | 市场回归 |
| $R_F$ | 0.50% | 短期国债 |
| $R_M - R_F$ | 7% | 市场风险溢价 |
| $R_D$ (YTM) | 3.15% | 债券市场 |
| $T_C$ | 35% | 边际税率 |
| $D/(D+E)$ | 29.4% | 市场价值 |

**步骤一**：估算 $R_E$
$$R_E = 0.50\% + 1.81 \times 7\% = 13.17\%$$

**步骤二**：估算税后 $R_D$
$$After\text{-}Tax\ R_D = 3.15\% \times (1 - 0.35) = 2.05\%$$

**步骤三**：计算 WACC
$$WACC = 70.6\% \times 13.17\% + 29.4\% \times 2.05\% = 9.30\% + 0.60\% = 9.90\%$$

> Eastman 的 WACC = **9.90%**。应将其作为与公司整体风险相当的项目的折现率。

### WACC 的适用前提

| ✅ 适用条件 | ❌ 不适用条件 |
|-------------|---------------|
| 项目风险 = 公司整体风险 | 项目风险显著不同于公司（→ 用项目特定折现率） |
| 项目融资结构 = 公司目标资本结构 | 项目改变了公司的资本结构 |
| | 项目规模大到影响公司整体风险 |

## 📐 公式

$$WACC = \frac{E}{E+D} \times R_E + \frac{D}{E+D} \times R_D \times (1 - T_C)$$

| 符号 | 含义 |
|------|------|
| $E$ | 权益市场价值 |
| $D$ | 债务市场价值 |
| $R_E$ | 权益资本成本（CAPM 或 DDM） |
| $R_D$ | 税前债务成本（YTM） |
| $T_C$ | 公司所得税率 |

## 🏛️ 应用
- **NPV 折现率**：公司整体项目的基准折现率
- **企业估值**：DCF 模型中自由现金流用 WACC 折现
- **业绩基准**：投资回报率 > WACC → 创造价值

## 📖 相关术语
- [[Cost of Equity Capital 权益资本成本]]：WACC 的权益部分
- [[Cost of Debt 债务资本成本]]：WACC 的债务部分（税后）
- [[Project Cost of Capital 项目资本成本]]：项目风险不同时不能用 WACC
- [[Capital Structure 资本结构]]（ch01）：$D/E$ 权重选择直接影响 WACC

## ⚖️ 易混点对照（人类填写区域）
- WACC vs $R_E$：
- 账面权重 vs 市场权重：

## 📄 来源原文
> The Weighted Average Cost of Capital (WACC) is given by: RWACC = E/(E+D) × REquity + D/(E+D) × RDebt × (1-TC). Because interest expense is tax-deductible, we multiply the last term by (1-TC). Market value weights are more appropriate than book value weights because the market values of the securities are closer to the actual dollars that would be received from their sale. Example: Eastman Chemical: β=1.81, RF=0.50%, RP=7%, RD=3.15%, TC=35%, D/V=29.4%. RE=13.17%, After-tax RD=2.05%, WACC=9.90%.
