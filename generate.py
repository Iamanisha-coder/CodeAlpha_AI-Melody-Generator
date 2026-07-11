import pickle
import numpy as np
import random

from music21 import instrument, note, stream, chord

from tensorflow.keras.models import load_model

# -------------------------------
# Load Model
# -------------------------------

model = load_model("models/music_model.h5")

# -------------------------------
# Load Notes
# -------------------------------

with open("models/notes.pkl", "rb") as f:
    notes = pickle.load(f)

pitchnames = sorted(set(notes))

note_to_int = {n: i for i, n in enumerate(pitchnames)}
int_to_note = {i: n for i, n in enumerate(pitchnames)}

sequence_length = 100

# -------------------------------
# Prepare Input
# -------------------------------

network_input = []

for i in range(len(notes) - sequence_length):
    sequence = notes[i:i + sequence_length]
    network_input.append([note_to_int[n] for n in sequence])

start = random.randint(0, len(network_input) - 1)

pattern = network_input[start]

prediction_output = []

# -------------------------------
# Generate Notes
# -------------------------------

for _ in range(300):

    prediction_input = np.reshape(
        pattern,
        (1, len(pattern), 1)
    )

    prediction_input = prediction_input / float(len(pitchnames))

    prediction = model.predict(prediction_input, verbose=0)

    index = np.argmax(prediction)

    result = int_to_note[index]

    prediction_output.append(result)

    pattern.append(index)
    pattern = pattern[1:]

# -------------------------------
# Convert to MIDI
# -------------------------------

offset = 0

output_notes = []

for pattern in prediction_output:

    if "." in pattern or pattern.isdigit():

        notes_in_chord = pattern.split(".")

        chord_notes = []

        for current_note in notes_in_chord:

            new_note = note.Note(int(current_note))

            new_note.storedInstrument = instrument.Piano()

            chord_notes.append(new_note)

        new_chord = chord.Chord(chord_notes)

        new_chord.offset = offset

        output_notes.append(new_chord)

    else:

        new_note = note.Note(pattern)

        new_note.offset = offset

        new_note.storedInstrument = instrument.Piano()

        output_notes.append(new_note)

    offset += 0.5

# -------------------------------
# Save MIDI
# -------------------------------

midi_stream = stream.Stream(output_notes)

midi_stream.write(
    "midi",
    fp="generated_music/AI_Melody.mid"
)

print("✅ Music generated successfully!")
print("Saved as: generated_music/AI_Melody.mid")
