import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

# Generate a test audio signal (sine wave)
fs = 44100
t = np.linspace(0, 1, fs)
audio_data = np.sin(2 * np.pi * 440 * t)

# Generate a test impulse response (simple decay)
impulse_response = np.exp(-5*t)

# Normalize
audio_data = audio_data / np.max(np.abs(audio_data))
impulse_response = impulse_response / np.max(np.abs(impulse_response))

# Linear convolution
linear_conv = convolve(audio_data, impulse_response, mode='full')

# Circular convolution
n = len(audio_data)
m = len(impulse_response)
circular_conv = np.fft.ifft(np.fft.fft(audio_data, n+m-1) * np.fft.fft(impulse_response, n+m-1)).real

# Plot
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(audio_data)
plt.title('Original Audio')

plt.subplot(3, 1, 2)
plt.plot(linear_conv)
plt.title('Linear Convolution Result')

plt.subplot(3, 1, 3)
plt.plot(circular_conv)
plt.title('Circular Convolution Result')

plt.tight_layout()
plt.show()
