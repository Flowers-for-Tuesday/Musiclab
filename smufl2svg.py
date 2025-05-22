from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
import svgwrite
from pathlib import Path
import re

def safe_filename(name: str) -> str:
    # 只保留字母数字，其他全部替换为下划线
    return re.sub(r'[^A-Za-z0-9]', '_', name)

# 字体文件夹路径
font_dir = Path(r"C:\Users\XMZ\Desktop\Notamia\gonville\otf")

# 输出文件夹
output_dir = Path(r".\MusicSvg")
output_dir.mkdir(exist_ok=True)

# 遍历otf文件
for font_path in font_dir.glob("*.otf"):
    print(f"处理字体文件：{font_path.name}")
    font = TTFont(str(font_path))
    glyph_set = font.getGlyphSet()
    units_per_em = font['head'].unitsPerEm

    # 针对每个字形导出svg
    for glyph_name in glyph_set.keys():
        glyph = glyph_set[glyph_name]
        pen = SVGPathPen(glyph_set)
        glyph.draw(pen)
        path_data = pen.getCommands()

        if not path_data.strip():
            continue

        safe_name = safe_filename(glyph_name)
        svg_file = output_dir / f"{safe_name}.svg"

        dwg = svgwrite.Drawing(str(svg_file), profile='tiny')
        group = dwg.g(transform=f"translate(0, {units_per_em}) scale(1, -1)")
        group.add(dwg.path(d=path_data, fill='black'))
        dwg.add(group)

        dwg.save()

print(f"导出完成，所有 SVG 文件在：{output_dir.resolve()}")
