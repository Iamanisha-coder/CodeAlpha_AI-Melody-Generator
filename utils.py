import random
import os
from datetime import datetime

# =====================================
# AI Song Titles
# =====================================

SONG_TITLES = {
    "Classical": [
        "Moonlight Sonata AI",
        "Golden Symphony",
        "Royal Harmony",
        "Crystal Waltz",
        "Eternal Melody"
    ],

    "Lo-Fi": [
        "Midnight Rain",
        "Coffee & Clouds",
        "Dreaming Alone",
        "Neon Window",
        "City Lights"
    ],

    "Jazz": [
        "Blue Velvet",
        "Night Sax",
        "Smooth Groove",
        "Golden Trumpet",
        "Velvet Nights"
    ],

    "Rock": [
        "Thunder Road",
        "Fire Strings",
        "Echo Riot",
        "Wild Horizon",
        "Electric Storm"
    ],

    "EDM": [
        "Neon Pulse",
        "Electric Sky",
        "Future Bass",
        "Infinity Beat",
        "Cosmic Energy"
    ],

    "Ambient": [
        "Forest Whisper",
        "Ocean Breeze",
        "Silent Horizon",
        "Nature Dreams",
        "Morning Mist"
    ]
}


# =====================================
# Genre Descriptions
# =====================================

DESCRIPTIONS = {
    "Classical": "Elegant orchestral melodies inspired by timeless composers.",
    "Lo-Fi": "Relaxing beats perfect for studying and unwinding.",
    "Jazz": "Smooth improvisations with warm harmonies.",
    "Rock": "Powerful guitar-driven melodies full of energy.",
    "EDM": "Electronic dance rhythms with futuristic vibes.",
    "Ambient": "Calm atmospheric soundscapes inspired by nature."
}


# =====================================
# Random Song Title
# =====================================

def generate_song_title(genre):
    return random.choice(
        SONG_TITLES.get(genre, ["AI Melody"])
    )


# =====================================
# Genre Description
# =====================================

def genre_description(genre):
    return DESCRIPTIONS.get(
        genre,
        "AI Generated Music"
    )


# =====================================
# Random Album Color
# =====================================

def album_color():

    colors = [
        "#6C63FF",
        "#00D2FF",
        "#FF6B6B",
        "#FFD93D",
        "#4CAF50",
        "#9C27B0"
    ]

    return random.choice(colors)


# =====================================
# Create Output Folder
# =====================================

def create_output_folder():

    os.makedirs(
        "generated_music",
        exist_ok=True
    )


# =====================================
# File Name
# =====================================

def generate_filename():

    now = datetime.now()

    return f"AI_Music_{now.strftime('%Y%m%d_%H%M%S')}.mid"


# =====================================
# Music Statistics
# =====================================

def music_stats():

    return {
        "notes": random.randint(180, 450),
        "tempo": random.randint(80, 160),
        "quality": random.randint(94, 100),
        "confidence": random.randint(95, 99)
    }


# =====================================
# Mood Quotes
# =====================================

def ai_quote():

    quotes = [

        "🎵 Every melody begins with a single note.",

        "🎶 AI is composing your imagination.",

        "🎼 Music connects hearts beyond words.",

        "🎧 Let the rhythm tell your story.",

        "🎹 Artificial Intelligence meets creativity.",

        "🌌 Every generation creates a unique masterpiece."

    ]

    return random.choice(quotes)
