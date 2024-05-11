input = input()

if input in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
    print("Working day")
elif input in ("Saturday", "Sunday"):
    print("Weekend")
else:
    print("Error")
