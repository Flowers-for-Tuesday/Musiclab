from manim import *
from Mobjects import *
from utils import *

class S(Scene):
    def construct(self):
        c = CircleOfFifth()
        self.play(Create(c))
        self.wait(2)

        #self.play(FadeOut(c))

        s = ScaleDegreeRing().scale(0.75).setPosition([0,0,0])
        self.play(Create(s))
        self.wait(2)