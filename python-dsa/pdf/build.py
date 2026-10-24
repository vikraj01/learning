"""Build the two PDFs in python-dsa/:

    python-for-leetcode.pdf   lessons 1-10 in learn/, each with its example script
    leetcode-list.pdf         leetcode-list.md: the 50 practice problems, with clickable links

Run from the repo root:  make pdf
Needs google-chrome (prints the HTML to PDF) and the uv environment (markdown, pygments).
"""

import re
import subprocess
import sys
import tempfile
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent  # python-dsa/
LEARN = ROOT / "learn"
STYLE = (Path(__file__).parent / "style.css").read_text()
LAST_LESSON = 10  # the 50 practice problems only need lessons 1-10


def to_html(md_text: str) -> str:
    return markdown.markdown(
        md_text,
        extensions=["fenced_code", "tables", "codehilite", "sane_lists"],
        extension_configs={"codehilite": {"noclasses": True, "pygments_style": "friendly", "guess_lang": False}},
    )


def plain_local_links(md_text: str) -> str:
    """Links to files in the repo don't work inside a PDF: keep the text, drop the link."""
    return re.sub(r"\[([^\]]+)\]\((?!https?://)[^)]*\)", r"\1", md_text)


def page(title: str, body: str) -> str:
    return f"""<!doctype html>
<html><head><meta charset="utf-8"><title>{title}</title>
<style>{STYLE}</style></head>
<body>{body}</body></html>"""


def print_pdf(html: str, out: Path) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "page.html"
        src.write_text(html)
        subprocess.run(
            ["google-chrome", "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
             f"--user-data-dir={tmp}/profile", f"--print-to-pdf={out}", src.as_uri()],
            check=True, capture_output=True,
        )
    print("wrote", out.relative_to(ROOT.parent))


def build_lessons() -> None:
    lessons = sorted(f for f in LEARN.glob("[0-9][0-9]-*.md") if int(f.stem[:2]) <= LAST_LESSON)
    toc, chapters = [], []
    for md_file in lessons:
        text = md_file.read_text()
        title = text.splitlines()[0].lstrip("# ").strip()
        num = md_file.stem[:2]
        anchor = f"lesson-{num}"
        toc.append(f'<li><a href="#{anchor}"><span class="num">{int(num)}</span>{title}</a></li>')
        # Lesson heading gets its number; the page's own "# Title" line is replaced.
        body_md = plain_local_links("\n".join(text.splitlines()[1:]))
        example = LEARN / "examples" / f"{md_file.stem}.py"
        if example.exists():
            body_md += (f"\n\n## Example script: `examples/{example.name}`\n\n"
                        "Run it from the `learn` folder, then change things and run it again.\n\n"
                        f"```python\n{example.read_text().rstrip()}\n```\n")
        chapters.append(
            f'<section class="lesson" id="{anchor}">'
            f'<div class="kicker">Lesson {int(num)}</div><h1>{title}</h1>'
            f"{to_html(body_md)}</section>"
        )
    cover = (
        '<section class="cover"><div class="kicker">Tanvi\'s study notes</div>'
        "<h1>Python for LeetCode</h1>"
        "<p class=\"lead\">Python from zero, up to what you need for your first 50 easy problems: "
        "numbers, if, functions, strings, lists, loops, dictionaries, sets and tuples.</p>"
        "<p>How to use this: read one lesson, run its example script, then solve that lesson's stage "
        "in the <b>practice list</b> (the other PDF). Then the next lesson.</p>"
        f'<h2>Lessons</h2><ol class="toc">{"".join(toc)}</ol></section>'
    )
    print_pdf(page("Python for LeetCode", cover + "".join(chapters)), ROOT / "python-for-leetcode.pdf")


def build_list() -> None:
    html = to_html((ROOT / "leetcode-list.md").read_text())
    print_pdf(page("Practice list", f'<section class="list">{html}</section>'), ROOT / "leetcode-list.pdf")


if __name__ == "__main__":
    which = sys.argv[1:] or ["lessons", "list"]
    if "lessons" in which:
        build_lessons()
    if "list" in which:
        build_list()
