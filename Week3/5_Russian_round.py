from math import floor, ceil
X = float(input())
if (floor(X * 10) == ceil(X * 10)) and (X * 10) % 10 == 5:
    print(int(X) + 1)
else:
    print(round(X))
