from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order
from product import Product


def test_association() -> None:
    print("=== Testing association between Supplier and Products ===")
    supplier = Supplier("S100", "TechCrop", "sales@techcrop.com")
    p1 = PhysicalProduct("P100", "Laptop", 1200.00, 10, 2.5, supplier)
    d1 = DigitalProduct("D100", "E-book", 15.00, 100, 5.0, supplier)

    print("\nBefore del supplier:")
    p1.display_supplier()
    d1.display_supplier()

    del supplier

    print("\nAfter del supplier:")
    p1.display_supplier()
    d1.display_supplier()


def test_aggregation() -> None:
    print("\n=== Testing aggregation between Inventory and Products ===")
    supplier = Supplier("S200", "GadgetHub", "hello@gadgethub.com")

    # 1. Product created before any inventory
    p1 = PhysicalProduct("P200", "Keyboard", 49.90, 30, 0.8, supplier)

    # 2. Add to Inventory A
    inventory_a = Inventory()
    inventory_b = Inventory()
    inventory_a.add_product(p1)
    print("\nInventory A after adding P200:")
    inventory_a.display_all()

    # 3. Remove from Inventory A
    inventory_a.remove_product("P200")
    print("\nInventory A after removing P200:")
    inventory_a.display_all()

    print("\nProduct still usable after removal:")
    p1.display_information()

    # 4. Add the same product to Inventory B
    inventory_b.add_product(p1)
    print("\nInventory B after adding the same P200:")
    inventory_b.display_all()

    print("\nSame object in Inventory B?", inventory_b.find_product("P200") is p1)


def test_composition() -> None:
    print("\n=== Testing composition between Order and OrderLine ===")
    supplier = Supplier("S300", "OfficeMart", "orders@officemart.com")
    p1 = PhysicalProduct("P300", "Desk", 120.00, 10, 15.0, supplier)
    d1 = DigitalProduct("D300", "Antivirus", 39.90, 100, 800.0, supplier)

    # Order 1 with two products
    order1 = Order("O001")
    order1.add_order_line(p1, 2)
    order1.add_order_line(d1, 1)
    print("\nOrder 1:")
    order1.display_order()

    # Same product (p1) added to a different order
    order2 = Order("O002")
    order2.add_order_line(p1, 5)
    print("\nOrder 2:")
    order2.display_order()

    # Predict-first check: compare the objects
    line_in_order1 = order1.get_order_lines()[0]
    line_in_order2 = order2.get_order_lines()[0]
    print("\nSame OrderLine object?", line_in_order1 is line_in_order2)
    print("Same Product object?", line_in_order1.get_product() is line_in_order2.get_product())
    print("OrderLine ids:", id(line_in_order1), id(line_in_order2))
    print("Product ids:", id(line_in_order1.get_product()), id(line_in_order2.get_product()))

    # Remove an order line through the Order
    print("\nRemoving P300 from Order 1:")
    order1.remove_order_line("P300")
    order1.display_order()


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


def test_lsp() -> None:
    print("\n=== Testing LSP: substitutability of Product subclasses ===")
    supplier = Supplier("S400", "MegaStore", "contact@megastore.com")
    p1 = PhysicalProduct("P400", "Monitor", 299.99, 8, 4.2, supplier)
    d1 = DigitalProduct("D400", "Photo Editor", 79.00, 200, 1500.0, supplier)

    print("\nshow_product_details() with a PhysicalProduct:")
    show_product_details(p1)

    print("\nshow_product_details() with a DigitalProduct:")
    show_product_details(d1)

    print("\nBoth types in one Inventory, using normal operations:")
    inventory = Inventory()
    inventory.add_product(p1)
    inventory.add_product(d1)
    inventory.display_all()
    print("update_stock on physical:", inventory.update_stock("P400", 12))
    print("update_stock on digital:", inventory.update_stock("D400", 180))
    print("find_product D400:", inventory.find_product("D400") is d1)

if __name__ == "__main__":
    test_association()
    test_aggregation()
    test_composition()
    test_lsp()