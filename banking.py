balance = 10000
choice =int( input("do you want to credit or debit?\n1 for credit and 2 for debit 3 for loan "))
if choice == 1 :
    amount = int(input("enter amount "))
    balance += amount 
    print("balance =",balance)
elif choice == 2:
    amount = int(input("enter amount "))
    if balance - amount  < 0 :
        print ("you lack ", amount - balance)
        choice = int(input("not enough funds would you like to take a loan?\n1 yes and 2 no" ))
        if choice == 1 :
           loan = int(input("amount for loan = "))
           balance += loan
           print(balance)
           choice =input("do you still want to debit?\n 1 yes 2 no")
           if choice == 1 :
               input(int(amount))
               if amount < balance :
                   print("amount withdrawn")
               else :
                   print ("not enough funds")   
         
           



