import os
inventory = 0
Rejected_entry = 0
deliveries = 0

def get_valid_input():
    Rejected_entry = 0
    while True:
        stock_value = input("Please enter the stock quantity: ")
        if stock_value == "Quit" or stock_value == "quit":
            return "quit", Rejected_entry
            
        elif stock_value.isdigit() == False:
            print("Please enter a valid stock quantity.")
            Rejected_entry += 1
            continue

        return int(stock_value), Rejected_entry

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

def calculate_tax(amount):
    tax = 0.1 * amount
    return tax

def generate_report(total_units, failed_attempts):
    print("Number of failed or rejected entries:", failed_attempts)
    print("Total deliveries processed:", total_units)

def load_inventory():
    transaction_history = []
    if os.path.exists("inventory.txt"):
        with open("inventory.txt", "r") as file:
            inventory_lines = file.readlines()
            for lines in inventory_lines[1:]:
                transaction_history.append(int(lines.strip()))
            return int(inventory_lines[0]), transaction_history
    else:
        return 0, transaction_history

def save_inventory():
    return
inventory, transaction_history = load_inventory()
while True:
    stock_value, rejected = get_valid_input()
    Rejected_entry += rejected
    if stock_value == "quit":
        generate_report(deliveries, Rejected_entry)
        print(transaction_history)
        break
    inventory = process_delivery(inventory, stock_value)
    deliveries += 1
    transaction_history.append(stock_value)
    tax = calculate_tax(stock_value)
    if inventory > 500:
        print("Alert: total stock has exceeded the maximum capacity.")
        break