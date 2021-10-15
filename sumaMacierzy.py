#!/opt/anaconda3/bin/python

import numpy as np
import random

def matrixGenerator():
    matrix = np.zeros((128, 128))
    for i in range(0, 128):
        matrix[i,:] = np.array([random.randint(1, 100000) for i in range (0, 128)])
    return matrix

matrix1 = matrixGenerator()
matrix2 = matrixGenerator()

sum = np.zeros((128, 128))
for i in range(0, 128):
    for j in range(0, 128):
        sum[i, j] = matrix1[i, j] + matrix2[i, j]

print(sum)

