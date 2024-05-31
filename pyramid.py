start=int(10/2)
end=int(10/2 -1)
for i in range(0,5):
    for j in range(0,10):
        if j in range(start,end):
            print("*",end='')
        else:
            print(" ",end="")
    start-=1
    end+=1
    print()