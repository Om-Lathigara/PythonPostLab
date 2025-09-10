import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,1,1000,endpoint=False)
sine = np.sin(2*np.pi*5*t)
shifted_sine = np.sin(2*np.pi*5*(t-0.1))

plt.plot(t,sine,label="Original")
plt.plot(t,shifted_sine,label="Shifted")
plt.legend()
plt.title("Original and Shifted 5Hz sine wave")
plt.show()
