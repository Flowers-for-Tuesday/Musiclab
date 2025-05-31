from manim import *
import numpy as np
import librosa


class AudioVisualizer(VGroup):
    def __init__(
        self,
        wav_path: str,
        duration: float = 5.0,
        num_bars: int = 20,
        time_per_frame: float = 0.1,
        max_bar_height: float = 2.0,
        bar_width: float = 0.08,
        spacing: float = 0.2,
        color: ManimColor = BLUE,
    ):
        super().__init__()

        self.wav_path = wav_path
        self.duration = duration
        self.num_bars = num_bars
        self.time_per_frame = time_per_frame
        self.max_bar_height = max_bar_height
        self.bar_width = bar_width
        self.spacing = spacing
        self.color = color

        self.bars = self._create_initial_bars()
        self.add(self.bars)

        self.spectrogram = self._load_and_process_audio()

    def _create_initial_bars(self):
        bars = VGroup()
        for i in range(self.num_bars):
            bar = Rectangle(
                width=self.bar_width, height=0.1,
                color=self.color, fill_opacity=0.8
            )
            bar.move_to(LEFT * (self.num_bars / 2 * self.spacing) + RIGHT * i * self.spacing)
            bar.align_to(ORIGIN, DOWN)
            bars.add(bar)
        return bars

    def _load_and_process_audio(self):
        y, sr = librosa.load(self.wav_path, sr=None, mono=True, duration=self.duration)
        hop_length = int(self.time_per_frame * sr)
        n_fft = 2048

        S = np.abs(librosa.stft(y, n_fft=n_fft, hop_length=hop_length))
        S_db = librosa.amplitude_to_db(S, ref=np.max)

        # 取前 num_bars 个频段（低频部分），并归一化
        S_norm = (S_db[:self.num_bars].T - S_db.min()) / (S_db.max() - S_db.min())
        return S_norm  # shape: (frames, num_bars)

    def get_animation(self):
        succession_list = []

        for t in range(self.spectrogram.shape[0]):
            frame = self.spectrogram[t]
            new_frame = VGroup()
            for i in range(self.num_bars):
                height = frame[i] * self.max_bar_height + 0.05
                bar = Rectangle(
                    width=self.bar_width, height=height,
                    color=self.color, fill_opacity=0.8
                )
                bar.move_to(LEFT * (self.num_bars / 2 * self.spacing) + RIGHT * i * self.spacing)
                bar.align_to(ORIGIN, DOWN)
                new_frame.add(bar)

            frame_anims = [
                old_bar.animate.become(new_bar)
                for old_bar, new_bar in zip(self.bars, new_frame)
            ]
            succession_list.append(AnimationGroup(*frame_anims, lag_ratio=0.0))
            succession_list.append(Wait(self.time_per_frame))

        return Succession(*succession_list)
