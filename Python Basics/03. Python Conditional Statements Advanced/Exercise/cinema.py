screening_type = input()
rows = int(input())
columns = int(input())

income = 0
cinema_capacity = rows * columns

if screening_type == "Premiere":
    income = 12 * cinema_capacity
elif screening_type == "Normal":
    income = 7.50 * cinema_capacity
elif screening_type == "Discount":
    income = 5 * cinema_capacity

print(f"{income:.2f} leva")