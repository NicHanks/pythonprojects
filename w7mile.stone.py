print("Welcome to the word guessing game!")
guess = "_"
guesses = 0

while guess.lower() != "mormon":
    guess = input("What is your guess? ")
    if guess.lower() != "mormon":
        print("I'm sorry, please try again. ")
    guesses = guesses + 1
print("Congratulations! You guessed it! ")
print(f"It took you {guesses} guesses. ")