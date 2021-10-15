#!/opt/anaconda3/bin/python

import numpy as np

a = np.array([1, 2, 12, 4])
b = np.array([2, 4, 2, 8])
result = 0
for i in range(0, len(a)):
    result = result + (a[i] * b[i])
print(result)
