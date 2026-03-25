    <!-- <h1>Footer loaded</h1> -->
    <footer>
        <span class="footer-title">Health Advice Group</span>
        <div class="footer-content">
            <div>
                <span>This should be on the left</span>
            </div>
            <div>
                <a href="about.php">About Us</a>
                <a href="terms-and-conditions.php">Terms and Conditions</a>
                <a href="cookie-policy.php">Cookies Policy</a>
            </div>
            <div>
                <span>This should be on the right</span>
            </div>
        </div>
    </footer>
    <?php if ($include_navbar) {
        echo '<script src="assets/js/navbar.js"></script>';
    }?>
</body>
</html>