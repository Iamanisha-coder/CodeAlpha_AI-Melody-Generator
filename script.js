// ================================
// MelodyAI - Dynamic Theme Script
// ================================

document.addEventListener("DOMContentLoaded", () => {

    const body = document.body;

    const themes = {
        "Classical": "linear-gradient(135deg,#F9D976,#F39F86)",
        "Lo-Fi": "linear-gradient(135deg,#4B79A1,#283E51)",
        "Jazz": "linear-gradient(135deg,#8E2DE2,#4A00E0)",
        "Rock": "linear-gradient(135deg,#232526,#414345)",
        "EDM": "linear-gradient(135deg,#00F260,#0575E6)",
        "Ambient": "linear-gradient(135deg,#56ab2f,#a8e063)"
    };

    function changeTheme(genre) {
        body.style.background = themes[genre];
        body.style.transition = "all 0.8s ease";
    }

    window.changeTheme = changeTheme;
});

// ================================
// Vinyl Animation
// ================================

function startVinyl() {
    const vinyl = document.getElementById("vinyl");
    if (vinyl) {
        vinyl.style.animation = "spin 3s linear infinite";
    }
}

function stopVinyl() {
    const vinyl = document.getElementById("vinyl");
    if (vinyl) {
        vinyl.style.animation = "none";
    }
}

// ================================
// Equalizer Animation
// ================================

function animateEqualizer() {

    const bars = document.querySelectorAll(".bar");

    setInterval(() => {

        bars.forEach(bar => {

            const height = Math.floor(Math.random() * 80) + 20;

            bar.style.height = height + "px";

        });

    }, 200);

}

// ================================
// Floating Notes
// ================================

function createMusicNote() {

    const note = document.createElement("div");

    note.innerHTML = "🎵";

    note.className = "music-note";

    note.style.left = Math.random() * window.innerWidth + "px";

    note.style.fontSize = (20 + Math.random() * 25) + "px";

    document.body.appendChild(note);

    setTimeout(() => {

        note.remove();

    }, 6000);

}

setInterval(createMusicNote, 1200);

// ================================
// Confetti
// ================================

function celebration() {

    alert("🎉 Melody Generated Successfully!");

}
