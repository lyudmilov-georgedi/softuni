n = int(input())
salary = int(input())

penalties = {"Facebook": 150, "Instagram": 100, "Reddit": 50}
total_penalty = 0

for _ in range(n):
    website = input()
    if website in penalties:
        total_penalty += penalties[website]
        salary -= penalties[website]
        if salary <= 0:
            print("You have lost your salary.")
            exit()

if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)
