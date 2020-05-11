minutes = int(input())

hours = (minutes // 60) % 24
minutes = minutes % 60
print(hours, minutes, sep=' ')
