from manim import *

class ArcText(VGroup):
    def __init__(
        self,
        text: str | Mobject,
        mob1: Mobject,
        mob2: Mobject,
        angle: float = PI / 3,
        buff: float = 0.2,
        text_buff: float = 0.4,
        text_size:float = 28,
        **kwargs
    ):
        super().__init__(**kwargs)

        # 获取两个Mobject的上方锚点
        p1 = mob1.get_top() + UP * buff
        p2 = mob2.get_top() + UP * buff

        # 创建弧线
        arc = ArcBetweenPoints(p1, p2, angle=-angle)

        # 创建文本对象
        label = text if isinstance(text, Mobject) else Text(text,font_size=text_size)
        
        # 将 label 放置在弧线的中心稍上方
        label.move_to(arc.point_from_proportion(0.5) + UP * text_buff)

        # 添加到VGroup
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
        text_size:float = 28,
        **kwargs
    ):
        super().__init__(**kwargs)

        # 顶部点位于 mob1 和 mob2 上方 line_height 的位置
        p1 = mob1.get_top()+UP*line_buff + UP * line_height
        p2 = mob2.get_top()+UP*line_buff + UP * line_height

        # 三段路径
        vertical1 = Line(mob1.get_top()+UP*line_buff, p1)
        vertical2 = Line(mob2.get_top()+UP*line_buff, p2)
        horizontal = Line(p1, p2)

        # 文本对象
        label = text if isinstance(text, Mobject) else Text(text,font_size=text_size)
        label.move_to(horizontal.get_center() + UP * text_buff)

        # 加入组
        self.add(vertical1, horizontal,vertical2, label)
        self.label = label
        self.verticals = VGroup(vertical1, vertical2)
        self.horizontal = horizontal