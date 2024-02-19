# Define a custom exception class for division by zero
class DivisionByZeroError(Exception):
    pass

# Function to perform division
def divide_numbers(num1, num2):
    if num2 == 0:
        raise DivisionByZeroError("Error: Division by zero is not allowed")
    return num1 / num2

# Main function
def main():
    try:
        # Get input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform division
        result = divide_numbers(num1, num2)
        print("Result of division:", result)

    except ValueError:
        print("Error: Please enter valid numbers")
    except DivisionByZeroError as e:
        print(e)

if __name__ == "__main__":
    main()
