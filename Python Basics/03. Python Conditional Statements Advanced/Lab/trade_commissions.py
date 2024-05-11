comission_rate = {
    "Sofia": [0.05, 0.07, 0.08, 0.12],
    "Varna": [0.045, 0.075, 0.10, 0.13],
    "Plovdiv": [0.055, 0.08, 0.12, 0.145]
}

city = input()
sales_volume = float(input())

if sales_volume < 0 or city not in comission_rate:
    print("error")
else:
    rate = comission_rate[city]
    if sales_volume <= 500:
        commission = sales_volume * rate[0]
    elif sales_volume <= 1000:
        commission = sales_volume * rate[1]
    elif sales_volume <= 10000:
        commission = sales_volume * rate[2]
    else:
        commission = sales_volume * rate[3]

    print(f"{commission:.2f}")