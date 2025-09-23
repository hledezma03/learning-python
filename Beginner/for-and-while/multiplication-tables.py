print('Enter a number: ')
user_input = int(input('> '))

for i in range(1, 11):
    result = i * user_input
    print(f"{i} x {user_input} = {result}")
