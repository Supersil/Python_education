a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())

if a == 0:
    y = e / b
    x = (f - d * y) / c
    print(x, y, sep=' ')
    exit()

if d == 0:
    x = -f / c
    if (b != 0):
        y = (e - a * x) / b
    print(x, y, sep=' ')
    exit()

dev = (a - b * c / d)
x = 0
if (dev != 0):
    x = (e - f * b / d) / dev
else:
    y = e / b
    x = (f - d * y) / c
    print(x, y, sep=' ')
    exit()
y = (f - c * x) / d
print(x, y, sep=' ')
