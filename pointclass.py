class Point:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")

#before def init
# point1=Point()
# point1.draw()
# point1.move
# point1.x=10
# print(point1.x)

point2=Point(10,20)
print(point2.x)
print(point2.y)