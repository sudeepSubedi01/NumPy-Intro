import numpy as np

# fileData = np.loadtxt('data.txt',delimiter=' ', dtype='int16')
# print(fileData)

fileData = np.genfromtxt('data.txt', delimiter=' ', dtype=None, encoding=None)
print(fileData)