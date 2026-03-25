<?php
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

include_once "helper.php";

if (empty($page_name)) {
    $page_title = "Rolsa Technologies";
} else {
    $page_title = "Rolsa Technologies - ".$page_name;
}

$include_navbar = $include_navbar ?? true; // include the navigation bar by default
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <base href="<?=$_base_path?>" target="_self">
    <link rel="icon" type="image/x-icon" href="assets/media/favicon.ico">
    <title><?= $page_title ?></title>

    <link rel='stylesheet' href='assets/css/styles.css'>
    <link rel='stylesheet' href='assets/css/footer.css'>
    <?php if ($include_navbar) {
        echo <<<HTML
        <link rel='stylesheet' href='assets/css/navbar.css'>
        <script src='https://kit.fontawesome.com/53a7d708ca.js' crossorigin='anonymous'></script>
        HTML;

        // apply CSS to specific pages
        switch (strtolower($page_name)) {
            case "homepage": // if the user is on the homepage
                echo "<link rel='stylesheet' href='assets/css/homepage.css'/>";
                break;
            case "login/register": // if the user is on the login page
                echo "<link rel='stylesheet' href='assets/css/login.css'/>";
                break;
            case "cookies policy": // if the user is on the cookies policy
            case "privacy policy": // or the privacy policy
            case "refunds & cancellations": // or the refunds & cancellations policy
            case "terms & conditions": // or the terms & caonditions
                echo "<link rel='stylesheet' href='assets/css/policies.css'/>";
                break;
            default:
                // we don't care...currently
                break;
        }
    }?>
</head>
<body>
    <?php if ($include_navbar) {
        include_once "assets/php/navbar.php";
    }?>