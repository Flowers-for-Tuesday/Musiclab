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
        piano = MultiOctavePianoKeyboard(octaves=3).scale(0.8).shift(UP*1)
        #showlabel(music1,'music1')
        self.play(Write(text1),Write(text2))
        self.play(Write(music1))
        self.play(FadeIn(piano))
        self.add_sound(audio1.wav_path, time_offset=0)
        events = score_events(score1,relative_octave=3,bpm=120)
        print(events)
        for event in events:
            self.play(piano.animate.markKeys(event[0]), run_time=0.05)
            wait_time = max(event[1] - 0.1, 0.01)
            self.wait(wait_time)
            self.play(piano.animate.unmarkKeys(event[0]), run_time=0.05)
        self.wait(2)

        score2 = create_piano_score2()
        music2 = MusicTex(score2).scale(1.3).shift(DOWN*2)
        treble = score2.getElementById("Treble")
        notes = treble.recurse().getElementsByClass('Note')
        sl = spanner.Slur()
        sl.addSpannedElements([notes[12], notes[15]])
        treble.insert(0, sl)
        audio2 = MusicAudio(score2)
        self.play(Transform(text1,text3),Transform(text2,text4),Transform(music1,music2))
        self.add_sound(audio2.wav_path, time_offset=0)
        events = score_events(score2,relative_octave=3,bpm=120)
        for event in events:
            self.play(piano.animate.markKeys(event[0]), run_time=0.05)
            wait_time = max(event[1] - 0.1, 0.01)
            self.wait(wait_time)
            self.play(piano.animate.unmarkKeys(event[0]), run_time=0.05)
        self.wait(2)

        score3 = create_piano_score3()
        music3 = MusicTex(score3).scale(1.3).shift(DOWN*2)
        treble = score3.getElementById("Treble")
        notes = treble.recurse().getElementsByClass('Note')
        sl = spanner.Slur()
        sl.addSpannedElements([notes[12], notes[15]])
        treble.insert(0, sl)
        audio3 = MusicAudio(score3)
        self.play(Transform(text1,text5),Transform(text2,text6),Transform(music1,music3))
        self.add_sound(audio3.wav_path, time_offset=0)
        events = score_events(score3,relative_octave=3,bpm=120)
        for event in events:
            self.play(piano.animate.markKeys(event[0]), run_time=0.05)
            wait_time = max(event[1] - 0.1, 0.01)
            self.wait(wait_time)
            self.play(piano.animate.unmarkKeys(event[0]), run_time=0.05)
        self.wait(2)

        score4 = create_piano_score4()
        music4 = MusicTex(score4).scale(1.3).shift(DOWN*2)
        treble = score4.getElementById("Treble")
        notes = treble.recurse().getElementsByClass('Note')
        sl = spanner.Slur()
        sl.addSpannedElements([notes[12], notes[15]])
        treble.insert(0, sl)
        audio4 = MusicAudio(score4)
        self.play(Transform(text1,text7),Transform(text2,text8),Transform(music1,music4))
        self.add_sound(audio4.wav_path, time_offset=0)
        events = score_events(score4,relative_octave=3,bpm=120)
        for event in events:
            self.play(piano.animate.markKeys(event[0]), run_time=0.05)
            wait_time = max(event[1] - 0.1, 0.01)
            self.wait(wait_time)
            self.play(piano.animate.unmarkKeys(event[0]), run_time=0.05)
        self.wait(2)

        score5 = create_piano_score5()
        music5 = MusicTex(score5).scale(1.3).shift(DOWN*2)
        treble = score5.getElementById("Treble")
        notes = treble.recurse().getElementsByClass('Note')
        sl = spanner.Slur()
        sl.addSpannedElements([notes[12], notes[15]])
        treble.insert(0, sl)
        audio5 = MusicAudio(score5)
        self.play(Transform(text1,text9),Transform(text2,text10),Transform(music1,music5))
        self.add_sound(audio5.wav_path, time_offset=0)
        events = score_events(score5,relative_octave=3,bpm=120)
        for event in events:
            self.play(piano.animate.markKeys(event[0]), run_time=0.05)
            wait_time = max(event[1] - 0.1, 0.01)
            self.wait(wait_time)
            self.play(piano.animate.unmarkKeys(event[0]), run_time=0.05)
        self.wait(2)

        score6 = create_piano_score6()
        music6 = MusicTex(score6).scale(1.3).shift(DOWN*2)
        treble = score6.getElementById("Treble")
        notes = treble.recurse().getElementsByClass('Note')
        sl = spanner.Slur()
        sl.addSpannedElements([notes[12], notes[15]])
        treble.insert(0, sl)
        audio6 = MusicAudio(score6)
        self.play(Transform(text1,text11),Transform(text2,text12),Transform(music1,music6))
        self.add_sound(audio6.wav_path, time_offset=0)
        events = score_events(score6,relative_octave=3,bpm=120)
        for event in events:
            self.play(piano.animate.markKeys(event[0]), run_time=0.05)
            wait_time = max(event[1] - 0.1, 0.01)
            self.wait(wait_time)
            self.play(piano.animate.unmarkKeys(event[0]), run_time=0.05)
        self.wait(2)

        score7 = create_piano_score7()
        music7 = MusicTex(score7).scale(1.3).shift(DOWN*2)
        treble = score7.getElementById("Treble")
        notes = treble.recurse().getElementsByClass('Note')
        sl = spanner.Slur()
        sl.addSpannedElements([notes[12], notes[15]])
        treble.insert(0, sl)
        audio7 = MusicAudio(score7)
        self.play(Transform(text1,text13),Transform(text2,text14),Transform(music1,music7))
        self.add_sound(audio7.wav_path, time_offset=0)
        events = score_events(score7,relative_octave=3,bpm=120)
        for event in events:
            self.play(piano.animate.markKeys(event[0]), run_time=0.05)
            wait_time = max(event[1] - 0.1, 0.01)
            self.wait(wait_time)
            self.play(piano.animate.unmarkKeys(event[0]), run_time=0.05)
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

def create_piano_score2():
    score = piano_score("Bb", "2/4", parts=["Treble", "Bass"], bpm=120)
    add_notes(score,"Treble", [('C5', 1.0), ('C5', 1.0), ('G5', 1.0), ('G5', 1.0)])
    add_notes(score,"Bass",[('C3', 1.0), ('C4', 1.0), ('E-4', 1.0), ('C4', 1.0)])
    add_notes(score,"Treble", [('A5', 1.0), ('A5', 1.0), ('G5', 1.0), ('G5', 1.0)])
    add_notes(score,"Bass",[('F4', 1.0), ('C4', 1.0), ('E-4', 1.0), ('C4', 1.0)])
    add_notes(score,"Treble", [('F5', 1.0), ('F5', 1.0), ('E-5', 1.0), ('E-5', 1.0)])
    add_notes(score,"Bass",[ ('D4', 1.0), ('B-3', 1.0), ('C4', 1.0), ('A3', 1.0)])
    add_notes(score,"Treble", [('D5', 1.0), ('D5', 0.75), ('E-5', 0.25), ('C5', 2.0)])
    add_notes(score,"Bass",[('F3', 1.0), ('G3', 1.0), ('C3', 2.0)])
    for p in score.parts:
        for m in p.getElementsByClass('Measure'):
            m.makeBeams(inPlace=True)
    return score

def create_piano_score3():
    score = piano_score("Ab", "2/4", parts=["Treble", "Bass"], bpm=120)
    add_notes(score,"Treble", [('C5', 1.0), ('C5', 1.0), ('G5', 1.0), ('G5', 1.0)])
    add_notes(score,"Bass",[('C3', 1.0), ('C4', 1.0), ('E-4', 1.0), ('C4', 1.0)])
    add_notes(score,"Treble", [('A-5', 1.0), ('A-5', 1.0), ('G5', 1.0), ('G5', 1.0)])
    add_notes(score,"Bass",[('F4', 1.0), ('C4', 1.0), ('E-4', 1.0), ('C4', 1.0)])
    add_notes(score,"Treble", [('F5', 1.0), ('F5', 1.0), ('E-5', 1.0), ('E-5', 1.0)])
    add_notes(score,"Bass",[ ('D-4', 1.0), ('B-3', 1.0), ('C4', 1.0), ('A-3', 1.0)])
    add_notes(score,"Treble", [('D-5', 1.0), ('D-5', 0.75), ('E-5', 0.25), ('C5', 2.0)])
    add_notes(score,"Bass",[('F3', 1.0), ('G3', 1.0), ('C3', 2.0)])
    for p in score.parts:
        for m in p.getElementsByClass('Measure'):
            m.makeBeams(inPlace=True)
    return score
        
def create_piano_score4():
    score = piano_score("G", "2/4", parts=["Treble", "Bass"], bpm=120)
    add_notes(score,"Treble", [('C5', 1.0), ('C5', 1.0), ('G5', 1.0), ('G5', 1.0)])
    add_notes(score,"Bass",[('C3', 1.0), ('C4', 1.0), ('E4', 1.0), ('C4', 1.0)])
    add_notes(score,"Treble", [('A5', 1.0), ('A5', 1.0), ('G5', 1.0), ('G5', 1.0)])
    add_notes(score,"Bass",[('F#4', 1.0), ('C4', 1.0), ('E4', 1.0), ('C4', 1.0)])
    add_notes(score,"Treble", [('F#5', 1.0), ('F#5', 1.0), ('E5', 1.0), ('E5', 1.0)])
    add_notes(score,"Bass",[ ('D4', 1.0), ('B3', 1.0), ('C4', 1.0), ('A3', 1.0)])
    add_notes(score,"Treble", [('D5', 1.0), ('D5', 0.75), ('E5', 0.25), ('C5', 2.0)])
    add_notes(score,"Bass",[('F#3', 1.0), ('G3', 1.0), ('C3', 2.0)])
    for p in score.parts:
        for m in p.getElementsByClass('Measure'):
            m.makeBeams(inPlace=True)
    return score

def create_piano_score5():
    score = piano_score("F", "2/4", parts=["Treble", "Bass"], bpm=120)
    add_notes(score,"Treble", [('C5', 1.0), ('C5', 1.0), ('G5', 1.0), ('G5', 1.0)])
    add_notes(score,"Bass",[('C3', 1.0), ('C4', 1.0), ('E4', 1.0), ('C4', 1.0)])
    add_notes(score,"Treble", [('A5', 1.0), ('A5', 1.0), ('G5', 1.0), ('G5', 1.0)])
    add_notes(score,"Bass",[('F4', 1.0), ('C4', 1.0), ('E4', 1.0), ('C4', 1.0)])
    add_notes(score,"Treble", [('F5', 1.0), ('F5', 1.0), ('E5', 1.0), ('E5', 1.0)])
    add_notes(score,"Bass",[ ('D4', 1.0), ('B-3', 1.0), ('C4', 1.0), ('A3', 1.0)])
    add_notes(score,"Treble", [('D5', 1.0), ('D5', 0.75), ('E5', 0.25), ('C5', 2.0)])
    add_notes(score,"Bass",[('F3', 1.0), ('G3', 1.0), ('C3', 2.0)])
    for p in score.parts:
        for m in p.getElementsByClass('Measure'):
            m.makeBeams(inPlace=True)
    return score

def create_piano_score6():
    score = piano_score("Eb", "2/4", parts=["Treble", "Bass"], bpm=120)
    add_notes(score,"Treble", [('C5', 1.0), ('C5', 1.0), ('G5', 1.0), ('G5', 1.0)])
    add_notes(score,"Bass",[('C3', 1.0), ('C4', 1.0), ('E-4', 1.0), ('C4', 1.0)])
    add_notes(score,"Treble", [('A-5', 1.0), ('A-5', 1.0), ('G5', 1.0), ('G5', 1.0)])
    add_notes(score,"Bass",[('F4', 1.0), ('C4', 1.0), ('E-4', 1.0), ('C4', 1.0)])
    add_notes(score,"Treble", [('F5', 1.0), ('F5', 1.0), ('E-5', 1.0), ('E-5', 1.0)])
    add_notes(score,"Bass",[ ('D4', 1.0), ('B-3', 1.0), ('C4', 1.0), ('A-3', 1.0)])
    add_notes(score,"Treble", [('D5', 1.0), ('D5', 0.75), ('E-5', 0.25), ('C5', 2.0)])
    add_notes(score,"Bass",[('F3', 1.0), ('G3', 1.0), ('C3', 2.0)])
    for p in score.parts:
        for m in p.getElementsByClass('Measure'):
            m.makeBeams(inPlace=True)
    return score

def create_piano_score7():
    score = piano_score("Db", "2/4", parts=["Treble", "Bass"], bpm=120)
    add_notes(score,"Treble", [('C5', 1.0), ('C5', 1.0), ('G-5', 1.0), ('G-5', 1.0)])
    add_notes(score,"Bass",[('C3', 1.0), ('C4', 1.0), ('E-4', 1.0), ('C4', 1.0)])
    add_notes(score,"Treble", [('A-5', 1.0), ('A-5', 1.0), ('G-5', 1.0), ('G-5', 1.0)])
    add_notes(score,"Bass",[('F4', 1.0), ('C4', 1.0), ('E-4', 1.0), ('C4', 1.0)])
    add_notes(score,"Treble", [('F5', 1.0), ('F5', 1.0), ('E-5', 1.0), ('E-5', 1.0)])
    add_notes(score,"Bass",[ ('D-4', 1.0), ('B-3', 1.0), ('C4', 1.0), ('A-3', 1.0)])
    add_notes(score,"Treble", [('D-5', 1.0), ('D-5', 0.75), ('E-5', 0.25), ('C5', 2.0)])
    add_notes(score,"Bass",[('F3', 1.0), ('G-3', 1.0), ('C3', 2.0)])
    for p in score.parts:
        for m in p.getElementsByClass('Measure'):
            m.makeBeams(inPlace=True)
    return score