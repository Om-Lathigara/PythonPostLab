import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,1,1000,endpoint=False)
sine1 = np.sin(2*np.pi*5*t)
sine2 = np.sin(2*np.pi*10*t)
sum_signal = sine1 + sine2

plt.plot(t,sum_signal)
plt.title("Sum of 5Hz and 10Hz sine waves")
plt.show()
