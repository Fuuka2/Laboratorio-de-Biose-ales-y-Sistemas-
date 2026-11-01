import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

t = np.linspace(0, 3, 500)
x = np.exp(-5 * t)

# a)
sys = signal.TransferFunction([6], [1, 6, 5])
_, h = signal.impulse(sys, T=t)
_, y, _ = signal.lsim(sys, x, t)

plt.figure(figsize=(7, 8))
plt.subplot(3, 1, 1)
plt.plot(t, x, color='purple', linewidth=2)
plt.title(r'$x(t) = e^{-5t}$')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, h, color='orange', linewidth=2)
plt.title(r'$H_a(s) = \frac{6}{s^2 + 6s + 5}$' + '  ⇒ \n ' + r'$h_a(t) = \left( \frac{3}{2}e^{-t} - \frac{3}{2}e^{-5t} \right)u(t)$')
plt.ylabel('Amplitud')
plt.xlabel('Tiempo (s)')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, y, color='red', linewidth=2.5)
plt.title(r'$y_a(t) = h_a(t) * x(t)$')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)

plt.tight_layout()
plt.show()