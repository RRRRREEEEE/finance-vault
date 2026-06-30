---
tags:
  - 公司财务管理
  - ch07-NPV与投资规则
  - 概念
courses:
  - 公司财务管理
aliases:
  - Discounted Payback Period
  - 折现回收期
  - 折现回收期法
created: 2026-06-30
source: Chap7_NPV.pdf 第16-19页
chapter: "第7章 NPV与投资规则"
importance: "**"
---

# 折现回收期 (Discounted Payback Period)

## 📌 定义
折现回收期是普通回收期法的改进版本：将未来现金流**先折现**，再计算累计折现现金流回收初始投资所需的年数。它解决了普通回收期"忽略时间价值"的缺陷，但仍忽略了回收期后的现金流。

> 💬 通俗理解：普通回收期问"多久回本？"——但把明年的 $1 和今天的 $1 当一回事。折现回收期说："先把未来的钱打个折，再算多久回本"——合理多了。

## 🔗 前置知识
- [[Payback Period 投资回收期]]
- [[NPV Investment Rule NPV投资法则]]
- [[Present Value 现值]]（货币金融学）

## 🧠 机制

### 计算实例

> 初始投资 $100,000，年现金流 $33,000 / $38,000 / $43,000 / $48,000 / $53,000，折现率 12%，管理层要求 3 年内回收。

| 年 | 现金流 | PV of CF (12%) | 累计 NPV | 尚未回收 |
|----|--------|---------------|----------|----------|
| 0 | −$100,000 | −$100,000 | −$100,000 | $100,000 |
| 1 | +$33,000 | +$29,464 | −$70,536 | $70,536 |
| 2 | +$38,000 | +$30,293 | −$40,242 | $40,242 |
| 3 | +$43,000 | +$30,607 | −$9,636 | $9,636 |
| 4 | +$48,000 | +$30,505 | +$20,869 | → **回收！** |
| 5 | +$53,000 | +$30,074 | +$50,943 | |

折现回收期 ≈ **3.3 年**（3 + 9,636/30,505）。

> 管理层要求 3 年内回收 → **拒绝**（3.3 > 3）。

### 与普通回收期的比较

| 维度 | 普通回收期 | 折现回收期 |
|------|-----------|-----------|
| 时间价值 | ❌ 不考虑 | ✅ 考虑 |
| 回收后现金流 | ❌ 忽略 | ❌ 仍然忽略 |
| 计算复杂度 | 简单 | 中等 |
| 与 NPV 一致性 | 弱 | 较强 |

### 优缺点

| 优点 | 缺点 |
|------|------|
| 考虑了货币时间价值 | 仍然忽略回收期后的现金流 |
| 比普通回收期更合理 | 截止期仍然主观 |
| | 既然已经做了折现，还不如直接算 NPV |

> 🎓 **学术评价**："等你费劲把所有现金流折现完，不如顺手把 NPV 也算了。"——折现回收期的所有信息都在 NPV 计算中，多此一步意义有限。

## 📊 图形

![[ch07 Discounted Payback Example.png]]

> 图形说明：折现回收期完整计算表——每年现金流折现后逐步减除初始投资。

## 🏛️ 应用
- 作为普通回收期的改进版，适用于对时间价值敏感的流动性评估
- 实践中使用频率低于普通回收期（过于复杂却仍不完善）

## 📖 相关术语
- [[Payback Period 投资回收期]]：未折现版本
- [[NPV Investment Rule NPV投资法则]]：NPV 已包含折现回收期的所有信息
- [[Present Value 现值]]（货币金融学）：折现的数学基础

## ⚖️ 易混点对照（人类填写区域）
- 回收期 vs 折现回收期：关键差异在"折现"

## 📝 个人批注（人类专属，AI 严禁写入）
- 考试重点：
- 计算陷阱：
- 个人理解：

## 📄 来源原文
> How long does it take the project to "pay back" its initial investment? (taking the time value of money into account). Decision rule: Accept the project if it pays back on a discounted basis within the specified time. Example: $100,000 investment, cash flows $33k/$38k/$43k/$48k/$53k, 12% discount, 3-year cutoff. Discounted payback ≈ 3.3 years → Reject. Pros & Cons: Looks better than payback period method, but still ignores NPV. By the time you have discounted the cash flows, you might as well calculate the NPV.
