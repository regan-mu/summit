hamburger = document.querySelector('.hamburger');
menuItems = document.querySelector('.menu .menu-items');
links = document.querySelectorAll('.item');

hamburger.addEventListener('click', () => {
    menuItems.classList.toggle('show-menu');
    // Animate the menu links.
    links.forEach((link, index) => {
        if (link.style.animation) {
            link.style.animation = '';
        }
        else {
            link.style.animation = `fadeIn 0.5s ease forwards ${index / 7 + 0.5}s`;
        }
    });
})