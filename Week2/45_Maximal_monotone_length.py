cnt = 1
max_cnt = 0
i = int(input())
if (i == 0):
    print(0)
    exit()
prev = i
sign = 0
prev_sign = 0
i = int(input())
if (i == 0):
    print(1)
    exit()
if (prev > i):
    prev_sign = +1
elif (prev < i):
    prev_sign = -1
else:
    prev_sign = 0

while i != 0:
    if (prev > i):
        sign = +1
    elif (prev < i):
        sign = -1
    else:
        sign = 0

    if sign != 0 and sign == prev_sign:
        cnt += 1
    elif sign != 0:
        cnt = 2
    else:
        cnt = 1
    if (cnt > max_cnt):
        max_cnt = cnt
    prev = i
    prev_sign = sign
    i = int(input())
print(max_cnt)
