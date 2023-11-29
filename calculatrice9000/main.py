def menu():
    print('\n')
    print("Choice 1: Perform Calculation")
    print("Choice 2: Show history")
    print("Choice 3: Delete history")
    print("Choice 4: Exit")


def calculator():
    history = []

    while True:
        menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            calculation(history)
        elif choice == '2':
            show_history(history)
        elif choice == '3':
            delete_history(history)
        elif choice == '4':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


def calculation(history):
    try:
        number1 = float(input("Enter the first number: "))
        operator = input("Enter the operator (+, -, x, /, %): ")
        number2 = float(input("Enter the second number: "))

        if operator == "+":
            result = number1 + number2
        elif operator == "-":
            result = number1 - number2
        elif operator == "x":
            result = number1 * number2
        elif operator == "/":
            if number2 != 0:
                result = number1 / number2
            else:
                print("Error: Division by zero.")
                return
        elif operator == "%":
            result = number1 % number2
        else:
            print("Error: Invalid operation.")
            return
        
        history.append(f"{number1} {operator} {number2} = {result}")
        print("The result is:", result)

    except ValueError:
        print("Error: Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e:
        print(f"An error occurred: {e}")


def show_history(history):
    print("\nCalculation history:")
    for calc in history:
        print(calc)


def delete_history(history):
    history.clear()
    print("Calculation history has been deleted.")

calculator()