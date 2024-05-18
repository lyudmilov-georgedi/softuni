max_number = None

while True:
    command = input()

    if command == "Stop":
        break

    number = int(command)

    if max_number is None or number > max_number:
        max_number = number

if max_number is not None:
    print(max_number)