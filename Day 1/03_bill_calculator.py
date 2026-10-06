# Program 3: Simple Bill Calculator
# Calculate subtotal, 18% GST, and final bill amount based on price and quantity.

# Take item price and quantity as input
price = float(input("Enter item price: "))
quantity = int(input("Enter item quantity: "))

# Calculate subtotal
subtotal = price * quantity

# Calculate 18% GST (18 / 100 = 0.18)
gst = subtotal * 0.18

# Calculate final amount
final_amount = subtotal + gst

# Print bill details using f-strings
print("\n--- Bill Summary ---")
print(f"Price per item : {price}")
print(f"Quantity       : {quantity}")
print(f"Subtotal       : {subtotal}")
print(f"GST (18%)      : {gst}")
print(f"Final Amount   : {final_amount}")
