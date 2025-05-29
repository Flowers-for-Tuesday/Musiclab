import os
import tempfile
import music21
import subprocess
import shutil
import uuid
from manim import *

__all__ = [
    "MusicTex",
    "SCORE_WIDTH"
]

SCORE_WIDTH = 0.2730748225013653  #musictex默认大小时两条谱线的间距

class MusicTex(SVGMobject):
    def __init__(
        self,
        score: music21.stream.Score,
        musicxml2ly_script=r".\lilypond-2.24.4\bin\musicxml2ly.py",
        python_executable=r".\lilypond-2.24.4\bin\python.exe",
        lilypond_executable=r".\lilypond-2.24.4\bin\lilypond.exe",
        svg_output_folder="svg_output",
        line_width=3,
        barline_on=True,#是否有小节线
        clef_on=True,#是否有谱号
        timesignature_on=True,#是否有拍号
        staffsymbol_on=True,#是否有五线谱
        **kwargs
    ):
        """
        score: music21 Score 对象
        musicxml2ly_script: musicxml2ly.py 脚本路径
        python_executable: python 可执行文件路径
        lilypond_executable: lilypond 可执行文件路径
        svg_output_folder: SVG 输出目录
        kwargs: 传递给 SVGMobject 的其他参数
        """
        self._tmp_dir = tempfile.TemporaryDirectory()
        tmpdir = self._tmp_dir.name

        self.barline_on = barline_on 
        self.clef_on = clef_on
        self.timesignature_on = timesignature_on
        self.staffsymbol_on = staffsymbol_on

        # 保存 MusicXML
        self.musicxml_file = os.path.join(tmpdir, "score.musicxml")
        score.write("musicxml", fp=self.musicxml_file)

        unique_prefix = f"score_{uuid.uuid4().hex[:8]}"
        self.intermediate_ly = os.path.join(tmpdir, "score.ly")
        self.processed_ly = os.path.join(tmpdir, "score_processed.ly")
        self.svg_basename = unique_prefix
        self.svg_output_folder = svg_output_folder
        self.svg_output_path = os.path.join(self.svg_output_folder, f"{self.svg_basename}.svg")

        # === 步骤 1: 转换为 .ly 文件 === #
        if not self._convert_musicxml_to_ly(self.musicxml_file, self.intermediate_ly, python_executable, musicxml2ly_script):
            raise RuntimeError("MusicXML 转换为 .ly 失败")

        # === 步骤 2: 处理 .ly 文件（去掉 header）=== #
        self._process_ly_file(self.intermediate_ly, self.processed_ly)

        # === 步骤 3: 生成 SVG 文件 === #
        if not self._generate_svg(lilypond_executable, self.processed_ly, self.svg_output_folder):
            raise RuntimeError("生成 SVG 文件失败")

        # === 步骤 4: 读取 SVG 文件 === #
        if not os.path.isfile(self.svg_output_path):
            raise FileNotFoundError(f"找不到生成的 SVG 文件: {self.svg_output_path}")

        super().__init__(file_name=self.svg_output_path, **kwargs)
        self._fix_svg_lines(line_width)#修复五线谱显示错误

    def _convert_musicxml_to_ly(self, musicxml_path, ly_output_path, python_exe, script_path):
        cmd = [python_exe, script_path, musicxml_path]
        try:
            subprocess.run(cmd, check=True)
            generated_ly = "score.ly"  # 默认生成在当前目录
            if not os.path.exists(generated_ly):
                print("未找到生成的 score.ly 文件")
                return False
            shutil.move(generated_ly, ly_output_path)
            print("MusicXML 转换为 .ly 成功")
            return True
        except subprocess.CalledProcessError as e:
            print("转换失败：", e)
            return False

    def _process_ly_file(self, input_path, output_path):
        with open(input_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        output_lines = []

        if not self.barline_on:
            output_lines.append('\\layout {\n  \\omit Staff.BarLine\n}\n\n')
        if not self.clef_on:
            output_lines.append('\\layout {\n  \\omit Staff.Clef\n}\n\n')
        if not self.timesignature_on:
            output_lines.append('\\layout {\n  \\omit Staff.TimeSignature\n}\n\n')
        if not self.staffsymbol_on:
            output_lines.append('\\layout {\n  \\omit Staff.StaffSymbol\n}\n\n')

        inside_header = False
        for line in lines:
            stripped = line.strip()

            # 跳过 header 块
            if stripped.startswith(r'\header'):
                inside_header = True
                continue
            if inside_header and '}' in stripped:
                inside_header = False
                continue
            if inside_header:
                continue

            output_lines.append(line)

        # 隐藏默认 tagline
        if not any('tagline = ##f' in l for l in output_lines):
            output_lines.append('\n\\paper {\n  tagline = ##f\n}\n')

        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(output_lines)

        print(f"处理后的 .ly 文件输出至 {output_path}")

    def _generate_svg(self, lilypond_exe, ly_path, output_dir):
        if not os.path.isdir(output_dir):
            os.makedirs(output_dir)

        cmd = [
            lilypond_exe,
            '-dbackend=svg',
            '-o', os.path.join(output_dir, self.svg_basename),  # 添加文件名前缀
            ly_path
        ]
        try:
            subprocess.run(cmd, check=True)
            print(f"SVG 文件生成成功：{self.svg_output_path}")
            return True
        except subprocess.CalledProcessError as e:
            print("SVG 生成失败：", e)
            return False
        
    def _fix_svg_lines(self, width=3):
        "修复线条错误"
        for submobj in self.submobjects:
            if isinstance(submobj, Line):
                submobj.set_stroke(width=width)

    def __del__(self):
        try:
            self._tmp_dir.cleanup()
        except Exception:
            pass
