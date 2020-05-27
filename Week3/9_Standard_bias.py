from math import sqrt

num = int(input())

if (num == 0):
    print(0)
    exit()
sum = 0
nums = []
while num != 0:
    sum += num
    nums.append(num)
    num = int(input())

mid = sum / len(nums)
sqr_sum = 0.0

for num in nums:
    sqr_sum += (num - mid)**2

sqr_sum /= (len(nums) - 1)

print(sqrt(sqr_sum))
