pinNumber = int(input("please enter your pin number : "))
if pinNumber == 1111 :
    name = input("please enter your full name : ")
    if name == "Abin Aneesh" :
        balance = 10000
        choice=int(input("would you like to withdraw,credit or loan?\n 1 for whitdrawal 2 for credit and 3 for loan "))
        if choice == 1 :
           amount=int(input("please input amount of money to withdraw :"))
           if amount < balance :
               print ("withdrawal succesful new balance", balance - amount)
           else :
               print("insufficant funds! your balance is", balance )    
        elif choice == 2 :
            amount = int(input("please input the amount of money you would like to credit"))
            newbalance = balance + amount
            loan =int(input("how much would you like to loan?")) 
            if loan > 3*balance :
                print ("you are loaning too much") 
            else :
                newbalance = balance + loan
                print ("loan succesfull! your new balance is =",newbalance)    
        
elif pinNumber == 2222 :
    name = input("please enter your full name : ")
    if name == "Nathania Aneesh" :
        balance = 5000
        choice=int(input("would you like to withdraw,credit or loan?\n 1 for whitdrawal 2 for credit and 3 for loan "))
        if choice == 1 :
           amount=int(input("please input amount of money to withdraw :"))
           if amount < balance :
               print ("withdrawal succesful new balance", balance - amount)
           else :
               print("insufficant funds! your balance is", balance )
        elif choice == 2 :
            amount = int(input("please input the amount of money you would like to credit"))
            newbalance = balance + amount
            print("new balance = ",newbalance)
        elif choice == 3 :
            loan =int(input("how much would you like to loan?")) 
            if loan > 3*balance :
                print ("you are loaning too much") 
            else :
                newbalance = balance + loan
                print ("loan succesfull! your new balance is =",newbalance)        
elif pinNumber == 3333 :
    name = input("please enter your full name : ")
    if name == "Bill Gates" :
        balance = 500000000000
        choice=int(input("would you like to withdraw,credit or loan?\n 1 for whitdrawal 2 for credit and 3 for loan "))
        if choice == 1 :
           amount=int(input("please input amount of money to withdraw :"))
           if amount < balance :
               print ("withdrawal succesful new balance", balance - amount)
           else :
               print("insufficant funds! your balance is", balance )
        elif choice == 2 :
            amount = int(input("please input the amount of money you would like to credit"))
            newbalance = balance + amount
            print("new balance = ",newbalance)
        elif choice == 3 :
            loan =int(input("how much would you like to loan?")) 
            if loan > 3*balance :
                print ("you are loaning too much") 
            else :
                newbalance = balance + loan
                print ("loan succesfull! your new balance is =",newbalance)         
else :
    print ("sorry,pin not recognised...you do not have an account here")