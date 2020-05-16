a, b, c, d = int(input()), int(input()), int(input()), int(input())

if a == 0:
    if b == 0:
        print('INF')
    else:
        print('NO')
    exit()

x = -b // a

if c != 0 and x == -d / c:
    print('NO')
elif b % a == 0:
    print(x)
else:
    print('NO')
