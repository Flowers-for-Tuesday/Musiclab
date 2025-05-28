from manim import *

def Flash_around(
    mobj: Mobject, 
    color=RED_A, 
    run_time=3, 
    buff=0.2, 
    stroke_width=4, 
    rest=False
) -> Animation:
    """
    返回一个在 mobject 周围闪动的 Animation。
    可用于 self.play(flash_around(...))
    """
    rect = SurroundingRectangle(mobj, buff=buff, color=color, stroke_width=stroke_width)

    if rest:
        return Write(rect, run_time=run_time)

    path = VMobject()
    path.set_points_as_corners([
        rect.get_corner(UL),
        rect.get_corner(DL),
        rect.get_corner(DR),
        rect.get_corner(UR),
        rect.get_corner(UL),
    ])
    path.set_stroke(color=color, width=stroke_width, opacity=1)

    return ShowPassingFlash(path, time_width=0.3, run_time=run_time)

def blink(mobj, duration=0.2):
    return Succession(
        mobj.animate.set_color(RED_A).set_run_time(duration),
        mobj.animate.set_color(WHITE).set_run_time(duration),
        lag_ratio=0.4
    )