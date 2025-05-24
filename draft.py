from music21 import *

# 加载 MIDI 文件
midi_file_path = 'For river.mid'  # 替换为你的文件路径
score = converter.parse(midi_file_path)

# 收集所有音高（包含音符和和弦）
pitches = []

for n in score.recurse().notes:
    if isinstance(n, note.Note):
        pitches.append(n.pitch)
    elif isinstance(n, chord.Chord):
        pitches.extend(n.pitches)

# 找出最高和最低音
if pitches:
    highest = max(pitches)
    lowest = min(pitches)
    print(f"🎼 最高音：{highest} （MIDI: {highest.midi}）")
    print(f"🎼 最低音：{lowest} （MIDI: {lowest.midi}）")
else:
    print("没有找到任何音符或和弦。")

# 查找所有速度标记
metronome_marks = score.recurse().getElementsByClass(tempo.MetronomeMark)

# 输出找到的 BPM
if metronome_marks:
    for i, mark in enumerate(metronome_marks, start=1):
        print(f"🎵 BPM #{i}: {mark.number}（备注: {mark.text}）")
else:
    print("⚠️ MIDI 中未找到明确的 BPM 标记。")
