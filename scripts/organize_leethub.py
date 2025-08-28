import os, re, shutil, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEST_DIR = ROOT / "solutions"
RAW_DIR = ROOT / ".raw"   # nơi gom rác

SAFE_SKIP = {".git", ".github", "scripts", "solutions", ".cache", ".venv", ".raw"}

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
    re.compile(r"(?P<slug>[A-Za-z][\w\s-]+)"),
]

def slugify(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s or "solution"

def parse_name(p: pathlib.Path):
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

def move_solutions():
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    moved = 0
    raw_moved = 0
    for dirpath, _, files in os.walk(ROOT):
        path_norm = pathlib.Path(dirpath)
        name = path_norm.name
        if name in SAFE_SKIP or path_norm == ROOT:
            continue
        if any(seg in str(path_norm).replace("\\", "/") for seg in ("/solutions", "/scripts", "/.git", "/.github", "/.cache", "/.venv", "/.raw")):
            continue

        for fname in files:
            p = pathlib.Path(dirpath) / fname
            ext = p.suffix.lower()
            if ext in (".py", ".sql"):
                # move vào solutions/
                qid, slug = parse_name(p)
                dest = DEST_DIR / f"{qid}-{slug}{ext}"
                i = 1
                while dest.exists() and not os.path.samefile(p, dest):
                    dest = DEST_DIR / f"{qid}-{slug}__{i}{ext}"
                    i += 1
                shutil.move(str(p), str(dest))
                moved += 1
            else:
                # rác -> move vào .raw/
                rel = p.relative_to(ROOT)
                dest = RAW_DIR / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                try:
                    shutil.move(str(p), str(dest))
                    raw_moved += 1
                except Exception:
                    pass

        # nếu thư mục rỗng → bỏ
        try:
            pathlib.Path(dirpath).rmdir()
        except OSError:
            pass
    print(f"Moved {moved} solutions into solutions/, {raw_moved} leftover files into .raw/")

def main():
    move_solutions()

if __name__ == "__main__":
    main()
