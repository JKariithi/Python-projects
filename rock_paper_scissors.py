# Rock paper Scissors Game
from numpy import random

# Defining our constants
ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

#Dictionary for storing our variables
emojis = {
        ROCK: '🪨',
        PAPER: '📄',
        SCISSORS: '✂️'
    }
choices = tuple(emojis.keys()) # avoids repetition of the words

#Users choice fn
def get_user_choice():
    while True:
      user_choice = input("Rock, paper or Scissors (r/p/s) ?: ").lower()
      if  user_choice in choices:
          return user_choice
      else:
          print("Invalid choice") # better way of handling the error

# Display choices
def display_choices(user_choice, computer_choice):
    print(f"Your chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

#Determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie!")
    elif (user_choice == ROCK and computer_choice == SCISSORS) or (user_choice == SCISSORS and computer_choice == PAPER) or (user_choice == PAPER and computer_choice == ROCK):
        print("You win!")
    else:
        print("You lose!")

def playing_game():
 while True:
   user_choice = get_user_choice()

   computer_choice = random.choice(choices)

   display_choices(user_choice, computer_choice)

   determine_winner(user_choice,computer_choice)

   continue_playing = input("Continue (type 'n' to stop) ?: ").lower()
   if continue_playing == 'n':
        break

playing_game()




