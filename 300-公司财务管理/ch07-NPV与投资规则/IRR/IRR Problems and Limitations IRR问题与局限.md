---
tags:
  - 公司财务管理
  - ch07-NPV与投资规则
  - 概念
courses:
  - 公司财务管理
aliases:
  - IRR Problems and Limitations
  - IRR问题与局限
  - MIRR
  - Modified IRR
created: 2026-06-30
source: Chap7_NPV.pdf 第36-42页
chapter: "第7章 NPV与投资规则"
importance: "****"
---

# IRR 问题与局限 (IRR Problems and Limitations)

## 📌 定义
IRR 在**非常规现金流**和**互斥项目**两种情况下可能给出与 NPV 相反的结论。主要问题包括：投融资混淆、多 IRR、规模问题、时序问题。修正内部报酬率（MIRR）可以部分解决这些问题。

> 💬 通俗理解：IRR 像一把"万能尺子"，常规项目量得很准，但遇到"先拿钱后还钱"或者"两个项目抢资金"时，这把尺子就弯了。这时候要换 NPV 来量。

## 🔗 前置知识
- [[Internal Rate of Return 内部报酬率]]
- [[NPV Investment Rule NPV投资法则]]

## 🧠 机制

### 问题一：投融资混淆 (Investing vs Financing)

> 两个互斥项目的现金流符号相反：

| 项目 | 第 0 年 | 第 1 年 | IRR | NPV@10% |
|------|---------|---------|-----|---------|
| A（投资） | −$100 | +$130 | 30% | +$18.2 |
| B（融资） | +$100 | −$130 | 30% | −$18.2 |

**陷阱**：IRR 都是 30%，但 A 是投资（IRR > R → 接受），B 是融资（IRR < R → 接受——因为你是"借"钱，成本越低越好）。

> **修正**：融资项目的决策规则应反转——接受 IRR < R 的项目。

### 问题二：规模问题 (Scale Problem)

| 机会 | 投入 | 产出 | IRR | NPV@0% |
|------|------|------|-----|--------|
| 1 | −$100 | +$200 | **100%** | $100 |
| 2 | −$10,000 | +$15,000 | 50% | **$5,000** |

> IRR 说选机会 1，但机会 2 让你多赚 $4,900。**互斥项目必须用 NPV！**

### 问题三：时序问题 (Timing Problem)

| 项目 | C₀ | C₁ | C₂ | C₃ | NPV@0% | NPV@10% | NPV@15% | IRR |
|------|-----|-----|-----|-----|--------|---------|---------|-----|
| A | −$10,000 | $10,000 | $1,000 | $1,000 | $2,000 | **$669** | $109 | **16%** |
| B | −$10,000 | $1,000 | $1,000 | $12,000 | $4,000 | $751 | −$484 | 13% |

> 折现率低时（0%、10%），B 的 NPV 更高；折现率高时（15%），A 的 NPV 更高。IRR 永远偏好高早期现金流的项目——不一定是对的。

### 问题四：多重 IRR (Multiple IRRs)

现金流符号变换超过一次 → 可能有多个 IRR（笛卡尔符号法则：$n$ 次符号变换 → 最多 $n$ 个 IRR）：

$$-\$100 \rightarrow +\$230 \rightarrow -\$132$$

IRR₁ = 10%，IRR₂ = 20% → 应该用哪个？都是数学解。

### 修正方案：MIRR（修正内部报酬率）

| 步骤 | 操作 |
|------|------|
| ① | 以**借款利率**计算所有现金流出的现值 |
| ② | 以**再投资利率**计算所有现金流进的终值 |
| ③ | 找到使这两者相等的折现率 = MIRR |

> MIRR 的优点：单一解、指定具体的借款和再投资利率（而非假设 IRR 收益率再投资）。

## 📊 图形

![[ch07 IRR Investing vs Financing.png]]

> 图形说明：投资 vs 融资——IRR 相同但 NPV 符号相反，决策方向也相反。

![[ch07 IRR Timing Problem.png]]

> 图形说明：IRR 的时序问题——IRR 偏好的项目不一定 NPV 最高。

## 🏛️ 应用

| 场景 | 方法选择 |
|------|----------|
| 常规现金流、独立项目 | IRR 或 NPV 均可 |
| 非常规现金流 | 不要用 IRR → 用 NPV |
| 互斥项目 | 不要用 IRR → **用 NPV** |
| 融资项目 | IRR 规则反转 |
| 现金符号变换多次 | 不要用 IRR → 用 NPV 或 MIRR |

## 📖 相关术语
- [[Internal Rate of Return 内部报酬率]]：IRR 的基本定义
- [[NPV Investment Rule NPV投资法则]]：NPV 是互斥项目的正确选择标准
- [[Profitability Index 获利指数]]：PI 也有规模问题

## ⚖️ 易混点对照（人类填写区域）
- IRR 什么时候和 NPV 决策不一致？
- MIRR vs IRR：

## 📝 个人批注（人类专属，AI 严禁写入）
- 考试重点：
- 计算陷阱：
- 个人理解：

## 📄 来源原文
> NPV and IRR will generally give the same decision. Exceptions: Non-conventional cash flows (no difference for financing or investing, Multiple IRR when cash flow signs change more than once). Mutually exclusive projects (Initial investments are substantially different - scale problem, Timing of cash flows is substantially different). MIRR: Calculate the net present value of all cash outflows using the borrowing rate. Calculate the net future value of all cash inflows using the investing rate. Find the rate of return that equates these values. Benefits: single answer and specific rates for borrowing and reinvestment.
