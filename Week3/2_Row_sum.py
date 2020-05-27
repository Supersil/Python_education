n = int(input())
sum = 0.0
i = 1
while i <= n:
    sum += 1 / (i * i)
    i += 1
print('{0:.5f}'.format(sum))
