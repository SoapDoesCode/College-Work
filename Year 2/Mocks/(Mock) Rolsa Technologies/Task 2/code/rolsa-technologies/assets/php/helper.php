<?php
// define the base path to this website on the server, makes referencing scripts and assets easier
$_domain = "http://tldnc.co.uk";
$_base_path = "/2025-2026/td2s/233753/rolsa-technologies/";
// $_base_path = "";

function redirect($url) {
    header("Location: ".$url); // redirect the client to the given url
    exit(); // stops all execution after the redirect, solves strange behaviour
}
?>