---
tags:
  - 公司财务管理
  - ch12-资本成本
  - 概念
courses:
  - 公司财务管理
aliases:
  - Project Cost of Capital
  - 项目资本成本
  - Divisional Cost of Capital
  - Hurdle Rate
created: 2026-06-30
source: Chap12_Cost_of_Capital.pdf 第30-32页
chapter: "第12章 资本成本"
importance: "***"
---

# 项目资本成本 (Project Cost of Capital)

## 📌 定义
不同风险的项目应使用**不同的折现率**。使用单一公司级折现率评估所有项目会在长期中增加公司风险同时降低公司价值——低风险项目被错误拒绝，高风险项目被错误接受。

> 💬 通俗理解：一个电力公司如果用公司整体的 10% 折现率去评估新开的汽车零售业务，会严重低估风险——汽车业务应该有更高的折现率。把公司所有项目都按一个标准定价，就像不管老少都收一样的保险费。

## 🔗 前置知识
- [[Cost of Equity Capital 权益资本成本]]
- [[Beta Estimation and Determinants 贝塔估计与决定因素]]

## 🧠 机制

### 单一折现率的陷阱

> 某集团 CAPM 成本 17%（$R_F=4\%$, $R_M-R_F=10\%$, $\beta_{firm}=1.3$），三个部门：

| 部门 | $\beta$ | 应使用的 $R$ | 按 17% 评估的后果 |
|------|:---:|:---:|------|
| 汽车零售 | 2.0 | **24%** | 高风险项目按过低的 17% 被**错误接受** |
| 硬盘制造 | 1.3 | 17% | 恰好 |
| 电力公用 | 0.6 | **10%** | 低风险项目按过高的 17% 被**错误拒绝** |

### 正确做法

$$R_{project} = R_F + \beta_{project} \times (R_M - R_F)$$

- 电力部门：$R = 4\% + 0.6 \times 10\% = 10\%$ → IRR > 10% 就接受
- 汽车零售：$R = 4\% + 2.0 \times 10\% = 24\%$ → IRR > 24% 才接受

### 实践方法

| 方法 | 说明 |
|------|------|
| **行业贝塔法** | 找到与项目同行业的上市公司，用其行业平均 $\beta$ 作为项目 $\beta$ |
| **去杠杆-再杠杆法** | 取可比公司 $\beta_E$ → 去杠杆得 $\beta_A$ → 按本公司杠杆再加回 |
| **分部报告法** | 大型集团为不同业务分部设定不同的折现率 |

## 📊 图形

![[ch12 One Discount Rate Problem.png]]

> 图形说明：使用单一折现率（虚线）——低贝塔的正 NPV 项目被错误拒绝，高贝塔的负 NPV 项目被错误接受。

![[ch12 Divisional Cost of Capital.png]]

> 图形说明：不同风险的项目应使用 SML 上对应的折现率——电力 10%、硬盘 17%、汽车 24%。

## 🏛️ 应用
- **集团公司**必须按业务分部设置不同折现率（零售 ≠ 电力 ≠ 科技）
- 跨行业并购时用目标行业贝塔而非收购方贝塔
- 避免"一刀切"折现率导致的资本错配

## 📖 相关术语
- [[Cost of Equity Capital 权益资本成本]]：项目折现率的基础
- [[Weighted Average Cost of Capital 加权平均资本成本]]：公司整体 WACC 不等于每个项目的折现率
- [[Beta Estimation and Determinants 贝塔估计与决定因素]]：项目贝塔的确定方法

## 📄 来源原文
> A firm that uses one discount rate for all projects may over time increase the risk of the firm while decreasing its value. Different divisions should use different discount rates matching their risk profiles. Example: Conglomerate with automotive retail (β=2.0, R=24%), hard drive (β=1.3, R=17%), electric utility (β=0.6, R=10%). Using 17% for all leads to incorrect project selection.
