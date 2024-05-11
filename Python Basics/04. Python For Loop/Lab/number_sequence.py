n = int(input())
numbers = []

for i in range(n):
    num = int(input())
    numbers.append(num)

max_num = max(numbers)
min_num = min(numbers)

print("Max number:", max_num)
print("Min number:", min_num)