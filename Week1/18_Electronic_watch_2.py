seconds = int(input())

hours = (seconds // 3600) % 24
minutes = (seconds % 3600) // 60
minutes = str(minutes // 10) + str(minutes % 10)
seconds = seconds % 60
seconds = str(seconds // 10) + str(seconds % 10)
print(hours, minutes, seconds, sep=':')
