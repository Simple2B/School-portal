document.addEventListener('DOMContentLoaded', function() {
    const logo = document.querySelector('.logo');
    const mobileMenuButton = document.querySelector('.mobile_menu_button');
    const webHeader = document.querySelector('.header_wrapper');
    const mobileMenu = document.querySelector('.mobile_menu');

    mobileMenuButton.addEventListener("click", function(event) {
        mobileMenuButton.style.display = "none";
        logo.style.display = "none";
        webHeader.style.display = "none";
        mobileMenu.style.display = "block";
    });
});
