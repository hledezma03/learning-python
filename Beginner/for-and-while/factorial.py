def factorial(num):
    total = 1
    for i in range(1, num  + 1):
        total *= i
    print(f'The result is {total}')

user_input = int(input("Enter a number to calculate factorial: "))
factorial(user_input)
