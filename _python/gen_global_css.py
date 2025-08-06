import argparse, pathlib, sys

GLOBAL_CSS_NAME = "global.css"
ROOT            = "../."            # NOTE: This needs to be changed in the event this script changes directory (currently `./_python/<this>`)

def _find_css_files(root, output_file):
    css_files = []
    for path in root.rglob('*.css'):
        parts = path.relative_to(root).parts
        if any(p.startswith('.') for p in parts):
            continue
        if path.resolve() == output_file.resolve():
            continue
        css_files.append(path)
    return sorted(css_files, key=lambda p: str(p))

def main():
    root_dir = pathlib.Path(ROOT).parent.resolve()
    output_file = (root_dir / GLOBAL_CSS_NAME).resolve()
    css_files = _find_css_files(root_dir, output_file)
    if not css_files:
        print('No CSS files found.', file=sys.stderr)
        sys.exit(1)
    with output_file.open('w', encoding='utf-8') as outfile:
        for css_file in css_files:
            rel_path = css_file.relative_to(root_dir)
            outfile.write(f'/* --- {rel_path} --- */\n')
            outfile.write(css_file.read_text(encoding='utf-8'))
            outfile.write('\n\n')
    print(f'Combined {len(css_files)} CSS files into {output_file}')
    return

if __name__ == '__main__':
    main()