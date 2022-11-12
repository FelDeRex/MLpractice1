import numpy as np

arr = np.random.randint(0, 10, 30)
print(arr)
print('Наиболее частое значение:', np.bincount(arr).argmax())
print('Частота этого значения:', np.bincount(arr).max())