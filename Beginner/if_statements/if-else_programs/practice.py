'''
Practice Questions
  1.  What are the two values of the Boolean data type? How do you write them?
A = True and False

  2.  What are the three Boolean operators?
A = not, and, or

  3.  Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
True and True = True
True and False = False
False and True = False
False and False = False

  4.  What do the following expressions evaluate to?

(5 > 4) and (3 == 5) A = False
not (5 > 4) A = False
(5 > 4) or (3 == 5) A = True
not ((5 > 4) or (3 == 5)) A = False
(True and True) and (True == False) A = False
(not False) or (not True) A = True
  5.  What are the six comparison operators?
==, !=, <, >, <=, >=
  6.  What is the difference between the equal to operator and the assignment operator?
The equal operator compares the left expression to the right one while the assigment operator assigns the value in the right side to the variable in the left
  7.  Explain what a condition is and where you would use one.
A condition is an expression that will validate if it is true or false to excute a piece of code or not
  8.  Identify the three blocks in this code:

spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
       print('bacon')
    else:
        print('ham')
    print('spam')
print('Done')

A = The first block is print eggs if spam == 10, the second it's print bacon if spam is greater than 5 and the third block is print ham if neither of the past conditions are true and finally print Done

  9.  Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
'''
spam = 0
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')