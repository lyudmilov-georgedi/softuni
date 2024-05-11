pens = int(input())
markers = int(input())
cleaner = int(input())
discount = int(input())

pen_price = pens * 5.80
markers_price = markers * 7.20
cleaner_price = cleaner * 1.20
total_price = pen_price + markers_price + cleaner_price
total_price_with_discount = total_price - (total_price * (discount/100))
print(total_price_with_discount)