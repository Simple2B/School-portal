document.addEventListener('DOMContentLoaded', function() {
    const logo = document.querySelector('.logo');
    const mobileMenuButton = document.querySelector('.mobile_menu_button');
    const webHeader = document.querySelector('.header_wrapper');
    const mobileMenu = document.querySelector('.mobile_menu');
    const contentSection = document.querySelector('.display_content');
    const footer = document.querySelector('.footer');

    mobileMenuButton.addEventListener("click", function(event) {
        mobileMenuButton.style.display = "none";
        logo.style.display = "none";
        webHeader.style.display = "none";
        contentSection.style.display = "none";
        footer.style.display = "none";
        document.body.style.backgroundColor = "#1d1b4c";
        mobileMenu.style.display = "block";
    });
});
