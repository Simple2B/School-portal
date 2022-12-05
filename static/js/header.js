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
    const services_button = document.querySelector('.services_button');
    const services_highlight = document.querySelector('.services_highlight');
    const projects_button = document.querySelector('.projects_button');
    const projects_highlight = document.querySelector('.projects_highlight');
    const about_button = document.querySelector('.about_button');
    const about_highlight = document.querySelector('.about_highlight');
    const blog_button = document.querySelector('.blog_button');
    const blog_highlight = document.querySelector('.blog_highlight');
    const careers_button = document.querySelector('.careers_button');
    const careers_highlight = document.querySelector('.careers_highlight');
    const contact_button = document.querySelector('.contact_button');
    const contact_highlight = document.querySelector('.contact_highlight');

    
    function disableAllHiglights() {
        for (let i = 0; i < allHighlights.length; i++) {
            allHighlights[i].style.display = "none";
        }
    }
    
    console.log(window.location.href);

    if (window.location.href.indexOf('careers') !== -1) {
        careers_highlight.style.display = "block";
    }  else if (window.location.href.indexOf('solutions') !== -1) {
        solutions_highlight.style.display = "block";
    }  else if (window.location.href.indexOf('services') !== -1) {
        services_highlight.style.display = "block";
    }  else if (window.location.href.indexOf('projects') !== -1) {
        projects_highlight.style.display = "block";
    }  else if (window.location.href.indexOf('about') !== -1) {
        about_highlight.style.display = "block";
    }  else if (window.location.href.indexOf('blog') !== -1) {
        blog_highlight.style.display = "block";
    }  else if (window.location.href.indexOf('contact') !== -1) {
        contact_highlight.style.display = "block";
    }

    const menuHighlights = {
        "solutions": careers_highlight,
        "projects": projects_highlight,
    }

    console.log(menuHighlights["solutions"])

    solutions_button.addEventListener("click", function(event) {
        disableAllHiglights();
        solutions_highlight.style.display = "block";
    });
    services_button.addEventListener("click", function(event) {
        disableAllHiglights();
        services_highlight.style.display = "block";
    });
    projects_button.addEventListener("click", function(event) {
        disableAllHiglights();
        projects_highlight.style.display = "block";
    });
    about_button.addEventListener("click", function(event) {
        disableAllHiglights();
        about_highlight.style.display = "block";
    });
    blog_button.addEventListener("click", function(event) {
        disableAllHiglights();
        blog_highlight.style.display = "block";
    });
    careers_button.addEventListener("click", function(event) {
        disableAllHiglights();
        careers_highlight.style.display = "block";
    });
    contact_button.addEventListener("click", function(event) {
        disableAllHiglights();
        contact_highlight.style.display = "block";
    });

    // logo.addEventListener("click", function(event) {
    //     alert("Click");
    // });
});
