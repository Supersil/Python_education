a = int(input())
b = int(input())
c = int(input())

ab = a + b
ac = a + c
bc = c + b

abc = a + b + c

a2 = a**2
b2 = b**2
c2 = c**2

if c >= ab or b >= ac or a >= bc:
    print('impossible')
elif a2 == b2 + c2 or b2 == a2 + c2 or c2 == a2 + b2:
    print('rectangular')
elif a2 > b2 + c2 or b2 > a2 + c2 or c2 > a2 + b2:
    print('obtuse')
else:
    print('acute')
