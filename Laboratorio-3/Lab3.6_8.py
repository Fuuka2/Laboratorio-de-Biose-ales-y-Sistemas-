import numpy as np
import matplotlib.pyplot as plt

# Definición del eje temporal
dt = 0.01
t = np.arange(-10, 10, dt)

# Definición de las señales base x1(t) y x6(t)
x1 = np.where((t > -2) & (t < 2), 1 - np.abs(t) / 2.0, 0.0)
x6 = np.where((t >= -1) & (t < 0), -2.0 * t, np.where((t >= 0) & (t <= 1), 2.0 * t, 0.0))

# Cálculo de la convolución y8(t)
y8 = np.convolve(x1, x6, mode='full') * dt
t_y = np.linspace(t[0] + t[0], t[-1] + t[-1], len(y8))

# Gráficas
plt.figure(figsize=(8, 10))

plt.subplot(3, 1, 1)
plt.plot(t, x1, 'b-', linewidth=2)
plt.title(r'Señal de entrada $x_1(t)$')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, x6, 'g-', linewidth=2)
plt.title(r'Señal de entrada $x_6(t)$')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t_y, y8, 'r-', linewidth=2)
plt.title(r'Convolución $y_8(t)=x_1(t)*x_6(t)$')
plt.xlabel(r'Tiempo ($t$)')
plt.grid(True)

plt.tight_layout()
plt.show()