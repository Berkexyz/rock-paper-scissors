import random

options = ['rock', 'paper', 'scissors']

computer = random.choice(options)
user = input('What is your choice? Rock, Paper, or Scissors? ').lower()

if user not in options:
    print("Invalid input! Please choose either 'Rock', 'Paper', or 'Scissors'.")
else:
    print(f"Computer choice is {computer.capitalize()}")
    if computer == user:
        print('Draw!')
    elif (computer == 'rock' and user == 'scissors') or \
            (computer == 'paper' and user == 'rock') or \
            (computer == 'scissors' and user == 'paper'):
        print('Computer won!')
    else:
        print('User won!')







