---
tags:
  - 公司财务管理
  - ch07-NPV与投资规则
  - 模型
courses:
  - 公司财务管理
aliases:
  - Internal Rate of Return
  - IRR
  - 内部报酬率
  - 内部收益率
created: 2026-06-30
source: Chap7_NPV.pdf 第31-41页
chapter: "第7章 NPV与投资规则"
importance: "*****"
---

# 内部报酬率 (Internal Rate of Return)

## 📌 定义
内部报酬率（IRR）是使项目 NPV 恰好等于零的折现率：$NPV(IRR) = 0$。决策规则：**如果 IRR > 必要回报率，接受项目**。IRR 是实践中与 NPV 并列最常用的投资决策方法。

> 💬 通俗理解：IRR 告诉你这个项目本身的"年化收益率"是多少——算出来是 19.44%，而你的资金成本是 12%，说明投这个项目赚的比资金成本高，值得投。

## 🔗 前置知识
- [[NPV Investment Rule NPV投资法则]]
- [[Net Present Value 净现值]]（ch04）
- [[Discount Rate 折现率]]

## 🧠 机制

### 定义公式

$$NPV = -C_0 + \frac{C_1}{1+IRR} + \frac{C_2}{(1+IRR)^2} + \cdots + \frac{C_T}{(1+IRR)^T} = 0$$

IRR 就是解这个方程得出的 $r$。

### 计算实例

> 项目现金流：−$200 / +$50 / +$100 / +$150

使用 Excel `=IRR({-200,50,100,150})` = **19.44%**

$$IRR = 19.44\% > 12\% \quad \text{→ 接受}$$

### NPV 曲线与 IRR

| 折现率 | NPV |
|--------|-----|
| 0% | $100.00 |
| 4% | $73.88 |
| 8% | $51.11 |
| 12% | $31.13 |
| 16% | $13.52 |
| **19.44%** | **$0.00** ← IRR |
| 24% | −$15.97 |
| 40% | −$58.60 |

> IRR = NPV 曲线与 x 轴的交点。折现率 < IRR → NPV > 0；折现率 > IRR → NPV < 0。

### 决策规则与关键假设

| 规则 | 说明 |
|------|------|
| 接受标准 | IRR > 必要回报率（$R$） |
| 排序标准（互斥项目） | 选 IRR 最高的 — ⚠️ 可能有陷阱 |
| **隐含假设** | **所有期间现金流均能以 IRR 的收益率再投资** |

### NPV 与 IRR 的决策一致性

对于**常规现金流**（先负后正，符号只变一次）：
- IRR > R ⇔ NPV > 0 → **决策一致**
- IRR < R ⇔ NPV < 0 → **决策一致**

> 常规现金流的独立项目：NPV 和 IRR 永远给出相同结论。

## 📊 图形

![[ch07 NPV and IRR Graph.png]]

> 图形说明：NPV 曲线随折现率递减——IRR = NPV 曲线与 x 轴的交点（IRR = 19.44%）。当折现率 < IRR 时 NPV > 0，接受；当折现率 > IRR 时 NPV < 0，拒绝。

## 📐 公式

$$0 = -C_0 + \sum_{t=1}^{T} \frac{C_t}{(1+IRR)^t}$$

## 🏛️ 应用
- 与 NPV 并列最常用的投资决策方法（大公司评分 3.41 vs NPV 的 3.42）
- **金融产品收益率表达**：债券的 YTM = 债券的 IRR
- 不需预先指定折现率即可计算（但需要折现率来做决策判断）

## 📖 相关术语
- [[NPV Investment Rule NPV投资法则]]：NPV 和 IRR 是"双胞胎"——常规项目决策一致
- [[IRR Problems and Limitations IRR问题与局限]]：非常规现金流和互斥项目时 IRR 可能"叛变"
- [[Yield to Maturity 到期收益率]]（货币金融学）：YTM = 债券的 IRR

## ⚖️ 易混点对照（人类填写区域）
- IRR vs NPV：哪个是"收益率"、哪个是"绝对值"？
- IRR vs 必要回报率：

## 📝 个人批注（人类专属，AI 严禁写入）
- 考试重点：
- 计算陷阱：
- 个人理解：

## 📄 来源原文
> IRR: the discount rate that sets NPV to zero. Decision Making Rule: Minimum Acceptance Criteria: Accept if the IRR exceeds the required return. Ranking Criteria: Select alternative with the highest IRR, for mutually exclusive projects. Assumption: All the cash flows are reinvested at the rate of return. Example: cash flows -$200 / +$50 / +$100 / +$150, IRR = 19.44% > 12% → Accept. If we graph NPV versus the discount rate, we can see the IRR as the x-axis intercept.
