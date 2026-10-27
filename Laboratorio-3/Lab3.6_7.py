import numpy as np
import matplotlib.pyplot as plt

# Definición del eje temporal
dt = 0.01
t = np.arange(-10, 10, dt)

# Definición de la señal base x6(t)
x6 = np.where((t >= -1) & (t < 0), -2.0 * t, np.where((t >= 0) & (t <= 1), 2.0 * t, 0.0))

# Cálculo de la convolución y7(t)
y7 = np.convolve(x6, x6, mode='full') * dt
t_y = np.linspace(t[0] + t[0], t[-1] + t[-1], len(y7))

# Gráficas
plt.figure(figsize=(8, 7))

plt.subplot(2, 1, 1)
plt.plot(t, x6, 'b-', linewidth=2)
plt.title(r'Señal de entrada $x_6(t)$')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t_y, y7, 'r-', linewidth=2)
plt.title(r'Convolución $y_7(t) = x_6(t) * x_6(t)$')
plt.xlabel(r'Tiempo ($t$)')
plt.grid(True)

plt.tight_layout()
plt.show()