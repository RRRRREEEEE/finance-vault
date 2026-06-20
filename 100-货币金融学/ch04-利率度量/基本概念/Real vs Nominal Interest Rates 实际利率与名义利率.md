---
tags:
  - 货币金融学
  - ch04-利率度量
  - 公式
courses:
  - 货币金融学
aliases:
  - Real vs Nominal Interest Rates
  - 实际利率与名义利率
  - Fisher Equation
  - 费雪方程式
created: 2026-06-06
source: Ch04-2026-T(3).pptx 第35-39页
chapter: Chapter 4 The Meaning of Interest Rates
importance: "*****"
---

# 实际利率与名义利率 (Real vs Nominal Interest Rates)

## 📌 定义
名义利率不考虑通货膨胀；实际利率根据价格水平变化调整，更准确反映借款的真实成本。费雪方程式：$i_r = i - \pi^e$。

> 💬 通俗理解：名义利率是银行标给你的利率（比如5%），实际利率是扣除通胀后你真正赚/付的利率（通胀3%→实际只有2%）。

## 🔗 前置知识
- [[Money and Interest Rates 货币与利率]]
- [[Money and Inflation 货币与通货膨胀]]

## 🧠 机制

### Fisher Equation（费雪方程式）
$$ i_r = i - \pi^e $$

> 变量说明：
> - $i_r$ = 实际利率（Real Interest Rate）
> - $i$ = 名义利率（Nominal Interest Rate）
> - $\pi^e$ = 预期通胀率

精确形式：$1 + i = (1 + i_r)(1 + \pi^e)$，但 $\pi^e$ 较小时可近似为 $i_r = i - \pi^e$。

### 关键洞察

| 情景 | 含义 |
|------|------|
| $i=5\%$, $\pi^e=0\%$ | $i_r=5\%$ —— 实际收益5% |
| $i=10\%$, $\pi^e=20\%$ | $i_r=-10\%$ —— 实际亏损！ |
| 实际利率低 | 借款激励强，贷款激励弱 |

### 事前实际利率 vs 事后实际利率

实际利率根据使用的通胀数据不同，分为事前和事后两种：

| 概念 | 英文 | 公式 | 通胀来源 | 使用场景 |
|------|------|------|----------|----------|
| **事前实际利率** | Ex Ante Real Interest Rate | $i_r^{ex\ ante} = i - \pi^e$ | **预期**通胀率 $\pi^e$ | 借款/投资**决策时**——签合同前估算真实成本 |
| **事后实际利率** | Ex Post Real Interest Rate | $i_r^{ex\ post} = i - \pi$ | **实际**通胀率 $\pi$ | 到期**核算时**——回头看实际赚/亏了多少 |

**核心区别**：事前用 $\pi^e$（预期），事后用 $\pi$（实际）。两者的值通常不相等——因为预期通胀和实际通胀很少一分不差。

**费雪方程式本质上是事前概念**：$i_r = i - \pi^e$。经济学家说"实际利率"时，默认指事前实际利率，因为它影响经济决策（借款/投资/储蓄）。事后实际利率则是你真正拿到手的——在合同签订时不可知。

**举例**：
- 银行给你名义利率 5%，你预期通胀 2% → 事前实际利率 = 3%（你觉得借这笔钱划算）
- 一年后实际通胀跑到了 4% → 事后实际利率 = 1%（实际上你赚的比预期少）

> ⚠️ AI备注：课件原文以 Fisher Equation 为主线定义实际利率（基于预期通胀），事前/事后是进一步的细分——同一个公式，换不同的 $\pi$ 而已。

### 税后实际利率
利息收入需缴税，税后实际利率 = $i(1-t) - \pi^e$（$t$ 为所得税率）。

## 📊 图形

![[货币金融学Ch04 实际利率与名义利率走势 Figure1 1953-2020.png]]

> 图形说明：Figure 1 展示 1953-2020 年美国三个月国债的实际利率与名义利率走势。名义利率来自 Federal Reserve Bank of St. Louis FRED database。

## 📖 相关术语（如有）
- [[Money and Interest Rates 货币与利率]]：费雪效应——货币增长→通胀预期↑→名义利率↑
- [[Money and Inflation 货币与通货膨胀]]：通胀预期是费雪方程的关键变量
- [[Present Value 现值]]：折现时应使用实际利率还是名义利率取决于现金流的计价方式

## 🔀 跨课程链接
- **中级微观经济学**：[[跨期选择]]、[[实际变量与名义变量]]
- **财政学**：[[通货膨胀税]]

## ⚖️ 易混点对照（人类填写区域）
- 名义利率 vs 实际利率：费雪方程式 $i_r = i - \pi^e$
- 事前 vs 事后：事前用预期通胀，事后用实际通胀
- GDP 实际/名义 vs 利率实际/名义：同理——名义值 = 实际值 + 价格变化

### 考研真题 📎
- 一年期定存利率 2.50%，CPI 3.80%，实际年利率 = (1+2.5%)/(1+3.80%)-1 = **-1.25%** [浙江工商大学2011研]
- 实际利率和名义利率**都可能为负** [中央财经大学2012研]——日本1990s、美国2008年均出现过负名义利率

## 📝 个人批注（人类专属，AI 严禁写入）
- 考试重点：
- 计算陷阱：
- 个人理解：

> 📌 考点提示：
> 💡 记忆技巧：
> 🔢 典型考题：

## 📄 来源原文
> Real Interest Rate: Interest rate that is adjusted for expected changes in the price level. ir = i - πe (Fisher Equation). Nominal interest rate makes no allowance for inflation. Ex ante real interest rate is adjusted for expected changes; ex post real interest rate is adjusted for actual changes.
