<?php
function _connect_db() {
    $_host = "DB_IP_ADDRESS";
    $_dbname = "DB_NAME";
    $_user = "DB_USERNAME";
    $_password = "DB_PASSWORD";

    // connect to db or something, idk i'm not a programmer
    $db_handle = pg_connect("host=$_host dbname=$_dbname user=$_user password=$_password");

    if ($db_handle) {
        // echo "Yay something works!<br>";
    } else {
        die("Connection died: ".pg_last_error());
        // echo "DB_NAME tried to swim in lava.<br>";
        echo "Something died... So now the CSS joins it :D";
    }
    return $db_handle;
}
?>