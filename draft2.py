from music21 import converter, tempo

# 加载 MIDI 文件
score = converter.parse("output.mid")

# 搜索 tempo 标记
metronome_marks = score.flat.getElementsByClass(tempo.MetronomeMark)

# 输出 BPM
for mark in metronome_marks:
    print(f"BPM: {mark.number}")
