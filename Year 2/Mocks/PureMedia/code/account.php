<?php
$page_title = "Account";
$include_navbar = true; /* optional (defaults to true if left undefined) */
include_once "php/header.php";
?>

<main class="content">
    <div class="accounts-container">
        <form method="POST" class="login-form show" id="login-form">
            <h2 class="section-title">SIGN IN</h2>
            <input type="email" id="login-email" placeholder="Email"><br>
            <input type="password" id="login-password" placeholder="Password"><br>
            <input type="submit" value="SIGN IN" class="submit-btn"><br>
            <span class="switch-form-btns" id="login-prompt">Don't have an account? <a id="signup-link">Register</a></span>
        </form>
        <form method="POST" class="signup-form" id="signup-form">
            <h2 class="section-title">SIGN UP</h2>
            <input type="text" id="first-name" placeholder="First name"><br>
            <input type="text" id="last-name" placeholder="Last name"><br>
            <input type="email" id="signup-email" placeholder="Email"><br>
            <input type="password" id="signup-password" placeholder="Password"><br>
            <input type="submit" value="CREATE" class="submit-btn"><br>
            <span class="switch-form-btns" id="signup-prompt">Already have an account? <a id="login-link">Sign In</a></span>
        </form>
    </div>
</main>

<?php include "php/footer.php";
// no blasphemy today :D ?>