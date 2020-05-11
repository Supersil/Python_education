n = int(input())

str1 = 'korov'
str2 = 'korova'
str3 = 'korovy'

if (10 < n < 20) or (n % 10 == 0) or (5 <= n % 10 <= 9):
    print(n, str1, sep=' ')
elif (n % 10 == 1):
    print(n, str2, sep=' ')
else:
    print(n, str3, sep=' ')
