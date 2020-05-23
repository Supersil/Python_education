cnt = 0
max = 0
i = int(input())
while i != 0:
    if (i > max):
        max = i
        cnt = 1
    else:
        if (i == max):
            cnt += 1

    i = int(input())
print(cnt)
