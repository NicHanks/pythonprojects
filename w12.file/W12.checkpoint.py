people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]


age = 999

for person in people:
    person = person.strip()
    person = person.split()
    yperson = person[0]
    yage = person[1]
    yage = int(yage)
    if age > yage:
        age = yage
        name = yperson

print(f"{name} is {age} which is the youngest of the group")