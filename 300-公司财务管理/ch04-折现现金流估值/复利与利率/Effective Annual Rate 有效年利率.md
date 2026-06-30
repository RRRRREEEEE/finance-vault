---
tags:
  - 公司财务管理
  - ch04-折现现金流估值
  - 公式
courses: [公司财务管理]
aliases: [Effective Annual Rate, 有效年利率, EAR]
created: 2026-06-29
source: "Chap4_Discounted Cash Evaluation.pdf 第38-48页"
chapter: "第4章 Discounted Cash Flow Valuation"
importance: "****"
---

# 有效年利率 (Effective Annual Rate)

## 📌 定义
有效年利率（EAR）是考虑了复利频率后的**实际年利率**：**EAR = (1 + APR/m)^m − 1**。12% 年利率半年复利 ≠ 12% 实际收益——EAR 才是真实的年回报率。

> 💬 通俗理解：银行说"年利率 12% 半年计息"，实际一年后 $1 变成了 (1+0.06)^2 = $1.1236。EAR = 12.36%——这才是你真正赚到的。银行报的是 APR（名义），EAR 才是实打实的。

## 🔗 前置知识
[[Compounding 复利]]

## 📐 公式与计算

$$ EAR = \left(1 + \frac{APR}{m}\right)^m - 1 $$

$$ EAR = \left(1 + \frac{0.18}{12}\right)^{12} - 1 = 19.56\% $$

> APR = 18% 月复利 → EAR = 19.56%。借款人实际支付的利率比名义的 18% 高了 1.56%。

### 验证
按 EAR 年复利 = 按 APR 半年复利：
$$ 1 \times (1 + EAR) = 1 \times \left(1 + \frac{APR}{m}\right)^m $$
$$ 1.1236 = (1.06)^2 = 1.1236 \checkmark $$

## 🧠 机制
- 复利频率越高 → EAR 越大（但收敛到 e^APR − 1）
- **APR 不能直接用于比较**——12% 月复利 vs 12.5% 年复利，哪个更贵？算出 EAR 才能比
- 中国监管要求披露 APR，但有些金融产品实际 EAR 远高于 APR

## 📖 相关术语
- [[APR 年百分比率]]：APR 是名义利率，EAR 是实际利率
- [[Continuous Compounding 连续复利]]：EAR 的极限 m → ∞
- [[Compounding 复利]]：复利频率是 EAR 的关键变量

## 📄 来源原文
> EAR = (1 + APR/m)^m − 1. The sum of principal and interest of 1 yuan invested over one year at the actual annual interest rate EAR is equal to 1*(1+APR/m)^m.
