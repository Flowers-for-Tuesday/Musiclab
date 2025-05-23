from manim import *
from MusicSvg import MusicSvg 
from MusicTex import MusicTex
from showlabel import showlabel
from MusicAudio import MusicAudio
from PianoKeyboard import *
from music21 import *

right_hand = stream.Part()
right_hand.insert(0, instrument.Piano())
right_hand.insert(0, meter.TimeSignature('4/4'))
right_hand.insert(0, key.Key('C'))
right_hand.insert(0, tempo.MetronomeMark(number=100))

# 添加几小节旋律
for pitch in ['C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6']:
    right_hand.append(note.Note(pitch, quarterLength=0.5))
    #right_hand.append(note.Rest(duration=duration.Duration(0.5)))

for _ in range(4):
    right_hand.append(chord.Chord(['E5', 'G5'], quarterLength=1))

# 左手（低音谱号）
left_hand = stream.Part()
left_hand.insert(0, instrument.Piano())
left_hand.insert(0, meter.TimeSignature('4/4'))
left_hand.insert(0, key.Key('C'))
left_hand.insert(0, tempo.MetronomeMark(number=100))

# 添加低音和弦进行
bass_chords = [
    ['C3', 'E3', 'G3'],
    ['F3', 'A3', 'C4'],
    ['G2', 'B2', 'D3'],
    ['C3', 'E3', 'G3']
]
for _ in range(4):
    for chord_notes in bass_chords:
        left_hand.append(chord.Chord(chord_notes, quarterLength=1))

# 组合为钢琴总谱
score = stream.Score()
score.insert(0, right_hand)
score.insert(0, left_hand)
score.write('midi', fp='output.mid')

def merge_events(events):
    # 1. 按offset排序
    events_sorted = sorted(events, key=lambda x: x[2])
    
    # 2. 找出所有关键时间点：每个事件的start和end
    time_points = set()
    for pitch, dur, offset in events_sorted:
        time_points.add(offset)
        time_points.add(offset + dur)
    time_points = sorted(time_points)
    
    merged = []
    
    # 3. 对相邻时间点合并音符
    for i in range(len(time_points) - 1):
        start = time_points[i]
        end = time_points[i+1]
        active_notes = []
        
        # 找出所有在[start, end)时间段起始，且覆盖该段的非休止音符
        for pitch, dur, offset in events_sorted:
            if pitch == None:
                continue  # 跳过休止符
            if offset <= start < offset + dur:
                active_notes.append(pitch)
        
        if active_notes:
            merged.append([active_notes, end - start, start])
    
    return merged

def playscore(score: stream.Score,relative_octave:int):
    # 收集所有钢琴声部里的所有音符MIDI
    piano_parts = [p for p in score.parts if 'Piano' in p.partName or 'piano' in p.partName.lower()]
    events = []

    relative_pitch = (relative_octave+1)*12
    for part in piano_parts:
        for elem in part.flatten().notesAndRests:
            if isinstance(elem, note.Note):
                events.append([elem.pitch.midi-relative_pitch,elem.duration.quarterLength,elem.offset])
            elif isinstance(elem, chord.Chord):
                for p in elem.pitches:
                    events.append([p.midi-relative_pitch,elem.duration.quarterLength,elem.offset])
            elif isinstance(elem, note.Rest):
                events.append([None,elem.duration.quarterLength,elem.offset])

    

