a, b, c = float(input()), float(input()), float(input())
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
if s.as_integer_ratio()[1] == 1:
    print(s.as_integer_ratio()[0])
else:
    print('{0:.6f}'.format(s))
