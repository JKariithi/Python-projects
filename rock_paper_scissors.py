# Rock paper Scissors Game
from numpy import random


emojis = {
        'r': '🪨',
        'p': '📄',
        's': '✂️'
    }
choices = ('r','p','s')

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
    elif (user_choice == 'r' and computer_choice == 's') or (user_choice == 's' and computer_choice == 'p') or (user_choice == 'p' and computer_choice == 'r'):
        print("You win!")
    else:
        print("You lose!")

def playing_game():
 while True:
   user_choice = get_user_choice()

   computer_choice = random.choice(choices)

   display_choices(user_choice, computer_choice)

   determine_winner(user_choice,computer_choice)

   continue_playing = input("Continue (y/n) ?: ").lower()
   if continue_playing == 'n':
        break

playing_game()




