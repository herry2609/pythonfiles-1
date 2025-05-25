# --------------------------------------------
# Data Types
# --------------------------------------------

integer_val = 10             # int
float_val = 3.14             # float
string_val = "Python"        # str
list_val = [1, 2, 3]         # list
bool_val = True              # bool

# --------------------------------------------
# if-elif-else with various operators
# --------------------------------------------

user_age = 20
has_id = True

if user_age >= 18 and has_id:
    print("Access granted.")
elif user_age >= 18 and not has_id:
    print("ID required for access.")
else:
    print("Access denied. You must be 18 or older.")

# --------------------------------------------
# Arithmetic and Assignment Operators
# --------------------------------------------

a = 8
b = 3

a += 2       # Now a = 10
result = a * b  # Multiplication
print("Arithmetic result:", result)

# --------------------------------------------
# Comparison and Logical Operators
# --------------------------------------------

x = 5
y = 5

if x == y or x > y:
    print("x is equal to or greater than y")

# --------------------------------------------
# Bitwise Operators
# --------------------------------------------

bitwise_result = x & y   # Both are 5 -> 0101 & 0101 = 0101
print("Bitwise AND result:", bitwise_result)

# --------------------------------------------
# Membership Operator
# --------------------------------------------

if 2 in list_val:
    print("2 is in the list")

# --------------------------------------------
# Identity Operator
# --------------------------------------------

list2 = list_val
list3 = [1, 2, 3]

print("list2 is list_val:", list2 is list_val)      # True
print("list3 is not list_val:", list3 is not list_val)  # True