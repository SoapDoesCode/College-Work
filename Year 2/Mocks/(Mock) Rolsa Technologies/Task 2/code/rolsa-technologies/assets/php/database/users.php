<?php
include_once "db-handler.php";

function user_exists($user_email) {
    $db_handle = _connect_db(); // open database connection so we can talk to it

    $query = "SELECT COUNT(1) FROM rolsa_users WHERE email = $1";

    // using pg_query_params as this mitigates the risk of SQL injection
    $result = pg_query_params($db_handle, $query, array($user_email));

    $row = pg_fetch_row($result); // convert the data to an associative array (dictionary) for easier processing
    $count = $row[0];

    pg_close($db_handle); // close database connection
    return ($count > 0); // return true if the user exists, else false
}

function register_user($user_email, $user_pass, $user_confirm_pass) {
    $user_email = strtolower($user_email);
    if (user_exists($user_email)) {
        return "An account with that email already exists";
    } else if ($user_pass !== $user_confirm_pass) {
        return "Passwords do not match";
    } else {
        $db_handle = _connect_db(); // open database connection

        $pass_hash = password_hash($user_pass, PASSWORD_ARGON2ID); // hash the password using the Argon2ID algorithm

        $register_query = "INSERT INTO rolsa_users (email, pass_hash) VALUES ('$user_email', '$pass_hash')";
        $result = pg_query($db_handle, $register_query);

        pg_close($db_handle); // close the database connection

        if ($result) {
            return null; // success, so return no error message
        } else {
            return "Failed to register user"; // failed, return an error
        }
    }
}

function login_user($user_email, $user_pass) {
    if (!user_exists($user_email)) {
        return "Incorrect email or password"; // user input incorrect details, return error
    }
    $db_handle = _connect_db(); // connect to the database

    $user_email = strtolower($user_email); // emails are case-insensitive, to cast it to lowercase

    $query = "SELECT pass_hash FROM rolsa_users WHERE email = $1";

    // using pg_query_params as this mitigates the risk of SQL injection
    $result = pg_query_params($db_handle, $query, array($user_email));

    $row = pg_fetch_assoc($result); // convert the data to an associative array (dictionary) for easier processing

    pg_close($db_handle); // close the database connection

    // check if the password hash matches the user's password hash
    if (password_verify($user_pass, $row['pass_hash'])) {
        return "success"; // success :D
    } else {
        return "Incorrect email or password"; // user input incorrect details, return error
    }
}

// echo register_user("soap@sillies.dev", "password123", "password123");
// register_user($_POST['register_email'], $_POST['register_pass'], $_POST['register_confirm_pass']);
?>