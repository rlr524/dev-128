from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    discount_percent: int

    def get_discount_amount(self):
        return self.price * self.discount_percent / 100

    def get_discount_price(self):
        return self.price - self.get_discount_amount()
