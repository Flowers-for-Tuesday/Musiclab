from manim import *
from Mobjects import *
from utils import *

class S(Scene):
    def construct(self):
        c = CircleOfFifths(type="Major",show_scores=True)
        self.play(Create(c))
        self.play(c.animate.rotate_to_key("B"))
        self.wait(2)