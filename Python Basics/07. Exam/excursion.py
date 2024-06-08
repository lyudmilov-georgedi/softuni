number_of_people = int(input())
number_of_nights = int(input())
number_of_transport_cards = int(input())
number_of_museum_tickets = int(input())

price_per_night = 20.00
price_per_transport_card = 1.60
price_per_museum_ticket = 6.00

total_per_person = (number_of_nights * price_per_night +
                    number_of_transport_cards * price_per_transport_card +
                    number_of_museum_tickets * price_per_museum_ticket)

total_for_group = total_per_person * number_of_people

total_with_extra_expenses = total_for_group * 1.25

print(f"{total_with_extra_expenses:.2f}")
