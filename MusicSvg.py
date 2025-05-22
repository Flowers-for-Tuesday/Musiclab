from manim import SVGMobject
from pathlib import Path

class MusicSvg(SVGMobject):
    MUSIC_SVG_DIR = Path("./MusicSvg")

    def __init__(self, text: str, **kwargs):
        svg_path = self.MUSIC_SVG_DIR / f"{text}.svg"

        if not svg_path.exists():
            raise FileNotFoundError(f"找不到对应的 SVG 文件：{svg_path}")

        super().__init__(str(svg_path), **kwargs)
