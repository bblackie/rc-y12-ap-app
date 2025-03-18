document.addEventListener("DOMContentLoaded", function () {
  console.log("JavaScript loaded!");

  // Initialize flatpickr for release date inputs
  var releaseDateMinInput = document.getElementById("release-date-min");
  if (releaseDateMinInput) {
    flatpickr(releaseDateMinInput, {
      dateFormat: "Y-m-d",
      minDate: "2000-01-01",
      maxDate: "2024-12-31",
    });
  }
  var releaseDateMaxInput = document.getElementById("release-date-max");
  if (releaseDateMaxInput) {
    flatpickr(releaseDateMaxInput, {
      dateFormat: "Y-m-d",
      minDate: "2000-01-01",
      maxDate: "2024-12-31",
    });
  }
});
