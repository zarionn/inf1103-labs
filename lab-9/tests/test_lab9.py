from supplier import Supplier
from physical_product import PhysicalProduct
from order import Order
from bulk_discount import BulkDiscount
from percentage_discount import PercentageDiscount
from student_discount import StudentDiscount
from product_factory import ProductFactory
from product_loader import load_products
from inventory import Inventory


def test_strategy() -> None:
    print("=== Testing Strategy pattern: discounts on an Order ===")
    supplier = Supplier("S100", "TechCorp", "sales@techcorp.com")
    p1 = PhysicalProduct("P100", "Desk", 100.00, 10, 15.0, supplier)
    p2 = PhysicalProduct("P101", "Chair", 50.00, 10, 6.0, supplier)

    order = Order("O001", BulkDiscount(200, 20))
    order.add_order_line(p1, 2)   # 200
    order.add_order_line(p2, 1)   # 50  -> lines add up to 250

    print("Total with BulkDiscount(200, 20):", order.calculate_total())

    order.set_discount(PercentageDiscount(10))
    print("Total after set_discount(PercentageDiscount(10)):", order.calculate_total())

    order.set_discount(StudentDiscount())
    print("Total after set_discount(StudentDiscount()):", order.calculate_total())

def test_factory() -> None:
    print("\n=== Testing ProductFactory with an unknown type ===")
    supplier = Supplier("S200", "ServiceCo", "help@serviceco.com")
    try:
        ProductFactory.create("service", "S001", "Installation", 30.00, 5, supplier)
    except ValueError as error:
        print("ValueError caught:", error)


def test_load_products() -> None:
    print("\n=== Testing load_products with products.csv ===")
    supplier = Supplier("S300", "CSV Supplies", "csv@supplies.com")
    inventory = Inventory()
    load_products("products.csv", inventory, supplier)
    inventory.display_all()

    print("\n=== Testing load_products with a missing file ===")
    load_products("missing_products.csv", Inventory(), supplier)


if __name__ == "__main__":
    test_strategy()
    test_factory()
    test_load_products()