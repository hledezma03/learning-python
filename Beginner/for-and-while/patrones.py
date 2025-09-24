def print_square(size):
    for i in range(size):
        print('* ' * size)

def print_triangle(size):
    for i in range(1, size + 1):
        print(' ' * (size - i) + '* ' * i)

def print_pyramid(size):
    for i in range(1, size + 1):
        if i == 1:
            print(' ' * (size - i) + '*')
        elif i == size:
            print('* ' * size)
        else:
            print(' ' * (size - i) + '*' + ' ' * (2*i - 3) + '*')




patron = input('Which patron do you want? Square (s), Triangle (t), Piramid (p): ')
size = int(input('How many * do you want to use? '))

while True:
    if patron == 's':
        print_square(size)
        break
    elif patron == 't':
        print_triangle(size)
        break
    elif patron == 'p':
        print_pyramid(size)
        break
    else:
        print('Select a patron. For square enter (s), for triangle enter (s) and for pyramid enter (p): ')
        patron = input('>')
