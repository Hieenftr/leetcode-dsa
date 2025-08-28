import os, re, shutil, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEST = {
    ".py":  ROOT / "solutions" / "python",
    ".sql": ROOT / "solutions" / "sql",
}

# LeetHub thường có metadata trong comment: @lc id=..., @lc title=...
def extract_from_header(p: pathlib.Path):
    try:
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            head = "".join([next(f) for _ in range(40)])
    except Exception:
        return None, None
    m_id = re.search(r"@lc\s+id\s*=\s*(\d+)", head, re.I)
    m_title = re.search(r"@lc\s+title\s*=\s*([^\n\r]+)", head, re.I)
    qid = m_id.group(1) if m_id else None
    title = m_title.group(1).strip() if m_title else None
    return qid, title

PATTERNS = [
    re.compile(r"(?P<id>\d{1,4})[.\s_-]+(?P<slug>[A-Za-z][\w\s-]+)"),
    re.compile(r"(?P<slug>[A-Za-z][\w\s-]+)"),  # fallback
]

def slugify(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s or "solution"

def parse_name(p: pathlib.Path):
    # 1) ưu tiên header
    qid, title = extract_from_header(p)
    if title:
        slug = slugify(title)
    else:
        stem = p.stem
        slug = None
        qid_found = None
        for pat in PATTERNS:
            m = pat.search(stem)
            if m:
                qid_found = (m.groupdict().get("id") or "").zfill(4) if m.groupdict().get("id") else None
                raw = m.groupdict().get("slug") or stem
                slug = slugify(raw)
                break
        if qid is None:
            qid = qid_found
    qid = (qid or "0").zfill(4)
    slug = slug or "solution"
    return qid, slug

def main():
    moved = 0
    for d in DEST.values():
        d.mkdir(parents=True, exist_ok=True)

    for dirpath, _, files in os.walk(ROOT):
        path_norm = dirpath.replace("\\", "/")
        # bỏ qua các thư mục đích & hệ thống
        if any(skip in path_norm for skip in ("/solutions", "/scripts", "/.git", "/.github", "__pycache__")):
            continue
        for fname in files:
            p = pathlib.Path(dirpath) / fname
            ext = p.suffix.lower()
            if ext not in DEST:
                continue
            qid, slug = parse_name(p)
            dest_dir = DEST[ext]
            dest = dest_dir / f"{qid}-{slug}{ext}"
            i = 1
            while dest.exists() and not os.path.samefile(p, dest):
                dest = dest_dir / f"{qid}-{slug}__{i}{ext}"
                i += 1
            shutil.move(str(p), str(dest))
            moved += 1
    print(f"Moved {moved} files into solutions/python & solutions/sql")

if __name__ == "__main__":
    main()
