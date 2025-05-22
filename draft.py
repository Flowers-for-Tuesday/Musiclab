from music21 import stream, note
from MusicAudio import MusicAudio

s = stream.Score()
p = stream.Part()
p.append([note.Note("C4"), note.Note("E4"), note.Note("G4")])
s.append(p)

converter = MusicAudio(score=s)
print("生成的 WAV 文件地址：", converter.wav_path)
