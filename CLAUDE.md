# CLAUDE.md · 金融知识图谱 Agent

> 红线与核心规则已通过 `.claude/rules/` 自动加载，本文只放项目身份、进度、操作入口。

@.claude/docs/AI协作指令_v2.md
@.claude/docs/笔记制作SOP.md
@.claude/docs/笔记检查清单.md
<!-- 如果 @import 未生效，请手动 Read 以上三个文件 -->

---

## 我是谁

将五门商科课程课件（PPTX/PDF）逐页拆分为 Obsidian 原子化笔记。AI 全权负责：提取→建笔记→评定重要性→双向链接→维护进度。

---

## 项目路径

```
Vault（笔记输出）: D:\data\金融学\
源文件（只读）  : D:\.pogget\user_storage\u_9e95ae\8e43a\{课程名}\
Python 环境     : C:\Users\14366\Desktop\金融项目操作库\.venv\Scripts\python

Vault 结构:
├── 100-货币金融学/   ✅ 12章
├── 200-财政学/       ✅ 11章
├── 300-公司财务管理/
├── 400-国际贸易/
├── 500-中级微观经济学/
├── 900-跨课程枢纽/
├── 999-Attachments/
└── 阅读进度.json
```

---

## 当前进度

| 课程 | 完成 | 下个任务 |
|------|------|----------|
| 货币金融学 | 12/12 ✅ | 用户笔记查缺补漏 |
| 财政学 | 11/11 ✅ | — |
| 公司财务管理 | 待开始 | 等源文件 |
| 国际贸易 | 待开始 | 7章源文件就绪 |
| 中级微观经济学 | 待开始 | 源文件就绪 |

财政学 ch05 源文件：`D:\.pogget\user_storage\u_9e95ae\8e43a\财政学\2026-05-第五讲-政治过程与集体选择.pptx`

---

## 当用户让你处理课程章节时

不管用户措辞怎么变——"继续财政学"、"做一下ch05"、"开始第五章"、"处理下一章"——你看到**"课程名 + 章节"意图**就自动执行以下流程，不要等用户告诉你具体怎么做：

```
1. 搜 → 读阅读进度.json找断点 + Grep/Glob全Vault去重
2. 扫 → python-pptx/PyMuPDF扫描总页数，写入进度文件
3. 提 → 分批(5-8页)提取文本+图片（图片全部来自课件原文件 🚫禁止matplotlib自绘）
4. 建 → 按模板建笔记，直接放课程章节文件夹（不进Inbox）
5. 插 → ![[图片名.png]] + 图形说明，确保无TODO残留
6. 更 → 每批完立即更新阅读进度.json
7. 检 → 跑笔记检查清单；整章完生成章节索引
```

如果用户只说"继续"没说具体章节 → 读进度JSON，自动找下一个 pending/in_progress 的章节。

## 工具速查

| 操作 | 工具 |
|------|------|
| PPTX 文本 | python-pptx |
| PPTX 嵌入图 | zipfile → 描述性命名 |
| PPTX 图表(AutoShape) | PowerPoint COM `slide.Export()` |
| PPTX EMF | PowerShell `System.Drawing.Image` |
| PDF 文本 | Read / pdftotext |
| PDF 渲染 | PyMuPDF `page.get_pixmap(dpi=200)` |

---

## 文档群

| 文档 | 加载方式 | 何时看 |
|------|---------|--------|
| `.claude/rules/always.md` | 🔄 自动 | — |
| `.claude/rules/vault-notes.md` | 🔄 操作Vault时自动 | — |
| `.claude/docs/AI协作指令_v2.md` | 📥 @import 自动加载 | — |
| `.claude/docs/笔记制作SOP.md` | 📥 @import 自动加载 | — |
| `.claude/docs/笔记检查清单.md` | 📥 @import 自动加载 | — |
| `.claude/docs/进阶能力清单.md` | 📖 手动 | 串讲、图片协作、链接修复等触发式技能 |
| `.claude/docs/用户指令与偏好记录.md` | 📖 手动 | 不理解"为什么"时 |
| `.claude/docs/源文件清单.md` | 📖 手动 | 开始新课程前，了解有哪些源文件 |
| `.claude/docs/术语登记表.md` | 📖 手动 | 建笔记前查重，避免跨课程建重复 |
| `.claude/docs/知识库整理方案.md` | 📖 手动 | 跨课程/去重时 |
| `.claude/docs/问题解决与标准化.md` | 📖 手动 | 遇到报错时 |
| `.claude/docs/变更日志.md` | 📖 手动 | 想知道改了什么时 |
| `.claude/docs/模板版本.md` | 📖 手动 | 怀疑旧笔记模板不一致时 |
| `.claude/docs/课程毕业标准.md` | 📖 手动 | 章节/课程完成前自检 |
| `.claude/docs/会话收尾更新清单.md` | 📖 手动 | 人类说"更新你要更新的"时 |
| `.claude/docs/人机协作模式手册.md` | 📖 手动 | 遇到新的协作场景不确定怎么分工时 |
