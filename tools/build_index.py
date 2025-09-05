from __future__ import annotations
import re
import sys
from pathlib import Path
from typing import List, Dict, Optional, Tuple

def clean_title(title: str) -> str:
    """
    Remove leading problem number like '20. ' or '394 ' from a title.
    Accepts optional dot and spaces.
    """
    return re.sub(r'^\s*\d+\s*\.?\s*', '', title).strip()

REPO_ROOT = Path(__file__).resolve().parents[1]
SOL_DIR = REPO_ROOT / "solutions"
README = REPO_ROOT / "README.md"

# Matches: solutions/s01_stack/lc_0020_valid_parentheses.py
FILE_GLOB = "s*/lc_*.py"

META_KEYS = ["Title", "Difficulty", "Tags", "Time", "Space"]
META_RE = re.compile(r"^\s*#\s*(Title|Difficulty|Tags|Time|Space)\s*:\s*(.*)$", re.IGNORECASE)

# Read up to this many lines at the top of each file to find metadata
SCAN_LINES = 40

INDEX_HEADER = (
    "| # | Title | Difficulty | Tags | Solution | Time | Space |\n"
    "|---|------|------------|------|---------|------|-------|\n"
)

START_MARK = "<!-- INDEX:START -->"
END_MARK = "<!-- INDEX:END -->"


def parse_problem_id_and_slug(path: Path) -> Tuple[int, str]:
    """Extract numeric id and slug from filename lc_XXXX_slug.py"""
    m = re.match(r"lc_(\d{1,4})_(.+)\.py$", path.name)
    if not m:
        raise ValueError(f"Unexpected solution filename: {path}")
    pid = int(m.group(1))
    slug = m.group(2).replace("_", "-")
    return pid, slug


def parse_metadata(path: Path) -> Dict[str, str]:
    meta: Dict[str, str] = {k: "" for k in META_KEYS}
    try:
        with path.open("r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                if i > SCAN_LINES:
                    break
                m = META_RE.match(line)
                if m:
                    key = m.group(1).title()
                    val = m.group(2).strip()
                    
                    if key == "Title":
                        val = clean_title(val)
                    # Normalize comma-separated tags
                    if key == "Tags":
                        parts = [t.strip() for t in re.split(r"[,/;]", val) if t.strip()]
                        val = ", ".join(parts)
                    meta[key] = val
                # Stop early if we've filled everything
                if all(meta[k] for k in META_KEYS):
                    break
    except Exception:
        pass
    return meta


def build_table_rows() -> List[str]:
    rows: List[str] = []
    files = sorted(SOL_DIR.glob(FILE_GLOB))
    items = []
    for p in files:
        try:
            pid, slug = parse_problem_id_and_slug(p)
        except ValueError:
            # Ignore unknown file naming
            continue
        meta = parse_metadata(p)
        title = clean_title(meta["Title"] or slug.replace("-", " ").title())
        diff = meta["Difficulty"] or "-"
        tags = meta["Tags"] or "-"
        time_c = meta["Time"] or "-"
        space_c = meta["Space"] or "-"
        rel = p.relative_to(REPO_ROOT).as_posix()
        link = f"[{p.name}]({rel})"
        items.append((pid, title, diff, tags, link, time_c, space_c))

    # sort by problem id
    items.sort(key=lambda x: x[0])
    for pid, title, diff, tags, link, time_c, space_c in items:
        rows.append(f"| {pid} | {title} | {diff} | {tags} | {link} | {time_c} | {space_c} |\n")
    return rows


def render_index_table() -> str:
    return INDEX_HEADER + "".join(build_table_rows())


def replace_index_in_readme(readme_text: str, table: str) -> str:
    """Replace section under '## Index' until next '## ' heading or markers."""
    # If markers exist, replace between them
    if START_MARK in readme_text and END_MARK in readme_text:
        return re.sub(
            rf"{re.escape(START_MARK)}[\s\S]*?{re.escape(END_MARK)}",
            f"{START_MARK}\n\n{table}\n{END_MARK}",
            readme_text,
            count=1,
        )

    # Else, find '## Index' heading
    idx = re.search(r"^##\s+Index\s*$", readme_text, flags=re.MULTILINE)
    if not idx:
        # No index heading — append at end with markers
        return readme_text.rstrip() + "\n\n## Index\n\n" + START_MARK + "\n\n" + table + "\n" + END_MARK + "\n"

    start = idx.end()
    # Find next level-2 heading after Index
    m = re.search(r"^##\s+", readme_text[start:], flags=re.MULTILINE)
    if m:
        end = start + m.start()
    else:
        end = len(readme_text)

    new_block = "\n\n" + START_MARK + "\n\n" + table + "\n" + END_MARK + "\n\n"
    return readme_text[:start] + new_block + readme_text[end:]


def main() -> int:
    if not SOL_DIR.exists():
        print(f"Solutions directory not found: {SOL_DIR}")
        return 1

    table = render_index_table()
    print("Generated table:\n\n" + table)

    if not README.exists():
        print(f"README not found at {README}; creating a basic one.")
        README.write_text("# LeetCode & DSA\n\n## Index\n\n" + START_MARK + "\n\n" + table + "\n" + END_MARK + "\n", encoding="utf-8")
        return 0

    text = README.read_text(encoding="utf-8")
    new_text = replace_index_in_readme(text, table)
    if new_text != text:
        README.write_text(new_text, encoding="utf-8")
        print("README.md updated ✅")
    else:
        print("README.md unchanged (no Index section found/changed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
