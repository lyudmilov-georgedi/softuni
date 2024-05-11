budget = int(input())
season = input()
fishermen_count = int(input())

boat_rental_price = 0

if season == "Spring":
    boat_rental_price = 3000
elif season == "Summer" or season == "Autumn":
    boat_rental_price = 4200
elif season == "Winter":
    boat_rental_price = 2600

if fishermen_count <= 6:
    boat_rental_price *= 0.9
elif 7 <= fishermen_count <= 11:
    boat_rental_price *= 0.85
else:
    boat_rental_price *= 0.75

if fishermen_count % 2 == 0 and season != "Autumn":
    boat_rental_price *= 0.95

if budget >= boat_rental_price:
    left_money = budget - boat_rental_price
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    needed_money = boat_rental_price - budget
    print(f"Not enough money! You need {needed_money:.2f} leva.")
