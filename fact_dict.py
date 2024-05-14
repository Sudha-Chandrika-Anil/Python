def factorial(n, memo={}):
    # Check if the factorial is already calculated
    if n in memo:
        return memo[n]
    
    # Base case for factorial of 0 and 1
    if n == 0 or n == 1:
        memo[n] = 1
        return 1
    
    # Calculate factorial recursively and store it in the dictionary
    result = n * factorial(n - 1, memo)
    memo[n] = result
    return result

factorial_cache = {}
number = int(input("Enter a number"))
print(f"Factorial of {number} is {factorial(number, factorial_cache)}")
print(f"Factorial cache: {factorial_cache}")
