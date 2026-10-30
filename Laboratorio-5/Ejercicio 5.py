import sympy as sp

t = sp.symbols('t', real=True)

A = sp.Matrix([
    [-1, -5],
    [ 1, -3]
])

Y0 = sp.Matrix([2, 5])

Y = sp.simplify(sp.exp(A*t) * Y0)

y1 = sp.trigsimp(sp.simplify(sp.expand_complex(Y[0])))
y2 = sp.trigsimp(sp.simplify(sp.expand_complex(Y[1])))

print("y1(t) en LaTeX:")
print(sp.latex(sp.Eq(sp.Function('y1')(t), y1)))
print()

print("y2(t) en LaTeX:")
print(sp.latex(sp.Eq(sp.Function('y2')(t), y2)))
