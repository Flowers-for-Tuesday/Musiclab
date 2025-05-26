from manim import *

class Flash(Scene):
    def construct(self):
        # 目标 Mobject：一个文字
        target = Tex("F Major", font_size=72,color=BLUE)
        
        text1 = Text("F# minor").next_to(target,DOWN)
        self.add(target,text1)

        rect = SurroundingRectangle(VGroup(target,text1), buff=0.2)
        path = VMobject()
        path.set_points_as_corners([
            rect.get_corner(UL),
            rect.get_corner(UR),
            rect.get_corner(DR),
            rect.get_corner(DL),
            rect.get_corner(UL), 
        ])
        path.set_stroke(width=4)
        path.set_color(YELLOW)
        self.play(ShowPassingFlash(path, time_width=0.3, run_time=3))
        self.wait(1)
