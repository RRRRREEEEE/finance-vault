---
tags:
  - 公司财务管理
  - ch06-股票估值
  - 模型
courses:
  - 公司财务管理
aliases:
  - Constant Growth Model
  - 固定增长模型
  - Gordon Growth Model Application
  - Dividend Growth Model
created: 2026-06-30
source: Chap6_Stock.pdf 第29-31页
chapter: "第6章 股票估值"
importance: "****"
---

# 固定增长模型 (Constant Growth Model)

## 📌 定义
固定增长模型假设公司股利以**恒定增长率 $g$** 永续增长：$P_0 = Div_1 / (R - g)$。这是戈登增长模型在估值实践中的直接应用，也是 DDM 最常用的版本。

> 💬 通俗理解：如果公司每年不仅分股利，而且分得越来越多（增速 $g$），那么股票的"真值" = 下年股利 ÷ (你的期望回报率 − 它的增长速度)。$g$ 越接近 $R$，股票越值钱——但永远不能 $g \ge R$。

## 🔗 前置知识
- [[Dividend Discount Model 股利折现模型]]
- [[Gordon Growth Model 戈登增长模型]]（货币金融学）
- [[Growing Perpetuity 增长永续年金]]
- [[Zero Growth Model 零增长模型]]

## 🧠 机制

### 推导

假设股利以 $g$ 恒定增长：
$$Div_1 = Div_0(1+g), \quad Div_2 = Div_1(1+g) = Div_0(1+g)^2, \quad \ldots$$

代入通用 DDM：
$$P_0 = \frac{Div_0(1+g)}{1+R} + \frac{Div_0(1+g)^2}{(1+R)^2} + \cdots = \frac{Div_1}{R - g}$$

### 公式

$$P_0 = \frac{Div_1}{R - g} = \frac{Div_0(1+g)}{R - g}$$

> ⚠️ **必要条件**：$R > g$（否则公式无意义）。

### 计算实例

> Big D, Inc. 刚刚支付了 $0.50 股利，预计每年增长 2%，市场要求回报率 15%。

- $Div_0 = \$0.50$（已支付）
- $Div_1 = \$0.50 \times (1 + 2\%) = \$0.51$
- $P_0 = \dfrac{\$0.51}{0.15 - 0.02} = \dfrac{\$0.51}{0.13} = \$3.92$

### 与零增长模型的对比

| 模型 | 公式 | 股利 | 适用 |
|------|------|------|------|
| 零增长 | $P_0 = Div/R$ | 恒定不变 | 优先股、现金牛 |
| 固定增长 | $P_0 = Div_1/(R-g)$ | 恒定增速 | 稳定增长企业 |

### $R$ 的分拆

将公式变形：$R = Div_1/P_0 + g$

| 组成部分 | 含义 |
|----------|------|
| $Div_1/P_0$ | 预期**股利收益率** (Dividend Yield) |
| $g$ | **资本利得收益率** (Capital Gains Yield) |

> 总回报 $R$ = 股利收益 + 资本利得（股价上涨）。

## 📐 公式

| 符号 | 含义 |
|------|------|
| $P_0$ | 股票当前内在价值 |
| $Div_0$ | 当期已支付股利 |
| $Div_1 = Div_0(1+g)$ | 下一期预期股利 |
| $g$ | 股利永续增长率 ($g < R$) |
| $R$ | 必要回报率（折现率） |

## 🏛️ 应用
- **成熟稳定企业估值**：增长率可预测的大盘蓝筹股
- 巴菲特 1988 年买入 Coca-Cola 的逻辑：估算其长期稳定 $g$，用 $P_0 = Div_1/(R-g)$ 定价
- $g$ 的微小变化会显著影响 $P_0$ —— **高增长预期本身就推高股价**

## 📖 相关术语
- [[Gordon Growth Model 戈登增长模型]]（货币金融学）：GGM = 固定增长模型（同一模型，货金侧重宏观应用，公司金融侧重估值计算）
- [[Growing Perpetuity 增长永续年金]]：数学等价物
- [[Differential Growth Model 变动增长模型]]：允许 $g$ 分阶段变化

## ⚖️ 易混点对照（人类填写区域）
- $Div_0$ vs $Div_1$（已付 vs 预期）：
- $g$ vs $R$ 的经济直觉：

## 📝 个人批注（人类专属，AI 严禁写入）
- 考试重点：
- 计算陷阱：
- 个人理解：

> 📌 考点提示：
> 💡 记忆技巧：
> 🔢 典型考题：

## 📄 来源原文
> Since future cash flows grow at a constant rate forever, the value of a constant growth stock is the present value of a growing perpetuity: $P_0 = Div_1 / (R - g)$. Note: Div1 is the expected dividend in next term, other than the current paid dividend. Example: Big D, Inc., just paid a dividend of $.50. Its dividend is expected to increase by 2% per year. Market requires return 15%. $P_0 = $0.51 / (15% - 2%) = $3.92$.
