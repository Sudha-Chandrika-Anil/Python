class Cat:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    
    def sound(self):
        print("Meow")
    
    def info(self):
        print(f"My name is {self.name} and I am a {self.breed}. ")

class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    
    def sound(self):
        print("Woof")
    
    def info(self):
        print(f"My name is {self.name} and I am a {self.breed}. ")

cat=Cat("Oliver","Munchkin")
dog=Dog("Jaggu","German Sheperd")

for x in (cat,dog):
    x.info()
    x.sound()
