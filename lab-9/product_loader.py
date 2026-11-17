import csv
from inventory import Inventory
from supplier import Supplier
from product_factory import ProductFactory

def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    try:
        file = open(path, newline="")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        with file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            loaded = 0
            for row in reader:
                try:
                    product = ProductFactory.create(row[0], row[1], row[2], float(row[3]), int(row[4]), supplier)
                    inventory.add_product(product)
                    loaded += 1
                except ValueError as e:
                    print(f"Error creating product from row {row}: {e}")
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")