---
tags:
  - 公司财务管理
  - ch06-股票估值
  - 模型
courses:
  - 公司财务管理
aliases:
  - Growth Rate Estimation
  - 增长率估计
  - Sustainable Growth Rate
  - g = b × ROE
created: 2026-06-30
source: Chap6_Stock.pdf 第42-45页
chapter: "第6章 股票估值"
importance: "***"
---

# 增长率估计 (Growth Rate Estimation)

## 📌 定义
在股利增长模型中，股利增长率 $g$ 可以通过公司基本面来估计：**$g = b \times ROE$**，其中 $b$ 为留存收益率（Retention Ratio），ROE 为净资产收益率。

> 💬 通俗理解：公司能成长多快取决于两个因素：挣了钱留多少在公司（$b$），以及留下的钱能赚多少（ROE）。全部分红 → $g=0$；一分不留全投资 → $g = ROE$。

## 🔗 前置知识
- [[Constant Growth Model 固定增长模型]]
- [[ROA and ROE 资产回报率与股本回报率]]（货币金融学）
- [[DuPont Identity 杜邦恒等式]]：ROE 的分解工具

## 🧠 机制

### 推导：$g = b \times ROE$

**假设**：留存收益是公司增长的唯一资金来源（无外部融资）。

**步骤**：
1. 下一期利润 = 当期利润 × (1 + g)
2. 下一期利润也可写作：当期利润 + 留存收益贡献
3. 留存收益贡献 = 当期留存收益 × 留存收益回报率

$$Current\ Earnings \times (1+g) = Current\ Earnings + Current\ R/E \times Return\ on\ R/E$$

4. 两边除以 Current Earnings：
$$1 + g = 1 + \frac{Current\ R/E}{Current\ Earnings} \times Return\ on\ R/E$$

$$g = b \times Return\ on\ R/E$$

其中 $b = R/E \div Earnings$（留存收益率）。

5. 理想情况下，留存收益回报率 ≈ ROE：
$$g = b \times ROE$$

### 重要恒等式

$$b + Dividend\ Payout\ Ratio = 1$$

即：留存收益率 + 股利支付率 = 100%。

### 计算实例

> 某公司股利支付率 30%（即 $b = 70\%$），ROE = 12%。

$$g = b \times ROE = 0.70 \times 0.12 = 0.084 = 8.4\%$$

公司股利将以每年 8.4% 的速度增长。

## 📐 公式

| 符号 | 含义 |
|------|------|
| $g$ | 股利可持续增长率 |
| $b$ | 留存收益率 = 留存收益/净利润 |
| $1-b$ | 股利支付率 = 股利/净利润 |
| $ROE$ | 净资产收益率 = 净利润/股东权益 |

## 🏛️ 应用
- **可持续增长率 (SGR)** 是公司金融的核心概念
- $b$ 越高 → 增长越快，但股利越少（股东现期收益降低）
- 借助 [[DuPont Identity 杜邦恒等式]] 可将 $g$ 进一步分解为利润率 × 周转率 × 权益乘数 × $b$

## 📖 相关术语
- [[ROA and ROE 资产回报率与股本回报率]]（货币金融学）：ROE 是 $g$ 的核心驱动因素
- [[DuPont Identity 杜邦恒等式]]：将 ROE 分解为三部分 → $g$ 的五因子分解
- [[Constant Growth Model 固定增长模型]]：$g$ 的最终去向
- [[Required Return Estimation 必要收益率估计]]：$R = D_1/P_0 + g$

## ⚖️ 易混点对照（人类填写区域）
- 留存收益率 $b$ vs 股利支付率：
- $g = b \times ROE$ vs $g = b \times ROA$：

## 📝 个人批注（人类专属，AI 严禁写入）
- 考试重点：
- 计算陷阱：
- 个人理解：

> 📌 考点提示：
> 💡 记忆技巧：
> 🔢 典型考题：

## 📄 来源原文
> Assume a company's growth rate g: Earnings next period = Current Earnings × (1+g) = Current Earnings + Current R/E × Return on R/E. Divided by Current Earnings: 1+g = 1 + (Current R/E / Current Earnings) × Return on R/E. g = R/E retention ratio × Return on R/E. R/E increases Equity, Return on R/E ≈ ROE under ideal scenario. ∴ g = b × ROE (b is the R/E retention ratio). Note: Current Earnings = Current R/E + Current Dividend. R/E retention rate + Dividend ratio = 1.
