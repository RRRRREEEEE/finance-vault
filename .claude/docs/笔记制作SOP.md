# 笔记制作标准操作流程 (SOP)

> **用途**：AI 处理每一章课件时的逐步操作清单。遇到不确定的情况，先查本文再动手。
> **更新日期**：2026-06-14

---

## 流程图

> 与 `CLAUDE.md` 7 步流程一致，本文是每一步的详细操作说明。

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
| 单课程知识点 | `{课程编号}-{课程名}/ch{XX}-{章节简称}/{英文 中文}.md` |
| 跨课程枢纽概念 | 首次出现课程的章节文件夹 |
| 壳笔记（仅1-2句定义）| 与内容笔记同路径 |
| 章节索引 | `{课程编号}-{课程名}/ch{XX}-{章节简称}/{课程名} ch{XX} {章节标题}.md` |

**路径示例**：
```
200-财政学/ch04-外部性与公共产品/Negative Externality 负外部性.md
200-财政学/ch04-外部性与公共产品/财政学 ch04 外部性与公共产品.md
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

## 第三步补充：外部 AI 讨论内容入笔记

> **场景**：人类用其他 AI（如豆包、ChatGPT 等）讨论了某个概念，把 Q&A 发给你，让你补充到笔记里。

### 3A.1 基本原则

1. **课件原文是唯一权威** — 外部 AI 讨论内容必须先与课件原文交叉验证。与课件冲突的 → 不采纳；课件没涉及的 → 标记来源；与课件一致的 → 精炼后补充
2. **验证后再落笔** — 外部 AI 说的对不对？课件有没有相关的表述支持？验证通过才能写入笔记。不能外部 AI 说什么就写什么
3. **精炼，不照搬** — 外部 AI 的 Q&A 通常是口语对话体，冗长啰嗦。必须压缩为笔记风格（要点式、学术化、去废话），绝不能整段黏贴
4. **不新建笔记** — 外部讨论通常是深化已有概念，优先找已有笔记补充
5. **不改写课件原文** — 外部 AI 内容标注来源，不与课件原文混淆（读者必须能分清：哪些是老师课件的，哪些是外部讨论的）
6. **找最自然的位置** — 插入笔记模板中语义最匹配的板块（机制 / 易混点 / 应用），不是另起炉灶

### 3A.2 执行流程

```
人类发来外部AI的Q&A
        ↓
1. 识别核心概念名 → Grep/Glob 搜 Vault 找到目标笔记
        ↓
2. Read 目标笔记全文（不改之前必须读完）
        ↓
3. 【验证】对照课件原文检查外部 AI 内容：
   - 与课件一致 → ✅ 通过，精炼后补充
   - 与课件冲突 → ❌ 不采纳，必要时在笔记中加 ⚠️ AI备注 提醒
   - 课件未涉及 → ⚠️ 通过但标注来源，不混入课件原文区
        ↓
4. 【精炼】外部 AI 的对话体 → 笔记体：
   - 删除口语感叹词、重复追问、聊天废话
   - 提取核心逻辑链，改写为分点/段落
   - 保留关键术语和变量符号，补全缩写全称
   - 冗长的 Q&A 压缩到原文的 1/3~1/5 篇幅
        ↓
5. 判断精炼后的内容归属哪个板块（见 3A.3 速查表）
        ↓
6. 用 Edit 精确插入，格式和语气与已有笔记保持一致
        ↓
7. 在插入内容末尾标注来源：
   > 📎 以上内容来自人类与 [AI名称] 的讨论，经 Claude 验证课件原文并精炼。
        ↓
8. 更新 frontmatter 的 source 字段（如新增来源）
```

### 3A.3 常见内容类型 → 落点速查

| 外部讨论内容 | 落点板块 | 说明 |
|-------------|----------|------|
| "为什么图中没有 XX 线" | 🧠 机制 | 新增小节，命名如"为什么图中没有单独的 SMR 曲线？" |
| 概念 A 和 B 的区别 | ⚖️ 易混点对照 | 追加到已有条目后 |
| 公式推导细节 | 📐 公式与计算 | 追加到已有公式下方 |
| 现实案例 | 🏛️ 应用 | 追加到应用节 |
| 纯定义确认/澄清 | 📌 定义 | 可微调定义措辞 |
| 缩写/术语的全称补全 | 各板块 | 在首次出现处加英文全称 |
| 讨论性质但无确定结论 | 📄 来源原文 | 末尾加引用块，标注来源 |

### 3A.4 实操示例

**输入**：人类发来豆包关于"负外部性为什么图中没有 SMR"的讨论。

**执行**：
1. Grep `负外部性\|Negative Externality` → 找到 `Negative Externality 负外部性.md`
2. Read 全文
3. 判断：这是解释"为什么"的逻辑 → 入 🧠 机制，在"模型设定"后新增小节
4. 改写为笔记风格：拆分逻辑链、加粗关键句、保留变量符号、补充双外部性说明
5. 在新增小节末尾加 `> 📎 以下内容来自人类与豆包的讨论，经编辑整合。`
6. 同步处理讨论中提到的缩写补全（如 SMR/SMC 首次出现时加英文全称）

### 3A.5 红线

- 🚫 **不验证就直接写入**：外部 AI 内容必须与课件原文交叉验证后才能落笔。课件是最高的权威
- 🚫 **照搬外部 AI 原文**：对话体的冗长 Q&A 必须精炼为笔记体，不能整段黏贴
- 🚫 **不加来源标注就把外部 AI 内容混入课件原文**（读者分不清谁说的）
- 🚫 **用外部 AI 讨论"纠正"课件原文**（外部讨论是补充，不是裁判；发现冲突标 ⚠️ AI备注，不改课件内容）
- 🚫 **外部讨论中提到的、课件没涉及的新概念自行扩展**（仍遵守"不扩展知识"红线）
- 🚫 **外部内容新建独立笔记**（除非概念在 Vault 中确实不存在）

---

## 第四步：收尾

### 4.1 更新进度文件
- [ ] 追加 `processed_pages`
- [ ] 追加 `notes_generated`
- [ ] 每批处理完立即更新，不要攒到最后

### 4.2 全部完成后
- [ ] 生成章节索引文件（按页码线性列出知识点+一句话概括）
- [ ] 更新进度 JSON：`status: "completed"`, 统计 content_notes/shell_notes
- [ ] 运行检查清单（见 `笔记检查清单.md`）
- [ ] 报告完成：笔记数量、TODO 项、待人类确认项

### 4.3 断点恢复
新对话中人类说"继续处理 {课程} ch{XX}"后：
1. 读 `阅读进度.json` 找断点
2. 读本 SOP 恢复流程
3. 从断点页继续

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
