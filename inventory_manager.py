import os
import json


def add_product(inventory):
    try:
        (print("\nAdd New Product"))
        product_id = input("Product ID: ")
        name = input("Product Name: ")
        price = float(input("Product Price: "))
        stock = int(input("Stock Quantity: "))
        inventory.append({"ID": product_id, "Name": name, "Price": price, "stock": stock})
        print("\nProduct added successfully")
    except ValueError:
        print("Invalid input. Please enter valid data types for price and stock.")


def update_stock(inventory, product_id):
    item = search_product(inventory, product_id)
    if item:
        print("Product Found:")
        print(f"Name: {item['Name']}")
        print(f"Current Stock: {item['stock']}")
        new_quantity = int(input("New Stock Quantity: "))
        item["stock"] = new_quantity
        print("Stock updated successfully!")
    else:
        print("Product not found")


def search_product(inventory, product_id):
    for item in inventory:
        if item["ID"] == product_id:
            return item
    return None


def display_all(inventory):
    print("Current Inventory")
    print("------------------------------------------------")
    for item in inventory:
        print(f"ID: {item['ID']} | Name: {item['Name']} | Price: ${item['Price']:.2f} | Stock: {item['stock']}")
    print("------------------------------------------------")
    return None


def load_inventory():
    if os.path.exists("inventory.json"):
        print("inventory.json found.")
        with open("inventory.json", "r") as file:
            inventory = json.load(file)
        print("Inventory loaded successfully.")
        return inventory
    else:
        print("inventory.json not found, starting with empty inventory.")
        return []

def menu():
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")
    inventory = load_inventory()
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")
    print("")
    while True:
        option = input("Enter option: ")
        if option == "1":
            display_all(inventory)
        elif option == "2":
            add_product(inventory)
        elif option == "3":
            print("Update Stock")
            product_id = input("Enter Product ID:")
            update_stock(inventory, product_id)
        elif option == "4":
            print("Search Product")
            product_id = input("Enter Product ID:")
            item = search_product(inventory, product_id)
            if item:
                print("\nProduct Found")
                print("------------------------------------------------")
                print(f"ID: {item['ID']}")
                print(f"Name: {item['Name']}")
                print(f"Price: ${item['Price']:.2f}")
                print(f"Stock: {item['stock']}")
                print("------------------------------------------------")
            else:
                print("Product not found.")
        elif option == "5":
            pass
        elif option == "6":
            print("Thank you for using Inventory Management System")
            print("Program terminated.")
            break
        else:
            print("Invalid option.")

menu()