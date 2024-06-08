price_goal = int(input())

price_haircut = {
    "mens": 15,
    "ladies": 20,
    "kids": 10
}

price_color = {
    "touch up": 20,
    "full color": 30
}

total_price = 0
target_reached = False

while not target_reached:
    command = input()

    if command == "closed":
        break

    if command == "haircut":
        haircut_command = input()
        total_price += price_haircut[haircut_command]
    elif command == "color":
        color_command = input()
        total_price += price_color[color_command]
    
    if total_price >= price_goal:
        target_reached = True

if total_price >= price_goal:
    print(f"You have reached your target for the day!")
else:
    price_difference = price_goal - total_price
    print(f"Target not reached! You need {price_difference}lv. more.")

print(f"Earned money: {total_price}lv.")