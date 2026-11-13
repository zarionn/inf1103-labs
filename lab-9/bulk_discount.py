from discount_strategy import DiscountStrategy

class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: float, discount_amount: float) -> None:
        self.__threshold: float = threshold
        self.__discount_amount: float = discount_amount

    def apply(self, total: float) -> float:
        if total >= self.__threshold:
            return total - self.__discount_amount
        return total