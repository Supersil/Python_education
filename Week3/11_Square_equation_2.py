from math import sqrt

a, b, c = float(input()), float(input()), float(input())

if a == 0 and b == 0 and c == 0:
    print(3)
    exit()

if (a == 0 and b != 0):
    print(1, -c / b, sep=' ')
    exit()
elif a == 0:
    print(0)
    exit()

d = b * b - 4 * a * c
if (d < 0):
    print(0)
    exit()

if (d == 0):
    x = (-b) / (2 * a)
    print(1, x, sep=' ')
    exit()

x1 = (-b - sqrt(d)) / (2 * a)
x2 = (-b + sqrt(d)) / (2 * a)

if x1 < x2:
    print(2, x1, x2, sep=' ')
else:
    print(2, x2, x1, sep=' ')
