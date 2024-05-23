import numpy as np

a = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(a.shape)
print()
print(np.zeros(5))
print(np.zeros((2,3)))
print(np.ones((2,3,4), dtype= 'int16'))
print(np.full((2,3), 56, dtype='int16'))
print(np.full_like(a.shape,4))
print(np.random.rand(4,2,2))
print(np.random.randint(4,7,size=(3,3)))
print(np.identity(5,dtype='int16'))

arr = np.array([[1,2,3]])
print(np.repeat(arr,3,axis=0))


outputMatrix = np.ones((5,5), dtype='int16')
zeroMatrix = np.zeros((3,3), dtype='int16')
zeroMatrix[1,1] = 9
# print(zeroMatrix)
outputMatrix[1:4,1:4] = zeroMatrix
print(outputMatrix)