hours = int(input())
minutes = int(input())

total_current_minutes = hours * 60 + minutes
total_minutes_plus_15 = total_current_minutes + 15

h = total_minutes_plus_15 // 60 % 24
m = total_minutes_plus_15 % 60

if m < 10:
    print(f"{h}:0{m}")
else:
    print(f"{h}:{m}")