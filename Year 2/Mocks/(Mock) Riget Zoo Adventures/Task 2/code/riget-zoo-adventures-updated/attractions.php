<?php
$page_name = "Attractions";
$include_navbar = true;
include_once "assets/php/header.php";
?>
<div class="content">
    <img class="banner-img" src="assets/media/webp/attractions-banner-penguin.webp" loading="lazy" alt="A picture of a penguin swimming">
    <h2>Our attractions</h2>
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
        <div class="attraction-card">
            <img src="assets/media/webp/attractions/meet-the-meerkats.webp" loading="lazy" alt="A picture of some penguins swimming" class="attraction-img">
            <a href="attractions.php" class="attraction-link">Meet the Meerkats<i class="fa-solid fa-circle-arrow-right"></i></a><br>
            <span class="attraction-desc">Feed our meerkat family some tasty snacks!</span>
        </div>
        <div class="attraction-card">
            <img src="assets/media/webp/attractions/meet-the-monkeys.webp" loading="lazy" alt="A picture of a tiger playing" class="attraction-img">
            <a href="attractions.php" class="attraction-link">Meet the Monkeys<i class="fa-solid fa-circle-arrow-right"></i></a><br>
            <span>Step into our Rainforest to feed our monkeys some tasty snacks and support our conservation efforts to protect their habitats.</span>
        </div>
        <div class="attraction-card">
            <img src="assets/media/webp/attractions/capybara-encounter.webp" loading="lazy" alt="A picture of some penguins swimming" class="attraction-img">
            <a href="attractions.php" class="attraction-link">Capybara Encounter<i class="fa-solid fa-circle-arrow-right"></i></a><br>
            <span class="attraction-desc">Learn all about our capybaras, their unique personalities, discover the science of positive reinforcement training, and help out with a training session.</span>
        </div>
    </div>
</div>
<?php
include_once "assets/php/footer.php";
?>