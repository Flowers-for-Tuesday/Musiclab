import subprocess
from pathlib import Path

fontforge_path = r".\FontForgeBuilds\bin\fontforge.exe"
font_path = r".\bravura-bravura-1.380\redist\otf\Bravura.otf"
output_dir = Path(r".\MusicSvg")
output_dir.mkdir(exist_ok=True)

pe_script_path = Path("export_all_glyphs.pe")

cmd = [
    fontforge_path,
    "-script",
    str(pe_script_path),
    str(font_path),
    str(output_dir)
]

subprocess.run(cmd, check=True)

print(f"导出完成，所有 SVG 文件在：{output_dir}")
