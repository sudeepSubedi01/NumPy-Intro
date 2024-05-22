import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

print(a[1,3])
print(a[0,:])
print(a[:,5])
print(a[0,1:6])
print(a[0,1:6:3])
print(a[0,1:-1:2])
a[1,5] = 0
a[0, : ] = 1
print(a)


b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b[0,1,1])
print(b)