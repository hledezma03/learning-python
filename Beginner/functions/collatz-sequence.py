def collatz(number):
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
    print(number, end=' ')
    return number


while True:
    try:
        num = int(input('Enter a positive integer: '))
        if num > 0:
            break
        else:
            print('Please enter a number greater than 0.')
    except ValueError:
        print('Please enter an integer.')

print(num, end=' ')
while num > 1:
    num = collatz(num)

print()