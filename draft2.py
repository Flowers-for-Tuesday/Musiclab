from manim import *
from Mobjects import *
from utils import *

class S(Scene):
    def construct(self):
        c = CircleOfFifths(show_scores=True)
        self.play(Create(c))
        self.play(c.animate.scale(1.5))
        self.wait(2)