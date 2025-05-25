# 1. Example of if and else

# Check if a number is even or odd

number = 7  # You can change this number

if number % 2 == 0:
    print("The number is even.")  # This line runs if the condition is True
else:
    print("The number is odd.")   # This line runs if the condition is False

# 2. Example of if, elif, and else

# Categorize a number as positive, negative, or zero

number = -3  # Try changing this value

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

# 3. Example of Nested if-else

# Check if a number is positive and further check if it is even or odd

number = 4  # Test with different values

if number > 0:
    print("The number is positive.")
    if number % 2 == 0:
        print("It is also even.")
    else:
        print("It is also odd.")
else:
    print("The number is not positive.")

# 4. Example with Combined Conditions (and, or, not)

# Check if a user can access a service based on age and ID status

age = 20         # Age of the user
has_id = True    # Whether the user has an ID

# The user gets access only if they are older than 18 AND have an ID
if age > 18 and has_id:
    print("Access granted.")
else:
    print("Access denied.")