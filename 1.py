from manim import *
from MusicSvg import MusicSvg 
from MusicTex import MusicTex
from showlabel import showlabel
from MusicAudio import MusicAudio
from music21 import *

class ShowLilyPondSVG(Scene):
    def construct(self):
        self.camera.background_color = WHITE  # 改成你想要的颜色

        s = stream.Score()
        piano_part = stream.Part()
        piano_part.insert(0, instrument.Piano())

        # 上声部
        upper = stream.Voice()
        upper.append(clef.TrebleClef())
        upper.append(meter.TimeSignature('4/4'))
        upper.append(key.KeySignature(2))  # D大调
        n1 = note.Note('e5', quarterLength=1)
        n2 = note.Note('f#5', quarterLength=1)
        n3 = note.Note('g5', quarterLength=1)
        slur = spanner.Slur(n1, n3)
        upper.append([n1, n2, n3])
        upper.insert(0, slur)

        # 下声部三连音
        lower = stream.Voice()
        triplet = duration.Tuplet(3, 2)  # 三连音
        for p in ['c4', 'd4', 'e4']:
            n = note.Note(p, quarterLength=1/3)
            n.duration.tuplets = [triplet]  # ✅ 修复：赋值元组列表
            lower.append(n)

        staff = stream.Stream()
        staff.append(upper)
        staff.append(lower)

        piano_part.append(staff)
        s.insert(0, piano_part)
        music1 = MusicTex(s)
        audio1 = MusicAudio(s)
        self.add_sound(audio1.wav_path)
        music2 = MusicTex(s,clef_on=False)
        music3 = MusicTex(s,timesignature_on=False)
        music4 = MusicTex(s,barline_on=False)
        music5 = MusicTex(s,staffsymbol_on=False)
        #showlabel(music1,'music1')
        self.play(Write(music1))
        self.wait(1)
        self.play(Transform(music1,music2))
        self.wait(1)
        self.play(Transform(music1,music3))
        self.wait(1)
        self.play(Transform(music1,music4))
        self.wait(1)
        self.play(Transform(music1,music5))
        self.wait(1)


        

