document.addEventListener("DOMContentLoaded", (e) => {
    const venues_btn = document.getElementById("venues-btn");
    const venues_dropdown = document.getElementById("venues-dropdown");

    document.addEventListener("click", (e) => {
        if (!venues_dropdown.contains(e.target)) {
            venues_btn.nextElementSibling.classList.remove("show");
        }
    });

    venues_btn.addEventListener("click", (e) => {
        venues_btn.nextElementSibling.classList.toggle("show")
    });
})