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
        die("Connection died: " . pg_last_error());
        // echo "DB_NAME tried to swim in lava.<br>";
        echo "Something died... So now the CSS joins it :D";
    }
    return $db_handle;
}

function _run_sql_query($query) {
    $db_handle = _connect_db();

    $result = pg_query($db_handle, $query);

    pg_close($db_handle); // we don't want to leave this open
    return $result;
}

function user_exists($user_email) {
    $_conn = _connect_db();

    $query = "SELECT COUNT(1) FROM riget_users_updated WHERE email = $1";
    $result = pg_query_params($_conn, $query, array($user_email));

    $row = pg_fetch_row($result);
    $count = $row[0];

    pg_close($_conn);

    return ($count > 0);
}

function register_user($user_email, $user_pass, $user_confirm_pass) {
    $user_email = strtolower($user_email);
    if (user_exists($user_email)) {
        return "An account with that email already exists";
    } else if ($user_pass !== $user_confirm_pass) {
        return "Passwords do not match";
    } else {
        $pass_hash = password_hash($user_pass, PASSWORD_ARGON2ID);

        $register_query = "INSERT INTO riget_users_updated (email, pass_hash) VALUES ('$user_email', '$pass_hash')";

        $result = _run_sql_query($register_query);

        if ($result) {
            return null; // success, so return no error message
        } else {
            return "Failed to register user";
        }
    }
}

function login_user($user_email, $user_pass) {
    if (!user_exists($user_email)) {
        return "Incorrect email or password";
    }

    $user_email = strtolower($user_email);

    $_conn = _connect_db();

    $query = "SELECT pass_hash FROM riget_users_updated WHERE email = $1";
    $result = pg_query_params($_conn, $query, array($user_email));

    $row = pg_fetch_assoc($result);

    if (password_verify($user_pass, $row['pass_hash'])) {
        return "success";
    } else {
        return "Incorrect email or password";
    }
}

// function add_booking_to_account($email, $booking_id) {
//     $_conn = _connect_db();

//     $update_query = "
//         UPDATE riget_users
//         SET account_bookings = array_append(
//             COALESCE(account_bookings, '{}'),
//             $1
//         )
//         WHERE email = $2
//     ";

//     $result = pg_query_params($_conn, $update_query, array($booking_id, $email));

//     if (!$result) {
//         echo "Failed to update user's bookings.";
//         exit;
//     }

//     pg_close($_conn);
// }

function book_hotel($email, $hotel_room_no, $booking_date, $duration, $num_adults, $num_children) {
    $_conn = _connect_db();
    $booking_query = "INSERT INTO riget_bookings_updated (email, hotel_room_no, booking_date, duration, num_adults, num_children) VALUES ($1, $2, $3, $4, $5, $6)";

    $result = pg_query_params(
        $_conn,
        $booking_query,
        array($email, $hotel_room_no, $booking_date, $duration, $num_adults, $num_children)
    );

    if ($result) {
        return "success";
    } else {
        return "Failed to book hotel";
    }

    pg_close($_conn);
}

function book_zoo($email, $booking_date, $num_adults, $num_children) {
    $_conn = _connect_db();
    $booking_query = "INSERT INTO riget_zoo_tickets_updated (email, booking_date, num_adults, num_children) VALUES ($1, $2, $3, $4)";

    $result = pg_query_params(
        $_conn,
        $booking_query,
        array($email, $booking_date, $num_adults, $num_children)
    );

    if ($result) {
        return "success";
    } else {
        return "Failed to book zoo tickets";
    }

    pg_close($_conn);
}

function get_all_hotel_bookings($email) {
    $_conn = _connect_db();

    $query = "
        SELECT *
        FROM riget_bookings_updated
        WHERE email = $1
        ORDER BY booking_date ASC
    ";

    $result = pg_query_params($_conn, $query, array($email));

    if (!$result) {
        return []; // query failed
    }

    $bookings = [];
    while ($row = pg_fetch_assoc($result)) {
        $bookings[] = $row;
    }

    pg_close($_conn);
    return $bookings;
}

function get_all_zoo_tickets($email) {
    $_conn = _connect_db();

    $query = "
        SELECT *
        FROM riget_zoo_tickets_updated
        WHERE email = $1
        ORDER BY booking_date ASC
    ";

    $result = pg_query_params($_conn, $query, array($email));

    if (!$result) {
        return []; // query failed
    }

    $bookings = [];
    while ($row = pg_fetch_assoc($result)) {
        $bookings[] = $row;
    }

    pg_close($_conn);
    return $bookings;
}

?>