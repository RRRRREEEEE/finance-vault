---
tags:
  - 货币金融学
  - ch04-利率度量
  - 公式
courses:
  - 货币金融学
aliases:
  - Yield to Maturity
  - 到期收益率
  - YTM
created: 2026-06-06
source: Ch04-2026-T(3).pptx 第14-23页
chapter: "第4章 利率度量"
importance: "*****"
---

# 到期收益率 (Yield to Maturity)

## 📌 定义
到期收益率（YTM）是最重要的利率指标，它指的是使债务工具未来现金流入的现值等于其当前价值的利率水平。

> 💬 通俗理解：YTM 就是"如果你把债券持有到期，平均**每年**能赚百分之几"——它是衡量利率最准确的方式。
>
> ⚡ **与 [[Current Yield 当期收益率]] 的区别**：当期收益率只看当年利息（$C/P$），YTM 把未来所有利息 + 本金偿还全部折现算进来——YTM 是全景，当期收益率是快照。

## 🔗 前置知识
- [[Present Value 现值]]
- [[Bond 债券]]

## 🧠 机制

### 四种信贷工具的 YTM

**1. [[Simple Loan 普通贷款|简式贷款（Simple Loan）]]**
$$ PV = \frac{FV}{(1 + i)^n} $$
本金 $100，利率 10%，3年 → YTM = 10%

**2. [[Fixed-Payment Loan 固定支付贷款|定期定额清偿贷款（Fixed-Payment Loan）]]**
$$ LV = \frac{FP}{1+i} + \frac{FP}{(1+i)^2} + ... + \frac{FP}{(1+i)^n} $$
> $LV$ = 贷款金额，$FP$ = 每期固定还款额

**3. 息票债券（Coupon Bond）**
$$ P = \frac{C}{1+i} + \frac{C}{(1+i)^2} + ... + \frac{C+F}{(1+i)^n} $$
> $P$ = 债券价格，$C$ = 年息票，$F$ = 面值

**4. 贴现债券 / 零息债券（Discount Bond）**
$$ i = \frac{F - P}{P} $$
$P=900$，$F=1000$，1年 → $i = 11.1\%$

**统一公债 / 永续债券（Consol）**：
$$ i = \frac{C}{P_c} $$

### YTM 与债券价格的关系

| 条件 | YTM 关系 |
|------|----------|
| 债券价格 = 面值 | YTM = 票面利率 |
| 债券价格 < 面值 | YTM > 票面利率 |
| 债券价格 > 面值 | YTM < 票面利率 |

**YTM 与债券价格负相关**。

## 📖 相关术语（如有）
- [[Present Value 现值]]：YTM 是使 PV = 价格的折现率
- [[Bond 债券]]：息票债券和贴现债券的 YTM 计算不同
- [[Rate of Return 回报率]]：YTM 是事前概念，回报率是事后概念

## 🔀 跨课程链接
- **公司财务管理**：[[内部报酬率]]、[[债券估值]]

### 考研真题 📎
- 若到期收益率**高于**票面利率，则债券**折价**出售 [中国科学技术大学2016研]
- 售价98元低于面值100元 → 折价发行 → YTM **大于**票面利率 [清华大学2015研]
- 永久债券理论价格 P = C/rm = 100×10%/8% = **125元** [中央财经大学2011研]

## ⚖️ 易混点对照（人类填写区域）
- YTM vs 票面利率：YTM 是实际收益率（考虑价格偏离面值），票面利率只是约定利息率
- YTM vs 当期收益率：当期收益率只看当年利息，YTM 考虑全部未来现金流

## 📝 个人批注（人类专属，AI 严禁写入）
- 考试重点：
- 计算陷阱：
- 个人理解：

> 📌 考点提示：
> 💡 记忆技巧：
> 🔢 典型考题：

## 📄 来源原文
> Yield to maturity: the interest rate that equates the present value of cash flow payments received from a debt instrument with its value today. When the coupon bond is priced at its face value, the yield to maturity equals the coupon rate. The price of a coupon bond and the yield to maturity are negatively related.
