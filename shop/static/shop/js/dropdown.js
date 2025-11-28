document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".drop-btn");

    buttons.forEach(btn => {
        btn.addEventListener("click", () => {
            const drop = btn.nextElementSibling;

            // Close other dropdowns
            document.querySelectorAll(".drop-content").forEach(d => {
                if (d !== drop) d.classList.remove("show");
            });

            // Toggle this one
            drop.classList.toggle("show");
        });
    });

    // Close dropdown if clicking outside
    document.addEventListener("click", (e) => {
        if (!e.target.closest(".filter-box")) {
            document.querySelectorAll(".drop-content").forEach(d => d.classList.remove("show"));
        }
    });
});
