# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started")
for item_name, data in inventory.items():
    current_stock, minimum_stock, restock_quantity, on_sale = data
    while current_stock < minimum_stock:
        current_stock += restock_quantity
        inventory[item_name][0] = current_stock
    print("Processing", item_name) 
    if current_stock > discount_threshold and on_sale == False:
        inventory[item_name][3] = True

print("Processing completed")
    
    