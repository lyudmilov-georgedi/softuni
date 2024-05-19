max_poor_grades = int(input())

poor_grade = 0
total_problems = 0
sum_grades = 0
last_problem = ""

while True:
    problem_name = input()

    if problem_name == "Enough":
        average_score = sum_grades / total_problems if total_problems > 0 else 0
        print(f"Average score: {average_score:.2f}")
        print(f"Number of problems: {total_problems}")
        print(f"Last problem: {last_problem}")
        break

    grade = int(input())

    total_problems += 1
    sum_grades += grade
    last_problem = problem_name

    if grade <= 4:
        poor_grade += 1
    
    if poor_grade == max_poor_grades:
        print(f"You need a break, {poor_grade} poor grades.")
        break
