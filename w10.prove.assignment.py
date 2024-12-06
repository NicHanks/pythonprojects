print("Welcome to the Shopping Cart Program! ")

list = []
cost_list = []
action = 0
while action != 5: 
    print()  
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
        
    elif action == 2:
        print("The contents of the shopping cart are: ")
        for i in range(len(list)):
            new_i = i + 1
            print(f"{new_i}. {list[i]} - ${cost_list[i]:.2f}")
        
    elif action == 3:
        item_remove = int(input("Whih item would you like to remove? "))
        item_remove -= 1
        list.pop(item_remove)
        cost_list.pop(item_remove)
        print("Item removed.")
        
    elif action == 4:
        sum = 0
        for item in cost_list:
            sum += item
        print(f"The total is: {sum:.2f}")
         
    elif action == 5:
        print("Thank you. Goodbye.")
        


