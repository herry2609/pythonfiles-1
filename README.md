# pythonfiles-1
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