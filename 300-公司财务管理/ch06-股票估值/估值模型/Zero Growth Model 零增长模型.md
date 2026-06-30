---
tags:
  - 公司财务管理
  - ch06-股票估值
  - 模型
courses:
  - 公司财务管理
aliases:
  - Zero Growth Model
  - 零增长模型
  - Constant Dividend Model
created: 2026-06-30
source: Chap6_Stock.pdf 第25-28页
chapter: "第6章 股票估值"
importance: "***"
---

# 零增长模型 (Zero Growth Model)

## 📌 定义
零增长模型假设公司股利**永远保持不变**（$g = 0$），股票价值等于永续年金的现值：**$P_0 = Div / R$**。这常用于优先股估值和"现金牛"型企业的估值。

> 💬 通俗理解：如果一家公司每年固定给你发 $2 股利，不再增长也不会减少，这就像一张永不还本的固定利息债券——用永续年金公式就能定价。

## 🔗 前置知识
- [[Dividend Discount Model 股利折现模型]]
- [[Perpetuity 永续年金]]
- [[Preferred Stock 优先股]]

## 🧠 机制

### 推导

通用 DDM 公式：
$$P_0 = \frac{Div_1}{1+R} + \frac{Div_2}{(1+R)^2} + \frac{Div_3}{(1+R)^3} + \cdots$$

令 $Div_1 = Div_2 = Div_3 = \ldots = Div$（恒常股利），则：

$$P_0 = Div \times \left[\frac{1}{1+R} + \frac{1}{(1+R)^2} + \cdots\right] = \frac{Div}{R}$$

### 公式

$$P_0 = \frac{Div}{R}$$

### 计算实例

> Big Deal Company 每年支付 $2.00 股利且永不增长，市场必要回报率 8.5%。

$$P_0 = \frac{\$2.00}{0.085} = \$23.53$$

> 你愿意支付的最高股价为 $23.53。

## 📐 公式

| 符号 | 含义 |
|------|------|
| $P_0$ | 股票当前价值 |
| $Div$ | 每股永续固定股利 |
| $R$ | 必要回报率 |

## 🏛️ 应用
- **优先股估值**：优先股股利通常固定不变 → 零增长模型
- **成熟"现金牛"企业**：无增长空间、将全部利润分红的企业
- 如果将 EPS 全部作为股利分配（股利支付率 100%），则 $P_0 = EPS / R$

## 📖 相关术语
- [[Dividend Discount Model 股利折现模型]]：通用模型，零增长是其特例
- [[Perpetuity 永续年金]]：$PV = C / r$ 是零增长模型的数学原型
- [[Preferred Stock 优先股]]：零增长模型的典型应用
- [[Constant Growth Model 固定增长模型]]：$g > 0$ 的推广版本

## ⚖️ 易混点对照（人类填写区域）
- 零增长模型 vs 永续年金：

## 📝 个人批注（人类专属，AI 严禁写入）
- 考试重点：
- 计算陷阱：
- 个人理解：

> 📌 考点提示：
> 💡 记忆技巧：
> 🔢 典型考题：

## 📄 来源原文
> Dividends will remain at the same level forever. Since future cash flows are constant, the value of a zero growth stock is the present value of a perpetuity: P = Div / R. Example: Big Deal Company will pay an annual dividend of $2.00 per common share that will never increase or decrease. The market rate of return is 8.5%. P = $2.00 / 8.5% = $23.53.
