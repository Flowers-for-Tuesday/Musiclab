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
        aligned: bool = False,
        **kwargs
    ):
        super().__init__(**kwargs)

        dir_vec = UP if direction == "UP" else DOWN

        # 物体中心
        c1, c2 = mob1.get_center(), mob2.get_center()

        if aligned:
            # 方向 UP: 以高的物体为基准线
            if direction == "UP":
                start_y = max(c1[1], c2[1]) + line_buff
                end_y = start_y + line_height
            else:
                # DOWN: 以低的物体为基准线
                start_y = min(c1[1], c2[1]) - line_buff
                end_y = start_y - line_height

            start1 = np.array([c1[0], start_y, c1[2]])
            start2 = np.array([c2[0], start_y, c2[2]])
            end1 = np.array([c1[0], end_y, c1[2]])
            end2 = np.array([c2[0], end_y, c2[2]])
        else:
            # 原始逻辑
            start1 = c1 + dir_vec * line_buff
            start2 = c2 + dir_vec * line_buff
            end1 = start1 + dir_vec * line_height
            end2 = start2 + dir_vec * line_height

        vertical1 = Line(start1, end1)
        vertical2 = Line(start2, end2)
        horizontal = Line(end1, end2)

        # 标签
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
