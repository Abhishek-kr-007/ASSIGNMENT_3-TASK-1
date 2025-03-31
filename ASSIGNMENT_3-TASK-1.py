def factorial(n):
    """Calculate the factorial of a number using a loop."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# User input
sample_number = int(input("Enter a number: "))
result = factorial(sample_number)
print(f"Factorial of {sample_number} is: {result}")
