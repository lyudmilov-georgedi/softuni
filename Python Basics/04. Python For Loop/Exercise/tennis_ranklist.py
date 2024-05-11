num_tournaments = int(input())
starting_points = int(input())

total_points = starting_points
total_wins = 0

for i in range (num_tournaments):
    result = input()

    if result == "W":
        total_points += 2000
        total_wins += 1
    elif result == "F":
        total_points += 1200
    elif result == "SF":
        total_points += 720
    
final_points = total_points
average_points = (total_points - starting_points) // num_tournaments
win_percentage = (total_wins / num_tournaments) * 100

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{win_percentage:.2f}%")