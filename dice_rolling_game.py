from numpy import random

while True:
    # asking for permission to play the game adn making sure the inputs are in lower case
    user_input = input("Roll the dice (y/n): ")
    # if input is y roll the dice
    if user_input == "y":
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"({die1},{die2})")
    elif user_input == 'n':
        print("Thanks for playing")
        break 
    else:
        print("Invalid input")







