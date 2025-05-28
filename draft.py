from manim import *

class SuccessionExample(Scene):
            def construct(self):
                dot1 = Dot(point=LEFT * 2 + UP * 2, radius=0.16, color=BLUE)
                dot2 = Dot(point=LEFT * 2 + DOWN * 2, radius=0.16, color=MAROON)
                dot3 = Dot(point=RIGHT * 2 + DOWN * 2, radius=0.16, color=GREEN)
                dot4 = Dot(point=RIGHT * 2 + UP * 2, radius=0.16, color=YELLOW)

                self.play(Create(VGroup(dot1,dot2,dot3,dot4)))
                self.wait(2)