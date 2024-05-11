from math import pi

figure = input()

if figure == "square":
    num = float(input())
    result = num * num
    print(f"{result:.3f}")
elif figure == "rectangle":
    first_num = float(input())
    second_num = float(input())
    result = first_num * second_num
    print(f"{result:.3f}")
elif figure == "circle":
    radius = float(input())
    result = radius * radius * pi
    print(f"{result:.3f}")
elif figure == "triangle":
    length = float(input())
    height = float(input())
    result = length * height / 2
    print(f"{result:.3f}")