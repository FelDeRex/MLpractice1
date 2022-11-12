import numpy as np

vector = np.arange(1, 6)
zerosCount = 3
vectorWithZeros = np.zeros(len(vector) + (len(vector) - 1) * zerosCount)
vectorWithZeros[::zerosCount+1] = vector
print(vectorWithZeros)
