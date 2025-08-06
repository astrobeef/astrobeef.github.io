HTML = `
    <aside class="sidebar">
        <div class="track" id="track">
            <a href="Projects/Anything But Shadows.md.html"><img src="./Media/Anything-but-Shadows.png"></a>
            <a href="Projects/Internship Scanner Summer 2026.md.html"><img
                    src="./Media/internship-scanner-email-screenshot.png"></a>
            <a href="Projects/Obsidian Markdown to HTML Converter.md.html"><img
                    src="./Media/md_html_converter_styled.png"></a>
            <a href="Projects/Moe's Diner Duel.md.html"><img src="./Media/Moes-diner-duel.png"></a>
        </div>
    </aside>
`

const track = document.getElementById('track');
const clones = track.cloneNode(true).children;
[...clones].forEach(img => track.appendChild(img.cloneNode(true)));