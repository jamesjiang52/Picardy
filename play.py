import os
import sys
import time
from pyknon.genmidi import Midi
from pyknon.music import Note, NoteSeq
import pygame as pg
import lut
import utils

NOTE_DURATION = 2  # beats
TEMPO = 60  # bpm


def play_chord(notes):
    """
    notes is a list of indices:
    [C1, C#1, D1, D#1, E1, F1, F#1, G1, G#1, A1, A#1, B1, C2, C#2, D2, D#2, E2, F2, F#2, G2, G#2, A2, A#2, B2]
    """
    chord = []
    for note in notes:
        chord.append(Note(value=(note % 12), octave=((note//12) + 4), dur=NOTE_DURATION))

    filepath = "chord.mid"

    midi = Midi(tempo=TEMPO)
    midi.seq_chords([NoteSeq(chord)])
    midi.write(filepath)

    pg.init()
    pg.mixer.music.load(filepath)
    pg.mixer.music.play()
    time.sleep(NOTE_DURATION*60/TEMPO)

    os.remove(filepath)


def main(argv):
    play_chord(utils.get_indices(lut.lut[utils.get_canonical_name(argv[1])]))


if __name__ == "__main__":
    main(sys.argv)
