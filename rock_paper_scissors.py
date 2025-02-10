# Rock paper Scissors Game
from numpy import random

#using a loop for the Game
while True:
    emojis = {
        'r': '🪨',
        'p': '📄',
        's': '✂️'
    }
    choices = ('r','p','s')
    user_choice = input("Rock, paper or Scissors (r/p/s) ?: ").lower()
    if  user_choice not in choices:
        print("Invalid choice") # better way of handling the error
        continue
    
    computer_choice = random.choice(choices)

    #Printing out the choices of the user and computer
    print(f"Your chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("Tie!")
    elif (user_choice == 'r' and computer_choice == 's') or (user_choice == 's' and computer_choice == 'p') or (user_choice == 'p' and computer_choice == 'r'):
        print("You win!")
    else:
        print("You lose!")

    # ask if they want to continue
    continue_playing = input("Continue (y/n) ?: ").lower()
    if continue_playing == 'n':
        break





