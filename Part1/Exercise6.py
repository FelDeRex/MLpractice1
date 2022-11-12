x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
reversedByOddIndexX = x[::-2]
print(reversedByOddIndexX)
j = 0
for i in range(1, len(x), 2):
    x[i] = reversedByOddIndexX[j]
    j += 1
print(x)