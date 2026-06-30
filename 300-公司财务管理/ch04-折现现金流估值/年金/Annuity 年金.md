---
tags:
  - 公司财务管理
  - ch04-折现现金流估值
  - 公式
courses: [公司财务管理]
aliases: [Annuity, 年金, Ordinary Annuity]
created: 2026-06-29
source: "Chap4_Discounted Cash Evaluation.pdf 第51-57页"
chapter: "第4章 Discounted Cash Flow Valuation"
importance: "****"
---

# 年金 (Annuity)

## 📌 定义
年金是在**固定期数**内，每期产生**等额现金流**的一系列支付。房贷月供、退休年金、分期付款都是年金的典型应用。

> 💬 通俗理解：每月还房贷 $3,000，还 30 年（360 个月）——这就是一笔年金。知道利率，就能算你需要借多少钱（PV），或者总共还多少（FV）。

## 🔗 前置知识
[[Present Value 现值]]、[[Future Value 终值]]

## 📐 公式与计算

### 年金的现值（PV）
$$ PV = C \times \frac{1 - (1 + r)^{-T}}{r} $$

| 变量 | 含义 |
|------|------|
| C | 每期固定支付额 |
| r | 每期利率 |
| T | 总期数 |
| $$ \frac{1-(1+r)^{-T}}{r} $$ | **年金现值系数 (PVIFA)** |

例：月供 $400，36 月，月利率 7%/12 = 0.583%：
$$ PV = 400 \times \frac{1 - (1.00583)^{-36}}{0.00583} = \$12,954.59 $$

→ 利率 7% 时，你最多能贷 $12,955 买车。

### 年金的终值（FV）
$$ FV = C \times \frac{(1 + r)^T - 1}{r} $$

## 🏛️ 应用
- 房贷月供计算
- 退休储蓄规划
- 债券定价（固定息票债券 = 年金 PV + 本金 PV）
- 租赁、保险精算

## 📖 相关术语
- [[Perpetuity 永续年金]]：年金 T → ∞ 的特例
- [[Growing Annuity 增长年金]]：现金流按固定增长率增长的年金
- [[Amortized Loan 分期偿还贷款]]：年金的实际应用——等额本息还款

## 📄 来源原文
> Annuity: A stream of constant cash flows that lasts for a fixed number of periods.
