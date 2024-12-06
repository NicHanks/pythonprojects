
choice1 = input("""You're walking through the halls when 
a cheerleader says "Hey there cute stuff..." Do you 
WALK AWAY or say, "hey there HOT STUFF." """)

if choice1.lower() == "walk away" :
    choice2 = input("""As you turn to leave, the door from the gym 
    opens and out comes her boyfriend, caption of 
    the football team... Shwooo. that could have been a bad! 
    Once you've made it out, what do you do? VIDEO GAMES or 
    NETFLIX?? """)

    if choice2.lower() == "video games":
        choice3 = input("""Right when you enter the front door 
        you plop down on the couch and that's when your
        mother says, "It's your turn to make the chicken 
        casserole!!" What do you do? 
        MAKE CHICKEN CASSEROLE, PASS, or DIP? """)

        if choice3.lower() == "make chicken casserole":
            print("""You plop down the 3lb chicken on the 
            cutting board and it looks up at you with 
            that look. The look of- please dont ki- 
            Swing! goes the hatchet and dinner is 
            served.  """)
        elif choice3.lower() == "pass":
            print("""You say pass and your mother 
            slips her sandal off her foot faster than you 
            can say never mind and wham! What a hit to the 
            head you just took! """)
        elif choice3.lower() == "dip":
            print("""You dip through the window out into the 
            cool night breeze and look up at the stars. """)
        else:
            print("Please try again... Something went wrong.")
    elif choice2.lower() == "netflix":
        choice3 = input("""Whipping out the phone spiderman into 
        spiderverse starts playing on netflix, it's nice, but the 
        Kardashians seems too intriguing to resist. It's 6pm 
        and the sun's about to go down, do you LEAVE, or let 
        AUTO PLAY do it's thing? """)
        if choice3.lower() == "leave":
            print("""It's hot outside and your walking 
            home when a guy in a van pulls up and says, "Hey!
            It's me, Billy. You want a ride home? It's your 
            friend Billy and you hop in and go to the 
            arcade with him. """)
        elif choice3.lower() == "auto play":
            print("""You get so caught up in the show that you 
            don't make it home until 3am. """)
        else:
            print("Please try agian... Something went wrong.")
    else:
        print("Please try agian... Something went wrong.")
elif choice1.lower() == "hot stuff": 
    choice2 = input("""She falls in love with you! You 
    get married and live happily ever after until one 
    day when you tell her it's aligator hunting season 
    but she doesn't want you to go! What do you do?
    Stay HAPPILY MARRIED or go ALIGATOR HUNTING? """)
    if choice2.lower() == "happily married":
        choice3 = input("""Well staying happily married is better 
        than aligator hunting, but you still feel sad that you 
        didn't get to go. The next hunting season comes and 
        instead of asking for permision, you ask for 
        forgiveness instead. But on your way back home the 
        guilt is eating up your inside so you go into a store
        to buy a aligator hunting hat, but there's two colors, 
        a PINK one and a BLUE one. Which one do you buy? """)
        if choice3.lower() == "pink":
            print("""She loves pink and forgets you even went
            aligator hunting! """)
        elif choice3.lower() == "blue":
            print("""She falls into your arms and tells you 
            how much she loves you but that if you go aligator 
            hunting one more time she is throwing out all of 
            your aligator hunting stuff out to the Good Will. """)
        else:
            print("Please try again... Something went wrong.")
    elif choice2.lower() == "aligator hunting":
        choice3 = input("""You go aligator hunting and when you're
        out there on the boat a big behemoth of a bahama moma 
        aligator comes out of the water and ends up jumping 
        right into your boat! What do you do?
        CHILL with it, or LOOK IT IN THE EYES? """)
        if choice3.lower() == "chill":
            print("""You sit down at the end of the boat and 
            don't make any sudden movements for hours, then, 
            when the sun starts to go down, it slowly taks one 
            step out of the boat and slowly eases back into 
            the water. """)
        elif choice3.lower() == "look it in the eyes":
            print("""You some how find the courage to look it
            in the eyes and as you do it becomes the most intense 
            stare-down battle you have ever had in your 
            entire life. But fly catches your attention so
            you blink and before you know the aligator is 
            on you and you jab it in the eyes with you two 
            fingers but then it rolls and drags you into 
            the water... """)
        else:
            print("Please try again... Something went wrong.")
    else:
        print("Please try again... Something went wrong.")
else:
    print("Please try again... Something went wrong.")