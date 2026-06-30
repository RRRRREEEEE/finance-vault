---
tags:
  - 公司财务管理
  - ch04-折现现金流估值
  - 公式
courses: [公司财务管理]
aliases: [Continuous Compounding, 连续复利]
created: 2026-06-29
source: "Chap4_Discounted Cash Evaluation.pdf 第49页"
chapter: "第4章 Discounted Cash Flow Valuation"
importance: "**"
---

# 连续复利 (Continuous Compounding)

## 📌 定义
连续复利是复利频率 m → ∞ 的极限情况——利息在每一瞬间都产生利息。**FV = PV × e^(rT)**，**EAR = e^r − 1**。

> 💬 通俗理解：月复利比年复利赚得多，日复利比月复利多……无限细分下去就是连续复利——理论上能赚最多的复利方式。

## 🔗 前置知识
[[Compounding 复利]]、[[Effective Annual Rate 有效年利率]]

## 📐 公式与计算

### 终值
$$ FV = PV \times e^{rT} $$

### 有效年利率
$$ EAR = e^{r} - 1 $$

12% APR 的极限：
$$ EAR = e^{0.12} - 1 = 12.75\% $$

（对比：月复利 12.68%，日复利 12.75%——几乎无差别。连续复利在实务中很少用，更多出现在期权定价等理论模型中。）

## 📄 来源原文
> The general formula for the future value of an investment compounded continuously: FV = PV × e^(rT).
