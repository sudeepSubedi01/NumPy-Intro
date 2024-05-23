import numpy as np
#----Copyping Array-------------------------------
a = np.array([1,2,3])
# b=a
b = a.copy()
b[0] = 66
print(a)
print(b)
#----Array Mathematics-------------------------------
print(a-2)
print(a*2)
print(a**2)
print(np.sin(a))
c = np.array([1,0,1])
print(a * c)
print(a ** c)

#----Linear Algebra-------------------------------
d = np.ones((2,3), dtype = 'int16')
e = np.full((3,2),2, dtype='int16')
print(np.matmul(d,e))

#----Determinant-------------------------------
f = np.identity(3)
print(np.linalg.det(f))

#----Matrix Statistics-------------------------------
g = np.array([[1,2,3],[4,5,6]])
print(np.min(g,axis=0))
print(np.sum(g))
print(np.sum(g,axis=0))

#----Reorganizing Arrays-------------------------------
before = np.array([[1,2,3,4],[5,6,7,8]])
after = before.reshape((8,1))
print(after)

#----Vertically Stacking Arrays-------------------------------
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print(np.vstack([v1,v2,v2,v1]))

#----Horizontally Stacking Arrays-------------------------------
h1 = np.array([1,2,3,4])
h2 = np.array([5,6,7,8])
print(np.hstack([h1,h2,h2,h1]))
