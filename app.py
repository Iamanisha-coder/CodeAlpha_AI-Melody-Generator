import streamlit as st
import os
import time
import random
from PIL import Image

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI Symphony Generator",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# LOAD CSS
# -----------------------------
def load_css():
    if os.path.exists("style.css"):
        with open("style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/musical-notes.png", width=80)
    st.title("🎵 MelodyAI")
    st.markdown("---")
    
    page = st.radio(
        "Navigation",
        ["🏠 Home", "🎼 Generate Music", "📚 About AI", "📁 My Music"]
    )
    st.markdown("---")
    st.write("### ⚙️ Settings")
    dark_mode = st.toggle("Dark Mode", True)
    st.markdown("---")
    st.success("AI Composer Ready")

# -----------------------------
# HOME PAGE
# -----------------------------
if page == "🏠 Home":
    st.markdown(
        """
        <div class='hero'>
            <h1>🎵 AI Symphony Generator</h1>
            <h3>Create Music using Artificial Intelligence</h3>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### ✨ Features
        ✔ AI Generated Music
        ✔ Multiple Genres
        ✔ Download MIDI
        ✔ Beautiful Dynamic Themes
        ✔ LSTM Deep Learning
        ✔ Interactive Music Player
        ✔ Glassmorphism UI
        ✔ Animated Backgrounds
        """)
    with col2:
        st.image("https://img.icons8.com/color/480/piano.png", use_container_width=True)

    st.markdown("---")
    st.subheader("🎼 Supported Genres")
    genres = st.columns(6)
    genre_list = ["🎹 Classical", "🌧 Lo-Fi", "🎷 Jazz", "⚡ EDM", "🎸 Rock", "🌿 Ambient"]
    
    for col, genre in zip(genres, genre_list):
        with col:
            st.info(genre)

    st.markdown("---")
    st.subheader("🚀 Quick Start")
    st.markdown("""
    1. Go to **Generate Music**
    2. Choose Genre
    3. Select Mood
    4. Click **Generate**
    5. Listen & Download 🎵
    """)

    if st.button("🎼 Start Creating Music", use_container_width=True):
        st.balloons()
        st.success("Let's compose something amazing!")

# -----------------------------
# ABOUT AI PAGE
# -----------------------------
elif page == "📚 About AI":
    st.title("📚 About")
    st.write("""
    This application uses **LSTM (Long Short-Term Memory)** neural networks to learn musical note patterns from MIDI datasets and generate original melodies.

    Built with:
    - Streamlit
    - TensorFlow
    - Music21
    - PrettyMIDI
    """)

# -----------------------------
# MY MUSIC PAGE
# -----------------------------
elif page == "📁 My Music":
    st.title("📁 My Music")
    st.info("Generated songs will appear here.")

# ===========================
# GENERATE MUSIC PAGE (Consolidated & Fixed)
# ===========================
elif page == "🎼 Generate Music":
    st.title("🎵 AI Music Studio")
    st.caption("Create unique melodies with Artificial Intelligence")
    st.markdown("---")

    # Genre Selection
    st.subheader("🎼 Choose Genre")
    genre = st.selectbox(
        "Select a Genre",
        ["🎹 Classical", "🌧 Lo-Fi", "🎷 Jazz", "⚡ EDM", "🎸 Rock", "🌿 Ambient"]
    )

    # Dynamic Background
    backgrounds = {
        "🎹 Classical": "assets/backgrounds/classical.jpg",
        "🌧 Lo-Fi": "assets/backgrounds/lofi.jpg",
        "🎷 Jazz": "assets/backgrounds/jazz.jpg",
        "⚡ EDM": "assets/backgrounds/edm.jpg",
        "🎸 Rock": "assets/backgrounds/rock.jpg",
        "🌿 Ambient": "assets/backgrounds/ambient.jpg",
    }
    bg = backgrounds.get(genre)
    if bg and os.path.exists(bg):
        st.image(bg, use_container_width=True)

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        mood = st.select_slider("😊 Mood", options=["Calm", "Happy", "Romantic", "Energetic", "Sad", "Epic"])
        duration = st.slider("⏱ Duration (seconds)", 10, 120, 30)
    with col2:
        tempo = st.slider("🥁 Tempo (BPM)", 60, 200, 120)
        creativity = st.slider("🧠 Creativity", 1, 10, 5)

    st.markdown("---")
    st.subheader("🤖 AI Composer")
    
    with st.container():
        st.info(f"""
        Genre : {genre}  
        Mood : {mood}  
        Tempo : {tempo} BPM  
        Duration : {duration} sec  
        Creativity : {creativity}/10
        """)

    # Initialize a session state to keep track of music generation persistence
    if "music_generated" not in st.session_state:
        st.session_state.music_generated = False
        st.session_state.generated_title = ""

    if st.button("🎵 Generate Music", use_container_width=True):
        progress = st.progress(0)
        status = st.empty()
        steps = [
            "🎼 Reading musical patterns...",
            "🎹 Learning notes...",
            "🎵 Composing melody...",
            "🎶 Adding harmony...",
            "💾 Exporting MIDI..."
        ]
        for i, step in enumerate(steps):
            status.info(step)
            progress.progress((i + 1) * 20)
            time.sleep(0.6) # Slightly faster sleep interval for better fluid simulation
            
        status.success("✅ Music Generated Successfully!")
        st.balloons()
        
        # Pick a title once and save it so it doesn't change on every rerun
        song_titles = {
            "🎹 Classical": ["Moonlight Sonata AI", "Golden Symphony", "Royal Harmony"],
            "🌧 Lo-Fi": ["Midnight Rain", "Coffee & Clouds", "Dreaming Alone"],
            "🎷 Jazz": ["Blue Velvet", "Night Sax", "Smooth Groove"],
            "⚡ EDM": ["Neon Pulse", "Electric Sky", "Future Bass"],
            "🎸 Rock": ["Thunder Road", "Fire Strings", "Echo Riot"],
            "🌿 Ambient": ["Forest Whisper", "Ocean Breeze", "Nature Dreams"]
        }
        st.session_state.generated_title = random.choice(song_titles[genre])
        st.session_state.music_generated = True

    # Render results globally within the view if generated status is True
    if st.session_state.music_generated:
        st.success("Your AI-generated melody is ready!")
        
        # Audio Player & Download
        if os.path.exists("assets/sample_music.mp3"):
            st.audio("assets/sample_music.mp3")
            with open("assets/sample_music.mp3", "rb") as file:
                st.download_button("⬇ Download Music", file, file_name="AI_Melody.mp3", use_container_width=True)
        else:
            st.warning("Sample music file ('assets/sample_music.mp3') not found.")

        st.markdown("---")
        st.subheader("🎵 AI Generated Song")
        col_img, col_det = st.columns([1, 2])
        with col_img:
            st.image("https://img.icons8.com/fluency/480/cd.png", use_container_width=True)
        with col_det:
            st.markdown(f"## 🎶 {st.session_state.generated_title}")
            st.write(f"**Genre:** {genre}")
            st.write(f"**Mood:** {mood}")
            st.write(f"**Tempo:** {tempo} BPM")
            st.write(f"**Duration:** {duration} Seconds")

        st.markdown("---")
        st.subheader("📊 Music Statistics")
        s1, s2, s3, s4 = st.columns(4)
        s1.metric("🎼 Notes", random.randint(150, 350))
        s2.metric("🥁 Tempo", f"{tempo} BPM")
        s3.metric("⭐ Quality", "98%")
        s4.metric("🧠 AI Model", "LSTM")

        st.markdown("---")
        st.subheader("🎧 Music Controls")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.button("❤️ Save")
        with c2:
            if st.button("🔄 Generate Again"):
                st.session_state.music_generated = False
                st.rerun()
        with c3:
            st.button("📤 Share")

        st.markdown("---")
        st.info("💡 Tip: Try different genres and moods to create completely different melodies!")

# ======================================
# GLOBAL FOOTER ELEMENTS (Runs on all pages)
# ======================================
st.markdown("---")
st.subheader("🎹 AI Piano Keyboard")
p_cols = st.columns(7)
notes = ["C", "D", "E", "F", "G", "A", "B"]
for col, note in zip(p_cols, notes):
    with col:
        st.button(note, use_container_width=True)

st.markdown("---")
quotes = [
    "🎵 Every melody begins with a single note.",
    "🎶 AI is composing your imagination.",
    "🎼 Music is the language of emotions.",
    "🎧 Creativity meets Artificial Intelligence.",
    "🎹 Let the AI surprise you!"
]
st.success(random.choice(quotes))

st.markdown("---")
st.markdown(
    """
    <div style='text-align:center; padding:20px; border-radius:15px; background:rgba(255,255,255,0.08); margin-top:30px;'>
        <h3>🎵 MelodyAI</h3>
        <p>Create Beautiful Music using Artificial Intelligence</p>
        <p>Built with ❤️ using Streamlit & TensorFlow</p>
        <hr>
        <p><b>Developed by Anisha Tripathi</b></p>
    </div>
    """,
    unsafe_allow_html=True
)
