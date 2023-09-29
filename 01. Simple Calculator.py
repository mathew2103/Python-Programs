print("Welcome to Calculator")
while True:
    x = int(input("Menu:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division \
                  \n5. Exponentiation\n6. Exit\nSelect the operation you want to carry out: "))
    if x == 6:
        break
        
    a = int(input("Enter first operand: "))
    b = int(input("Enter second operand: "))

    if x == 1:
        print("Sum:",a+b)
    elif x == 2:
        print("Difference:",a-b)
    elif x == 3:
        print("Product:",a*b)
    elif x == 4:
        print("Quotient:",a/b)
    elif x == 5:
        print(a,"^", b, "=", a**b)
    else:
        print("Invalid input")
