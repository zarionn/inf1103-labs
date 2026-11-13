from supplier import Supplier
from physical_product import PhysicalProduct
from order import Order
from bulk_discount import BulkDiscount
from percentage_discount import PercentageDiscount
from student_discount import StudentDiscount


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


if __name__ == "__main__":
    test_strategy()