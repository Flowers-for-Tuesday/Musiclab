from manim import *
from utils import *
from Mobjects import *
from music21 import *

class ShowLilyPondSVG(Scene):
    def construct(self):
        self.camera.background_color = WHITE  # 改成你想要的颜色

        score1 = create_piano_score1()
        music1 = MusicTex(score1).scale(1).shift(DOWN*1)
        audio1 = MusicAudio(score1)
        piano1 = MultiOctavePianoKeyboard(octaves=5).scale(0.6).shift(UP*2)
        #showlabel(music1,'music1')
        self.play(Write(music1),run_time = 4)
        self.play(FadeIn(piano1))
        self.add_sound(audio1.wav_path, time_offset=0.3-2*64/120-1)
        events = score_events(score1,relative_octave=2,bpm=64)
        print(events)
        for i, (pitches, duration,offset) in enumerate(events):
            self.play(piano1.animate.markKeys(pitches), run_time=0.2/3)
            wait_time = max(duration - 0.2/3, 0)
            self.wait(wait_time)
            
            if i + 1 < len(events):
                next_pitches = set(events[i + 1][0])
                to_unmark = [p for p in pitches if p not in next_pitches]
            else:
                to_unmark = pitches  # 最后一个事件，全部抬起

            if to_unmark:
                self.play(piano1.animate.unmarkKeys(to_unmark), run_time=0.2/3)
        self.wait(2)

def create_piano_score1():
    score = piano_score("C", "4/4", parts=["Treble", "Bass"], bpm=64)
    add_notes(score,"Treble", [('rest',2),('E4', 0.5), ('G4', 0.5), ('C5', 0.5), ('E5', 0.5)])
    add_notes(score,"Bass",[('rest', 4)])
    add_notes(score,"Treble", [('E5', 1.5), ('F5', 0.5), ('D5', 2.0)])
    add_notes(score,"Bass",[('F2', 0.5), ('C3', 0.5), ('A3', 1.0), ('G2', 0.5), ('D3', 0.5), ('B3', 1.0)])
    add_notes(score,"Treble", [('D5', 1.0), ('G5', 0.5), ('B4', 0.5), ('C5', 2.0)])
    add_notes(score,"Bass",[('E3', 0.5), ('B3', 0.5), ('D4', 1.0), ('A2', 0.5), ('E3', 0.5), ('A2', 0.5), ('G2', 0.5)])
    add_notes(score,"Treble", [('E5', 0.5), ('F5', 0.5), ('G5', 0.5), ('C5', 0.5), ('C5', 1.0), ('D5', 1.0)])
    add_notes(score,"Bass",[('F2', 0.5), ('C3', 0.5), ('A3', 0.5), ('F3', 0.5), ('G2', 0.5), ('D3', 0.5), ('B3', 0.5), ('F3', 0.5)])
    for p in score.parts:
        for m in p.getElementsByClass('Measure'):
            m.makeBeams(inPlace=True)
    return score

def create_piano_score2():
    score = piano_score("C", "4/4", parts=["Treble", "Bass"], bpm=64)
    add_notes(score,"Treble", [('E4', 0.5), ('G4', 0.5), ('C5', 0.5), ('E5', 0.5)])
    add_notes(score,"Bass",[('F2', 0.5), ('C3', 0.5), ('A3', 1.0), ('G2', 0.5), ('D3', 0.5), ('B3', 1.0)])
    return score

def create_piano_score3():
    score = piano_score("C", "4/4", parts=["Treble", "Bass"], bpm=64)
    add_notes(score,"Treble", [('E4', 0.5), ('G4', 0.5), ('C5', 0.5), ('E5', 0.5)])
    add_notes(score,"Bass",[('F2', 0.5), ('C3', 0.5), ('A3', 1.0), ('G2', 0.5), ('D3', 0.5), ('B3', 1.0)])
    return score   


        

