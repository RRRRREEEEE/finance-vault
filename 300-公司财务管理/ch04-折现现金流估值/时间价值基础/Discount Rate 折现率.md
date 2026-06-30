---
tags:
  - 公司财务管理
  - ch04-折现现金流估值
  - 概念
courses: [公司财务管理]
aliases: [Discount Rate, 折现率, Required Rate of Return, 必要回报率]
created: 2026-06-29
source: "Chap4_Discounted Cash Evaluation.pdf 第7、13、33页"
chapter: "第4章 Discounted Cash Flow Valuation"
importance: "***"
---

# 折现率 (Discount Rate)

## 📌 定义
折现率是将未来现金流折现为现值所使用的利率。它反映投资者要求的必要回报率（Required Rate of Return）——即资金的机会成本。

> 💬 通俗理解：折现率问"你的钱如果不投这个项目，放在别处能赚多少？"——那个"别处的回报率"就是折现率。风险越高，折现率越高，现值越低。

## 🔗 前置知识
[[Present Value 现值]]、[[Net Present Value 净现值]]

## 🧠 机制

### 折现率 ≠ 利率
- **利率**：市场上资金的价格（如存款利率、贷款利率）
- **折现率**：投资者的**必要回报率** = 无风险利率 + 风险溢价
- 同一个项目，不同投资者可能用不同折现率（取决于各自的机会成本）

### 折现率对现值的影响
$$ PV = \frac{FV}{(1+r)^T} $$

| r | T=5, FV=$10,000 | 现值 |
|----|----|------|
| 5% | — | $7,835 |
| 10% | — | $6,209 |
| 15% | — | $4,972 |

折现率越高 → 未来钱越不值钱 → 长期项目越难通过 NPV 检验。

### 从给定数据解出 r
$$ r = \left(\frac{FV}{PV}\right)^{1/T} - 1 $$

例：大学学费 12 年后需 $50,000，现有 $5,000 → r = (50000/5000)^(1/12) − 1 = **21.15%**

## 📖 相关术语
- [[Net Present Value 净现值]]：折现率直接决定 NPV
- [[Present Value 现值]]：折现是求现值的操作
- [[Effective Annual Rate 有效年利率]]：折现率通常以 EAR 形式使用

## 📄 来源原文
> If you know your required rate of return and the length of time before cash is harvested, you can calculate PV and FV.
