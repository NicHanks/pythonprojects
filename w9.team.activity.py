print("Enter a list of numbers, type 0 when finished.")

numbers = []
new_number = ""

while new_number != 0:
    new_number = int(input("Enter number: "))
    if new_number != 0:
        numbers.append(new_number)
    
print(numbers)
sum = 0
average = 0
for i in numbers:
    sum += i
    average = sum / len(numbers)

biggest_number = 0
for i in numbers:    
    if i > biggest_number:
        biggest_number = i
    

print(f"The sum is: ", sum)
print(f"The average is: ", average)
print(f"The largest number is: ", biggest_number)
