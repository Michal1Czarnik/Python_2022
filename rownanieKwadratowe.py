#!/usr/bin/python3
import math
import sys

print('Podaj wartosc a: ')
a = float(input())
print('\nPodaj wartosc b: ')
b = float(input())
print('\nPodaj wartosc c: ')
c = float(input())

if (a == 0):
    print('\nTo nie jest rowanie kwadratowe tylko liniowe')
    sys.exit()

delta = (pow(b, 2) - (4 * a * c))
if (delta > 0):
    x1 = (- b - math.sqrt(delta)) / (2 * a)
    x2 = (- b + math.sqrt(delta)) / (2 * a)
    print('\nx1 = ' + str(x1))
    print('\nx2 = ' + str(x2))
elif (delta == 0):
    x0 = (- b / (2 * a))
    print('\nx0 = ' + str(x0))
else:
    print("\nNie ma miejsc zerowych")
