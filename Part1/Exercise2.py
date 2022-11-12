def season(month):
    global s
    if ((month >= 1) & (month <= 2)) | (month == 12):
        s = 'Зима'
    elif (month >= 3) & (month <= 5):
        s = 'Весна'
    elif (month >= 6) & (month <= 8):
        s = 'Лето'
    elif (month >= 9) & (month <= 11):
        s = 'Осень'

season(4)
print(s)