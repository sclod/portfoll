// Переключатель теми: темна за замовчуванням, світла — за вибором, вибір запам'ятовується.
(function () {
  var root = document.documentElement;
  var button = document.querySelector(".theme-toggle");
  var meta = document.querySelector('meta[name="theme-color"]');
  if (!button) return;

  function apply(theme) {
    root.dataset.theme = theme;
    button.setAttribute("aria-pressed", String(theme === "light"));
    if (meta) meta.content = theme === "light" ? "#f7f7f4" : "#0e1116";
  }

  apply(root.dataset.theme === "light" ? "light" : "dark");
  button.hidden = false;

  button.addEventListener("click", function () {
    var next = root.dataset.theme === "light" ? "dark" : "light";
    apply(next);
    try { localStorage.setItem("theme", next); } catch (e) {}
  });
})();
