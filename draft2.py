from manim import *
from text_config import latexConfig

class TestScene(Scene):
    def construct(self):
        tex = Tex(
            r"质能方程 $E=mc^2$", 
            tex_template=latexConfig["tex_template"]
        )
        self.play(Write(tex))
        self.wait()
