n = int(input())
current_number = 1
break_outer = False

for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(current_number, end=" ")
        current_number += 1
        if current_number > n:
            break_outer = True
            break
    print()
    
    if break_outer:
        break
