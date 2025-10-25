import numpy as np

#print(np.__version__)

array = np.array([1, 2, 3, 4])
array = array * 2

print(array)    # [2 4 6 8]
print(type(array))  # <class 'numpy.ndarray'>

list = [1, 2, 3, 4]

print(list * 2) # [1, 2, 3, 4, 1, 2, 3, 4]

# the difference between np array and list is that we can duplicate the list by multiplying the list by 2; 
# however, when we multiply an np array, we multiply every single element by 2