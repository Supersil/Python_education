K = int(input())
i = 1
cnt = 0
while i <= K:
    n = i
    s = ''
    while n > 0:
        s += str(n % 10)
        n //= 10
    if (i == int(s)):
        cnt += 1
    i += 1
print(cnt)
