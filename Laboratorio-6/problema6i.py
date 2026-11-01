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

# i) x(t)[u(t+1)-delta(t-0.5)]
# Parte continua: x(t)u(t+1)
u = np.where(t >= -1, 1.0, 0.0)
y = x(t)*u

fig, ax = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("INCISO I: x(t)[u(t+1)-δ(t-0.5)]",
             fontsize=16, fontweight="bold")

for g in ax:
    g.plot(t, y, color="blue", linewidth=2.5,
           label="Parte continua: x(t)u(t+1)")
    g.set_xlabel("Tiempo (t)", fontsize=12)
    g.set_ylabel("Amplitud / peso del impulso", fontsize=11)
    g.grid(True, linestyle="--", alpha=0.6)
    g.axhline(0, color="black", linewidth=1)
    g.axvline(0, color="black", linewidth=1)
    g.tick_params(labelsize=10)
    # Impulso negativo: -x(0.5)delta(t-0.5) = -0.5delta(t-0.5)
    g.annotate(
        "",
        xy=(0.5, -0.5),
        xytext=(0.5, 0),
        arrowprops=dict(arrowstyle="-|>", color="red", linewidth=2.2)
    )
    g.text(0.5, -0.68, "-0.5", color="red",
           ha="center", va="center", fontsize=10)

ax[0].set_title("Intervalo completo: -13 < t < 13")
ax[0].set_xlim(-13, 13)
ax[0].set_ylim(-1.0, 1.5)

ax[1].set_title("Acercamiento de la señal")
ax[1].set_xlim(-1.5, 1.5)
ax[1].set_ylim(-1.0, 1.5)

ax[0].legend(loc="upper right")
plt.tight_layout()
plt.show()
