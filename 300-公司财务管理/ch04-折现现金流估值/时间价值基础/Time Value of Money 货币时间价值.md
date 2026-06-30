---
tags:
  - 公司财务管理
  - ch04-折现现金流估值
  - 概念
courses: [公司财务管理]
aliases: [Time Value of Money, 货币时间价值, TVM]
created: 2026-06-29
source: "Chap4_Discounted Cash Evaluation.pdf 第3-7页"
chapter: "第4章 Discounted Cash Flow Valuation"
importance: "****"
---

# 货币时间价值 (Time Value of Money)

## 📌 定义
今天的一块钱比未来的一块钱更有价值——这是金融学最基础的原则。因为今天的钱可以**投资产生更多钱**，也可以**立即消费**。时间价值是折现现金流（DCF）估值的基石。

> 💬 通俗理解：现在给你 100 块 vs 一年后给你 100 块——你肯定选现在。因为存银行一年后变 105，或者现在就能花。

## 🧠 机制

### 四个核心变量
所有时间价值问题都涉及四个变量：
| 变量 | 符号 | 含义 |
|------|------|------|
| 现值 | PV (C₀) | 今天值多少钱 |
| 终值 | FV (C_T) | 未来值多少钱 |
| 时间 | T | 多少期 |
| 利率 | r | 每期回报率 |

知道任意三个，解出第四个。

### 核心公式一览
| 问题 | 公式 |
|------|------|
| 求终值 | FV = PV × (1 + r)^T |
| 求现值 | PV = FV / (1 + r)^T |
| 求净现值 | NPV = PV − Cost |
| 求期数 | T = ln(FV/PV) / ln(1+r) |
| 求利率 | r = (FV/PV)^(1/T) − 1 |

## 📖 相关术语
- [[Future Value 终值]]：时间价值的前向视角
- [[Present Value 现值]]：时间价值的后向视角（折现）
- [[Net Present Value 净现值]]：项目估值的基础——NPV > 0 接受
- [[Discount Rate 折现率]]：折现未来现金流的利率

## 📝 个人批注
- 考试重点：四变量互求
- 个人理解：

> 📌 考点提示：
> 💡 记忆技巧：
> 🔢 典型考题：

## 📄 来源原文
> A dollar today is more valuable than a dollar to be received in the future. Why? It can be invested to make more dollars; it can be immediately consumed.
