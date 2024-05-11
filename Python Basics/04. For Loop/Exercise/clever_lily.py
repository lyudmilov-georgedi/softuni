age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money_saved_odd = 0
money_saved_even = 0

for birthday in range(1, age +1):
    if birthday % 2 == 1:
        money_saved_odd += toy_price
    else:
        money_saved_even += 10 * (birthday // 2)
        money_saved_even -= 1
    
total_money_saved = money_saved_odd + money_saved_even

if total_money_saved >= washing_machine_price:
    print(f"Yes! {total_money_saved - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price - total_money_saved:.2f}")