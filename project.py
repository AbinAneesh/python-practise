book =(input("pls enter the name of the book youve borrowed : "))
if book == "Harry potter" :
    serealNumber =int(input("please enter the sereal number of the book youve borrowed : "))
    if serealNumber == 1234567 :
        date =int(input("please enter the date in which you have borrowed this book : "))
        month = input("please enter the month when your borrowing this book")
        if datetime.now()  :
            print ("please return this book by " ,date + 15,"th")
        elif date > 15 :
            print ("please return this book by ")