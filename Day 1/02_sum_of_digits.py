# Program 2: Sum of Digits
# Extract digits from a 3-digit number using // and % operators and calculate their sum.

# Take a 3-digit integer input from user
number = int(input("Enter a 3-digit number: "))

# Extract hundreds digit using floor division (//)
# Example: 123 // 100 = 1
hundreds = number // 100

# Extract tens digit using modulo (%) and floor division (//)
# Example: 123 % 100 = 23, then 23 // 10 = 2
tens = (number % 100) // 10

# Extract units digit using modulo (%)
# Example: 123 % 10 = 3
units = number % 10

# Calculate the sum of the extracted digits
digit_sum = hundreds + tens + units

# Display the individual digits and the final sum
print(f"Hundreds digit: {hundreds}")
print(f"Tens digit: {tens}")
print(f"Units digit: {units}")
print(f"Sum of digits ({hundreds} + {tens} + {units}): {digit_sum}")

