# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices
def apply_discount(prices):
    prices_copy = prices.copy()
    for index in range(len(prices_copy)):
        if prices_copy[index] > 2.00:
            prices_copy[index] = prices_copy[index] * 0.9
    return prices_copy
updated_prices = apply_discount(product_prices)

print(f"Updated product prices: {updated_prices}")