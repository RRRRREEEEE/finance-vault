---
tags:
  - 公司财务管理
  - ch06-股票估值
  - 模型
courses:
  - 公司财务管理
aliases:
  - Total Payout Valuation
  - 总支付估值
  - Share Repurchase Valuation
created: 2026-06-30
source: Chap6_Stock.pdf 第49-56页
chapter: "第6章 股票估值"
importance: "**"
---

# 总支付估值 (Total Payout Valuation)

## 📌 定义
公司向股东支付现金的方式不只有股利，还包括**股票回购**。总支付模型将回购视为"隐性股利"，以"股利 + 回购"的总额代入 DDM，得到更真实的股价估计。

> 💬 通俗理解：以前公司把利润分给你叫"股利"，现在很多公司改为买回自己的股票（推高股价让你赚差价）。如果只看股利不看回购，会低估公司给股东的实际回报。

## 🔗 前置知识
- [[Constant Growth Model 固定增长模型]]
- [[Cash Flow to Shareholders 股东现金流量]]：CF(S) = 股利 + 股票回购 - 新发行
- [[Dividend Discount Model 股利折现模型]]

## 🧠 机制

### 为什么只考虑股利会低估？

| 情形 | DDM 输入的 $Div_1$ | 股价估计 |
|------|-------------------|----------|
| 仅考虑股利 | 每股股利 | 较低 |
| 考虑总支付（股利 + 回购） | 每股总支付 | 较高 |

### 计算实例

> 某公司预期每股收益 $4.00，30% 用于股利，30% 用于股票回购，其余留存。增长率 5%，必要回报率 10%。求股价。

**仅考虑股利**：
- $Div_1 = \$4.00 \times 30\% = \$1.20$
- $P_0 = \dfrac{\$1.20}{0.10 - 0.05} = \$24.00$

**考虑总支付**：
- $Total\ Payout_1 = \$4.00 \times (30\% + 30\%) = \$2.40$
- $P_0 = \dfrac{\$2.40}{0.10 - 0.05} = \$48.00$

> **股价差一倍**——只关注股利会严重低估公司价值。

### 为什么公司偏好回购？

- **灵活性**：回购可以随时调整，股利一旦设立市场预期难以改变
- **税收优势**（部分国家）：资本利得税率低于股利税率
- **信号效应**：回购传递管理层认为股价被低估的信号

## 🏛️ 应用
- **科技公司估值**：Apple、Google 等大量回购的公司，总支付模型更准确
- 实际分析中应查看现金流量表中的 **CF(S)**（股东现金流量）= 股利 + 回购 − 新发行
- 回购是利润分配的另一形式，不应被估值模型忽略

## 📖 相关术语
- [[Cash Flow to Shareholders 股东现金流量]]：CF(S) 包含回购
- [[Constant Growth Model 固定增长模型]]：总支付可替代 $Div_1$ 进入公式
- [[Dividend Discount Model 股利折现模型]]：广义上"股利"可理解为总支付

## ⚖️ 易混点对照（人类填写区域）
- 股利 vs 回购对股价的影响机制：
- 总支付 vs 自由现金流：

## 📝 个人批注（人类专属，AI 严禁写入）
- 考试重点：
- 计算陷阱：
- 个人理解：

> 📌 考点提示：
> 💡 记忆技巧：
> 🔢 典型考题：

## 📄 来源原文
> A company's cash payout to Shareholders: Dividends and Repurchase of shares outstanding. What if considering the repurchase as implicit dividend? Answer: higher share price if considering total payout rather than just dividends. Example: A firm forecasts income of $4 per share and will payout 30% as dividends, 30% as share repurchase. If only considering dividend, D1 = $1.2, P0 = $24. If considering total payout, D1 = $2.4, P0 = $48.
