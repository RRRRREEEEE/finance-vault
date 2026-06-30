---
tags:
  - 公司财务管理
  - ch04-折现现金流估值
  - 概念
courses: [公司财务管理]
aliases: [APR, Annual Percentage Rate, 年百分比率, Nominal Rate, 名义利率]
created: 2026-06-29
source: "Chap4_Discounted Cash Evaluation.pdf 第45-48页"
chapter: "第4章 Discounted Cash Flow Valuation"
importance: "**"
---

# 年百分比率 (APR)

## 📌 定义
APR 是金融机构报价使用的**名义年利率**——它没有考虑复利频率的影响。APR = m × 每期利率。12% APR 月复利 = 每月 1%，EAR = (1.01)^12 − 1 = 12.68%。

> 💬 通俗理解：APR 是银行广告里的数字，EAR 是你口袋里的实际数字。永远用 EAR 比较不同产品。

## 🔗 前置知识
[[Effective Annual Rate 有效年利率]]

## 📐 公式与计算

$$ APR = m \times r_{period} $$

$$ EAR = \left(1 + \frac{APR}{m}\right)^m - 1 $$

| APR | 复利频率 | m | EAR |
|-----|----------|-----|------|
| 12% | 年 | 1 | 12.00% |
| 12% | 半年 | 2 | 12.36% |
| 12% | 月 | 12 | 12.68% |
| 12% | 日 | 365 | 12.75% |

## ⚖️ 易混点对照
- **APR vs EAR**：APR = 名义报价利率（不含复利频率因素），EAR = 实际年收益率（含复利频率）。永远用 EAR 做决策

## 📄 来源原文
> What is the Effective Annual Rate (EAR) of an 18% APR loan that is compounded monthly? EAR = (1 + 0.18/12)^12 − 1 = 19.56%.
