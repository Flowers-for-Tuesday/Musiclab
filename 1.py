from manim import *
from utils import *
from Mobjects import *
from music21 import *

class ShowLilyPondSVG(Scene):
    def construct(self):
        self.camera.background_color = WHITE  # 改成你想要的颜色

        text1 = Text("C Ionian / C major",color=BLACK ,font="Times New Roman",slant=ITALIC).shift(UP*3.3)
        text2 = Text("(  C  D  E  F  G  A  B  )",color=BLACK).scale(0.4).shift(UP*2.8)
        text3 = Text("C Dorian",color=BLACK ,font="Times New Roman",slant=ITALIC).shift(UP*3.3)
        text4 = Text("(  C  D  E♭  F  G  A  B♭  )",color=BLACK).scale(0.4).shift(UP*2.8)
        text5 = Text("C Phrygian",color=BLACK ,font="Times New Roman",slant=ITALIC).shift(UP*3.3)
        text6 = Text("(  C  D♭  E♭  F  G  A♭  B♭  )",color=BLACK).scale(0.4).shift(UP*2.8)
        text7 = Text("C Lydian",color=BLACK ,font="Times New Roman",slant=ITALIC).shift(UP*3.3)
        text8 = Text("(  C  D  E  F♯  G  A  B  )",color=BLACK).scale(0.4).shift(UP*2.8)
        text9 = Text("C Mixolydian",color=BLACK ,font="Times New Roman",slant=ITALIC).shift(UP*3.3)
        text10 = Text("(  C  D  E  F  G  A  B♭  )",color=BLACK).scale(0.4).shift(UP*2.8)
        text11 = Text("C Aeolian / A minor",color=BLACK ,font="Times New Roman",slant=ITALIC).shift(UP*3.3)
        text12 = Text("(  C  D  E♭  F  G  A♭  B♭  )",color=BLACK).scale(0.4).shift(UP*2.8)
        text13 = Text("C Locrian",color=BLACK ,font="Times New Roman",slant=ITALIC).shift(UP*3.3)
        text14 = Text("(  C  D♭  E♭  F  G♭  A♭  B♭  )",color=BLACK).scale(0.4).shift(UP*2.8)
          
        score1 = create_piano_score1()
        treble = score1.getElementById("Treble")
        notes = treble.recurse().getElementsByClass('Note')
        sl = spanner.Slur()
        sl.addSpannedElements([notes[12], notes[15]])
        treble.insert(0, sl)
        score1.parts[0].measure(1).insert(0, dynamics.Dynamic('mf'))
        music1 = MusicTex(score1).scale(1.3).shift(DOWN*2)
        audio1 = MusicAudio(score1)
        piano = MultiOctavePianoKeyboard(octaves=3,start_octave=3,show_labels=False).scale(0.8).shift(UP*1)
        #showlabel(piano,'piano')
        self.play(Write(text1),Write(text2))
        self.play(Write(music1))
        self.play(FadeIn(piano))
        #self.add_sound(audio1.wav_path, time_offset=0)
        self.play(Flash_around(piano[1]))
        events = score_events(score1,relative_octave=3,bpm=120)
        print(events)
        self.wait(2)

def create_piano_score1():
    score = piano_score("C", "2/4", parts=["Treble", "Bass"], bpm=120)
    add_notes(score,"Treble", [('C5', 1.0), ('C5', 1.0), ('G5', 1.0), ('G5', 1.0)])
    add_notes(score,"Bass",[('C3', 1.0), ('C4', 1.0), ('E4', 1.0), ('C4', 1.0)])
    add_notes(score,"Treble", [('A5', 1.0), ('A5', 1.0), ('G5', 1.0), ('G5', 1.0)])
    add_notes(score,"Bass",[('F4', 1.0), ('C4', 1.0), ('E4', 1.0), ('C4', 1.0)])
    add_notes(score,"Treble", [('F5', 1.0), ('F5', 1.0), ('E5', 1.0), ('E5', 1.0)])
    add_notes(score,"Bass",[ ('D4', 1.0), ('B3', 1.0), ('C4', 1.0), ('A3', 1.0)])
    add_notes(score,"Treble", [('D5', 1.0), ('D5', 0.75), ('E5', 0.25), ('C5', 2.0)])
    add_notes(score,"Bass",[('F3', 1.0), ('G3', 1.0), ('C3', 2.0)])
    for p in score.parts:
        for m in p.getElementsByClass('Measure'):
            m.makeBeams(inPlace=True)
    return score
