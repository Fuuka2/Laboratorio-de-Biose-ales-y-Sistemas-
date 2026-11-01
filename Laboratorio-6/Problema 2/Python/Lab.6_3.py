import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

t = np.linspace(0, 3, 500)
x = np.exp(-5 * t)

# Sistema C
sys = signal.TransferFunction([1, 0], [1, 2, 3])
_, h = signal.impulse(sys, T=t)
_, y, _ = signal.lsim(sys, x, t)

plt.figure(figsize=(7, 8))
plt.subplot(3, 1, 1)
plt.plot(t, x, color='purple', linewidth=2)
plt.title(r'$x(t) = e^{-5t}$')
plt.ylabel('Amplitud')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, h, color='orange', linewidth=2)
plt.title(r'$H_c(s) = \frac{s}{s^2 + 2s + 3}$' + '  ⇒ \n ' + r'$h_c(t) = e^{-t}\left( \cos(\sqrt{2}t) - \frac{1}{\sqrt{2}}\sin(\sqrt{2}t) \right)u(t)$')
plt.ylabel('Amplitud')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, y, color='blue', linewidth=2.5)
plt.title(r'$y_c(t) = h_c(t) * x(t)$')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)

plt.tight_layout()
plt.show()
