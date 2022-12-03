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

    const allHighlights = document.querySelectorAll('.highlight');
    const solutions_button = document.querySelector('.solutions_button');
    const solutions_highlight = document.querySelector('.solutions_highlight');

    const projects_button = document.querySelector('.projects_button');
    const projects_highlight = document.querySelector('.projects_highlight');
    
    const careers_button = document.querySelector('.careers_button');
    const careers_highlight = document.querySelector('.careers_highlight');

    console.log(allHighlights.length)

    function disableAllHiglights() {
        for (let i = 0; i < allHighlights.length; i++) {
            console.log(allHighlights[i], allHighlights[i].style.backgroundColor)
            allHighlights[i].style.display = "none";
        }
    }

    solutions_button.addEventListener("click", function(event) {
        disableAllHiglights();
        solutions_highlight.style.display = "block";
    });

    projects_button.addEventListener("click", function(event) {
        disableAllHiglights();
        projects_highlight.style.display = "block";
    });
    
    careers_button.addEventListener("click", function(event) {
        disableAllHiglights();
        careers_highlight.style.display = "block";
    });
});
