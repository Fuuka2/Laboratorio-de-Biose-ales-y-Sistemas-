import sympy as sp

t, s = sp.symbols('t s', real=True)

funciones_s = [
    (s + 3) / (s**2 + 7*s + 10),
    (2*s - 4) / (s*(s + 1)*(s + 2)),
    1 / ((s - 5)**2 * (s + 7)),
    (s + 2) / (s**2 + 9),
    1 / ((s**2 + 4)*(s**2 + 9)),
    2 / (s**2 + 4)**2
]

for i, F in enumerate(funciones_s, start=1):
    f = sp.inverse_laplace_transform(F, s, t)
    f = sp.simplify(f)

    print(f"Ejercicio {i}:")
    print("f(t) en LaTeX:")
    print(sp.latex(f))
    print("\n")
