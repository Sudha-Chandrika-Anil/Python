n=int(input("Enter the number: "))
fact=1
while n>1:
    fact*=n
    n-=1

print("The factorial of ",n," is:",fact)
