from manim import *
from Mobjects import *
from utils import *

class S(Scene):
    def construct(self):
        c = CircleOfFifths(type="Major",show_scores=False)
        self.play(Create(c))
        self.play(c.animate.rotate_to_key("B"))
        self.wait(2)
        self.play(c.show_chord("m",bpm=60))
        self.wait(2)