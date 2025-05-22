from music21 import stream, note, chord, meter, key, instrument, tempo, dynamics, articulations, expressions, metadata, converter,environment

# 获取配置对象

us = environment.UserSettings()
us['musicxmlPath'] = r"C:\Program Files\MuseScore 4\bin\MuseScore4.exe"

# 也可以尝试设置直接PNG渲染路径（可选）
us['musescoreDirectPNGPath'] = r"C:\Program Files\MuseScore 4\bin\MuseScore4.exe"
print(us['musescoreDirectPNGPath'])  # 如果你配置的是这个路径
print(us['musicxmlPath'])             # MusicXML路径
#print(us['musescorePath'])      
# 创建一个简单乐谱
# 1. 创建乐谱对象
score = stream.Score()
score.metadata = metadata.Metadata()
#score.metadata.title = "Example: Complex music21 Score"
#score.metadata.composer = "Your Name"

# 2. 设置调式与节拍
ks = key.KeySignature(0)  # C major
ts = meter.TimeSignature('4/4')
tempoMark = tempo.MetronomeMark(number=90)

# 3. Soprano 声部（旋律）
soprano = stream.Part()
soprano.id = 'Soprano'
soprano.append(instrument.Soprano())
soprano.append(ks)
soprano.append(ts)
soprano.append(tempoMark)

# 添加旋律（带歌词、连音线、力度、跳音、倚音等）
melody = [
    note.Note('C5', quarterLength=1, lyrics=["Do"]),
    note.Note('E5', quarterLength=1, lyrics=["re"]),
    note.Note('F5', quarterLength=1, lyrics=["mi"]),
    note.Note('G5', quarterLength=1, lyrics=["fa"]),
    note.Rest(quarterLength=1),
    note.Note('A5', quarterLength=2, lyrics=["so"])
]

# 添加演奏标记（staccato）
melody[4].articulations = [articulations.Staccato()]
melody[5].expressions.append(expressions.TextExpression("breath"))

# 添加力度
melody[0].dynamics = dynamics.Dynamic('mf')
melody[4].dynamics = dynamics.Dynamic('f')

# 加入旋律
for n in melody:
    soprano.append(n)

# 4. Bass 声部（和声/低音）
bass = stream.Part()
bass.id = 'Bass'
bass.append(instrument.Bass())
bass.append(ks)
bass.append(ts)

# 添加低音音符与和弦
bass_line = [
    chord.Chord(['C3', 'E3', 'G3'], quarterLength=2),
    chord.Chord(['F3', 'A3', 'C4'], quarterLength=2),
    chord.Chord(['G3', 'B3', 'D4'], quarterLength=2),
    note.Rest(quarterLength=1),
    note.Note('C3', quarterLength=1),
    chord.Chord(['A2', 'E3'], quarterLength=2)
]

for n in bass_line:
    bass.append(n)

# 5. 添加声部进主乐谱
score.append([soprano, bass])
score.metadata = None
# 6. 展示并保存为 MusicXML 文件（你也可以保存为 MIDI、PDF 等）
score.write('musicxml', fp='score.musicxml')

# 若你有 MuseScore 安装好，可直接使用：
#score.show()  # 直接调用 MuseScore 打开