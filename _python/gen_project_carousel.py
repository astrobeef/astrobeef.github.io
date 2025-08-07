# first-party
from html import escape
from pathlib import Path

EXPORT_PATH = Path("./project_carousel.html")

ITEMS = [
    {
        "src"       : Path("Media/Anything-but-Shadows.png"),
        "href"      : Path("./Projects/Anything But Shadows.md.html")
     },
    {
        "src"       : Path("./Media/internship-scanner-email-screenshot.png"),
        "href"      : Path("./Projects/Internship Scanner Summer 2026.md.html")
     },
    {
        "src"       : Path("./Media/md_html_converter_styled.png"),
        "href"      : Path("./Projects/Obsidian Markdown to HTML Converter.md.html")
     },
    {
        "src"       : Path("./Media/Moes-diner-duel.png"),
        "href"      : Path("./Projects/Moe's Diner Duel.md.html")
     },
]

def _gen_alt_text(item) -> str:
    image_path: Path = item["src"]
    name = image_path.stem
    name = name.replace('_', ' ').replace('-', ' ')
    name = name.strip().title()
    return name

def _as_root_relative(path: Path) -> str:
    return '/' + str(path).lstrip("./\\").replace("\\", "/")

def _gen_carousel_snippet(items) -> str:
    tile_html = []
    for item in items:
        href = escape(_as_root_relative(item["href"]))
        src = escape(_as_root_relative(item["src"]))
        alt = escape(_gen_alt_text(item))
        tile_html.append(
            f'<a href="{href}"><img loading="lazy" src="{src}" alt="{alt}"></a>'
        )
    # Duplicate for seamless looping
    tiles = ''.join(tile_html) * 2
    snippet = (
        f'<aside class="sidebar"><div class="track" id="track">'
        f'{tiles}</div></aside>'
    )
    return snippet

def _write(snippet: str):
    EXPORT_PATH.write_text(snippet, 'utf-8')

def main():
    snippet = _gen_carousel_snippet(ITEMS)
    _write(snippet)
    print(f"Wrote carousel HTML to: \"{str(EXPORT_PATH)}\"")

if __name__ == "__main__":
    main()