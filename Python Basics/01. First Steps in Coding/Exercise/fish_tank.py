length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

aquarium_volume = length * width * height
volume_in_liters = aquarium_volume / 1000
liters_needed = volume_in_liters * (1 - percentage/100)

print(liters_needed)