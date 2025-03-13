// static/js/main.js

// When the DOM is fully loaded, execute the following code
document.addEventListener("DOMContentLoaded", function () {
  // Log to the console to confirm that the JavaScript file has been loaded
  console.log("JavaScript loaded!");

  // Select elements that will have the fade-in effect
  const fadeElems = document.querySelectorAll(
    ".btn-fade, .home-container, .search-page, .game-detail-container"
  );

  // Loop over each selected element
  fadeElems.forEach((elem) => {
    // Set initial opacity to 0 (invisible)
    elem.style.opacity = 0;
    // After a short delay, apply the transition effect to fade in the element
    setTimeout(() => {
      elem.style.transition = "opacity 1s";
      elem.style.opacity = 1; // Fade the element in to full opacity
    }, 100); // 100ms delay before starting the fade-in
  });
});
