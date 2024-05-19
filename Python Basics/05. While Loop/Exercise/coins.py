change = float(input())

change = round(change * 100)

coins = [200, 100, 50, 20, 10, 5, 2, 1]
count = 0

while change > 0:
    for coin in coins:
        while change >= coin:
            change -= coin
            count += 1

print(count)