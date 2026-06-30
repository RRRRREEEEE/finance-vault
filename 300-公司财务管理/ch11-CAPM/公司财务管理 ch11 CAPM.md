---
tags:
  - 公司财务管理
  - ch11-CAPM
  - 索引
courses:
  - 公司财务管理
created: 2026-06-30
source: Chap11_CAPM.pdf
chapter: "第11章 CAPM"
importance: "*****"
---

# 公司财务管理 · ch11 CAPM

> 57 页 PDF | 2026-06-30 完成 | 8 篇笔记 | 8 张图表

## 章节概要

本章从单只证券的期望收益和风险出发，引入协方差与相关系数量化证券间的互动关系；进而推导资产组合的收益与风险公式，揭示分散化的数学基础；通过有效边界理论确定最优组合集合；将收益和风险分别分解为系统与非系统部分，论证只有系统风险获得市场补偿；最后引入贝塔系数和 CAPM 公式，建立期望收益与系统风险之间的线性定价关系（SML），以及夏普比率的风险调整绩效评价。

## 内容结构

| # | 主题 | 页数 | 笔记 |
|---|------|------|------|
| ① | 单只证券特征 | 3-13 | [[Expected Return and Risk 期望收益与风险]]、[[Covariance and Correlation 协方差与相关系数]] |
| ② | 资产组合 | 15-20 | [[Portfolio Return and Risk 资产组合收益与风险]] |
| ③ | 有效边界 | 22-28 | [[Efficient Frontier 有效边界]] |
| ④ | 收益/风险分解 | 30-39 | [[Systematic and Unsystematic Risk 系统风险与非系统风险]] |
| ⑤ | 贝塔系数 | 41-44 | [[Beta Coefficient 贝塔系数]] |
| ⑥ | CAPM | 46-57 | [[Capital Asset Pricing Model 资本资产定价模型]]、[[Sharpe Ratio 夏普比率]] |

## 笔记列表

### 风险与收益
- [[Expected Return and Risk 期望收益与风险]] (****)
- [[Covariance and Correlation 协方差与相关系数]] (***)
- [[Systematic and Unsystematic Risk 系统风险与非系统风险]] (*****)

### 资产组合
- [[Portfolio Return and Risk 资产组合收益与风险]] (*****)
- [[Efficient Frontier 有效边界]] (****)

### CAPM
- [[Beta Coefficient 贝塔系数]] (*****)
- [[Capital Asset Pricing Model 资本资产定价模型]] (*****)
- [[Sharpe Ratio 夏普比率]] (**)

## 关键公式速查

| 概念 | 公式 |
|------|------|
| 期望收益 | $E(R) = \sum W_i R_i$ |
| 方差 | $\sigma^2 = \sum W_i [R_i - E(R)]^2$ |
| 协方差 | $Cov(a,b) = \sum W_i [R_a - E(R_a)][R_b - E(R_b)]$ |
| 相关系数 | $\rho = Cov(a,b) / (\sigma_a \sigma_b)$ |
| 组合方差 | $\sigma_P^2 = w_S^2\sigma_S^2 + w_B^2\sigma_B^2 + 2w_S w_B Cov(S,B)$ |
| 贝塔 | $\beta_i = Cov(R_i, R_M) / \sigma_M^2$ |
| **CAPM** | $E(R_i) = R_F + \beta_i [E(R_M) - R_F]$ |
| 夏普比率 | $Sharpe = (R_i - R_F) / \sigma_i$ |

## 逻辑链

```
单只证券: E(R) + σ²
    ↓
协方差 Cov → 相关系数 ρ
    ↓
组合理论: E(R_P)=加权平均, σ_P < 加权平均 σ
    ↓
有效边界: 给定收益最小风险 / 给定风险最大收益
    ↓
风险分解: 总风险 = 系统 + 非系统 → 分散化消除非系统
    ↓
贝塔 β: 标准化系统风险度量
    ↓
CAPM: E(R_i) = R_F + β_i(E(R_M)-R_F) → SML
    ↓
夏普比率: 风险调整绩效 = (R-R_F)/σ
```

## 图像附件

- ![[ch11 Stock Bond Risk Return Table.png]]
- ![[ch11 Portfolio Diversification Effect.png]]
- ![[ch11 Portfolio Risk Return Combinations.png]]
- ![[ch11 Correlation and Diversification.png]]
- ![[ch11 Efficient Frontier.png]]
- ![[ch11 Systematic vs Unsystematic Risk.png]]
- ![[ch11 Beta Regression Line.png]]
- ![[ch11 SML Security Market Line.png]]

> 共 8 张图像。
