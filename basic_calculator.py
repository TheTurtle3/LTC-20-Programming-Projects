def add(x, y):
    ans = x + y
    print(str(x) + " + " + str(y) + " = " + str(ans) + "\n")

def sub(x, y):
    ans = x - y
    print(str(x) + " - " + str(y) + " = " + str(ans)  + "\n")

def mul(x, y):
    ans = x * y
    print(str(x) + " * " + str(y) + " = " + str(ans)  + "\n")

def div(x, y):
    ans = x / y
    print(str(x) + " / " + str(y) + " = " + str(ans)  + "\n")

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("iput your choice: ")

    if choice == 'a' or choice == 'A':
        print("Addition")
        x = int(input("Enter your first number: "))
        y = int(input("Enter your second number: "))
        add(x, y)
    elif choice == 'b' or choice == 'B':
        print("Subtraction")
        x = int(input("Enter your first number: "))
        y = int(input("Enter your second number: "))
        sub(x, y)
    elif choice == 'c' or choice == 'C':
        print("Multiplication")
        x = int(input("Enter your first number: "))
        y = int(input("Enter your second number: "))
        mul(x, y)
    elif choice == 'd' or choice == 'D':
        print("Division")
        x = int(input("Enter your first number: "))
        y = int(input("Enter your second number: "))
        div(x, y)
    elif choice == 'e' or choice == 'E':
        print("Program has ended")
        quit()