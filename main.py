import random

print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.""")

difficulty = input("""Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter your choice: """)

def game(level):
    if level == '1':
        computer_number = random.randint(1,100)
        max_guess = 10
        guesses = 0
        print('''You have selected the easy difficulty!
        Lets get started!''')
        while guesses <= max_guess:
            guess = int(input('Enter your guess: '))
            if guess == computer_number:
                print('You got it!', computer_number)
                break

            elif guess < computer_number:
                print(f'Incorrect!The number is greater than {guess}.')
                guesses += 1
            elif guess > computer_number:
                print(f'Incorrect!The number is less than {guess}.')
                guesses += 1



game(difficulty)