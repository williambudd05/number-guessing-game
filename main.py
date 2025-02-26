import random

print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.""")



difficulty = input("""Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter your choice: """)

def play_game(max_guesses, difficulty_name):
    computer_number = random.randint(1, 100)
    print(f'''You have selected the difficulty level: {difficulty_name}
Lets Begin the game''')

    for i in range(max_guesses):
        guess = int(input('Enter your guess: '))
        if guess == computer_number:
            print('You guessed the correct number!')
            break
        elif guess < computer_number:
            print('Your guess is too low!')
        elif guess > computer_number:
            print('Your guess is too high!')
    else: print("Sorry, you couldn't guess the right number!, the answer was " + str(computer_number))


if difficulty == '1':
    play_game(10, difficulty)
elif difficulty == '2':
    play_game(5, difficulty)
elif difficulty == '3':
    play_game(3, difficulty)
else: print("Invalid choice, please choose a valid option!")
