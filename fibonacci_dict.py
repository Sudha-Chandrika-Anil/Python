def fibonacci(n, memo={}):
    # Check if the value is already calculated
    if n in memo:
        return memo[n]

    # Base cases for the Fibonacci sequence
    if n == 0:
        memo[n] = 0
        return 0
    elif n == 1:
        memo[n] = 1
        return 1

    # Recursive calculation and storing the result in the dictionary
    result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    memo[n] = result
    return result

fibonacci_cache = {}
number = int(input("Enter a number"))

# Generate the Fibonacci sequence up to 'number'
for i in range(number + 1):
    print(f"Fibonacci({i}) = {fibonacci(i, fibonacci_cache)}")

print(f"Fibonacci cache: {fibonacci_cache}")
