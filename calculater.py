#calculater
# Menu-driven program to perform basic arithmetic operations
while True:
    # Displaying the menu
        print("Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
    
    # Taking user input
        choice = input("Enter your choice (1/2/3/4/5): ")

    # Check the user's choice and perform the corresponding operation
        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("sum of the numbers:", num1 + num2)

        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("difference of the numbers:", num1 - num2)

        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("product of the numbers:", num1 * num2)

        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num2 != 0:
                print("quotient of the division:", num1 / num2)
            else:
                print("Error: Division by zero is not allowed.")

        elif choice == '5':
            print("Exiting the program...")
            break  # Exit the loop and terminate the program

        else:
            print("Invalid choice, please try again.")
    