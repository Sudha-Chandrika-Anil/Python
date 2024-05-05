def _sum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

if __name__ == "__main__":
    arr = []
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        value = int(input("Enter element {}: ".format(i+1)))
        arr.append(value)
        
    ans = _sum(arr)
    print('Sum of the array is', ans)
