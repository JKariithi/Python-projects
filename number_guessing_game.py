from numpy import random


# loop over everything
i = 1 
number = random.randint(1,100)
while i <= 6:
    # make sure we only have integers
    try:
        guess = int(input("Guess the number between 1 and 100: "))
        if guess > number:
            print("Your guess is too high")
        elif guess < number:
            print("Your guess is too low")
        else:
            print("Congratulations! you guessed the correct number")
            break
    except ValueError:
        print("Invalid input. Please enter an integer")
    i += 1
print(f"\n The correct answer is {number}")
