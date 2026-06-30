---
tags:
  - 公司财务管理
  - ch04-折现现金流估值
  - 公式
courses: [公司财务管理]
aliases: [Growing Annuity, 增长年金]
created: 2026-06-29
source: "Chap4_Discounted Cash Evaluation.pdf 第58-60页"
chapter: "第4章 Discounted Cash Flow Valuation"
importance: "**"
---

# 增长年金 (Growing Annuity)

## 📌 定义
增长年金是每期现金流按**固定增长率 g** 递增的有限期现金流序列。退休金（每年递增 3% 抗通胀）、递增租金都是典型应用。

> 💬 通俗理解：退休后每年领退休金，但每年比前一年多 3% 来跑赢通胀——这不是固定年金，是增长年金。

## 🔗 前置知识
[[Annuity 年金]]

## 📐 公式与计算

$$ PV = C \times \frac{1 - \left(\frac{1+g}{1+r}\right)^T}{r - g} $$

> C = 第一笔现金流，g = 增长率，r = 折现率，T = 期数

例：退休金每年 $20,000 共 40 年，每年增 3%，r = 7%：
$$ PV = 20000 \times \frac{1 - (1.03/1.07)^{40}}{0.07 - 0.03} $$

> ⚠️ r ≠ g ——分母不可为零

## 📖 相关术语
- [[Annuity 年金]]：g = 0 的特例
- [[Growing Perpetuity 增长永续年金]]：T → ∞ 的特例

## 📄 来源原文
> A growing stream of cash flows with a fixed maturity.
