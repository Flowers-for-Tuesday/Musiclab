from manim import *
from Mobjects import *
from utils import *

class S(Scene):
    def construct(self):
        c = CircleOfFifths(type="Major")
        #showlabel(c,"c")
        text1 = Text("F",font="Times New Roman",font_size=36,weight=BOLD)
        text2 = Text("Am",font="Times New Roman",font_size=36,weight=BOLD,)
        text3 = Text("C7",font="Times New Roman",font_size=36,weight=BOLD)
        text4 = Text("Bdim",font="Times New Roman",font_size=36,weight=BOLD)
        self.play(Create(c))
        self.play(c.animate.rotate_to_key("F"))
        self.wait(1)
        self.play(Write(text1),c.show_chord("major",bpm=60))
        self.play(c.animate.rotate_to_key("A"),FadeOut(text1))
        self.wait(1)
        self.play(Write(text2),c.show_chord("minor",bpm=60))
        self.play(c.animate.rotate_to_key("C"),FadeOut(text2))
        self.wait(1)
        self.play(Write(text3),c.show_chord("dominant7",bpm=60))
        self.play(c.animate.rotate_to_key("B"),FadeOut(text3))
        self.wait(1)
        self.play(Write(text4),c.show_chord("diminished",bpm=60))
        self.wait(2)
        c2 = CircleOfFifths(type="Minor")
        self.play(Transform(c,c2))
        self.wait(2)