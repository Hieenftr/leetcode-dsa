import re, json, time, pathlib, requests, collections

ROOT = pathlib.Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
SOL_DIR = ROOT / "solutions"

CACHE_DIR = ROOT / ".cache"
CACHE_FILE = CACHE_DIR / "leetcode_meta.json"
CACHE_DIR.mkdir(exist_ok=True)

API_URL = "https://leetcode.com/graphql"
HEADERS = {"Content-Type": "application/json"}

# ----------------- utilities -----------------
def read_header_fields(path: pathlib.Path):
    """Parse Title/Time/Space/Tags from first ~40 lines."""
    title = time_c = space_c = ""
    tags = []
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            head = "".join([next(f) for _ in range(40)])
    except Exception:
        head = ""
    m_title = re.search(r"^\s*(?:#|--)?\s*Title:\s*([^\n\r]+)", head, re.I | re.M)
    m_time  = re.search(r"^\s*(?:#|--)?\s*Time:\s*([^\n\r]+)", head, re.I | re.M)
    m_space = re.search(r"^\s*(?:#|--)?\s*Space:\s*([^\n\r]+)", head, re.I | re.M)
    m_tags  = re.search(r"^\s*(?:#|--)?\s*Tags?:\s*([^\n\r]+)", head, re.I | re.M)
    if m_title: title = m_title.group(1).strip()
    if m_time:  time_c = m_time.group(1).strip()
    if m_space: space_c = m_space.group(1).strip()
    if m_tags:
        tags = [t.strip() for t in re.split(r"[,/]", m_tags.group(1)) if t.strip()]
    return title, time_c, space_c, tags

def load_cache():
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}

def save_cache(cache):
    CACHE_FILE.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")

def fetch_meta_from_leetcode(slug, backoff=1.0, retries=3):
    query = {
        "query": """
        query getQuestion($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            questionId
            title
            difficulty
            stats
          }
        }""",
        "variables": {"titleSlug": slug},
    }
    for _ in range(retries):
        try:
            r = requests.post(API_URL, json=query, headers=HEADERS, timeout=10)
            r.raise_for_status()
            data = r.json().get("data", {}).get("question")
            if not data:
                return None
            stats = json.loads(data.get("stats", "{}"))
            ac = stats.get("acRate", None)
            try:
                ac_str = f"{float(ac):.1f}%"
            except Exception:
                ac_str = "-"
            return {
                "id": str(data.get("questionId") or "").strip(),
                "title": data.get("title") or slug.replace("-", " ").title(),
                "difficulty": data.get("difficulty") or "-",
                "acceptance": ac_str,
            }
        except requests.RequestException:
            time.sleep(backoff)
            backoff *= 2
    return None

def get_meta(slug, cache):
    if slug in cache:
        return cache[slug]
    meta = fetch_meta_from_leetcode(slug)
    if meta:
        cache[slug] = meta
        save_cache(cache)
    return meta

# ----------------- build entries -----------------
def collect_entries():
    """
    Return:
      entries_by_key[(id, slug)] = {
        "id": int, "slug": str, "title": str, "files": {"py": path, "sql": path},
        "time": str, "space": str, "tags": [..],
        "acceptance": str, "difficulty": str
      }
    """
    cache = load_cache()
    entries = {}
    if not SOL_DIR.exists():
        return entries
    for f in sorted(SOL_DIR.iterdir()):
        if not f.is_file() or f.suffix.lower() not in (".py", ".sql"):
            continue
        m = re.match(r"(\d+)-(.+)\.(py|sql)$", f.name, re.I)
        if not m:
            continue
        pid = int(m.group(1))
        slug = m.group(2).lower()
        ext = m.group(3).lower()
        title_h, time_h, space_h, tags_h = read_header_fields(f)
        key = (pid, slug)
        if key not in entries:
            # GraphQL metadata
            meta = get_meta(slug, cache) or {}
            entries[key] = {
                "id": int(meta.get("id") or pid),
                "slug": slug,
                "title": meta.get("title") or title_h or slug.replace("-", " ").title(),
                "files": {},
                "time": time_h,
                "space": space_h,
                "tags": tags_h[:],
                "acceptance": meta.get("acceptance", "-"),
                "difficulty": meta.get("difficulty", "-"),
            }
        else:
            # prefer any missing time/space/tags from other file
            if not entries[key]["time"] and time_h: entries[key]["time"] = time_h
            if not entries[key]["space"] and space_h: entries[key]["space"] = space_h
            entries[key]["tags"].extend([t for t in tags_h if t not in entries[key]["tags"]])
        entries[key]["files"][ext] = f
    return entries

# ----------------- sections -----------------
def build_badges(entries):
    solved = len(entries)
    badges = [
        f"![language](https://img.shields.io/badge/language-Python%20%2F%20SQL-orange)",
        f"![license](https://img.shields.io/badge/license-MIT-blue)",
        f"![update](https://img.shields.io/badge/update-weekly-brightgreen)",
        f"![solved](https://img.shields.io/badge/solved-{solved}-informational)",
        f"![visitors](https://komarev.com/ghpvc/?username=Hieenftr&repo=leetcode-dsa&style=flat)",
    ]
    return " ".join(badges)

def build_table(entries):
    header = "| No.  | Title | Solution | Acceptance | Difficulty | Time | Space |\n" \
             "|------|-------|----------|------------|------------|------|-------|"
    rows = []
    for key in sorted(entries.keys(), key=lambda k: entries[k]["id"]):
        e = entries[key]
        slug = e["slug"]
        title_md = f"[{e['title']}](https://leetcode.com/problems/{slug}/)"
        sols = []
        if "py" in e["files"]:
            sols.append(f"[Python]({e['files']['py'].as_posix()})")
        if "sql" in e["files"]:
            sols.append(f"[SQL]({e['files']['sql'].as_posix()})")
        sol_md = " · ".join(sols)
        rows.append(f"| {e['id']:04d} | {title_md} | {sol_md} | {e['acceptance']} | {e['difficulty']} | {e['time'] or '-'} | {e['space'] or '-'} |")
    return "\n".join([header] + rows)

def build_topics(entries):
    # gom theo tag (từ header file)
    tags = collections.defaultdict(list)
    for e in entries.values():
        for t in e["tags"]:
            tags[t].append((e["id"], e["title"], e["slug"]))
    if not tags:
        return "_Add `Tags:` lines in file headers to populate this section._"
    # sắp xếp tag theo alphabet
    out = []
    for tag in sorted(tags.keys(), key=str.lower):
        out.append(f"### {tag}")
        items = []
        for pid, title, slug in sorted(tags[tag], key=lambda x: x[0]):
            items.append(f"- [{pid:04d} · {title}](https://leetcode.com/problems/{slug}/)")
        out.append("\n".join(items))
        out.append("")  # blank line
    return "\n".join(out)

def patch_readme(section_marker_start, section_marker_end, content):
    md = README.read_text(encoding="utf-8")
    new = re.sub(
        rf"({re.escape(section_marker_start)})(.*?){re.escape(section_marker_end)}",
        rf"\1\n{content}\n{section_marker_end}",
        md, flags=re.S
    )
    README.write_text(new, encoding="utf-8")

def main():
    entries = collect_entries()
    # badges
    patch_readme("<!-- BADGES_START -->", "<!-- BADGES_END -->", build_badges(entries))
    # table
    patch_readme("<!-- TABLE_START -->", "<!-- TABLE_END -->", build_table(entries))
    # topics
    patch_readme("<!-- TOPICS_START -->", "<!-- TOPICS_END -->", build_topics(entries))
    print("README updated (badges + table + topics).")

if __name__ == "__main__":
    main()
