        <footer>
            <a href="" class="footer-logo">YUNGBLUD</a>
            <div class="socials">
                <a href="https://www.youtube.com/@yungblud" rel="noopener" target="_blank" class="youtube"></a>
                <a href="https://music.apple.com/us/artist/yungblud/213048599" rel="noopener" target="_blank" class="apple-music"></a>
                <a href="https://www.deezer.com/en/artist/12133088" rel="noopener" target="_blank" class="deezer"></a>
                <a href="https://www.facebook.com/yungblud" rel="noopener" target="_blank" class="facebook"></a>
                <a href="https://www.instagram.com/yungblud" rel="noopener" target="_blank" class="instagram"></a>
                <a href="https://open.spotify.com/artist/6Ad91Jof8Niiw0lGLLi3NW" rel="noopener" target="_blank" class="spotify"></a>
            </div>
            <p>Made with <span class="heart">♥</span> for Yungblud</p>
            <p>&copy; 2025 Yungblud demo site by SoapDoesCode.<br>All rights reserved.</p>
        </footer>
        <?php
        // we can do stuff for specific pages now :D
        switch (strtolower($page_title)) {
            case "account":
                echo "<script src='js/account.js'></script>";
                break;
            default:
                // we don't care...currently
                break;
        }
        ?>
    </body>
</html>