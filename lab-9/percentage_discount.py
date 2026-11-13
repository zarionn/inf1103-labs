from discount_strategy import DiscountStrategy

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float) -> None:
        self.__percentage: float = percentage

    def apply(self, total: float) -> float:
        discount_amount = total * (self.__percentage / 100)
        return total - discount_amount