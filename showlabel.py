import os
from manim import *

def showlabel(svgmob, filename):
    from manim import Scene, FullScreenRectangle, index_labels

    bg = FullScreenRectangle(fill_color=WHITE, fill_opacity=1)
    labels = index_labels(svgmob)

    class TempScene(Scene):
        def construct(temp_self):
            temp_self.add(bg)
            temp_self.add(svgmob)
            temp_self.add(labels)
    output_path = os.path.join("./" +filename)
    config.output_file = output_path

    scene = TempScene()
    scene.render()  # 渲染，默认生成到 media 文件夹

#showlabel(SVGMobject("test.svg"),'test')