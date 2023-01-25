import math

class Point():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
        
    def __str__(self):
        return f"Point {self.__name__}, x = {self.x}, y = {self.y}"
    

def dist(p1, p2):
    return math.sqrt(math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2))


p1 = Point(0, 0)
p2 = Point(0, 5)

print( p1 == p2 )