#Faça um sistema que pegue todos os valores maiores que 10 de uma matriz 10x10

import numpy as np

matriz = np.random.randint(0, 20, (3, 3))
print(matriz)

for i in range(2):
    for j in range(2):
        if matriz[i][j] > 10:
            print(matriz[i][j])
        
