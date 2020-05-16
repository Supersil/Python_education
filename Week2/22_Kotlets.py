k, m, n = int(input()), int(input()), int(input())

sides = n * 2

time = max(((sides + k - 1) // k), 2) * m

print(time)
