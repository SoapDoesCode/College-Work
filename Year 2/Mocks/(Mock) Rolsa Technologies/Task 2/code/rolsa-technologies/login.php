<?php
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

include_once "assets/php/helper.php";

include_once "assets/php/database/db-handler.php";
include_once "assets/php/database/users.php";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // check if the request is a login attempt
    // we do this by checking if both 'login_email' and 'login_pass' are set
    if (isset($_POST['login_email']) && isset($_POST['login_pass'])) {
        login_user($_POST['login_email'], $_POST['login_pass']);
        redirect($_domain.$_base_path."dashboard.php");
    // check if the request is a registration attempt
    // we do this by checking if the variables 'register_email', 'register_pass', and 'register_confirm_pass' are set
    } elseif (isset($_POST['register_email']) && isset($_POST['register_pass']) && isset($_POST['register_confirm_pass'])) {
        $result = register_user($_POST['register_email'], $_POST['register_pass'], $_POST['register_confirm_pass']);

        // if register_user returns anything, the registration attempt failed
        if ($result) {
            $_register_error = $result;
        } else {
            // user just created their account, log them in for convenience
            login_user($_POST['register_email'], $_POST['register_pass']);
            redirect($_domain.$_base_path."dashboard.php");
    }
    }
}

$page_name = "Login/Register";
$include_navbar = true;
include_once "assets/php/header.php";

?>
<div class="content">
    <div class="account-container">
        <form method="POST" action="login.php" class="login-form show" id="login-form">
            <h2 class="section-title">Login</h2>
            <input type="email" class="text-field" name="login_email" id="login-email" placeholder="Enter your email"><br>
            <small id="loginEmailError" class="error-text"></small><br>
            <input type="password" class="text-field" name="login_pass" id="login-password" placeholder="Enter your password"><br>
            <small id="loginPassError" class="error-text"></small><br>
            <?php if (isset($_login_error)) {
                echo "<small id='loginAuthError' class='error-text show'>$_login_error</small><br>";
            }?>
            <input type="submit" value="Login" class="submit-btn" id="login-submit"><br>
        </form>
        <form method="POST" action="login.php" class="register-form show" id="register-form">
            <h2 class="section-title">Register</h2>
            <input type="email" class="text-field" name="register_email" id="register-email" placeholder="Enter your email"><br>
            <small id="registerEmailError" class="error-text"></small><br>
            <input type="password" class="text-field" name="register_pass" id="register-password" placeholder="Create a password"><br>
            <small id="registerPassError" class="error-text"></small><br>
            <ul id="register-requirements">
                <li class="pass-req" id="req-len">At least 12 characters</li>
                <li class="pass-req" id="req-upper">One uppercase letter</li>
                <li class="pass-req" id="req-lower">One lowercase letter</li>
                <li class="pass-req" id="req-num">One number</li>
                <li class="pass-req" id="req-symbol">One symbol</li>
            </ul>
            <input type="password" class="text-field" name="register_confirm_pass" id="register-confirm-password" placeholder="Confirm your password"><br>
            <small id="registerConfirmPassError" class="error-text"></small><br>
            <?php if (isset($_register_error)) {
                echo "<small id='registerAuthError' class='error-text show'>$_register_error</small><br>";
            }?>
            <input type="submit" value="Register" class="submit-btn" id="register-submit"><br>
        </form>
    </div>
</div>
<?php
include_once "assets/php/footer.php";
?>