---
tags:
  - 公司财务管理
  - ch07-NPV与投资规则
  - 概念
courses:
  - 公司财务管理
aliases:
  - Capital Budgeting Methods Comparison
  - 资本预算方法比较
  - Investment Decision Rules
created: 2026-06-30
source: Chap7_NPV.pdf 第44-49页
chapter: "第7章 NPV与投资规则"
importance: "**"
---

# 资本预算方法比较 (Capital Budgeting Methods Comparison)

## 📌 定义
企业实践中存在六种主要的资本预算方法：**NPV、IRR、回收期、折现回收期、AAR 和 PI**。各方法在理论正确性和实践使用频率上存在显著差异。NPV 是理论上唯一没有严重缺陷的方法。

> 💬 通俗理解：NPV 是"正规军"，IRR 是"特战队"（大部分时候靠得住但有两个弱点），回收期是"辅警"（不够严谨但快），AAR 是"用算盘的会计"（完全不在现代金融的频道上）。

## 🔗 前置知识
所有六种方法。

## 🧠 机制

### 六种方法全景对比

| 方法 | 接受标准 | 使用现金流？ | 考虑时间价值？ | 考虑全部现金流？ | 理论正确性 |
|------|----------|:---:|:---:|:---:|:---:|
| **NPV** | NPV > 0 | ✅ | ✅ | ✅ | ⭐⭐⭐⭐⭐ |
| **IRR** | IRR > R | ✅ | ✅ | ✅ | ⭐⭐⭐⭐ |
| **PI** | PI > 1 | ✅ | ✅ | ✅ | ⭐⭐⭐ |
| **折现回收期** | ≤ 截止期 | ✅ | ✅ | ❌ | ⭐⭐ |
| **回收期** | ≤ 截止期 | ✅ | ❌ | ❌ | ⭐ |
| **AAR** | AAR > 目标 | ❌ | ❌ | — | — |

### 实务使用频率调查

> 0 = 从不使用，4 = 始终使用

| 方法 | 大公司 | 小公司 |
|------|:---:|:---:|
| **IRR** | 3.41 | 2.87 |
| **NPV** | **3.42** | 2.83 |
| 回收期 | 2.25 | 2.72 |
| 折现回收期 | 1.55 | 1.58 |
| AAR | 1.25 | 1.41 |
| PI | 0.75 | 0.88 |

> **大公司**：NPV 和 IRR 几乎并列第一（3.42 vs 3.41）。**小公司**：回收期使用频率显著更高（2.72，接近 NPV 的 2.83）。

### 黄金准则

| 场景 | 最佳方法 |
|------|----------|
| 常规现金流 + 独立项目 | NPV = IRR，任选 |
| 互斥项目 | **NPV**（IRR 有规模/时序问题） |
| 非常规现金流 | **NPV**（IRR 可能多重或无解） |
| 资本配给 | PI 排序（但最终仍看 NPV） |
| 小型投资 | 回收期初筛 + NPV 确认 |

## 📊 图形

![[ch07 Capital Budgeting Survey.png]]

> 图形说明：大公司与小公司六种资本预算方法的使用频率比较——NPV 和 IRR 是最普遍的方法。

## 🏛️ 应用
- **NPV 永远是最优准则**——其他方法都是它的近似或补充
- 实践中企业常同时使用多种方法：NPV 做主要决策，IRR 做收益率表达，回收期做初筛
- 大公司更依赖 NPV/IRR（分析能力更强），小公司更依赖回收期（简单直观、偏好流动性）

## 📖 相关术语
- [[NPV Investment Rule NPV投资法则]]：唯一的无缺陷方法
- [[Internal Rate of Return 内部报酬率]]：最常用的 NPV 替代方法
- [[Capital Budgeting 资本预算]]（ch01）：所有方法服务于资本预算决策
- [[Payback Period 投资回收期]]：最简单的非折现方法

## 📄 来源原文
> The most frequently used technique for large and small firms is either IRR, NPV or Payback method. Net present value: Difference between market value and cost, Accept the project if the NPV is positive, Has no serious problems, Preferred decision criterion. IRR is unreliable with non-conventional cash flows or mutually exclusive projects. PI: May be used to rank projects in the presence of capital rationing. AAR: Serious problems. Payback: Doesn't account for time value of money.
