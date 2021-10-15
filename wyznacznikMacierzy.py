#!/opt/anaconda3/bin/python

import numpy as np
import sys
import random

def matrixGenerator(x):
    matrix = np.zeros((x, x))
    for i in range(0, x):
        matrix[i,:] = np.array([random.randint(1, 100) for i in range (0, x)])
    return matrix

print('Podaj ilosc wierszy: ')
row = int(input())
print('Podaj ilosc kolumn')
column = int(input())
if (row == column):
    matrix = matrixGenerator(int(row))
    print('\nTwoja peudolosowa macierz: ')
    print(matrix)
    print('\n')
    matrixDeterminant = np.linalg.det(matrix)
    print(matrixDeterminant)
else:
    print('\nWyznacznik mozna obliczac tylko dla macierzy kwadratowej!')
    sys.exit()