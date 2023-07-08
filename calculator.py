def add(x, y):
    return x+y


def sub(x, y):
    return x-y


def mul(x, y):
    return x*y


def div(x, y):
    return x/y

while True:
    print("""Operations
        1)add
        2)subtract
        3)multiply
        4)Divide
        5)Exit""")
    operation = int(input("Enter operation: "))
    if operation == 5:
        break
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    z = 0
    if operation == 1:
        z = add(x, y)
    elif operation == 2:
        z = sub(x, y)
    elif operation == 3:
        z = mul(x, y)
    elif operation == 4:
        z = div(x, y)
    else:
        print("Invalid operation")
    print(z)