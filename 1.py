from manim import *
from MusicSvg import MusicSvg 
from MusicTex import MusicTex
from showlabel import showlabel
from MusicAudio import MusicAudio
from PianoKeyboard import *
from music21 import *

class ShowLilyPondSVG(Scene):
    def construct(self):
        self.camera.background_color = WHITE  # 改成你想要的颜色

        score = create_e_major_piano_score()
        music1 = MusicTex(score).scale(1.4).shift(DOWN*1)
        audio1 = MusicAudio(score)
        piano1 = MultiOctavePianoKeyboard(octaves=6).scale(0.6).shift(UP*2)
        #showlabel(music1,'music1')
        self.play(Write(music1),run_time = 6)
        self.play(FadeIn(piano1))
        self.add_sound(audio1.wav_path, time_offset=0.3)
        for event in score_events(score,relative_octave=2,bpm=100):
            self.play(piano1.animate.markKeys(event[0]),run_time = 0.05)
            self.wait(event[1]-0.1)
            self.play(piano1.animate.unmarkKeys(event[0]),run_time=0.05)
        self.wait(2)

def create_e_major_piano_score():
    score = stream.Score()
    score.append(meter.TimeSignature('3/4'))
    score.append(key.KeySignature(4))
    score.append(instrument.Piano())

    # 右手高音部，生成一小段四分和十六分混合的音符
    rh_notes = [
        note.Note('E5', type='quarter'),
        note.Note('F#5', type='16th'),
        note.Note('G#5', type='16th'),
        note.Note('B5', type='quarter'),
        note.Rest(type='quarter'), 
    ]

    right_hand = stream.Part()
    right_hand.append(instrument.Piano())
    right_hand.append(clef.TrebleClef())
    right_hand.append(key.KeySignature(4))
    right_hand.append(meter.TimeSignature('3/4'))
    right_hand.append(rh_notes)  # 一次性添加列表里的所有元素

    score.insert(0, right_hand)

    return score
            


        

