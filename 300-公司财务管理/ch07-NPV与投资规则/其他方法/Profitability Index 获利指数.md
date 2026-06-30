---
tags:
  - 公司财务管理
  - ch07-NPV与投资规则
  - 公式
courses:
  - 公司财务管理
aliases:
  - Profitability Index
  - PI
  - 获利指数
  - Benefit-Cost Ratio
created: 2026-06-30
source: Chap7_NPV.pdf 第25-29页
chapter: "第7章 NPV与投资规则"
importance: "***"
---

# 获利指数 (Profitability Index)

## 📌 定义
获利指数（PI）= 未来现金流的现值 ÷ 初始投资 = $PV / C_0$。它衡量**每一元投资能创造多少现值**——PI > 1 ⇔ NPV > 0。在资本受限时，PI 可用于排序。

> 💬 通俗理解：有两个项目——A 投 $100 赚 $200（PI=2），B 投 $10,000 赚 $15,000（PI=1.5）。PI 说 A 更"高效"，但 B 实际让你多赚了 $5,000。这就是 PI 的核心矛盾：效率 vs 规模。

## 🔗 前置知识
- [[NPV Investment Rule NPV投资法则]]
- [[Net Present Value 净现值]]（ch04）

## 🧠 机制

### 公式

$$PI = \frac{PV\ of\ Future\ Cash\ Flows}{Initial\ Investment}$$

### 决策规则

| 项目类型 | 接受标准 | 排序标准 |
|----------|----------|----------|
| 独立项目 | PI > 1 （⇔ NPV > 0） | — |
| 互斥项目 | — | ⚠️ **不能**用 PI 排序（规模问题） |

### 计算实例

> 初始投资 $200，年现金流 $50 / $100 / $150，折现率 12%。

$$PV = \frac{50}{1.12} + \frac{100}{1.12^2} + \frac{150}{1.12^3} = 44.64 + 79.72 + 106.77 = 231.13$$

$$PI = \frac{231.13}{200} = 1.16 > 1 \quad \text{→ 接受}$$

### 规模问题 (Scale Problem)

> 折现率为 0（单日投资），两个机会：

| 机会 | 投入 | 产出 | PI | NPV |
|------|------|------|-----|-----|
| 机会 1 | −$100 | +$200 | **2.0** | $100 |
| 机会 2 | −$10,000 | +$15,000 | **1.5** | $5,000 |

> PI 说选机会 1（2.0 > 1.5），但机会 2 多赚 $4,900！

**结论**：互斥项目 → 用 NPV 排序，用 NPV 排序，用 NPV 排序。

### 优缺点

| 优点 | 缺点 |
|------|------|
| 考虑了时间价值 | 互斥项目有**规模问题** |
| 资本受限时可用于排序 | PI 最高 ≠ NPV 最高 |
| 直观（"每一元赚多少"） | |
| 独立项目决策正确 | |

## 📊 图形

![[ch07 PI Scale Problem.png]]

> 图形说明：PI 的规模问题——两个机会 PI 高低与 NPV 大小恰好相反。

## 🏛️ 应用
- **资本配给 (Capital Rationing)**：资金有限时，按 PI 从高到低排序选择项目组合
- 独立项目初筛：PI > 1 等同于 NPV > 0
- 互斥项目 → 请使用 NPV

## 📖 相关术语
- [[NPV Investment Rule NPV投资法则]]：NPV = PI × C₀ − C₀
- [[Internal Rate of Return 内部报酬率]]：IRR 也有规模问题
- [[Capital Budgeting 资本预算]]（ch01）

## ⚖️ 易混点对照（人类填写区域）
- PI vs NPV：PI = 效率，NPV = 绝对值
- 什么时候用 PI 排序？

## 📝 个人批注（人类专属，AI 严禁写入）
- 考试重点：
- 计算陷阱：
- 个人理解：

## 📄 来源原文
> Profitability Index (PI) = PV of Future Cash Flows / Initial Investment. Minimum Acceptance Criteria (Independent project): Accept if PI > 1. Ranking Criteria (Mutually exclusive projects): Select alternative with highest PI. The Scale Problem: Opportunity 1 (-$100 → +$200, PI=2, NPV=$100) vs Opportunity 2 (-$10,000 → +$15,000, PI=1.5, NPV=$5,000). Choose the project with the highest NPV. Advantages: Time value of cash flows are considered, May be useful when available investment funds are limited. Disadvantages: Scale problem (with mutually exclusive investments).
