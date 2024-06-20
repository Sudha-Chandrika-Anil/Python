count = 0
sum = 0
for num in range(101, 200):
    if num % 7 == 0:
        count += 1
        sum+= num
print("Number of integers divisible by 7 :"+str(count))
print("Sum of integers divisible by 7 :"+str(sum))