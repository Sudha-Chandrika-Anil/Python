def dec_to_bin(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return dec_to_bin(n // 2) + str(n % 2)


num = int(input("Enter a decimal number: "))


binary = dec_to_bin(num)


print(f"The binary representation of {num} is: {binary}")
