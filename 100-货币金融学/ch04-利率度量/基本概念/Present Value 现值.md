---
tags:
  - 货币金融学
  - ch04-利率度量
  - 公式
courses:
  - 货币金融学
aliases:
  - Present Value
  - 现值
  - PV
  - Future Value
  - 未来值
  - FV
  - Discounting
  - 折现
created: 2026-06-06
source: Ch04-2026-T(3).pptx 第6-11页
chapter: "第4章 利率度量"
importance: "*****"
---

# 现值 (Present Value)

## 📌 定义
现值是未来现金流按利率折现后的当前价值。一年后收到的一美元不如今天的一美元值钱——因为今天的一美元可以赚取利息。

> 💬 通俗理解：今天给你100块 vs 一年后给你100块——你肯定选今天，因为今天的钱存银行能生利息。现值就是算"未来的钱今天值多少"。

## 🔗 前置知识
- [[Money and Interest Rates 货币与利率]]

## 🧠 机制

### 未来值（Future Value）
$$ FV = PV \times (1 + i)^n $$

### 现值（Present Value）
$$ PV = \frac{CF}{(1 + i)^n} $$

### 多期现金流的现值
$$ PV = \sum_{t=1}^{n} \frac{CF_t}{(1 + i)^t} $$

> 变量说明：
> - $PV$ = 现值
> - $FV$ = 未来值
> - $CF_t$ = 第 $t$ 期的现金流
> - $i$ = 利率（折现率）
> - $n$ = 期数

**核心原则**：不同时点的现金流不能直接比较——必须折现到同一时点。

### 单利 vs 复利

| 方式 | 公式 | 特点 |
|------|------|------|
| 单利（Simple Interest） | $FV = PV(1 + n \cdot i)$ | 利息不计息 |
| 复利（Compound Interest） | $FV = PV(1 + i)^n$ | 利滚利，资金增长更快 |

> 10年每年复利回报使资金翻倍 → 需要 $i \approx 7.2\%$（72法则）

### 案例：彩票真的值2000万吗？

纽约州彩票头奖 $2000 万 = 每年 $100 万 × 20 年。按利率折现后，实际价值远低于 $2000 万。

## 📖 相关术语（如有）
- [[Yield to Maturity 到期收益率]]：使现金流入现值等于当前价格的利率
- [[Rate of Return 回报率]]：基于现值的实际收益计算

## 🔀 跨课程链接
- **公司财务管理**：[[净现值]]、[[内部报酬率]]、[[贴现现金流]]

## ⚖️ 易混点对照（人类填写区域）
- PV vs NPV：PV 是现金流入现值，NPV = PV - 初始投资

## 📝 个人批注（人类专属，AI 严禁写入）
- 考试重点：
- 计算陷阱：
- 个人理解：

> 📌 考点提示：
> 💡 记忆技巧：
> 🔢 典型考题：

## 📄 来源原文
> Present value: a dollar paid to you one year from now is less valuable than a dollar paid to you today. A dollar deposited today can earn interest and become $1 x (1+i) one year from today.
