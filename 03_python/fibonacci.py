def fibonacci_iterative(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Example usage
n = 10
print(f"Fibonacci number at position {n} (Iterative): {fibonacci_iterative(n)}")
