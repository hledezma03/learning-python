import random



secret_number = random.randint(1, 20)
while True:
    try:
        user_guess = int(input("Enter a number between 1-20: "))
    except ValueError:
        print("You should enter a number between 1 and 20: ")
        continue
    if user_guess < 1 or user_guess > 20:
        print("Please enter a number between 1 and 20!")
        continue
    else:
        if secret_number == user_guess:
            print("Excellent that was the right number!")
            break
        elif user_guess > secret_number:
            print("Nice try the secret number is lower")
        else:
            print("Nice try the secret number is higher")