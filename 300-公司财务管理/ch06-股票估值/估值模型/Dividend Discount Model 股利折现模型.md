---
tags:
  - 公司财务管理
  - ch06-股票估值
  - 模型
courses:
  - 公司财务管理
aliases:
  - Dividend Discount Model
  - DDM
  - 股利折现模型
  - Generalized Dividend Model
created: 2026-06-30
source: Chap6_Stock.pdf 第22-24页
chapter: "第6章 股票估值"
importance: "*****"
---

# 股利折现模型 (Dividend Discount Model)

## 📌 定义
股利折现模型（DDM）是股票估值的理论基础：**股票的内在价值等于其所有未来预期股利的现值之和**。无论投资者持有一期还是永远持有，两种估值方式等价。

> 💬 通俗理解：如果问"这只股票值多少钱"，最简单的回答是：把它未来每一年能分给你多少钱全部加在一起（当然要折现到今天）。

## 🔗 前置知识
- [[Gordon Growth Model 戈登增长模型]]（货币金融学）：DDM 的最常用简化版本
- [[Stock Valuation 股票估值]]（货币金融学）：一期估值模型的基础
- [[Present Value 现值]]（货币金融学）：折现的核心概念
- [[Net Present Value 净现值]]：项目估值与股票估值的共通逻辑

## 🧠 机制

### 推导：为什么两种估值等价？

**一期持有估值**（买入持有一年再卖出）：

$$P_0 = \frac{Div_1 + P_1}{1 + R}$$

其中 $P_1$ 是下一年卖出时的价格，而 $P_1$ 本身又由下一年股利和再下一年的价格决定：

$$P_1 = \frac{Div_2 + P_2}{1 + R}, \quad P_2 = \frac{Div_3 + P_3}{1 + R}, \ldots$$

**无限代入后**，所有中间价格 $P_t$ 被消去，得到：

$$P_0 = \sum_{t=1}^{\infty} \frac{Div_t}{(1 + R)^t}$$

### 通用股利折现模型

$$P_0 = \frac{Div_1}{1+R} + \frac{Div_2}{(1+R)^2} + \frac{Div_3}{(1+R)^3} + \cdots$$

其中：
- $P_0$ = 股票当前内在价值
- $Div_t$ = 第 $t$ 期预期股利
- $R$ = 股票折现率（必要回报率）

### 推论
> **股票的价值只取决于未来的股利**——卖出价格本身也是未来股利的反映。因此，永远持有一期的估值等价于持有全部未来股利的现值。

### DDM 的三种特殊情形

| 模型 | 股利假设 | 公式 | 对应数学工具 |
|------|----------|------|-------------|
| **零增长模型** | $Div_1 = Div_2 = \ldots = Div$ | $P_0 = Div / R$ | [[Perpetuity 永续年金]] |
| **固定增长模型** | 股利以恒定 $g$ 永续增长 | $P_0 = Div_1 / (R - g)$ | [[Growing Perpetuity 增长永续年金]] |
| **变动增长模型** | 前 $N$ 年以 $g_1$ 增长，之后以 $g_2$ 永续增长 | 分段折现 | 增长年金 + 增长永续年金 |

## 📐 公式

| 符号 | 含义 |
|------|------|
| $P_0$ | 当前股票内在价值 |
| $Div_t$ | 第 $t$ 期预期每股股利 |
| $R$ | 股票必要回报率（折现率） |

## 🏛️ 应用
- DDM 是所有绝对估值法的理论基础
- 巴菲特买入 Coca-Cola（1988）就是基于 DDM 判断其被低估
- 局限性：对未来股利预测高度敏感，零股利公司不适用

## 📖 相关术语
- [[Gordon Growth Model 戈登增长模型]]（货币金融学）：$g$ 恒定的 DDM 特例
- [[Growing Perpetuity 增长永续年金]]：固定增长 DDM 的数学基础
- [[Constant Growth Model 固定增长模型]]：$P_0 = D_1/(R-g)$
- [[Differential Growth Model 变动增长模型]]：两阶段 DDM
- [[Zero Growth Model 零增长模型]]：$P_0 = Div/R$

## ⚖️ 易混点对照（人类填写区域）
- DDM vs DCF：
- 股利 vs 自由现金流：

## 📝 个人批注（人类专属，AI 严禁写入）
- 考试重点：
- 计算陷阱：
- 个人理解：

> 📌 考点提示：
> 💡 记忆技巧：
> 🔢 典型考题：

## 📄 来源原文
> Value of stocks: Suppose one will buy the stock and hold it for one year. PV of dividend (next term) + stock price (next term), or PV of all future dividends: General dividend model.
> $$P_0 = \frac{Div_1}{1+R} + \frac{Div_2}{(1+R)^2} + \frac{Div_3}{(1+R)^3} + \cdots = \sum_{t=1}^{\infty} \frac{Div_t}{(1+R)^t}$$
> ($Div_t$ 为第 $t$ 期的股利，$R$ 为股票折现率)
