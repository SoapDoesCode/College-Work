<?php
$page_name = "Plan your stay";
$include_navbar = true;
include_once "assets/php/header.php";
include_once "assets/php/database/db-handler.php";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_SESSION['email']) and isset($_POST['date']) and isset($_POST['num_nights']) and isset($_POST['num_adults']) and isset($_POST['num_children'])) {
        $booking_result = book_hotel($_SESSION['email'], random_int(1, 500), $_POST['date'], $_POST['num_nights'], $_POST['num_adults'], $_POST['num_children']);

        if ($booking_result === "success") {
            echo '<script>alert("Hotel booked successfully! Redirecting to dashboard..."); window.location.href="account.php";</script>';
        }
    }
}
?>
<div class="content">
    <img class="banner-img" src="assets/media/webp/lion-cub-banner.webp" loading="lazy">
    <h2>Hotel Booking - Riget Zoo Adventures</h2>
    <form method="POST" action="" class="availability-panel">
        <h3 class="section-title">Book your stay</h3>
        <input type="date" name="date" id="date" class="input-field" required>
        <div class="bottom">
            <select required name="num_nights" id="num-nights" class="input-field">
                <option selected disabled value="">Nights</option>
                <?php for ($i = 1; $i <= 7; $i++) { echo "<option value='$i'>$i</option>"; }?>
            </select>
            <select required name="num_adults" id="num-adults" class="input-field">
                <option selected disabled value="">Adults</option>
                <?php for ($i = 1; $i <= 10; $i++) { echo "<option value='$i'>$i</option>"; }?>
            </select>
            <select required name="num_children" id="num-children" class="input-field">
                <option selected disabled value="">Children (0-15 yrs)</option>
                <?php for ($i = 0; $i <= 10; $i++) { echo "<option value='$i'>$i</option>"; }?>
            </select>
            <input type="submit" value="Complete" class="complete-btn" id="complete-submit">
        </div>
        <?php if (!isset($_SESSION['email'])) {
            echo <<<HTML
            <h3 class="warning">YOU MUST FIRST BE LOGGED IN TO BOOK A STAY</h3>
            <a href="account.php" class="tickets-btn">Login</a>
            HTML;
        }?>
    </form>
    <h3 class="wrap-short">LUXURY ACCOMMODATION WITH AN UNFORGETTABLE WILDLIFE EXPERIENCE</h3>
    <!-- <div class="slideshow-container">
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    </div> -->
</div>
<?php
include_once "assets/php/footer.php";
?>