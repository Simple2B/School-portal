document.addEventListener('DOMContentLoaded', function() {
    const mobileMenu = document.querySelector('.mobile_menu_button');

    mobileMenu.addEventListener("click", function(event) {
        mobileMenu.style.display = "none";
    });
});
