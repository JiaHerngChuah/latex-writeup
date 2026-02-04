import re
from pathlib import Path

TEX_DIR = Path("tex")
OUT = Path("index.md")

pattern = {
    "id": re.compile(r"% ID:\s*(.+)"),
    "title": re.compile(r"% Title:\s*(.+)"),
    "tags": re.compile(r"% Tags:\s*(.+)"),
    "source": re.compile(r"% Source:\s*(.+)")
}

entries = []

for tex in sorted(TEX_DIR.glob("P*.tex")):
    text = tex.read_text()
    data = {}
    for key, pat in pattern.items():
        m = pat.search(text)
        data[key] = m.group(1) if m else "unknown"
    entries.append(data)

with OUT.open("w") as f:
    f.write("# AI-Assisted Mathematics Archive\n\n")
    f.write("## Problems\n\n")
    for e in entries:
        f.write(f"### {e['id']} - {e['title']}\n")
        f.write(f"- Tags: {e['tags']}\n")
        f.write(f"- Source: {e['source']}\n")
        f.write(f"- [Solution PDF](solutions/{e['id']}.pdf)\n\n")
