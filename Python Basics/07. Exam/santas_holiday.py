number_of_days = int(input())
room_type = input()
score = input()

price_per_room_for_one_person = 18.00
price_per_apartment = 25.00
price_per_president_apartment = 35.00
total_price = 0

if number_of_days < 10:
    price_per_apartment = price_per_apartment * 0.70
    price_per_president_apartment = price_per_president_apartment * 0.90
elif number_of_days > 15:
    price_per_apartment = price_per_apartment * 0.50
    price_per_president_apartment = price_per_president_apartment * 0.80
else:  
    price_per_apartment = price_per_apartment * 0.65
    price_per_president_apartment = price_per_president_apartment * 0.85

number_of_nights = number_of_days - 1

if room_type == "room for one person":
    total_price = number_of_nights * price_per_room_for_one_person
elif room_type == "apartment":
    total_price = number_of_nights * price_per_apartment
elif room_type == "president apartment":
    total_price = number_of_nights * price_per_president_apartment

if score == "positive":
    total_price = total_price * 1.25
elif score == "negative":
    total_price = total_price * 0.90

print(f"{total_price:.2f}")