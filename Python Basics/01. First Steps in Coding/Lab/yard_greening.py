sqr_meter = float(input())
greening_price = sqr_meter * 7.61
discount = 0.18 * greening_price
final_price = greening_price - discount
print("The final price is: {:.2f} lv.".format(final_price))
print("The discount is: {:.2f} lv.".format(discount))