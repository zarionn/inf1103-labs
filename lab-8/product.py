from abc import ABC, abstractmethod
from supplier import Supplier


class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier) -> None:
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock
        self.__supplier: Supplier = supplier

    def get_product_id(self) -> str:
        return self.__product_id

    def update_stock(self, quantity: int) -> bool:
        if quantity < 0:
            print("Stock cannot be negative")
            return False
        self.__stock = quantity
        return True

    def display_information(self) -> None:
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}")

    def display_supplier(self) -> None:
        self.__supplier.display_information()

    def to_dict(self) -> dict:
        return {"ID": self.__product_id, "Name": self.__name, "Price": self.__price, "stock": self.__stock}

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass