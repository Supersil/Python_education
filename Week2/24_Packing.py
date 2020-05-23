l1, w1, h1 = int(input()), int(input()), int(input())
l2, w2, h2 = int(input()), int(input()), int(input())
lc, wc, hc = int(input()), int(input()), int(input())

# vertical

if hc >= h1 + h2:
    firstFits = (l1 <= lc and w1 <= wc) or (l1 <= wc and w1 <= lc)
    secondFits = (l2 <= lc and w2 <= wc) or (l2 <= wc and w2 <= lc)
    if firstFits and secondFits:
        print('YES')
        exit()
if hc >= h1 and hc >= h2:
    if (w1 + w2) <= wc and l1 <= lc and l2 <= lc:
        print('YES')
        exit()
    if (w1 + l2) <= wc and l1 <= lc and w2 <= lc:
        print('YES')
        exit()
    if (l1 + w2) <= wc and w1 <= lc and l2 <= lc:
        print('YES')
        exit()
    if (l1 + l2) <= wc and w1 <= lc and w2 <= lc:
        print('YES')
        exit()
    if (w1 + w2) <= lc and l1 <= wc and l2 <= wc:
        print('YES')
        exit()
    if (w1 + l2) <= lc and l1 <= wc and w2 <= wc:
        print('YES')
        exit()
    if (l1 + w2) <= lc and w1 <= wc and l2 <= wc:
        print('YES')
        exit()
    if (l1 + l2) <= lc and w1 <= wc and w2 <= wc:
        print('YES')
        exit()

print('NO')
