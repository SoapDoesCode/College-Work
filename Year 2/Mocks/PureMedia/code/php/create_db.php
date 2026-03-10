<?php

include "db.php";

// $create_db_query = "DROP TABLE puremedia_yungblud;
// CREATE TABLE IF NOT EXISTS puremedia_yungblud (
//     id SERIAL PRIMARY KEY,
//     city VARCHAR(255) NOT NULL,
//     venue VARCHAR(255) NOT NULL,
//     date_time VARCHAR(255) NOT NULL,
//     img_url VARCHAR(255) NOT NULL,
//     min_price DECIMAL NOT NULL,
//     max_price DECIMAL NOT NULL
// )";

$create_events_db = "CREATE TABLE IF NOT EXISTS puremedia_yungblud_events (
    id SERIAL PRIMARY KEY,
    city VARCHAR(255) NOT NULL,
    venue VARCHAR(255) NOT NULL,
    date_time VARCHAR(255) NOT NULL,
    img_url VARCHAR(255) NOT NULL,
    min_price DECIMAL NOT NULL,
    max_price DECIMAL NOT NULL
)";

$create_merch_db = "CREATE TABLE IF NOT EXISTS puremedia_yungblud_merch (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    img_url VARCHAR(255) NOT NULL,
    price DECIMAL NOT NULL
)";

run_sql_query($create_events_db);
run_sql_query($create_merch_db);

?>
