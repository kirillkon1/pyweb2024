// src/js/scripts.js
document.addEventListener('DOMContentLoaded', () => {
    console.log('Сайт загружен и работает!');

    // Bulma Burger Menu
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

    if ($navbarBurgers.length > 0) {
        $navbarBurgers.forEach(el => {
            el.addEventListener('click', () => {
                const target = el.dataset.target;
                const $target = document.getElementById(target);

                el.classList.toggle('is-active');
                $target.classList.toggle('is-active');
            });
        });
    }

    // Добавьте свои JS-функции ниже
});
