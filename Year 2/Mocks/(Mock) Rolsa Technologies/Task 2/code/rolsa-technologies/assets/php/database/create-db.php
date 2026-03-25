<?php
include "db-handler.php";

function _create_table() {
    $db_handle = _connect_db();
    $query = "CREATE TABLE IF NOT EXISTS rolsa_users (
        id SERIAL PRIMARY KEY,
        email VARCHAR(255) NOT NULL UNIQUE,
        pass_hash VARCHAR(255) NOT NULL
    )";

    // execute the query
    $result = pg_query($db_handle, $query);

    // check if the table was created successfully
    if ($result) {
        echo "Table 'rolsa_users' created successfully!";
    } else {
        echo "Error creating table: " . pg_last_error($db_handle);
    }

    pg_close($db_handle);
}

_create_table();
?>