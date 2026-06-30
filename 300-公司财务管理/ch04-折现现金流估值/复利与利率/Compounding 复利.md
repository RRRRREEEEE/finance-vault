---
tags:
  - 公司财务管理
  - ch04-折现现金流估值
  - 概念
courses: [公司财务管理]
aliases: [Compounding, 复利, Compound Interest]
created: 2026-06-29
source: "Chap4_Discounted Cash Evaluation.pdf 第19-26页"
chapter: "第4章 Discounted Cash Flow Valuation"
importance: "***"
---

# 复利 (Compounding)

## 📌 定义
复利是将利息再投资产生更多利息的过程——"利滚利"。FV = PV × (1+r)^T 中的指数 T 体现了复利效应：不仅是本金生息，已获得的利息也在后续期间生息。

> 💬 通俗理解：单利是"只算本金的利息"，复利是"连利息一起算利息"。存 10 年，单利 = 本金 × (1+10r)，复利 = 本金 × (1+r)^10——差距随 T 增长呈指数扩大。

## 🔗 前置知识
[[Future Value 终值]]、[[Time Value of Money 货币时间价值]]

## 🧠 机制

### 单利 vs 复利
$1,000 存 5 年，9% 利率：
| | 单利 | 复利 |
|------|------|------|
| 公式 | 1000 × (1+5×0.09) | 1000 × 1.09^5 |
| 终值 | $1,450 | $1,538.62 |
| 利息 | $450 | $538.62 |

差额 $88.62 = 利滚利的部分（interest on interest）。

### 复利频率（Compounding Frequency）
$$ FV = PV \times \left(1 + \frac{r}{m}\right)^{mT} $$

| 频率 | m | $1 按 12% 存 1 年的 FV |
|------|-----|------|
| 年复利 | 1 | $1.1200 |
| 半年复利 | 2 | $1.1236 |
| 季复利 | 4 | $1.1255 |
| 月复利 | 12 | $1.1268 |
| 日复利 | 365 | $1.1275 |

m 越大 → FV 越大 → 实际年利率越高。

## 📖 相关术语
- [[Effective Annual Rate 有效年利率]]：整合复利频率后的真实年利率
- [[Continuous Compounding 连续复利]]：m → ∞ 的极限
- [[Future Value 终值]]：复利是 FV 计算的数学基础

## 📄 来源原文
> Interest on interest — the power of compounding. FV = C₀ × (1 + r)^T.
