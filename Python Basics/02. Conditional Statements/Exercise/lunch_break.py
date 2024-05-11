import math

series_name = input()
episode_duration = int(input())
rest_duration = int(input())

lunch_time = rest_duration / 8
rest_time = rest_duration / 4

time_left = rest_duration - lunch_time - rest_time

if episode_duration <= time_left:
    time_left = math.ceil(time_left - episode_duration)
    print(f"You have enough time to watch {series_name} and left with {time_left} minutes free time.")
else:
    time_needed = math.ceil(episode_duration - time_left)
    print(f"You don't have enough time to watch {series_name}, you need {time_needed} more minutes.")