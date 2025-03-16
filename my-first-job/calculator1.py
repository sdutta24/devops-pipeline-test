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
    if len(sys.argv) != 4:
        print("Usage: python calculator1.py <operation> <num1> <num2>")
        sys.exit(1)

    operation = sys.argv[1].lower()
    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])

    result = calculate(operation, num1, num2)
    print(f"Result: {result}")
