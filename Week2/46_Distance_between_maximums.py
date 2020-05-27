first = 0
second = 0
third = 0
num = 0
i = int(input())
if (i == 0):
    print(0)
    exit()
first = i
i = int(input())
if (i == 0):
    print(0)
    exit()
second = i
i = int(input())
if (i == 0):
    print(0)
    exit()
third = i
prev_max = 0
max = 0
max_dist = 0
num = 2
while i != 0:
    if second > first and second > third:
        prev_max = max
        max = num
        if (prev_max != 0):
            dist = max - prev_max
            if dist < max_dist or max_dist == 0:
                max_dist = dist
    i = int(input())
    first = second
    second = third
    third = i
    num += 1
print(max_dist)
