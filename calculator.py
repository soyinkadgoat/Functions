def Add(First, Second):
    addition = First + Second
    return "The addition of", str(First), "and", str(Second), "is", str(addition)

def Subtract(First, Second):
    subtraction = First - Second
    return "The subtraction of", str(First), "and", str(Second), "is", str(subtraction)

def Multiply(First, Second):
    multiplication = First * Second
    return "The multiplication of", str(First), "and", str(Second), "is", str(multiplication)

def Divide(First, Second):
    division = First/Second
    return "The division of", str(First), "and", str(Second), "is", str(division)

choice = input("A: Add, B: Subtract, C: Multiply, D: Divide\nEnter your choice: ")
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

if choice.lower() == 'a':
    print(Add(num1, num2))
elif choice.lower() == 'b':
    print(Subtract(num1, num2))
elif choice.lower() == 'c':
    print(Multiply(num1, num2))
else:
    print(Divide(num1, num2))