<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- VERY IMPORTANT ON THIS SERVER -->
    <base href="/2025-2026/td2s/233753/puremedia-yungblud-website/" target="_self">
    <!-- VERY IMPORTANT ON THIS SERVER -->
    <link rel="icon" type="image/x-icon" href="img/favicon.ico">
    <title><?php echo ("Yungblud - " . $page_title) ?? "Yungblud - A PureMedia Website"; ?></title>
    <link rel="stylesheet" href="css/fonts.css"/>
    <link rel="stylesheet" href="css/styles.css"/>
    <link rel="stylesheet" href="css/footer.css"/>

    <?php
    // we can do stuff for specific pages now :D
    switch (strtolower($page_title)) {
        case "account":
            echo "<link rel='stylesheet' href='css/account.css'/>";
            break;
        case "about":
            echo "<link rel='stylesheet' href='css/about.css'/>";
        default:
            // we don't care...currently
            break;
    }
    ?>

    <?php
    /* sets the value of $include_navbar to true if not already set */
    $include_navbar ??= true;
    if ($include_navbar) {
        echo '<link rel="stylesheet" href="css/navbar.css"/>';
    }?>
    
</head>

<body class="body">
    <?php
    /* if $include_navbar is true, include the navbar (woah, what a shocker) */
    // $include_navbar ? include "html/navbar.html" : null;
    $include_navbar ? include "php/navbar.php" : null;
    ?>