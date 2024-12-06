###Ask the user for their grade percentage, then write a series of if-elif-else statements to print out the appropriate letter grade. (At this point, you'll have a separate print statement for each grade letter in the appropriate block.)
###Assume that you must have at least a 70 to pass the class. After determining the letter grade and printing it out. Add a separate if statement to determine if the user passed the course, and if so display a message to congratulate them. If not, display a different message to encourage them for next time.
###Change your code from the first part, so that instead of printing the letter grade in the body of each if, elif, or else block, instead create a new variable called letter and then in each block, set this variable to the appropriate value. Finally, after the whole series of if-elif-else statements, have a single print statement that prints the letter grade once.


percentage = float(input("What is your grade percentage? "))

if percentage >= 90:
    if percentage >= 97:
        print("You got an A+!")
    elif percentage < 93:
        print("You got an A-.")
    else:
        print("You got an A.")
elif percentage >= 80:
    if percentage >= 87:
        print("You got a B+.")
    elif percentage < 83:
        print("You got a B-.")
    else:
        print("You got a B.")
elif percentage >= 70:
    if percentage >= 87:
        print("You got a c+.")
    elif percentage < 83:
        print("You got a c-.")
    else:
        print("You got a c.")
elif percentage >= 60:
    if percentage >= 87:
        print("You got a D+.")
    elif percentage < 83:
        print("You got a D-.")
    else:
        print("You got a D.")
else :
    print("You got a F.")

sign = ""

remainder = percentage % 10

if remainder >= 7:
    sign = "+"
if percentage >= 70:
    print("You passed!")
else:
    print("Better luck next time!")


#     File: teach05_stretch_sample.py
# Author: Brother Burton

# Purpose: Determine and display letter grades, including +/-.
# """

# grade = int(input("What is your grade percent? "))

# if grade >= 90:
#     letter = "A"
# elif grade >= 80:
#     letter = "B"
# elif grade >= 70:
#     letter = "C"
# elif grade >= 60:
#     letter = "D"
# else:
#     letter = "F"

# # Stretch Challenge 1
# sign = ""

# last_digit = grade % 10

# if last_digit >= 7:
#     sign = "+"
# elif last_digit < 3:
#     sign = "-"
# else:
#     sign = ""

# # Stretch Challenge 2
# if grade >= 93:
#     sign = ""

# # Stretch Challenge 3
# if letter == "F":
#     sign = ""

# print(f"Your letter grade is: {letter}{sign}")

# if grade >= 70:
#     print("Congratulations! You passed the class!")
# else:
#     print("Stay focused and you'll get it next time!")
