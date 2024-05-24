def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
    print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
select = int(input("Select operations form 1, 2, 3, 4 :"))
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
if select == 1:
    print(x, "+", y, "=",
                    add(x, y)) 
elif select == 2:
    print(x, "-", y, "=",
                    subtract(x, y))
elif select == 3:
    print(x, "*", y, "=",
                    multiply(x, y))
elif select == 4:
    print(x, "/", y, "=",
                    divide(x, y))
else:
    print("Invalid input")