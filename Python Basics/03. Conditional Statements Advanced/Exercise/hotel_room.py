month = input()
number_of_nights = int(input())

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if 7 < number_of_nights < 14:
        studio_price *= 0.95
    elif number_of_nights > 14:
        studio_price *= 0.70
        apartment_price *= 0.90
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if number_of_nights > 14:
        studio_price *= 0.80
        apartment_price *= 0.90
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
    if number_of_nights > 14:
        apartment_price *= 0.90

full_apartment_price = number_of_nights * apartment_price
full_studio_price = number_of_nights * studio_price
print(f"Apartment: {full_apartment_price:.2f} lv.")
print(f"Studio: {full_studio_price:.2f} lv.")
