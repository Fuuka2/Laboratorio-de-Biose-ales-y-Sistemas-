import numpy as np
def sumar(vector):
    vec_np = np.array(vector)
    resultado = vec_np + 1.75
    return resultado

v1 = [1, 2, 3, 4, 5]
v2 = sumar(v1)

print("Vector de entrada:", v1)
print("Vector resultante:", v2)
