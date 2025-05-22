from manim import *

class TagSubmobjects(Scene):
    def construct(self):
        svg = SVGMobject("test.svg")
        
        # 假设svg有多个子物体，我们给它们自定义“标签”属性
        for i, sub in enumerate(svg.submobjects):
            sub.label = f"part_{i}"  # 给每个子物体打个名字
        
        # 打印标签
        for sub in svg.submobjects:
            print(sub.label)
        
        self.add(svg)
        self.wait()
