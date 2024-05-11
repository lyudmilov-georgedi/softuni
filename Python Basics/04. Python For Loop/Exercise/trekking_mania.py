num_groups = int(input())
total_climbers = 0
musala_climbers = 0
monblan_climbers = 0
kilimanjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0

for i in range(num_groups):
    group_size = int(input())
    total_climbers += group_size
    
    if group_size <= 5:
        musala_climbers += group_size
    elif 6 <= group_size <= 12:
        monblan_climbers += group_size
    elif 13 <= group_size <= 25:
        kilimanjaro_climbers += group_size
    elif 26 <= group_size <= 40:
        k2_climbers += group_size
    else:
        everest_climbers += group_size

musala_percentage = (musala_climbers / total_climbers) * 100
monblan_percentage = (monblan_climbers / total_climbers) * 100
kilimanjaro_percentage = (kilimanjaro_climbers / total_climbers) * 100
k2_percentage = (k2_climbers / total_climbers) * 100
everest_percentage = (everest_climbers / total_climbers) * 100

print(f"{musala_percentage:.2f}%")
print(f"{monblan_percentage:.2f}%")
print(f"{kilimanjaro_percentage:.2f}%")
print(f"{k2_percentage:.2f}%")
print(f"{everest_percentage:.2f}%")

