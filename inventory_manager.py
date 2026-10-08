inventory = [
    {"ID": "P001", "Name": "Laptop", "Price": 1200.00, "stock": 15},
    {"ID": "P002", "Name": "Mouse", "Price": 25.50, "stock": 40},
    {"ID": "P003", "Name": "Keyboard", "Price": 45.00, "stock": 25}
]


def add_product(inventory):
    
    pass


def update_stock():
    pass


def search_product():
    pass

def display_all(inventory):
    print("Current Inventory")
    print("------------------------------------------------")
    for item in inventory:
        print(f"ID: {item['ID']} | Name: {item['Name']} | Price: ${item['Price']:.2f} | Stock: {item['stock']}")
    print("------------------------------------------------")
    return None