<?php
$policy = $_GET['policy'] ?? "";
switch ($policy) {
    case "cookies-policy":
        $page_name = "Cookies Policy";
        $policy_file = "policies/" . $policy . ".html";
        break;
    case "privacy-policy";
        $page_name = "Privacy Policy";
        $policy_file = "policies/" . $policy . ".html";
        break;
    case "refunds-and-cancellations-policy";
        $page_name = "Refunds & Cancellations Policy";
        $policy_file = "policies/" . $policy . ".html";
        break;
    case "terms-and-conditions";
        $page_name = "Terms & Conditions";
        $policy_file = "policies/" . $policy . ".html";
        break;
    default:
        $page_name = "Policies";
        break;
}
$include_navbar = true;
include_once "assets/php/header.php";
?>
<div class="policy-content">
    <div id="navbar-pad"></div>
    <?php
    if (!empty($policy_file)) {
        include_once $policy_file;
    } else { // everything below is now inside this else ?>
    <h1>Our policies</h1>
    <a href="policies.php?policy=cookies-policy">Cookies Policy</a><br>
    <a href="policies.php?policy=privacy-policy">Privacy Policy</a><br>
    <a href="policies.php?policy=refunds-and-cancellations-policy">Refunds & Cancellations Policy</a><br>
    <a href="policies.php?policy=terms-and-conditions">Terms & Conditions</a>
    <?php } // closing the else block from earlier?>
</div>
<?php
include_once "assets/php/footer.php";
?>