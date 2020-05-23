prev = -1
max = 0
i = int(input())
while i != 0:
    if (i > max):
        if (max != 0):
            prev = max
        max = i
    else:
        if (i > prev):
            prev = i
    i = int(input())
print(prev)
