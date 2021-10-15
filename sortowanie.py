#!/usr/bin/python3

import random

numbers = [random.randint(1, 10000000) for i in range (0, 50)]
sort_num = []
for i in range(50):
    temp = max(numbers)
    sort_num.append(temp)
    numbers.remove(temp)
print(sort_num)