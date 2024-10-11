from typing import Union
from datetime import datetime

class Base:
    def __init__(
        self,
        product_name: str,
        product_price: float,
        product_stock: int,
        product_weight: float
    ):
        self.product_name = product_name
        self.product_price = product_price
        self.product_stock = product_stock
        self.product_weight = product_weight
        self.date_added = "10/10/2024"

    def get_product_info(self) -> str:
        return f"Product Name: {self.product_name}, Price: ${self.product_price}, Stock: {self.product_stock}, Weight: {self.product_weight} kg, Date Added: {self.date_added}"

    def apply_price_discount(self, discount_percentage: Union[float, int]) -> None:
        self.product_price -= self.product_price * (discount_percentage / 100)

    def check_product_stock(self, quantity: int) -> str:
        if self.product_stock >= quantity:
            self.product_stock -= quantity
            return f"Order {quantity} units of {self.product_name}: Successful, Stock Remaining: {self.product_stock}"
        else:
            return "Not enough stock available"

    def calculate_shipping_charge(self) -> float:
        return self.product_weight * 10


class ElectronicItem(Base):
    def __init__(
        self,
        product_name: str,
        product_price: float,
        product_stock: int,
        product_weight: float,
        warranty_duration: int,
        brand_name: str
    ):
        super().__init__(product_name, product_price, product_stock, product_weight)
        self.warranty_duration = warranty_duration
        self.brand_name = brand_name

    def get_product_info(self) -> str:
        return f"Electronic Product: {self.product_name} (Brand: {self.brand_name}), Price: ${self.product_price}, Warranty: {self.warranty_duration} years, Stock: {self.product_stock}, Weight: {self.product_weight} kg, Date Added: {self.date_added}"

    def extend_warranty_duration(self, extra_years: int) -> str:
        self.warranty_duration += extra_years
        return f"Warranty extended to {self.warranty_duration} years for {self.product_name}"


class GroceryItem(Base):
    def __init__(
        self,
        product_name: str,
        product_price: float,
        product_stock: int,
        product_weight: float,
        expiration_date_str: str,
        is_product_perishable: bool
    ):
        super().__init__(product_name, product_price, product_stock, product_weight)
        self.expiration_date_str = expiration_date_str
        self.is_product_perishable = is_product_perishable

    def get_product_info(self) -> str:
        return f"Grocery Product: {self.product_name}, Price: ${self.product_price}, Expiration Date: {self.expiration_date_str}, Stock: {self.product_stock}, Weight: {self.product_weight} kg, Perishable: {self.is_product_perishable}, Date Added: {self.date_added}"

    def check_if_expired(self, current_date_str: str) -> bool:
        expiration_date = datetime.strptime(self.expiration_date_str, "%m/%d/%Y")
        current_date = datetime.strptime(current_date_str, "%m/%d/%Y")
        return current_date > expiration_date


laptop_item = ElectronicItem(
    product_name="Laptop",
    product_price=1500.0,
    product_stock=10,
    product_weight=2.5,
    warranty_duration=3,
    brand_name="Dell"
)

milk_item = GroceryItem(
    product_name="Milk",
    product_price=4.0,
    product_stock=50,
    product_weight=1.0,
    expiration_date_str="11/15/2024",
    is_product_perishable=True
)

print(laptop_item.get_product_info())
print(milk_item.get_product_info())

laptop_item.apply_price_discount(15)
print(f"After 15% discount:\n{laptop_item.get_product_info()}")
print(laptop_item.check_product_stock(5))
print(milk_item.check_product_stock(5))

print(f"Shipping cost for Laptop: ${laptop_item.calculate_shipping_charge()}")
print(f"Shipping cost for Milk: ${milk_item.calculate_shipping_charge()}")

print(laptop_item.extend_warranty_duration(2))
print(f"Is Milk expired? {milk_item.check_if_expired('10/10/2024')}")
