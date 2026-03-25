// wait until the DOM is fully parsed before doing anything
document.addEventListener("DOMContentLoaded", () => {
    window.addEventListener("load", function() {
        // select the navbar's container element (light green background)
        let navbar_pad = document.getElementById("navbar-container");

        // if the navbar pad is present (it should be)
        if (navbar_pad) {
            // get the height of the navbar (including padding)
            let navbar = document.getElementById("navbar");
            let navbar_height = navbar.offsetHeight;
            let navbar_margin = parseFloat(getComputedStyle(navbar).marginTop) + parseFloat(getComputedStyle(navbar).marginBottom);
            let extra_pad = 2 * parseFloat(getComputedStyle(navbar).top);

            let navbar_pad_size = navbar_height + navbar_margin + extra_pad;

            // set the height of the #navbar-pad div to match the navbar's height
            navbar_pad.style.paddingTop = navbar_pad_size+"px";
        }
    });
});