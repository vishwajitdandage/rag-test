def divide(a, b):
    # PR Change: Added input validation but buggy logic
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    if a == 0:
        raise ValueError("Numerator should not be zero.")  # <-- Bug introduced
    return a / b

def main():
    print("---Division---")
    result = divide(0, 2)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
