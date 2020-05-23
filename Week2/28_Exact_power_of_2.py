N = int(input())

while N != 1:
    if (N % 2 != 0):
        print('NO')
        exit()
    N /= 2
print('YES')
