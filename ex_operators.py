# --------------------------------------------
# 1. Arithmetic Operators
# --------------------------------------------

a = 10
b = 3

print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a / b)   # Division (float): 3.333...
print(a // b)  # Floor Division: 3
print(a % b)   # Modulus (remainder): 1
print(a ** b)  # Exponentiation: 10^3 = 1000

# --------------------------------------------
# 2. Comparison Operators
# --------------------------------------------

x = 5
y = 10

print(x == y)   # False, because 5 is not equal to 10
print(x != y)   # True, because 5 is not equal to 10
print(x > y)    # False
print(x < y)    # True
print(x >= y)   # False
print(x <= y)   # True

# --------------------------------------------
# 3. Logical Operators
# --------------------------------------------

a = True
b = False

print(a and b)   # False, because both are not True
print(a or b)    # True, because one is True
print(not a)     # False, because not True is False

# --------------------------------------------
# 4. Assignment Operators
# --------------------------------------------

x = 5
x += 2   # Same as x = x + 2
print(x) # 7

x -= 1   # Same as x = x - 1
print(x) # 6

x *= 2   # Same as x = x * 2
print(x) # 12

x /= 3   # Same as x = x / 3
print(x) # 4.0

x //= 2  # Same as x = x // 2
print(x) # 2.0

x %= 2   # Same as x = x % 2
print(x) # 0.0

x = 3
x **= 2  # Same as x = x ** 2
print(x) # 9

# --------------------------------------------
# 5. Bitwise Operators
# --------------------------------------------

a = 5       # 0101 in binary
b = 3       # 0011 in binary

print(a & b)  # AND: 0001 -> 1
print(a | b)  # OR: 0111 -> 7
print(a ^ b)  # XOR: 0110 -> 6
print(~a)     # NOT: -(5+1) = -6 (inverts all bits)
print(a << 1) # Left shift: 1010 -> 10
print(a >> 1) # Right shift: 0010 -> 2

# --------------------------------------------
# 6. Membership Operators
# --------------------------------------------

list1 = [1, 2, 3]

print(2 in list1)     # True, 2 is in the list
print(5 not in list1) # True, 5 is not in the list

# --------------------------------------------
# 7. Identity Operators
# --------------------------------------------

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # True, both refer to the same object
print(a is not c)  # True, different objects even with same content