---
tags:
  - 公司财务管理
  - ch06-股票估值
  - 模型
courses:
  - 公司财务管理
aliases:
  - NPVGO
  - 增长机会净现值
  - Growth Opportunities
  - Net Present Value of Growth Opportunities
created: 2026-06-30
source: Chap6_Stock.pdf 第57-61页
chapter: "第6章 股票估值"
importance: "*****"
---

# 增长机会净现值 (NPVGO)

## 📌 定义
NPVGO（Net Present Value of Growth Opportunities）将股票价值拆解为两部分：**现有资产的价值**（假设全部利润分红的零增长部分）+ **未来增长机会的净现值**。公式：$P_0 = EPS/R + NPVGO$。

> 💬 通俗理解：股票值多少钱 = "吃老本"的价值 + "开创新天地"的价值。如果公司发现了好项目能赚超额回报，NPVGO > 0，股价就比"吃老本"的公司高。

## 🔗 前置知识
- [[Net Present Value 净现值]]：NPVGO 本质是未来所有正 NPV 项目的现值之和
- [[Dividend Discount Model 股利折现模型]]
- [[Zero Growth Model 零增长模型]]
- [[Constant Growth Model 固定增长模型]]

## 🧠 机制

### 增长的两个必要条件

公司要实现增长，必须同时满足：
1. **不把全部利润分光**：留存收益（$b > 0$）以提供增长资金
2. **投资项目有正 NPV**：NPVGO > 0，否则留存不如分给股东

> 如果公司留存了利润但投资于 NPV < 0 的项目 → 留存越多，股价越低！

### 股价的两种拆解

$$P_0 = \underbrace{\frac{EPS}{R}}_{\text{零增长部分}} + \underbrace{NPVGO}_{\text{增长机会净现值}}$$

| 部分 | 含义 | 条件 |
|------|------|------|
| $EPS/R$ | 如果公司将全部利润分红（$b=0, g=0$），股价就是这个永续年金的现值 | 底线价值 |
| $NPVGO$ | 留存利润再投资于正 NPV 项目带来的**额外**价值 | 可以 >0、=0 或 <0 |

### NPVGO 的含义

| NPVGO 状态 | 含义 | 股价变化 |
|------------|------|----------|
| **NPVGO > 0** | 公司发现了正 NPV 项目 | 股价高于 $EPS/R$ → 留存创造价值 |
| **NPVGO = 0** | 再投资项目仅赚回资本成本 | 留存和分红无差异 |
| **NPVGO < 0** | 再投资项目亏钱（NPV < 0） | 股价低于 $EPS/R$ → 利润应该全部还给股东 |

### 与固定增长模型的关系

固定增长模型 $P_0 = Div_1/(R-g)$ 可以通过 NPVGO 重写：

$$P_0 = \frac{EPS_1}{R} + NPVGO$$

当 NPVGO > 0 时，$P_0 > EPS_1/R$，股价有"增长溢价"。

## 📐 公式

| 符号 | 含义 |
|------|------|
| $P_0$ | 当前股价 |
| $EPS$ | 每股收益 |
| $R$ | 必要回报率 |
| $EPS/R$ | 零增长价值（"吃老本"） |
| $NPVGO$ | 增长机会净现值 |

## 🏛️ 应用
- **解释高 P/E**：P/E 高并非"泡沫"，而是市场预期 NPVGO 大
- **管理层决策指导**：只有 NPVGO > 0 的留存才有意义，否则应当分红或回购
- **价值投资**：分析股价中有多少来自"吃老本"、多少来自"增长预期"

## 📖 相关术语
- [[Net Present Value 净现值]]：NPVGO = 未来所有正 NPV 项目的总现值
- [[PE Ratio 市盈率]]：$P/E = 1/R + NPVGO/EPS$，当 NPVGO > 0 时 $P/E > 1/R$
- [[Constant Growth Model 固定增长模型]]：NPVGO 隐藏在 $g$ 中
- [[No Dividend Firms 零股利公司]]：零股利公司的全部价值来源

## ⚖️ 易混点对照（人类填写区域）
- NPVGO vs NPV：
- $EPS/R$ vs 账面价值：

## 📝 个人批注（人类专属，AI 严禁写入）
- 考试重点：
- 计算陷阱：
- 个人理解：

> 📌 考点提示：
> 💡 记忆技巧：
> 🔢 典型考题：

## 📄 来源原文
> Growth opportunities: the opportunities to invest in projects with positive NPV. 2 conditions for a company to grow: ① Not paying out all earnings as dividends, otherwise no retained earnings for funding growth. ② Investing in projects with positive NPVGO. If NPVGO > 0, stock price will increase, company value will increase. If NPVGO < 0, stock price will decrease. Maximum stock price: The value of a firm that pays out 100% earnings as dividends (when Div = EPS, and then g = 0), Stock price P0 = Div/R = EPS/R, plus NPV of the Growth Opportunities per share (NPVGO). $P_0 = EPS/R + NPVGO$.
