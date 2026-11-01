import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

t = np.linspace(0, 3, 500)
x = np.exp(-5 * t)

# Sistema B
sys = signal.TransferFunction([1, 0, -1], [1, -1, 0, -12])
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
plt.title(r'$H_b(s) = \frac{s^2 - 1}{s^3 - s^2 - 12}$' + '  ⇒ \n ' + r'$h_b(t) = \left( \frac{4}{5}e^{3t} + \frac{1}{5}e^{-t}\cos(\sqrt{3}t) - \frac{\sqrt{3}}{5}e^{-t}\sin(\sqrt{3}t) \right)u(t)$')
plt.ylabel('Amplitud')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, y, color='green', linewidth=2.5)
plt.title(r'$y_b(t) = h_b(t) * x(t)$')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)

plt.tight_layout()
plt.show()
