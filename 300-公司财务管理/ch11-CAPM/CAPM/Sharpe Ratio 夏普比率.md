---
tags:
  - 公司财务管理
  - ch11-CAPM
  - 公式
courses:
  - 公司财务管理
aliases:
  - Sharpe Ratio
  - 夏普比率
  - Reward-to-Variability Ratio
created: 2026-06-30
source: Chap11_CAPM.pdf 第53页
chapter: "第11章 CAPM"
importance: "**"
---

# 夏普比率 (Sharpe Ratio)

## 📌 定义
夏普比率由 William Sharpe 于 1966 年提出，衡量**每单位总风险获得的风险溢价**：$Sharpe\ Ratio = (R_i - R_F) / \sigma_i$。值越大，风险调整后的收益越好。

> 💬 通俗理解：两个基金经理都说自己赚了 15%。A 基金的波动是 10%，B 基金波动是 20%。谁更"划算"？夏普比率告诉你——A 的夏普比率 = (15% - 3%)/10% = 1.2，B 的 = (15% - 3%)/20% = 0.6。A 的"单位风险赚的钱"是 B 的两倍。

## 🔗 前置知识
- [[Capital Asset Pricing Model 资本资产定价模型]]
- [[Expected Return and Risk 期望收益与风险]]

## 🧠 机制

### 公式

$$Sharpe\ Ratio = \frac{R_i - R_F}{\sigma_i} = \frac{Risk\ Premium}{Total\ Risk}$$

| 组成部分 | 含义 |
|----------|------|
| $R_i - R_F$ | 风险溢价（超出无风险利率的收益） |
| $\sigma_i$ | 总风险（标准差） |

### 解释

| 夏普比率 | 含义 |
|:---:|------|
| > 1 | 优秀——每单位风险获得超过 100% 的补偿 |
| 0.5-1 | 良好 |
| < 0.5 | 一般 |
| < 0 | 连无风险收益都没跑赢 |

### 与其他指标的区别

| 指标 | 风险度量 | 问题 |
|------|----------|------|
| **夏普比率** | 总风险 $\sigma$ | — |
| **Treynor 比率** | 系统风险 $\beta$ | 适用于充分分散的组合 |
| **Jensen's Alpha** | $\beta$（回归截距） | 衡量超越 CAPM 的超额收益 |

## 🏛️ 应用
- **基金排名**：晨星等机构的基金评级核心指标之一
- **经理人评价**：排除规模因素后的"能力"度量
- 局限性：基于总风险 $\sigma$，对于未分散的组合可能不准确（此时用 Treynor 比率更好）

## 📖 相关术语
- [[Capital Asset Pricing Model 资本资产定价模型]]：CAPM 的理论延伸
- [[Beta Coefficient 贝塔系数]]：Treynor 比率使用 $\beta$ 而非 $\sigma$

## 📄 来源原文
> By William Sharpe in 1966. The ratio to evaluate a stock return by adjusting its risk. Sharpe Ratio = Risk Premium / SD. Also known as the Sharpe index, the Sharpe measure, and the reward-to-variability ratio. Usually, the larger the Sharpe ratio, the better the stock.
