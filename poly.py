class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Move!")
        

class Car(Vehicle):
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def move(self):
        print("Drive")

class Boat(Vehicle):
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def move(self):
        print("Sail")

class Plane(Vehicle):
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Fly")

car1=Car("xyz","abc")
boat1=Boat("qwe","asdf")
plane1=Plane("yui","bnm")

for x in(car1,plane1,boat1):
    x.move()
        
