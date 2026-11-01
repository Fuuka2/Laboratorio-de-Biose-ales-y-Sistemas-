import numpy as np

# 5. Programa que realiza la suma de un vector de 'n' posiciones
def sumar_vector_n(vec):
    total = 0
    for elemento in vec:
        total += elemento
    return total

#vector de prueba
mi_vector = np.array([10, 20, 30, 40, 50])
print(f"Ejercicio 5:\nSuma de {mi_vector} es = {sumar_vector_n(mi_vector)}")