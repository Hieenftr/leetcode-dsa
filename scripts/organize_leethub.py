import os, re, shutil, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEST_DIR = ROOT / "solutions"
RAW_DIR  = ROOT / ".raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

SKIP_PREFIXES = (".git", ".github", "scripts", "solutions", ".cache", ".venv", ".raw")
SAFE_ROOT_FILES = {"README.md", ".gitignore", "stats.json"}  # giữ nguyên ở root

# ---------- helpers ----------
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

_PATTERNS = [
    re.compile(r"(?P<id>\d{1,5})[.\s_-]+(?P<slug>[A-Za-z][\w\s-]+)"),
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
        for pat in _PATTERNS:
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

def looks_like_leethub_dir(dirname: str) -> bool:
    return bool(re.match(r"^\d{3,5}([\-_.\s].+)?$", dirname))

def looks_like_solution_filename(name: str) -> bool:
    return bool(re.match(r"^\d{3,5}-[a-z0-9\-]+\.(py|sql)$", name, re.I))

# ---------- core movers ----------
def move_candidate_file(p: pathlib.Path) -> bool:
    """Move 1 file .py/.sql hợp lệ vào solutions/. Trả về True nếu đã move."""
    ext = p.suffix.lower()
    if ext not in (".py", ".sql"):
        return False
    has_id, has_title = extract_from_header(p)
    is_solution_name = looks_like_solution_filename(p.name)
    in_leethub_dir = looks_like_leethub_dir(p.parent.name)
    if not (in_leethub_dir or has_id or has_title or is_solution_name):
        return False
    qid, slug = parse_name(p)
    dest = DEST_DIR / f"{qid}-{slug}{ext}"
    i = 1
    while dest.exists() and not os.path.samefile(p, dest):
        dest = DEST_DIR / f"{qid}-{slug}__{i}{ext}"
        i += 1
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(p), str(dest))
    return True

def hoist_legacy_subdirs():
    """Kéo mọi file hợp lệ trong solutions/python & solutions/sql lên thẳng solutions/."""
    moved = 0
    for sub in ("python", "sql"):
        d = DEST_DIR / sub
        if not d.exists():
            continue
        for f in list(d.glob("*")):
            if f.is_file() and f.suffix.lower() in (".py", ".sql"):
                # đặt tên lại chuẩn nếu cần
                if looks_like_solution_filename(f.name):
                    dest = DEST_DIR / f.name
                else:
                    qid, slug = parse_name(f)
                    dest = DEST_DIR / f"{qid}-{slug}{f.suffix.lower()}"
                i = 1
                while dest.exists() and not os.path.samefile(f, dest):
                    dest = DEST_DIR / f"{dest.stem}__{i}{dest.suffix}"
                    i += 1
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(f), str(dest))
                moved += 1
        # xóa thư mục nếu trống
        try:
            d.rmdir()
        except OSError:
            pass
    return moved

def move_solutions_flat():
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    moved, archived = 0, 0

    # 1) Quét toàn repo (cắt tỉa nhánh skip)
    for dirpath, dirnames, filenames in os.walk(ROOT, topdown=True):
        rel = pathlib.Path(dirpath).relative_to(ROOT).as_posix()
        dirnames[:] = [d for d in dirnames
                       if not any((rel + "/" + d).startswith(skip) or d == skip
                                  for skip in SKIP_PREFIXES)]
        dpath = pathlib.Path(dirpath)

        for fname in filenames:
            # giữ nguyên file quan trọng ở root
            if dpath == ROOT and fname in SAFE_ROOT_FILES:
                continue

            p = dpath / fname
            # 1a) nếu là solution hợp lệ -> move vào solutions/
            if move_candidate_file(p):
                moved += 1
                continue

            # 1b) còn lại -> archive vào .raw/
            rel_file = p.relative_to(ROOT)
            raw_dest = RAW_DIR / rel_file
            raw_dest.parent.mkdir(parents=True, exist_ok=True)
            try:
                shutil.move(str(p), str(raw_dest))
                archived += 1
            except Exception:
                pass

        # dọn thư mục rỗng
        try:
            dpath.rmdir()
        except OSError:
            pass

    # 2) Kéo mọi thứ còn trong solutions/python & solutions/sql lên thẳng solutions/
    moved += hoist_legacy_subdirs()

    print(f"[organize] moved {moved} solutions into solutions/, archived {archived} leftovers into .raw/")

def main():
    move_solutions_flat()

if __name__ == "__main__":
    main()
