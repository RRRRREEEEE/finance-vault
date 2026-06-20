# Always-On Rules

> 每次对话自动加载。放最核心、最容易忘、犯错代价最大的规则。

## 红线（违反重来）

1. 🚫 **不扩展知识** — 只写原文，不补维基/AI知识
2. 🚫 **不编造数据/公式/链接** — 不确定标 TODO
3. 🚫 **不自己画图** — 图片来自课件原文件（PPTX→COM导出，PDF→PyMuPDF渲染）
4. 🚫 **不修改源文件** — `D:\.pogget\...` 下文件绝不碰
5. 🚫 **不合并知识点** — 一页一文件，宁可碎
6. 🚫 **不标注考试重点** — 人类自己写
7. 🚫 **笔记不进 Inbox** — 直接放课程章节文件夹

## Git 版本管理

### 版本号规则
- 当前基线：**v2.0**（第二版）
- 人类说"更新" = **小版本**（v2.0 → v2.1 → v2.2…）
- 人类说"大版本" = **大版本**（v2.x → v3.0）
- 注意：`模板版本.md` 的 v2.4 是**笔记模板格式**的版本号，和项目 git tag 是两套独立的版本体系

### 每次收尾
```bash
git add -A
git commit -m "vX.Y.Z · {一句话概括}"
git tag "vX.Y.Z"
git push --follow-tags
```

### 分支策略
- 非平凡改动（合并文档/重构规则/批量修改笔记）→ 先 `git checkout -b feature/xxx`
- 搞砸了 → `git checkout master` 回滚，删分支
- 做对了 → merge 回 master + push
- 日常笔记生成/章节处理 → 直接在 master 提交（不打分支）

### 仓库
- `github.com/RRRRREEEEE/finance-vault`（SSH 协议，无需梯子）

## 每次必须

- 建笔记前 Grep/Glob 搜全 Vault 去重
- 凡提到的概念都建笔记（1句话也行，importance `"*"`）
- importance 加引号：`"****"` 不是 `****`
- 图片描述性命名：`{课程}Ch{XX} {描述}.png`
- 每批完立即更新 `阅读进度.json`
- 整章完跑 `笔记检查清单.md`
