const links = document.querySelector('.nav-links')
const hamburger = document.querySelector(".hamburger")

hamburger.addEventListener('click', () => {
    links.classList.toggle('show')
})