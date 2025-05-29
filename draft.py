from manim import *
from Mobjects import *
from music21 import *
from utils import *

class VerticalDifference(Scene):
    def construct(self):
        sc = piano_score("C","4/4",["Treble"])
        
        add_notes(sc,"Treble",[("C5",1),("E5",1)])
        musictext = MusicTex(sc).set_color(WHITE)
        #showlabel(musictext)
        self.play(Create(musictext))
        self.wait(2)
        self.play(VGroup(musictext[7],musictext[11]).animate.shift(UP*SCORE_WIDTH*0.5))
        self.wait(1)
        self.play(Circumscribe(VGroup(musictext[5],musictext[6])))
        self.wait(1)
        self.play(Write(BracketText("上行",musictext[11],musictext[6],line_height=0.3)))
        self.wait(1)