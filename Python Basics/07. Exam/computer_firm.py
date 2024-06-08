n = int(input()) # number of computers

total_sales = 0
total_rating = 0

for item in range(n):
    data = int(input())
    rating = data % 10
    possible_sales = data // 10
    
    if rating == 2:
        sales = 0
    elif rating == 3:
        sales = possible_sales * 0.50
    elif rating == 4:
        sales = possible_sales * 0.70
    elif rating == 5:
        sales = possible_sales * 0.85
    elif rating == 6:
        sales = possible_sales * 1.00
    
    total_sales += sales
    total_rating += rating

average_rating = total_rating / n

print(f"{total_sales:.2f}")
print(f"{average_rating:.2f}")