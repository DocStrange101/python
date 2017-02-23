class circle:

    def __init__(self,radius):
        self.radius = radius

    def circlearea(self):
        return 3.14*self.radius*self.radius

    def circumfrance(self):
        return 6.28*self.radius

c1 = circle(10)
print c1.circlearea()
print c1.circumfrance()
