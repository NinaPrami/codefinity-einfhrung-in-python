def apply_discount(price, discount=0.05):
    price *= (1 - discount)
    return price
def apply_tax(price, tax=0.07):
    price *= (1 + tax)
    return price
def calculate_total(price, discount=0.05, tax=0.07):
    discounted_price = apply_discount(price, discount)
    final_price = apply_tax(discounted_price, tax)
    return final_price

total_price_default = calculate_total(120)
print(f"Total cost with default discount and tax: ${total_price_default}")

total_price_custom = calculate_total(100, discount=0.10, tax=0.08)
print(f"Total cost with custom discount and tax: ${total_price_custom}")
