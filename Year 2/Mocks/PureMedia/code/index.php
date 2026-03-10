<?php
$venue = !empty($_GET['venue']) ? $_GET['venue'] : NULL;

$page_title = (is_null($venue)) ? "Home Page" : $venue;;
$include_navbar = true; /* optional (defaults to true if left undefined) */
include_once "php/header.php";
include_once "php/db.php";
include_once "php/event_helper.php";

if (is_null($venue)) {
    $events_html = "";
    foreach (find_events() as $event) {
        $events_html .= get_event_html($event);
    }

    $videos = ['ozzy-osbourne', 'idols'];
    $video_idx = array_rand($videos);
    $rand_video = $videos[$video_idx];

    echo <<<HTML
    <main class="content">
        <video autoplay muted loop playsinline preload="auto" class="banner-video"><source src="img/banner-videos/$rand_video.webm" poster="img/banner-videos/$rand_video.webp" type="video/webm" loading="lazy" onerror="this.onerror=null; this.src='https://httpducks.com/404.jpg';"></video>
        <h1 class="events-title">Upcoming Events</h1>
        <div class="events">
            $events_html
        </div>
    </main>
    HTML;
} else {
    $events_html = "";

    // if the venue exists, find all events at that venue
    if (in_array($venue, find_all_cities())) {
        foreach (find_events($venue) as $event) {
            $events_html .= get_event_html($event);
        }
    } else {
        $events_html = "<h1>There are no events in $venue</h1>";
    }

    echo <<<HTML
    <main class="content">
        <h1 class="events-title">Events in $venue</h1>
        <div class="events">
            $events_html
        </div>
    </main>
    HTML;
}
?>




<!-- <?php
echo "<h1>" . $venue . "</h1>";
?> -->

<?php include "php/footer.php";
// no blasphemy today :D ?>