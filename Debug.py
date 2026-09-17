
name = input("What's your name, Guardian?").title()
gear_name = input("What gear do you want")

price = 12
quantity = input("How many would you like?")

remaining_stock = quantity - 1

subtotal = price * quantity

shipping_fee = 5
total = subtotal - shipping_fee
print("Hello," + name + "! Here's your order:")
print("Item: " + gear_name)
print("Quantity: " + str(quantity))
print
print