<?php
$page_name = "Book tickets";
$include_navbar = true;
include_once "assets/php/header.php";
include_once "assets/php/database/db-handler.php";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_SESSION['email']) and isset($_POST['date']) and isset($_POST['num_adults']) and isset($_POST['num_children'])) {
        $booking_result = book_zoo($_SESSION['email'], $_POST['date'], $_POST['num_adults'], $_POST['num_children']);

        if ($booking_result === "success") {
            echo '<script>alert("Zoo tickets booked successfully! Redirecting to dashboard..."); window.location.href="account.php";</script>';
        }
    }
}
?>
<div class="content">
    <img class="banner-img" src="assets/media/webp/lion-cub-banner.webp" loading="lazy">
    <h2>Zoo Tickets Booking - Riget Zoo Adventures</h2>
    <h3>A great <span class="riget-green">day out</span> for the whole family!</h3>
    <p class="short-desc">This is a short description about Riget Zoo Adventures and what you'll see Lorem ipsum dolor sit amet consectetur adipiscing elit. Consectetur adipiscing elit quisque faucibus ex sapien vitae. Ex sapien vitae pellentesque sem placerat in id.</p>
    <form method="POST" action="" class="availability-panel">
        <h3 class="section-title">Book tickets</h3>
        <input type="date" name="date" id="date" class="input-field" required>
        <div class="bottom">
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
            <h3 class="warning">YOU MUST FIRST BE LOGGED IN TO BOOK TICKETS</h3>
            <a href="account.php" class="tickets-btn">Login</a>
            HTML;
        }?>
    </form>
</div>
<?php
include_once "assets/php/footer.php";
?>