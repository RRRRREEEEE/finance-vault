---
tags:
  - 公司财务管理
  - ch03-财务报表分析
  - 模型
courses: [公司财务管理]
aliases: [DuPont Identity, 杜邦恒等式, DuPont Analysis, 杜邦分析]
created: 2026-06-29
source: "Chap3_Financial Statement Analysis.pptx 第58-66页"
chapter: "第3章 Financial Statements Analysis"
importance: "*****"
---

# 杜邦恒等式 (DuPont Identity)

## 📌 定义
杜邦恒等式将 ROE 分解为三个驱动因素的乘积：**ROE = PM × TAT × EM**。它揭示了 ROE 的来源——利润来自经营效率、资产效率还是财务杠杆，为改进方向提供了明确的分解框架。

> 💬 通俗理解：ROE 只是一个最终数字。DuPont 把它拆成三块：赚得快不快（PM）、转得快不快（TAT）、借得多不多（EM）。ROE 高是因为产品暴利还是高杠杆——差别大了。

## 🔗 前置知识
[[ROA and ROE 资产回报率与股本回报率]]、[[Profit Margin 销售利润率]]、[[Total Asset Turnover 总资产周转率]]、[[Equity Multiplier 权益乘数]]

## 🧠 机制

### 推导过程
$$ ROE = \frac{NI}{TE} $$

乘以 1（TA/TA）并重排：
$$ ROE = \frac{NI}{TE} \times \frac{TA}{TA} = \frac{NI}{TA} \times \frac{TA}{TE} = ROA \times EM $$

再次展开 ROA：
$$ ROE = \frac{NI}{Sales} \times \frac{Sales}{TA} \times \frac{TA}{TE} = PM \times TAT \times EM $$

### 数值验证
| 组件 | 公式 | 数值 |
|------|------|------|
| PM | NI / Sales | 363 / 2311 = 15.7% |
| TAT | Sales / TA | 2311 / 3588 = 0.64 |
| EM | TA / TE | 3588 / 2591 = 1.39 |
| **ROE** | **PM × TAT × EM** | **15.7% × 0.64 × 1.39 = 14.0%** |

### 三种商业模式

| 策略 | PM | TAT | EM | ROE | 典型 |
|------|-----|-----|------|-----|------|
| **厚利少销** | 高 (30%+) | 低 (<0.5) | 低 | 中等 | 奢侈品、茅台 |
| **薄利多销** | 低 (<5%) | 高 (>1.5) | 中 | 中等 | Walmart、Costco |
| **高杠杆** | 中 | 中 | 高 (>5) | 高 | 银行、地产 |

### ROE 的"质量"判断
- PM 驱动的 ROE → 可持续（经营能力强）
- TAT 驱动的 ROE → 可持续（运营效率高）
- EM 驱动的 ROE → **风险高**（靠借债放大收益，衰退时放大亏损）

## 📊 图形

![[公司财务管理Ch03 杜邦推导1.png]]

> 图形说明：杜邦分析推导第一步——ROE = ROA × EM，将 ROE 拆解为资产回报率和权益乘数。

![[公司财务管理Ch03 杜邦推导2.png]]

> 图形说明：杜邦分析推导第二步——ROA = PM × TAT，再将 ROA 拆解为利润率和资产周转率。

![[公司财务管理Ch03 杜邦分析 茅台示例.png]]

> 图形说明：贵州茅台 2023年5月 DuPont 分析示例——极高的 PM（约50%）驱动 ROE，几乎不依赖杠杆（EM 接近 1.2）。

## 🏛️ 应用
- 企业诊断：ROE 下降 → 三个因素哪个在恶化？
- 目标管理：ROE 要提升 5% → 哪个维度最有空间？
- 竞争分析：同行 ROE 相同但驱动因素不同 → 商业模式差异

## 📖 相关术语
- [[ROA and ROE 资产回报率与股本回报率]]：ROE 是最终指标
- [[Profit Margin 销售利润率]]：DuPont 第一要素
- [[Total Asset Turnover 总资产周转率]]：DuPont 第二要素
- [[Equity Multiplier 权益乘数]]：DuPont 第三要素

## 📝 个人批注
- 考试重点：三因素分解公式 + 提高 ROE 的三种途径
- 计算陷阱：
- 个人理解：

> 📌 考点提示：**ROE = PM × TAT × EM = (NI/S) × (S/TA) × (TA/TE)**
> 💡 记忆技巧：PM 是"赚得快"，TAT 是"转得快"，EM 是"借得多"
> 🔢 典型考题：

## 📄 来源原文
> ROE = NI / TE = (NI / TA) (TA / TE) = ROA × EM. ROE = PM × TAT × EM. Profit margin measures operating efficiency, total asset turnover measures asset use efficiency, equity multiplier measures financial leverage.
