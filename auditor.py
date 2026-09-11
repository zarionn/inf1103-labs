inventory = 0
while True:
    stock_value = input("Please enter the stock quantity: ")
    if stock_value == "Quit" or stock_value == "quit":
        break
    elif stock_value.isdigit() == False:
        print("Please enter a vaid stock quantity.")
        continue
    stock_value = int(stock_value)
