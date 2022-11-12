import numpy as np

matrix = np.random.randint(10, size=(3, 3))
print(matrix)

lineMiddle = matrix.mean(axis=1)
print(matrix - lineMiddle)