epsilon = 1e-6

a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())

if (a == 0 and b == 0 and e == 0) and (c == 0 and d == 0 and f == 0):
    print(5)
    exit()

if (a == 0 and b == 0 and e != 0) or (c == 0 and d == 0 and f != 0):
    print(0)
    exit()

if (a == 0 and b == 0 and e == 0):
    if c == 0 and d != 0:
        print(4, end=' ')
        print(f/d, end=' ')
        exit()
    if c != 0 and d == 0:
        print(3, end=' ')
        print(f/c, end=' ')
        exit()
    print(1, end=' ')
    print(-c/d, end=' ')
    print(f, end=' ')
    exit()

if (c == 0 and d == 0 and f == 0):
    if a == 0 and b != 0:
        print(4, end=' ')
        print(e/b, end=' ')
        exit()
    if a != 0 and b == 0:
        print(3, end=' ')
        print(e/a, end=' ')
        exit()
    print(1, end=' ')
    print(-a/b, end=' ')
    print(e, end=' ')
    exit()

if c != 0 and d != 0 and f != 0:
    aa = a / c
    bb = b / d
    ee = e / f
    if aa == bb == ee:
        print(1, end=' ')
        print(-a/b, end=' ')
        print(e/b, end=' ')
        exit()
    if aa == bb != ee:
        print(0)
        exit()

if a == 0:
    y = e / b
    if c != 0:
        x = (f - y * d) / c
        print(2, end=' ')
        print(x, end=' ')
        print(y, end=' ')
        exit()
    else:
        if abs(y - f / d) > epsilon:
            print(0)
            exit()
        print(4, end=' ')
        print(y, end=' ')
        exit()

if c == 0:
    y = f / d
    if a != 0:
        x = (e - y * b) / a
        print(2, end=' ')
        print(x, end=' ')
        print(y, end=' ')
        exit()
    else:
        if abs(y - e / b) > epsilon:
            print(0)
            exit()
        print(4, end=' ')
        print(y, end=' ')
        exit()

if b == 0:
    x = e / a
    if d != 0:
        y = (f - x * c) / d
        print(2, end=' ')
        print(x, end=' ')
        print(y, end=' ')
        exit()
    else:
        if abs(x - f / c) > epsilon:
            print(0)
            exit()
        print(3, end=' ')
        print(x, end=' ')
        exit()

if d == 0:
    x = e / c
    if b != 0:
        y = (e - x * a) / b
        print(2, end=' ')
        print(x, end=' ')
        print(y, end=' ')
        exit()
    else:
        if abs(x - e / a) > epsilon:
            print(0)
            exit()
        print(3, end=' ')
        print(x, end=' ')
        exit()

coef = -c / a

bb = coef * b + d
ee = coef * e + f

y = ee / bb

x = (f - y * d) / c

if (a * x + b * y - e > epsilon):
    print(0)
    exit()

print(2, end=' ')
print(x, end=' ')
print(y, end=' ')
