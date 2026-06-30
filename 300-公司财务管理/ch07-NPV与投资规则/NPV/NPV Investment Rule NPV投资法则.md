---
tags:
  - 公司财务管理
  - ch07-NPV与投资规则
  - 模型
courses:
  - 公司财务管理
aliases:
  - NPV Investment Rule
  - NPV投资法则
  - NPV Decision Rule
created: 2026-06-30
source: Chap7_NPV.pdf 第5-10页
chapter: "第7章 NPV与投资规则"
importance: "*****"
---

# NPV 投资法则 (NPV Investment Rule)

## 📌 定义
NPV 投资法则：**接受所有 NPV > 0 的项目，选择 NPV 最高的项目**。这是公司金融中最优的投资决策准则——接受正 NPV 项目等于直接增加股东财富，公司价值上升的幅度恰好等于项目的 NPV。

> 💬 通俗理解：如果你能投一个"算出赚 $23"的项目，放到 5% 的市场上比"存银行吃利息"多赚 $23——这 $23 就是 NPV，纯赚的，投了股东就多赚。

## 🔗 前置知识
- [[Net Present Value 净现值]]（ch04）：NPV = PV − Cost 的基本定义
- [[Present Value 现值]]（货币金融学）
- [[Capital Budgeting 资本预算]]（ch01）：NPV 是资本预算的核心工具

## 🧠 机制

### 决策三步法

| 步骤 | 内容 |
|------|------|
| ① 估算 | 预测未来现金流：多少？何时？ |
| ② 确定折现率 | 使用项目风险对应的必要回报率 |
| ③ 计算 | $NPV = -C_0 + \sum \frac{C_t}{(1+r)^t}$ |

### 决策规则

| 项目类型 | 接受标准 | 排序标准 |
|----------|----------|----------|
| 独立项目 | NPV > 0 | 选 NPV 最高的 |
| 互斥项目 | — | **选 NPV 最高的**（而非 IRR 最高或 PI 最高） |

### 计算实例：礼品店

> 初始投资 $100,000，经营 5 年：年现金流 $33,000 / $38,000 / $43,000 / $48,000 / $53,000（每年递增 $5,000），要求回报 12%。

$$NPV = -100{,}000 + \frac{33{,}000}{1.12} + \frac{38{,}000}{1.12^2} + \frac{43{,}000}{1.12^3} + \frac{48{,}000}{1.12^4} + \frac{53{,}000}{1.12^5}$$

### NPV 为什么是最优准则？

| 优势 | 说明 |
|------|------|
| **使用现金流** | 不用会计利润（利润可被操纵），现金流才是真实的 |
| **使用全部现金流** | 不像回收期法——NPV 考虑项目全生命周期的所有现金流 |
| **正确折现** | 考虑了货币时间价值——$1 今天 ≠ $1 明年 |

## 📊 图形

![[ch07 NPV Shareholder Value.png]]

> 图形说明：接受正 NPV 项目 → 股东受益 → 公司价值上升的幅度 = NPV。

## 📐 公式

$$NPV = -C_0 + \sum_{t=1}^{T} \frac{C_t}{(1+r)^t}$$

| 符号 | 含义 |
|------|------|
| $C_0$ | 初始投资 |
| $C_t$ | 第 $t$ 期现金流 |
| $r$ | 折现率（必要回报率） |
| $T$ | 项目总期数 |

## 🏛️ 应用
- **股东财富最大化**：NPV 与股东财富直接挂钩——NPV +$1M → 公司价值 +$1M
- **资本预算基准**：所有其他方法（IRR、回收期、PI）最终都应与 NPV 决策一致
- 当其他方法与 NPV 结论冲突时 → **以 NPV 为准**

## 📖 相关术语
- [[Net Present Value 净现值]]（ch04）：NPV 基础公式
- [[Capital Budgeting 资本预算]]（ch01）：NPV 是资本预算的核心决策准则
- [[Internal Rate of Return 内部报酬率]]：IRR = 使 NPV = 0 的折现率
- [[Profitability Index 获利指数]]：PI = PV / 初始投资

## ⚖️ 易混点对照（人类填写区域）
- NPV vs 净利润：
- NPV = 0 为什么还值得投？（恰好赚到要求的回报率）

## 📝 个人批注（人类专属，AI 严禁写入）
- 考试重点：
- 计算陷阱：
- 个人理解：

## 📄 来源原文
> Net Present Value (NPV) = Total PV of future CF's - Initial Investment. Process: ① Estimate future cash flows: how much? and when? ② Estimate discount rate ③ Calculate PV & NPV. Decision-making: Minimum Acceptance Criteria: Accept if NPV > 0. Ranking Criteria: Choose the highest NPV. NPV uses cash flows (Not profit!), NPV uses all the cash flows of the project, NPV discounts the cash flows properly. Accepting positive NPV projects benefits shareholders. The value of the firm rises by the NPV of the project.
