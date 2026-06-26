# 笔记制作标准操作流程 (SOP)

> **用途**：AI 处理每一章课件时的逐步操作清单。遇到不确定的情况，先查本文再动手。
> **更新日期**：2026-06-26

---

## 流程图

> 与 `CLAUDE.md` 流程一致：前置准备 → 分批提取 → 创建笔记 → **生成知识串讲** → 收尾检查。

---

## 第一步：前置准备

### 1.1 读取上下文
- [ ] 读取 `阅读进度.json`，找到当前课程和待处理章节
- [ ] 读取 `AI协作指令_v2.md` 刷新模板和规则
- [ ] 如章节已在进度中标记 `in_progress`，从 `processed_pages` 断点继续

### 1.2 定位源文件
```
源文件目录：D:\.pogget\user_storage\u_9e95ae\8e43a\{课程名}\
```
- [ ] 用 `ls` 列出源文件，找到目标章节的文件名
- [ ] 确认文件格式（`.pptx` / `.pdf`）
- [ ] ⚠️ 源文件目录**只读**，绝不修改或删除

### 1.3 扫描全部页数
- [ ] PPTX：`python-pptx` 读取 `len(prs.slides)`，逐页预览首行文本
- [ ] PDF：PyMuPDF `len(doc)` 或 Read 工具
- [ ] 将总页数写入 `阅读进度.json`，状态标记为 `in_progress`

### 1.4 搜索已有笔记
- [ ] 根据页面预览识别核心概念名
- [ ] 对每个概念执行 `Grep` + `Glob` 搜索全 Vault
- [ ] 已有 → 标记"待补充"；没有 → 标记"待新建"

---

## 第二步：分批提取

### 2.1 选批策略

> 详见 `AI协作指令_v2.md` §5.8。简记：正常 5-8 页/批，密集章 3-5，稀疏章 8-12，补漏整章扫。

### 2.2 提取文本

**PPTX（.pptx）**：
```bash
.venv/Scripts/python -c "
from pptx import Presentation
prs = Presentation(r'源文件路径')
for i in range(start, end):  # 0-indexed
    slide = prs.slides[i]
    for shape in slide.shapes:
        if shape.has_text_frame:
            for para in shape.text_frame.paragraphs:
                if para.text.strip():
                    print(para.text.strip())
        if shape.has_table:
            # 逐行打印表格
"
```

**PDF（.pdf）**：
- 小文件（<20MB）→ Read 工具直接读取
- 大文件 → `pdftotext -layout "源文件" "输出.txt"`

### 2.3 提取/生成图片

> **关键原则：笔记里的图不能是 TODO。每张图必须有实际文件。**

#### 情况A：PPTX 嵌入图片（PNG/JPEG）
```bash
# 1. 用 zipfile 提取 ppt/media/ 中全部图片
# 2. 通过 slideN.xml.rels 匹配图片→页面
# 3. 按描述性名称重命名 → 放入 999-Attachments/
```
命名格式：`{课程名}Ch{XX} {描述}.png`
示例：`财政学Ch04 负外部性的经济影响.png`

#### 情况B：PPTX 嵌入矢量图（EMF/WMF）
```powershell
# 用 PowerShell System.Drawing 转换
Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Image]::FromFile('输入.emf')
$bmp = New-Object System.Drawing.Bitmap($img.Width, $img.Height)
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.Clear([System.Drawing.Color]::White)
$g.DrawImage($img, 0, 0)
$bmp.Save('输出.png', [System.Drawing.Imaging.ImageFormat]::Png)
```
转换后按描述性名称重命名。

#### 情况C：PPTX 绘制图形（AutoShape/Line，无嵌入图片）

> **🚫 严禁用 matplotlib 自己画图。必须用课件原图！**

```bash
# 用 PowerPoint COM 导出整页为高清 PNG
.venv/Scripts/python -c "
import win32com.client, os
powerpoint = win32com.client.Dispatch('PowerPoint.Application')
pres = powerpoint.Presentations.Open(r'源文件.pptx', ReadOnly=True, WithWindow=False)
slide = pres.Slides(页码)  # 1-indexed
slide.Export(r'D:\data\金融学\999-Attachments\财政学ChXX 描述.png', 'PNG', 1920, 1080)
pres.Close()
powerpoint.Quit()
"
```

> ⚠️ 需要 pywin32：`.venv/Scripts/pip install pywin32`（仅首次）

#### 情况D：PDF 嵌入图片
```python
import fitz
doc = fitz.open("源文件.pdf")
page = doc[page_num]
for img in page.get_images():
    xref = img[0]
    pix = fitz.Pixmap(doc, xref)
    pix.save(f"输出.png")
```

#### 情况E：PDF 整页渲染（矢量图/复杂排版）
```python
import fitz
doc = fitz.open("源文件.pdf")
page = doc[page_num]
pix = page.get_pixmap(dpi=200)
pix.save("输出.png")
```

### 2.4 图片命名与归档
- [ ] 所有图片放入 `999-Attachments/`
- [ ] 命名格式：`{课程名}Ch{XX} {描述性中文名称}.{png/jpg}`
- [ ] **严禁** hash 命名（如 `ch04_a1b2c3d4.png`）
- [ ] 与 ch03 图片命名风格一致（参考 `财政学Ch03 帕累托最优局部均衡.png`）

---

## 第三步：创建笔记

### 3.1 确定目标路径

| 情况 | 路径 |
|------|------|
| 单课程知识点 | `{课程编号}-{课程名}/ch{XX}-{章节简称}/{主题子文件夹}/{英文 中文}.md` |
| 跨课程枢纽概念 | 首次出现课程的章节文件夹 |
| 壳笔记（仅1-2句定义）| 与内容笔记同路径 |
| 章节索引 | `{课程编号}-{课程名}/ch{XX}-{章节简称}/{课程名} ch{XX} {章节标题}.md` |

**主题子文件夹**：笔记**必须**归入主题子文件夹，不允许直接放在章文件夹根目录。子文件夹按章内主题板块划分，每组 3-8 个概念。汉语命名，如 `外部性/`、`投票与公共选择/`、`早期贸易理论/`。

**路径示例**：
```
200-财政学/ch04-外部性与公共产品/外部性/Negative Externality 负外部性.md
200-财政学/ch04-外部性与公共产品/公共产品/Public Goods 公共产品.md
200-财政学/ch04-外部性与公共产品/财政学 ch04 外部性与公共产品.md  ← 章节索引在章根
```

### 3.2 确定文件名

**知识点笔记**：`{English Term} {中文术语}.md`
- 英文首字母大写，中英文间一个空格
- 无标准英文术语 → 只写中文
- 示例：`Liquidity Preference Theory 流动性偏好理论.md`

**章节索引**：`{课程名} ch{XX} {章节标题}.md`
- ch 小写，XX 两位数字
- 示例：`财政学 ch04 外部性与公共产品.md`

### 3.3 填写 Frontmatter

```yaml
---
tags:
  - {课程名}           # 或 枢纽概念
  - ch{XX}-{章节简称}   # 如 ch04-外部性与公共产品
  - {知识类型}          # 概念/理论/模型/公式/政策/制度/工具/现象
courses: [{课程名}]     # 跨课程概念列多个
aliases: [{英文全称}, {英文缩写}, {中文名}, {中文别名}]
created: {YYYY-MM-DD}
source: "{文件名} 第{X}页"
chapter: "{第X讲} {标题}"
importance: "{* 到 *****}"   # AI自评，必须加引号
---
```

### 3.4 填写正文（按模板）

模板详见 `AI协作指令_v2.md` §3.3。核心规则：

| 板块 | 触发条件 | 无内容时 |
|------|----------|----------|
| 📌 定义 | **必填** | — |
| 💬 通俗理解 | 学术表述干涩 | 删除该行 |
| 🔗 前置知识 | 原文提到依赖概念 | 写"无" |
| 🧠 机制 | 原文有逻辑推导 | — |
| 📐 公式与计算 | 原文有公式 | 删除整节 |
| 📊 图形 | 原文有图表 | 删除整节 |
| 🏛️ 应用 | 原文涉及政策/实践 | 删除整节 |
| 📖 相关术语 | 原文含待扩展概念 | 删除整节 |
| 🔀 跨课程链接 | 原文提到关联 | 删除对应行 |
| ⚖️ 易混点 | — | 保留空节等人类 |
| 📝 个人批注 | — | AI 严禁写入 |
| 📄 来源原文 | **必填** | — |

### 3.5 插入图片

```markdown
## 📊 图形

![[财政学Ch04 负外部性的经济影响.png]]

> 图形说明：{原文对图的解释，没有则写"见原文"}
```

- [ ] 图片引用格式：`![[{描述性名称}.png]]`
- [ ] 紧跟一行 `> 图形说明：...`
- [ ] 不放尺寸参数（Obsidian 自适应）

---

## 第四步：生成知识串讲

> **整章笔记全部完成后自动执行**，不等人类说。串讲是讲稿式复习文件。

### 4.1 什么是串讲

一章一篇的**讲稿式复习文件**。把该章所有原子笔记重组为连贯叙事，用口语化语气把概念串成故事。读者看完应能回答"这一章到底讲了什么、为什么是这个逻辑"。

**与笔记的区别**：笔记是字典（查概念），串讲是课堂（学逻辑）。

### 4.2 文件命名与路径

```
{课程编号}-{课程名}/ch{XX}-{章节简称}/Ch{XX} 知识串讲 {核心问题}.md
```

核心问题用一句话概括整章要回答的问题。示例：`Ch01 知识串讲 为什么要进行国际贸易.md`

### 4.3 正文模板

```markdown
# 第X章 知识串讲：{一句话概括整章的核心问题}

## 一、一句话回答
{用最短的话回答标题的问题。10-30字。}

---
## 二、{第一个叙事板块}
...
## 末、概念对照表
| 概念对 | 区别 |

## 末+1、最重要的故事 / 考试最易考点
```

### 4.4 写作规则

- **叙事重组，不按页码罗列**：找到章的逻辑主线，按因果/时间/层次重新编排
- **口语化语气**：用"你"称呼读者，用反问句引导思考，用大白话翻译学术概念（配合 `> ` 引用块）
- **关键概念加粗 + 英文**：首次出现的重要概念——**中文**（English）。⚠️ 不用 `[[wiki 链接]]`（串讲是线性阅读）
- **善用表格和文字流程图**：适合分类对比、因果链推导
- **两个标配收尾**：概念对照表（≥3 对易混概念）+ 最重要的故事/考试最易考点
- **长度控制**：25-40 页课件 → 80-200 行，概念密集章可到 250 行

### 4.5 红线

- 🚫 不新增知识
- 🚫 不逐页罗列
- 🚫 不用 wiki 链接
- 🚫 不替代章节索引

---

## 附录：常见错误速查

| 错误 | 原因 | 解决方案 |
|------|------|----------|
| 笔记放在 Vault 根目录 | 没指定目标路径 | 按 §3.1 确定路径 |
| 图片用 hash 命名 | 提取后没重命名 | 按 §2.4 重命名 |
| 图表写 TODO 占位 | 没提取/没生成图片 | 按 §2.3 四种情况分别处理 |
| 章节索引放错位置 | 放课程文件夹而非章文件夹内 | 索引和笔记放在一起 |
| 重复建笔记 | 没先搜索 Vault | 按 §1.4 搜索 |
| importance 忘加引号 | YAML 解析需要 | `importance: "****"` 不是 `importance: ****` |
| 中文在 matplotlib 里显示方框 | 没配置中文字体 | `plt.rcParams['font.family'] = 'SimHei'` |
