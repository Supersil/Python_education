A = int(input())
B = int(input())
C = int(input())

max = A if (A > B) else B
print(max if (max > C) else C)
