def largest(arr, n):

	max = arr[0]

	for i in range(1, n):
		if arr[i] > max:
			max = arr[i]
	return max

arr = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    value = int(input("Enter element {}: ".format(i+1)))
    arr.append(value)
Ans = largest(arr, n)
print("Largest in given array ", Ans)
