import math
# length = طول مستطیل 
# width = عرض مستطیل 
class Rectangle :
    def __init__(self , length = 2 , width = 1 ):
        self.lendth = length
        self.width = width

    def getArea(self) :
        area = self.lendth * self.width 
        return area

    def getPerimeter(self):
        perimeter = 2 * ( self.lendth + self.width)
        return perimeter
    
    def setrectangle(self, lenght , width):
        self.lendth = lenght
        self.width = width

lenght =eval (input("enter first num "))
width =eval(input("enter second num "))
rectangle = Rectangle (lenght , width)
print(f"the area of rectangle is {rectangle.getArea()}")
print(f"the perimeter of rectangle is {rectangle.getPerimeter()}")