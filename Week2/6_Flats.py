x = int(input())
y = int(input())

stages = y - x + 1

if (x - 1) % stages == 0:
    print("YES")
else:
    print("NO")
