class Room:
    length=0.00
    breadth=0.00
    def calc_area(self):
        return self.length*self.breadth
    
r1=Room()
r1.length=12.50
r1.breadth=10.25
res=r1.calc_area()
print("The Area of the Room is: "+str(res)+" cm")