user_budget = int(input("Please enter your budget in this month: RM"))
Expenses_details = []
Expenses_amount = []
while True:
    print("___________________")
    print("Budget Tracker App")
    print("1. Add an expense")
    print("2. Check budget details")
    print("3. Check my Balance")
    print("4. Exit")
    choice = input("Choose your action: ")
    print("___________________")
    if choice == '1':
        details = input("Enter item category : ")
        Expenses_details.append(details)
        amount = float(int(input("Enter expenses amount : RM")))
        Expenses_amount.append(amount)
    elif choice == '2':
        Sum = 0
        print("Item Categories | Amount")
        for i in range(len(Expenses_details)):
            print(Expenses_details[i], "|","RM",Expenses_amount[i])
        for j in Expenses_amount:
            Sum += j
        print("Total expenses : RM",Sum)
    elif choice == '3':
        Sum = 0
        for j in Expenses_amount:
            Sum += j
        Total = user_budget - Sum
        print("Your Balance : RM", Total)
    elif choice == '4':
        print('Thank you for using our App!')
        break
    else:
        print("Invalid Choice, Please Try Again")
