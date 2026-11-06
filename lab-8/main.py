from digital_product import DigitalProduct
from physical_product import PhysicalProduct
from inventory import Inventory

def menu():
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")
    inventory = Inventory()
    inventory.load()
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
                product_type = input("Physical or Digital? (p/d): ").lower()
                if product_type not in ("p", "d"):
                    print("Invalid product type.")
                    continue
                product_id = input("Product ID: ")
                name = input("Product Name: ")
                price = float(input("Product Price: "))
                stock = int(input("Stock Quantity: "))
                if product_type == "p":
                    weight = float(input("Weight(kg): "))
                    product = PhysicalProduct(product_id, name, price, stock, weight)
                else:
                    download_size = float(input("Download Size(MB): "))
                    product = DigitalProduct(product_id, name, price, stock, download_size)
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
                if inventory.update_stock(product_id, new_quantity):
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
            inventory.save()
            print("Inventory saved successfully to inventory.json.")
        elif option == "6":
            print("Saving inventory before exit...")
            inventory.save()
            print("Inventory saved successfully.\n")
            print("Thank you for using Inventory Management System")
            print("Program terminated.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    menu()