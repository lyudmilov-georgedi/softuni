excursion_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

puzzle_price = 2.60
doll_price = 3
bear_price = 4.10
minion_price = 8.20
truck_price = 2

total_price = (puzzles * puzzle_price) + (dolls * doll_price) + (bears * bear_price) + (minions * minion_price) + (trucks * truck_price)

if puzzles + dolls + bears + minions + trucks >= 50:
    total_price *= 0.75

total_price -= total_price * 0.10 

if total_price >= excursion_price:
    left_money = total_price - excursion_price
    print(f"Yes! {left_money:.2f} lv left.")
else:
    needed_money = excursion_price - total_price
    print(f"Not enough money! {needed_money:.2f} lv needed.")
