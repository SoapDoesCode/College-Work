<?php
if (empty($page_name)) {
    $page_title = "Health Advice Group";
} else {
    $page_title = "Health Advice Group - " . $page_name;
}

$include_navbar = $include_navbar ?? true; // include the navigation bar by default
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <base href="/2025-2026/td2s/233753/health-advice-group/" target="_self">
    <link rel="icon" type="image/x-icon" href="assets/media/favicon.ico">
    <title><?= $page_title ?></title>

    <link rel='stylesheet' href='assets/css/styles.css'>
    <link rel='stylesheet' href='assets/css/footer.css'>
    <?php if ($include_navbar) {
        echo "<link rel='stylesheet' href='assets/css/navbar.css'>
        <script src='https://kit.fontawesome.com/53a7d708ca.js' crossorigin='anonymous'></script>";
    }?>
</head>

<body>
    <?php if ($include_navbar) {
        include_once "assets/php/navbar.php";
    }?>