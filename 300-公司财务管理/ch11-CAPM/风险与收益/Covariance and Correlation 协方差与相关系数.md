---
tags:
  - 公司财务管理
  - ch11-CAPM
  - 公式
courses:
  - 公司财务管理
aliases:
  - Covariance and Correlation
  - 协方差与相关系数
created: 2026-06-30
source: Chap11_CAPM.pdf 第11-13页
chapter: "第11章 CAPM"
importance: "***"
---

# 协方差与相关系数 (Covariance and Correlation)

## 📌 定义
**协方差**衡量两只证券收益的**同向变动程度**。**相关系数** $\rho$ 将协方差标准化到 $[-1, 1]$ 区间：$\rho = +1$ 完全正相关，$\rho = -1$ 完全负相关，$\rho = 0$ 不相关。

> 💬 通俗理解：协方差告诉你"股票 A 涨的时候股票 B 是涨还是跌"——但协方差的数字不好理解（单位太奇怪）。相关系数把它压到 -1 到 +1 之间——+1 就是神同步，-1 就是你赚我亏，0 就是各玩各的。

## 🔗 前置知识
- [[Expected Return and Risk 期望收益与风险]]
- [[Portfolio Return and Risk 资产组合收益与风险]]

## 🧠 机制

### 协方差公式

$$Cov(a, b) = E\left[(R_a - E(R_a)) \times (R_b - E(R_b))\right]$$

| 协方差符号 | 含义 |
|------------|------|
| Cov > 0 | a 和 b 同方向变动 |
| Cov < 0 | a 和 b 反方向变动 |
| Cov = 0 | a 和 b 不相关 |

### 计算实例（股票基金 vs 债券基金）

| 情景 | $R_a - E(R_a)$ | $R_b - E(R_b)$ | 乘积 | 加权 |
|------|:---:|:---:|:---:|:---:|
| 衰退 | −18% | +10% | −0.0180 | −0.0060 |
| 正常 | +1% | 0% | 0 | 0 |
| 繁荣 | +17% | −10% | −0.0170 | −0.0057 |
| **合计** | | | | **−0.0117** |

$$Cov(Stock, Bond) = -0.0117$$

> 负协方差 → 股票和债券基金**反向变动**——这对分散化极其有利！

### 相关系数

$$\rho_{a,b} = \frac{Cov(a, b)}{\sigma_a \times \sigma_b}$$

$$\rho_{S,B} = \frac{-0.0117}{0.143 \times 0.082} = -0.998$$

| $\rho$ 值 | 含义 | 分散化效果 |
|-----------|------|:---:|
| $\rho = +1$ | 完全正相关 | 无 |
| $\rho = 0$ | 不相关 | 中等 |
| $\rho = -1$ | 完全负相关 | **最大** |
| $\rho = -0.998$ | 接近完全负相关 | **极强** |

## 📐 公式

| 概念 | 公式 |
|------|------|
| 协方差 | $Cov(a,b) = \sum W_i[R_a - E(R_a)][R_b - E(R_b)]$ |
| 相关系数 | $\rho_{a,b} = Cov(a,b) / (\sigma_a \sigma_b)$ |

## 📖 相关术语
- [[Portfolio Return and Risk 资产组合收益与风险]]：$\rho$ 决定了分散化能降低多少组合风险
- [[Systematic and Unsystematic Risk 系统风险与非系统风险]]：$\rho < 1$ 是分散化的数学基础

## ⚖️ 易混点对照（人类填写区域）
- 协方差 vs 相关系数：

## 📝 个人批注（人类专属，AI 严禁写入）

## 📄 来源原文
> If Cov(a,b) > 0, a and b have the same direction of changing. If Cov(a,b) < 0, a and b have the opposite direction of changing. The correlation of A and B is defined as: their covariance standardized by their standard deviations. If ρ=1, a and b have full positive relations. If ρ=-1, a and b have full negative relations.
