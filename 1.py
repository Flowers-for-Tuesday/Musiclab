from manim import *
from utils import *
from Mobjects import *
from music21 import *

class ShowLilyPondSVG(Scene):
    def construct(self):
        self.camera.background_color = WHITE  # 改成你想要的颜色

        score1 = create_piano_score1()
        music1 = MusicTex(score1).scale(1.4).shift(DOWN*1)
        audio1 = MusicAudio(score1)
        piano1 = MultiOctavePianoKeyboard(octaves=5).scale(0.6).shift(UP*2)
        #showlabel(music1,'music1')
        self.play(Write(music1),run_time = 4)
        self.play(FadeIn(piano1))
        self.add_sound(audio1.wav_path, time_offset=0.3)
        events = score_events(score1,relative_octave=2,bpm=64)
        for event in events:
            self.play(piano1.animate.markKeys(event[0]),run_time = 0.2/3)
            self.wait(event[1]-0.4/3)
            self.play(piano1.animate.unmarkKeys(event[0]),run_time=0.2/3)
        self.wait(2)

def create_piano_score1():
    score = piano_score("C", "4/4", parts=["Treble", "Bass"], bpm=64)

    # 添加到 Treble
    add_notes(score,"Treble", [
        ("E5", 0.5),
        (["G#5", "B5", "E6"], 1.0),
        ("F#5", 0.5),
        (["A5", "C#6", "E6"], 1.0)
    ])

    # 添加到 Bass
    add_notes(score,"Bass", [
        ("E3", 1.5),
        ("A2", 1.5)
    ])
    # 添加到 Treble
    add_notes(score,"Treble", [
        ("E5", 0.5),
        (["G#5", "B5", "E6"], 1.0),
        ("F#5", 0.5),
        (["A5", "C#6", "E6"], 1.0)
    ])

    # 添加到 Bass
    add_notes(score,"Bass", [
        ("E3", 1.5),
        ("A2", 1.5)
    ])
    return score
            


        

