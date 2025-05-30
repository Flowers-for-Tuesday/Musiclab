import librosa
import librosa.display
import matplotlib.pyplot as plt

y, sr = librosa.load("your_audio.wav")
plt.figure(figsize=(10, 4))
librosa.display.waveshow(y, sr=sr)
plt.title("Waveform")
plt.tight_layout()
plt.show()
