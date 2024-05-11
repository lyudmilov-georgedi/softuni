year_tax = int(input())

shoes = year_tax - year_tax * 0.4
equipment = shoes - shoes * 0.2
ball = equipment / 4
accessories = ball / 5

total_equipment_price = year_tax + shoes + equipment + ball + accessories

print(total_equipment_price)