const resize = document.getElementById("phone-nav")
const margin_1 = document.getElementById("adjust-margin-1")
const margin_2 = document.getElementById("adjust-margin-2")
const cart = document.getElementById("cart-ul")
const nav_cart = document.getElementById("nav-cart")

window.addEventListener("resize", function () {
    if (window.innerWidth < 982) {
        resize.classList.remove("navbar-nav")
        margin_1.classList.remove("ml-5")
        margin_2.classList.remove("ml-5", "pl-5")
        cart.style.display = 'none'
        nav_cart.hidden = false
    }
    else {
        resize.classList.add("navbar-nav")
        margin_1.classList.add("ml-5", "pl-5")
        margin_2.classList.add("ml-5", "pl-5")
        cart.style.display = ''
        nav_cart.hidden = true
    }
});
if (window.innerWidth < 982) {
    resize.classList.remove("navbar-nav")
    margin_1.classList.remove("ml-5", "pl-5")
    margin_2.classList.remove("ml-5", "pl-5")
    cart.style.display = 'none'
    nav_cart.hidden = false
}