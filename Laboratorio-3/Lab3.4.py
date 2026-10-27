import numpy as np

def semicuadrado(vector):
    vector1 = np.array(vector)
    resultado = np.sum(vector1 ** 2) / 2.0
    return resultado

v1 = [1, 2, 3, 4]
v2 = semicuadrado(v1)

print("Vector de entrada:", v1) 
print("Semisuma de cuadrados:", v2)