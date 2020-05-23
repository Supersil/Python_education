cnt = 0
prev = -1
i = int(input())
while i != 0:
    if (prev != -1) and (i > prev):
        cnt += 1
    prev = i
    i = int(input())
print(cnt)
