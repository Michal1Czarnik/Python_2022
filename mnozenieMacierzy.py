#!/opt/anaconda3/bin/python

import numpy as np
import random

def matrixGenerator():
    matrix = np.zeros((8, 8))
    for i in range(0, 8):
        matrix[i,:] = np.array([random.randint(1, 100) for i in range (0, 8)])
    return matrix

matrix1 = matrixGenerator()
matrix2 = matrixGenerator()

multi = np.zeros((8, 8))
for i in range(0, 8):
    for j in range(0, 8):
        matrixElement = 0
        for k in range(0, 8):
            matrixElement = matrixElement + (matrix1[i][k] * matrix2[j][k])
            multi[i][j] = matrixElement
print(multi)
