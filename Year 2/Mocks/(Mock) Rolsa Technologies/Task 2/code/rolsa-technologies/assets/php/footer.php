<?php
$page = strtolower($page_name); // convert the page_name to lowercase for easier matching

// function used so footer links can detect if they are the active page
// if the link is determined to be the active page, it will apply the "active-link"
// class in order to underline the link in the footer
function isactive($name, $page) {
    // $name is the name of the page the link represents
    // $page is the name of the current page
    return strtolower($page) === strtolower($name) ? "active-link" : "";
}
?>
    <footer id="footer">
        <div class="footer-sect"><a href="index.php"><img class="footer-logo-img" src="assets/media/webp/logo.webp" alt="Rolsa Technologies logo"></a></div>
        <div class="footer-link-sect">
            <a href="index.php" class="footer-link <?= isactive("homepage", $page)?>">HOME</a>
            <a href="login.php" class="footer-link <?= isactive("login/register", $page)?>">LOGIN/REGISTER</a>
            <a href="reduce-carbon-footprint.php" class="footer-link <?= isactive("reduce carbon footprint", $page)?>">REDUCE CARBON FOOTPRINT</a>
            <a href="carbon-calculator.php" class="footer-link <?= isactive("carbon footprint calculator", $page)?>">CARBON FOOTPRINT CALCULATOR</a>
            <a href="green-energy.php" class="footer-link <?= isactive("green energy products", $page)?>">GREEN ENERGY PRODUCTS</a>
            <a href="installation.php" class="footer-link <?= isactive("book an installation", $page)?>">BOOK AN INSTALLATION</a>
            <a href="consultation.php" class="footer-link <?= isactive("book a consultation", $page)?>">BOOK A CONSULTATION</a>
            <a href="about.php" class="footer-link <?= isactive("about us", $page)?>">ABOUT</a>
        </div>
        <div class="footer-link-sect">
            <a href="policies.php?policy=cookies-policy" class="footer-link <?= isactive("cookies policy", $page)?>">COOKIES POLICY</a>
            <a href="policies.php?policy=privacy-policy" class="footer-link <?= isactive("privacy policy", $page)?>">PRIVACY POLICY</a>
            <a href="policies.php?policy=terms-and-conditions" class="footer-link <?= isactive("terms & conditions", $page)?>">TERMS & CONDITIONS</a>
            <a href="policies.php?policy=refunds-and-cancellations-policy" class="footer-link <?= isactive("refunds & cancellations", $page)?>">REFUNDS & CANCELLATIONS POLICY</a>
        </div>
    </footer>
    <?php if ($include_navbar) {
        echo '<script src="assets/js/navbar.js"></script>';
    }
    
    switch ($page) {
        case "login/register":
            echo '<script src="assets/js/login.js"></script>';
            break;
        default:
            // we don't care...currently
            break;
        }
    ?>
</body>
</html>