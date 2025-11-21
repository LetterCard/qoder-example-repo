#!/usr/bin/env python3
\"\"\"
Example Python script created through Qoder GitHub tools
\"\"\"

def greet(name):
    \"\"\"
    Greet a person by name
    
    Args:
        name (str): The name of the person to greet
        
    Returns:
        str: A greeting message
    \"\"\"
    return f"Hello, {name}! Welcome to the Qoder GitHub example."

def factorial(n):
    \"\"\"
    Calculate the factorial of a number
    
    Args:
        n (int): The number to calculate factorial for
        
    Returns:
        int: The factorial of n
    \"\"\"
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    \"\"\"
    Main function to demonstrate the greet and factorial functions
    \"\"\"
    print(greet("Qoder User"))
    print(f"Factorial of 5 is: {factorial(5)}")
    
if __name__ == "__main__":
    main()