from math import floor, ceil
P, X, Y, K = float(input()), float(input()), float(input()), float(input())
total = X * 100.0 + Y
while K != 0:
    total = total * (100.0 + P) / 100.0
    total = (int(total))
    K -= 1
print(total // 100, total % 100, sep=' ')
