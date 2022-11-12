import numpy as np

def ReverseNumberIfBetween3and8(arr):
    for i in range(0, len(arr)):
        if (arr[i] >= 3) & (arr[i] <= 8):
            arr[i] *= -1

arr = np.random.randint(0, 10, 10)
print(arr)

ReverseNumberIfBetween3and8(arr)
print(arr)