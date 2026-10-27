import numpy as np
import matplotlib.pyplot as plt

def pares(vector):
   
    vo = np.array(vector, dtype=int)
    vm = vo.copy()
   
    # Elevar al cuadrado
    vm[::2] = vm[::2] ** 2
   
    #Gráfica
    plt.figure(figsize=(8, 4))
   
    plt.stem(vo, linefmt='b-', markerfmt='bo', basefmt='r-', label='Vector Original')
   
    plt.stem(vm, linefmt='g--', markerfmt='go', basefmt='r-', label='Pares al Cuadrado')
   
    plt.title("Ejercicio 5: Modificación de Posiciones Pares")
    plt.xlabel("Índice (i)")
    plt.ylabel("Valor")
    plt.grid(True)
    plt.legend()
    plt.show()
   
    return vm

# Ejemplo
v1 = [2, 3, 4, 5, 6]
v2 = pares(v1)

print("Vector de entrada:  ", v1)
print("Vector modificado:  ", v2.tolist())