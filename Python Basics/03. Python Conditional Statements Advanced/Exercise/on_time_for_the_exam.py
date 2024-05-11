exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time = exam_hour * 60 + exam_minute
arrival_time = arrival_hour * 60 + arrival_minute

difference = arrival_time - exam_time

if difference > 0:
    print("Late")
elif difference >= -30:
    print("On time")
else:
    print("Early")

difference = abs(difference)

if difference >= 60:
    hours = difference // 60
    minutes = difference % 60
    print(f"{hours}:{minutes:02d} hours {'before' if arrival_time < exam_time else 'after'} the start")
else:
    print(f"{difference} minutes {'before' if arrival_time < exam_time else 'after'} the start")