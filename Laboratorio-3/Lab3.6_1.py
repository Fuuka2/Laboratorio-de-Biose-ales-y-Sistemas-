import numpy as np
import matplotlib.pyplot as plt

# Definición del eje temporal
dt = 0.01
t = np.arange(-10, 10, dt)

# Definición de la señal triangular x1(t)
x1 = np.where((t > -2) & (t < 2), 1 - np.abs(t) / 2.0, 0.0)

# Cálculo de la convolución y1(t)
y1 = np.convolve(x1, x1, mode='full') * dt
t_y = np.linspace(t[0] + t[0], t[-1] + t[-1], len(y1))

# Gráficas
plt.figure(figsize=(8, 8))

plt.subplot(2, 1, 1)
plt.plot(t, x1, 'b-', linewidth=2)
plt.title(r'Señal de entrada $x_1(t)$') 
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t_y, y1, 'r-', linewidth=2)
plt.title(r'Convolución $y_1(t)=x_1(t)*x_1(t)$') 
plt.xlabel(r'Tiempo ($t$)')
plt.grid(True)

plt.tight_layout()
plt.show()