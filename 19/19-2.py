import numpy as np
import matplotlib.pyplot as plt
numerator = [0.5, -1.6, 0.63]
denominator = [1, -1, -0.24]
poles = np.roots(denominator)
plt.figure(figsize=(6, 6))
plt.scatter(np.real(poles), np.imag(poles), color='red', label='Poles')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.title('Pole-Zero Plot')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.grid()
plt.legend()
plt.show()
is_stable = all(abs(p) < 1 for p in poles)
print("Poles:", poles)
print("Is the system stable?", is_stable)
