import math

def gcd(a, b):
    return math.gcd(a, b)

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
print("GCD of", num1, "and", num2, "is", gcd(num1, num2))
