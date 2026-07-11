import glob
import pickle
import numpy as np

from music21 import converter, instrument, note, chord

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.layers import Activation
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import ModelCheckpoint

# ===========================
# READ MIDI FILES
# ===========================

notes = []

for file in glob.glob("dataset/*.mid"):

    print("Reading:", file)

    midi = converter.parse(file)

    parts = instrument.partitionByInstrument(midi)

    if parts:
        notes_to_parse = parts.parts[0].recurse()
    else:
        notes_to_parse = midi.flat.notes

    for element in notes_to_parse:

        if isinstance(element, note.Note):
            notes.append(str(element.pitch))

        elif isinstance(element, chord.Chord):
            notes.append('.'.join(str(n) for n in element.normalOrder))

# ===========================
# SAVE NOTES
# ===========================

with open("models/notes.pkl", "wb") as f:
    pickle.dump(notes, f)

print("Total Notes:", len(notes))

# ===========================
# CREATE VOCABULARY
# ===========================

pitchnames = sorted(set(notes))

note_to_int = dict((n, i) for i, n in enumerate(pitchnames))

sequence_length = 100

network_input = []
network_output = []

for i in range(len(notes) - sequence_length):

    sequence_in = notes[i:i + sequence_length]

    sequence_out = notes[i + sequence_length]

    network_input.append([note_to_int[n] for n in sequence_in])

    network_output.append(note_to_int[sequence_out])

n_patterns = len(network_input)

network_input = np.reshape(
    network_input,
    (n_patterns, sequence_length, 1)
)

network_input = network_input / float(len(pitchnames))

network_output = to_categorical(network_output)

# ===========================
# BUILD MODEL
# ===========================

model = Sequential()

model.add(
    LSTM(
        512,
        input_shape=(network_input.shape[1], network_input.shape[2]),
        return_sequences=True
    )
)

model.add(Dropout(0.3))

model.add(LSTM(512))

model.add(Dense(256))

model.add(Dropout(0.3))

model.add(Dense(len(pitchnames)))

model.add(Activation("softmax"))

model.compile(
    loss="categorical_crossentropy",
    optimizer="adam"
)

# ===========================
# SAVE BEST MODEL
# ===========================

checkpoint = ModelCheckpoint(
    "models/music_model.h5",
    monitor="loss",
    save_best_only=True,
    mode="min"
)

print("Training Started...")

model.fit(
    network_input,
    network_output,
    epochs=50,
    batch_size=64,
    callbacks=[checkpoint]
)

print("Training Complete!")
