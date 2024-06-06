n = int(input("Enter the no.of terms: "))
#using lambda function to calculate the powers of 2
#the map function applies lambda function to each numbers in the range 0 to n-1 and then it's converted to a list
pow_of_2 = list(map(lambda x: 2 ** x,range(n)))
print(f"Powers of 2 upto {n-1} are: {pow_of_2}")
