import os
import json


class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def update_stock(self, quantity):
        if quantity < 0:
            print("Stock cannot be negative")
            return False
        self.__stock = quantity
        return True

    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}")

    def to_dict(self):
        return {"ID": self.__product_id, "Name": self.__name, "Price": self.__price, "stock": self.__stock}


class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")


class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size =  download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size} MB")


class Inventory:
    def __init__(self):
        self.__products = []


    def add_product(self, product):
        self.__products.append(product)


    def search_product(self, product_id):
        for item in self.__products:
            if item.get_product_id() == product_id:
                return item
        return None

    def display_all(self):
        print("Current Inventory")
        print("------------------------------------------------")
        for item in self.__products:
            item.display_information()
        print("------------------------------------------------")
        return None

    def get_all(self):
        return self.__products


def load_inventory():
    inventory = Inventory()
    if os.path.exists("inventory.json"):
        print("inventory.json found.")
        with open("inventory.json", "r") as file:
            data = json.load(file)
        for item in data:
            product = Product(item["ID"], item["Name"], item["Price"], item["stock"])
            inventory.add_product(product)
        print("Inventory loaded successfully.")
        return inventory
    else:
        print("inventory.json not found, starting with empty inventory.")
        return inventory


def save_inventory(inventory):
    data = []
    for product in inventory.get_all():
        data.append(product.to_dict())
    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

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
            inventory.display_all()
        elif option == "2":
            try:
                print("\nAdd New Product:")
                product_id = input("Product ID: ")
                name = input("Product Name: ")
                price = float(input("Product Price: "))
                stock = int(input("Stock Quantity: "))
                product = Product(product_id, name, price, stock)
                inventory.add_product(product)
                print("\nProduct added successfully")
            except ValueError:
                print("Invalid input. Please enter valid data types for price and stock")
            
        elif option == "3":
            print("Update Stock")
            product_id = input("Enter Product ID:")
            item = inventory.search_product(product_id)
            if item:
                print("Product Found:")
                item.display_information()
                new_quantity = int(input("New Stock Quantity: "))
                if item.update_stock(new_quantity):
                    print("Stock updated successfully!")
            else:
                print("Product not found")
        elif option == "4":
            print("Search Product")
            product_id = input("Enter Product ID:")
            item = inventory.search_product(product_id)
            if item:
                print("\nProduct Found")
                print("------------------------------------------------")
                item.display_information()
                print("------------------------------------------------")
            else:
                print("Product not found.")
        elif option == "5":
            print("Saving inventory...")
            save_inventory(inventory)
            print("Inventory saved successfully to inventory.json.")
        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Inventory saved successfully.\n")
            print("Thank you for using Inventory Management System")
            print("Program terminated.")
            break
        else:
            print("Invalid option.")


menu()