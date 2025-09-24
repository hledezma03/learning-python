user_input = int(input("Enter a number to calculate factorial: "))
total = 1
for i in range(1, user_input  + 1):
    total *= i
print(f'The result is {total}')