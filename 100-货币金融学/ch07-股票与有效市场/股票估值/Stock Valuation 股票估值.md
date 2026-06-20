---
tags:
  - 货币金融学
  - ch07-股票与有效市场
  - 模型
courses:
  - 货币金融学
aliases:
  - Stock Valuation
  - 股票估值
  - Gordon Growth Model
  - 戈登增长模型
  - Dividend Discount Model
created: 2026-06-06
source: Ch07-2026-T(1).pptx 第4-22页
chapter: Chapter 7 Stock Market, Rational Expectations, EMH
importance: "*****"
---

# 股票估值 (Stock Valuation)

## 📌 定义
股票估值通过将未来预期现金流（股利 + 卖出价）折现来确定股票当前的内在价值。Gordon 增长模型是最常用的简化形式。

> 💬 通俗理解：股票值多少钱 = 未来所有股利的现值总和。如果公司增长快（$g$ 大），股票就更值钱。

## 🔗 前置知识
- [[Common Stock 普通股]]
- [[Present Value 现值]]
- [[Yield to Maturity 到期收益率]]

## 🧠 机制

### 一期估值模型
$$ P_0 = \frac{Div_1 + P_1}{1 + k_e} $$

### 广义股利估值模型
$$ P_0 = \sum_{t=1}^{\infty} \frac{Div_t}{(1 + k_e)^t} $$

### Gordon 增长模型（戈登增长模型）
假设股利以恒定速率 $g$ 永续增长：
$$ P_0 = \frac{Div_1}{k_e - g} $$

> 变量说明：
> - $P_0$ = 当前股价
> - $Div_1$ = 下一期预期股利
> - $k_e$ = 必要回报率（Required Rate of Return）
> - $g$ = 股利增长率（需 $k_e > g$）

### 其他估值方法

| 方法 | 公式/概念 |
|------|-----------|
| P/E（市盈率） | 股价/每股收益 |
| P/CF | 股价/每股现金流 |
| P/BV | 股价/每股账面价值 |
| P/S | 股价/每股销售收入 |

### 应用：货币政策与股票价格

美联储降息 → 两条路径推高股价：
1. $k_e$↓（债券替代品收益下降）→ 分母↓ → $P_0$↑
2. $g$↑（低利率刺激经济）→ 分母进一步↓ → $P_0$↑

**案例**：次贷危机（2007-2008）→ $g$↓ + $k_e$↑ → 50年最严重熊市；新冠（2020.3）→ DJIA 从 29,551 跌至 18,561（-37%）。

## 📖 相关术语（如有）
- [[Common Stock 普通股]]：股票估值是确定普通股内在价值的方法
- [[Present Value 现值]]：所有估值模型的基础
- [[Efficient Market Hypothesis 有效市场假说]]：市场有效→股价=内在价值

## 🔀 跨课程链接
- **公司财务管理**：[[股利折现模型]]、[[权益估值]]、[[P/E比率]]

## 📄 来源原文
> Gordon Growth Model: P0 = Div1/(ke - g). Monetary policy affects stock prices through ke (lower rates → lower required return → higher stock prices) and g (lower rates stimulate economy → higher dividend growth).
