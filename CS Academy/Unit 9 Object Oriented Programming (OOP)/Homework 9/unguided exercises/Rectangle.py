from cmu_cpcs_utils import testFunction

class Rectangle:
    def __init__(self, left, top, width, height):
        self.left=left
        self.top=top
        self.width=width
        self.height=height
    
    def getArea(self):
        return self.width*self.height
        
    def getRight(self):
        return self.left+self.width
        
    def getBottom(self):
        return self.top+self.height
        
    def isSquare(self):
        return self.width==self.height

    def intersect(self, other):
        newLeft=max(self.left, other.left)
        newTop=max(self.top, other.top)
        newWidth=min(self.getRight(), other.getRight())-newLeft
        newHeight=min(self.getBottom(), other.getBottom())-newTop
        return Rectangle(newLeft, newTop, newWidth, newHeight)
        
@testFunction
def testRectangleClass():
    rect1 = Rectangle(10, 20, 30, 40)
    assert(rect1.left == 10)
    assert(rect1.top == 20)
    assert(rect1.width == 30)
    assert(rect1.height == 40)
    assert(rect1.getArea() == 1200) # width * height
    assert(rect1.getRight() == 40) # left + width
    assert(rect1.getBottom() == 60) # top + height
    assert(rect1.isSquare() == False)

    rect2 = Rectangle(30, 40, 50, 50)
    assert(rect2.left == 30)
    assert(rect2.top == 40)
    assert(rect2.width == 50)
    assert(rect2.height == 50)
    assert(rect2.getArea() == 2500) # width * height
    assert(rect2.getRight() == 80) # left + width
    assert(rect2.getBottom() == 90) # top + height
    assert(rect2.isSquare() == True)

    rect3 = rect1.intersect(rect2)
    assert(rect3.left == 30)
    assert(rect3.top == 40)
    assert(rect3.width == 10)
    assert(rect3.height == 20)
    assert(rect3.getArea() == 200) # width * height
    assert(rect3.getRight() == 40) # left + width
    assert(rect3.getBottom() == 60) # top + height
    assert(rect3.isSquare() == False)

def main():
    testRectangleClass()

main()
