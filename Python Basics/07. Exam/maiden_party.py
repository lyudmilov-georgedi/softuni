party_cost = float(input())
num_love_messages = int(input())
num_wax_roses = int(input())
num_keychains = int(input())
num_caricatures = int(input())
num_surprise = int(input())

price_love_message = 0.60
price_wax_rose = 7.20
price_keychain = 3.60
price_caricature = 18.20
price_surprise = 22.00

total_sum = (num_love_messages * price_love_message +
             num_wax_roses * price_wax_rose +
             num_keychains * price_keychain +
             num_caricatures * price_caricature +
             num_surprise * price_surprise)

total_items = (num_love_messages + num_wax_roses + num_keychains + num_caricatures + num_surprise)

if total_items >= 25:
    total_sum = total_sum * 0.65

profit = total_sum * 0.90

if profit >= party_cost:
    money_left = profit - party_cost
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_needed = abs(profit - party_cost)
    print(f"Not enough money! {money_needed:.2f} lv needed.")