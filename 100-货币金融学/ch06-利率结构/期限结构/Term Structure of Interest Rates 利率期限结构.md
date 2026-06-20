---
tags:
  - 货币金融学
  - ch06-利率结构
  - 理论
courses:
  - 货币金融学
aliases:
  - Term Structure of Interest Rates
  - 利率期限结构
  - Yield Curve
  - 收益率曲线
  - Expectations Theory
  - 预期理论
  - Segmented Markets Theory
  - 分割市场理论
  - Liquidity Premium Theory
  - 流动性溢价理论
created: 2026-06-06
source: Ch06-2026-T [自动保存].pptx 第22-44页
chapter: Chapter 6 The Risk and Term Structure of Interest Rates
importance: "*****"
---

# 利率期限结构 (Term Structure of Interest Rates)

## 📌 定义
利率期限结构研究相同风险、流动性、税收特征的债券，其利率如何随到期期限变化。收益率曲线是描述这种关系的图形。

> 💬 通俗理解：为什么10年期国债利率通常比1年期高？收益率曲线为什么差不多总是向上倾斜？三种理论来回答。

## 🔗 前置知识
- [[Risk Structure of Interest Rates 利率风险结构]]
- [[Yield to Maturity 到期收益率]]
- [[Bond 债券]]

## 🧠 机制

### 收益率曲线（Yield Curve）

三种形态：
| 形态 | 特征 | 含义 |
|------|------|------|
| **上倾** | 长期利率 > 短期利率 | 常见形态 |
| **平坦** | 长期利率 = 短期利率 | |
| **倒挂** | 长期利率 < 短期利率 | 通常预示衰退 |

### 三个经验事实（Term Structure Facts）

1. **不同期限利率同向波动**
2. **短期利率低时曲线多上倾，短期利率高时曲线多下倾**
3. **收益率曲线通常向上倾斜**

### 三种理论

#### 1. 预期理论（Expectations Theory）

**假设**：不同期限债券完全可替代

**结论**：长期利率 = 未来短期利率预期的平均值
$$ i_{nt} = \frac{i_t + i_{t+1}^e + i_{t+2}^e + ... + i_{t+n-1}^e}{n} $$

**解释力**：
- ✅ 事实1：短期利率↑→未来预期↑→长期利率↑
- ✅ 事实2：短期低→预期回升→曲线上倾；短期高→预期下降→曲线下倾
- ❌ 事实3：无法解释——短期利率未来升降概率均等，长期均值不应总是更高

#### 2. 分割市场理论（Segmented Markets Theory）

**假设**：不同期限债券完全不可替代，市场完全分割

**结论**：每种期限的利率独立决定。人们偏好短期→短期债券需求高→价格高→利率低；长期利率高→曲线通常上倾。

**解释力**：
- ✅ 事实3：解释曲线通常上倾
- ❌ 事实1、2：无法解释（独立决定则不应同向波动）

#### 3. 流动性溢价理论（Liquidity Premium Theory）

**假设**：不同期限债券可替代但不完全可替代

**结论**：长期利率 = 预期短期利率均值 + 流动性溢价（期限溢价）
$$ i_{nt} = \frac{i_t + i_{t+1}^e + ... + i_{t+n-1}^e}{n} + l_{nt} $$

其中 $l_{nt}$ 为期限 $n$ 的流动性溢价，随期限增加而增大。

**解释力**：✅ 解释全部三个事实！
- 事实1：预期部分带来同向波动
- 事实2：短期低时预期回升 + 升水 = 陡上倾
- 事实3：流动性溢价 $l_{nt} > 0$ 导致曲线通常上倾

### 解读收益率曲线

收益率曲线反映市场对未来短期利率的**预期**：
- 陡上倾 → 市场预期短期利率将上升
- 轻微上倾 → 仅流动性溢价，短期利率预期不变
- 平坦/倒挂 → 市场预期短期利率将大幅下降

## 📖 相关术语（如有）

### 三个理论（按解释力递增）
- [[Expectations Theory 预期理论]]：完全替代 → 长期利率 = 预期短期均值 → 解释事实 1、2，不能解释 3
- [[Segmented Markets Theory 分割市场理论]]：完全不可替代 → 各期限独立 → 解释事实 3，不能解释 1、2
- [[Liquidity Premium Theory 流动性溢价理论]]：替代但不完全 → 预期均值 + 期限溢价 $l_{nt}$ → **解释全部三个事实** ✅
- [[Preferred Habitat Theory 习惯性偏好理论]]：流动性溢价理论的广义版，溢价不必随期限单调递增

### 图形与现象
- [[Yield Curve 收益率曲线]]：期限结构的图形表达——上倾/平坦/倒挂三种形态
- [[Inverted Yield Curve 翻转的收益率曲线]]：倒挂的详细分析——短期利率异常高时的衰退预警

### 与风险结构的关系
- [[Risk Structure of Interest Rates 利率风险结构]]：两个框架都涉及"流动性"，但含义不同——
  - **期限结构（本笔记）**：流动性溢价是补偿项 $l_{nt}$ → 期限越长补偿越大 → 影响不同期限的利差
  - **风险结构**：流动性是资产的属性 → 变现快不快 → 影响同期限不同债券的利差
- [[Liquidity 流动性]]：区分"资产流动性属性"和"期限流动性补偿"
- [[Interest-Rate Risk 利率风险]]：长期债券对利率更敏感——这是期限结构存在的重要原因
- [[Yield to Maturity 到期收益率]]：YTM 用于构建收益率曲线

## 📄 来源原文
> Expectations Theory: long-term rate = average of expected future short-term rates. Segmented Markets: bonds of different maturities are not substitutes. Liquidity Premium Theory = Expectations + Liquidity Premium. Liquidity Premium Theory explains all 3 facts.
