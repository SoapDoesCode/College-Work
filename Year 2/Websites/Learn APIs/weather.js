
const API_KEY = "API KEY";
const city = "CITY";

const weather_url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}&units=metric`;

async function get_weather() {
    try {
        const response = await fetch(weather_url);
        if (!response.ok) {
            throw new Error(`HTTP error!! Status: ${response.status}`);
        }

        const weather_data = await response.json();

        console.log("Weather Details:");
        console.log(`City: ${weather_data.name}`);
        console.log(`Temperature: ${weather_data.main.temp}°C`);
        console.log(`Weather: ${weather_data.weather[0].description}`);
        console.log(`Humidity: ${weather_data.main.humidity}%`);
        console.log(`Wind Speed: ${weather_data.wind.speed}m/s`);

        document.getElementById("weather").innerHTML = `
        <h2>Weather in ${weather_data.name}</h2>
        <p>Temperature: ${weather_data.main.temp}°C</p>
        <p>Weather: ${weather_data.weather[0].description}</p>
        <p>Humidity: ${weather_data.main.humidity}%</p>
        <p>Wind Speed: ${weather_data.wind.speed}m/s</p>
        `;
    } catch (error) {
        console.error("HAH SOMETHING DIED", error);
    }
}

get_weather();