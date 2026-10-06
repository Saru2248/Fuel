# Program 1: Circle Calculator
# Calculate the area and circumference of a circle based on user input.

# Define constant value of PI
PI = 3.14

# Take radius input from user and convert to float (decimals allowed)
radius = float(input("Enter the radius of the circle: "))

# Calculate area and circumference using arithmetic operators
area = PI * radius * radius
circumference = 2 * PI * radius

# Display results using f-strings
print(f"Radius: {radius}")
print(f"Area of the circle: {area}")
print(f"Circumference of the circle: {circumference}")

