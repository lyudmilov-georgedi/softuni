n = int(input())
odd_sum = 0
even_sum = 0
numbers = []

for i in range(n):
    num = int(input())
    numbers.append(num)

for j in range(len(numbers)):
    if j % 2 == 0:
        even_sum += numbers[j]
    else:
        odd_sum += numbers[j]

if even_sum == odd_sum:
    print("Yes")
    print("Sum =", even_sum)
else:
    diff = abs(even_sum - odd_sum)
    print("No")
    print("Diff =", diff)