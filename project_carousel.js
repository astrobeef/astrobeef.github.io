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

    if (!target) return;

    fetch(CAROUSEL_SNIPPET_PATH)
        .then(res => res.text())
        .then(html => {
            const template = document.createElement('template');
            template.innerHTML = html.trim();
            const carouselNode = template.content.firstElementChild;
            target.insertAdjacentElement('afterend', carouselNode);
            carouselNode.classList.add('carousel-loaded');
        });
}