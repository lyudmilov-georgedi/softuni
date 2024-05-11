import math

number_of_pages = int(input())
pages_read_per_hour = int(input())
number_of_days_per_book = int(input())
hours_per_day_per_book = (number_of_pages / pages_read_per_hour) / number_of_days_per_book
print(math.floor(hours_per_day_per_book))