# Input variables
product_type = "Dairy"  
day_of_week = "Wednesday"
if product_type == "Fruits":
    if day_of_week == "Monday":
        print("10% discount on Fruits today!")
    else:
        print("No special discounts today.")
elif product_type == "Vegetables":
    if day_of_week == "Tuesday":
        print("15% discount on Vegetables today!")
    else:
        print("No special discounts today.")
elif product_type == "Dairy":
    if day_of_week == "Wednesday":
        print("20% discount on Dairy today!")
    else:
        print("No special discounts today.")
elif product_type == "Other":
    print("No discount available.")
else:
    print("No special discounts today.")