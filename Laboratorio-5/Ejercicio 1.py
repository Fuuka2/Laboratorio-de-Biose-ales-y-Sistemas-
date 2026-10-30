import sympy as sp

t, s = sp.symbols('t s', real=True)

funciones = {
    "x1(t) = e^(3t) cos(2t)": sp.exp(3*t) * sp.cos(2*t),
    "x2(t) = e^(3t) sen(2t)": sp.exp(3*t) * sp.sin(2*t),
    "x3(t) = t sen(2t)": t * sp.sin(2*t),
    "x4(t) = t cos(2t)": t * sp.cos(2*t),
    "x5(t) = e^t + e^(-t)": sp.exp(t) + sp.exp(-t)
}

for nombre, funcion in funciones.items():
    resultado = sp.laplace_transform(funcion, t, s, noconds=True)
    resultado = sp.factor(resultado)

    print(nombre)
    print("F(s) en LaTeX:")
    print(sp.latex(resultado))
    print("\n")
