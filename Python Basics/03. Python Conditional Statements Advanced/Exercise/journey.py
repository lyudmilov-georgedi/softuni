budget = float(input())
season = input()

spend = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        spend = budget * 0.30
    elif season == "winter":
        spend = budget * 0.70
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        spend = budget * 0.40
    elif season == "winter":
        spend = budget * 0.80
elif budget > 1000:
    destination = "Europe"
    spend = budget * 0.90

if season == "summer" and destination != "Europe":
    vacation_type = "Camp"
elif season == "winter" or destination == "Europe":
    vacation_type = "Hotel"

print(f"Somewhere in {destination}")
print(f"{vacation_type} - {spend:.2f}")
