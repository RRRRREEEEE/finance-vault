---
tags:
  - 公司财务管理
  - ch06-股票估值
  - 模型
courses:
  - 公司财务管理
aliases:
  - Differential Growth Model
  - 变动增长模型
  - Two-Stage DDM
  - 两阶段股利折现模型
created: 2026-06-30
source: Chap6_Stock.pdf 第32-39页
chapter: "第6章 股票估值"
importance: "****"
---

# 变动增长模型 (Differential Growth Model)

## 📌 定义
变动增长模型（两阶段 DDM）是股利折现模型中**最贴近现实**的版本：假设股利在前 $T$ 年以较高增长率 $g_1$ 增长，$T$ 年后切换为永续增长率 $g_2$。股票价值 = 前 $T$ 年增长年金现值 + $T+1$ 年起增长永续年金的折现值。

> 💬 通俗理解：现实中很多公司的增长不是一成不变的——前期高增长（抢占市场），后期稳定（成熟期）。两阶段模型就是把这两段分别算好，再折现到今天。

## 🔗 前置知识
- [[Dividend Discount Model 股利折现模型]]
- [[Constant Growth Model 固定增长模型]]
- [[Growing Annuity 增长年金]]
- [[Growing Perpetuity 增长永续年金]]

## 🧠 机制

### 推导

**阶段一**（前 $T$ 年）：股利以 $g_1$ 增长
$$Div_1 = Div_0 (1+g_1), \quad Div_2 = Div_0 (1+g_1)^2, \quad \ldots, \quad Div_T = Div_0 (1+g_1)^T$$

**阶段二**（$T$ 年以后）：股利以 $g_2$ 永续增长
$$Div_{T+1} = Div_T (1+g_2) = Div_0 (1+g_1)^T (1+g_2)$$

### 公式：两段相加

$$P_0 = \underbrace{\frac{Div_1}{R - g_1}\left[1 - \left(\frac{1+g_1}{1+R}\right)^T\right]}_{\text{前 T 年：增长年金现值}} + \underbrace{\frac{\frac{Div_{T+1}}{R - g_2}}{(1+R)^T}}_{\text{T+1 年起：增长永续年金折现}}$$

即：
$$P_0 = \frac{Div_1}{R - g_1}\left[1 - \left(\frac{1+g_1}{1+R}\right)^T\right] + \frac{Div_1(1+g_1)^{T-1}(1+g_2)}{(R-g_2)(1+R)^T}$$

### 完整计算实例

> 某股票刚刚支付了 $2.00 股利，预计前 3 年以 8% 增长，之后以 4% 永续增长。折现率 12%。求股价。

**步骤一**：计算各期股利
- $Div_1 = \$2.00 \times (1.08) = \$2.16$
- $Div_2 = \$2.00 \times (1.08)^2 = \$2.33$
- $Div_3 = \$2.00 \times (1.08)^3 = \$2.52$
- $Div_4 = \$2.52 \times (1.04) = \$2.62$

**步骤二**：计算阶段一（3 年增长年金）
$$P_A = \frac{\$2.16}{0.12 - 0.08}\left[1 - \left(\frac{1.08}{1.12}\right)^3\right] = \$5.58$$

**步骤三**：计算阶段二（$T=3$ 年末增长永续年金，再折现）
$$P_B = \frac{\$2.62}{0.12 - 0.04} \div (1.12)^3 = \$32.75 \times 0.7118 = \$23.31$$

**步骤四**：加总
$$P_0 = \$5.58 + \$23.31 = \$28.89$$

## 📊 图形

![[ch06 Stock Valuation Overview.png]]

> 图形说明：变动增长模型的现金流时间线——前 $T$ 年按 $g_1$ 增长，$T$ 年后切换为 $g_2$ 永续增长。

## 📐 公式

| 符号 | 含义 |
|------|------|
| $P_0$ | 股票当前内在价值 |
| $Div_0$ | 当期已支付股利 |
| $g_1$ | 阶段一增长率（通常更高） |
| $g_2$ | 阶段二永续增长率（通常更低） |
| $T$ | 阶段一持续年数 |
| $R$ | 必要回报率 |

## 🏛️ 应用
- **成长型企业估值**：初创期高增长 + 成熟期稳定增长
- **行业周期调整**：企业经历了快速增长后将回归行业平均增长率
- 分析师可以分阶段预测不同时期的股利增长率，比单阶段更灵活

## 📖 相关术语
- [[Constant Growth Model 固定增长模型]]：$g_1 = g_2$ 的特例
- [[Zero Growth Model 零增长模型]]：$g_1 = g_2 = 0$ 的特例
- [[NPVGO 增长机会净现值]]：解释为什么 $g_1 > g_2$

## ⚖️ 易混点对照（人类填写区域）
- 两阶段 vs 三阶段 DDM：
- $g_1$ 和 $g_2$ 选择依据：

## 📝 个人批注（人类专属，AI 严禁写入）
- 考试重点：
- 计算陷阱：
- 个人理解：

> 📌 考点提示：
> 💡 记忆技巧：
> 🔢 典型考题：

## 📄 来源原文
> Dividends will grow at rate g1 for N years and then grow at rate g2 thereafter. Total PV = a T-year growing annuity at rate g1 plus the discounted value of a growing perpetuity at rate g2 that starts in year T+1. Example: A common stock just paid a dividend of $2. The dividend is expected to grow at 8% for 3 years, and then will grow at 4% in perpetuity. The discount rate is 12%. P = $5.58 + $23.31 = $28.89.
