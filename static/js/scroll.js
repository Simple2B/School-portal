document.addEventListener('DOMContentLoaded', function() {
    const contact_button = document.querySelector('.contact_button');

    contact_button.addEventListener("click", function(event) {
        event.preventDefault();
        document.querySelector('#contacts_form').scrollIntoView({
            behavior: 'smooth'
        });
    });
});
