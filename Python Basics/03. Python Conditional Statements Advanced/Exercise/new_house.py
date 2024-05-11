flower = input()
number_of_flowers = int(input())
budget = int(input())


roses_price = 5
dahlias_price = 3.80
tulips_price = 2.80
narcissus_price = 3
gladiolus_price = 2.50
price = 0

if flower == "Roses":
    price = number_of_flowers * roses_price
    if number_of_flowers > 80:
        price = price - price * 0.1
elif flower == "Dahlias":
    price = number_of_flowers * dahlias_price
    if number_of_flowers > 90:
        price = price - price * 0.15
elif flower == "Tulips":
    price = number_of_flowers * tulips_price
    if number_of_flowers > 80:
        price = price - price * 0.15
elif flower == "Narcissus":
    price = number_of_flowers * narcissus_price
    if number_of_flowers < 120:
        price = price + price * 0.15
elif flower == "Gladiolus":
    price = number_of_flowers * gladiolus_price
    if number_of_flowers < 80:
        price = price + price * 0.2

if price <= budget:
    money_left = budget - price
    print(f"Hey, you have a great garden with {number_of_flowers} {flower} and {money_left:.2f} leva left.")
else:
    money_needed = price - budget
    print(f"Not enough money, you need {money_needed:.2f} leva more.")