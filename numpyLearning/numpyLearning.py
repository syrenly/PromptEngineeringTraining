# numpy =  numerical python library
# numpy array = collection of numbers stored in a grid-like structure. It supports multi-dimensional data

import numpy as nu

# create array
arr = nu.array([1, 2, 3, 4, 5])
print(arr)  # [1 2 3 4 5]

# create a list; see the difference
list_data = [1, 2, 3]
print(list_data)  # [1, 2, 3]

# array shape and dimensions

matrix = nu.array([[1, 2], [3, 4]])  # matrix 2x2
print(matrix)
# [[1 2]
#  [3 4]]
print(matrix.shape)  # (2, 2)

# SCALAR BROADCASTING
print(
    arr + 2
)  # creates a new array [2 2 2 2 2] which is summed to the first one => [3 4 5 6 7]; this is called SCALAR BROADCASTING+VECTORIZATION

# BROADCASTING; only array with same dimensions
a = nu.array([1, 2])
b = nu.array([3, 4])
print(a + b)  # [4 6]

# Broadcasting rules
# 1. compare shape from left to right
A = nu.array([1, 2])  # => (1,2)
B = nu.array(
    [
        1,
    ]
)  # => (  1)

# 2. dimensions must match or be 1
A = nu.array([1, 2])
B = nu.array([1, 2, 3])
C = nu.array([3, 4])

print(A + 2)  # ok
print(A + C)  # ok

try:
    print(
        B + C
    )  # ko => ValueError: operands could not be broadcast together with shapes (3,) (2,)
except ValueError:
    print("ValueError: operands could not be broadcast together with shapes (3,) (2,)")

# NORMALIZATION = to scale values to a range of more handy values; so numbers are more understandable and being smaller require less resources

imagePixels = nu.array([200, 120, 150])
normalizedPixels = imagePixels / 255  # 255 max value for a pixel

print(normalizedPixels)
