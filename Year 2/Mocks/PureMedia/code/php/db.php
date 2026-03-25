<?php

function _connect_db() {
    $_host = "IP ADDRESS";
    $_dbname = "DB NAME";
    $_user = "USER NAME";
    $_password = "PASSWORD";

    // connect to db or something, idk i'm not a programmer
    $db_handle = pg_connect("host=$_host dbname=$_dbname user=$_user password=$_password");

    if ($db_handle) {
        // echo "Yay something works!<br>";
    } else {
        die("Connection died: " . pg_last_error());
        // echo "DB_NAME tried to swim in lava.<br>";
    }
    return $db_handle;
}

function run_sql_query(string $query) {
    $db_handle = _connect_db();

    $result = pg_query($db_handle, $query);

    pg_close($db_handle); // we don't wanna leave this open :D
    return $result; // kinda needed ngl
}

function find_all_cities() {
    $db_result = run_sql_query("SELECT city FROM puremedia_yungblud_events");

    $cities = [];

    while ($row = pg_fetch_assoc($db_result)) {
        $city = $row['city'];

        if (in_array($city, $cities)) { // check if the city is in the cities array
            // echo "$city already in cities<br>";
        } else { // add the city to the cities array if it isn't already
            // echo "adding $city to cities<br>";
            $cities[] = $city; // add the city to the cities array
        }
    }
    // var_dump($cities);
    return $cities;
}

function find_events(string $city = "all") {
    if ($city == "all") {
        $db_result = run_sql_query("SELECT * FROM puremedia_yungblud_events");
    } else {
        $db_result = run_sql_query("SELECT * FROM puremedia_yungblud_events WHERE city = '$city'");
    }

    $events = [];

    while ($row = pg_fetch_assoc($db_result)) {
        $events[] = $row;
        /* echo "city: " . $row['city'] . "<br>";
        echo "venue: " . $row['venue'] . "<br>";
        echo "date_time: " . $row['date_time'] . "<br>";
        echo "img_url: " . $row['img_url'] . "<br>";
        echo "min_price: " . $row['min_price'] . "<br>";
        echo "max_price: " . $row['max_price'] . "<br>";
        echo "<br>"; */
    }
    // var_dump($events);
    return $events;
}

// find_all_cities();
// load_events("all");

?>
