nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

nylon_price = (nylon + 2) * 1.50
paint_price = (paint + paint*0.1) * 14.50
thinner_price = thinner * 5.00
total_materials_price = nylon_price + paint_price + thinner_price + 0.40
worker_price = (total_materials_price * 0.3) * 8
total_price =  total_materials_price + worker_price

print(total_price)