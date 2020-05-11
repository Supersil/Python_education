number = int(input())
rev_number = (number % 10) * 1000 + ((number // 10) % 10) * 100 + \
    ((number // 100) % 10) * 10 + (number // 1000)

print(1 * (number == rev_number))
