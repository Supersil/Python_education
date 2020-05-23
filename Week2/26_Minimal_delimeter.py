N = int(input())
m = N
i = N
while i != 1:
    if N % i == 0:
        m = i
    i -= 1
print(m)
