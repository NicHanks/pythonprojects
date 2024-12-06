adjective = input("adjective: ")
animal = input("animal: ")
verb = input("verb: ")
exclamation = input("exclamation: ")
verb2 = input("verb: ")
verb3 = input("verb: ")
adjective2 = input("adjective: ")
celebrity = input("Enter the name of a celebrity: ")
aunt_name = input("What is your aunts name? ")
color = input("color: ")

#I used single quotes (') because of the exlamation variable with quotes. 
print(f'''The other day, I was really in trouble. It all started when I saw a very 
{adjective} {animal} {verb} down the hallway. "{exclamation.capitalize()}!" I yelled. But all
I could think to do was to {verb2} over and over. Miraculously, 
that caused it to stop, but not before it tried to {verb3} 
right in front of my family. \t
We were all shocked as it left us and rounded the corner, 
but soon after my Aunt {aunt_name} started to chase after it! 
As I followed her in hot pursuit, I began to round the corner 
and to my suprise I found {celebrity} picking up the {animal}! 
That is when I turned to see Aunt {aunt_name} pulling three 
apples {adjective2} out of her {color} purse and giving them 
to us. And that is when I knew that that was the best 
family vacation I have ever been on! ''')