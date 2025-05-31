from collections.abc import Sequence, Iterable
from typing import TypeVar

from manim import *
from svgelements import Path as SVGPath

from music21 import *

__all__ = [
    "PianoKeyboard",
    "MultiOctavePianoKeyboard",
    "MARK_RED",
    "MARK_GREEN",
    "MARK_BLUE",
    "MARK_GRAY",
]

M = TypeVar("M", bound=Mobject)
_MarkColorType = tuple[ManimColor, ManimColor]

_keys = (
    (False, 0),
    (True, 0),
    (False, 1),
    (True, 1),
    (False, 2),
    (False, 3),
    (True, 2),
    (False, 4),
    (True, 3),
    (False, 5),
    (True, 4),
    (False, 6),
)

MARK_RED = (RED_B, RED_D)
MARK_GREEN = (GREEN_B, GREEN_D)
MARK_BLUE = (BLUE_B, BLUE_D)
MARK_GRAY = (GRAY_B, GRAY_D)


class PianoKeyboard(VGroup):
    def __init__(
        self,
        /,
        whiteWidth=0.5,
        whiteHeight=2.5,
        blackWidth=0.25,
        blackHeight=1.5,
        cornerWidth=0.08,
        blackDisplace=(-0.1, 0.1, -0.1, 0, 0.1),
        markColor: _MarkColorType = MARK_BLUE,
        **kwargs,
    ):

        super().__init__(**kwargs)

        w1, h1 = whiteWidth, whiteHeight
        w2, h2 = blackWidth, blackHeight
        cw = cornerWidth

        self._markColor = markColor
        self._markedKeys = set()

        mob_whiteKeyTemplate = VMobjectFromSVGPath(
            SVGPath(
                "m 0,0 "
                f"h {w1} "
                f"v {-h1 + cw} "
                f"q 0,{-cw} {-cw},{-cw} "
                f"h {-w1 + 2 * cw}"
                f"q {-cw},0 {-cw},{cw} "
                "z"
            ),
            fill_color=WHITE,
            stroke_color=GRAY,
            stroke_width=2,
            fill_opacity=1,
        )
        mob_blackKeyTemplate = VMobjectFromSVGPath(
            SVGPath(
                f"m 0,0 "
                f"h {w2} "
                f"v {-h2 + cw} "
                f"q 0,{-cw} {-cw},{-cw} "
                f"h {-w2 + 2 * cw}"
                f"q {-cw},0 {-cw},{cw} "
                "z"
            ),
            fill_color=BLACK,
            stroke_color=GRAY_D,
            stroke_width=2,
            fill_opacity=1,
        )

        self._mob_whiteKeys = VGroup()
        self._mob_blackKeys = VGroup()

        for i in range(7):
            mob_whiteKey = mob_whiteKeyTemplate.copy().shift((i * w1, 0, 0))
            mob_whiteKey.isBlack = False
            self._mob_whiteKeys.add(mob_whiteKey)

        for i, dx in zip((0, 1, 3, 4, 5), blackDisplace):
            blackX = (i + 1) * w1 + w2 * (dx - 0.5)
            mob_blackKey = mob_blackKeyTemplate.copy().shift((blackX, 0, 0))
            mob_blackKey.isBlack = True
            self._mob_blackKeys.add(mob_blackKey)

        self.add(self._mob_whiteKeys, self._mob_blackKeys)

    def getKey(self, idx: int) -> SVGPath:
        isBlack, groupIndex = _keys[idx]
        if isBlack:
            return self._mob_blackKeys[groupIndex]
        else:
            return self._mob_whiteKeys[groupIndex]

    def markKey(
        self,
        key: int,
        /,
        markColor: _MarkColorType | None = None,
    ):
        if markColor is None:
            markColor = self._markColor
        isBlack = _keys[key][0]
        color = markColor[isBlack]
        mob_key = self.getKey(key)
        mob_key.set_fill(color=color)
        self._markedKeys.add(key)
        return self

    def markKeys(self, keys: Iterable[int], /, markColor: _MarkColorType | None = None):
        for key in keys:
            self.markKey(key, markColor=markColor)
        return self

    def unmarkKey(self, key: int):
        isBlack = _keys[key][0]
        self._markedKeys.discard(key)
        mob_key = self.getKey(key)
        mob_key.set_fill(color=BLACK if isBlack else WHITE)
        return self

    def unmarkKeys(self, keys: Iterable[int]):
        for key in keys:
            self.unmarkKey(key)
        return self

    def resetMarks(self):
        self.unmarkKeys(frozenset(self._markedKeys))
        return self

    def alignToKey(self, key: int, mob: M, buff: float = 0.2) -> M:
        mob_key = self.getKey(key)
        mob.move_to(mob_key).align_to(mob_key, DOWN).shift(UP * buff)
        return mob


class MultiOctavePianoKeyboard(VGroup):
    def __init__(
            self, 
            octaves=2, #跨多少八度
            start_octave: int = 4,#起始C音符音高
            show_labels: bool = False,#是否显示标签
            whiteWidth=0.5,
            **kwargs
        ):

        super().__init__()
        self.octaves = octaves
        self.start_octave = start_octave
        wo = whiteWidth * 7
        mob_keyboardTemplate = PianoKeyboard(whiteWidth=whiteWidth, **kwargs)

        for i in range(octaves):
            mob_keyboard = mob_keyboardTemplate.copy().shift((i * wo, 0, 0))
            self.add(mob_keyboard)

        self.move_to(ORIGIN) #初始化到中央位置

        if show_labels: self._add_labels()

    def markKey(self, key: int, /, markColor: _MarkColorType | None = None):
        octave, idx = divmod(key, 12)
        self[octave].markKey(idx, markColor=markColor)
        return self

    def getKey(self, key: int) -> Mobject:
        octave, idx = divmod(key, 12)
        return self[octave].getKey(idx)

    def markKeys(self, keys: Iterable[int], /, markColor: _MarkColorType | None = None):
        for key in keys:
            self.markKey(key, markColor=markColor)
        return self

    def unmarkKey(self, key: int):
        octave, idx = divmod(key, 12)
        self[octave].unmarkKey(idx)
        return self

    def unmarkKeys(self, keys: Iterable[int]):
        for key in keys:
            self.unmarkKey(key)
        return self

    def resetMarks(self):
        for mob_keyboard in self:
            mob_keyboard.resetMarks()
        return self

    def alignToKey(self, key: int, mob: M, buff: float = 0.2) -> M:
        '''
        将mob移动到指定key位置
        '''
        mob_key = self.getKey(key)
        mob.move_to(mob_key).align_to(mob_key, DOWN).shift(UP * buff)
        return mob
    
    def markNotes(self, notes: str | Iterable[str], /, markColor: _MarkColorType | None = None):
        """
        高亮指定音符（如 "C4" 或 ["F4", "G#4"]）
        """
        if isinstance(notes, str):
            notes = [notes]
        keys = []
        for n in notes:
            midi = note.Note(n).pitch.midi
            key = midi - (self.start_octave+1) * 12
            if not (0 <= key < self.octaves * 12):
                raise ValueError(f"Note '{n}' is out of range for current keyboard.")
            keys.append(key)
        return self.markKeys(keys, markColor=markColor)

    def unmarkNotes(self, notes: str | Iterable[str]):
        """
        取消高亮指定音符
        """
        if isinstance(notes, str):
            notes = [notes]
        keys = []
        for n in notes:
            midi = note.Note(n).pitch.midi
            key = midi - (self.start_octave+1) * 12
            if not (0 <= key < self.octaves * 12):
                raise ValueError(f"Note '{n}' is out of range for current keyboard.")
            keys.append(key)
        return self.unmarkKeys(keys)
    
    def _add_labels(self):
        note_names = ["C", "C♯", "D", "D♯", "E", "F", "F♯", "G", "G♯", "A", "A♯", "B"]
        for i in range(self.octaves*12):
            midi = self.start_octave*12 + i
            pitch_class = midi % 12
            octave = midi // 12
            if (pitch_class in [0,2,4,5,7,9,11]):
                label = Text(f"{note_names[pitch_class]}{octave}",color=BLACK).scale(0.4)
            else:
                label = Text(f"{note_names[pitch_class]}\n  {octave}",color=WHITE).scale(0.27)
            self.alignToKey(i, label)
            self.add(label)

