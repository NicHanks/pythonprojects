can_ride = False

age = int(input("What is the age of the first rider? "))
height = int(input("What is the height of the first rider? "))

rider2 = input("Is there a second rider (yes/no)? ")
if rider2.lower() == "yes":
    age2 = int(input("What is the age of the second rider? "))
    height2 = int(input("What is the height of the second rider? "))
    if height < 36 or height2 < 36:
        can_ride = False
    else:
        if age >= 18 or age2 >= 18:
            can_ride = True
        else:
            can_ride = False
else:
    if age >= 18 and height > 62:
        can_ride = True
    else:
        can_ride = False

if can_ride:
    print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, but you may not ride this ride. ")

# if height < 36:
#     
# if height > 62 and age >= 18:
#     print("Welcome to the ride. Please be safe and have fun!")
# if rider2.lower() == "yes":
#     age2 = int(input("What is the age of the second rider? "))
# else:
#     if age2 >= 18:
#             
