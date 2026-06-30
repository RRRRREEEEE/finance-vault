---
tags:
  - 公司财务管理
  - ch04-折现现金流估值
  - 公式
courses: [公司财务管理]
aliases: [Growing Perpetuity, 增长永续年金, Gordon Growth Model]
created: 2026-06-29
source: "Chap4_Discounted Cash Evaluation.pdf 第64-66页"
chapter: "第4章 Discounted Cash Flow Valuation"
importance: "***"
---

# 增长永续年金 (Growing Perpetuity)

## 📌 定义
增长永续年金是每期现金流按**固定增长率 g** 递增的永久现金流：**PV = C₁ / (r − g)**。这是**戈登增长模型**（Gordon Growth Model）的数学基础——股票估值的核心公式。

> 💬 通俗理解：一家公司明年分红 $1.30，以后每年增 5%，r = 10% → PV = 1.30/(0.10−0.05) = $26。这就是股票的内在价值。

## 🔗 前置知识
[[Perpetuity 永续年金]]、[[Growing Annuity 增长年金]]

## 📐 公式与计算

$$ PV = \frac{C_1}{r - g} $$

> 条件：r > g（分母不可为负或零）

推导：增长年金公式中 T → ∞，(1+g)^T/(1+r)^T → 0（当 r > g）：
$$ PV = C \times \frac{1 - \left(\frac{1+g}{1+r}\right)^T}{r-g} \rightarrow \frac{C_1}{r-g} \text{ as } T \rightarrow \infty $$

例：明年股利 $1.30，g = 5%，r = 10%：
$$ PV = \frac{1.30}{0.10 - 0.05} = \$26.00 $$

## 🏛️ 应用
- **戈登增长模型** = 股票估值最基础的 DCF 模型
- ch06 股票估值将以此为核心公式
- 永续现金流现值评估（如永续特许权）

## 📖 相关术语
- [[Perpetuity 永续年金]]：g = 0 的特例
- [[Stock Valuation 股票估值]]（货币金融学）：戈登模型 = 增长永续年金的经典应用
- [[Growing Annuity 增长年金]]：有限期版本

## 📄 来源原文
> A growing stream of cash flows that lasts forever. PV = C₁/(r − g). The expected dividend next year is $1.30, growing at 5% forever, discount rate 10% → $26.00.
