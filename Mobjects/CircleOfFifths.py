from manim import *
from music21 import *
from .MusicTex import *

__all__ = [
    "CircleOfFifths",
]

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

class CircleOfFifths(VGroup):
    def __init__(
            self, radius=1.5, 
            dot_radius=0.06,
            show_scores = False,# 是否显示乐谱
            **kwargs
            ):
        super().__init__(**kwargs)

        # 标签内容（从C开始，顺时针，每隔纯五度）
        labels = [
            "C", "G", "D", "A", "E", "B", "F♯", "D♭",
            "A♭", "E♭", "B♭", "F"
        ]
        labelscopy = [
            "C", "G", "D", "A", "E", "B", "F#", "Db",
            "Ab", "Eb", "Bb", "F"
        ]

        # 背景圆
        circle = Circle(radius=radius, color=GREY_B, stroke_width=3)
        self.add(circle)

        # 添加12个点与标签
        for i, label in enumerate(labels):
            angle = PI / 2 - i * TAU / 12  # C 在顶部，逆时针增加角度
            direction = np.array([np.cos(angle), np.sin(angle), 0])
            point_pos = radius * direction

            # Dot
            dot = Dot(point_pos, radius=dot_radius, color=WHITE)
            self.add(dot)

            # Label
            text = Text(label, font_size=32,weight=BOLD).scale(0.6)
            text.move_to(point_pos + 0.4 * direction)  # 标签稍微偏离圆心方向
            self.add(text)

            if show_scores:
                score = blank_score(labelscopy[i],"4/4",["Treble","Bass"])
                musictex = MusicTex(score,line_width=1,barline_on=False,timesignature_on=False)
                musictex.scale(0.4)
                musictex.move_to(point_pos + 1.3 * direction)
                musictex.set_color(WHITE)
                self.add(musictex)

def blank_score(
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

        # 添加一个全休符（空白音符）
        m = stream.Measure(number=0)
        r = note.Rest(quarterLength=2)
        m.append(r)
        p.append(m)

        sc._part_dict[part_name] = p
        sc.append(p)
    
    return sc