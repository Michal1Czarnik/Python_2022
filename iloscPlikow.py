#!/usr/bin/python3

import os

numer = str(len(os.listdir('/dev')))
print("W katalogu /dev jest: " + numer + " plikow.")