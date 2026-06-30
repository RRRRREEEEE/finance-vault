---
tags:
  - 公司财务管理
  - ch12-资本成本
  - 公式
courses:
  - 公司财务管理
aliases:
  - Cost of Equity with DDM
  - 股利折现法估算权益成本
  - DDM Cost of Equity
created: 2026-06-30
source: Chap12_Cost_of_Capital.pdf 第27-28页
chapter: "第12章 资本成本"
importance: "**"
---

# 股利折现法估算权益成本 (Cost of Equity with DDM)

## 📌 定义
DDM 提供了 CAPM 之外的另一种估算 $R_E$ 的方法：从固定增长模型反推 $R_E = D_1/P_0 + g$。学术界通常偏好 CAPM，但 DDM 可作为交叉验证。

> 💬 通俗理解：如果一只股票现在 $61，下一年股利大约 $0.84，预期每年增长 5%——那么市场隐含的期望回报 = $0.84/$61 + 5% = 6.38%。这就是 DDM 告诉你的"股东要求的回报率"。

## 🔗 前置知识
- [[Cost of Equity Capital 权益资本成本]]
- [[Constant Growth Model 固定增长模型]]（ch06）
- [[Required Return Estimation 必要收益率估计]]（ch06）

## 🧠 机制

### 公式

$$R_E = \frac{D_1}{P_0} + g$$

| 组成部分 | 含义 | 来源 |
|----------|------|------|
| $D_1/P_0$ | 预期股利收益率 | 分析师预测 / 历史股利 |
| $g$ | 股利长期增长率 | 分析师预测 / $g = b \times ROE$ |

### 计算实例

> Eastman Chemical：分析师一致预测 5 年盈利增长 7%，股利收益率 4.40%。

$$R_E = 4.40\% + 7\% = 11.40\%$$

### CAPM vs DDM

| 方法 | 公式 | 优点 | 缺点 |
|------|------|------|------|
| **CAPM** | $R_E = R_F + \beta(R_M - R_F)$ | 理论基础强，学术偏好 | 需要估 $\beta$ 和市场风险溢价 |
| **DDM** | $R_E = D_1/P_0 + g$ | 简单直观 | 需要预测 $g$（测量误差大） |

> 实践中企业更多使用 CAPM。两者可以交叉验证——如果结果差异很大，需检查假设是否正确。

## 📖 相关术语
- [[Cost of Equity Capital 权益资本成本]]：主要方法
- [[Required Return Estimation 必要收益率估计]]（ch06）：同公式，两种视角
- [[Constant Growth Model 固定增长模型]]（ch06）：公式来源

## 📄 来源原文
> The DDM is an alternative to the CAPM for calculating a firm's cost of equity. The DDM and CAPM are internally consistent, but academics generally favor the CAPM and companies seem to use the CAPM more consistently. This may be due to the measurement error associated with estimating company growth. R = D1/P0 + g.
