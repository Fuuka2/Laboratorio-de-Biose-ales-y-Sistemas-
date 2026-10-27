import numpy as np

def rest(vector):
    vector1 = np.array(vector)
    r = vector1[0] - np.sum(vector1[1:])
    return r

v1 = [8, 3, 2, 1]
v2 = rest(v1)

print("Vector de entrada:", v1)
print("Resultado de la resta:", v2)

