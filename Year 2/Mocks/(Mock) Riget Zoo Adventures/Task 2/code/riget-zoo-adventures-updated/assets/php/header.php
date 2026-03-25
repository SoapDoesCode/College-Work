<?php
// check if a PHP session has been started
if (session_status() === PHP_SESSION_NONE) {
    // if no session has been started, start one
    session_start();
}

if (empty($page_name)) {
    // set a default title if the page never sets its name
    $page_title = "Riget Zoo Adventures";
} else {
    $page_title = "Riget Zoo Adventures - " . $page_name;
}

$include_navbar = $include_navbar ?? true; // include the navigation bar by default
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <base href="/2025-2026/td2s/233753/riget-zoo-adventures-updated/" target="_self">
    <link rel="icon" type="image/x-icon" href="assets/media/favicon.ico">
    <title><?= $page_title ?></title>

    <link rel='stylesheet' href='assets/css/styles.css'>
    <link rel='stylesheet' href='assets/css/footer.css'>
    <?php if ($include_navbar) {
        // include the css for the navbar
        echo "<link rel='stylesheet' href='assets/css/navbar.css'>";

        // fetch the account icon from FontAwesome
        echo "<script src='https://kit.fontawesome.com/53a7d708ca.js' crossorigin='anonymous'></script>";

        // use the page name to check which CSS to include
        switch (strtolower($page_name)) {
            case "homepage": // check if we're on the homepage
                // load the CSS relevant to the homepage
                echo "<link rel='stylesheet' href='assets/css/homepage.css'/>";
                echo "<link rel='stylesheet' href='assets/css/attractions.css'/>";
                break;
            case "about us": // check if we're on the about us page
                // load the CSS relevant to the about us page
                echo "<link rel='stylesheet' href='assets/css/about.css'/>";
                break;
            case "attractions": // check if we're on the attractions page
                // load the CSS relevant to the attractions page
                echo "<link rel='stylesheet' href='assets/css/attractions.css'/>";
                break;
            case "login/register": // check if we're on the account page
                // load the CSS relevant to the account page
                echo "<link rel='stylesheet' href='assets/css/account/login.css'/>";
                break;
            case "account dashboard": // check if we're on the account dashboard
                // load the CSS relevant to the account dashboard
                echo "<link rel='stylesheet' href='assets/css/account/dashboard.css'/>";
                break;
            case "plan your stay": // check if we're on the hotel booking page
                // load the CSS relevant to the hotel booking page
                echo "<link rel='stylesheet' href='assets/css/hotel-booking.css'/>";
                break;
            case "book tickets": // check if we're on the ticket booking page
                // load the CSS relevant to the ticket booking page
                echo "<link rel='stylesheet' href='assets/css/hotel-booking.css'/>";
                break;
            default:
                // we don't need to load any CSS
                break;
        }
    }?>
</head>

<body>
    <?php if ($include_navbar) {
        // include the navbar on pages that ask for it
        include_once "assets/php/navbar.php";
    }?>