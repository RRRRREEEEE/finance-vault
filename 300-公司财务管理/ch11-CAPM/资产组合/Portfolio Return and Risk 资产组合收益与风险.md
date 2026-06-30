---
tags:
  - 公司财务管理
  - ch11-CAPM
  - 模型
courses:
  - 公司财务管理
aliases:
  - Portfolio Return and Risk
  - 资产组合收益与风险
  - Diversification Effect
created: 2026-06-30
source: Chap11_CAPM.pdf 第15-20页
chapter: "第11章 CAPM"
importance: "*****"
---

# 资产组合收益与风险 (Portfolio Return and Risk)

## 📌 定义
资产组合的**收益**是各资产收益的加权平均，但组合的**风险**通常**小于**各资产风险的加权平均——这就是分散化效应：只要 $\rho < 1$，组合标准差就小于加权平均标准差。

> 💬 通俗理解：单独买股票 A 波动 14%，单独买债券 B 波动 8%——按说各买一半应该波动 11%？实际只有 3.08%！少掉的 8% 波动来自 A 和 B 的负相关——"一只跌另一只涨，加在一起就稳了"。

## 🔗 前置知识
- [[Expected Return and Risk 期望收益与风险]]
- [[Covariance and Correlation 协方差与相关系数]]
- [[Diversification 多样化]]（货币金融学）
- [[Portfolio 资产组合]]（货币金融学）

## 🧠 机制

### 组合收益：加权平均

$$E(R_P) = w_S \times E(R_S) + w_B \times E(R_B)$$

$$E(R_P) = 50\% \times 11\% + 50\% \times 7\% = 9.0\%$$

### 组合方差：不是简单平均！

$$\sigma_P^2 = w_S^2 \sigma_S^2 + w_B^2 \sigma_B^2 + 2 w_S w_B \rho_{S,B} \sigma_S \sigma_B$$

$$= 0.5^2 \times 0.0205 + 0.5^2 \times 0.0067 + 2 \times 0.5 \times 0.5 \times (-0.0117)$$
$$= 0.005125 + 0.001675 - 0.00585 = 0.0010$$

$$\sigma_P = \sqrt{0.0010} = 3.08\%$$

### 分散化效应一目了然

| 度量 | 股票 | 债券 | 50-50 组合 | 简单平均 |
|------|:---:|:---:|:---:|:---:|
| 期望收益 | 11.0% | 7.0% | **9.0%** | 9.0% |
| 标准差 | 14.3% | 8.2% | **3.08%** | 11.25% |

> **收益是线性平均（9.0%），但风险大幅降低（3.08% << 11.25%）**——Markowitz 称之为"投资中唯一的免费午餐"。

### 为什么？第三项是关键

$$\sigma_P^2 = \underbrace{w_S^2\sigma_S^2 + w_B^2\sigma_B^2}_{\text{加权方差}} + \underbrace{2w_S w_B Cov(S,B)}_{\text{交叉项}}$$

- 当 $Cov < 0$（负协方差）→ 交叉项为**负** → 组合方差变小
- 当 $\rho = -1$ → 理论上可以**完全消除风险**

## 📊 图形

![[ch11 Portfolio Diversification Effect.png]]

> 图形说明：50-50 组合——收益是加权平均（9.0%），但标准差降至 3.08%，远低于任一只资产。

## 🏛️ 应用
- **分散化是风险管理的基石**：绝大多数机构投资者持有多样化组合
- 风险降低程度取决于 $\rho$：$\rho$ 越小，分散化效果越好
- 国际分散化：不同国家市场相关性通常低于国内，可进一步降低风险

## 📖 相关术语
- [[Efficient Frontier 有效边界]]：所有最优组合构成的曲线
- [[Covariance and Correlation 协方差与相关系数]]：$\rho$ 是分散化效果的决定因素
- [[Systematic and Unsystematic Risk 系统风险与非系统风险]]：分散化只能消除非系统风险

## 📄 来源原文
> The rate of return on the portfolio is a weighted average of the returns on the stocks and bonds. The expected rate of return on the portfolio is a weighted average of the expected returns on the securities. The variance of the rate of return on the two risky assets portfolio is: σ² = wS²σS² + wB²σB² + 2wSwBρB,SσBσS. Observe the decrease in risk that diversification offers. An equally weighted portfolio (50% stocks and 50% bonds) has less risk than either stock or bond.
