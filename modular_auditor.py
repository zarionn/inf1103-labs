inventory = 0
Rejected_entry = 0
# while True:
#     stock_value = input("Please enter the stock quantity: ")
#     if stock_value == "Quit" or stock_value == "quit":
#         print("Total units processed:", inventory)
#         print("Number of failed or rejected entries:", Rejected_entry)
#         break
#     elif stock_value.isdigit() == False:
#         print("Please enter a valid stock quantity.")
#         Rejected_entry += 1
#         continue

#     stock_value = int(stock_value)

#     if stock_value < 0:
#         print("Stock quantity cannot be negative.")
#         Rejected_entry += 1
#         continue

#     inventory += stock_value

#     if inventory > 500:
#         print("Alert: total stock has exceeded the maximum capacity.")
#         break

def get_valid_input():
    global Rejected_entry
    while True:
        stock_value = input("Please enter the stock quantity: ")
        if stock_value == "Quit" or stock_value == "quit":
            return "quit"
            
        elif stock_value.isdigit() == False:
            print("Please enter a valid stock quantity.")
            Rejected_entry += 1
            continue
        return int(stock_value)
        
            