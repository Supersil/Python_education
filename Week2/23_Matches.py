# Cases
# 1)   [1 1] [2 2]
# 1.1) [1 1] [2 2] [3 3]  ?
# 1.2) [1 1] [2 [3 3] 2]  1
# 1.3) [1 1] [2 [3 2] 3]  1
# 2)   [1 [2 2] 1]
# 2.1) [1 [2 2] 1] [3 3] 3
# 2.2) [1 [2 2] [3 1] 3] 0
# 2.3) [1 [2 2] [3 3] 1] 0
# 2.4) [1 [2 [3 2] 1] 3] 0
# 2.5) [1 [2 [3 2] 3] 1] 0
# 2.6) [1 [2 [3 3] 2] 1] 0
# 3)   [1 [2 1] 2]
# 3.1) [1 [2 1] 2] [3 3] 3
# 3.2) [1 [2 1] [3 2] 3] 0
# 3.3) [1 [2 1] [3 3] 2] 0
# 3.4) [1 [2 [3 1] 2] 3] 0
# 3.5) [1 [2 [3 1] 3] 2] 0
# 3.6) [1 [2 [3 3] 1] 2] 0

l1, r1, l2 = int(input()), int(input()), int(input())
r2, l3, r3 = int(input()), int(input()), int(input())

m = {1: (l1, r1, 1), 2: (l2, r2, 2), 3: (l3, r3, 3)}

if m[1][0] > m[2][0]:
    tmp = m[2]
    m[2] = m[1]
    m[1] = tmp

if m[2][0] > m[3][0]:
    tmp = m[3]
    m[3] = m[2]
    m[2] = tmp

if m[1][0] > m[2][0]:
    tmp = m[2]
    m[2] = m[1]
    m[1] = tmp

m1 = m[1][2]
m2 = m[2][2]
m3 = m[3][2]

m10 = m[1][0]
m11 = m[1][1]
m20 = m[2][0]
m21 = m[2][1]
m30 = m[3][0]
m31 = m[3][1]

if m21 <= m11:
    if m30 > m11:
        if m2 < m3 and m2 < m1:
            if (m21 - m20) >= (m30 - m11):
                print(m2)
                exit()
        if m1 < m3 and m1 < m2:
            if (m11 - m10) >= (m30 - m21):
                print(m1)
                exit()
        if m2 < m3:
            if (m21 - m20) >= (m30 - m11):
                print(m2)
                exit()
        if m1 < m3:
            if (m11 - m10) >= (m30 - m21):
                print(m1)
                exit()
        print(m3)
        exit()
    else:
        print(0)
        exit()
if m11 >= m20 and m21 > m11:
    if m30 > m21:
        if m2 < m3 and m2 < m1:
            if (m21 - m20) >= (m30 - m11):
                print(m2)
                exit()
        if m1 < m3 and m1 < m2:
            if (m11 - m10) >= (m30 - m21):
                print(m1)
                exit()
        if m2 < m3:
            if (m21 - m20) >= (m30 - m11):
                print(m2)
                exit()
        if m1 < m3:
            if (m11 - m10) >= (m30 - m21):
                print(m1)
                exit()
        print(m3)
        exit()
    else:
        print(0)
        exit()

if m11 < m20:
    if m21 >= m30:
        if m2 < m1 and m2 < m3:
            if (m21 - m20) >= (m30 - m11):
                print(m2)
                exit()
        if m3 < m1 and m3 < m2:
            if (m31 - m30) >= (m20 - m11):
                print(m3)
                exit()
        if m2 < m1:
            if (m21 - m20) >= (m30 - m11):
                print(m2)
                exit()
        if m3 < m1:
            if (m31 - m30) >= (m20 - m11):
                print(m3)
                exit()
        print(m1)
        exit()
    else:
        if (m11 - m10 >= m30 - m21) and (m31 - m30 >= m20 - m11):
            if m1 < m3:
                print(m1)
                exit()
            else:
                print(m3)
                exit()
        if m11 - m10 >= m30 - m21:
            print(m1)
            exit()
        if m31 - m30 >= m20 - m11:
            print(m3)
            exit()

print(-1)
