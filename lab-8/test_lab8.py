from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory


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

if __name__ == "__main__":
    test_association()
    test_aggregation()