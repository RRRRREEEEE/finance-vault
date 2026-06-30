---
tags:
  - 公司财务管理
  - ch11-CAPM
  - 模型
courses:
  - 公司财务管理
aliases:
  - Capital Asset Pricing Model
  - CAPM
  - 资本资产定价模型
  - SML
  - Security Market Line
created: 2026-06-30
source: Chap11_CAPM.pdf 第46-57页
chapter: "第11章 CAPM"
importance: "*****"
---

# 资本资产定价模型 (CAPM)

## 📌 定义
CAPM（Capital Asset Pricing Model）由 William Sharpe 于 1964 年提出（1990 年诺贝尔奖），描述了单只股票**期望收益与其系统风险（$\beta$）之间的线性关系**：

$$E(R_i) = R_F + \beta_i \times [E(R_M) - R_F]$$

> 💬 通俗理解：你想知道持有一只股票该要求多少回报？答案 = 无风险利率 + 股票的市场敏感度 × 市场的"超额回报"。无风险利率是保底，$\beta$ 越大你要求的额外回报越高。

## 🔗 前置知识
- [[Beta Coefficient 贝塔系数]]
- [[Systematic and Unsystematic Risk 系统风险与非系统风险]]
- [[Expected Return and Risk 期望收益与风险]]
- [[Required Return Estimation 必要收益率估计]]（ch06）

## 🧠 机制

### CAPM 公式拆解

$$E(R_i) = \underbrace{R_F}_{\text{无风险利率}} + \underbrace{\beta_i}_{\text{系统风险量}} \times \underbrace{[E(R_M) - R_F]}_{\text{市场风险溢价}}$$

| 组成部分 | 含义 |
|----------|------|
| $R_F$ | 无风险利率（时间价值） |
| $E(R_M) - R_F$ | **市场风险溢价**（Market Risk Premium）——市场比无风险资产多补偿多少 |
| $\beta_i \times [E(R_M) - R_F]$ | **个股风险溢价** — 个股因承担系统风险获得的额外补偿 |
| $E(R_i)$ | 个股的**期望/必要回报率** |

### SML (Security Market Line 证券市场线)

SML 是 CAPM 的**图形表达**——横轴为 $\beta$，纵轴为期望收益：

![[ch11 SML Security Market Line.png]]

| SML 上的关键点 | $\beta$ | $E(R)$ |
|:---|:---:|:---|
| 无风险资产 | 0 | $R_F$ |
| 市场组合 | 1 | $E(R_M)$ |
| 进攻型股票 | 1.5 | $R_F + 1.5(E(R_M)-R_F)$ |
| 防御型股票 | 0.5 | $R_F + 0.5(E(R_M)-R_F)$ |

### 计算实例

> $R_F = 3\%$，$E(R_M) = 10\%$，股票 $\beta_i = 1.5$。

$$E(R_i) = 3\% + 1.5 \times (10\% - 3\%) = 3\% + 10.5\% = 13.5\%$$

### 三种特殊情况

| $\beta_i$ | $E(R_i)$ | 含义 |
|:---:|------|------|
| 0 | $R_F$ | 零系统风险，只拿无风险收益 |
| 0 < β < 1 | 介于 $R_F$ 和 $R_M$ 之间 | 防御型 |
| 1 | $R_M$ | 与市场同风险同收益 |
| > 1 | 大于 $R_M$ | 进攻型——高收益补偿高风险 |

### CAPM 的关键假设

- 投资者是理性的均值-方差优化者
- 市场无摩擦（无交易成本、无税）
- 所有投资者可以以无风险利率无限借贷
- 所有投资者对期望收益、方差、协方差**预期一致**（同质预期）

## 📐 公式

$$E(R_i) = R_F + \beta_i \times [E(R_M) - R_F]$$

$$Individual\ Stock\ Risk\ Premium = \beta_i \times Market\ Risk\ Premium$$

| 符号 | 含义 |
|------|------|
| $E(R_i)$ | 股票 $i$ 的期望收益 |
| $R_F$ | 无风险利率 |
| $\beta_i$ | 股票 $i$ 的贝塔系数 |
| $E(R_M)$ | 市场组合的期望收益 |
| $E(R_M) - R_F$ | 市场风险溢价 |

## 🏛️ 应用
- **估算必要回报率 $R$**：CAPM 是估计股票折现率的最常用方法（用于 DDM 和 DCF）
- **投资决策**：如果预期收益 > CAPM 要求收益 → 股票被低估 → 买入
- **业绩评价**：比较实际收益与 CAPM 预测的"理应收益"
- **资本成本**：CAPM 是估算权益资本成本的基础（ch12 将展开）

## 📖 相关术语
- [[Beta Coefficient 贝塔系数]]：$\beta$ 是 CAPM 唯一的个股特定输入
- [[Systematic and Unsystematic Risk 系统风险与非系统风险]]：CAPM 只对系统风险定价
- [[Efficient Frontier 有效边界]]：加入无风险资产后，有效边界变为 CML
- [[Required Return Estimation 必要收益率估计]]（ch06）：$R = D_1/P_0 + g$ 是另一种估算 $R$ 的方法

## ⚖️ 易混点对照（人类填写区域）
- SML vs CML：
- CAPM 中的 $R$ vs DDM 中的 $R$：

## 📝 个人批注（人类专属，AI 严禁写入）

## 📄 来源原文
> CAPM describes the relationship between the expected return and risk of a stock together the market movement. Promoted by William Sharpe (1964), won Nobel Memorial Prize in Economics in 1990. $E(R_i) = R_F + \beta_i(R_M - R_F)$. SML (Security Market Line): the graphical representation of CAPM. β=0 → E(R)=RF (No Risk). β=1 → E(R)=RM (Same Risk with Market). β>1 → E(R)>RM (Bigger Risk). Individual Stock Risk Premium = β × Market Risk Premium.
