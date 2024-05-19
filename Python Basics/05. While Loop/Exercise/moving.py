width = int(input())
length = int(input())
height = int(input())

free_space = width * length * height

occupied_space = 0

while True:
    command = input()
    
    if command == "Done":
        break
    
    boxes = int(command)
    occupied_space += boxes
    
    if occupied_space > free_space:
        break

if occupied_space > free_space:
    print(f"No more free space! You need {occupied_space - free_space} Cubic meters more.")
else:
    print(f"{free_space - occupied_space} Cubic meters left.")
