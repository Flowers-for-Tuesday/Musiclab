from manim import *
from Mobjects import *
from music21 import *
from utils import *

class VerticalDifference(Scene):
    def construct(self):
        sc = piano_score("C","4/4",["Treble"])
        
        add_notes(sc,"Treble",[("C5",1)])
        musictext = MusicTex(sc).set_color(WHITE)
        #showlabel(musictext)
        self.play(Create(musictext))
        self.wait(2)
        self.play(VGroup(musictext[7],musictext[9]).animate.shift(UP*SCORE_WIDTH))
        self.wait(1)
        self.play(Circumscribe(VGroup(musictext[5],musictext[6])))
