people = ["Christopher", "Susan"]

print()
for name in people:
    print(name)

index = 0
while index < len(people):
    print(people[index])
    index = index + 1

print()

#example
first_name = "Brigham"
total_letters = len(first_name)

for i in range(total_letters):
    letter = first_name[i]
    print(f"The letter is: {letter}")

colors = ["red", "blue", "green", "yellow"]

for i in colors:
    print(i)

for i in range(1, 9):
   print(i)

for i in range(2, 22, 2):
    print(i)


for i, letter in enumerate(first_name):
    print(f"The letter {letter} is at position {i}")