from music21 import *

KEY_DICT = {
    "C": key.Key("C"),
    "G": key.Key("G"),
    "D": key.Key("D"),
    "A": key.Key("A"),
    "E": key.Key("E"),
    "B": key.Key("B"),
    "F#": key.Key("F#"),
    "C#": key.Key("C#"),
    "F": key.Key("F"),
    "Bb": key.Key("Bb"),
    "Eb": key.Key("Eb"),
    "Ab": key.Key("Ab"),
    "Db": key.Key("Db"),
    "Gb": key.Key("Gb"),
    "Cb": key.Key("Cb"),

    "Am": key.Key("A", "minor"),
    "Em": key.Key("E", "minor"),
    "Bm": key.Key("B", "minor"),
    "F#m": key.Key("F#", "minor"),
    "C#m": key.Key("C#", "minor"),
    "G#m": key.Key("G#", "minor"),
    "D#m": key.Key("D#", "minor"),
    "A#m": key.Key("A#", "minor"),
    "Dm": key.Key("D", "minor"),
    "Gm": key.Key("G", "minor"),
    "Cm": key.Key("C", "minor"),
    "Fm": key.Key("F", "minor"),
    "Bbm": key.Key("Bb", "minor"),
    "Ebm": key.Key("Eb", "minor"),
    "Abm": key.Key("Ab", "minor"),
}

def piano_score(
    key_signature: str,
    time_signature: str,
    parts: list[str],
    bpm: int = 100
) -> stream.Score:
    """
    创建一个空的 Score，包含指定声部和基础设置。
    parts 是 ["Treble", "Bass"] 的子集。
    """
    valid_parts = {"Treble", "Bass"}
    if not set(parts).issubset(valid_parts):
        raise ValueError("parts must be subset of ['Treble', 'Bass']")
    if not parts:
        raise ValueError("parts must contain at least one of ['Treble', 'Bass']")
    
    k = KEY_DICT.get(key_signature)
    if k is None:
        raise ValueError(f"Unknown key signature: {key_signature}")

    sc = stream.Score()
    sc._part_dict = {}  # 自定义属性，方便后续访问

    for part_name in parts:
        p = stream.Part()
        p.id = part_name
        p.append(instrument.Piano())
        if part_name == "Treble":
            p.append(clef.TrebleClef())
        else:
            p.append(clef.BassClef())
        p.append(k)
        p.append(meter.TimeSignature(time_signature))
        p.append(tempo.MetronomeMark(number=bpm))
        sc._part_dict[part_name] = p
        sc.append(p)

    return sc

def add_notes(
    score: stream.Score,
    part: str,
    notes: list[tuple[str | list[str], float]]
):
    """
    向 score 指定声部添加一个小节的音符序列。
    notes 格式为 [(音名或和弦列表, 时值), ...]
    """
    if not hasattr(score, "_part_dict"):
        raise ValueError("Score has no '_part_dict' attribute; use piano_score() to create score.")
    if part not in score._part_dict:
        raise ValueError(f"Part '{part}' not found in score.")

    m = stream.Measure()
    for pitch, dur in notes:
        if pitch == "rest":
            n = note.Rest()
        elif isinstance(pitch, list):
            n = chord.Chord(pitch)
        else:
            n = note.Note(pitch)
        n.quarterLength = dur
        m.append(n)
    score._part_dict[part].append(m)
