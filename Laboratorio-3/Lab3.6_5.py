import numpy as np
import matplotlib.pyplot as plt

# Definición del eje temporal
dt = 0.01
t = np.arange(-15, 15, dt)

# Definición de las señales base x3(t) y x4(t)
x3 = np.zeros_like(t)
x3[np.argmin(np.abs(t - 5))] = 1.0 / dt  

x4 = np.where((t > -6) & (t < 6), np.sinc(t / 2.0), 0.0)

# Cálculo de la convolución y5(t)
y5 = np.convolve(x3, x4, mode='full') * dt
t_y = np.linspace(t[0] + t[0], t[-1] + t[-1], len(y5))

# Gráficas
plt.figure(figsize=(8, 10))

plt.subplot(3, 1, 1)
plt.plot(t, x3, 'b-', linewidth=2)
plt.title(r'Señal de entrada $x_3(t)$')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, x4, 'g-', linewidth=2)
plt.title(r'Señal de entrada $x_4(t)$')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t_y, y5, 'r-', linewidth=2)
plt.title(r'Convolución $y_5(t) = x_3(t) * x_4(t)$')
plt.xlabel(r'Tiempo ($t$)')
plt.grid(True)

plt.tight_layout()
plt.show()