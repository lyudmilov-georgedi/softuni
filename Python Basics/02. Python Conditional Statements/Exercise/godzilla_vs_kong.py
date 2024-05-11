movie_budget = float(input())
number_of_extras = int(input())
clothing_price_for_one_extra = float(input())

set_price = movie_budget * 0.1
clothing_price = number_of_extras * clothing_price_for_one_extra
total_price = movie_budget + set_price + clothing_price

if number_of_extras > 150:
    clothing_price = clothing_price - clothing_price * 0.10
    total_price -= clothing_price

if set_price + clothing_price > movie_budget:
    money_needed = (set_price + clothing_price) - movie_budget
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")
elif set_price + clothing_price <= movie_budget:
    money_left = movie_budget - (set_price + clothing_price)
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")