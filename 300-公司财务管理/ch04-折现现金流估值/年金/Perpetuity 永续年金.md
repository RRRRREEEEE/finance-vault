---
tags:
  - 公司财务管理
  - ch04-折现现金流估值
  - 公式
courses: [公司财务管理]
aliases: [Perpetuity, 永续年金, 永续债券]
created: 2026-06-29
source: "Chap4_Discounted Cash Evaluation.pdf 第61-63页"
chapter: "第4章 Discounted Cash Flow Valuation"
importance: "***"
---

# 永续年金 (Perpetuity)

## 📌 定义
永续年金是**永远**每期支付等额现金流的资产。**PV = C / r**——这是金融学中最简洁的估值公式之一。

> 💬 通俗理解：英国政府发行的统一公债（consol）承诺永远每年付 £15，r = 10% → PV = 15/0.10 = £150。花 £150 就买了一份永久年金。

## 🔗 前置知识
[[Annuity 年金]]、[[Present Value 现值]]

## 📐 公式与计算

$$ PV = \frac{C}{r} $$

推导：年金 PV 公式中 T → ∞，(1+r)^(−T) → 0：
$$ PV = C \times \frac{1 - (1+r)^{-T}}{r} \rightarrow \frac{C}{r} \text{ as } T \rightarrow \infty $$

考例：英国统一公债每年 £15，利率 10%：
$$ PV = \frac{15}{0.10} = £150 $$

## 📖 相关术语
- [[Annuity 年金]]：年金 T → ∞ 的极限就是永续年金
- [[Growing Perpetuity 增长永续年金]]：现金流以 g 增长的永续年金
- [[Consol 永续债券]]（货币金融学）：永续年金在债券市场的经典案例

## 📄 来源原文
> A constant stream of cash flows that lasts forever. PV = C/r.
