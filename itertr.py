"""t=("red","black","gold")
itr=iter(t)
print(next(itr))
print(next(itr))
print(next(itr))

#iterate through string
str = "banglore"
ir=iter(str)
for x in ir:
    print(x)"""

#iterator in class
class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=10:
            b = self.a
            self.a+=1
            return b
        else:
            raise StopIteration
    
    
obj = MyNumbers()
itrr=iter(obj)
for x in itrr:
    print(x)
