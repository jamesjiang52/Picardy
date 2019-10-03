def get_indices(names):
    notes = ["C1", "C#1", "D1", "D#1", "E1", "F1", "F#1", "G1", "G#1", "A1", "A#1", "B1", "C2", "C#2", "D2", "D#2", "E2", "F2", "F#2", "G2", "G#2", "A2", "A#2", "B2"]
    return [*map(lambda x: notes.index(x), names)]


def get_canonical_name(name):
    i = 0
    while i < len(name):
        if name[i] not in ["C", "D", "E", "F", "G", "A", "B", "#", "b", "x"]:
            break
        i += 1

    note_name = name[:i]
    note_name = {
        "B#": "C", "C": "C", "Dbb": "C",
        "Bx": "C#", "C#": "C#", "Db": "C#",
        "Cx": "D", "D": "D", "Ebb": "D",
        "D#": "D#", "Eb": "D#", "Fbb": "D#",
        "Dx": "E", "E": "E", "Fb": "E",
        "E#": "F", "F": "F", "Gbb": "F",
        "Ex": "F#", "F#": "F#", "Gb": "F#",
        "Fx": "G", "G": "G", "Abb": "G",
        "G#": "G#", "Ab": "G#",
        "Gx": "A", "A": "A", "Bbb": "A",
        "A#": "A#", "Bb": "A#", "Cbb": "A#",
        "Ax": "B", "B": "B", "Cb": "B"
    }[note_name]

    if i < len(name):
        note_name += name[i:]

    return note_name
