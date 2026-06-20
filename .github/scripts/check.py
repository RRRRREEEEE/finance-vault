#!/usr/bin/env python3
"""
Vault 质检 — GitHub Actions 版
检查当前目录下所有 .md 笔记的常见问题，输出 GitHub 注释格式。
"""
import os, re, sys, json
from pathlib import Path
from collections import defaultdict

try:
    import yaml
except ImportError:
    print("::error::pyyaml not installed")
    sys.exit(1)

VAULT = Path.cwd()
ATTACHMENTS = VAULT / "999-Attachments"

def parse_frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return None, None
    try:
        return yaml.safe_load(m.group(1)), m.group(1)
    except yaml.YAMLError:
        return None, m.group(1)

def importance_quoted(raw_yaml):
    if not raw_yaml:
        return None
    m = re.search(r"^importance:\s*(.+?)\s*$", raw_yaml, re.MULTILINE)
    if not m:
        return None
    val = m.group(1)
    return val.startswith('"') or val.startswith("'")

def check_note(rel_path, text, filenames, aliases_map, image_files):
    issues = []
    fm, raw = parse_frontmatter(text)

    # importance 引号
    r = importance_quoted(raw)
    if r is False:
        issues.append(("error", "importance 缺少引号"))
    elif r is None and fm:
        issues.append(("error", "缺少 importance 字段"))

    # TODO 残留
    for pat, desc in [(r"TODO:\s*截图替换", "残留 TODO: 截图替换")]:
        for m in re.finditer(pat, text):
            line = text[:m.start()].count("\n") + 1
            issues.append(("warning", f"{desc} (第{line}行)"))

    # 死链
    for link in re.findall(r"\[\[([^\]]+)\]\]", text):
        target = link.split("|")[0].split("#")[0].strip()
        if not target or target.startswith("http"):
            continue
        if re.match(r".+\.(png|jpg|jpeg|gif|svg|webp|bmp)$", target, re.I):
            continue
        target_name = target.split("/")[-1]
        if target_name.endswith(".md"):
            target_name = target_name[:-3]
        if target_name not in filenames and target_name not in aliases_map:
            issues.append(("error", f"死链: [[{target}]]"))

    # 图片引用
    for ref in re.findall(r"!\[\[([^\]]+)\]\]", text):
        fname = ref.split("/")[-1].strip()
        if fname not in image_files:
            issues.append(("error", f"图片缺失: ![[{ref}]]"))

    # frontmatter 必填字段
    if fm:
        for field in ["tags", "courses", "aliases", "created", "source", "chapter", "importance"]:
            if field not in fm or fm[field] is None:
                issues.append(("warning", f"缺少字段: {field}"))

    return issues

def main():
    filenames = set()
    aliases_map = defaultdict(set)
    image_files = set()
    all_notes = []

    # 收集元数据
    for f in VAULT.rglob("*.md"):
        if any(p.startswith(".") for p in f.relative_to(VAULT).parts):
            continue
        rel = str(f.relative_to(VAULT))
        filenames.add(f.stem)
        try:
            text = f.read_text(encoding="utf-8")
        except Exception:
            continue
        all_notes.append((rel, text))
        fm, _ = parse_frontmatter(text)
        if fm:
            aliases = fm.get("aliases", [])
            if isinstance(aliases, list):
                for a in aliases:
                    if isinstance(a, str) and a.strip():
                        aliases_map[a.strip()].add(f.stem)
            elif isinstance(aliases, str) and aliases.strip():
                aliases_map[aliases.strip()].add(f.stem)

    # 收集图片
    if ATTACHMENTS.exists():
        for f in ATTACHMENTS.iterdir():
            if f.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}:
                image_files.add(f.name)

    # 检查
    errors = 0
    warnings = 0
    for rel, text in all_notes:
        issues = check_note(rel, text, filenames, aliases_map, image_files)
        for severity, msg in issues:
            if severity == "error":
                errors += 1
                print(f"::error file={rel},title=质检::{msg}")
            else:
                warnings += 1
                print(f"::warning file={rel},title=质检::{msg}")

    # 孤儿图片
    referenced = set()
    for _, text in all_notes:
        for ref in re.findall(r"!\[\[([^\]]+)\]\]", text):
            referenced.add(ref.split("/")[-1].strip())
    for img in sorted(image_files - referenced):
        if not img.startswith("_") and not img.startswith("Pasted"):
            warnings += 1
            print(f"::warning file=999-Attachments/{img},title=质检::孤儿图片")

    print(f"\n📊 {len(all_notes)} 篇笔记 | ❌ {errors} | ⚠️ {warnings}")
    if errors > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()
