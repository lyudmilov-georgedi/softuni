n = int(input())
count_p1 = count_p2 = count_p3 = count_p4 = count_p5 = 0

for i in range(n):
    num = int(input())

    if num < 200:
        count_p1 += 1
    elif 200 <= num < 400:
        count_p2 += 1
    elif 400 <= num < 600:
        count_p3 += 1
    elif 600 <= num < 800:
        count_p4 += 1
    else:
        count_p5 += 1

total = count_p1 + count_p2 + count_p3 + count_p4 + count_p5
print(f'{count_p1 / total * 100:.2f}%')
print(f'{count_p2 / total * 100:.2f}%')
print(f'{count_p3 / total * 100:.2f}%')
print(f'{count_p4 / total * 100:.2f}%')
print(f'{count_p5 / total * 100:.2f}%')