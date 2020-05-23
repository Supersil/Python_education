A = int(input())
i = 1
f0 = 0
f1 = 1
if A <= 1:
    print(A)
    exit()

while f1 < A:
    tmp = f0 + f1
    f0 = f1
    f1 = tmp
    i += 1
    if (f1 == A):
        print(i)
        exit()
print(-1)
