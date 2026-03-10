document.addEventListener("DOMContentLoaded", (e) => {
    const login_form = document.getElementById("login-form");
    const signup_form = document.getElementById("signup-form");
    const login_link = document.getElementById("login-link");
    const signup_link = document.getElementById("signup-link");

    login_link.addEventListener("click", (e) => {
        signup_form.classList.remove("show");
        login_form.classList.add("show");
        console.log("login press");
    });

    signup_link.addEventListener("click", (e) => {
        login_form.classList.remove("show");
        signup_form.classList.add("show");
        console.log("signup press");
    });
})