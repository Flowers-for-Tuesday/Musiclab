from manim import *

def flash_around(scene: Scene, mobj: Mobject, color=RED_A, run_time=3, buff=0.2, stroke_width=4,rest = False):
    """
    在给定的 Scene 中，让一个路径沿着 mobject 的矩形边缘进行 ShowPassingFlash 闪动动画。

    flash_around(self, group, color=ORANGE, run_time=2)
    """
    rect = SurroundingRectangle(mobj, buff=buff,color=color,stroke_width=stroke_width)
    path = VMobject()
    path.set_points_as_corners([
        rect.get_corner(UL),
        rect.get_corner(DL),
        rect.get_corner(DR),
        rect.get_corner(UR),
        rect.get_corner(UL),
    ])
    path.set_stroke(color=color, width=stroke_width, opacity=1)

    if not rest : scene.play(ShowPassingFlash(path, time_width=0.3, run_time=run_time))
    else : scene.play(Write(rect),run_time=run_time)
    scene.wait(0.5)