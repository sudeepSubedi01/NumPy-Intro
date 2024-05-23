import numpy as np

# fileData = np.loadtxt('data.txt',delimiter=' ', dtype='int16')
# print(fileData)

fileData = np.genfromtxt('data.txt', delimiter=' ', dtype=None, encoding=None)
print(fileData)

print(fileData>50)
print(fileData[fileData>50])
print(np.any(fileData>50, axis=0))

a = np.array([2,3,4,5,6,7,8,9])
print(a[[2,3,4]])