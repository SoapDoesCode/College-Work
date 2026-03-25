<?php
$page_name = "Login/Register";
$include_navbar = true;
$navbar_pad_fix = true;
include_once "assets/php/header.php";
?>
<div class="content">
    <div id="navbar-pad"></div>
    <div class="account-container">
        <form method="POST" action="account.php" class="login-form show" id="login-form">
            <h2 class="section-title">Login</h2>
            <input type="email" class="text-field" name="login_email" id="login-email" placeholder="Enter your email"><br>
            <small id="loginEmailError" class="error-text"></small><br>
            <input type="password" class="text-field" name="login_pass" id="login-password" placeholder="Enter your password"><br>
            <small id="loginPassError" class="error-text"></small><br>
            <div class="login-pad"></div>
            <?php if (isset($_login_error)) {
                echo "<small id='loginAuthError' class='error-text show'>$_login_error</small><br>";
            }?>
            <input type="submit" value="Login" class="submit-btn" id="login-submit"><br>
        </form>
        <form method="POST" action="account.php" class="register-form show" id="register-form">
            <h2 class="section-title">Register</h2>
            <input type="email" class="text-field" name="register_email" id="register-email" placeholder="Enter your email"><br>
            <small id="registerEmailError" class="error-text"></small><br>
            <input type="password" class="text-field" name="register_pass" id="register-password" placeholder="Create a password"><br>
            <small id="registerPassError" class="error-text"></small><br>
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