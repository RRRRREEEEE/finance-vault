---
tags:
  - 公司财务管理
  - ch07-NPV与投资规则
  - 概念
courses:
  - 公司财务管理
aliases:
  - Payback Period
  - 投资回收期
  - 回收期法
created: 2026-06-30
source: Chap7_NPV.pdf 第12-14页
chapter: "第7章 NPV与投资规则"
importance: "***"
---

# 投资回收期 (Payback Period)

## 📌 定义
投资回收期是**收回初始投资所需的年数**：累计未折现现金流何时等于初始投资。回收期越短越好，企业管理层设定一个**主观的回收截止期**来决定是否接受项目。

> 💬 通俗理解：你投了 $50,000 开店，第一年赚 $30,000，第二年赚 $20,000——两年就回了本。如果老板说"超过 3 年的项目不投"，这恰好过关。但如果老板说了 2 年……这项目就无缘了——问题就出在这个"老板说了"上。

## 🔗 前置知识
- [[NPV Investment Rule NPV投资法则]]
- [[Capital Budgeting 资本预算]]（ch01）

## 🧠 机制

### 计算方法

> 项目初始投资 $50,000，年现金流：$30,000 → $20,000 → $10,000。

| 年 | 现金流 | 累计现金流 | 尚未收回 |
|----|--------|-----------|----------|
| 0 | −$50,000 | −$50,000 | $50,000 |
| 1 | +$30,000 | −$20,000 | $20,000 |
| 2 | +$20,000 | $0 | $0 → **回收！** |

回收期 = **2 年**。

> 若每年均匀流入 $20,000：回收期 = $50,000 / $20,000 = **2.5 年**。

### 决策规则

| 规则 | 说明 |
|------|------|
| 接受标准 | 回收期 ≤ 管理层预先设定的截止期 |
| 排序标准 | 选择回收期最短的项目 |

### 优缺点

| 优点 | 缺点 |
|------|------|
| **简单易懂** | ❌ **忽略货币时间价值**（不折现） |
| **偏好流动性**（尽快回本的项目风险更小） | ❌ **忽略回收期后的现金流**（短期偏见） |
| 实践中常用于小型投资决策 | ❌ **排斥长期项目**（R&D、品牌建设等） |
| | ❌ **截止期完全主观**——没有客观标准 |
| | ❌ **按回收期接受的项目 NPV 可能为负** |

> 🎓 学术界普遍批评回收期法，但实务中它仍然被广泛使用——尤其是配合作为主流方法（NPV/IRR）的**辅助筛选工具**。

## 📐 公式

$$Payback\ Period = T \quad \text{当} \sum_{t=1}^{T} CF_t = \text{Initial Investment}$$

## 🏛️ 应用
- 小型投资决策（"小项目没必要算 NPV"）
- 流动性紧张的企业（尽快回本）
- 作为 NPV/IRR 的**初筛**工具——先筛掉回收期过长的，再细算

## 📖 相关术语
- [[NPV Investment Rule NPV投资法则]]：最优准则（回收期法有严重缺陷）
- [[Discounted Payback Period 折现回收期]]：改进版——考虑了时间价值
- [[Internal Rate of Return 内部报酬率]]：另一种"速度"视角的决策方法

## ⚖️ 易混点对照（人类填写区域）
- 回收期 vs 折现回收期：
- 为什么学术界批评但实务界还在用？

## 📝 个人批注（人类专属，AI 严禁写入）
- 考试重点：
- 计算陷阱：
- 个人理解：

## 📄 来源原文
> How long does it take the project to "pay back" its initial investment? Payback Period = number of years to recover initial investment. Decision making: Compare to the predetermined time period (set by the management). Ranking Criteria: Choose the shortest payback period. Disadvantages: Ignores the time value of money, Ignores cash flows after the payback period, Biased against long-term projects, Requires an arbitrary acceptance criteria, A project accepted based on the payback criteria may not have a positive NPV. Advantages: Easy to understand, Biased toward liquidity.
