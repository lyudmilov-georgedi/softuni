days = int(input())
room_type = input()
rating = input()

prices = {
    "room for one person": 18,
    "apartment": 25,
    "president apartment": 35
}

days -= 1

total_price = days * prices[room_type]

if days > 15:
    if room_type == "room for one person":
        discount = 0
    elif room_type == "apartment":
        discount = 0.5
    else:
        discount = 0.2
elif 10 <= days <= 15:
    if room_type == "room for one person":
        discount = 0
    elif room_type == "apartment":
        discount = 0.35
    else:
        discount = 0.15
else:
    if room_type == "room for one person":
        discount = 0
    elif room_type == "apartment":
        discount = 0.3
    else:
        discount = 0.1

final_price = total_price - (total_price * discount)

if rating == "positive":
    final_price += final_price * 0.25
else:
    final_price -= final_price * 0.1

print(f"{final_price:.2f}")
