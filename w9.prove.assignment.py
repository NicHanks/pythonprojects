print("Welcome to the Shopping Cart Program! ")
print()

list = []
cost_list = []
action = 0
while action != 5:
    if action == 0:
        print("""Please select one of the following: 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit""")
        action = int(input("Please enter an action: "))

    if action == 1:
        new_item = input("What Item would you like to add? ")
        list.append(new_item)
        cost_list.append(float(input("What is the cost of the item? ")))
        print(f"'{new_item}' has been added to the cart. ")
        action = 0
        print()
    elif action == 2:
        print("The contents of the shopping cart are: ")
        for item in list:
            print(item)
        action = 0
        print()
    elif action == 3:
        item_remove = input("What item would you like removed? ")
        for item in list:
            if item == item_remove:
                list.remove(item_remove)
            else:
                print("Sorry, unable to find that item. ")
        print("Item removed.")
        action = 0
        print()
    elif action == 4:
        sum = 0
        for item in cost_list:
            item = int(item)
            sum += item
        print(f"The total is: {sum}")
        action = 0
        print() 
    elif action == 5:
        print("Thank you. Goodbye.")
        print()
    else:
        print("I'm sorry I didn't understand that one. ")
        action == 0
        print()


