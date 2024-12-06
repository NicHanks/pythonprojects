user = ""
list = []

while user.lower() != "quit":
    user = input("say 'quit' to exit, \nWhat would you like to add to your shopping list? ")
    if user.lower() != "quit":
        list.append(user)

for i in range(len(list)):
    print(f"{i}.", list[i])

remove = int(input("Which item would you like to change? "))
new_item = input("What is the new item you would like to add? ")
list[remove] = new_item

for i in range(len(list)):
    print(f"{i}.", list[i])