inventory = 0
while True:
    stock_value = input("Please enter the stock quantity: ")
    if stock_value == "Quit" or stock_value == "quit":
        break
    stock_value = int(stock_value)
