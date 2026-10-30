import sympy as sp

t = sp.symbols('t', real=True)
y = sp.Function('y')

eq1 = sp.Eq(
    sp.diff(y(t), t, 2) + 7*sp.diff(y(t), t)
    + 10*y(t), 0
)

sol1 = sp.dsolve(
    eq1, y(t),
    ics={y(0): 7, sp.diff(y(t), t).subs(t, 0): -26}
)

eq2 = sp.Eq(
    sp.diff(y(t), t, 2) + 5*sp.diff(y(t), t)
    + 6*y(t), 2*sp.exp(-t)
)

sol2 = sp.dsolve(
    eq2, y(t),
    ics={y(0): 1, sp.diff(y(t), t).subs(t, 0): 0}
)

eq3 = sp.Eq(
    sp.diff(y(t), t, 2) + 2*sp.diff(y(t), t)
    + 2*y(t), sp.exp(-t)*sp.sin(t)
)

sol3 = sp.dsolve(
    eq3, y(t),
    ics={y(0): 1, sp.diff(y(t), t).subs(t, 0): 1}
)

eq4 = sp.Eq(
    sp.diff(y(t), t, 3)
    + 3*sp.diff(y(t), t, 2)
    + 2*sp.diff(y(t), t)
    - 6*y(t),
    sp.exp(-2*t)
)

sol4 = sp.dsolve(
    eq4, y(t),
    ics={
        y(0): 0,
        sp.diff(y(t), t).subs(t, 0): 0,
        sp.diff(y(t), t, 2).subs(t, 0): 0
    }
)

for i, sol in enumerate([sol1, sol2, sol3, sol4], start=1):
    print(f"Ecuacion {i}:")
    print(sp.latex(sol))
    print()
