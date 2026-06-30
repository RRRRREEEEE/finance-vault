---
tags:
  - 公司财务管理
  - ch11-CAPM
  - 公式
courses:
  - 公司财务管理
aliases:
  - Beta Coefficient
  - 贝塔系数
  - β
created: 2026-06-30
source: Chap11_CAPM.pdf 第41-44页
chapter: "第11章 CAPM"
importance: "*****"
---

# 贝塔系数 (Beta Coefficient)

## 📌 定义
贝塔（$\beta$）是衡量单只股票**系统风险**的标准化指标：$\beta_i = Cov(R_i, R_M) / \sigma_M^2$。它度量股票收益对市场组合收益的**敏感度**——市场涨 1%，这只股票平均涨 $\beta_i\%$。

> 💬 通俗理解：$\beta = 1$ → 这只股票和市场同涨同跌（大盘股）。$\beta = 1.5$ → 市场涨 1%，它涨 1.5%（高弹性——涨得多也跌得狠）。$\beta = 0.5$ → 市场涨 1%，它只涨 0.5%（防御型——稳）。

## 🔗 前置知识
- [[Systematic and Unsystematic Risk 系统风险与非系统风险]]
- [[Covariance and Correlation 协方差与相关系数]]
- [[Capital Asset Pricing Model 资本资产定价模型]]

## 🧠 机制

### 贝塔公式

$$\beta_i = \frac{Cov(R_i, R_M)}{\sigma_M^2} = \frac{\rho_{i,M} \times \sigma_i \times \sigma_M}{\sigma_M^2} = \rho_{i,M} \times \frac{\sigma_i}{\sigma_M}$$

### 贝塔的回归解释

$$R_i = \alpha_i + \beta_i R_M + \varepsilon_i$$

- $\alpha_i$：截距（股票独立于市场的超额收益）
- $\beta_i$：斜率 = 贝塔 = 股票对市场的敏感度
- $\varepsilon_i$：误差项（公司特有部分 = 非系统风险）

### 贝塔的含义

| $\beta$ 值 | 含义 | 典型股票 |
|:---:|------|------|
| $\beta = 0$ | 与市场无关（理论上的无风险资产） | 短期国债 |
| $0 < \beta < 1$ | 防御型——波动小于市场 | 公用事业、消费品 |
| $\beta = 1$ | 与市场同幅度波动 | 大盘指数基金 |
| $\beta > 1$ | 进攻型——波动大于市场 | 科技股、周期股 |
| $\beta < 0$ | 与市场反向（罕见） | 黄金（有时） |

### 中国股票贝塔示例

| 股票 | $\beta$ |
|------|:---:|
| 阿里巴巴 | 1.60 |
| 贵州茅台 (600519) | 1.33 |
| 腾讯 | 0.99 |
| 京东 | 0.89 |

### 组合贝塔

$$\beta_P = \sum_{i=1}^{n} w_i \times \beta_i$$

> 组合的贝塔 = 各只股票贝塔的**加权平均**（与收益的计算方式一样）。

## 📊 图形

![[ch11 Beta Regression Line.png]]

> 图形说明：$\beta$ 的回归估计——横轴为市场收益 $R_M$，纵轴为股票收益 $R_i$，贝塔 = 回归线的斜率。

## 🏛️ 应用
- **CAPM 的核心输入**：$E(R_i) = R_F + \beta_i (E(R_M) - R_F)$
- **风险对冲**：如果组合 $\beta_P = 1.2$ 太激进 → 卖出 $\beta$ 高的股票或加入低 $\beta$ 资产
- 贝塔通常用过去 3-5 年月度数据回归估算

## 📖 相关术语
- [[Capital Asset Pricing Model 资本资产定价模型]]：$\beta$ → CAPM → 期望收益
- [[Systematic and Unsystematic Risk 系统风险与非系统风险]]：$\beta$ 度量的是系统风险
- [[SML Security Market Line 证券市场线]]：$\beta$ 在 SML 上是横坐标

## ⚖️ 易混点对照（人类填写区域）
- $\beta$ vs $\sigma$：$\beta$ = 系统风险度量，$\sigma$ = 总风险度量
- $\beta$ vs 相关系数：

## 📝 个人批注（人类专属，AI 严禁写入）

## 📄 来源原文
> The "best" measure of the risk of a stock in a large portfolio is the beta (β) of the security. Beta: the responsiveness of a stock to the movements in the market portfolio. βi = Cov(Ri, RM) / σM². The responsiveness of a portfolio of stocks to the movement in stock market: βportfolio = Σ(wi × βi). Alibaba: 1.60, JINGDONG: 0.89, Tencent: 0.99, 贵州茅台: 1.33.
