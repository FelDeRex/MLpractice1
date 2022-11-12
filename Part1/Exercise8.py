def more_than_ten(lst):
    moreThanTenList = []
    for i in range(len(lst)):
        if abs(lst[i]) > 10:
            moreThanTenList.append(lst[i])
    return moreThanTenList

x = [10, 2, 40, -60, 4, -5, 60, 50]
print(more_than_ten(x))
