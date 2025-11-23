import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate

# Generate test audio signals
fs = 44100
t = np.linspace(0, 1, fs)

clean_audio = np.sin(2 * np.pi * 440 * t)                     # Clean sine wave
noisy_audio = clean_audio + 0.5 * np.random.randn(fs)         # Add noise
periodic_audio = np.sin(2 * np.pi * 5 * t)                   # Low frequency periodic signal

clean_audio = clean_audio / np.max(np.abs(clean_audio))
noisy_audio = noisy_audio / np.max(np.abs(noisy_audio))
periodic_audio = periodic_audio / np.max(np.abs(periodic_audio))

def autocorrelation(x):
    return correlate(x, x, mode='full') / len(x)

def cross_correlation(x, y):
    return correlate(x, y, mode='full') / min(len(x), len(y))

auto_corr_clean = autocorrelation(clean_audio)
auto_corr_noisy = autocorrelation(noisy_audio)
auto_corr_periodic = autocorrelation(periodic_audio)
cross_corr_clean_noisy = cross_correlation(clean_audio, noisy_audio)

plt.figure(figsize=(12, 10))

plt.subplot(4, 1, 1)
plt.plot(auto_corr_clean, color='b')
plt.title('Autocorrelation of Clean Audio')
plt.xlabel('Lag')
plt.ylabel('Correlation')

plt.subplot(4, 1, 2)
plt.plot(auto_corr_noisy, color='g')
plt.title('Autocorrelation of Noisy Audio')
plt.xlabel('Lag')
plt.ylabel('Correlation')

plt.subplot(4, 1, 3)
plt.plot(auto_corr_periodic, color='r')
plt.title('Autocorrelation of Periodic Audio')
plt.xlabel('Lag')
plt.ylabel('Correlation')

plt.subplot(4, 1, 4)
plt.plot(cross_corr_clean_noisy, color='m')
plt.title('Cross-Correlation between Clean and Noisy Audio')
plt.xlabel('Lag')
plt.ylabel('Correlation')

plt.tight_layout()
plt.show()
