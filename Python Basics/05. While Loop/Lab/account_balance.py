total = 0

while True:
    command = input()

    if command == "NoMoreMoney":
        break

    ammount = float(command)

    if ammount < 0:
        print("Invalid operation!")
        break

    total += ammount

    print(f"Increase: {ammount:.2f}")

print(f"Total: {total:.2f}")