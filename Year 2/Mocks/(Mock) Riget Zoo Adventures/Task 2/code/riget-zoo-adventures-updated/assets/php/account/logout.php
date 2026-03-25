<?php 
session_start(); // start the session
session_destroy(); // destroy the session
header("Location: http://tldnc.co.uk/2025-2026/td2s/233753/riget-zoo-adventures-updates/account.php"); // Redirect to the accounts page
exit(); // ensure no further code is executed
?>