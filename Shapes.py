class Shape:
    def __init__(this,color,is_filled):
        this.color=color
        this.is_filled=is_filled
    def describe(this):
        print(f"It is a {this.color} filled {this.is_filled} ")

    

class Circle(Shape):
    def __init__(this,color,is_filled,radius):
        super().__init__(color,is_filled)
        this.radius=radius
    def describe(this):
        print(f"It is a {this.color} filled {this.is_filled} ")

         

class Square(Shape):
    def __init__(this,color,is_filled,width):
       super().__init__(color,is_filled)
       this.width=width
       this.area=width*width
    def describe(this):
        print(f"It is a {this.color} filled {this.area} ")


class Triangl(Shape):
    def __init__(this,color,is_filled,height):
        super().__init__(color,is_filled)
        this.height=height
        this.area=height*height
    def describe(this):
        super().describe()
        print(f"It is a {this.color} filled {this.area} ")



gola=Circle("Red",True,45)
box=Square("Black",True,15)
print(gola.radius)
print(box.width)
box.describe()