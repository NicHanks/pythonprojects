positive_number = int(input("Please type a positive number. "))

while positive_number < 0:
    print("Sorry, that is a negative number. Please try again.")
    positive_number = int(input("Please type a positive number. "))

print(f"The positive number is: {positive_number}")

# candy = input("May I have a piece of candy? ")

# while candy.lower() != "yes":
#     candy = input("May I have a piece of candy? ")

# print("Thank you.")