x1, y1, z1, x2, y2, z2 = int(input()), int(input()), int(input()),\
     int(input()), int(input()), int(input())

max_cnt = 0

size = [[x2, y2, z2], [x2, z2, y2], [y2, z2, x2], [y2, x2, z2],
        [z2, y2, x2], [z2, x2, y2]]

for i in range(6):
    tmp = 1
    tmp *= (x1 // size[i][0])
    tmp *= (y1 // size[i][1])
    tmp *= (z1 // size[i][2])
    if tmp > max_cnt:
        max_cnt = tmp

print(max_cnt)
