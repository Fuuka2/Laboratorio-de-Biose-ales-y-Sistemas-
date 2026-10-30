import numpy as np
import matplotlib.pyplot as plt

# Definición del eje temporal
dt = 0.01
t = np.arange(-10, 15, dt)

# Definición de las señales base x2(t) y x4(t-3)
x2 = np.where((t >= -1) & (t <= 1), 1.0, 0.0)
x4_desplazado = np.where(((t - 3) > -6) & ((t - 3) < 6), np.sinc((t - 3) / 2.0), 0.0)

# Cálculo de la convolución y10(t)
y10 = np.convolve(x2, x4_desplazado, mode='full') * dt
t_y = np.linspace(t[0] + t[0], t[-1] + t[-1], len(y10))

# Gráficas
plt.figure(figsize=(8, 10))

plt.subplot(3, 1, 1)
plt.plot(t, x2, 'b-', linewidth=2)
plt.title(r'Señal de entrada $x_2(t)$')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, x4_desplazado, 'g-', linewidth=2)
plt.title(r'Señal de entrada $x_4(t-3)$')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t_y, y10, 'r-', linewidth=2)
plt.title(r'Convolución $y_{10}(t) = x_2(t) * x_4(t-3)$')
plt.xlabel(r'Tiempo ($t$)')
plt.grid(True)

plt.tight_layout()
plt.show()