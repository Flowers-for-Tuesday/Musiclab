import subprocess
import os

def convert_musicxml_to_ly(musicxml_path, ly_output_path, musicxml2ly_path, python_exe):
    if not os.path.isfile(musicxml_path):
        print(f"错误: 找不到输入文件 {musicxml_path}")
        return False

    cmd = [python_exe, musicxml2ly_path, musicxml_path]

    try:
        subprocess.run(cmd, check=True)
        generated_ly = os.path.splitext(musicxml_path)[0] + ".ly"
        if not os.path.exists(generated_ly):
            print("转换失败：找不到生成的 .ly 文件")
            return False
        os.rename(generated_ly, ly_output_path)
        print(f"转换成功！生成文件：{ly_output_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"转换失败，错误信息：\n{e}")
        return False

def process_ly_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    output_lines = []
    inside_header = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith(r'\header'):
            inside_header = True
            continue
        if inside_header and '}' in stripped:
            inside_header = False
            continue
        if not inside_header:
            output_lines.append(line)

    paper_block = '\n\\paper {\n  tagline = ##f\n}\n'
    if not any('tagline = ##f' in l for l in output_lines):
        output_lines.append(paper_block)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)
    print(f".ly 文件处理完成，输出文件：{output_path}")

def generate_svg(lilypond_exe_path, ly_file_path, output_dir):
    if not os.path.isfile(lilypond_exe_path):
        print(f"错误: 找不到LilyPond可执行文件 {lilypond_exe_path}")
        return False
    if not os.path.isfile(ly_file_path):
        print(f"错误: 找不到输入的.ly文件 {ly_file_path}")
        return False
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    cmd = [
        lilypond_exe_path,
        '-dbackend=svg',
        '-o', output_dir,
        ly_file_path
    ]
    print("正在生成SVG文件...")
    try:
        subprocess.run(cmd, check=True)
        print(f"SVG生成成功，输出目录：{output_dir}")
        return True
    except subprocess.CalledProcessError as e:
        print("生成SVG失败，错误信息：")
        print(e)
        return False

if __name__ == "__main__":
    musicxml_file = "score.musicxml"
    intermediate_ly = "score_raw.ly"     # MusicXML转出的初始ly
    processed_ly = "score_processed.ly" # 处理过的ly文件
    musicxml2ly_script = r".\lilypond-2.24.4\bin\musicxml2ly.py"
    python_executable = r".\lilypond-2.24.4\bin\python.exe"
    lilypond_executable = r".\lilypond-2.24.4\bin\lilypond.exe"
    svg_output_folder = "svg_output"

    # 1. MusicXML -> ly
    if convert_musicxml_to_ly(musicxml_file, intermediate_ly, musicxml2ly_script, python_executable):
        # 2. 处理 ly 文件
        process_ly_file(intermediate_ly, processed_ly)
        # 3. 生成 SVG
        generate_svg(lilypond_executable, processed_ly, svg_output_folder)
