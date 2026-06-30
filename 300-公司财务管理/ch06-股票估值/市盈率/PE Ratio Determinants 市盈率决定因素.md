---
tags:
  - 公司财务管理
  - ch06-股票估值
  - 模型
courses:
  - 公司财务管理
aliases:
  - P/E Ratio Determinants
  - 市盈率决定因素
  - P/E Decomposition
created: 2026-06-30
source: Chap6_Stock.pdf 第63-76页
chapter: "第6章 股票估值"
importance: "****"
---

# 市盈率决定因素 (P/E Ratio Determinants)

## 📌 定义
市盈率（P/E）并非一个简单的"贵不贵"指标——它可以被 DL 解为三大驱动因素的函数：**留存收益率 $b$**、**净资产收益率 $ROE$** 和**必要回报率 $R$**。$P/E = (1-b)(1+b \times ROE)/(R - b \times ROE)$。

> 💬 通俗理解：P/E 高低不是随意定价，而是由"留多少利润再投资"、"利润能赚多少回报"和"投资者要求多高回报"这三个变量共同决定的。高 P/E 不一定是泡沫，可能是公司 ROE 确实远超市场要求回报率。

## 🔗 前置知识
- [[PE Ratio 市盈率]]：基本定义 $P/E = Price\ per\ Share / EPS$
- [[Growth Rate Estimation 增长率估计]]：$g = b \times ROE$
- [[Constant Growth Model 固定增长模型]]
- [[NPVGO 增长机会净现值]]
- [[ROA and ROE 资产回报率与股本回报率]]（货币金融学）

## 🧠 机制

### P/E 的 DGM 推导

从固定增长模型出发：
$$P_0 = \frac{D_0(1+g)}{R-g}$$

已知 $D_0 = EPS_0 \times (1-b)$（$(1-b)$ 为股利支付率）且 $g = b \times ROE$：

$$P_0 = \frac{EPS_0 \times (1-b) \times (1+g)}{R-g}$$

除以 $EPS_0$：
$$\frac{P}{E} = \frac{(1-b)(1+g)}{R-g} = \frac{(1-b)(1 + b \times ROE)}{R - b \times ROE}$$

### P/E 与 $b$（留存率）的关系

| 条件 | $b$↑（多留存少分红）对 P/E 的影响 |
|------|----------------------------------|
| **ROE > R** | P/E **大幅上升**（留存创造价值） |
| **ROE = R** | P/E **缓慢上升**（留存和分红无差异） |
| **ROE < R** | P/E **下降**（留存破坏价值，应全部分红） |

> 核心结论：**ROE 越高 → P/E 越高**。增长本身不自动创造价值，只有 ROE 超过 $R$ 的增长才创造价值。

### P/E 与 $R$（必要回报率）的关系

| 条件 | $R$ 变化对 P/E 的影响 |
|------|----------------------|
| 一般规律 | $R$↓ → P/E↑（分母变小，未来现金流现值变大） |
| 市场利率下行时 | 股市整体 P/E 趋于上升 |

> 核心结论：**市场 $R$ 越低 → P/E 越高**。美联储降息周期通常推高股市 P/E。

### P/E 的 NPVGO 分解

$$P/E = \frac{P_0}{EPS} = \frac{EPS/R + NPVGO}{EPS} = \frac{1}{R} + \frac{NPVGO}{EPS}$$

- 当 NPVGO = 0：$P/E = 1/R$（底线 P/E）
- 当 NPVGO > 0：$P/E > 1/R$（增长溢价）
- 当 NPVGO 很大：P/E 可以远超 $1/R$

### 影响 P/E 的其他因素

| 因素 | 影响方向 | 机制 |
|------|----------|------|
| **增长机会** (NPVGO) | ↑ | NPVGO 越大 → P/E 越高 |
| **会计政策** | — | 保守会计（LIFO 在通胀下）→ P/E 偏高；激进会计（FIFO）→ P/E 偏低 |
| **风险** (β) | ↓ | 风险越高 → $R$ 越高 → P/E 越低 |

## 🏛️ 应用
- **行业对比**：同一行业中，ROE 高的公司 P/E 更高是合理的
- **利率环境判断**：低利率 → 高 P/E 是合理的（$1/R$ 变大）
- **不要孤立看 P/E**：P/E 高不一定贵——可能 NPVGO 确实大；P/E 低不一定便宜——可能 ROE < R
- LIFO vs FIFO：通货膨胀期间，使用 LIFO 的公司 EPS 偏低 → P/E 被夸大，需调整后比较

## 📖 相关术语
- [[PE Ratio 市盈率]]：基本定义和公式
- [[NPVGO 增长机会净现值]]：解释 P/E 为何高于 $1/R$
- [[Growth Rate Estimation 增长率估计]]：$g = b \times ROE$ 是 P/E 分解的枢纽
- [[ROA and ROE 资产回报率与股本回报率]]（货币金融学）：ROE 驱动 P/E 的机制
- [[DuPont Identity 杜邦恒等式]]：ROE → 三因子 → P/E 五因子分解

## ⚖️ 易混点对照（人类填写区域）
- P/E 高 = 贵？还是 P/E 高 = 增长好？
- LIFO vs FIFO 对 P/E 的影响方向：

## 📝 个人批注（人类专属，AI 严禁写入）
- 考试重点：
- 计算陷阱：
- 个人理解：

> 📌 考点提示：
> 💡 记忆技巧：
> 🔢 典型考题：

## 📄 来源原文
> In Dividend Growth Model: Stock price = EPS0 × (1-b) × (1+g) / (R-g). P/E ratio = (1-b)(1+g)/(R-g) = (1-b)(1+b×ROE)/(R-b×ROE). If ROE > R: the more the firm holds Retained earnings, the bigger the firm's P/E ratio. If ROE = R: P/E ratio will increase but slowly. If ROE < R: the more the firm holds Retained earnings, the smaller the firm's P/E ratio. Growth opportunities: firms with growth opportunities → greater P/E ratios. P/E ratio = 1/R + NPVGO/EPS > 1/R (when NPVGO > 0). Accounting policies: firms with conservative accounting policies → higher P/E ratios.
