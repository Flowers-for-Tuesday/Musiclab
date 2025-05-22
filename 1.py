from manim import *

class ShowLilyPondSVG(Scene):
    def construct(self):
        self.camera.background_color = WHITE  # 改成你想要的颜色
         
        svg1 = SVGMobject("score_processed.svg",color=BLACK)

        # 初始透明进入
        self.play(Create(svg1))
        self.wait(2)
        self.play(svg1.animate.scale(2))

        self.wait(2)
        Text

