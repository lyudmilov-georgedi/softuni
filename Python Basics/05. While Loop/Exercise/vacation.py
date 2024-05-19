needed_money = float(input())
current_money = float(input())

total_days = 0
consecutive_spend_days = 0

while current_money < needed_money and consecutive_spend_days < 5:
    action = input()
    amount = float(input())
    total_days += 1
    
    if action == "spend":
        current_money -= amount

        if current_money < 0:
            current_money = 0
            
        consecutive_spend_days += 1

    elif action == "save": 
        current_money += amount
        consecutive_spend_days = 0

if consecutive_spend_days == 5:
    print("You can't save the money.")
    print(total_days)

elif current_money >= needed_money:
    print(f"You saved the money for {total_days} days.")
