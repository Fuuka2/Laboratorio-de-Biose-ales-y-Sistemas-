import sympy as sp

t, s = sp.symbols('t s', real=True, positive=True)

H = 2*s / (s + 3)

u = sp.Heaviside(t)

h = 2*sp.DiracDelta(t) - 6*sp.exp(-3*t)*u

print("1. Respuesta impulsiva:")
sp.pprint(h)

X1 = 3 / (s + 2)
Y1 = sp.apart(X1 * H, s)
y1 = sp.inverse_laplace_transform(Y1, s, t)

print("\n2.1 Salida:")
sp.pprint(y1)

X2 = 6 / s**4
Y2 = sp.apart(X2 * H, s)
y2 = sp.inverse_laplace_transform(Y2, s, t)

print("\n2.2 Salida:")
sp.pprint(y2)

X3 = 3 / (s + 3)
Y3 = sp.apart(X3 * H, s)
y3 = sp.inverse_laplace_transform(Y3, s, t)

print("\n2.3 Salida:")
sp.pprint(y3)
