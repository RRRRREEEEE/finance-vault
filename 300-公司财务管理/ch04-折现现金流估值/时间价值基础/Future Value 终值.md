---
tags:
  - 公司财务管理
  - ch04-折现现金流估值
  - 公式
courses: [公司财务管理]
aliases: [Future Value, 终值, FV, Compound Value]
created: 2026-06-29
source: "Chap4_Discounted Cash Evaluation.pdf 第8-25页"
chapter: "第4章 Discounted Cash Flow Valuation"
importance: "****"
---

# 终值 (Future Value)

## 📌 定义
终值（FV）是将当前的一笔资金按给定利率复利增长到未来某一时点的价值。**FV = C₀ × (1 + r)^T**。

> 💬 通俗理解：今天 $10,000 按 5% 存 5 年 → FV = 10000 × 1.05^5 = $12,762.82。利滚利的魔力在于指数增长。

## 🔗 前置知识
[[Time Value of Money 货币时间价值]]

## 📐 公式与计算

### 单期
$$ FV = C_0 \times (1 + r) $$

### 多期（一般公式）
$$ FV = C_0 \times (1 + r)^T $$

> $C_0$ = 初始投资，$r$ = 每期利率，$T$ = 期数

### 复利的威力
股利 $1.10，每年增长 40%，5 年后：
$$ 1.10 \times (1.40)^5 = \$5.92 $$

简单加总 = $1.10 + 5 × 0.44 = $3.30
实际终值 = **$5.92**
差距来自**利滚利**（compound interest on interest）。

## 🧠 机制
- (1+r)^T 是指数函数 → T 越大增长越快
- FV 对 r 和 T 都高度敏感
- 72 法则：估算翻倍年数 ≈ 72 ÷ r(%)

## 📖 相关术语
- [[Present Value 现值]]：FV 的逆运算
- [[Compounding 复利]]：指数增长背后的机制
- [[Effective Annual Rate 有效年利率]]：复利频率影响实际 FV

## 📄 来源原文
> The general formula for FV: FV = C₀ × (1 + r)^T. The total amount due at the end of the investment is called the Future Value.
