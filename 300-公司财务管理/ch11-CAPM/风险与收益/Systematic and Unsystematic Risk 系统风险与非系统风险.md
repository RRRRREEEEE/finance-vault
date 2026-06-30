---
tags:
  - 公司财务管理
  - ch11-CAPM
  - 概念
courses:
  - 公司财务管理
aliases:
  - Systematic and Unsystematic Risk
  - 系统风险与非系统风险
  - Diversifiable Risk
  - Market Risk
created: 2026-06-30
source: Chap11_CAPM.pdf 第30-39页
chapter: "第11章 CAPM"
importance: "*****"
---

# 系统风险与非系统风险 (Systematic and Unsystematic Risk)

## 📌 定义
总风险可以分解为两部分：**系统风险**（市场风险，不可分散）和**非系统风险**（公司特有风险，可分散）。在大规模、充分分散化的组合中，非系统风险几乎被完全消除——只有系统风险才获得风险溢价。

> 💬 通俗理解：你持有一只股票，它的波动来自两个层面：整个市场好坏（系统风险——央行加息、经济衰退，所有股票都受影响）和你买的这家公司自己的问题（非系统风险——CFO 造假、产品召回）。买 30 只不同的股票后，CFO 造假之类的问题被互相抵消——但市场崩盘你躲不掉。

## 🔗 前置知识
- [[Portfolio Return and Risk 资产组合收益与风险]]
- [[Diversification 多样化]]（货币金融学）
- [[Risk 风险]]（货币金融学）

## 🧠 机制

### 收益分解

$$Total\ Return = \underbrace{E(R)}_{\text{期望部分}} + \underbrace{Systematic\ Portion}_{\text{系统性惊喜/惊吓}} + \underbrace{Unsystematic\ Portion}_{\text{公司特有惊喜/惊吓}}$$

- 期望部分 = 市场已知信息已被定价
- 系统部分 = 宏观经济变化（GDP、利率、通胀）
- 非系统部分 = 公司特定事件（新产品、CEO 更换、诉讼）

### 风险分解

$$Total\ Risk = Systematic\ Risk + Unsystematic\ Risk$$

### 分散化效应

![[ch11 Systematic vs Unsystematic Risk.png]]

| 组合中股票数量 | 非系统风险 | 系统风险 | 总风险 |
|:---:|:---:|:---:|:---:|
| 1 | 高 | 不变 | 高 |
| 10 | 中 | 不变 | 中 |
| 30+ | 接近 0 | 不变 | ≈ 系统风险 |

> **充分分散化后，总风险 ≈ 系统风险。市场只为系统风险提供补偿（风险溢价）——非系统风险可以免费消除，不配获得溢价。**

### 关键洞见

| 概念 | 别称 | 可分散？ | 获得补偿？ |
|------|------|:---:|:---:|
| 系统风险 | 市场风险 / 不可分散风险 | ❌ | ✅ **有溢价** |
| 非系统风险 | 公司特有风险 / 可分散风险 | ✅ | ❌ **无溢价** |

> 🎓 **CAPM 的核心逻辑**：投资者只应该为承担**系统风险**获得回报——因为你本可以通过分散化免费消除非系统风险。决定一只股票期望收益的不是它的总风险 $\sigma$，而是它的**贝塔** $\beta$。

## 🏛️ 应用
- **分散化投资的终极理由**：消除免费的非系统风险，只留下必须承担的系统风险
- 决定一只股票在 CAPM 中期望收益的**不是 $\sigma$，而是 $\beta$**
- 实践中，持有 20-30 只不同行业的股票即可消除绝大部分非系统风险

## 📖 相关术语
- [[Beta Coefficient 贝塔系数]]：$\beta$ 度量系统风险（而非总风险）
- [[Capital Asset Pricing Model 资本资产定价模型]]：$E(R_i) = R_F + \beta_i(E(R_M) - R_F)$
- [[Efficient Frontier 有效边界]]：有效组合沿有效边界分布

## ⚖️ 易混点对照（人类填写区域）
- 系统风险 vs 非系统风险：
- 为什么非系统风险没有溢价？

## 📝 个人批注（人类专属，AI 严禁写入）

## 📄 来源原文
> Total Return = expected return + unexpected return. Unexpected return = systematic portion + unsystematic portion. Total risk = systematic risk + unsystematic risk. For well-diversified portfolios, unsystematic risk is very small. Consequently, the total risk for a well diversified portfolio is essentially equivalent to the systematic risk. Diversification of risks of stock returns: combining hedging securities into a portfolio can help "neutralize" the risks. However, there is a minimum level of risk that cannot be diversified away, which is the systematic portion.
