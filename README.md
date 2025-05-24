# pythonfiles-1
#----------------------------------------------------------------------
Python Operators :-  
Python provides a variety of operators that allow you to perform operations on variables and values. Operators are categorized based on the type of operations they perform.
#----------------------------------------------------------------------
# 1. Arithmetic Operators :- 
Used for basic mathematical operations:-

| Operator | Description         | Example  |
| -------- | ------------------- | -------- |
| `+`      | Addition            | `a + b`  |
| `-`      | Subtraction         | `a - b`  |
| `*`      | Multiplication      | `a * b`  |
| `/`      | Division            | `a / b`  |
| `//`     | Floor Division      | `a // b` |
| `%`      | Modulus (remainder) | `a % b`  |
| `**`     | Exponentiation      | `a ** b` |
#----------------------------------------------------------------------
# 2. Comparison Operators :-
Compare values and return True or False:-

| Operator | Description      | Example  |
| -------- | ---------------- | -------- |
| `==`     | Equal to         | `a == b` |
| `!=`     | Not equal to     | `a != b` |
| `>`      | Greater than     | `a > b`  |
| `<`      | Less than        | `a < b`  |
| `>=`     | Greater or equal | `a >= b` |
| `<=`     | Less or equal    | `a <= b` |
#----------------------------------------------------------------------
# 3. Logical Operators :-
Used to combine conditional statements :-

| Operator | Description                      | Example            |
| -------- | -------------------------------- | ------------------ |
| `and`    | True if both conditions are True | `a > 5 and b < 10` |
| `or`     | True if at least one is True     | `a > 5 or b < 10`  |
| `not`    | Reverses the condition           | `not(a > 5)`       |
#----------------------------------------------------------------------
# 4. Assignment Operators :-
Assign values to variables :-

| Operator | Description         | Example   |
| -------- | ------------------- | --------- |
| `=`      | Assign              | `a = 5`   |
| `+=`     | Add and assign      | `a += 1`  |
| `-=`     | Subtract and assign | `a -= 1`  |
| `*=`     | Multiply and assign | `a *= 2`  |
| `/=`     | Divide and assign   | `a /= 2`  |
| `//=`    | Floor divide assign | `a //= 2` |
| `%=`     | Modulus and assign  | `a %= 3`  |
| `**=`    | Power and assign    | `a **= 2` |
#----------------------------------------------------------------------
# 5. Bitwise Operators :-
Operate on binary representations :-

| Operator | Description | Example  |     |     |
| -------- | ----------- | -------- | --- | --- |
| `&`      | AND         | `a & b`  |     |     |
| \`       | \`          | OR       | \`a | b\` |
| `^`      | XOR         | `a ^ b`  |     |     |
| `~`      | NOT         | `~a`     |     |     |
| `<<`     | Left Shift  | `a << 1` |     |     |
| `>>`     | Right Shift | `a >> 1` |     |     |
#----------------------------------------------------------------------
# 6. Membership Operators :-
Test for membership in a sequence :-

| Operator | Description       | Example            |
| -------- | ----------------- | ------------------ |
| `in`     | True if found     | `'a' in 'abc'`     |
| `not in` | True if not found | `'z' not in 'abc'` |
#----------------------------------------------------------------------
# 7. Identity Operators :-
Compare memory locations of objects :-

| Operator | Description          | Example      |
| -------- | -------------------- | ------------ |
| `is`     | True if same object  | `a is b`     |
| `is not` | True if not same obj | `a is not b` |


# IF - ELSE (Conditional statements):
#----------------------------------------------------------------------
Conditional statements in Python allow the program to execute certain pieces of code based on whether a condition is True or False. They help in decision-making processes.
#----------------------------------------------------------------------
Basic Structure :- 

if condition:
    # code block executed if condition is True
if, elif, and else
# code
x = 10

if x > 0:
    print("Positive number")
elif x == 0:
    print("Zero")
else:
    print("Negative number")

#----------------------------------------------------------------------

if: Checks the initial condition.
elif: (short for "else if") Checks another condition if the previous one was False.
else: Executes when none of the above conditions are True.

#----------------------------------------------------------------------
Nested Conditions :- 
# code
x = 5
if x > 0:
    if x < 10:
        print("Single-digit positive number")
#----------------------------------------------------------------------
Logical Operators :-
and, or, not can be used to combine conditions:

# code
if age > 18 and has_id:
    print("Access granted")
#----------------------------------------------------------------------
Ternary Conditional (One-liner) :- 
# code
result = "Even" if num % 2 == 0 else "Odd"
#----------------------------------------------------------------------