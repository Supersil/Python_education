l1, r1, l2 = int(input()), int(input()), int(input())
r2, l3, r3 = int(input()), int(input()), int(input())


(left_l, left_r) = (l1, r1)

if (l2 < left_l):
    (left_l, left_r) = (l2, r2)

if (l3 < left_l):
    (left_l, left_r) = (l3, r3)

(right_l, right_r) = (l1, r1)
if (r2 > right_r):
    (right_l, right_r) = (l2, r2)
if (r3 > right_r):
    (right_l, right_r) = (l3, r3)

if (left_l, left_r) == (right_l, right_r):
    print(0)
    exit()


print(0)
print(-1)
