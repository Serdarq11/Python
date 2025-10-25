import numpy as np

# Scalar Arithmetic

array = np.array([1, 2, 3])

print(array + 1)    # [2 3 4]
print(array - 2)    # [-1  0  1]
print(array * 3)    # [3 6 9]
print(array / 4)    # [0.25 0.5  0.75]
print(array ** 5)   # [ 1  32 243]

# Vectorized Math Functions

print(np.sqrt(array))   # [1.         1.41421356 1.73205081]

arr = np.array([1.01, 2.5, 3.99])
print(np.round(arr)) # [1. 2. 4.]
print(np.floor(arr)) # [1. 2. 3.]
print(np.ceil(arr))  # [2. 3. 4.]

# EXERCISE

radii = np.array([1, 2, 3])
print(np.pi * radii ** 2)   # [ 3.14159265 12.56637061 28.27433388]

# Element Wise Arithmetic

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + array2)  # [5 7 9]
print(array1 - array2)  # [-3 -3 -3]
print(array1 * array2)  # [ 4 10 18]
print(array1 / array2)  # [0.25 0.4  0.5 ]
print(array1 ** array2) # [  1  32 729]

# Comparison Operators

scores = np.array([91, 55, 100, 73, 82, 64])

print(scores == 100)    # [False False  True False False False] -> boolean array
print(scores >= 60)     # [ True False  True  True  True  True]

scores[scores < 60] = 0
print(scores)   # [ 91   0 100  73  82  64]