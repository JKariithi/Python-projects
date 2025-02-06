# Rock paper Scissors Game
from numpy import random

#using a loop for the Game
while True:
    user_choice = input("Rock, paper or Scissors (r/p/s) ?: ").lower()
    computer_choice = random.choice(['r','p','s'])

    # For user's choice
    if user_choice == 'r':
        print("You chose r")
    elif user_choice == 's':
        print("You chose s")
    elif user_choice == 'p':
        print("You chose p")
    else:
        print("Invalid choice")
        continue

    #For computer's choice
    if computer_choice == 'r':
        print("Computer chose r")
    elif computer_choice == 's':
        print("Computer chose s")
    else:
        print("Computer chose p")

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





