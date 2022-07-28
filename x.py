from cmath import sin
from math import pi
import turtle

class circle_funtions():
    
    def __init__(self,radius,angle):
        self.radius = radius
        self.angle = angle
        
    def circumference(self):
        circun = 2*pi*self.radius
        print("The perimeter of the circumference is: ",circun)
        t = turtle.Turtle()
        t.circle(self.radius)
    def area(self):
        area = pi*self.radius**2
        print("The Area of the circunference is: ",area)
        t = turtle.Turtle()
        t.circle(self.radius)
    def arclenght(self):
        arc = 2*pi*self.radius*(self.angle/180)
        print("The lenght of the arc is: ",arc)
        t = turtle.Turtle()
        t.circle(self.radius)
    def sectorperimeter(self):
        sectorperimeter = (2*pi*self.radius*(self.angle/360)) + 2*self.radius
        print("The Perimeter of the sector is: ",sectorperimeter)
        t = turtle.Turtle()
        t.circle(self.radius)
    def sectorarea(self,):
        sectorarea = pi*(self.radius**2)*self.angle/360
        print("The area of the sector is: ",sectorarea)
        t = turtle.Turtle()
        t.circle(self.radius)
    def chordlength(self):
        chordlength = 2*self.radius*sin(self.angle/2)
        print("the lenght of the chord is: ",chordlength)
        t = turtle.Turtle()
        t.circle(self.radius)
    def segmentperimeter(self):
        segmentperimeter = 2*pi*self.radius*(self.angle/360) + 2*self.radius*sin(self.angle/2)
        print("The perimeter of Segment is: ",segmentperimeter)
        t = turtle.Turtle()
        t.circle(self.radius)
    def areasegment(self):
        areasegment = (self.radius**2)*(pi*(self.angle/360) - (sin(self.angle))/2)
        t = turtle.Turtle()
        print("The area of the segments is ",areasegment)
        t.circle(self.radius)



p1 = circle_funtions(10,50)

p1.areasegment()
