units = int(input("Enter the number of units consumed: "))
total = 0
if units <= 200:
    total = units * 0.50
elif units>200 and units<=400:
    total=(200*0.5)+((units-200)*0.65)
elif units>400 and units<=600:
     total=(400*0.65)+((units-400)*0.80)
elif units>600:
     total=(600*0.80)+((units-600)*1)
if total > 400:
    surcharge = total * 0.15
    total += surcharge
if total < 100:
        total = 100
print("The electricity bill amount is: Rs."+str(total))