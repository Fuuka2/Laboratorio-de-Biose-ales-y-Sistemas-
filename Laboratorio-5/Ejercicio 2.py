import sympy as sp

t, s = sp.symbols('t s', positive=True)

F1 = sp.integrate(2 * sp.exp(-s*t), (t, 2, 4))
F2 = sp.integrate(t * sp.exp(-s*t), (t, 0, 2))
F3 = (
    sp.integrate(t**2 / 2 * sp.exp(-s*t), (t, 0, 2))
    + sp.integrate(2 * sp.exp(-s*t), (t, 2, sp.oo))
)

for i, F in enumerate([F1, F2, F3], start=1):
    resultado = sp.factor(F)
    print(f"Grafica {i}:")
    print(sp.latex(resultado))
    print()
