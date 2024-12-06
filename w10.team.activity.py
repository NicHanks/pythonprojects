bank_account = []
balance = []
#supposed to be balances, lol, don't have enough time to change. 

print("Enter the names and balances of bank accounts (type: quit when done)")

new_account = ""
while new_account.lower() != "quit":
    new_account = input("What is the name of this account? ")
    if new_account.lower() != "quit":
        bank_account.append(new_account)
        new_balance = float(input(f"What is the balance? "))
        balance.append(new_balance)

print
print("Account information: ")
for i, word in enumerate(bank_account):
    print(f"{word} - ${balance[i]}")

total = 0
for i in balance:
    total += i

average = total/len(balance)

highest_balance = 0
highest_account = ""
for i in balance:
    if i > highest_balance:
        highest_balance = i
        highest_account = bank_account[i]

print(f"Total: ${total:.2f}")
print(f"Average: ${average:.2f}")
print(f"Highest balance: {highest_account}: - ${highest_balance}")

change_account = "yes"

while change_account == "yes":
    change_account = input("\nDo you want to update an account? ")

    if change_account == "yes":
        index = int(input("What account index do you want to update? "))
        new_amount = float(input("What is the new amount? "))

        balance[index] = new_amount
    
    # Now print the balances
    print("\nAccount Information:")
    for i in range(len(bank_account)):
        print(f"{i}. {bank_account[i]} - ${balance[i]:.2f}")
