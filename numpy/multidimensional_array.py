import numpy as np

array = np.array('A')   # [1, 2, 3] -> 1D, [[1, 2, 3], [4, 5, 6], [7, 8, 9]] -> 2D
print(array.ndim)   # 0 -> ndim gives us the dimension number 

array2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(array2.shape) # (3, 3) -> 3 * 3 matrix

array3 = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                   [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                   [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])

print(array3[0, 0, 0])  # A -> layer 0, row 0, column 0

word = array3[0, 0, 0] + array3[2, 0, 0] + array3[2, 0, 0]

print(word) # ASS