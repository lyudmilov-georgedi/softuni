n = int(input())

special_numbers = []

for number in range(1111, 10000):
    num_str = str(number)
    is_special = True
    for digit in num_str:
        if int(digit) == 0 or n % int(digit) != 0:
            is_special = False
            break
    if is_special:
        special_numbers.append(number)

print(" ".join(map(str, special_numbers)))
