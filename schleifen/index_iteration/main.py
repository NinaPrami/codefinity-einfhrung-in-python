prices = [29.99, 45.50, 12.75, 38.20]

for index in range(len(prices)):
    if index == 0:
        factor = 0.9
    elif index == 1:
        factor = 0.8
    elif index == 2:
        factor = 0.85
    elif index == 3:
        factor = 0.95
    prices[index] = prices[index] * factor
    print(f"Updated price for item {index}: ${prices[index]:.2f}")
  
    
