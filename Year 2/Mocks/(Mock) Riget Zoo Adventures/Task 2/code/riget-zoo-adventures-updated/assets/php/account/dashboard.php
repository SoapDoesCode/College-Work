<?php
$page_name = "Account Dashboard";
$include_navbar = true;
$navbar_pad_fix = true;
include_once "assets/php/header.php";
include_once "assets/php/database/db-handler.php";
?>
<div class="content">
    <div id="navbar-pad"></div>
    <h1>LOGGED IN</h1>
    <h3>Your email: <?= $_SESSION['email'] ?></h3>
    <a href="assets/php/account/logout.php" class="tickets-btn">Log out</a>
    <h2>Your hotel bookings:</h2>
    <?php
    $bookings = get_all_hotel_bookings($_SESSION['email']);
    // $bookings = $_SESSION['email'];
    if (empty($bookings)) {
        echo "<h3>No hotel bookings found</h3>";
    } else {
        foreach ($bookings as $booking) {
            ?>
            <div class="booking">
                <h3>Room <?= htmlspecialchars($booking['hotel_room_no']) ?></h3>
                <p>Date: <?= htmlspecialchars($booking['booking_date']) ?></p>
                <p>Duration: <?= htmlspecialchars($booking['duration']) ?> nights</p>
                <p>Guests:
                    <?= htmlspecialchars($booking['num_adults']) ?> adults,
                    <?= htmlspecialchars($booking['num_children']) ?> children
                </p>
            </div>
            <?php
        }
    }
    ?>
    <h2>Your zoo tickets:</h2>
    <?php
    $tickets = get_all_zoo_tickets($_SESSION['email']);
    if (empty($tickets)) {
        echo "<h3>No zoo tickets found</h3>";
    } else {
        foreach ($tickets as $ticket) {
            ?>
            <div class="booking">
                <h3>Date: <?= htmlspecialchars($ticket['booking_date']) ?></h3>
                <p>Guests:
                    <?= htmlspecialchars($ticket['num_adults']) ?> adults,
                    <?= htmlspecialchars($ticket['num_children']) ?> children
                </p>
            </div>
            <?php
        }
    }
    ?>
</div>
<?php
include_once "assets/php/footer.php";
?>