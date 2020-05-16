k = int(input())

if k % 3 == 0 or k % 5 == 0:
    print('YES')
    exit()

flag = False

for i in range(k // 5):
    if (k - i * 5) % 3 == 0:
        flag = True

if flag:
    print('YES')
else:
    print('NO')
