import math

record_seconds = float(input())
meters_to_swim = float(input())
swiming_speed_time = float(input())

resistance_delay = math.floor(meters_to_swim / 15) * 12.5

total_swim_time = meters_to_swim * swiming_speed_time + resistance_delay

if total_swim_time < record_seconds:
    print(f"Yes, he succeeded! The new world record is {total_swim_time:.2f} seconds.")
else:
    seconds_slower = total_swim_time - record_seconds
    print(f"No, he failed! He was {seconds_slower:.2f} seconds slower.")
