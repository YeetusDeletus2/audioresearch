
from pydub import AudioSegment
import numpy as np
import noisereduce as nr
from scipy.io import wavfile

# Load MP3 and convert to mono 16-bit PCM
audio = AudioSegment.from_mp3("XC281151-210 4 Bosruiter 4 Roep.mp3")
audio = audio.set_channels(1).set_frame_rate(44100).set_sample_width(2)

# Convert audio to numpy array
data = np.array(audio.get_array_of_samples())
rate = audio.frame_rate

# Apply noise reduction
reduced_noise = nr.reduce_noise(y=data, sr=rate)

# Save to WAV
wavfile.write("output.wav", rate, reduced_noise.astype(np.int16))
