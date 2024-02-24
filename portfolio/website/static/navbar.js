// Navbar //
let hamburger = document.getElementById('hamburger_menu');
let drop_down = document.getElementById('drop_down_nav');

function respnav() {
    drop_down.classList.toggle('active');
}


hamburger.addEventListener("click", respnav);
