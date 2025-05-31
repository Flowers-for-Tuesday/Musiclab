from manim import *
from Mobjects import *
from utils import *
from music21 import *

class Scene2(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        sc1 = piano_score("C","4/4",["Treble"])
        add_notes(sc1,"Treble",[("E4",4),("G4",4)])
        mtx1 = MusicTex(sc1,clef_on=False,keysignature_on=False,timesignature_on=False,barline_on=False).scale(0.7)
        self.play(Write(mtx1))
        self.wait(2)
        self.play(VGroup(mtx1[5],mtx1[6]).animate.shift(UP*SCORE_INTERVAL*2*0.6))
        self.wait(0.5)
        self.play(VGroup(mtx1[5],mtx1[6]).animate.shift(UP*SCORE_INTERVAL*1*0.6))
        self.wait(0.5)
        self.play(VGroup(mtx1[5],mtx1[6]).animate.shift(DOWN*SCORE_INTERVAL*3*0.6))
        self.wait(1)
        mtx2 = MusicTex(sc1,timesignature_on=False,barline_on=False).scale(0.7)
        #showlabel(mtx2)
        self.play(Transform(mtx1,mtx2))
        self.wait(1)
        text1 = Text("G4",color=BLACK,weight=BOLD).scale(0.4).next_to(mtx2[1],RIGHT)
        self.add_sound(NoteAudio("G4").wav_path)
        self.play(Indicate(mtx1[1],color=BLUE),Indicate(mtx1[7],color=BLUE),Write(text1))
        self.wait(1)
        sc2 = piano_score("C","4/4",["Treble"])
        add_notes(sc2,"Treble",[("C4",4),("D4",4),("E4",4),("F4",4),("G4",4),("A4",4),("B4",4)])
        mtx2 = MusicTex(sc2,timesignature_on=False,barline_on=False).scale(0.7)
        self.play(Transform(mtx1,mtx2),FadeOut(text1))
        #showlabel(mtx2)
        text2 = TextWithBackground(Text("C4",color=BLACK,weight=BOLD).scale(0.4).next_to(mtx2[11],DOWN))
        text3 = TextWithBackground(Text("D4",color=BLACK,weight=BOLD).scale(0.4).next_to(mtx2[9],DOWN))
        text4 = TextWithBackground(Text("E4",color=BLACK,weight=BOLD).scale(0.4).next_to(mtx2[13],DOWN))
        text5 = TextWithBackground(Text("F4",color=BLACK,weight=BOLD).scale(0.4).next_to(mtx2[12],DOWN))
        text6 = TextWithBackground(Text("G4",color=BLACK,weight=BOLD).scale(0.4).next_to(mtx2[7],DOWN))
        text7 = TextWithBackground(Text("A4",color=BLACK,weight=BOLD).scale(0.4).next_to(mtx2[6],DOWN))
        text8 = TextWithBackground(Text("B4",color=BLACK,weight=BOLD).scale(0.4).next_to(mtx2[8],DOWN))
        self.wait(1)
        self.play(Write(VGroup(text2,text3,text4,text5,text6,text7,text8)))
        self.wait(1)
        self.add_sound(NoteAudio("C4").wav_path)
        self.play(Indicate(mtx1[11],color=RED_A))
        self.add_sound(NoteAudio("D4").wav_path)
        self.play(Indicate(mtx1[9],color=RED_A))
        self.add_sound(NoteAudio("E4").wav_path)
        self.play(Indicate(mtx1[13],color=RED_A))
        self.add_sound(NoteAudio("F4").wav_path)
        self.play(Indicate(mtx1[12],color=RED_A))
        self.add_sound(NoteAudio("G4").wav_path)
        self.play(Indicate(mtx1[7],color=RED_A))
        self.add_sound(NoteAudio("A4").wav_path)
        self.play(Indicate(mtx1[6],color=RED_A))
        self.add_sound(NoteAudio("B4").wav_path)
        self.play(Indicate(mtx1[8],color=RED_A))
        self.wait(2)
        sc3 = piano_score("C","4/4",["Bass"])
        add_notes(sc3,"Bass",[("C3",4),("D3",4),("E3",4),("F3",4),("G3",4),("A3",4),("B3",4)])
        mtx3 = MusicTex(sc3,timesignature_on=False,barline_on=False).scale(0.5)
        #showlabel(mtx3)
        self.play(*[mob.animate.shift(UP*2) for mob in self.mobjects])
        self.play(Write(mtx3))
        self.wait(1)
        text9 = Text("G4",color=BLACK,weight=BOLD).scale(0.4).next_to(mtx3[3],RIGHT)
        self.play(Indicate(mtx3[3],color=BLUE),Indicate(mtx3[11],color=BLUE),Write(text9))
        self.wait(1)
        text16 = TextWithBackground(Text("C3",color=BLACK,weight=BOLD).scale(0.4).next_to(mtx3[10],DOWN))
        text10 = TextWithBackground(Text("D3",color=BLACK,weight=BOLD).scale(0.4).next_to(mtx3[8],DOWN))
        text11 = TextWithBackground(Text("E3",color=BLACK,weight=BOLD).scale(0.4).next_to(mtx3[12],DOWN))
        text12 = TextWithBackground(Text("F3",color=BLACK,weight=BOLD).scale(0.4).next_to(mtx3[11],DOWN))
        text13 = TextWithBackground(Text("G3",color=BLACK,weight=BOLD).scale(0.4).next_to(mtx3[6],DOWN))
        text14 = TextWithBackground(Text("A3",color=BLACK,weight=BOLD).scale(0.4).next_to(mtx3[5],DOWN))
        text15 = TextWithBackground(Text("B3",color=BLACK,weight=BOLD).scale(0.4).next_to(mtx3[7],DOWN))
        self.play(Write(VGroup(text16,text10,text11,text12,text13,text14,text15)),FadeOut(text9))
        self.wait(1)

        sc4 = piano_score("C","4/4",["Treble","Bass"])
        add_notes(sc4,"Treble",[("C4",4),("D4",4),("E4",4),("F4",4),("G4",4),("A4",4),("B4",4)])
        add_notes(sc4,"Bass",[("C3",4),("D3",4),("E3",4),("F3",4),("G3",4),("A3",4),("B3",4)])
        mtx4 = MusicTex(sc4,timesignature_on=False,barline_on=False).scale(1.5)
        text17 = Text("大谱表（Grand Staff）",color=BLACK).next_to(mtx4,UP)
        self.play(Transform(VGroup(mtx1,mtx3),mtx4),FadeOut(text2,text3,text4,text5,text6,text7,text7,text8,text10,text11,text12,text13,text14,text15,text16))
        self.play(Write(text17))
        self.wait(2)
        self.play(FadeOut(text17))
        self.play(Circumscribe(mtx4[21],color=BLUE_D),run_time=2)
        self.wait(1)
        sc5 = piano_score("C","4/4",["Treble","Bass"])
        add_notes(sc5,"Treble",[("C5",4),("D5",4),("E5",4),("F5",4),("G5",4),("A5",4),("B5",4)])
        add_notes(sc5,"Bass",[("C2",4),("D2",4),("E2",4),("F2",4),("G2",4),("A2",4),("B2",4)])
        mtx5 = MusicTex(sc5,timesignature_on=False,barline_on=False).scale(1.7)
        self.play(FadeOut(*self.mobjects),FadeIn(mtx5))
        self.wait(2)
        sc6 = piano_score("C","4/4",["Treble","Bass"])
        add_notes(sc6,"Treble",[("C6",4),("D6",4),("E6",4),("F6",4),("G6",4),("A6",4),("B6",4)])
        add_notes(sc6,"Bass",[("C1",4),("D1",4),("E1",4),("F1",4),("G1",4),("A1",4),("B1",4)])
        mtx6 = MusicTex(sc6,timesignature_on=False,barline_on=False).scale(1.9)
        self.play(FadeOut(mtx5),FadeIn(mtx6))
        #showlabel(mtx6)
        self.wait(4)
        image1 = ImageMobject("3.png").scale(0.7)
        text18 =Text("Liszt, “Sursum corda” from Années de Pèlerinage, Year 3",t2s={"Années de Pèlerinage":ITALIC},color=BLACK).scale(0.4).next_to(image1,DOWN)
        self.play(FadeOut(mtx6),FadeIn(image1))
        self.play(Write(text18))
        self.wait(2)
        text19 = Text("8va : 上移八度\n8vb : 下移八度",color=BLACK).scale(0.6).next_to(image1,UP)
        self.play(Write(text19))
        self.wait(3)
        self.play(FadeOut(*self.mobjects))
        sc7 = piano_score("C","4/4",["Treble"],bpm=60)
        add_notes(sc7, "Treble", [
            ("rest", 0.5),
            [("F#4", 0.25), ("A4", 0.25)],
            [("D5", 0.25), ("F#4", 0.25), ("A4", 0.25), ("D5", 0.25)],
            ("rest", 0.5),
            [("F4", 0.25), ("A4", 0.25)],
            [("D5", 0.25), ("F4", 0.25), ("A4", 0.25), ("D5", 0.25)]
        ])

        mtx7 = MusicTex(sc7,timesignature_on=False)
        #showlabel(mtx7)
        self.play(Write(mtx7))
        self.wait(1)
        self.play(Indicate(mtx7[32]),run_time=2)
        self.play(mtx7.animate.shift(DOWN*1))
        piano2 = MultiOctavePianoKeyboard().shift(UP*1.5)
        self.play(FadeIn(piano2))
        self.add_sound(MusicAudio(sc7).wav_path)
        for event in score_events(sc7,relative_octave=4,bpm=60):
            self.play(piano2.animate.markKeys(event[0]), run_time=0.05)
            wait_time = max(event[1] - 0.1, 0.01)
            self.wait(wait_time)
            self.play(piano2.animate.unmarkKeys(event[0]), run_time=0.05)
        self.wait(2)

        sc8 = piano_score("C","4/4",["Treble"],bpm=60)
        add_notes(sc8, "Treble", [
            ("rest", 0.5),
            [("F#4", 0.25), ("A4", 0.25)],
            [("D5", 0.25), ("F#4", 0.25), ("A4", 0.25), ("D5", 0.25)],
            ("rest", 0.5),
            [("F4", 0.25), ("A4", 0.25)],
            [("D5", 0.25), ("F4", 0.25), ("A4", 0.25), ("D5", 0.25)]
        ])
        mtx8 = MusicTex(sc8,timesignature_on=False).shift(DOWN*1)
        self.play(FadeOut(mtx7),FadeIn(mtx8))
        #showlabel(mtx8)
        
        

        

