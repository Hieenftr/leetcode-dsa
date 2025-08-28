import re, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
SOL = {
    "python": ROOT / "solutions" / "python",
    "sql":    ROOT / "solutions" / "sql",
}

LANG_LABEL = {"python": "Python", "sql": "SQL"}

def iter_entries():
    entries = {}
    for lang, folder in SOL.items():
        if not folder.exists(): 
            continue
        for f in sorted(folder.iterdir()):
            if not f.is_file(): 
                continue
            m = re.match(r"(\d+)-(.+)\.(\w+)$", f.name)
            if not m: 
                continue
            pid = int(m.group(1))
            slug = m.group(2)
            title = slug.replace("-", " ").title()
            key = (pid, title)
            link = f"[{LANG_LABEL[lang]}]({f.as_posix()})"
            if key not in entries:
                entries[key] = {"id": pid, "title": title, "solutions": [link]}
            else:
                entries[key]["solutions"].append(link)
    return entries

def build_table():
    entries = iter_entries()
    rows = []
    for (pid, title) in sorted(entries.keys()):
        slug = title.lower().replace(" ", "-")
        title_md = f"[{title}](https://leetcode.com/problems/{slug}/)"
        sol_md = " · ".join(entries[(pid, title)]["solutions"])
        rows.append(f"| {pid:04d} | {title_md} | {sol_md} | - | - |")
    header = "| No.  | Title | Solution | Acceptance | Difficulty |\n|------|-------|----------|------------|------------|"
    return "\n".join([header] + rows)

def main():
    table = build_table()
    md = README.read_text(encoding="utf-8")
    new = re.sub(r"(<!-- TABLE_START -->)(.*?)(<!-- TABLE_END -->)",
                 r"\1\n" + table + r"\n\3", md, flags=re.S)
    README.write_text(new, encoding="utf-8")
    print("README updated.")

if __name__ == "__main__":
    main()
