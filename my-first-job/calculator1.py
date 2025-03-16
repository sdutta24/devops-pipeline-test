import sys

def calculate(operation, num1, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2
    else:
        return "Invalid operation"

if __name__ == "__main__":
    # Check if arguments are provided
    if len(sys.argv) == 4:
        operation = sys.argv[1].lower()
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])
    else:
        # Default values for non-interactive environments (like Jenkins)
        operation = "add"
        num1 = 10
        num2 = 5

    result = calculate(operation, num1, num2)
    print(f"Operation: {operation}, Numbers: {num1}, {num2}, Result: {result}")
