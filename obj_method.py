class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def func(self):
        print("My name is "+ self.name )
        print("My age is "+ str(self.age) )


obj=Person("Sudha",22)
obj.func()
obj.age = 23
obj.func()
#del obj
#del obj.age


