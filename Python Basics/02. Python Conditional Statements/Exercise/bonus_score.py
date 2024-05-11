# SOLUTION 1:

points = int(input())
bonus = 0

if points <= 100:
    bonus = 5
elif 100 < points < 1000:
    bonus = points * 0.2
else:
    bonus = points * 0.1

if points % 2 == 0:
    bonus = bonus + 1
elif points % 10 == 5:
    bonus = bonus + 2

print(bonus)
print(bonus + points)



# SOLUTION 2:

# BONUS_POINTS_BELOW_HUNDRED = 5
# BONUS_PERCENT_ABOVE_HUNDRED = 20 / 100
# BONUS_PERCENT_ABOVE_THOUSAND = 10 / 100
# BONUS_POINTS_EVEN = 1
# BONUS_POINTS_END_WITH_FIVE = 2

# points = int(input())

# total_points = points

# if points <= 100:
#     total_points += BONUS_POINTS_BELOW_HUNDRED
# elif 1000 > points > 100:
#     total_points = total_points + points * BONUS_PERCENT_ABOVE_HUNDRED
# elif points > 1000:
#     total_points = total_points + points * BONUS_PERCENT_ABOVE_THOUSAND

# if points % 2 == 0:
#     total_points += BONUS_POINTS_EVEN
# elif points % 10 == 5:
#     total_points += BONUS_POINTS_END_WITH_FIVE

# print(total_points - points)
# print(total_points) 