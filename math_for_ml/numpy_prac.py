#Learning numpy from keith galli
#import numpy as np
"""
#Robot position vector:
position = np.array([0, 0, 0])
#                   x, y, z

print(position.ndim)
print(position.shape)
print(position.dtype)
print(position.itemsize)
print(position.nbytes)
print(position.size)
"""

#position = np.array([1, 2, 3])
#                    x, y, z
"""
#Get specifically x, y coordinate from the array
x = position[0]
z = position[2]

print(f"(x, y) = {x, z}")

#Get specific row or get all of x, y, z coordinate
pose = position[:]
print(pose)

#Get specifically middle or set of data in the middle  [startindex:endindex:stepsize] (excludes endindex)
y = position[1:2:1]
print(y)
"""
"""
#Change specific coordinate like x or y or z
position[1] = 4
x = position[1]
print(x)
"""
"""
angle = np.radians(90)
rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle), np.cos(angle)]
])


print(np.round(rotation))
"""

"""
#Creating matrix using arrays

print(np.zeros((2,3)))
print(np.ones((2,2)))

print(np.full((2,2), 99))

print(np.random.rand(4,2))
print(np.random.randint(-2, 7, size=(3,3)))

print(np.identity(5))

rep = np.array([[3,2,1]])
r1 = np.repeat(rep, 3, axis = 0)
print(r1)
"""
"""
Create a matrix:
    1 1 1 1 1
    1 0 0 0 1
    1 0 9 0 1
    1 0 0 0 1
    1 1 1 1 1
"""
"""
import numpy as np

mat = np.ones((5,5))

zeros = np.mat[0, (:1:)]
print(zeros)
"""
"""
#copying arrays
a = np.array([1,2,3])
b = a.copy()
b[0] = 100
print(b)
"""
#Mathematics
#simple
"""
#Linear algebra
import numpy as np

a = np.ones((2,3))

b = np.full((3,2), 2)

print(np.matmul(a,b))

#Determinant
c = np.identity(3)
print(np.linalg.det(c))

#statistics
stats = np.array([[1,2,3],[4,5,6]])

print(np.min(stats, axis = 1))

print(np.max(stats))
print(np.sum(stats, axis = 0))
"""
#Reorganizing Arrays
import numpy as np
"""
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

after = before.reshape((2,3))
print(after)
"""
"""
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

print(np.vstack([v1,v2]))  #Vertical stack

h1 = np.ones((2,4))
h2 = np.zeros((2,2))

print(np.hstack([h1, h2]))  #Horizontal stack
"""
"""
#Load data from file
filedata = np.genfromtxt("_.txt", delimiter=",")
filedata = filedata.astype("int32")
print(filedata)

#Boolean Masking and Advanced Indexing
file data > 50
filedata[filedata > 50]
np.any(filedata > 50, axis = 0)
np.all(filedata >50, axis = 0)
(~(filedata > 50 & filedata < 100))
"""
