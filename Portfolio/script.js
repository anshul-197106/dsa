// THEME TOGGLE
const toggle = document.getElementById("themeToggle");
const html = document.documentElement;

toggle.onclick = () => {
  html.classList.toggle("light");
  toggle.textContent = html.classList.contains("light") ? "☀️" : "🌙";
};

// ACTIVE NAV + SCROLL ANIMATION
const sections = document.querySelectorAll("section");
const navLinks = document.querySelectorAll(".nav a");
const reveals = document.querySelectorAll(".reveal");

window.addEventListener("scroll", () => {
  let current = "";

  sections.forEach(sec => {
    const top = window.scrollY;
    const offset = sec.offsetTop - 150;
    const height = sec.offsetHeight;

    if (top >= offset && top < offset + height) {
      current = sec.getAttribute("id");
    }
  });

  navLinks.forEach(a => {
    a.classList.remove("active");
    if (a.getAttribute("href") === `#${current}`) {
      a.classList.add("active");
    }
  });

  reveals.forEach(el => {
    const rect = el.getBoundingClientRect().top;
    if (rect < window.innerHeight - 100) {
      el.classList.add("active");
    }
  });
});
