n = int(input())
sum_left = 0
sum_right = 0

for i in range(n):
    num = int(input())
    sum_left += num

for i in range(n):
    num = int(input())
    sum_right += num

if sum_left == sum_right:
    print("Yes, sum =", sum_left)
else:
    diff = abs(sum_left - sum_right)
    print("No, diff =", diff)