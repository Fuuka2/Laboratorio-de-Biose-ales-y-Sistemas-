import numpy as np
import matplotlib.pyplot as plt

# Definición de X(t) - Figura 2 (Izquierda): Rampa continua de 0 a 5 de altura 4
t_cont = np.linspace(-7, 7, 2000)

def X_func(t_arr):
    y = np.zeros_like(t_arr, dtype=float)
    cond = (t_arr >= 0) & (t_arr <= 5)
    y[cond] = (4.0 / 5.0) * t_arr[cond]
    return y

X_t = X_func(t_cont)
X_minus_t = X_func(-t_cont)

X_par = 0.5 * (X_t + X_minus_t)
X_impar = 0.5 * (X_t - X_minus_t)

# Definición de y(n) - Figura 2 (Derecha): Señal discreta
# Impulsos en n=1 (amplitud 2), n=2 (amplitud 4), n=3 (amplitud 2)
n = np.arange(-6, 7)

def y_func(n_arr):
    y = np.zeros_like(n_arr, dtype=float)
    y[n_arr == 1] = 2.0
    y[n_arr == 2] = 4.0
    y[n_arr == 3] = 2.0
    return y

y_n = y_func(n)
y_minus_n = y_func(-n)

y_par = 0.5 * (y_n + y_minus_n)
y_impar = 0.5 * (y_n - y_minus_n)

# Gráficas
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Componentes de X(t)
axes[0, 0].plot(t_cont, X_par, 'g-', linewidth=2)
axes[0, 0].set_title('Componente Par: $X_{par}(t)$')
axes[0, 0].grid(True)

axes[0, 1].plot(t_cont, X_impar, 'm-', linewidth=2)
axes[0, 1].set_title('Componente Impar: $X_{impar}(t)$')
axes[0, 1].grid(True)

# Componentes de y(n)
axes[1, 0].stem(n, y_par, linefmt='g-', markerfmt='go', basefmt=" ")
axes[1, 0].set_title('Componente Par: $y_{par}(n)$')
axes[1, 0].grid(True)

axes[1, 1].stem(n, y_impar, linefmt='m-', markerfmt='mo', basefmt=" ")
axes[1, 1].set_title('Componente Impar: $y_{impar}(n)$')
axes[1, 1].grid(True)

for ax in axes.flat:
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)

plt.tight_layout()
plt.show()