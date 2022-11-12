import numpy as np

matrix = np.random.randint(10, size=(5, 3))
print(matrix)
matrix[[0, 1]] = matrix[[1, 0]]
print(matrix)