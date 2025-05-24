from music21 import *

def merge_events(events,bpm):
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
            merged.append([active_notes, 60/bpm*(end - start), start])
    
    return merged

def score_events(score: stream.Score,relative_octave:int,bpm:int):
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
    return merge_events(events,bpm)
    