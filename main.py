def divide(a, b):
    # Added input validation 
    if a == 0:
        raise ValueError("Numerator should not be zero.")
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def main():
    print("---Division---")
    result = divide(0, 2)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
