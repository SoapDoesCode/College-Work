<?php
$page_name = "Homepage";
$include_navbar = true;
include_once "assets/php/header.php";
?>
<div class="content">
    <img class="banner-img" src="assets/media/webp/homepage-banner.webp" loading="lazy">
    <p class="short-desc">This is a short description about Riget Zoo Adventures. Lorem ipsum dolor sit amet consectetur adipiscing elit. Consectetur adipiscing elit quisque faucibus ex sapien vitae. Ex sapien vitae pellentesque sem placerat in id.</p>
    <div class="link-container">
        <div class="link-row-top">
            <div class="green-link link-item">Open daily from 10am</div>
            <a class="yellow-link link-item" href="zoo-booking.php">Book tickets</a>
            <div class="green-link link-item">Upcoming events</div>
        </div>
        <div class="link-row-bottom">
            <a class="yellow-link link-item" href="account.php">Create an account</a>
            <a class="green-link link-item" href="about.php">More about us</a>
            <a class="yellow-link link-item" href="attractions.php">Attractions and facilities</a>
        </div>
    </div>
    <h2>New attractions</h2>
    <div class="attractions-container">
        <div class="attraction-card">
            <img src="assets/media/webp/attractions/tiger-keeper.webp" loading="lazy" alt="A picture of a tiger playing" class="attraction-img">
            <a href="attractions.php" class="attraction-link">(NEW) Tiger Keeper Experience<i class="fa-solid fa-circle-arrow-right"></i></a><br>
            <span>Experience what it takes to be a tiger keeper in this truly unique experience.</span>
        </div>
        <div class="attraction-card">
            <img src="assets/media/webp/attractions/penguin-keeper.webp" loading="lazy" alt="A picture of some penguins swimming" class="attraction-img">
            <a href="attractions.php" class="attraction-link">(NEW) Penguin Keeper Experience<i class="fa-solid fa-circle-arrow-right"></i></a><br>
            <span class="attraction-desc">Join us as an honorary zookeeper for a flipping good time!</span>
        </div>
        <div class="attraction-card">
            <img src="assets/media/webp/attractions/komodo-dragon.webp" loading="lazy" alt="A picture of a komodo dragon" class="attraction-img">
            <a href="attractions.php" class="attraction-link">(NEW) The Komodo Dragon<i class="fa-solid fa-circle-arrow-right"></i></a><br>
            <span>Experience what it takes to be a Komodo dragon keeper in this truly unique experience.</span>
        </div>
    </div>
</div>
<?php
include_once "assets/php/footer.php";
?>