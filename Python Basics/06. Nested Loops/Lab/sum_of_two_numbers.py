start = int(input())
end = int(input())
magic_number = int(input())

combination_count = 0
found = False

for i in range(start, end + 1):
    for j in range(start, end + 1):
        combination_count += 1
        if i + j == magic_number:
            found = True
            print(f"Combination N:{combination_count} ({i} + {j} = {magic_number})")
            break
    if found:
        break

if not found:
    print(f"{combination_count} combinations - neither equals {magic_number}")
