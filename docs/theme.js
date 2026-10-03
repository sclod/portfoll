// Переключатель теми: темна за замовчуванням, світла — за вибором, вибір запам'ятовується.
(function () {
  var root = document.documentElement;
  var button = document.querySelector(".theme-toggle");
  if (!button) return;
  var name = button.querySelector(".theme-name");
  var hint = button.querySelector(".visually-hidden");
  var meta = document.querySelector('meta[name="theme-color"]');

  function apply(theme) {
    var light = theme === "light";
    root.dataset.theme = theme;
    name.textContent = light ? "світла" : "темна";
    hint.textContent = light ? ". Увімкнути темну" : ". Увімкнути світлу";
    if (meta) meta.content = light ? "#f4f6fb" : "#07090d";
  }

  apply(root.dataset.theme === "light" ? "light" : "dark");
  button.hidden = false;

  button.addEventListener("click", function () {
    var next = root.dataset.theme === "light" ? "dark" : "light";
    apply(next);
    try { localStorage.setItem("theme", next); } catch (e) {}
  });
})();
