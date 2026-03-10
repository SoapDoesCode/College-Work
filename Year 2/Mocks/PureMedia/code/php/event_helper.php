<?php

function get_event_html(array $event) {
    // echo "city: " . $event['city'] . "<br>";
    // echo "venue: " . $event['venue'] . "<br>";
    // echo "date_time: " . $event['date_time'] . "<br>";
    // echo "img_url: " . $event['img_url'] . "<br>";
    // echo "min_price: " . $event['min_price'] . "<br>";
    // echo "max_price: " . $event['max_price'] . "<br>";
    // echo "<br>";

    // oooooo heredoc :D
    return <<<HTML
    <a href="https://http.cat/200" style="text-decoration: none;">
        <div class="event">
            <img src="{$event['img_url']}" class="event-img" onerror="this.onerror=null; this.src='https://httpducks.com/404.jpg';" loading="lazy"/>
            <span class="caption">{$event['venue']}, {$event['city']}<br>
            {$event['date_time']}<br>
            £{$event['min_price']}-{$event['max_price']}</span>
        </div>
    </a>
    HTML;
}

?>