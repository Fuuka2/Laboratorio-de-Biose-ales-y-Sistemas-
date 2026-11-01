import numpy as np
import matplotlib.pyplot as plt

def x(t):
    """Señal original definida por tramos."""
    return np.select(
        [
            (t >= -2) & (t < -1),
            (t >= -1) & (t <= 0),
            (t > 0) & (t <= 1)
        ],
        [t + 1, 1, 1 - t],
        default=0.0
    )

def preparar_graficas(titulo, y, zoom, ylim=(-1.5, 1.5)):
    fig, ax = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle(titulo, fontsize=16, fontweight="bold")

    # Vista del intervalo solicitado
    ax[0].plot(t, y, color="blue", linewidth=2.5)
    ax[0].set_title("Intervalo completo: -13 < t < 13")
    ax[0].set_xlim(-13, 13)
    ax[0].set_ylim(*ylim)

    # Vista ampliada para apreciar la forma de onda
    ax[1].plot(t, y, color="blue", linewidth=2.5)
    ax[1].set_title("Acercamiento de la señal")
    ax[1].set_xlim(*zoom)
    ax[1].set_ylim(*ylim)

    for g in ax:
        g.set_xlabel("Tiempo (t)", fontsize=12)
        g.set_ylabel("Amplitud", fontsize=12)
        g.grid(True, linestyle="--", alpha=0.6)
        g.axhline(0, color="black", linewidth=1)
        g.axvline(0, color="black", linewidth=1)
        g.tick_params(labelsize=10)

    plt.tight_layout()
    plt.show()

# Malla de tiempo para representar las señales
t = np.linspace(-13, 13, 20001)

# d) x(4-t/2)
y = x(4 - t/2)
preparar_graficas("INCISO D: x(4-t/2)", y, zoom=(5.5, 12.5))
