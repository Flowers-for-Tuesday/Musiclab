from manim import *
from MusicSvg import MusicSvg 
from MusicTex import MusicTex
from music21 import *

class ShowLilyPondSVG(Scene):
    def construct(self):
        self.camera.background_color = WHITE  # 改成你想要的颜色

        # 创建一个新的乐谱对象
        score = stream.Score()

        part = stream.Part()

        # 设置调号（C大调）和拍号（4/4）
        part.append(key.KeySignature(0))       # 0 代表 C 大调/A 小调
        part.append(meter.TimeSignature('4/4'))

        # 添加四个音符 C D E F
        notes = ['C4', 'D4', 'E4','F4']
        for pitch in notes:
            n = note.Note(pitch)
            n.quarterLength = 1  # 每个音符一个四分音符时值
            part.append(n)

        # 将乐段添加到乐谱
        score.append(part)
        music1 = MusicTex(score,clef_on=False)
        self.play(Write(music1))
        self.wait(2)

        # 添加四个音符 C D E F
        # 创建一个新的乐谱对象
        score2 = stream.Score()

        # 创建一个新的乐段（Part），可以是钢琴、长笛等任意乐器
        part = stream.Part()

        # 设置调号（C大调）和拍号（4/4）
        part.append(key.KeySignature(0))       # 0 代表 C 大调/A 小调
        notes = ['C4', 'D4', 'E4', 'F4','G4']
        for pitch in notes:
            n = note.Note(pitch)
            n.quarterLength = 1  # 每个音符一个四分音符时值
            part.append(n)
        score2.append(part)
        music2 = MusicTex(score2,measure_on=False,timesignature_on=False)
        self.play(Transform(music1,music2))
        self.wait(2)

