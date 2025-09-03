import re, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOL_DIR = ROOT / "solutions"
README = ROOT / "README.md"

row_tpl = "| {id} | {title} | {diff} | {tags} | {link} | {time} | {space} |\n"
pattern = re.compile(
    r"# Title:\s*(\d+)\.\s*(.+)\n"
    r"# Difficulty:\s*(.+)\n"
    r"# Tags:\s*(.+)\n"
    r"# Link:\s*(.+)\n"
    r"# Time:\s*(.+)\n"
    r"# Space:\s*(.+)"
)

rows = []
for py in SOL_DIR.rglob("solution.py"):
    text = py.read_text(encoding="utf-8", errors="ignore")
    m = pattern.search(text)
    if not m:
        continue
    pid, title, diff, tags, link, time_c, space_c = [g.strip() for g in m.groups()]
    rel = py.relative_to(ROOT).as_posix()
    rows.append(row_tpl.format(
        id=pid, title=title, diff=diff, tags=tags,
        link=f"[solution.py]({rel})", time=time_c, space=space_c
    ))

rows.sort(key=lambda r: int(r.split("|")[1].strip()))

with README.open("r", encoding="utf-8") as f:
    content = f.read()

start = content.find("| # | Title | Difficulty |")
end = content.find("\n\n## Conventions")
if start != -1 and end != -1 and end > start:
    header = content[:start]
    footer = content[end:]
    table_header = "| # | Title | Difficulty | Tags | Solution | Time | Space |\n|---|-------|------------|------|----------|------|-------|\n"
    new_table = table_header + "".join(rows)
    content = header + new_table + footer
    README.write_text(content, encoding="utf-8")
    print("README index updated.")
else:
    print("Could not locate index section anchors.")
