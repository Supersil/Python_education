from math import floor, ceil

n = int(input())
x = float(input())
sum = 0.0
i = 0
while i <= n:
    coef = float(input())
    sum = sum * x + coef
    i += 1
print(sum)
