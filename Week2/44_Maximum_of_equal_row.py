cnt = 0
max_cnt = 0
i = int(input())
prev = i
while i != 0:
    if (i == prev):
        cnt += 1
    else:
        cnt = 1
    if (cnt > max_cnt):
        max_cnt = cnt
    prev = i
    i = int(input())
print(max_cnt)
