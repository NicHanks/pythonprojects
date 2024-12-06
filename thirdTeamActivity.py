import random
from tkinter.messagebox import YES
play_again = "yes"

while play_again.lower() == "yes":
    
    number = random.randint(1, 100)

    times = 0
    guess = -1 
    
    while guess != number:
        guess = int(input("What is your guess? "))

        if guess > number:
            print("Lower")
        elif guess < number:
            print("Higher")
        else:
            print("You guessed it!")
        times = times + 1

    print(f"It took you {times} try(s)! ")
    play_again = input(f"""Would you like to play again? """)


print("Thanks for playing, see you again soon! ")