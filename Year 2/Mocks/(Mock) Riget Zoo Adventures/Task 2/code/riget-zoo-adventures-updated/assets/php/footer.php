    <!-- <footer>
    </footer> -->
    <?php if ($include_navbar) {
        echo '<script src="assets/js/navbar.js"></script>';
    }
    
    // use the page name to check which JavaScript to include
    switch (strtolower($page_name)) {
        case "login/register": // check if we're on the account page
            // load the JavaScript relevant to the account page
            echo '<script src="assets/js/account.js"></script>';
            break;
        case "plan your stay": // check if we're on the hotel booking page
        case "book tickets": // check if we're on the ticket booking page
            // load the JavaScript relevant to the hotel and ticket booking pages
            echo '<script src="assets/js/hotel-booking.js"></script>';
            break;
        default:
            // we don't need to load any JavaScript
            break;
        }
    ?>
</body>
</html>