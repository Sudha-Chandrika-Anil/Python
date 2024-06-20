num = int(input("Enter the number: "))
num1 = num
reversed_sum = 0

while num != 0:
    count = num % 10
    reversed_sum = reversed_sum * 10 + count
    num = num // 10

num1 = num1 + reversed_sum

if str(num1) == str(num1)[::-1]:
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")