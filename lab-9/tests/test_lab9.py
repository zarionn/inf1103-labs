from supplier import Supplier
from physical_product import PhysicalProduct
from order import Order
from bulk_discount import BulkDiscount
from percentage_discount import PercentageDiscount
from student_discount import StudentDiscount
from product_factory import ProductFactory
from product_loader import load_products
from inventory import Inventory
from order_line import OrderLine
import builtins
from main import get_positive_float



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

def test_validation() -> None:
    print("\n=== Testing validation ===")
    supplier = Supplier("S400", "CheckCo", "check@co.com")

    try:
        PhysicalProduct("P900", "Bad Price", -10.00, 5, 1.0, supplier)
    except ValueError as error:
        print("Negative price rejected:", error)

    try:
        PhysicalProduct("P901", "Bad Stock", 10.00, -3, 1.0, supplier)
    except ValueError as error:
        print("Negative stock rejected:", error)

    good = PhysicalProduct("P902", "Good", 10.00, 5, 1.0, supplier)
    try:
        good.update_stock(-1)
    except ValueError as error:
        print("Negative stock update rejected:", error)

    try:
        OrderLine(good, 0)
    except ValueError as error:
        print("Zero order quantity rejected:", error)


def test_get_positive_float() -> None:
    print("\n=== Testing get_positive_float with abc, -5, 12.50 ===")
    answers = iter(["abc", "-5", "12.50"])
    original_input = builtins.input
    builtins.input = lambda prompt="": next(answers)
    try:
        result = get_positive_float("Price: ")
        print("Returned:", result)
    finally:
        builtins.input = original_input

if __name__ == "__main__":
    test_strategy()
    test_factory()
    test_load_products()
    test_validation()
    test_get_positive_float()