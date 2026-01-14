const body = document.body;
const btn = document.getElementById("themeToggle");

const savedTheme = localStorage.getItem("deeps4cast-theme") || "scientific";
body.setAttribute("data-theme", savedTheme);

btn.addEventListener("click", () => {
    const current = body.getAttribute("data-theme");
    const next = current === "scientific" ? "modern" : "scientific";

    body.setAttribute("data-theme", next);
    localStorage.setItem("deeps4cast-theme", next);
});
