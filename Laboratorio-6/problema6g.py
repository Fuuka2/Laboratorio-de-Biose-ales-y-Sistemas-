import matplotlib.pyplot as plt


def dibujar_impulso(ax, posicion, peso, etiqueta=None):
    """Dibuja una flecha para representar un impulso de Dirac.
    La altura visual es proporcional al peso; no es una altura física finita.
    """
    ax.annotate(
        "",
        xy=(posicion, peso),
        xytext=(posicion, 0),
        arrowprops=dict(arrowstyle="-|>", color="red", linewidth=2.2)
    )
    if etiqueta is not None:
        desplazamiento = 0.12 if peso >= 0 else -0.18
        ax.text(posicion, peso + desplazamiento, etiqueta,
                color="red", ha="center", va="center", fontsize=10)

def preparar_impulsos(titulo, impulsos, zoom, ylim=(-0.5, 1.5)):
    fig, ax = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle(titulo, fontsize=16, fontweight="bold")

    for g in ax:
        g.set_xlabel("Tiempo (t)", fontsize=12)
        g.set_ylabel("Peso del impulso (representación)", fontsize=11)
        g.grid(True, linestyle="--", alpha=0.6)
        g.axhline(0, color="black", linewidth=1)
        g.axvline(0, color="black", linewidth=1)
        g.set_ylim(*ylim)
        g.tick_params(labelsize=10)

    ax[0].set_title("Intervalo completo: -13 < t < 13")
    ax[0].set_xlim(-13, 13)
    ax[1].set_title("Acercamiento de la señal")
    ax[1].set_xlim(*zoom)

    for posicion, peso, etiqueta in impulsos:
        for g in ax:
            dibujar_impulso(g, posicion, peso, etiqueta)

    plt.tight_layout()
    plt.show()

# g) x(t)delta(t-0.5) = x(0.5)delta(t-0.5)
# Como x(0.5)=0.5, el impulso tiene peso 0.5.
impulsos = [(0.5, 0.5, "0.5")]
preparar_impulsos("INCISO G: x(t)δ(t-0.5)", impulsos, zoom=(-1, 2))
