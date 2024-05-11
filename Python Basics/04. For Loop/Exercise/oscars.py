actor_name = input()
academy_points = float(input())
number_of_evaluators = int(input())

total_points = academy_points

for i in range(number_of_evaluators):
    evaluator_name = input()
    evaluator_points = float(input())
    evaluator_points = len(evaluator_name) * evaluator_points / 2
    total_points += evaluator_points

    if total_points > 1250.50:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break
    
if total_points <= 1250.50:
    points_needed = 1250.50 - total_points
    print(f"Sorry, {actor_name} you need {points_needed:.1f} more!")