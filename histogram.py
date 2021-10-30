#!/opt/anaconda3/bin/python

import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(size=1000)

plt.hist(x, density=True, bins=30) 
plt.ylabel('Prawdopodobieństwo')
plt.xlabel('Dane')
plt.show()