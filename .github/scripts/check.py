#!/usr/bin/env python3
"""
Vault 质检脚本 — 自动检查 Obsidian 笔记库的常见问题。

用法：
    .venv/Scripts/python check_vault.py              # 检查全部
    .venv/Scripts/python check_vault.py --course 货币金融学  # 只查某课程
    .venv/Scripts/python check_vault.py --json       # JSON 输出（供其他工具调用）

检查项：
    1. importance 是否加了引号
    2. TODO: 截图替换 / TODO: 原文模糊 残留
    3. [[wiki链接]] 目标是否存在（含 alias 解析）
    4. ![[图片]] 引用是否对应真实文件
    5. frontmatter 必填字段是否齐全
    6. aliases 是否跨文件冲突
    7. 图片文件是否被引用（孤儿图片检测）
"""

import os
import sys
import re
import json
import argparse

# Windows 终端编码修复
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from pathlib import Path
from collections import defaultdict
from datetime import datetime

import yaml

VAULT = Path.cwd()  # CI 环境中 cwd 即仓库根目录；本地运行可手动改路径
ATTACHMENTS = VAULT / "999-Attachments"
IGNORE_DIRS = {".obsidian", ".trash", "999-Attachments", "900-跨课程枢纽"}

# 必填 frontmatter 字段
REQUIRED_FM_FIELDS = ["tags", "courses", "aliases", "created", "source", "chapter", "importance"]


# ── 工具函数 ──────────────────────────────────────────

def parse_frontmatter(text: str):
    """从 md 文本中提取 YAML frontmatter。返回 (dict, raw_yaml_str, error_msg)"""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return None, None, "无 frontmatter"
    raw = m.group(1)
    try:
        fm = yaml.safe_load(raw)
        if not isinstance(fm, dict):
            return None, raw, "frontmatter 不是有效的 YAML 字典"
        return fm, raw, None
    except yaml.YAMLError as e:
        return None, raw, f"YAML 解析错误: {e}"


def importance_quoted_check(raw_yaml: str):
    """检查 importance 是否用引号包裹。返回 True=正确引号, False=缺少引号, None=无importance字段"""
    m = re.search(r"^importance:\s*(.+?)\s*$", raw_yaml, re.MULTILINE)
    if not m:
        return None  # 没有 importance 字段
    val = m.group(1)
    if val.startswith('"') and val.endswith('"'):
        return True
    if val.startswith("'") and val.endswith("'"):
        return True
    return False


def resolve_link_target(target: str, filenames: set, aliases_map: dict):
    """检查 [[target]] 是否有对应文件。返回 (found_file, is_alias_match)"""
    # [[target|display]] → target 是实际目标
    target = target.split("|")[0].strip()
    # 去掉可能的路径前缀
    target_name = target.split("/")[-1]
    # 可能包含 .md 扩展名
    if target_name.endswith(".md"):
        target_name = target_name[:-3]

    # 1. 精确匹配文件名
    if target_name in filenames:
        return True, False

    # 2. 去掉英文部分只留中文（处理 "English Chinese" → "Chinese"）
    # 3. alias 匹配
    if target_name in aliases_map:
        return True, True

    # 4. 模糊匹配：尝试把所有 alias 展开再搜
    #    （aliases_map 是 alias → set of filenames）
    return False, False


def collect_vault_metadata(vault: Path):
    """扫描全 Vault，返回 (filenames, aliases_map, frontmatters, image_files)"""
    filenames = set()       # 不含 .md 的文件名
    aliases_map = {}        # alias → set of filenames
    frontmatters = {}       # relative_path → frontmatter dict
    all_md_files = []       # [(relative_path, full_text)]

    for root, dirs, files in os.walk(vault):
        # 跳过忽略目录
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith(".")]
        for f in files:
            if not f.endswith(".md"):
                continue
            fpath = Path(root) / f
            rel = fpath.relative_to(vault)
            filenames.add(fpath.stem)
            try:
                text = fpath.read_text(encoding="utf-8")
            except Exception:
                continue
            all_md_files.append((rel, text))

    for rel, text in all_md_files:
        fm, raw, err = parse_frontmatter(text)
        if fm:
            frontmatters[str(rel)] = fm
            # 收集 aliases
            aliases = fm.get("aliases", [])
            if isinstance(aliases, list):
                for a in aliases:
                    if isinstance(a, str) and a.strip():
                        a_clean = a.strip()
                        if a_clean not in aliases_map:
                            aliases_map[a_clean] = set()
                        aliases_map[a_clean].add(Path(rel).stem)
            elif isinstance(aliases, str):
                a_clean = aliases.strip()
                if a_clean:
                    if a_clean not in aliases_map:
                        aliases_map[a_clean] = set()
                    aliases_map[a_clean].add(Path(rel).stem)

    # 收集图片文件
    image_files = set()
    if ATTACHMENTS.exists():
        for f in ATTACHMENTS.iterdir():
            if f.is_file() and f.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp"}:
                image_files.add(f.name)

    return filenames, aliases_map, frontmatters, image_files, all_md_files


# ── 各检查项 ──────────────────────────────────────────

def check_importance_quotes(all_md_files) -> list:
    """检查 1: importance 是否加引号"""
    issues = []
    for rel, text in all_md_files:
        _, raw, err = parse_frontmatter(text)
        if err:
            continue
        if raw is None:
            continue
        result = importance_quoted_check(raw)
        if result is False:
            issues.append({"file": str(rel), "issue": "importance 缺少引号", "severity": "error"})
        elif result is None:
            issues.append({"file": str(rel), "issue": "缺少 importance 字段", "severity": "error"})
    return issues


def check_todo_residuals(all_md_files) -> list:
    """检查 2: TODO 残留"""
    issues = []
    patterns = {
        r"TODO:\s*截图替换": "残留 TODO: 截图替换",
        r"TODO:\s*原文模糊": "残留 TODO: 原文模糊",
    }
    for rel, text in all_md_files:
        for pat, desc in patterns.items():
            for m in re.finditer(pat, text):
                line = text[:m.start()].count("\n") + 1
                issues.append({"file": str(rel), "issue": f"{desc} (第{line}行)", "severity": "warning"})
    return issues


def check_wikilinks(all_md_files, filenames, aliases_map) -> list:
    """检查 3: [[wiki链接]] 目标是否存在"""
    issues = []
    # 过滤掉非笔记的内部链接模式
    ignore_patterns = [
        r"^https?://",  # URL
        r"^\d{4}-\d{2}-\d{2}",  # 日期
        r"^#",  # 内部标题链接
    ]

    for rel, text in all_md_files:
        links = re.findall(r"\[\[([^\]]+)\]\]", text)
        for link in links:
            target = link.split("|")[0].split("#")[0].strip()
            if not target:
                continue
            if any(re.match(pat, target) for pat in ignore_patterns):
                continue
            # 忽略图片链接（由 check_image_refs 处理）
            if target.startswith("999-Attachments/") or re.match(r".+\.(png|jpg|jpeg|gif|svg|webp|bmp)$", target, re.I):
                continue

            found, _ = resolve_link_target(target, filenames, aliases_map)
            if not found:
                issues.append({"file": str(rel), "issue": f"死链: [[{target}]]", "severity": "error"})
    return issues


def check_image_refs(all_md_files, image_files) -> list:
    """检查 4: ![[图片]] 引用是否存在 + 孤儿图片"""
    issues = []
    referenced_images = set()

    for rel, text in all_md_files:
        img_refs = re.findall(r"!\[\[([^\]]+)\]\]", text)
        for ref in img_refs:
            # 提取文件名（去掉路径）
            fname = ref.split("/")[-1].strip()
            referenced_images.add(fname)
            if fname not in image_files:
                issues.append({"file": str(rel), "issue": f"图片缺失: ![[{ref}]]", "severity": "error"})

    # 孤儿图片
    for img in sorted(image_files - referenced_images):
        # 排除系统文件和临时文件
        if img.startswith("_") or img.startswith("Pasted image"):
            continue
        issues.append({"file": f"999-Attachments/{img}", "issue": "孤儿图片: 未被任何笔记引用", "severity": "warning"})

    return issues


def check_frontmatter_fields(all_md_files) -> list:
    """检查 5: frontmatter 必填字段"""
    issues = []
    for rel, text in all_md_files:
        fm, raw, err = parse_frontmatter(text)
        if err:
            # 跳过无 frontmatter 的文件（可能是章节索引等）
            continue
        if fm is None:
            continue
        for field in REQUIRED_FM_FIELDS:
            if field not in fm or fm[field] is None:
                issues.append({"file": str(rel), "issue": f"缺少必填字段: {field}", "severity": "error"})
                continue
            # 检查空值
            val = fm[field]
            if isinstance(val, str) and not val.strip():
                issues.append({"file": str(rel), "issue": f"必填字段为空: {field}", "severity": "warning"})
            elif isinstance(val, list) and len(val) == 0:
                issues.append({"file": str(rel), "issue": f"必填字段为空列表: {field}", "severity": "warning"})
    return issues


def check_alias_conflicts(frontmatters) -> list:
    """检查 6: aliases 跨文件冲突（同一个 alias 被多个笔记声明）"""
    issues = []
    alias_to_files = defaultdict(set)

    for rel, fm in frontmatters.items():
        aliases = fm.get("aliases", [])
        if isinstance(aliases, str):
            aliases = [aliases]
        if not isinstance(aliases, list):
            continue
        for a in aliases:
            if isinstance(a, str) and a.strip():
                alias_to_files[a.strip()].add(Path(rel).stem)

    for alias, files in alias_to_files.items():
        if len(files) > 1:
            issues.append({
                "issue": f"alias 冲突: \"{alias}\" → {sorted(files)}",
                "severity": "error",
            })

    return issues


def check_graduation_standards(all_md_files) -> list:
    """检查 8: 课程毕业标准 — 内容质量底线"""
    issues = []
    for rel, text in all_md_files:
        # 跳过非笔记文件（索引、考题、知识串讲）
        name = Path(rel).stem
        if any(kw in name for kw in ["知识串讲", "学习笔记", "概述", "术语索引", "总索引"]):
            continue

        # 1. 定义节有内容
        def_match = re.search(r"## 📌 定义\s*\n(.*?)(?=\n## |\n---|\Z)", text, re.DOTALL)
        if not def_match:
            issues.append({"file": str(rel), "issue": "缺少 📌 定义节", "severity": "warning"})
        elif len(def_match.group(1).strip()) < 10:
            issues.append({"file": str(rel), "issue": "📌 定义节内容过短 (<10字)", "severity": "warning"})

        # 2. 来源原文节有内容
        src_match = re.search(r"## 📄 来源原文\s*\n(.*?)(?=\n## |\n---|\Z)", text, re.DOTALL)
        if not src_match:
            issues.append({"file": str(rel), "issue": "缺少 📄 来源原文节", "severity": "warning"})
        elif len(src_match.group(1).strip()) < 5:
            issues.append({"file": str(rel), "issue": "📄 来源原文节为空", "severity": "warning"})

        # 3. 至少 1 个 wiki 链接（壳笔记 importance * 或 ** 忽略）
        fm, _, _ = parse_frontmatter(text)
        imp = fm.get("importance", "***") if fm else "***"
        if not re.search(r"\[\[[^\]]+\]\]", text):
            if imp not in ('"*"', '"**"', "*", "**"):
                issues.append({"file": str(rel), "issue": "无任何 [[wiki链接]]（非壳笔记应有至少 1 个链接）", "severity": "warning"})

    return issues


def check_image_naming(image_files) -> list:
    """检查 7: 图片命名是否合规（检测 hash 命名）"""
    issues = []
    hash_pattern = re.compile(r"^[a-f0-9]{8,}\.png$", re.I)
    for img in sorted(image_files):
        if hash_pattern.match(img):
            issues.append({"file": f"999-Attachments/{img}", "issue": "图片疑似 hash 命名，建议改为描述性名称", "severity": "warning"})
    return issues


# ── 主流程 ────────────────────────────────────────────

def run_checks(course_filter=None):
    print("🔍 扫描 Vault ...")
    filenames, aliases_map, frontmatters, image_files, all_md_files = collect_vault_metadata(VAULT)

    # 过滤课程
    if course_filter:
        course_pattern = f"{course_filter}"
        all_md_files = [(rel, text) for rel, text in all_md_files if course_pattern in str(rel)]
        frontmatters = {rel: fm for rel, fm in frontmatters.items() if course_pattern in rel}
        print(f"📂 筛选课程: {course_filter} → {len(all_md_files)} 篇笔记\n")

    print(f"📊 总计 {len(all_md_files)} 篇笔记, {len(image_files)} 张图片\n")

    all_issues = []
    all_issues.extend(check_importance_quotes(all_md_files))
    all_issues.extend(check_todo_residuals(all_md_files))
    all_issues.extend(check_wikilinks(all_md_files, filenames, aliases_map))
    all_issues.extend(check_image_refs(all_md_files, image_files))
    all_issues.extend(check_frontmatter_fields(all_md_files))
    all_issues.extend(check_alias_conflicts(frontmatters))
    all_issues.extend(check_image_naming(image_files))
    all_issues.extend(check_graduation_standards(all_md_files))

    return all_issues, len(all_md_files), len(image_files)


def print_report(issues, note_count, image_count):
    errors = [i for i in issues if i["severity"] == "error"]
    warnings = [i for i in issues if i["severity"] == "warning"]

    # 按文件分组
    by_file = defaultdict(list)
    for i in issues:
        fname = i.get("file", "(全局)")
        by_file[fname].append(i)

    print(f"{'─'*60}")
    print(f"📋 质检报告 — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'─'*60}")
    print(f"笔记: {note_count} 篇  |  图片: {image_count} 张")
    print(f"❌ 错误: {len(errors)}  |  ⚠️ 警告: {len(warnings)}")
    print()

    if not issues:
        print("✅ 全部通过！")
        return

    for fname in sorted(by_file.keys()):
        file_issues = by_file[fname]
        print(f"📄 {fname}")
        for i in file_issues:
            icon = "❌" if i["severity"] == "error" else "⚠️"
            print(f"   {icon} {i['issue']}")
        print()

    # 汇总
    print(f"{'─'*60}")
    issue_types = defaultdict(int)
    for i in issues:
        issue_types[i["issue"].split(":")[0].split(" ")[0]] += 1
    print("问题分类统计:")
    for k, v in sorted(issue_types.items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")
    print()
    if errors:
        print(f"🔴 {len(errors)} 个错误需要修复")
    if warnings:
        print(f"🟡 {len(warnings)} 个警告建议处理")


def main():
    parser = argparse.ArgumentParser(description="Vault 笔记质检")
    parser.add_argument("--course", type=str, help="筛选课程 (如: 货币金融学, 财政学)")
    parser.add_argument("--json", action="store_true", help="JSON 输出")
    args = parser.parse_args()

    issues, note_count, image_count = run_checks(args.course)

    if args.json:
        print(json.dumps({
            "timestamp": datetime.now().isoformat(),
            "note_count": note_count,
            "image_count": image_count,
            "error_count": len([i for i in issues if i["severity"] == "error"]),
            "warning_count": len([i for i in issues if i["severity"] == "warning"]),
            "issues": issues,
        }, ensure_ascii=False, indent=2))
    else:
        print_report(issues, note_count, image_count)


if __name__ == "__main__":
    main()
