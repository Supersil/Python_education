from math import floor, ceil
P, X, Y = float(input()), float(input()), float(input())
total = X * 100.0 + Y
total = total * (100.0 + P) / 100.0
total = int(total)
print(total // 100, total % 100, sep=' ')
