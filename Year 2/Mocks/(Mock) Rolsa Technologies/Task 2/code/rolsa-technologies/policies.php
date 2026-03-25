<?php
include_once "assets/php/helper.php";

$policy = $_GET['policy'] ?? "";
switch ($policy) { // check which policy page is selected
    case "cookies-policy": // load the cookies policy
        $page_name = "Cookies Policy";
        $policy_file = "assets/policies/".$policy.".html";
        break;
    case "privacy-policy"; // load the privacy policy
        $page_name = "Privacy Policy";
        $policy_file = "assets/policies/".$policy.".html";
        break;
    case "refunds-and-cancellations-policy"; // load the refunds & cancellations policy
        $page_name = "Refunds & Cancellations";
        $policy_file = "assets/policies/".$policy.".html";
        break;
    case "terms-and-conditions"; // load the terms & conditions
        $page_name = "Terms & Conditions";
        $policy_file = "assets/policies/".$policy.".html";
        break;
    default: // if no policy is set, default to the terms & conditions
        redirect("policies.php?policy=terms-and-conditions");
        break;
}
$include_navbar = true;
include_once "assets/php/header.php";
?>
<div class="content">
    <div id="navbar-pad"></div>
    <?php
    if (!empty($policy_file)) {
        include_once $policy_file;
    }?>
</div>
<?php
include_once "assets/php/footer.php";
?>