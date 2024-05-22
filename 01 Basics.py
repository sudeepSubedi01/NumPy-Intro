import numpy as np

a = np.array([1,2,3,5,9],dtype='int16')
print(a)
print(a.ndim)
print(a.shape)
print(a.dtype)
print(a.itemsize)

print()
print()
b = np.array([[1.0,5.6,6.5],[4.1,6,9]])
print(b)
print(b.ndim)
print(b.shape)
print(b.dtype)
print(b.itemsize)