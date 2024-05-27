def fibona(n):
    seq = []
    a, b = 0, 1
    while len(seq) < n:
        seq.append(a)
        a, b = b, a + b
    return seq

num = int(input("Enter the number of terms in the Fibonacci sequence: "))

fib_sequence = fibona(num)

print("Fibonacci sequence:")
for x in fib_sequence:
    print(x)
