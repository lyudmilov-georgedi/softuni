search_book = input()

checked_books = 0

while True:
    current_book = input()

    if current_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {checked_books} books.")
        break

    if current_book == search_book:
        print(f"You checked {checked_books} books and found it.")
        break
    
    checked_books += 1
    