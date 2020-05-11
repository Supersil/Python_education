a, b, c, d, e = int(input()), int(input()), int(input()), int(input()),\
     int(input())

if a > b:
    (a, b) = (b, a)

if b > c:
    (b, c) = (c, b)

if (a <= d and b <= e) or (a <= e and b <= d):
    print('YES')
else:
    print('NO')
