A = int(input())
B = int(input())

print('YES' * (A % B == 0) + 'NO' * (A % B != 0))
