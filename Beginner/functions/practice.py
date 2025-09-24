'''
1.  Why are functions advantageous to have in your programs?
A = Because we can use it every time we want without retyping our code, the functions are also easier to update and make our code more readable
  2.  When does the code in a function execute: when the function is defined or when the function is called?
A = When the function is called
  3.  What statement creates a function?
A = def + name of the function + ()
  4.  What is the difference between a function and a function call?
A = A function is the code we write and what it is going to be execute while a function call is when we name the function and excute the code inside it
  5.  How many global scopes are there in a Python program? How many local scopes are there?
A = There is one global scope and as much local scopes as functions we have
  6.  What happens to variables in a local scope when the function call returns?
A = The variable is given as a result of calling the function
  7.  What is a return value? Can a return value be part of an expression?
A = It is the value a function give as a response and yes it can be part of an expression
  8.  If a function does not have a return statement, what is the return value of a call to that function?
A = None
  9.  How can you force a variable in a function to refer to the global variable?
A = with the global statement
10.  What is the data type of None?
A = it has no value
11.  What does the import areallyourpetsnamederic statement do?
A = I do not understand this question
12.  If you had a function named bacon() in a module named spam, how would you call it after importing spam?
A = spam.bacon()
13.  How can you prevent a program from crashing when it gets an error?
A = using try-except
14.  What goes in the try clause? What goes in the except clause?
A = What we want to execute when there are no errors
15.  Write the following program in a file named notrandomdice.py and run it. Why does each function call return the same number?
import random
random_number = random.randint(1, 6)

def get_random_dice_roll():
    # Returns a random integer from 1 to 6
    return random_number

print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())

A = Because we are assigning the value of the variable in a global scope so it's value doesn't change when we call the function




Answers by ChatGPT
1. Why are functions advantageous to have in your programs?
✅ Because they let us reuse code without retyping it, make programs easier to read, test, and update.

2. When does the code in a function execute: when the function is defined or when the function is called?
✅ The code executes only when the function is called.

3. What statement creates a function?
✅ The def statement, for example:

def my_function():
    pass


4. What is the difference between a function and a function call?
✅ A function is the definition (the block of code). A function call is when you use the function’s name (with parentheses) to run that code.

5. How many global scopes are there in a Python program? How many local scopes are there?
✅ One global scope. Each function call creates its own local scope, so there can be many local scopes.

6. What happens to variables in a local scope when the function call returns?
✅ They are destroyed (forgotten). Local variables exist only while the function is running.

7. What is a return value? Can a return value be part of an expression?
✅ It is the value a function gives back when it finishes. Yes, return values can be used inside expressions.

8. If a function does not have a return statement, what is the return value of a call to that function?
✅ None.

9. How can you force a variable in a function to refer to the global variable?
✅ By declaring it with the global statement.

10. What is the data type of None?
✅ Its type is NoneType.

11. What does the statement import areallyourpetsnamederic do?
✅ It tries to import a module named areallyourpetsnamederic. Since it doesn’t exist, Python raises an ImportError.

12. If you had a function named bacon() in a module named spam, how would you call it after importing spam?
✅ spam.bacon()

13. How can you prevent a program from crashing when it gets an error?
✅ By using a try/except block to handle errors gracefully.

14. What goes in the try clause? What goes in the except clause?
✅

try: the code that might cause an error.

except: the code that runs if an error happens.

15. Why does each function call in the following program return the same number?

import random
random_number = random.randint(1, 6)

def get_random_dice_roll():
    return random_number

print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())


✅ Because random.randint(1, 6) was executed once at the top of the program, storing a single random value in the global variable random_number. The function just returns that fixed value every time.

👉 To make it random on each call, you should move the random.randint() inside the function:

import random

def get_random_dice_roll():
    return random.randint(1, 6)
'''