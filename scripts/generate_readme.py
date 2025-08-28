import re, json, time, pathlib, requests

ROOT = pathlib.Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
SOL = {
    "python": ROOT / "solutions" / "python",
    "sql":    ROOT / "solutions" / "sql",
}
LANG_LABEL = {"python": "Python", "sql": "SQL"}

CACHE_DIR = ROOT / ".cache"
CACHE_DIR.mkdir(exist_ok=True)
CACHE_FILE = CACHE_DIR / "leetcode_meta.json"

API_URL = "https://leetcode.com/graphql"
HEADERS = {"Content-Type": "application/json"}

# ----------------- Cache helpers -----------------
def load_cache():
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}

def save_cache(cache):
    CACHE_FILE.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")

# ----------------- API call -----------------
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
    for i in range(retries):
        try:
            r = requests.post(API_URL, json=query, headers=HEADERS, timeout=10)
            r.raise_for_status()
            data = r.json().get("data", {}).get("question")
            if not data:
                return None
            stats = json.loads(data.get("stats", "{}"))
            ac_rate = stats.get("acRate", None)
            if isinstance(ac_rate, (int, float, str)):
                try:
                    ac = f"{float(ac_rate):.1f}%"
                except Exception:
                    ac = "-"
            else:
                ac = "-"
            return {
                "questionId": str(data.get("questionId") or "").strip(),
                "title": data.get("title") or slug.replace("-", " ").title(),
                "difficulty": data.get("difficulty") or "-",
                "acceptance": ac,
            }
        except requests.RequestException:
            time.sleep(backoff)
            backoff *= 2
    return None

def get_meta(slug, cache):
    # return cached if any
    if slug in cache:
        return cache[slug]
    meta = fetch_meta_from_leetcode(slug)
    if meta:
        cache[slug] = meta
        save_cache(cache)
    return meta

# ----------------- Table build -----------------
def iter_entries():
    entries = {}
    for lang, folder in SOL.items():
        if not folder.exists():
            continue
        for f in sorted(folder.iterdir()):
            if not f.is_file():
                continue
            m = re.match(r"(\d+)-(.+)\.(py|sql)$", f.name, re.I)
            if not m:
                continue
            pid = int(m.group(1))
            slug = m.group(2)
            title_guess = slug.replace("-", " ").title()
            key = (pid, slug, title_guess)
            link = f"[{LANG_LABEL[lang]}]({f.as_posix()})"
            if key not in entries:
                entries[key] = {"id": pid, "slug": slug, "title_guess": title_guess, "solutions": [link]}
            else:
                entries[key]["solutions"].append(link)
    return entries

def build_table():
    cache = load_cache()
    entries = iter_entries()
    rows = []
    for (pid, slug, title_guess) in sorted(entries.keys()):
        meta = get_meta(slug, cache)
        if meta:
            title_md = f"[{meta['title']}](https://leetcode.com/problems/{slug}/)"
            difficulty = meta.get("difficulty", "-")
            acceptance = meta.get("acceptance", "-")
            shown_id = meta.get("questionId") or pid
        else:
            title_md = f"[{title_guess}](https://leetcode.com/problems/{slug}/)"
            difficulty = "-"
            acceptance = "-"
            shown_id = pid

        sol_md = " · ".join(entries[(pid, slug, title_guess)]["solutions"])
        rows.append(f"| {int(shown_id):04d} | {title_md} | {sol_md} | {acceptance} | {difficulty} |")

    header = "| No.  | Title | Solution | Acceptance | Difficulty |\n|------|-------|----------|------------|------------|"
    return "\n".join([header] + rows)

def main():
    table = build_table()
    md = README.read_text(encoding="utf-8")
    new = re.sub(r"(<!-- TABLE_START -->)(.*?)(<!-- TABLE_END -->)",
                 r"\1\n" + table + r"\n\3", md, flags=re.S)
    README.write_text(new, encoding="utf-8")
    print("README updated with acceptance/difficulty.")

if __name__ == "__main__":
    main()
