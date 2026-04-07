from abc import ABC,abstractmethod
class Shape:
    @abstractmethod
    def area(this):
        pass

    

class Circle(Shape):
    def __init__(this,radius):
        
        this.radius=radius
    def area(this):
        return (this.radius*this.radius)*3.14

         

class Square(Shape):
    def __init__(this,width):
       this.width=width
    def area(this):
        return this.width*this.width


class Triangle(Shape):
    def __init__(this,height,base):
        this.height=height
        this.base=base
        
    def area(this):
        return 0.5*this.base*this.height
    
#create an object of similar shape and use these traits
class Pizza(Circle):
    def __init__(this,radius,name):
        super().__init__(radius)
        this.name=name

shapes=[Circle(3),Square(4),Triangle(4,5)]
for i in shapes:
    print(f"{i.area()}cm")

dominos=Pizza(12,"peproni")
print(dominos.area(),dominos.name)