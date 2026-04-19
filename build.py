#!/usr/bin/env python3
"""
Portfolio build script.
Scans content/*/index.md, parses frontmatter and H2 headings,
groups by section → tag → date, and outputs projects.json.

Run: python build.py
"""

import os
import json
import re
from pathlib import Path

# ── Configuration ────────────────────────────────────────────────────────────
# Edit these lists to add, remove, or reorder tags within each section.
# Projects with tags not listed here will be appended at the end in the order
# they are encountered.

TAG_ORDER = {
    "project":      ["employment", "competitive", "school", "freelance"],
    "mini-project": ["led_art", "bicycles", "fabrication"],
    "adventure":    [],
}

# ── Frontmatter parser ────────────────────────────────────────────────────────

def parse_frontmatter(text):
    """Return (meta_dict, body_str) from a markdown string with YAML frontmatter."""
    if not text.startswith("---"):
        return {}, text

    # Find closing ---
    end = text.find("---", 3)
    if end == -1:
        return {}, text

    yaml_block = text[3:end].strip()
    body = text[end + 3:].strip()
    meta = parse_simple_yaml(yaml_block)
    return meta, body


def parse_simple_yaml(text):
    """Minimal YAML parser supporting strings, lists, booleans, ints, null."""
    result = {}
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.strip().startswith("#"):
            i += 1
            continue

        # key: value or key: [inline list]
        match = re.match(r'^(\w[\w\-]*)\s*:\s*(.*)', line)
        if not match:
            i += 1
            continue

        key = match.group(1)
        val = match.group(2).strip()

        # Inline list: [a, b, c]
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1]
            items = [x.strip().strip("\"'") for x in inner.split(",")]
            result[key] = [x for x in items if x]

        # Multi-line list (lines starting with -)
        elif val == "":
            sub = []
            i += 1
            while i < len(lines) and lines[i].startswith("  - "):
                sub.append(lines[i].strip().lstrip("- ").strip("\"'"))
                i += 1
            result[key] = sub
            continue

        elif val.lower() == "true":
            result[key] = True
        elif val.lower() == "false":
            result[key] = False
        elif val.lower() in ("null", "~", ""):
            result[key] = None
        else:
            # Strip surrounding quotes
            if (val.startswith('"') and val.endswith('"')) or \
               (val.startswith("'") and val.endswith("'")):
                val = val[1:-1]
            else:
                # Try integer
                try:
                    val = int(val)
                except ValueError:
                    pass
            result[key] = val

        i += 1
    return result


# ── Markdown heading extractor ────────────────────────────────────────────────

def extract_h2_headings(body):
    """Return list of H2 heading text strings from markdown body."""
    headings = []
    for line in body.split("\n"):
        m = re.match(r'^##\s+(.+)', line)
        if m:
            headings.append(m.group(1).strip())
    return headings


# ── Slug helper for anchor IDs ────────────────────────────────────────────────

def make_anchor(text):
    """Convert heading text to a URL-safe anchor id."""
    return re.sub(r'[^\w\-]', '-', text.lower()).strip('-')


# ── Date sorting key ──────────────────────────────────────────────────────────

def date_sort_key(project):
    """Return a sortable tuple from date_start (YYYY-MM or YYYY). Higher = newer."""
    ds = str(project.get("date_start") or "0000")
    parts = ds.split("-")
    year = int(parts[0]) if parts[0].isdigit() else 0
    month = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 0
    return (year, month)


# ── Main build ────────────────────────────────────────────────────────────────

def build():
    content_dir = Path("content")
    if not content_dir.exists():
        print("Error: 'content/' directory not found. Run from repo root.")
        return

    projects = []

    for project_dir in sorted(content_dir.iterdir()):
        index_file = project_dir / "index.md"
        if not project_dir.is_dir() or not index_file.exists():
            continue

        text = index_file.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)

        if not meta:
            print(f"  Skipping {project_dir.name}: no frontmatter")
            continue

        slug = project_dir.name
        section = meta.get("section")
        if not section:
            print(f"  Skipping {slug}: no 'section' field")
            continue

        tags = meta.get("tags") or []
        if isinstance(tags, str):
            tags = [tags]

        headings = extract_h2_headings(body)
        heading_anchors = [
            {"text": h, "anchor": f"{slug}-{make_anchor(h)}"}
            for h in headings
        ]

        # Collect images from content/{slug}/images/
        image_exts = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}
        images_dir = project_dir / "images"
        images = []
        if images_dir.is_dir():
            for f in sorted(images_dir.iterdir()):
                if f.suffix.lower() in image_exts:
                    images.append(f"content/{slug}/images/{f.name}")

        projects.append({
            "slug":        slug,
            "title":       meta.get("title") or slug,
            "thumbnail":   meta.get("thumbnail"),
            "caption":     meta.get("caption") or "",
            "section":     section,
            "tags":        tags,
            "employer":    meta.get("employer"),
            "date_start":  str(meta.get("date_start") or ""),
            "date_end":    str(meta.get("date_end") or ""),
            "order":       meta.get("order") or 999,
            "visible":     meta.get("visible", True),
            "headings":    heading_anchors,
            "images":      images,
        })

    # Group by section → tag
    output = {}
    sections = list(TAG_ORDER.keys())
    # Collect any sections found in content that aren't in TAG_ORDER
    for p in projects:
        if p["section"] not in output:
            output[p["section"]] = {}

    for section_name, groups in output.items():
        canonical_tags = TAG_ORDER.get(section_name, [])
        section_projects = [p for p in projects if p["section"] == section_name]

        # Gather all tags in canonical order, then any extras
        all_tags = list(canonical_tags)
        for p in section_projects:
            for t in p["tags"]:
                if t not in all_tags:
                    all_tags.append(t)

        for tag in all_tags:
            tagged = [p for p in section_projects if tag in p["tags"]]
            tagged.sort(key=date_sort_key, reverse=True)
            if tagged:
                groups[tag] = tagged

        # Projects with no matching tag go into an "other" bucket
        tagged_slugs = {p["slug"] for tag_list in groups.values() for p in tag_list}
        others = [p for p in section_projects if p["slug"] not in tagged_slugs]
        others.sort(key=date_sort_key, reverse=True)
        if others:
            groups["other"] = others

        output[section_name] = {
            "tag_order": all_tags,
            "groups": groups,
        }

    # Thumbnail strip order: visible projects per section, sorted by order field
    for section_name, data in output.items():
        all_in_section = [p for p in projects if p["section"] == section_name]
        strip = [p for p in all_in_section if p.get("visible")]
        strip.sort(key=lambda p: p.get("order") or 999)
        data["thumbnail_strip"] = strip

    out_path = Path("projects.json")
    out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Built {out_path} with {len(projects)} projects across {len(output)} sections.")

    for section_name, data in output.items():
        total = sum(len(v) for v in data["groups"].values())
        print(f"  {section_name}: {total} projects in {list(data['groups'].keys())}")


if __name__ == "__main__":
    build()
