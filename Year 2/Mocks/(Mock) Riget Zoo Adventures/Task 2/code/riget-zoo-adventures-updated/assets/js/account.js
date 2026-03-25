function isValidEmail(email_addr, error_msg) {
    const email_regex = /^[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    // strip leading/trailing whitespace
    email_addr.value = email_addr.value.trim();

    if (!email_addr.value) {
        // runs if email address is not set
        error_msg.textContent = "Email address is required."; // set error message
        error_msg.classList.add("show"); // sets the error to display
        return false;
    } else if (!email_addr.value.match(email_regex)) {
        // runs if the entered email address is not valid
        error_msg.textContent = "Please enter a valid email address"; // set error message
        error_msg.classList.add("show"); // sets the error to display
        return false;
    } else {
        // runs if the entered email address is valid
        error_msg.textContent = ""; // clear the error message
        error_msg.classList.remove("show"); // sets the error to hidden
        return true;
    }
}

function isValidPassword(password, error_msg) {
    password.value = password.value.trim();

    if (!/\d/.test(password.value)) {
        // check if password contains a number
        error_msg.textContent = "Password must contain a number.";
        error_msg.classList.add("show");
        return false;
    } else if (!/[a-z]/.test(password.value)) {
        // check if password contains a lowercase letter
        error_msg.textContent = "Password must contain a lowercase letter.";
        error_msg.classList.add("show");
        return false;
    } else if (!/[A-Z]/.test(password.value)) {
        // check if password contains an uppercase letter
        error_msg.textContent = "Password must contain an uppercase letter.";
        error_msg.classList.add("show");
        return false;
    } else if (!/[!@#$%\^&*()\-_+={}\[\]|\\:;"'<>,.\/?~]/.test(password.value)) {
        // check if password contains special characters (!@#$%^&*()-_+={}[]|\;:"'<>,./?~)
        error_msg.textContent = "Password must contain a special character.";
        error_msg.classList.add("show");
        return false;
    } else if (password.value.length < 8) {
        // check if password is contains 8+ characters
        error_msg.textContent ="Password must contain at least 8 characters." ;
        error_msg.classList.add("show");
        return false;
    } else {
        // password is fully valid
        error_msg.textContent = "";
        error_msg.classList.remove("show");
        return true;
    }
}

function isValidConfirmPassword(password, confirm_password, error_msg) {
    if (password.value === confirm_password.value) {
        error_msg.textContent = "";
        error_msg.classList.remove("show");
        return true;
    } else {
        error_msg.textContent = "Passwords do not match.";
        error_msg.classList.add("show");
        return false;
    }
}

function isFormValid(val_results) {
    // check if all validation results are true
    return val_results.every(result => result === true);
}

document.addEventListener("DOMContentLoaded", (e) => {
    const login_form = document.getElementById("login-form");
    const login_email = document.getElementById("login-email");
    const login_password = document.getElementById("login-password");
    const login_submit = document.getElementById("login-submit");
    // error texts:
    const loginEmailError = document.getElementById("loginEmailError");
    const loginPassError = document.getElementById("loginPassError");

    const register_form = document.getElementById("register-form");
    const register_email = document.getElementById("register-email");
    const register_password = document.getElementById("register-password");
    const register_confirm_password = document.getElementById("register-confirm-password");
    const register_submit = document.getElementById("register-submit");
    // error texts:
    const registerEmailError = document.getElementById("registerEmailError");
    const registerPassError = document.getElementById("registerPassError");
    const registerConfirmPassError = document.getElementById("registerConfirmPassError");

    // detect changes to the inputs for live updates
    login_email.addEventListener("input", (e) => {
        isValidEmail(login_email, loginEmailError);
    });

    login_password.addEventListener("input", (e) => {
        isValidPassword(login_password, loginPassError);
    });

    register_email.addEventListener("input", (e) => {
        isValidEmail(register_email, registerEmailError);
    });

    register_password.addEventListener("input", (e) => {
        isValidPassword(register_password, registerPassError);
    });

    register_confirm_password.addEventListener("input", (e) => {
        isValidConfirmPassword(register_password, register_confirm_password, registerConfirmPassError);
    });

    login_submit.addEventListener("click", (e) => {
        e.preventDefault(); // prevent the form from submitting until we validate once more

        if (isFormValid(val_results = [
            isValidEmail(login_email, loginEmailError),
            isValidPassword(login_password, loginPassError)
        ])) {
            alert("Login submitted successfully!")
            login_form.submit()
        }
    });

    register_form.addEventListener("click", (e) => {
        e.preventDefault(); // prevent the form from submitting until we validate once more

        if (isFormValid(val_results = [
            isValidEmail(register_email, registerEmailError),
            isValidPassword(register_password, registerPassError),
            isValidConfirmPassword(register_password, register_confirm_password, registerConfirmPassError)
        ])) {
            alert("Register submitted successfully!")
            register_form.submit()
        }
    });
});