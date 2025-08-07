const CAROUSEL_SNIPPET_PATH = '/project_carousel.html';

export function doInjectCarousel(){
    return true;
}

/**
 * Injects pre-generated carousel HTML (from CAROUSEL_SNIPPET_PATH) after a target element.
 * @param {HTMLElement|string} anchor - Element or selector after which to insert the carousel
 */
export function injectCarousel(anchor) {
    const target = typeof anchor === 'string'
        ? document.querySelector(anchor)
        : anchor;
    console.log("1")

    if (!target) return;
    console.log("2")

    fetch(CAROUSEL_SNIPPET_PATH)
        .then(res => res.text())
        .then(html => {
            console.log("3")
            const template = document.createElement('template');
            template.innerHTML = html.trim();
            const carouselNode = template.content.firstElementChild;
            target.insertAdjacentElement('afterend', carouselNode);
            carouselNode.classList.add('carousel-loaded');
            console.log("4")
        });
}