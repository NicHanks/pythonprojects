# word = "commitment"

# favorite_letter = input("What is your favorite letter? ")

    # for i, letter in enumerate(word):
    #     if letter.lower() == favorite_letter.lower():
    #         print("_", end="")
#     else:
#         print(letter.lower(), end="")

phrase = ("""In coming days, it will not be possible to survive 
spiritually without the guiding, directing, comforting, 
and constant influence of the Holy Ghost.""")
again = "yes"
while again.lower() == "yes":
    number = int(input("please enter a number: "))

    for i, letter in enumerate(phrase):
        # Remember that the % operator divides by a number and returns the remainder.
        # So we can get eveery 3rd letter by dividing by 3 and looking for a remainder of 0,
        # or more generically, we can divide by the user's number. 
        if i % number == 0:
            print(letter.upper(), end="")
        else:
            print(letter.lower(), end="")
    #this puts a new line at the end of qoute
    print()
        
    again = input("Would you like to enter another number? ")
print("Goodbye")