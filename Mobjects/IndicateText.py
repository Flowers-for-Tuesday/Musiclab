from manim import *
from typing import Literal

class ArcText(VGroup):
    def __init__(
        self,
        text: str | Mobject,
        mob1: Mobject,
        mob2: Mobject,
        angle: float = PI / 3,
        buff: float = 0.2,
        text_buff: float = 0.4,
        text_size: float = 28,
        direction: Literal["UP", "DOWN"] = "UP",
        **kwargs
    ):
        super().__init__(**kwargs)

        dir_vec = UP if direction == "UP" else DOWN
        arc_angle = -angle if direction == "UP" else angle

        p1 = mob1.get_center() + dir_vec * buff
        p2 = mob2.get_center() + dir_vec * buff

        arc = ArcBetweenPoints(p1, p2, angle=arc_angle)
        label = text if isinstance(text, Mobject) else Text(text, font_size=text_size)
        label.move_to(arc.point_from_proportion(0.5) + dir_vec * text_buff)

        self.add(arc, label)
        self.arc = arc
        self.label = label

class BracketText(VGroup):
    def __init__(
        self,
        text: str | Mobject,
        mob1: Mobject,
        mob2: Mobject,
        line_height: float = 0.5,
        line_buff: float = 0.2,
        text_buff: float = 0.4,
        text_size: float = 28,
        direction: Literal["UP", "DOWN"] = "UP",
        **kwargs
    ):
        super().__init__(**kwargs)

        dir_vec = UP if direction == "UP" else DOWN

        p1 = mob1.get_center() + dir_vec * line_buff + dir_vec * line_height
        p2 = mob2.get_center() + dir_vec * line_buff + dir_vec * line_height

        vertical1 = Line(mob1.get_center() + dir_vec * line_buff, p1)
        vertical2 = Line(mob2.get_center() + dir_vec * line_buff, p2)
        horizontal = Line(p1, p2)

        label = text if isinstance(text, Mobject) else Text(text, font_size=text_size)
        label.move_to(horizontal.get_center() + dir_vec * text_buff)

        self.add(vertical1, horizontal, vertical2, label)
        self.label = label
        self.verticals = VGroup(vertical1, vertical2)
        self.horizontal = horizontal

class ArrowText(VGroup):
    def __init__(
        self,
        text: str | Mobject,
        mob1: Mobject,
        mob2: Mobject,
        buff: float = 0.5,
        text_buff: float = 0.3,
        text_size: float = 28,
        direction: Literal["UP", "DOWN"] = "UP",
        arrow_kwargs: dict = {},
        **kwargs
    ):
        super().__init__(**kwargs)

        dir_vec = UP if direction == "UP" else DOWN

        # 起点与终点向外偏移
        v = mob2.get_center() - mob1.get_center()
        v_norm = v / np.linalg.norm(v)

        start = mob1.get_center() + v_norm * buff
        end = mob2.get_center() - v_norm * buff

        # 创建箭头
        arrow = Arrow(start, end, **arrow_kwargs)

        # 创建文本
        label = text if isinstance(text, Mobject) else Text(text, font_size=text_size)
        label.move_to(arrow.get_center() + dir_vec * text_buff)

        # 加入组
        self.add(arrow, label)
        self.arrow = arrow
        self.label = label