x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dx = x2 - x1
dy = y2 - y1

if dx < 0 or dy < 0 or dx > dy:
    print('NO')
elif dx % 2 == dy % 2:
    print('YES')
else:
    print('NO')
