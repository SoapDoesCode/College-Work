document.addEventListener("DOMContentLoaded", () => {
    console.log("DOM fully loaded and parsed");
    
    window.addEventListener('load', function() {
        let navbar_pad = document.getElementById("navbar-pad");
        if (navbar_pad) {
            // get the height of the navbar (including padding)
            let navbar = document.getElementById("navbar")
            let navbar_height = navbar.offsetHeight;
            let navbar_margin = parseFloat(getComputedStyle(navbar).marginTop) + parseFloat(getComputedStyle(navbar).marginBottom);

            let navbar_pad_size = navbar_height + navbar_margin;

            // set the height of the #navbar-pad div to match the navbar's height
            navbar_pad.style.paddingTop = navbar_pad_size+"px";
        }
    });
});