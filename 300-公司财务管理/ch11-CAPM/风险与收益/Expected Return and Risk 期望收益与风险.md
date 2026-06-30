---
tags:
  - 公司财务管理
  - ch11-CAPM
  - 公式
courses:
  - 公司财务管理
aliases:
  - Expected Return and Risk
  - 期望收益与风险
  - Variance and Standard Deviation
created: 2026-06-30
source: Chap11_CAPM.pdf 第3-13页
chapter: "第11章 CAPM"
importance: "****"
---

# 期望收益与风险 (Expected Return and Risk)

## 📌 定义
单只证券的两个基本特征：**期望收益** $E(R)$（加权平均的未来可能收益）和**风险**（用方差 $\sigma^2$ 或标准差 $\sigma$ 度量——收益偏离期望值的波动程度）。

> 💬 通俗理解：买一只股票你关心两件事——平均能赚多少（$E(R)$），以及赚多赚少有多不稳定（$\sigma$）。如果两个股票期望收益一样，你肯定选波动小的那个。

## 🔗 前置知识
- [[Risk 风险]]（货币金融学）
- [[Portfolio 资产组合]]（货币金融学）

## 🧠 机制

### 计算实例

> 三种经济状态（等概率），两只风险资产：

| 情景 | 概率 | 股票基金 | 债券基金 |
|------|:---:|:---:|:---:|
| 衰退 (Recession) | 33.3% | −7% | 17% |
| 正常 (Normal) | 33.3% | 12% | 7% |
| 繁荣 (Boom) | 33.3% | 28% | −3% |

### 期望收益

$$E(R) = \sum_{i=1}^{n} W_i \times R_i$$

$$E(R_{stock}) = 33.3\%\times(-7\%) + 33.3\%\times12\% + 33.3\%\times28\% = 11.00\%$$
$$E(R_{bond}) = 33.3\%\times17\% + 33.3\%\times7\% + 33.3\%\times(-3\%) = 7.00\%$$

### 方差与标准差

$$\sigma^2 = \sum W_i \times [R_i - E(R)]^2$$

| 资产 | 方差 $\sigma^2$ | 标准差 $\sigma$ |
|------|:---:|:---:|
| 股票基金 | 0.0205 | **14.3%** |
| 债券基金 | 0.0067 | **8.2%** |

> 股票基金：更高收益（11% vs 7%），但也更高风险（14.3% vs 8.2%）——**风险-收益权衡**。

## 📊 图形

![[ch11 Stock Bond Risk Return Table.png]]

> 图形说明：股票基金与债券基金的收益、方差、标准差计算表。

## 📐 公式

| 概念 | 公式 |
|------|------|
| 期望收益 | $E(R) = \sum W_i R_i$ |
| 方差 | $\sigma^2 = \sum W_i [R_i - E(R)]^2$ |
| 标准差 | $\sigma = \sqrt{\sigma^2}$ |

## 📖 相关术语
- [[Covariance and Correlation 协方差与相关系数]]：两只证券之间的互动关系
- [[Portfolio Return and Risk 资产组合收益与风险]]：组合后的收益和风险不是简单平均
- [[Systematic and Unsystematic Risk 系统风险与非系统风险]]：总风险的分解

## ⚖️ 易混点对照（人类填写区域）
- 方差 vs 标准差：方差是平方，标准差还原了量纲
- 期望收益 vs 实现收益：

## 📝 个人批注（人类专属，AI 严禁写入）
- 考试重点：
- 计算陷阱：
- 个人理解：

## 📄 来源原文
> Characteristics of individual securities: Return: Expected Return, Risk: Variance and Standard Deviation, Interaction: Covariance and Correlation. Expected return: E(R) = Σ Wi × Ri. Variance: the expectation of the squared differences between stock returns over their expected ones → uncertainty → risk. Standard deviation: the square root of variance.
