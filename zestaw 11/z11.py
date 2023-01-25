import math

class Calculator():
    
    @staticmethod
    def circle_area(radius):
        return math.pi * pow(radius, 2)
    
    @staticmethod
    def rectangle_area(side_1, side_2):
        return side_1 * side_2
    
    @staticmethod
    def triangle_area(base, height):
        return (base * height) / 2
    
    
print(Calculator().triangle_area(2, 6))