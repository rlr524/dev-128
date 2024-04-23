from product import Product

ice_cream = Product("Ice Cream - Chocolate", 3.99, 10)
taiyaki = Product("Taiyaki", 1.99, 15)

print("Product Data")
print(f"Name:               {ice_cream.name}")
print(f"Price:              ${ice_cream.price}")
print(f"Discount percent:   {ice_cream.discount_percent:d}%")
print(f"Discount amount:    ${ice_cream.get_discount_amount():.2f}")
print(f"Discount price:     ${ice_cream.get_discount_price():.2f}")
