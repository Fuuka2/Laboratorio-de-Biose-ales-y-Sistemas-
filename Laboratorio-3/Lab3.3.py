import numpy as np

def cuadrado(vector):
    vector1 = np.array(vector)
    resultado = vector1 ** 2
    return resultado

v1 = [1, 2, 3, 4, 5]
v2 = cuadrado(v1)


print("Vector de entrada:", v1) 
print("Vector resultante:", v2)
