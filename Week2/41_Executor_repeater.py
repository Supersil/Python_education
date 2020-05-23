A = int(input())
B = int(input())

while A >= 2 * B:
    if (A % 2 == 1):
        print('-1')
        A -= 1
    print(':2')
    A /= 2

while A > B:
    print('-1')
    A -= 1
