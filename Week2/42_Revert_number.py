N = int(input())
s = ''

while N > 0:
    s += str(N % 10)
    N //= 10
print(s)
