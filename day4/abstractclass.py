# Create an abstract class Shape that defines:
 
# An abstract method area() (no implementation).
# Create two child classes that inherit from Shape:
# Rectangle → has attributes length, breadth, and implements area().
# Circle → has attribute radius, and implements area().
# Task:
# Define the abstract class Shape using the abc module.
# Implement Rectangle and Circle classes by providing their own version of area().
# Create one object of Rectangle and one of Circle, then display their areas.
 
# from abc import ABC, abstractmethod
 
# # Abstract class
# class Shape(ABC):
 
#     @abstractmethod           # Abstract method
#     def area(self):
#         pass   

class Shape():
    # @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*(self.radius**2)
rect1=Rectangle(5,4)
res1=rect1.area()
print("area of rectangle:",res1)
cir1=Circle(5)
res2=cir1.area()
print("area of circle:",res2)