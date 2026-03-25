function highlightCurrentPage() {
    let page = document.title.replace("Health Advice Group - ", "")

    if (page === "Home Page") {
        document.getElementById("home-btn").classList.add("underline");
    } else if (page === "Articles") {
        document.getElementById("articles-btn").classList.add("underline");
    } else if (page === "Weather") {
        document.getElementById("weather-btn").classList.add("underline");
    } else if (page === "Account") {
        document.getElementById("account-btn").classList.add("underline");
    } else if (page === "About") {
        document.getElementById("about-btn").classList.add("underline");
    }
}

document.addEventListener("DOMContentLoaded", () => {
    console.log("DOM fully loaded and parsed");
    
    highlightCurrentPage();
});