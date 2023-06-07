import random

MIN_NUMBER = 1
MAX_NUMBER = 99

print("Think of a number between 1 and 99.")

# Generate a random number between 1 and 99
guess = random.randint(MIN_NUMBER, MAX_NUMBER)

print(f'Is it {guess}?')

# Loop until the correct number is guessed
while True:
    user_input = input("Enter 'l' if the number is lower, 'h' if it's higher, or 'c' if it's correct: ")

    if user_input == 'l':
        MAX_NUMBER = guess - 1
        guess = random.randint(MIN_NUMBER, MAX_NUMBER)

    elif user_input == 'h':
        MIN_NUMBER = guess + 1
        guess = random.randint(MIN_NUMBER, MAX_NUMBER)

    elif user_input == 'c':
        print("Congratulations! You guessed the number.")
        break

    else:
        print("Invalid input. Please enter 'l', 'h', or 'c'.")
    
    print(f'Is it {guess}?')
    
    
