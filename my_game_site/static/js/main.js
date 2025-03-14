document.addEventListener("DOMContentLoaded", function () {
  console.log("JavaScript loaded!");

  // Fade-in effect for selected elements
  const fadeElems = document.querySelectorAll(
    ".btn-fade, .home-container, .search-page, .game-detail-container"
  );
  fadeElems.forEach((elem) => {
    elem.style.opacity = 0;
    setTimeout(() => {
      elem.style.transition = "opacity 1s";
      elem.style.opacity = 1;
    }, 100);
  });

  // Initialize flatpickr for minimum release date input
  var releaseDateMinInput = document.getElementById("release-date-min");
  if (releaseDateMinInput) {
    flatpickr(releaseDateMinInput, {
      dateFormat: "Y-m-d",
      minDate: "2000-01-01",
      maxDate: "2024-12-31",
    });
  }

  // Initialize flatpickr for maximum release date input
  var releaseDateMaxInput = document.getElementById("release-date-max");
  if (releaseDateMaxInput) {
    flatpickr(releaseDateMaxInput, {
      dateFormat: "Y-m-d",
      minDate: "2000-01-01",
      maxDate: "2024-12-31",
    });
  }
});
