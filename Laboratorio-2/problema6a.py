
import numpy as np
import matplotlib.pyplot as plt

# Señal original
def x(t):
    return np.select(
        [
            (t >= -2) & (t < -1),
            (t >= -1) & (t <= 0),
            (t > 0) & (t <= 1)
        ],
        [
            t + 1,
            1,
            1 - t
        ],
        default=0
    )

# Intervalo de tiempo
t = np.linspace(-13, 13, 10000)

# Transformación
y = x(t - 1)

# Crear dos gráficas
fig, ax = plt.subplots(1, 2, figsize=(15, 5))

fig.suptitle('INCISO A: x(t-1)', fontsize=16, fontweight='bold')

# GRÁFICA 1: Intervalo completo
ax[0].plot(t, y, color='blue', linewidth=2.5)
ax[0].set_title('Intervalo completo (-13 a 13)')
ax[0].set_xlim(-13, 13)
ax[0].set_ylim(-1.5, 1.5)

# GRÁFICA 2: Acercamiento
ax[1].plot(t, y, color='blue', linewidth=2.5)
ax[1].set_title('Acercamiento de la señal')
ax[1].set_xlim(-1.5, 2.5)
ax[1].set_ylim(-1.5, 1.5)

# Configuración de ambos gráficos
for grafica in ax:
    grafica.set_xlabel('Tiempo (t)', fontsize=12)
    grafica.set_ylabel('Amplitud', fontsize=12)
    grafica.grid(True, linestyle='--', alpha=0.6)
    grafica.axhline(0, color='black', linewidth=1)
    grafica.axvline(0, color='black', linewidth=1)
    grafica.tick_params(labelsize=10)

plt.tight_layout()
plt.show()
