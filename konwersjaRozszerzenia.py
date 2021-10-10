#!/usr/bin/python3

import os

file1 = 'file1.jpg'
file2 = 'file2.jpg'
file3 = 'file3.jpg'
file4 = 'file4.jpg'

directoryBCr = os.listdir(os.getcwd())
print('List of file befere creation: ')
print(directoryBCr)

for file in [file1, file2, file3, file4]:
    with open(os.path.join(os.getcwd(), file), 'w') as fp:
        pass

directoryACr = os.listdir(os.getcwd())
print('List of file after creation: ')
print(directoryACr)

for i in range(0,len(directoryACr)):
    if(directoryACr[i].find('.jpg') != -1):
        os.rename(directoryACr[i], directoryACr[i][0:directoryACr[i].find('.jpg')] + '.png')

directoryACh = os.listdir(os.getcwd())
print('List of file after changes: ')
print(directoryACh)