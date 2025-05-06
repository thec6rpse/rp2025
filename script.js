document.addEventListener("DOMContentLoaded", () => {
    const links = document.querySelectorAll("a[href^='#']");
    const sections = document.querySelectorAll("div[id]");

    links.forEach(link => {
        link.addEventListener("click", () => {
            // Remove highlight from all sections
            sections.forEach(section => section.classList.remove("highlight"));

            // Highlight the target section
            const targetId = link.getAttribute("href").substring(1);
            const targetSection = document.getElementById(targetId);
            if (targetSection) {
                targetSection.classList.add("highlight");
            }
        });
    });
});