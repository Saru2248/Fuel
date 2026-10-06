# Program 4: Time Converter
# Convert total seconds into hours, minutes, and remaining seconds using // and % operators.

# Take total seconds as input from user
total_seconds = int(input("Enter total seconds: "))

# 1 hour = 3600 seconds
hours = total_seconds // 3600

# Remaining seconds after extracting hours
remaining_seconds = total_seconds % 3600

# 1 minute = 60 seconds
minutes = remaining_seconds // 60

# Remaining seconds after extracting minutes
seconds = remaining_seconds % 60

# Display the converted time using f-strings
print(f"{total_seconds} seconds = {hours} hour(s), {minutes} minute(s), {seconds} second(s)")
