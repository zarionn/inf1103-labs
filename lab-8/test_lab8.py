from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct


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


if __name__ == "__main__":
    test_association()