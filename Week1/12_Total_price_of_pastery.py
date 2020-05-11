A = int(input())
B = int(input())
N = int(input())

price = (A * 100 + B) * N

print(price // 100, price % 100, sep=' ')
