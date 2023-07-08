# Library management software that handles data regrding the books borrowed and their deadlines.
from datetime import datetime
import json
def newBorrow():
    # new book borrow window
    booksBorrowed = []
    currentDate = datetime.now()
    username = input("Enter username: ")
    n = int(input("Enter no of books borrowed: "))
    print("Enter names of the books borrowed: ")
    for i in range(n):
        print(i+1, end="")
        booksBorrowed.append(input(" Name of Book: "))
    dueDate = input("Enter due date: ")
    # update this details into the file for further retrival of data
    file = open("libraryData.txt", "a")
    data = {"username":username, "noOfBooksBorrowed":5, "Books":[i for i in booksBorrowed], "dueDate":dueDate}
    file.write(json.dumps(data)+"\n")
    file.close()

def showReturnStatus():
    # lets set the dueamount to be 3 dollars for each day delayed after the due date
    dueAmount = 3 
    print("The list of defaulters: ")
    file = open("libraryData.txt", "r")
    for i in file:
        data = json.loads(i)
        date = data["dueDate"].split("-")
        dueDate = datetime(int(date[0]), int(date[1]), int(date[2]), 0, 0, 0)
        if datetime.now() > dueDate:
            daysLate = (datetime.now() - dueDate).days
            print(data["username"]," delayed by ", daysLate, "dueAmount = ", daysLate*dueAmount)
if __name__ == "__main__":
    # menu
    while True:
        print("Operations\n1.New Borrow\n2.Show return status\n3.Exit\nChoose operation: ")
        choice = int(input())
        if choice == 1:
            newBorrow()
        elif choice == 2:
            showReturnStatus()
        elif choice == 3:
            break
        else:
            print("Invalid Operation")