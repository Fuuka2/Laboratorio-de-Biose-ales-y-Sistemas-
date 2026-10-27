import numpy as np
import matplotlib.pyplot as plt

# Definición del eje temporal
dt = 0.01
t = np.arange(-10, 10, dt)

# Definición del pulso rectangular x2(t)
x2 = np.where((t >= -1) & (t <= 1), 1.0, 0.0)

# Cálculo de la convolución y3(t)
y3 = np.convolve(x2, x2, mode='full') * dt
t_y = np.linspace(t[0] + t[0], t[-1] + t[-1], len(y3))

# Gráficas
plt.figure(figsize=(8, 7))

plt.subplot(2, 1, 1)
plt.plot(t, x2, 'b-', linewidth=2)
plt.title(r'Señal de entrada $x_2(t)$')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t_y, y3, 'r-', linewidth=2)
plt.title(r'Convolución $y_3(t) = x_2(t) * x_2(t)$')
plt.xlabel(r'Tiempo ($t$)')
plt.grid(True)

plt.tight_layout()
plt.show()