from math import sqrt, pow

x1 = 2;
y1 = 5;
x2 = 5;
y2 = 10;

def distance(x1, y1, x2, y2):
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))


print(distance(x1, y1, x2, y2))