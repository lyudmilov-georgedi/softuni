start = int(input())
end = int(input())

result = []

for number in range(start, end + 1):
    str_number = str(number)
    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate(str_number):
        if (index + 1) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if even_sum == odd_sum:
        result.append(number)

if result:
    print(" ".join(map(str, result)))
