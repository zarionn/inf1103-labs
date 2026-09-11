inventory = 0
total_stock = 0
while True:
    stock_value = input("Please enter the stock quantity: ")
    if stock_value == "Quit" or stock_value == "quit":
        break
    elif stock_value.isdigit() == False:
        print("Please enter a valid stock quantity.")
        continue

    stock_value = int(stock_value)

    if stock_value < 0:
        print("Stock quantity cannot be negative.")
        continue
    
    total_stock += stock_value
