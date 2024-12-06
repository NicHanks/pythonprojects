print("For each of these questions, please provide a 1-10 rating:")

size = int(input("How large is the loan? "))
history = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
payment = int(input("How large is your down payment? "))

if size >= 5:
    if history >= 7 and history >= 7:
        loan = True
    elif (history >= 7 or income >= 7) and payment >= 5:
        loan = True
    else:
        loan = False
else:
    if history < 4:
        loan = False
    elif income >= 7 or payment >= 7:
        loan = True
    elif income >= 4 and payment >= 4:
        loan = True
    else:
        loan = False


if loan:
    print("Loan: Yes")
else:
    print("Loan: No")