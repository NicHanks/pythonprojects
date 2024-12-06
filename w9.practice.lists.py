friends = []

new_friend = ""
while new_friend != "end":
    new_friend = input("Type the name of a friend: ")
    if new_friend != "end":
        friends.append(f"{new_friend}")

print("Your friends are: ")
for friend in friends:
    print(f"{friend}")