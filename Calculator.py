



#calculator

while True:
    print("\n--- simple calculator ---")

    print()


# take operator
    op = input("Enter operator (+,-,/,*): ")

    # quit when user type "q"
    if op.lower() == "q":
        print("Calculator exited. Goodbye!🤗 ")
        break

# take first number
    num1 = float(input("Enter the first Number: "))

# take second number
    num2 = float(input("Enter the second Number: "))



# operation
    if op == "+":
        result = num1 + num2
        print("result:", round(result, 6))
    elif op == "-":
        result = num1 - num2
        print("result:", round(result, 6))
    elif op == "*":
        result = num1 * num2
        print("result:", round(result, 6))
    elif op == "/":
        if num2 != 0:
            result = num1 / num2
            print("result:", round(result, 6))
        else:
            print("can not divide by zero")
    else:
        print("invalid operator. Please use (+,-,*,/)")









