import numpy as np
import matplotlib.pyplot as plt

# Definición del eje temporal
dt = 0.01
t = np.arange(-10, 10, dt)

# Definición de las señales base x1(t) y x5(t)
x1 = np.where((t > -2) & (t < 2), 1 - np.abs(t) / 2.0, 0.0)
x5 = np.where((t >= 0) & (t <= 1), 2.0 * t, 0.0)

# Cálculo de la convolución y2(t)
y2 = np.convolve(x1, x5, mode='full') * dt
t_y = np.linspace(t[0] + t[0], t[-1] + t[-1], len(y2))

# Gráficas
plt.figure(figsize=(8, 10))

plt.subplot(3, 1, 1)
plt.plot(t, x1, 'b-', linewidth=2)
plt.title(r'Señal de entrada $x_1(t)$')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, x5, 'g-', linewidth=2)
plt.title(r'Señal de entrada $x_5(t)$')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t_y, y2, 'r-', linewidth=2)
plt.title(r'Convolución $y_2(t)=x_1(t)*x_5(t)$')
plt.xlabel(r'Tiempo ($t$)')
plt.grid(True)

plt.tight_layout()
plt.show()