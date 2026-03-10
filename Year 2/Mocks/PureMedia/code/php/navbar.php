<!-- we kinda need this, else icons go funky... -->
<script
    src="https://kit.fontawesome.com/53a7d708ca.js"
    crossorigin="anonymous"
></script>
<script src="js/navbar.js"></script>

<header>
    <nav class="navbar">
        <div class="navbar-links-left">
            <a href="" id="navbar-title">YUNGBLUD</a> <!-- href="" takes us to the home page -->
            <div id="venues-dropdown">
                <button id="venues-btn">
                    VENUES<i class="fa-solid fa-chevron-down"></i>
                </button>
                <div class="venues-content">
                    <?php
                    require_once "php/db.php";
                    foreach (find_all_cities() as $city) {
                        $city_lower = strtolower($city);
                        $city_upper = strtoupper($city);
                        echo "<a href='?venue=$city'>$city_upper</a>";
                    }
                    ?>
                </div>
            </div>
            <a href="merch.php" id="merch-btn">MERCH</a>
            <a href="about.php" id="about-btn">ABOUT</a>
        </div>
        <div class="navbar-links-right">
            <a href="account.php" id="account-btn"><i class="fa-solid fa-user"></i></a>
            <a href="basket.php" id="basket-btn"
                ><i class="fa-solid fa-cart-shopping"></i
            ></a>
        </div>
    </nav>
</header>
<!-- look into https://www.w3schools.com/css/css3_shadows_box.asp -->
