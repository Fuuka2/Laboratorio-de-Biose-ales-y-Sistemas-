import numpy as np
import matplotlib.pyplot as plt

# Definición del eje temporal
dt = 0.01
t = np.arange(-8, 5, dt)

# Definición de las señales x(t) y h(t)
x = np.where((t >= 0) & (t <= 1), t + 1.0, np.where((t > 1) & (t <= 2), 2.0 - t, 0.0))

h = np.zeros_like(t)
h[np.argmin(np.abs(t - (-2)))] = 1.0 / dt  
h[np.argmin(np.abs(t - (-1)))] = 2.0 / dt  

# Cálculo de la convolución y(t)
y = np.convolve(x, h, mode='full') * dt
t_y = np.linspace(t[0] + t[0], t[-1] + t[-1], len(y))

# Gráficas
plt.figure(figsize=(8, 10))

plt.subplot(3, 1, 1)
plt.plot(t, x, 'b-', linewidth=2)
plt.title(r'Señal de entrada $x(t)$')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, h, 'g-', linewidth=2)
plt.title(r'Señal de entrada $h(t) = \delta(t+2) + 2\delta(t+1)$')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t_y, y, 'r-', linewidth=2)
plt.title(r'Convolución $y(t) = x(t) * h(t)$')
plt.xlabel(r'Tiempo ($t$)')
plt.grid(True)

plt.tight_layout()
plt.show()