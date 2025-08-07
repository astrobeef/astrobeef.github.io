import { doInjectCarousel, injectCarousel } from "./project_carousel.js"

document.addEventListener('DOMContentLoaded', () => {
    if (doInjectCarousel())
        injectCarousel(document.body);
});
