<?php
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}
include_once "assets/php/database/db-handler.php";

function account_login($email, $pass) {
    // check login, then set session
    $result = login_user($email, $pass);
        
    if ($result == "success") {
        // session_start();
        $_SESSION['email'] = $email;
        include_once "assets/php/account/dashboard.php";
    } else {
        $_login_error = $result;
        include_once "assets/php/account/login.php";
    }
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // echo "<h1>POST :D</h1>";
    if (isset($_POST['login_email'])) {
        account_login($_POST['login_email'], $_POST['login_pass']);
    } else if (isset($_POST['register_email'])) {
        $result = register_user($_POST['register_email'], $_POST['register_pass'], $_POST['register_confirm_pass']);
        
        // if register_user returns anything, it failed
        if ($result) {
            $_register_error = $result;
            include_once "assets/php/account/login.php";
        } else {
            // user just created their account, so log them in
            account_login($_POST['register_email'], $_POST['register_pass']);
        }
    }
} else {
    if (isset($_SESSION['email'])) {
        include_once "assets/php/account/dashboard.php";
    } else {
        include_once "assets/php/account/login.php";
    }
}
?>
<!-- <p>This page should load from <b>php/login.php</b> or <b>php/dashboard.php</b> depending on whether the user is logged in or not!</p> -->