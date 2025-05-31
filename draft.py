# music_visualizer.py
from manim import *
from Mobjects import *
from utils import *
import numpy as np
import librosa

class MusicVisualizer(Scene):
    def construct(self):
        sc7 = piano_score("C","4/4",["Treble"],bpm=60)
        add_notes(sc7, "Treble", [
            ("rest", 0.5),
            [("F#4", 0.25), ("A4", 0.25)],
            [("D5", 0.25), ("F#4", 0.25), ("A4", 0.25), ("D5", 0.25)],
            ("rest", 0.5),
            [("F4", 0.25), ("A4", 0.25)],
            [("D5", 0.25), ("F4", 0.25), ("A4", 0.25), ("D5", 0.25)]
        ])

        mtx7 = MusicTex(sc7,timesignature_on=False).set_color(WHITE)
        self.play(Write(mtx7))
        self.wait(2)
