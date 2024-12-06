print("Welcome to the word guessing game!")
guess = "NA"
guesses = 0
word = "job"
print("Your hint is" )
word_length = len(word)
for j in range(word_length):
    print("_ ", end="")
while guess.lower() != word:    
    print()
    guess = input("What is your guess? ")
    guess = guess.lower()
    guess_length = len(guess)
    word_length = len(word)
    word_1 = word[0]
    word_2 = word[1]
    word_3 = word[2]
    print("Your hint is: ", end="")
    for i, letter in enumerate(guess):        
        if letter == word_1:            
            if i == 0:
                print(f"{word_1.upper()}", end="") 
            else:
                print(f"{word_1}", end="")           
        elif letter == word_2:
            if i == 1:
                print(f"{word_2.upper()}", end="") 
            else:
                print(f"{word_2}", end="") 
        elif letter == word_3:
            if i == 2:
                print(f"{word_3.upper()}", end="") 
            else:
                print(f"{word_3}", end="")                  
        else:
            print("_ ", end="" )
    print()
#    guess = len(guess)
#    if guess != "mormon":
#        print("Your hint is: ", end="")
#        for letter in guess:
#            for letter1 in word:
#                
#                elif letter == "o":
#                    print("o ", end="")
#                elif letter == "r":
#                    print("r ", end="")
#                elif letter == "m":
#                    print("m ", end="")
#                elif letter == "o":
#                    print("o ", end="")
#                elif letter == "n":
#                    print("n ", end="")
#                else:
#                    print("_ ", end="")

    guesses = guesses + 1
print("Congratulations! You guessed it! ")
print(f"It took you {guesses} guesses. ")











# play_again = "yes"
# while play_again.lower() == "yes":
#     word = "mosiah" 
#     guesses = 0   
#     guess = input("What is your guess? ")
#     guess = guess.lower()
#     word_letters = len(word)
#     guess_letters = len(guess)
#     if guess == word:
#         print(f"The word is {guess.upper()}! ")
#         print("Congratulations! You guessed it! ")
#         guess = guess + 1
#         print(f"It took you {guesses} guesses. ")
#     else:
#         print("Your hint is: ", end="")
#         for i, letter in enumerate(guess):
#             letter = guess[i]
            
#             print(f"{letter}", end="")
#         else:
#             print("")
#         print(f"The word is {guess.upper()}! ")
#         print("Congratulations! You guessed it! ")
#         guess = guess + 1
#         print(f"It took you {guesses} guesses. ")
#     play_again = input("Would you like to play again? ")
# print("Okay, hope you have a good Day! ")


# if letter == "m":
#     print("M", end="")
# elif letter == "o":
#     print("O", end="")
# elif letter == "r":
#     print("R", end="")
# elif letter == "m":
#     print("M", end="")
# elif letter == "o":
#     print("O", end="")
# elif letter == "n":
#     print("N", end="")
# else:
#     print("_")