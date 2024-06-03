n = int(input())
total_score = 0
presentation_count = 0

while True:
    presentation = input()
    if presentation == "Finish":
        break
    
    presentation_count += 1
    presentation_score = 0
    
    for i in range(n):
        score = float(input())
        presentation_score += score
    
    average_score = presentation_score / n
    total_score += average_score
    
    print(f"{presentation} - {average_score:.2f}.")

final_assessment = total_score / presentation_count

print(f"Student's final assessment is {final_assessment:.2f}.")
