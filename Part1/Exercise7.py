def IsThereEight(number):
    while number > 0:
        if number % 10 == 8:
            return True
        number //= 10
    return False


for number in range(0, 500, 7):
    if IsThereEight(number):
        print(number)
