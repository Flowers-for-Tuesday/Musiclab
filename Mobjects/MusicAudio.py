import os
import uuid
import subprocess
import tempfile
from music21 import *

class MusicAudio:
    def __init__(self, score: stream.Score, output_dir: str = "./wav_output"):
        self.score = score
        self.output_dir = output_dir
        self.wav_path = None

        # 默认路径（相对于当前工作目录）
        self.fluidsynth_exe = r".\fluidsynth-2.4.6\bin\fluidsynth.exe"
        self.soundfont_path = r".\SF2_SoundFonts\GeneralUser-GS-v1.471.sf2"

        os.makedirs(self.output_dir, exist_ok=True)
        self._convert_to_wav()

    def _convert_to_wav(self):
        tmp_dir = tempfile.gettempdir()
        file_id = uuid.uuid4().hex
        midi_path = os.path.join(tmp_dir, f"{file_id}.mid")
        wav_path = os.path.join(self.output_dir, f"{file_id}.wav")

        self.score.write('midi', fp=midi_path)

        # 执行 fluidsynth 合成命令
        subprocess.run([
            self.fluidsynth_exe,
            "-ni","-F",
            wav_path, 
            "-r", "44100",
            self.soundfont_path,midi_path
        ], check=True)

        self.wav_path = wav_path

        # 清理临时 midi 文件
        try:
            os.remove(midi_path)
        except OSError:
            pass

class NoteAudio(MusicAudio):
    def __init__(self, input_note, duration: float = 1.0,
                 output_dir: str = "./wav_output",
                 ):
        """
        参数:
        - input_note: 一个音符名字符串（如 "C4"），或一个音符列表表示和弦（如 ["C3", "E3", "G3"]）
        - duration: 音长（以四分音符为单位）
        """
        p = stream.Part()
        if isinstance(input_note, str):
            n = note.Note(input_note)
            n.quarterLength = duration
            p.append(n)
        elif isinstance(input_note, (list, tuple)):
            c = chord.Chord(input_note)
            c.quarterLength = duration
            p.append(c)
        else:
            raise ValueError("input_note 必须是字符串或字符串列表。")

        s = stream.Score()
        s.append(p)

        # 调用父类构造器
        super().__init__(s, output_dir=output_dir)