from music21 import converter, note, chord, stream, tempo

def analyze_midi(file_path: str):
    # 读取 MIDI 文件
    score = converter.parse(file_path)

    # 确保是 stream.Score 类型
    if not isinstance(score, stream.Score):
        score = stream.Score([score])

    # 查找第一个 tempo 标记（通常在第一个小节）
    bpm = None
    for t in score.recurse().getElementsByClass(tempo.MetronomeMark):
        if t.number is not None:
            bpm = t.number
            break

    print(f"\n🎵 Detected BPM: {bpm if bpm is not None else 'Not found'}")

    # 遍历每个 Part
    for i, part in enumerate(score.parts):
        print(f"\n--- Part {i+1}: {part.partName or part.id or f'Unnamed Part {i+1}'} ---")

        notes_chords_list = []  # 用于存储当前 part 的 note 和 chord

        for n in part.recurse().notes:
            if isinstance(n, note.Note):
                pitch = n.pitch.nameWithOctave
                duration = n.quarterLength
                offset = n.offset
                print(f"Note: {pitch}, Duration: {duration}, Offset: {offset}")
                # 存储为 ("E5", 0.5) 形式
                notes_chords_list.append((pitch, duration))
            elif isinstance(n, chord.Chord):
                pitches = [p.nameWithOctave for p in n.pitches]
                duration = n.quarterLength
                offset = n.offset
                print(f"Chord: {pitches}, Duration: {duration}, Offset: {offset}")
                # 存储为 (["G#5", "B5", "E6"], 1.0) 形式
                notes_chords_list.append((pitches, duration))

        # 输出该 part 收集的列表
        print("\nCollected notes and chords in this part:")
        print(notes_chords_list)
