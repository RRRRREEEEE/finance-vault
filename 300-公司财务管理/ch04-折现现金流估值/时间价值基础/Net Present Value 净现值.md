---
tags:
  - 公司财务管理
  - ch04-折现现金流估值
  - 公式
courses: [公司财务管理]
aliases: [Net Present Value, 净现值, NPV]
created: 2026-06-29
source: "Chap4_Discounted Cash Evaluation.pdf 第13-18页"
chapter: "第4章 Discounted Cash Flow Valuation"
importance: "*****"
---

# 净现值 (Net Present Value)

## 📌 定义
净现值（NPV）是投资项目预期现金流的现值减去投资成本：**NPV = PV − Cost**。NPV > 0 → 接受项目；NPV < 0 → 拒绝项目。这是公司金融最核心的决策准则。

> 💬 通俗理解：一个项目让你现在花 $9,500，一年后收回 $10,000。按 5% 折现，$10,000 的现值 = $9,523.81。NPV = $9,523.81 − $9,500 = $23.81 > 0。值得投。

## 🔗 前置知识
[[Present Value 现值]]、[[Future Value 终值]]

## 📐 公式与计算

### 单期
$$ NPV = \frac{C_1}{1 + r} - Cost $$

$$ = \frac{10,000}{1.05} - 9,500 = 9,523.81 - 9,500 = 23.81 > 0 $$

### 验证：NPV > 0 意味着什么？
不投这个项目，把 $9,500 投到别处 5% → FV = $9,975 < $10,000
投这个项目 → FV = $10,000 > $9,975
**NPV > 0 = 你比次优选择赚得更多。**

### 多期
$$ NPV = -C_0 + \sum_{t=1}^{T} \frac{C_t}{(1+r)^t} $$

## 🧠 机制
- NPV 是**绝对金额**——告诉你赚了多少钱（不是百分比）
- NPV = 0：刚好赚到要求的回报率（不亏不赚）
- NPV 最大化 = 股东财富最大化

## 🏛️ 应用
- 公司金融最重要的投资决策规则——接受所有 NPV > 0 的项目
- 第1章资本预算的核心方法就是 NPV
- 整个 DCF 估值的理论基础

## 📖 相关术语
- [[Capital Budgeting 资本预算]]：NPV 是资本预算的核心方法
- [[Discount Rate 折现率]]：折现率的选取直接决定 NPV 的大小
- [[Present Value 现值]]：NPV = PV − Cost
- [[NPV Investment Rule NPV投资法则]]（ch07）：NPV 作为投资决策黄金准则的完整论述

## 📄 来源原文
> The Net Present Value (NPV) of an investment is the present value of the expected cash flows less the cost of the investment. NPV = PV of future cash flow − Cost.
