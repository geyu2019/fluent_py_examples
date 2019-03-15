
from math import hypot

class Vertor :
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __repr__(self):
        return 'Vector(%r,%r)' % (self.x,self.y)
    def __abs__(self):
        return hypot(self.x,self.y)
    def __bool__(self):
        return hypot(self.x,self.y)
    def __bool__(self):
        return bool(abs(self))
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)
    def __mul__(self,scalar):
        return Vector(self.x * scalar,self.y * scalar)


vertor = Vertor(1,2)
print(vertor.__repr__())
print(dir(vertor))
for i in dir(vertor):
    if i == '__dir__' :
        print(dir(vertor))

a = '%r' % Vertor
print(eval(a))
b=a
print(type(b))