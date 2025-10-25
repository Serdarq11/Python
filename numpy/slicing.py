import numpy as np

array = np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8], 
                  [9, 10, 11, 12], 
                  [13, 14, 15, 16]])

# array[start:end:step]

# 1st row
print(array[0])

# first 3 row
print(array[0:3])

# give me every second row starting with first row
print(array[0:4:2]) #or array[::2]

# all the rows reversed
print(array[::-1])

# column 0
print(array[ : , 0 ])   # [ 1  5  9 13]

# column 2
print(array[ : , 1 ])   # [ 2  6 10 14]

# first 3 columns
print(array[ : , 0 : 3])

# every second column
print(array[ : , :: 2])

# reversed columns
print(array[ : , :: -1])

# first 2 rows and first 2 columns
print(array[ : 2, : 2])


