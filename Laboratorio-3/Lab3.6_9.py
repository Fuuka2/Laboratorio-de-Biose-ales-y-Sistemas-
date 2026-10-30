import numpy as np
import matplotlib.pyplot as plt

# Definición del eje temporal
dt = 0.01
t = np.arange(-10, 15, dt)

# Definición de las señales base x1(t) y x3(t)
x1 = np.where((t > -2) & (t < 2), 1 - np.abs(t) / 2.0, 0.0)

x3 = np.zeros_like(t)
x3[np.argmin(np.abs(t - 5))] = 1.0 / dt  

# Cálculo de la convolución y9(t)
y9 = np.convolve(x1, x3, mode='full') * dt
t_y = np.linspace(t[0] + t[0], t[-1] + t[-1], len(y9))

# Gráficas
plt.figure(figsize=(8, 10))

plt.subplot(3, 1, 1)
plt.plot(t, x1, 'b-', linewidth=2)
plt.title(r'Señal de entrada $x_1(t)$')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, x3, 'g-', linewidth=2)
plt.title(r'Señal de entrada $x_3(t)$')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t_y, y9, 'r-', linewidth=2)
plt.title(r'Convolución $y_9(t) = x_1(t) * x_3(t)$')
plt.xlabel(r'Tiempo ($t$)')
plt.grid(True)

plt.tight_layout()
plt.show()