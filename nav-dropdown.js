// Smooth Header Dropdown Navigation with Debounce Buffer
document.addEventListener('DOMContentLoaded', function () {
  var dropdowns = document.querySelectorAll('.dropdown');
  
  dropdowns.forEach(function (dropdown) {
    var timeoutId = null;
    var trigger = dropdown.querySelector('a');

    dropdown.addEventListener('mouseenter', function () {
      if (timeoutId) clearTimeout(timeoutId);
      dropdown.classList.add('is-open');
    });

    dropdown.addEventListener('mouseleave', function () {
      timeoutId = setTimeout(function () {
        dropdown.classList.remove('is-open');
      }, 250); // 250ms grace period so moving mouse down never snaps closed
    });

    // Mobile touch toggle
    if (trigger) {
      trigger.addEventListener('click', function (e) {
        if (window.innerWidth <= 768) {
          e.preventDefault();
          dropdown.classList.toggle('is-open');
        }
      });
    }
  });

  // Close on click outside
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.dropdown')) {
      dropdowns.forEach(function (d) {
        d.classList.remove('is-open');
      });
    }
  });
});

