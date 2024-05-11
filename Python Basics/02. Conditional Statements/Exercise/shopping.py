budget = float(input())
gpu_number = int(input())
cpu_number = int(input())
ram_number = int(input())

gpu_price = gpu_number * 250
cpu_price = cpu_number * (gpu_price * 0.35)
ram_price = ram_number * (gpu_price * 0.1)

total_price = gpu_price + cpu_price + ram_price

if gpu_number > cpu_number:
    total_price *= 0.85

if budget >= total_price:
    money_left = budget - total_price
    print(f"You have {money_left:.2f} leva left!")
else:
    money_needed = total_price - budget
    print(f"Not enough money! You need {money_needed:.2f} leva more!")