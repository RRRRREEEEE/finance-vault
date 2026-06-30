---
tags:
  - 公司财务管理
  - ch06-股票估值
  - 模型
courses:
  - 公司财务管理
aliases:
  - Required Return Estimation
  - 必要收益率估计
  - Dividend Yield
  - Capital Gains Yield
created: 2026-06-30
source: Chap6_Stock.pdf 第46-49页
chapter: "第6章 股票估值"
importance: "***"
---

# 必要收益率估计 (Required Return Estimation)

## 📌 定义
在固定增长模型中，必要回报率 $R$ 可以从市场价格反推：**$R = Div_1 / P_0 + g$**，即预期股利收益率 + 资本利得收益率。

> 💬 通俗理解：你持有一只股票的预期回报来自两部分——每年分红的"利息"（股利收益率）+ 股价上涨的"差价"（资本利得）。两者相加就是你要求的总回报率。

## 🔗 前置知识
- [[Constant Growth Model 固定增长模型]]
- [[Growth Rate Estimation 增长率估计]]
- [[Discount Rate 折现率]]

## 🧠 机制

### 推导

从固定增长模型反推 $R$：
$$P_0 = \frac{Div_1}{R - g}$$

$$R - g = \frac{Div_1}{P_0}$$

$$R = \frac{Div_1}{P_0} + g$$

### 两个组成部分

| 部分 | 公式 | 含义 |
|------|------|------|
| **股利收益率** (Dividend Yield) | $Div_1 / P_0$ | 下一年股利占当前股价的比例，类似"利息" |
| **资本利得收益率** (Capital Gains Yield) | $g$ | 股价年增长率——在固定增长模型中等同于股利增长率 |
| **总回报** | $R = Div_1/P_0 + g$ | 两部分的加总 |

### 计算实例

> Solar Corp. 上一期股利 $0.65/股，股利增速 4%，当前股价 $11.25。求市场隐含的 $R$。

- $Div_1 = Div_0 \times (1+g) = \$0.65 \times 1.04 = \$0.676$
- 股利收益率 = $\$0.676 / \$11.25 = 6\%$
- 资本利得收益率 = $g = 4\%$
- $R = 6\% + 4\% = 10\%$

> 市场对 Solar Corp. 要求的回报率为 10%。

### 参数估计的两大问题

| 问题 | 说明 | 解决方法 |
|------|------|----------|
| $R$ 的估计不稳定 | 单一公司的 $R$ 可能波动很大 | 使用**行业平均** $R$ 替代单个公司 |
| $g \ge R$ 怎么办？ | 分母为负或零，公式无意义 | $g > R$ 只能在短期内维持，不能用于永续模型——应检查 $g$ 的估计是否合理 |

## 🏛️ 应用
- **从股价反推市场预期**：已知 $P_0$ 和 $g$ → 算出市场要求的 $R$
- **CAPM 交叉验证**：用 $R = D_1/P_0 + g$ 估算的 $R$ 可与 CAPM 计算的 $R$ 对比
- 股利收益率高的公司通常处于成熟期（低 $g$）

## 📖 相关术语
- [[Constant Growth Model 固定增长模型]]：$R$ 的出处
- [[Growth Rate Estimation 增长率估计]]：$g$ 的估计方法
- [[Capital Asset Pricing Model 资本资产定价模型]]（ch11）：另一种估计 $R$ 的方法——$E(R_i) = R_F + \beta_i(E(R_M)-R_F)$
- [[Discount Rate 折现率]]：$R$ 就是股票估值中的折现率

## ⚖️ 易混点对照（人类填写区域）
- 股利收益率 vs 资本利得收益率：
- 必要回报率 vs 预期回报率：

## 📝 个人批注（人类专属，AI 严禁写入）
- 考试重点：
- 计算陷阱：
- 个人理解：

> 📌 考点提示：
> 💡 记忆技巧：
> 🔢 典型考题：

## 📄 来源原文
> Start with the Dividend Growth Model: $P_0 = D_0(1+g)/(R-g)$. Rearrange and solve for R: $R = D_1/P_0 + g$. D1/P0: expected dividend yield (预期股利收益率). g: also as capital gains yield (资本利得收益率). R connects 2 parts: expected dividend yield, plus capital gains yield. Example: Solar Corp.'s last dividend was $.65 per share. Its dividends are growing at a rate of 4% and the current price per share is $11.25. D1 = $.65 × 1.04 = $.676. Dividend yield = 6%. Capital gains yield = 4%. R = 6% + 4% = 10%.
