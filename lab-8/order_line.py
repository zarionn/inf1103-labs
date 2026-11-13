from product import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int) -> None:
        self.__quantity: int = quantity
        self.__product: Product = product

    def get_product(self) -> Product:
        return self.__product

    def calculate_subtotal(self) -> float:
        return self.__product.get_price() * self.__quantity

    def display_information(self) -> None:
        print(f"Product ID: {self.__product.get_product_id()} | Quantity: {self.__quantity} | Subtotal: ${self.calculate_subtotal():.2f}")