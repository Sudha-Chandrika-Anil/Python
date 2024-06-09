def natural_no_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

n = int(input("Enter a natural number(limit): "))
total = natural_no_sum(n)
print(f"The sum of natural numbers up to {n} is {total}.")