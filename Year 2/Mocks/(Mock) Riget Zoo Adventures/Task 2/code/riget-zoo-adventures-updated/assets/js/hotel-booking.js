document.addEventListener("DOMContentLoaded", (e) => {
    const date_selector = document.getElementById("date");

    const today = new Date();
    const todayISO = today.toISOString().split('T')[0];

    date_selector.setAttribute("min", todayISO);
    date_selector.value = todayISO;
});